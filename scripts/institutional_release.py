"""Scoped static releases over SFTP, verified backup, health check and rollback.
No credentials are accepted as command-line arguments. DEMOS is never a target.
"""
import argparse
import errno
import hashlib
import io
import json
import os
from pathlib import Path, PurePosixPath
import re
import stat
import time
from urllib.parse import quote
from urllib.request import Request, urlopen

TARGETS = {
    'laboratorio': ('subdomains/lab', 'https://lab.elcarmencienaga.edu.co/'),
    'portal-cultural': ('subdomains/semanacultural', 'https://semanacultural.elcarmencienaga.edu.co/'),
    'portal-principal': ('', 'https://elcarmencienaga.edu.co/'),
}
WEBROOT = 'domains/elcarmencienaga.edu.co/public_html'
EXTENSIONS = {'.html', '.css', '.js', '.json', '.jpg', '.jpeg', '.png', '.webp', '.svg', '.ico', '.pdf', '.txt', '.xml', '.woff', '.woff2'}
TEXT = {'.html', '.css', '.js', '.json', '.txt', '.xml', '.svg'}


def digest(data):
    return hashlib.sha256(data).hexdigest()


def safe_file(value):
    p = PurePosixPath(value)
    if not value or not p.parts or str(p) != value or p.is_absolute() or '\\' in value:
        raise ValueError('Invalid release path')
    if any(x in ('.', '..') or x.startswith('.') or x.startswith('wp-') for x in p.parts):
        raise ValueError('Protected path')
    if p.parts[0] in ('demos', 'subdomains', 'laboratorio', 'semanacultural') or p.suffix.lower() not in EXTENSIONS:
        raise ValueError('Path outside static release scope')
    return value


def load_bundle(folder):
    folder = Path(folder)
    manifest = json.loads((folder / 'manifest.json').read_text())
    if manifest['target'] not in ('portal-cultural', 'portal-principal'):
        raise ValueError('Unknown production target')
    if not re.fullmatch('[a-f0-9]{40}', manifest['commit']):
        raise ValueError('Expected an exact commit')
    if not manifest['files']:
        raise ValueError('Empty release')
    files = {}
    for name, expected in manifest['files'].items():
        safe_file(name)
        p = folder / 'files' / name
        if any(parent.is_symlink() for parent in (p, *p.parents)):
            raise ValueError('Symlink in package')
        data = p.read_bytes()
        if digest(data) != expected:
            raise ValueError('Package checksum mismatch: ' + name)
        files[name] = data
    return manifest, files


def package(repo, output, commit):
    repo, output = Path(repo), Path(output)
    config = json.loads((repo / 'deploy/release.json').read_text())
    if config['target'] not in ('portal-cultural', 'portal-principal'):
        raise ValueError('Unknown target')
    names = config['files']
    if len(names) != len(set(names)):
        raise ValueError('Duplicate release files')
    if output.exists():
        raise ValueError('Output already exists')
    output.mkdir(parents=True)
    manifest = dict(target=config['target'], description=config['description'], commit=commit, files={})
    source = repo / 'laboratorio'
    for name in names:
        safe_file(name)
        p = source / name
        if p.is_symlink() or source.resolve() not in p.resolve().parents:
            raise ValueError('Source escapes laboratorio')
        if any(parent.is_symlink() for parent in p.parents if parent != repo.parent):
            raise ValueError('Symlink source')
        data = p.read_bytes()
        dest = output / 'files' / name
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(data)
        manifest['files'][name] = digest(data)
    (output / 'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2))
    if names:
        load_bundle(output)
    return manifest


class Publisher:
    def __init__(self, sftp, target, release):
        if target not in TARGETS or not re.fullmatch('[A-Za-z0-9_-]{1,100}', release):
            raise ValueError('Invalid target or release ID')
        self.sftp, self.target, self.release = sftp, target, release
        self.home = sftp.normalize('.').rstrip('/')
        suffix, self.url = TARGETS[target]
        self.root = self.home + '/' + WEBROOT + ('/' + suffix if suffix else '')
        self.private = self.home + '/.ieec-releases'
        self.snapshot = self.private + '/' + target + '/' + release
        self.lock = self.private + '/publish.lock'

    def exists(self, path):
        try:
            return self.sftp.lstat(path)
        except OSError as exc:
            if exc.errno == errno.ENOENT:
                return None
            raise

    def safe(self, path, create=False, private=False):
        relative = PurePosixPath(path).relative_to(self.home)
        current = self.home
        for part in relative.parts:
            current += '/' + part
            info = self.exists(current)
            if info and stat.S_ISLNK(info.st_mode):
                raise ValueError('Remote symlink refused')
            if not info and create:
                self.sftp.mkdir(current, mode=0o700 if private else 0o755)
            elif info and not stat.S_ISDIR(info.st_mode):
                raise ValueError('Expected directory')
            elif not info:
                raise FileNotFoundError(current)

    def read(self, path):
        with self.sftp.open(path, 'rb') as f:
            return f.read()

    def write(self, path, data, private=False, mode=0o644):
        self.safe(str(PurePosixPath(path).parent), create=True, private=private)
        info = self.exists(path)
        if info and not stat.S_ISREG(info.st_mode):
            raise ValueError('Non-regular destination')
        temp = path + '.ieec-' + self.release
        if self.exists(temp):
            raise ValueError('Temporary file already exists')
        try:
            with self.sftp.open(temp, 'wx') as f:
                f.write(data)
            self.sftp.chmod(temp, 0o600 if private else mode)
            if digest(self.read(temp)) != digest(data):
                raise ValueError('Upload verification failed')
            self.sftp.posix_rename(temp, path)
        finally:
            if self.exists(temp):
                self.sftp.remove(temp)

    def current(self):
        p = self.private + '/' + self.target + '/current.json'
        return json.loads(self.read(p)) if self.exists(p) else None

    def set_current(self, value):
        self.write(self.private + '/' + self.target + '/current.json', json.dumps(value).encode(), private=True)

    def restore(self, backup, check_current=True):
        if backup['target'] != self.target or backup['root'] != self.root:
            raise ValueError('Backup target mismatch')
        if check_current and self.current() != {'release': self.release}:
            raise ValueError('Only the current release can be rolled back')
        # Read and verify every backup before changing a public file.
        originals = {}
        for name, record in backup['files'].items():
            safe_file(name)
            path = self.root + '/' + name
            self.safe(str(PurePosixPath(path).parent))
            if record['old'] is not None:
                data = self.read(self.snapshot + '/files/' + name)
                if digest(data) != record['old']:
                    raise ValueError('Backup checksum mismatch')
                originals[name] = data
            if check_current:
                info = self.exists(path)
                if not info or not stat.S_ISREG(info.st_mode) or digest(self.read(path)) != record['new']:
                    raise ValueError('Live file changed since deployment; manual review required')
        for name, record in backup['files'].items():
            path = self.root + '/' + name
            if record['old'] is None:
                if self.exists(path):
                    self.sftp.remove(path)
            else:
                self.write(path, originals[name], mode=record['mode'])
        self.set_current(backup['previous'])

    def publish(self, files, health):
        self.safe(self.root)
        if self.exists(self.snapshot):
            raise ValueError('Release ID already used')
        self.safe(self.snapshot, create=True, private=True)
        backup = dict(target=self.target, root=self.root, previous=self.current(), files={})
        # Complete backup and reread it BEFORE the first public write.
        for name, data in files.items():
            safe_file(name)
            dest = self.root + '/' + name
            self.safe(str(PurePosixPath(dest).parent), create=True)
            info = self.exists(dest)
            if info and not stat.S_ISREG(info.st_mode):
                raise ValueError('Protected destination')
            original = self.read(dest) if info else None
            if original is not None:
                self.write(self.snapshot + '/files/' + name, original, private=True)
            backup['files'][name] = dict(old=digest(original) if original is not None else None,
                                         new=digest(data), mode=(info.st_mode & 0o777) if info else 0o644)
        encoded = json.dumps(backup).encode()
        self.write(self.snapshot + '/backup.json', encoded, private=True)
        if self.read(self.snapshot + '/backup.json') != encoded:
            raise ValueError('Backup manifest verification failed')
        try:
            for name, data in files.items():
                self.write(self.root + '/' + name, data, mode=backup['files'][name]['mode'])
            health(self.url, files)
            self.set_current({'release': self.release})
        except Exception:
            self.restore(backup, check_current=False)
            raise
        return backup

    def run(self, operation):
        self.safe(self.private, create=True, private=True)
        self.sftp.mkdir(self.lock, mode=0o700)  # Atomic lock; a stale lock requires investigation.
        try:
            return operation()
        finally:
            self.sftp.rmdir(self.lock)


def health(url, files):
    # Verify text bytes, not merely HTTP 200. Images may be transformed by the CDN.
    for name, expected in files.items():
        error = None
        for attempt in range(3):
            try:
                req = Request(url + quote(name) + '?ieec=' + digest(expected)[:16], headers={'Cache-Control': 'no-cache'})
                with urlopen(req, timeout=30) as response:
                    actual = response.read()
                    if response.status != 200 or not actual:
                        raise ValueError('HTTP verification failed')
                    if Path(name).suffix.lower() in TEXT and digest(actual) != digest(expected):
                        raise ValueError('Published text does not match release: ' + name)
                error = None
                break
            except Exception as exc:
                error = exc
                if attempt < 2:
                    time.sleep(2)
        if error:
            raise error


def connect():
    import paramiko
    client = paramiko.SSHClient()
    client.load_host_keys(os.environ['IEEC_KNOWN_HOSTS_FILE'])
    client.set_missing_host_key_policy(paramiko.RejectPolicy())
    client.connect(os.environ['IEEC_SFTP_HOST'], port=int(os.environ['IEEC_SFTP_PORT']),
                   username=os.environ['IEEC_SFTP_USER'], key_filename=os.environ['IEEC_SFTP_KEY_FILE'],
                   look_for_keys=False, allow_agent=False, timeout=30)
    return client


def validate_protection(environment):
    reviewers = [reviewer for rule in environment.get('protection_rules', [])
                 if rule.get('type') == 'required_reviewers' for reviewer in rule.get('reviewers', [])]
    if not any(x.get('reviewer', {}).get('login') == 'Leo-Omicron' for x in reviewers):
        raise ValueError('Produccion must require approval from Leo-Omicron')
    if environment.get('can_admins_bypass', True):
        raise ValueError('Disable administrator bypass before activation')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('command', choices=['package', 'deploy', 'rollback', 'check-protection'])
    parser.add_argument('--bundle', default='candidate')
    parser.add_argument('--commit')
    parser.add_argument('--target', choices=list(TARGETS))
    parser.add_argument('--release')
    args = parser.parse_args()
    if args.command == 'check-protection':
        repo = os.environ['GITHUB_REPOSITORY']
        if not re.fullmatch('[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', repo):
            raise ValueError('Invalid repository')
        # Public repository metadata: fail closed if unavailable or made private.
        with urlopen(Request('https://api.github.com/repos/' + repo + '/environments/produccion',
                             headers={'Accept': 'application/vnd.github+json'}), timeout=30) as response:
            environment = json.load(response)
        validate_protection(environment)
        print('Production approval gate verified')
        return
    if args.command == 'package':
        m = package('.', args.bundle, args.commit)
        print('Packaged', len(m['files']), 'files; target:', m['target'])
        return
    manifest, files = load_bundle(args.bundle) if args.command == 'deploy' else (None, None)
    if manifest and args.target != 'laboratorio' and args.target != manifest['target']:
        raise ValueError('Production target differs from tested package')
    with connect() as client:
        with client.open_sftp() as sftp:
            pub = Publisher(sftp, args.target, args.release)
            if args.command == 'deploy':
                pub.run(lambda: pub.publish(files, health))
                receipt = dict(release=args.release, commit=manifest['commit'], target=args.target,
                               manifest_sha256=digest(Path(args.bundle, 'manifest.json').read_bytes()))
                Path(args.bundle, 'receipt.json').write_text(json.dumps(receipt))
            else:
                backup = json.loads(pub.read(pub.snapshot + '/backup.json'))
                pub.run(lambda: pub.restore(backup))
    print(args.command, 'completed:', args.target, args.release)


if __name__ == '__main__':
    main()
