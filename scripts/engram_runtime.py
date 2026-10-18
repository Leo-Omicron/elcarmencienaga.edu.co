"""Mantenimiento acotado de un almacén Engram existente (sin inicialización)."""
import argparse
from contextlib import closing
import json
import os
from pathlib import Path
import sqlite3
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.request


class RuntimeFailure(Exception):
    pass


def existing_store(directory):
    data = Path(directory).resolve()
    if not (data / "engram.db").is_file():
        raise RuntimeFailure("existing engram.db required")
    return data


def read_database(path):
    # mode=ro is essential: sqlite3.connect's default silently creates databases.
    return sqlite3.connect(path.resolve().as_uri() + "?mode=ro", uri=True, timeout=2)


def verify(path):
    if not path.is_file():
        raise RuntimeFailure("existing backup required")
    with closing(read_database(path)) as conn:
        if conn.execute("PRAGMA quick_check").fetchall() != [("ok",)]:
            raise RuntimeFailure("SQLite validation failed")
        counts = {table: conn.execute(f'SELECT COUNT(*) FROM "{table}"').fetchone()[0]
                  for table in ("observations", "sessions", "user_prompts")}
    return {"path": str(path), "counts": counts}


def backup(data):
    directory = data / "backups"
    directory.mkdir(exist_ok=True)
    fd, name = tempfile.mkstemp(prefix="engram-", suffix=".partial", dir=directory)
    os.close(fd)
    path = Path(name)
    deadline = time.monotonic() + 10

    def progress(*_):
        if time.monotonic() >= deadline:
            raise RuntimeFailure("backup deadline exceeded")

    # SQLite's backup API includes committed WAL data; never copy the live file.
    with closing(read_database(data / "engram.db")) as source:
        with closing(sqlite3.connect(path, timeout=2)) as target:
            source.backup(target, pages=128, progress=progress, sleep=0.05)
    report = verify(path)
    final = path.with_suffix(".db")
    path.rename(final)
    report["path"] = str(final)
    return report


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):
        return None


def identity(data):
    path = data / ".instance-id"
    if not path.is_file():
        raise RuntimeFailure("existing .instance-id required")
    value = path.read_text(encoding="utf-8").strip()
    if not value:
        raise RuntimeFailure("existing .instance-id required")
    return value


def healthy(expected):
    # No proxies, redirects or caller-supplied URLs: only the native local port.
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}), NoRedirect())
    try:
        with opener.open("http://127.0.0.1:7437/health", timeout=3) as response:
            value = json.loads(response.read(4097))
        if not isinstance(value, dict) or value.get("instance_id") != expected:
            raise RuntimeFailure("server identity unavailable or different")
        return True
    except urllib.error.URLError as exc:
        if isinstance(exc.reason, ConnectionRefusedError):
            return False
        raise RuntimeFailure("server identity unavailable or different") from None
    except (ValueError, OSError):
        raise RuntimeFailure("server identity unavailable or different") from None


def serve(data, executable, expected):
    if healthy(expected):
        return
    backup(data)
    temporary = data / "runtime-tmp"
    temporary.mkdir(exist_ok=True)
    env = dict(os.environ, ENGRAM_DATA_DIR=str(data), TEMP=str(temporary),
               TMP=str(temporary), ENGRAM_CLOUD_AUTOSYNC="0")
    # Keep native Pi ownership checks: never set ENGRAM_URL.
    options = ({"creationflags": subprocess.DETACHED_PROCESS | subprocess.CREATE_NEW_PROCESS_GROUP}
               if os.name == "nt" else {"start_new_session": True})
    subprocess.Popen([executable, "serve"], env=env, stdin=subprocess.DEVNULL,
                     stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                     close_fds=True, **options)
    deadline = time.monotonic() + 8
    while time.monotonic() < deadline:
        if healthy(expected):
            return
        time.sleep(0.2)
    raise RuntimeFailure("startup deadline exceeded; no process stopped")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    descriptions = {"serve": "Arrancar si falta; respaldar antes, sin detener procesos",
                    "check": "Verificar identidad HTTP sin escribir",
                    "backup": "Respaldar con SQLite y validar integridad y conteos",
                    "verify-backup": "Validar respaldo sin restaurar ni sobrescribir"}
    for name, description in descriptions.items():
        sub = commands.add_parser(name, help=description, description=description)
        sub.add_argument("--data-dir", required=True, help="Almacén existente; nunca se crea")
        if name == "serve":
            sub.add_argument("--engram", required=True, help="Ejecutable Engram ya instalado")
        if name == "verify-backup":
            sub.add_argument("backup", type=Path, help="Archivo SQLite existente")
    args = parser.parse_args()
    try:
        data = existing_store(args.data_dir)
        if args.command == "backup":
            report = backup(data)
        elif args.command == "verify-backup":
            report = verify(args.backup.resolve())
        else:
            expected = identity(data)
            if args.command == "serve":
                serve(data, args.engram, expected)
            elif not healthy(expected):
                raise RuntimeFailure("server not running")
            report = {"status": "ready"}
        print(json.dumps(report, sort_keys=True))
        return 0
    except (RuntimeFailure, sqlite3.Error, OSError, UnicodeError) as exc:
        # Do not expose database rows, executable output, paths or credentials.
        message = str(exc) if isinstance(exc, RuntimeFailure) else (
            "SQLite validation failed" if isinstance(exc, sqlite3.Error) else "runtime I/O failed")
        print("error: " + message, file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
