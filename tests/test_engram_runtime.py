"""Public CLI tests; all state and transport doubles live in system temp."""
from contextlib import closing
import json
import os
from pathlib import Path
import sqlite3
import subprocess
import sys
import tempfile
import unittest


CLI = Path(__file__).resolve().parents[1] / "scripts" / "engram_runtime.py"

# Inject doubles in the CLI interpreter, never contact the real port/store.
TRANSPORT = '''
import io, json, os, subprocess, time, urllib.request
from urllib.error import URLError
from pathlib import Path
state = Path(os.environ["TEST_STATE"])
def urlopen(*args, **kwargs):
    mode = os.environ["TEST_HEALTH"]
    if mode == "windows-startup" and not state.exists():
        raise URLError(TimeoutError() if kwargs.get("timeout", 0) < 2 else ConnectionRefusedError())
    if mode in ("offline", "neverready") or (mode == "startup" and not state.exists()):
        raise URLError(ConnectionRefusedError())
    if mode == "unverifiable":
        raise URLError(TimeoutError())
    if mode == "malformed":
        return io.BytesIO(b"not json")
    if mode == "missing-id":
        return io.BytesIO(b"{}")
    return io.BytesIO(json.dumps({"instance_id": "foreign" if mode == "foreign" else "fixture-id"}).encode())
def launch(args, **kwargs):
    state.write_text(json.dumps({"args": args, "env": {k: kwargs["env"].get(k) for k in
        ("ENGRAM_DATA_DIR", "TEMP", "TMP", "ENGRAM_CLOUD_AUTOSYNC")},
        "stdio": all(kwargs[k] == subprocess.DEVNULL for k in ("stdin", "stdout", "stderr")),
        "detached": bool(kwargs.get("creationflags") or kwargs.get("start_new_session")),
        "backups": len(list(Path(kwargs["env"]["ENGRAM_DATA_DIR"]).glob("backups/*.db")))}))
    return object()
class Opener:
    open = staticmethod(urlopen)
urllib.request.build_opener = lambda *args: Opener()
subprocess.Popen = launch
if os.environ["TEST_HEALTH"] == "neverready":
    ticks = iter(range(1000))
    time.monotonic = lambda: next(ticks)
    time.sleep = lambda seconds: None
'''


class RuntimeTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.data = self.root / "store"
        self.data.mkdir()
        self.db = self.data / "engram.db"
        with closing(sqlite3.connect(self.db)) as conn:
            for table in ("observations", "sessions", "user_prompts"):
                conn.execute(f"CREATE TABLE {table} (id INTEGER PRIMARY KEY, value TEXT)")
                conn.execute(f"INSERT INTO {table}(value) VALUES ('private-content')")
            conn.commit()
        (self.data / ".instance-id").write_text("fixture-id\n")
        (self.root / "sitecustomize.py").write_text(TRANSPORT)
        self.state = self.root / "child.json"
        self.env = dict(os.environ, PYTHONPATH=str(self.root), TEST_STATE=str(self.state),
                        TEST_HEALTH="offline", PYTHONDONTWRITEBYTECODE="1")

    def run_cli(self, *args, health="offline"):
        result = subprocess.run([sys.executable, str(CLI), *args],
                                env=dict(self.env, TEST_HEALTH=health),
                                capture_output=True, text=True, timeout=5)
        return result.returncode, result.stdout, result.stderr

    def call(self, command, *args, health="offline"):
        return self.run_cli(command, "--data-dir", str(self.data), *args, health=health)

    def snapshot(self):
        return {str(p.relative_to(self.data)): p.read_bytes()
                for p in self.data.rglob("*") if p.is_file()}

    def test_missing_store_never_initializes(self):
        missing = self.root / "absent"
        for command in ("check", "backup", "verify-backup", "serve"):
            extra = [str(self.db)] if command == "verify-backup" else []
            if command == "serve":
                extra = ["--engram", "fixture-engram"]
            self.assertEqual(self.run_cli(command, "--data-dir", str(missing), *extra),
                             (1, "", "error: existing engram.db required\n"))
            self.assertFalse(missing.exists())

    def test_missing_database_in_existing_directory(self):
        empty = self.root / "empty"
        empty.mkdir()
        self.assertEqual(self.run_cli("backup", "--data-dir", str(empty)),
                         (1, "", "error: existing engram.db required\n"))
        self.assertEqual(list(empty.iterdir()), [])

    def test_backup_and_verify_preserve_source(self):
        before = self.db.read_bytes()
        paths = []
        for _ in range(2):
            rc, out, err = self.call("backup")
            self.assertEqual((rc, err), (0, ""))
            report = json.loads(out)
            path = Path(report["path"])
            paths.append(path)
            expected = {"path": str(path), "counts": dict(observations=1, sessions=1, user_prompts=1)}
            self.assertEqual(out, json.dumps(expected, sort_keys=True) + "\n")
            self.assertEqual(path.parent, self.data / "backups")
            self.assertEqual(self.call("verify-backup", str(path)), (0, out, ""))
        self.assertNotEqual(*paths)
        self.assertEqual(self.db.read_bytes(), before)
        self.assertNotIn("private-content", out)

    def test_rejects_bad_backup_without_live_changes(self):
        bad = self.root / "bad.db"
        bad.write_bytes(b"not sqlite")
        before = self.snapshot()
        self.assertEqual(self.call("verify-backup", str(bad)),
                         (1, "", "error: SQLite validation failed\n"))
        self.assertEqual(self.snapshot(), before)
        absent = self.root / "absent.db"
        self.assertEqual(self.call("verify-backup", str(absent)),
                         (1, "", "error: existing backup required\n"))
        self.assertFalse(absent.exists())

    def test_foreign_and_unverifiable_servers_leave_store_unchanged(self):
        for health in ("foreign", "unverifiable", "malformed", "missing-id"):
            for command in ("check", "serve"):
                before = self.snapshot()
                args = ["--engram", "fixture-engram"] if command == "serve" else []
                self.assertEqual(self.call(command, *args, health=health),
                                 (1, "", "error: server identity unavailable or different\n"))
                self.assertEqual(self.snapshot(), before)
                self.assertFalse(self.state.exists())

    def test_check_and_idempotent_serve(self):
        before = self.snapshot()
        for command, args in (("check", []), ("serve", ["--engram", "fixture-engram"])):
            self.assertEqual(self.call(command, *args, health="same"),
                             (0, '{"status": "ready"}\n', ""))
            self.assertEqual(self.snapshot(), before)
        self.assertFalse(self.state.exists())

    def test_startup_environment_and_backup_before_launch(self):
        self.env["ENGRAM_CLOUD_AUTOSYNC"] = "1"
        self.assertEqual(self.call("serve", "--engram", "fixture-engram", health="startup"),
                         (0, '{"status": "ready"}\n', ""))
        child = json.loads(self.state.read_text())
        self.assertEqual(child["args"], ["fixture-engram", "serve"])
        self.assertEqual(child["env"], {"ENGRAM_DATA_DIR": str(self.data),
                         "TEMP": str(self.data / "runtime-tmp"),
                         "TMP": str(self.data / "runtime-tmp"), "ENGRAM_CLOUD_AUTOSYNC": "0"})
        self.assertTrue(child["stdio"])
        self.assertTrue(child["detached"])
        self.assertEqual(child["backups"], 1)
        self.assertTrue((self.data / "runtime-tmp").is_dir())

    def test_missing_identity_and_offline_check_are_read_only(self):
        before = self.snapshot()
        self.assertEqual(self.call("check"), (1, "", "error: server not running\n"))
        self.assertEqual(self.snapshot(), before)
        # A directory fixture without identity must never be assigned a new identity.
        other = self.root / "no-identity"
        other.mkdir()
        with closing(sqlite3.connect(other / "engram.db")) as conn:
            conn.execute("CREATE TABLE untouched(id)")
            conn.commit()
        self.assertEqual(self.run_cli("serve", "--data-dir", str(other), "--engram", "fixture"),
                         (1, "", "error: existing .instance-id required\n"))
        self.assertEqual([p.name for p in other.iterdir()], ["engram.db"])

    def test_windows_refusal_needs_sufficient_connect_deadline(self):
        self.assertEqual(self.call("serve", "--engram", "fixture-engram", health="windows-startup"),
                         (0, '{"status": "ready"}\n', ""))
        self.assertTrue(self.state.exists())

    def test_startup_has_finite_deadline(self):
        self.assertEqual(self.call("serve", "--engram", "fixture-engram", health="neverready"),
                         (1, "", "error: startup deadline exceeded; no process stopped\n"))
        self.assertTrue(self.state.exists())

    def test_backup_includes_committed_wal(self):
        with closing(sqlite3.connect(self.db)) as writer:
            writer.execute("PRAGMA journal_mode=WAL")
            writer.execute("INSERT INTO observations(value) VALUES ('new-private-content')")
            writer.commit()
            rc, out, err = self.call("backup")
            self.assertEqual((rc, err), (0, ""))
            self.assertEqual(json.loads(out)["counts"], dict(observations=2, sessions=1, user_prompts=1))
            self.assertEqual(self.call("verify-backup", json.loads(out)["path"]), (0, out, ""))

    def test_help_and_required_arguments(self):
        rc, out, err = self.run_cli("--help")
        self.assertEqual((rc, err), (0, ""))
        for command in ("serve", "check", "backup", "verify-backup"):
            self.assertIn(command, out)
        rc, out, err = self.run_cli("serve", "--data-dir", str(self.data))
        self.assertEqual((rc, out), (2, ""))
        self.assertIn("--engram", err)


if __name__ == "__main__":
    unittest.main()
