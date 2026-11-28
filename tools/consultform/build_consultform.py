#!/usr/bin/env python3
"""Generate personal CONSULTFORM candidate locally. Do not commit owner study material."""
import argparse, collections, hashlib, json, pathlib, unicodedata
P=pathlib.Path
HERE=P(__file__).resolve().parent

def norm(s):
    out=[]; pos=[]
    for i,c in enumerate(s):
        for v in unicodedata.normalize('NFD',c.casefold()):
            if unicodedata.combining(v): continue
            if v.isspace():
                if out and out[-1]!=' ': out.append(' ');pos.append(i)
            else: out.append(v);pos.append(i)
    return ''.join(out),pos

def highlight(ctx,answer):
    if not ctx or not ctx.get('highlight_paragraph'):return False
    p=ctx['highlight_paragraph']; n,idx=norm(p); a,_=norm(answer);a=a.strip().rstrip('.,;:!?')
    offset=n.find(a)
    if offset<0 or not a:return False
    start=idx[offset];end=idx[offset+len(a)-1]+1
    ctx['highlight_segments']=[p[:start],p[start:end],p[end:]]
    assert ''.join(ctx['highlight_segments'])==p
    return True

def build(payload,index,out):
    rows=json.loads(payload.read_text(encoding='utf-8'))['records']
    ix=json.loads(index.read_text(encoding='utf-8'))['records']
    assert len(rows)==len(ix)==305
    assert len({r['id'] for r in rows})==305 and {r['id'] for r in rows}=={i['id'] for i in ix}
    assert collections.Counter(r['grade'] for r in rows)=={'G1':151,'G2':154}
    assert collections.Counter(r['category'] for r in rows)=={'LEGISLATIE':104,'NORME_TEHNICE':201}
    byid={x['id']:x for x in ix};result=[]
    for r in rows:
        i=byid[r['id']];assert (r['grade'],r['answer'],r['reference'])==(i['grade'],i['key'],i['reference'])
        opts=r['options'];assert set(opts)=={'A','B','C'} and opts[r['answer']]==r['correct_text'] and r['source']['yellow_answer']==r['answer']
        highlight(r['card']['source_context'],r['correct_text'])
        e=None
        if i.get('editorial_rationale'):
            prov=i['editorial_provenance'];e={'text':i['editorial_rationale'],'source':prov['path'],'record':prov['record']}
        q={'ID':r['id'],'Categorie':{'LEGISLATIE':'Legislație','NORME_TEHNICE':'Norme tehnice'}[r['category']], 'Sursa':r['source']['file'],'Versiune':'CONSULTFORM CKPT-431','Rand_sursa':r['source']['row'],'Intrebare':r['question'],**opts,'Raspuns':r['answer'],'Grade':'I' if r['grade']=='G1' else 'II','Tip':'A+B','reference':r['reference'],'card':r['card'],'editorial':e}
        result.append(q)
    assert sum(q['editorial'] is not None for q in result)==144
    assert sum(q['card']['source_context'] is not None for q in result)==167
    js=json.dumps(result,ensure_ascii=False,separators=(',',':')).replace('<','\\u003c').replace('\u2028','\\u2028').replace('\u2029','\\u2029')
    shell=(HERE/'consultform_shell.html').read_text(encoding='utf-8');runtime=(HERE/'consultform_runtime.js').read_text(encoding='utf-8')
    assert shell.count('/*__DATA__*/[]')==shell.count('/*__RUNTIME__*/')==1
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(shell.replace('/*__DATA__*/[]',js).replace('/*__RUNTIME__*/',runtime),encoding='utf-8')
    print('305 questions; SHA256',hashlib.sha256(out.read_bytes()).hexdigest())
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--payload',required=True,type=P);p.add_argument('--index',type=P,default=HERE.parent.parent/'docs/CONSULTFORM/CKPT_431_CARD_INDEX_305.json');p.add_argument('--out',required=True,type=P);a=p.parse_args();build(a.payload,a.index,a.out)
