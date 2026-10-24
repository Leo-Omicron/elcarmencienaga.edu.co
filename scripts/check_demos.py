"""Validate DEMOS links, markup and gallery behavior. Python 3 + Node.js only."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import subprocess, json
ROOT = Path(__file__).resolve().parents[1]
class Page(HTMLParser):
    def __init__(self, text):
        super().__init__(); self.ids=set(); self.refs=[]; self.scripts=[]; self.photos=[]; self.inline=0
        self.feed(text)
    def handle_starttag(self, tag, attrs):
        a=dict(attrs)
        if 'id' in a:
            assert a['id'] not in self.ids, f"Duplicate id {a['id']}"
            self.ids.add(a['id'])
        if 'style' in a:self.inline+=1
        if tag in ('a','link','script','img','iframe'):
            ref=a.get('href', a.get('src',''))
            if ref:self.refs.append(ref)
        if tag=='script' and a.get('src'):self.scripts.append(a['src'])
        if a.get('onclick','').startswith('openLightbox('):
            self.photos.append(int(a['onclick'].split('(')[1].split(')')[0]))
            assert a.get('role')=='button' and a.get('tabindex')=='0'
pages={p:Page(p.read_text()) for p in (ROOT/'demos').glob('*.html')}
for path,page in pages.items():
    assert not page.inline, path
    assert 'contenido' in page.ids, path
    for ref in page.refs:
        u=urlsplit(ref)
        if u.scheme or u.netloc:continue
        target=(path.parent/unquote(u.path)).resolve() if u.path else path
        assert target.exists(), (path, ref)
        if u.fragment and target.suffix=='.html':
            dest=pages.get(target) or Page(target.read_text())
            assert unquote(u.fragment) in dest.ids, (path,ref)
    for script in page.scripts:
        subprocess.run(['node','--check',str(path.parent/script)],check=True,capture_output=True)
    if path.stem.startswith('dia'):
        script=path.parent/'js'/f'{path.stem}.js'
        harness='''const fs=require('node:fs'), vm=require('node:vm'), assert=require('node:assert/strict');
const elements={};
function element(id){return elements[id]??=(id==='photo-lightbox'?{open:false,showModal(){this.open=true},close(){this.open=false},addEventListener(){}}:{textContent:'',src:'',alt:''})}
const context=vm.createContext({document:{getElementById:element,addEventListener(){}}});
vm.runInContext(fs.readFileSync(SCRIPT,'utf8'),context);
const items=vm.runInContext('galleryItems',context);
assert.equal(items.length,INDICES.length);
for(const i of INDICES){assert(items[i]); vm.runInContext(`openLightbox(${i})`,context); assert.equal(elements['lightbox-img'].src,items[i].file)}
vm.runInContext('openLightbox(0);changeLightbox(-1)',context);assert.equal(elements['lightbox-img'].src,items.at(-1).file);
vm.runInContext('changeLightbox(1)',context);assert.equal(elements['lightbox-img'].src,items[0].file);
vm.runInContext('closeLightbox()',context);assert.equal(elements['photo-lightbox'].open,false);
console.log(JSON.stringify(items.map(x=>x.file)));
'''.replace('SCRIPT',json.dumps(str(script))).replace('INDICES',json.dumps(page.photos))
        result=subprocess.run(['node','-e',harness],check=True,text=True,capture_output=True)
        for image in json.loads(result.stdout):assert (path.parent/image).is_file(),image
        print(path.name, len(page.photos), 'gallery entries: PASS')
print('7 pages: local links, fragments, unique IDs, external styles/scripts, gallery wraparound: PASS')
