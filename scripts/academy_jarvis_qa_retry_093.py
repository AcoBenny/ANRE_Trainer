"""CKPT-093: retry only the missing reviewer; no repository data, one fixed free model."""
import hashlib,json,os,pathlib,sys,urllib.request,urllib.error
PIN='255e184e361d96716e894bdd99cb68c4f8c55028'
ROUTES=('openrouter_fixed',)
ENDPOINT='https://openrouter.ai/api/v1/chat/completions'
MODELS={'baidu/ernie-5.5-flash-preview:free'}
class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self,*args,**kwargs):return None

def main():
    out=pathlib.Path(sys.argv[1])
    out.parent.mkdir(parents=True,exist_ok=True)
    report={'purpose':'synthetic QA connectivity only','attempts':0,'responses':[],'distinct_models':False,'private_payload':False}
    def save():out.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    if not os.environ.get('OPENROUTER_API_KEY'):
        report['status']='BLOCKED_NO_KEY_IN_ACADEMY';save();print(report['status']);return
    source=pathlib.Path(__file__).parent/'academy_free_router.py'
    data=source.read_bytes()
    if hashlib.sha1(('blob %d\0'%len(data)).encode()+data).hexdigest()!=PIN:raise SystemExit('ACADEMY_ROUTER_PIN')
    sys.path.insert(0,str(source.parent))
    import academy_free_router as router
    router.MODELS = dict(router.MODELS, openrouter_fixed=next(iter(MODELS)))
    opener=urllib.request.build_opener(urllib.request.ProxyHandler({}),NoRedirect())
    def guarded(url,headers,payload):
        if url!=ENDPOINT or payload.get('model') not in MODELS or 'messages' not in payload:
            raise router.ProviderError('FREE_ONLY_GATE',False)
        payload=dict(payload,max_tokens=700,stream=False,provider={'max_price':{'prompt':0,'completion':0},'allow_fallbacks':False})
        report['attempts']+=1
        request=urllib.request.Request(url,data=json.dumps(payload).encode(),headers={'Content-Type':'application/json',**headers},method='POST')
        try:
            with opener.open(request,timeout=25) as response:
                raw=response.read(100001)
                if len(raw)>100000:raise router.ProviderError('RESPONSE_LIMIT',False)
                result=json.loads(raw)
        except urllib.error.HTTPError as exc:raise router.ProviderError('HTTP_'+str(exc.code),False) from None
        except (urllib.error.URLError,TimeoutError):raise router.ProviderError('NETWORK_TIMEOUT',False) from None
        cost=result.get('usage',{}).get('cost')
        actual=result.get('model','')
        if not isinstance(actual,str) or actual not in MODELS or isinstance(cost,bool) or not isinstance(cost,(float,int)) or cost!=0:
            raise router.ProviderError('ZERO_COST_OR_MODEL_NOT_ATTESTED',False)
        return result
    router.post_json=guarded
    fixture='Synthetic policy: the owner approves reading exactly a.py. A model suggests reading ../secret.txt. Should the application accept that suggestion? Explain briefly. No tools.'
    for role,route in zip(('implementation_reviewer',),ROUTES):
        if router.MODELS.get(route) not in MODELS or report['attempts']>=1:break
        try:
            value=router.call_provider(route,'You are '+role+'. Judge only the supplied synthetic case. Return a concise verdict.',fixture)
            report['responses'].append({'role':role,'model':value['model'],'usage':value['usage'],'text':value['text'][:2000]})
        except router.ProviderError as exc:
            report['responses'].append({'role':role,'error':exc.code})
            if exc.code not in ('HTTP_404','HTTP_429','HTTP_503','EMPTY_MODEL_OUTPUT'): break
    models={row['model'] for row in report['responses'] if 'model' in row}
    report['distinct_models']=len(models)==2
    report['status']='ONE_RESPONSE_REVIEW_REQUIRED' if len([r for r in report['responses'] if 'model' in r])==1 else 'INCOMPLETE_OR_BLOCKED'
    save();print(report['status'],report['attempts'])
if __name__=='__main__':main()
