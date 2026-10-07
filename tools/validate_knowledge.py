"""Validate the authored architecture, local navigation and current demo evidence."""
import hashlib,json,re,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def read(rel):return json.loads((ROOT/rel).read_text())
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def validate():
    errors=[];checks=[]
    def check(condition,message):
        if not condition:errors.append(message)
        checks.append(message)
    domains=read('architecture/domains.json');concepts=read('architecture/concepts.json');sources=read('evidence/sources.json')
    ids={d['id'] for d in domains};sids={s['id'] for s in sources}
    check(ids=={f'M{i:02d}' for i in range(1,23)},'exact22domainIDs')
    check(len(domains)==len(ids),'uniqueDomainIDs')
    check(len(concepts)==len({c['id'] for c in concepts})==198,'unique198conceptIDs')
    required=['Manifestasi yang ditampilkan','Cakupan dan batas','Fondasi yang membentuk tampilan','Penurunan mekanisme dan contoh terhitung','Kasus produksi','Memilih teknik dan trade-offs','Alur kerja operasional','Verifikasi dan kriteria penguasaan','Cabang spesialis dalam cakupan']
    for d in domains:
        p=ROOT/'knowledge/domains'/f"{d['slug']}.md"
        check(p.is_file(),f"chapterExists:{d['id']}")
        if not p.is_file():continue
        text=p.read_text();check(all('## '+h in text for h in required),f"chapterSections:{d['id']}")
        check(len(re.findall(r'^## '+d['id']+r'\.\d{2} — ',text,re.M))==9,f"nineConceptSections:{d['id']}")
        check(len(text.split())>550,f"substantiveChapter:{d['id']}")
        check(set(d['related'])<=ids,f"relatedIDs:{d['id']}")
        check(set(d['sources'])<=sids,f"sourceIDs:{d['id']}")
        dc=[c for c in concepts if c['domain']==d['id']]
        check({c['id'] for c in dc}=={f"{d['id']}.{i:02d}" for i in range(1,10)},f"conceptCoverage:{d['id']}")
        for c in dc:check((ROOT/c['path']).resolve()==p.resolve() and c['title'] in text,f"conceptPath:{c['id']}")
    graph=read('architecture/relationships.json')
    check(set(graph['nodes'])==ids,'graphNodeCoverage')
    check(all(e['from'] in ids and e['to'] in ids for e in graph['edges']),'graphEdgeValidity')
    reached={'M01'}
    while True:
        expanded=reached|{e['to'] for e in graph['edges'] if e['from'] in reached}|{e['from'] for e in graph['edges'] if e['to'] in reached}
        if expanded==reached:break
        reached=expanded
    check(reached==ids,'graphConnectedUndirected')
    link_count=0
    for p in ROOT.rglob('*.md'):
        text=p.read_text()
        for target in re.findall(r'\]\(([^)]+)\)',text):
            if re.match(r'(https?://|mailto:)',target):continue
            rel,_,anchor=target.partition('#');q=(p.parent/rel).resolve() if rel else p
            check(q.is_relative_to(ROOT),f"linkInsideRepo:{p.relative_to(ROOT)}:{target}")
            check(q.is_file(),f"linkExists:{p.relative_to(ROOT)}:{target}")
            if anchor and q.is_file():
                t=q.read_text();check(f'id="{anchor}"' in t,f"explicitAnchor:{p.relative_to(ROOT)}:{target}")
            link_count+=1
    for p in ROOT.rglob('*.json'):
        try:json.loads(p.read_text())
        except Exception as e:errors.append(f'invalidJSON:{p.name}:{e}')
    rr=read('evidence/render-report.json');mr=read('evidence/media-report.json');nr=read('evidence/numeric-report.json')
    video=ROOT/'examples/rendered/demo.mp4'
    check(digest(video)==rr['mp4_sha256']==mr['sha256'],'videoHashMatchesReports')
    check(digest(ROOT/'examples/demo.json')==rr['config_sha256'],'configHashCurrent')
    for name,h in rr['code_sha256'].items():check(digest(ROOT/'runtime'/name)==h,f'renderCodeHashCurrent:{name}')
    check(mr['status']=='PASS' and mr['frames']==180 and mr['duration_seconds']==6,'executedMediaChecks')
    check(nr['status']=='PASS' and nr['tests_run']==12,'executedNumericChecks')
    check(digest(ROOT/'tests/test_motion.py')==nr['test_code_sha256'],'numericTestHashCurrent')
    check(not any((ROOT/name).exists() for name in ['00_CONTROL','07_RUNTIME_SKILL','08_RELEASES','mirror-manifest','GITHUB_MIRROR_STATUS.md','PROJECT_REPORT_ID.md']),'noLegacyActivePaths')
    files=[p for p in ROOT.rglob('*') if p.is_file() and '__pycache__' not in p.parts]
    report={'status':'PASS' if not errors else 'FAIL','domains':len(domains),'concepts':len(concepts),'source_records':len(sources),'relationship_edges':len(graph['edges']),'local_links_checked':link_count,'checks':len(checks),'markdown_files':len(list(ROOT.rglob('*.md'))),'markdown_words':sum(len(p.read_text().split()) for p in ROOT.rglob('*.md')),'tracked_candidate_files':len(files),'errors':errors,'scope':'Architecture/content sections, indexes, internal paths/anchors, connected domain relationships, JSON, demo/input/report hashes and absence of legacy active paths. Not scientific peer review of every sentence.'}
    return report

if __name__=='__main__':
    report=validate();print(json.dumps(report,ensure_ascii=False,indent=2));sys.exit(0 if report['status']=='PASS' else 1)
