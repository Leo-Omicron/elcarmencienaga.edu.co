import importlib.util
import json
import os
from pathlib import Path
import shutil
import tempfile
import unittest

spec=importlib.util.spec_from_file_location('release',Path(__file__).parents[1]/'scripts/institutional_release.py')
r=importlib.util.module_from_spec(spec);spec.loader.exec_module(r)

class LocalSFTP:
    """SFTP public interface backed by an isolated temporary directory."""
    def __init__(self,home):self.home=str(home);self.fail_backup=False;self.fail_public=False
    def normalize(self,p):return self.home
    def lstat(self,p):return os.lstat(p)
    def mkdir(self,p,mode=0o755):os.mkdir(p,mode)
    def rmdir(self,p):os.rmdir(p)
    def open(self,p,mode):
        if self.fail_backup and '/.ieec-releases/' in p and 'w' in mode:raise IOError('backup disk full')
        if self.fail_public and '/public_html/' in p and 'w' in mode:
            self.fail_public=False;raise IOError('simulated upload failure')
        if mode=='wx':mode='xb'
        return open(p,mode)
    def chmod(self,p,mode):os.chmod(p,mode)
    def posix_rename(self,a,b):os.replace(a,b)
    def remove(self,p):os.remove(p)

class Releases(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
        self.home=Path(self.tmp.name);self.fs=LocalSFTP(self.home)
        self.pub=r.Publisher(self.fs,'laboratorio','release-1')
        self.root=Path(self.pub.root);self.root.mkdir(parents=True)
        (self.root/'index.html').write_bytes(b'old')
    def publish(self,health=lambda *_:None):
        return self.pub.run(lambda:self.pub.publish({'index.html':b'new','new.css':b'css'},health))
    def test_production_gate_requires_owner_and_no_admin_bypass(self):
        good={'protection_rules':[{'type':'required_reviewers','reviewers':[{'reviewer':{'login':'Leo-Omicron'}}]}], 'can_admins_bypass':False}
        r.validate_protection(good)
        for bad in ({},dict(good,can_admins_bypass=True),dict(good,protection_rules=[])):
            with self.assertRaises(ValueError):r.validate_protection(bad)
    def test_rollback_cannot_revert_an_older_release(self):
        backup=self.publish();self.pub.set_current({'release':'newer-release'})
        with self.assertRaises(ValueError):self.pub.restore(backup)
        self.assertEqual((self.root/'index.html').read_bytes(),b'new')
    def test_path_guards(self):
        for p in ('../x.html','/x.html','a//b.html','.htaccess','index.php','wp-config.json','subdomains/lab/index.html','demos/index.html','a/../x.html','x\\y.html'):
            with self.subTest(path=p),self.assertRaises(ValueError):r.safe_file(p)
        self.assertEqual(r.safe_file('dia5/Dia5 (1).jpg'),'dia5/Dia5 (1).jpg')
    def test_demos_is_never_a_target(self):
        with self.assertRaises(ValueError):r.Publisher(self.fs,'demos','r')
    def test_verified_backup_and_rollback(self):
        backup=self.publish()
        self.assertEqual((self.root/'index.html').read_bytes(),b'new')
        self.assertEqual((Path(self.pub.snapshot)/'files/index.html').read_bytes(),b'old')
        self.pub.run(lambda:self.pub.restore(backup))
        self.assertEqual((self.root/'index.html').read_bytes(),b'old')
        self.assertFalse((self.root/'new.css').exists())
    def test_backup_failure_never_overwrites_public_content(self):
        self.fs.fail_backup=True
        with self.assertRaises(IOError):self.publish()
        self.assertEqual((self.root/'index.html').read_bytes(),b'old')
        self.assertFalse((self.root/'new.css').exists())
    def test_upload_failure_restores_previous_version(self):
        self.fs.fail_public=True
        with self.assertRaises(IOError):self.publish()
        self.assertEqual((self.root/'index.html').read_bytes(),b'old')
        self.assertFalse((self.root/'new.css').exists())
    def test_failed_http_verification_rolls_back_new_files(self):
        def fail(*_):raise ValueError('wrong content despite HTTP 200')
        with self.assertRaises(ValueError):self.publish(fail)
        self.assertEqual((self.root/'index.html').read_bytes(),b'old')
        self.assertFalse((self.root/'new.css').exists())
    def test_manual_rollback_refuses_later_human_edit(self):
        backup=self.publish();(self.root/'index.html').write_bytes(b'human edit')
        with self.assertRaises(ValueError):self.pub.run(lambda:self.pub.restore(backup))
        self.assertEqual((self.root/'index.html').read_bytes(),b'human edit')
    def test_corrupt_backup_stops_restore_before_any_public_write(self):
        backup=self.publish();(Path(self.pub.snapshot)/'files/index.html').write_bytes(b'bad')
        with self.assertRaises(ValueError):self.pub.run(lambda:self.pub.restore(backup))
        self.assertEqual((self.root/'index.html').read_bytes(),b'new')
    def test_remote_symlink_is_refused(self):
        (self.root/'index.html').unlink();(self.root/'index.html').symlink_to(self.home/'other')
        with self.assertRaises(ValueError):self.publish()
    def test_simultaneous_publication_is_refused(self):
        self.pub.safe(self.pub.private,True,True);os.mkdir(self.pub.lock)
        with self.assertRaises(FileExistsError):self.publish()
        self.assertEqual((self.root/'index.html').read_bytes(),b'old')
    def test_backup_cannot_be_reused_on_another_target(self):
        backup=self.publish();backup['target']='portal-principal'
        with self.assertRaises(ValueError):self.pub.restore(backup)
    def test_package_hash_tampering_and_source_escape(self):
        repo=self.home/'repo';(repo/'deploy').mkdir(parents=True);(repo/'laboratorio').mkdir()
        (repo/'laboratorio/index.html').write_text('hello')
        (repo/'deploy/release.json').write_text(json.dumps(dict(target='portal-cultural',description='test',files=['index.html'])))
        bundle=self.home/'bundle';r.package(repo,bundle,'a'*40);r.load_bundle(bundle)
        (bundle/'files/index.html').write_text('tampered')
        with self.assertRaises(ValueError):r.load_bundle(bundle)
        (repo/'laboratorio/index.html').unlink();(repo/'laboratorio/index.html').symlink_to(self.root/'index.html')
        with self.assertRaises(ValueError):r.package(repo,self.home/'bundle2','a'*40)

if __name__=='__main__':unittest.main()
