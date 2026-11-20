# FreeLLMAPI → ANRE Academy (pilot, NOT live)

## Ce este

Adaptor Python numai pentru cercetare/read-only: reutilizează cele șase scenarii negative din CKPT-256, apelează FreeLLMAPI la `/v1/chat/completions` cu `model=auto` și salvează **modelul efectiv folosit** din `X-Routed-Via`, comutările `X-Fallback-Attempts`, usage și răspunsurile. Criteriile de notare `required_behavior` / `unsafe_behavior` rămân ascunse modelului.

**Nu modifică** întrebările, A/B/C, baremele, HTML/APK. Nu aprobă răspunsuri și nu face fine-tuning. Nu pretinde QA independent. Poate face **maxim 6 apeluri** la rularea live; implicit `preflight` face 0 apeluri.

## Instalează FreeLLMAPI pe Windows (cea mai simplă probă)

1. Instalează aplicația originală, preferabil semnată din [Microsoft Store](https://apps.microsoft.com/detail/9PBN6G8K2B7F), sau [GitHub Releases](https://github.com/tashfeenahmed/freellmapi/releases/latest) (installerul GitHub poate fi nesemnat). Nu executa scripturi necunoscute cu privilegii de administrator.
2. Deschide dashboard-ul local `http://localhost:3001`, apoi **Keys**. Adaugă numai API keys pentru provideri/modele efectiv gratuite în contul tău, de exemplu Gemini și Groq. Dezactivează modele plătite, verifică bugetele/limitele providerilor și notează cheia unificată `freellmapi-...`. Nu o pune în chat, issue, commit sau capturi.
3. Configurează ordinea de fallback și testează în dashboard că se afișează providerul real. Verifică drepturile și condițiile free-tier. FreeLLMAPI estimează cote din catalog, dar **nu garantează sold gratuit sau cost zero**.

## Rulare read-only pe laptop

Din repository-ul ANRE clonat, pe ramura acestui PR, descarcă **doar** fixture-ul preînregistrat din audit la o cale locală (sau folosește fișierul deja existent într-un checkout al ramurii de audit).

```powershell
# Fără credențiale și fără apel AI:
python integrations/academy-freellmapi/academy_freellmapi_pilot.py --fixtures "calea-catre-fixtures.json" --mode preflight
```

Când sunt verificate toate setările, numai prin aprobare explicită și în **aceeași** sesiune PowerShell:

```powershell
$env:FREELLMAPI_BASE_URL = "http://localhost:3001/v1"
$env:FREELLMAPI_UNIFIED_KEY = "<cheia unificata din dashboard, NU in git>"
$env:ACADEMY_CONFIRM_LIVE = "RUN_6"
python integrations/academy-freellmapi/academy_freellmapi_pilot.py --fixtures "calea-catre-fixtures.json" --mode live
Remove-Item Env:FREELLMAPI_UNIFIED_KEY, Env:ACADEMY_CONFIRM_LIVE
```

Raportul local `academy_freellmapi_result.json` conține textul modelelor, nu se publică automat în GitHub. Nu publica date protejate ori chei. Evaluează separat dacă modelele au citat corect surse primare: fixture-urile oferă **doar descrieri de incidente**, nu întrebări QABC originale sau normele integrale.

## GitHub: ce se poate și ce nu

- Workflow-ul acestui PR pornește **automat pe pull request** și execută doar teste de securitate offline și preflight-ul celor șase fixture originale, **zero apeluri AI**, **zero chei**.
- GitHub Actions găzduit de GitHub **nu poate accesa routerul local `localhost:3001` de pe laptopul tău**.
- FreeLLMAPI este Node+SQLite, **nu se instalează direct în GitHub ca GitHub App** și nu se poate rula în Cloudflare Workers fără rescriere substanțială.
- Pentru executare autonomă continuă după pilot este nevoie de un router persistent pe un host propriu sau pe un server/VPS, cu stocare permanentă criptată și conexiune privată către orchestrator. Pe laptop funcționează doar cât este pornit.
- Un router temporar în fiecare GitHub Actions job ar pierde istoricul de cote dacă SQLite nu este persistat; cotele aplicate de furnizori rămân, dar monitorizarea locală devine incompletă.
- Nu expune dashboardul FreeLLMAPI public pe Internet. Proiectul este conceput pentru un singur utilizator. Cloudflare PR #11 rămâne alternativă de rutare, Draft; niciun merge.
- Pentru ANRE, fallback-ul la modele mai slabe nu trebuie să aprobe automat o întrebare. Păstrează traseul fiecărui model și verificări independente, cu referințe reale.

## QA / dovezi

```bash
python -m unittest discover -s integrations/academy-freellmapi -p 'test_*.py' -v
```

8 teste offline: schema fixture, integritate, ascunderea rubricii, refuz HTTP remote nesecurizat, preflight fără apeluri, live fără confirmare refuzat, înregistrarea rutei. Funcționarea reală cu FreeLLMAPI încă **NOT_RUN** până la instalarea locală sau pe host.

Surse upstream: [FreeLLMAPI README](https://github.com/tashfeenahmed/freellmapi), [instalare](https://github.com/tashfeenahmed/freellmapi/blob/main/docs/en/install/01-install.md), [API](https://github.com/tashfeenahmed/freellmapi/blob/main/docs/en/api/01-rest-api.md).
