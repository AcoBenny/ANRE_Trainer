"""Prepare exact audit work units; export batches; check result structure, not truth."""
import argparse, collections, csv, hashlib, json, pathlib, subprocess, sys

ROOT=pathlib.Path(__file__).resolve().parents[2]
OUT=pathlib.Path(__file__).resolve().parent/'DEEP_EXECUTION_2026_11_11'
BRANCH='audit/anre-v8-priority-17-20261109'
BLOB='bc5b5a61954ba138cf83987bfc932eca517f3b21'
MASTER=pathlib.Path(__file__).resolve().parent/'V95_ALL_822_MASTER_AFTER_FOCUSED_RECHECKS_AND_SEPARATE_AI_QA.csv'
FIELDS=['Intrebare','A','B','C']
def read_csv(p): return list(csv.DictReader(p.open()))
def write_csv(name,rs):
    with (OUT/name).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rs[0]),lineterminator='\n');w.writeheader();w.writerows(rs)
def load():
    branch=subprocess.check_output(['git','branch','--show-current'],cwd=ROOT,text=True).strip()
    assert branch==BRANCH,('Unexpected branch',branch)
    raw=(ROOT/'app/src/main/assets/anre_trainer.html').read_bytes()
    assert hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==BLOB,'Canonical data drift: stop and reconcile'
    records=json.JSONDecoder().raw_decode(raw.decode().split('const DATA=',1)[1])[0]
    canon={r['ID']:r for r in records};master={r['ID']:r for r in read_csv(MASTER)}
    assert len(canon)==len(records)==822 and set(canon)==set(master)
    return canon,master
def units(canon,master):
    grouped=collections.defaultdict(list)
    for r in canon.values(): grouped[tuple(r[k] for k in FIELDS)].append(r)
    result=[]
    for text,members in grouped.items():
        encoded=json.dumps(text,ensure_ascii=False,separators=(',',':')).encode()
        digest=hashlib.sha256(encoded).hexdigest();ids=sorted(r['ID'] for r in members)
        risk=min(master[id]['risk_current_priority_UNCHANGED'] for id in ids)
        cats={r['Categorie'] for r in members};assert len(cats)==1
        code={'Electrotehnică':'ELE','Norme tehnice':'NOR','Legislație':'LEG'}[next(iter(cats))]
        result.append(dict(unit_id='AU-'+digest[:16],qabc_sha256=digest,category=code,risk=risk,representative_id=ids[0],member_ids=';'.join(ids),key_conflict='YES' if len({r['Raspuns'] for r in members})>1 else 'NO',original_keys_by_id=json.dumps({r['ID']:r['Raspuns'] for r in members},ensure_ascii=False,separators=(',',':')),prior_focus_ids=';'.join(id for id in ids if master[id]['focused_evidence_batches']!='NO_FOCUSED_RECHECK_RECORDED'),prior_independent_AI_review_ids=';'.join(id for id in ids if master[id]['independent_AI_claim_verdicts_NOT_ANSWER_APPROVAL']!='NOT_RUN'),batch_id='',decision='NOT_ADJUDICATED',approved_for_learning='NO'))
    ordered=sorted(result,key=lambda r:(r['category'],r['risk'],r['key_conflict']!='YES',r['representative_id']))
    bycat=collections.Counter()
    for r in ordered:
        i=bycat[r['category']];r['batch_id']=f"DEEP-{r['category']}-{i//20+1:02d}";bycat[r['category']]+=1
    assert len({r['unit_id'] for r in ordered})==len(ordered)==568
    assert collections.Counter(id for r in ordered for id in r['member_ids'].split(';'))==collections.Counter(canon.keys()),'Every canonical ID must be routed exactly once'
    return ordered
def prepare():
    canon,master=load();uu=units(canon,master);OUT.mkdir(exist_ok=True)
    write_csv('UNITS_568.csv',uu)
    batch=[]
    for bid in sorted({u['batch_id'] for u in uu}):
        group=[u for u in uu if u['batch_id']==bid];batch.append(dict(batch_id=bid,category=group[0]['category'],unique_units=len(group),canonical_ids=sum(len(u['member_ids'].split(';')) for u in group),P0_units=sum(u['risk']=='P0' for u in group),key_conflict_units=sum(u['key_conflict']=='YES' for u in group),author_role={'ELE':'Electrical-domain analyst','NOR':'Normative source and edition analyst','LEG':'Legal source and temporal analyst'}[group[0]['category']],reviewer_role='Distinct AI technical/source/linguistic reviewer',status='QUEUED_NOT_EXECUTED'))
    write_csv('BATCHES_30.csv',batch)
    routes=[]
    for u in uu:
        for id in u['member_ids'].split(';'):
            routes.append(dict(ID=id,unit_id=u['unit_id'],batch_id=u['batch_id'],original_key_UNCHANGED=canon[id]['Raspuns'],risk=master[id]['risk_current_priority_UNCHANGED'],source_file=canon[id].get('Sursa',''),source_row=canon[id].get('Rand_sursa',''),prior_master='V95',closure='NOT_ADJUDICATED',approved_for_learning='NO'))
    write_csv('ID_ROUTING_822.csv',routes)
    summary=dict(canonical_blob=BLOB,canonical_records=len(canon),unique_qabc_units=len(uu),exact_duplicate_groups=sum(len(u['member_ids'].split(';'))>1 for u in uu),key_conflict_groups=sum(u['key_conflict']=='YES' for u in uu),batches=len(batch),batch_size_max=20,units_by_category=dict(collections.Counter(u['category'] for u in uu)),unit_risks=dict(collections.Counter(u['risk'] for u in uu)),source_master_sha256=hashlib.sha256(MASTER.read_bytes()).hexdigest(),prepared_not_audited=True,target_date_local='2026-11-11',timezone='Europe/Bucharest',completion_promise=False)
    (OUT/'PREPARATION_QA.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n');print(json.dumps(summary,ensure_ascii=False))
def export_batch(bid):
    canon,master=load();uu=[u for u in units(canon,master) if u['batch_id']==bid]
    assert uu,'Unknown batch'
    payload=[]
    for u in uu:
        r=canon[u['representative_id']]
        payload.append(dict(**u,question=r['Intrebare'],choices={k:r[k] for k in ['A','B','C']},original_members=[{k:canon[id].get(k) for k in ['ID','Grade','Sursa','Rand_sursa','Versiune','Raspuns','Explicatie']} for id in u['member_ids'].split(';')],existing_evidence={id:master[id] for id in u['member_ids'].split(';')}))
    print(json.dumps(dict(batch_id=bid,author_instruction='Reuse prior evidence; reopen precise primary sources; evaluate every ABC and member ID; do not edit app/keys; no self-review.',units=payload),ensure_ascii=False,indent=2))
def validate(path):
    canon,master=load();allunits={u['unit_id']:u for u in units(canon,master)};data=json.loads(pathlib.Path(path).read_text())
    expected={u['unit_id'] for u in allunits.values() if u['batch_id']==data.get('batch_id')}
    records=data.get('results',[]);assert expected,'Unknown batch';assert len(records)==len(expected) and {r['unit_id'] for r in records}==expected,'Batch coverage mismatch'
    for r in records:
        u=allunits[r['unit_id']];assert r.get('qabc_sha256')==u['qabc_sha256'],'Text provenance mismatch'
        assert r.get('author') and r.get('reviewer') and r['author']!=r['reviewer'],'Independent reviewer required'
        assert r.get('review_status') in ['SUPPORTED','REVISE','BLOCKED'],'Explicit reviewer outcome required'
        assert {x['ID'] for x in r.get('members',[])}==set(u['member_ids'].split(';')),'Every canonical ID needs adjudication'
        assert len(r['members'])==len(u['member_ids'].split(';')),'Duplicate member decision'
        assert r.get('status') in ['VERIFIED_AS_STORED','CORRECTION_READY_REVIEWED','BLOCKED_SOURCE','BLOCKED_EDITION','BLOCKED_DIAGRAM','BLOCKED_AMBIGUITY'],'Invalid status'
        for m in r['members']:
            assert m.get('original_key')==canon[m['ID']]['Raspuns'],'Original key drift'
            assert m.get('key_change_authorized')=='NO' and m.get('approved_for_learning')=='NO','Approval must not be invented'
        if r['status'].startswith('BLOCKED'):
            assert r.get('blocker') and r.get('next_action'),'Describe unresolved blocker'
            continue
        assert not (u['key_conflict']=='YES' and r['status']=='VERIFIED_AS_STORED'),'Contradictory original keys cannot all be verified as stored'
        assert len({m.get('proposed_key') for m in r['members']})==1,'Exact QABC needs one adjudicated proposed answer; divergent contexts require a separately reviewed split, not automatic closure'
        assert r['review_status']=='SUPPORTED','Cannot close a rejected or blocked review'
        assert all(isinstance(r.get('ABC',{}).get(k),str) and len(r['ABC'][k].strip())>=20 for k in ['A','B','C']),'All ABC need substantive reasoning'
        assert r.get('source_reference') and r.get('exact_locator') and r.get('edition'),'Exact primary source, locator and edition required'
        assert r.get('source_kind') in ['official_normative','author_published_didactic','manufacturer','university','derivation_with_primary_basis'],'Answer banks cannot validate answers'
        assert all(r.get(k) is True for k in ['source_opened','edition_verified','exam_applicability_verified','reviewer_reopened_source']),'Source/version/applicability independent checks required'
        assert r.get('single_answer_demonstrated') is True,'A unique answer must be established under original or explicitly corrected wording'
        assert r.get('reviewer_evidence_ref'),'Independent review evidence must be traceable'
        assert r.get('linguistic_findings') and r.get('technical_adjudication'),'Language and technical adjudication required'
        for m in r['members']:
            assert m.get('proposed_key') in ['A','B','C'] and m.get('grade_applicability'),'Each grade/member requires an answer and scope'
            assert m.get('explanation_assessment'),'Existing explanation must also be assessed per member ID'
            if r['status']=='VERIFIED_AS_STORED':assert m['proposed_key']==m['original_key'],'A key change needs correction status'
            if r['status']=='CORRECTION_READY_REVIEWED':assert m.get('exact_correction_before_after') and m.get('proposed_explanation'),'Concrete correction and source-supported explanation required'
    return dict(batch_id=data['batch_id'],structure='PASS',domain_truth='NOT_ESTABLISHED_BY_SCRIPT',unit_count=len(records),status_counts=dict(collections.Counter(r['status'] for r in records)),learning_approvals=0)
def final_check(directory):
    canon,master=load();uu=units(canon,master);expected={u['batch_id'] for u in uu}
    fs=sorted(pathlib.Path(directory).glob('*.json'));found=[];statuses=collections.Counter()
    for f in fs:
        data=json.loads(f.read_text())
        if 'results' not in data:continue
        check=validate(f);found.append(check['batch_id']);statuses.update(check['status_counts'])
    assert len(found)==len(expected) and set(found)==expected,'All 30 batches required exactly once'
    assert not any(k.startswith('BLOCKED') and v for k,v in statuses.items()),'Unresolved blockers prevent final content closure'
    return dict(batches=30,units=568,canonical_ids=822,structural_closure='PASS',domain_truth='REQUIRES_REVIEW_EVIDENCE_NOT_PROVED_BY_SCRIPT',content_decisions='READY_FOR_AGGREGATE_REVIEW',implementation_authorized=False,learning_approvals=0)
if __name__=='__main__':
    a=argparse.ArgumentParser();a.add_argument('action',choices=['prepare','batch','validate','final-check']);a.add_argument('value',nargs='?');args=a.parse_args()
    try:
        if args.action=='prepare':prepare()
        elif args.action=='batch':export_batch(args.value)
        elif args.action=='validate':print(json.dumps(validate(args.value)))
        else:print(json.dumps(final_check(args.value)))
    except (AssertionError,KeyError,TypeError,ValueError) as e:
        print('AUDIT STRUCTURAL GATE FAILED: '+str(e),file=sys.stderr);sys.exit(2)
