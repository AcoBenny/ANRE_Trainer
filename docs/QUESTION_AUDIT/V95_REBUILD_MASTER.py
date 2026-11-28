import csv, json, pathlib, hashlib, collections, subprocess
repo=pathlib.Path(__file__).resolve().parents[2]
p=repo/'docs/QUESTION_AUDIT'
def rows(f):
    return list(csv.DictReader(f.open()))
canon=json.JSONDecoder().raw_decode((repo/'app/src/main/assets/anre_trainer.html').read_text().split('const DATA=',1)[1])[0]
c={r['ID']:r for r in canon}
old=rows(next(p.glob('V83*.csv')))
baseline={r['ID']:r for r in old}
analyses=collections.defaultdict(list);reviews=collections.defaultdict(list);errors=[];counts={}
for version in ['V85','V86','V87','V88','V90','V91','V92']:
    f=next(p.glob(version+'*.csv')); rr=rows(f);counts[version]=len(rr)
    for r in rr:
        id=r['ID']; q=c[id]
        for col in ['A','B','C']:
            if q[col]!=r[col]:errors.append([version,id,col])
        if q['Intrebare']!=r['question']:errors.append([version,id,'question'])
        if q['Raspuns']!=r['canonical_key_UNCHANGED']:errors.append([version,id,'key'])
        analyses[id].append((version,f.name,r))
for version in ['V89','V93','V97','V98','V99']:
    fs=list(p.glob(version+'*.csv'))
    if not fs:continue
    f=fs[0];rr=rows(f);counts[version]=len(rr)
    for r in rr:
        assert r['ID'] in c,(version,r['ID'])
        reviews[r['ID']].append((version,f.name,r))
assert len(canon)==len(c)==822
assert set(c)==set(baseline)
assert not errors,errors
newfocus={id for id in analyses if baseline[id]['focus_audit_batch_2026_11_11']=='NONE_THIS_SESSION'}
prevfocus={id for id,r in baseline.items() if r['focus_audit_batch_2026_11_11']!='NONE_THIS_SESSION'}
cols=['ID','grade','category','canonical_key_UNCHANGED','risk_current_priority_UNCHANGED','legacy_locator_status_V73','focused_evidence_batches','new_analysis_files','new_candidate_or_qualification_NOT_APPROVED','new_source_urls_recorded_NOT_CERTIFIED','new_exact_locator','new_edition_and_remaining_gate','independent_AI_review_files','independent_AI_claim_verdicts_NOT_ANSWER_APPROVAL','qualified_human_signoff','approved_for_learning','key_change_authorized']
def value(r,keys):
    return next((r[k] for k in keys if r.get(k)), '')
with (p/'V95_ALL_822_MASTER_AFTER_FOCUSED_RECHECKS_AND_SEPARATE_AI_QA.csv').open('w',newline='') as out:
    w=csv.DictWriter(out,fieldnames=cols,lineterminator='\n');w.writeheader()
    for b in old:
        id=b['ID'];aa=analyses.get(id,[]);rr=reviews.get(id,[])
        prior=b['focus_audit_batch_2026_11_11'];focus=([prior] if prior!='NONE_THIS_SESSION' else [])+[a[0] for a in aa if a[0]!='V91']
        latest=aa[-1][2] if aa else {}
        w.writerow(dict(ID=id,grade=b['grade'],category=b['category'],canonical_key_UNCHANGED=c[id]['Raspuns'],risk_current_priority_UNCHANGED=b['risk_current_priority'],legacy_locator_status_V73=b['source_locator_status_V73'],focused_evidence_batches=';'.join(focus) or 'NO_FOCUSED_RECHECK_RECORDED',new_analysis_files=';'.join(a[1] for a in aa),new_candidate_or_qualification_NOT_APPROVED=value(latest,['candidate_NOT_APPROVED','candidate_PRELIMINARY','preliminary_status']) or b['candidate_OR_qualification_NOT_APPROVED'],new_source_urls_recorded_NOT_CERTIFIED=value(latest,['source_url','source_uri']) or b['source_url_recorded'],new_exact_locator=latest.get('article_or_page',''),new_edition_and_remaining_gate=' | '.join(filter(None,[latest.get('edition',''),value(latest,['remaining_gate','applicability_gate'])])),independent_AI_review_files=';'.join(r[1] for r in rr),independent_AI_claim_verdicts_NOT_ANSWER_APPROVAL=';'.join(r[0]+':'+r[2].get('verdict','UNSPECIFIED') for r in rr) or 'NOT_RUN',qualified_human_signoff='NOT_RUN',approved_for_learning='NO',key_change_authorized='NO'))
summary=dict(baseline_commit='ceea23837613cb4a8bcd7d34aa39ae3dfe6c4433',canonical_blob='bc5b5a61954ba138cf83987bfc932eca517f3b21',canonical_records=len(canon),unique_ids=len(c),batch_row_counts=counts,analysis_rows=sum(counts[x] for x in ['V85','V86','V87','V88','V90','V91','V92']),analysis_unique_ids=len(analyses),new_focus_unique_ids=len(newfocus),previous_focus_unique_ids=len(prevfocus),total_focus_unique_ids=len(prevfocus|newfocus),new_focus_P0=sum(baseline[id]['risk_current_priority']=='P0' for id in newfocus),new_focus_P1=sum(baseline[id]['risk_current_priority']=='P1' for id in newfocus),P0_without_recorded_focused_attempt=[id for id,b in baseline.items() if b['risk_current_priority']=='P0' and id not in prevfocus|newfocus],independent_AI_review_rows=sum(len(v) for v in reviews.values()),independent_AI_review_unique_ids=len(reviews),independent_AI_review_verdict_counts=dict(collections.Counter(r[2].get('verdict','') for a in reviews.values() for r in a)),qualified_human_signoffs=0,learning_approvals=0,canonical_text_choice_key_mismatches=errors,risk_distribution=dict(collections.Counter(b['risk_current_priority'] for b in old)))
summary['new_analysis_files_sha256']={f.name:hashlib.sha256(f.read_bytes()).hexdigest() for f in sorted(p.glob('V*.csv')) if f.name[:3] in counts}
(p/'V95_EXECUTED_DATA_QA_SUMMARY.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(summary,ensure_ascii=False,indent=2))
