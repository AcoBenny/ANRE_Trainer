# CKPT-058 | Avengers Asamble v0.4.6: inferență bidirecțională enunț–răspunsuri | 2026-11-16

## Scop / proveniență
- Continuă CKPT-054–057, în special [CKPT-057](./CKPT_057_ELE128_OPTION_GUIDED_TERMINOLOGICAL_INFERENCE_2026_11_16.md), fără a repeta cercetarea ELE-128/222.
- Repo `AcoBenny/ANRE_Trainer`, branch `audit/anre-v8-priority-17-20261109`, PR #7 **OPEN/DRAFT**, HEAD înainte de documentare `3fed24e921bf1cfdb99ce7c9aaeaed69912504f3`.
- Input utilizator (acord explicit): „Foarte bine articulat răspunsul este Da începem să integrăm și această logică”.
- Regula formulată anterior de utilizator: deducerea/eliminarea funcționează **între enunț și variante**, nu doar **între variante**; un răspuns oferit poate dezvălui modelul didactic probabil, fără a redefini termenul fizic universal.

## Integrare realizată în pluginul personal
- Plugin: [Avengers Asamble](https://chatgpt.com/plugins/plugins_6aeee75a94cc819195c0aeb3a9649391), `plugins_6aeee75a94cc819195c0aeb3a9649391`.
- Versiune **0.4.6**, release `pluginrel_6afb1e6344b881918d4adbb5d5190499`; confirmat prin citire ulterioară a pluginului. **Scope USER / PRIVATE**, fără schimbarea audienței.
- Nou skill transversal: `skills/bidirectional-answer-inference/SKILL.md`.
- Script de preflight: `skills/bidirectional-answer-inference/scripts/bidirectional_gate.py`; unit tests: `skills/bidirectional-answer-inference/tests/test_bidirectional_gate.py`.
- Integrat efectiv în `skills/agent-router/SKILL.md` (ruting implicit al grilelor ambigue) și `skills/qa-evidence-gate/SKILL.md` (negative QA). Actualizate metadatele `plugin.json`, `.codex-plugin/plugin.json`, `CHANGELOG.md`. Restul fișierelor istorice au fost păstrate prin update cu overlay.
- Control readback live: versiunea 0.4.6, release ID și prezența noului skill, scriptului, rutării și QA gate au fost confirmate; fișierele context-expansion-reasoning v0.4.5 rămân disponibile.

## Regula formală
1. **Vertical:** enunț ↔ fiecare A/B/C, cu definiții, condiții, context, semn, calcule și compatibilitate.
2. **Orizontal:** A↔B, A↔C, B↔C: contradicție, incluziune, suprapunere, alternative independente.
3. **Reversibil:** candidatul dedus trebuie să poată fi explicat printr-un model **coerent și susținut afirmativ** de sursa potrivită; păstrează contramodelul generic și condiția nespusă. O variantă rămasă prin eliminare NU devine astfel automat adevăr universal sau cheie oficială.

**Stop conditions:** nicio opțiune exactă; două opțiuni compatibile simultan; ipoteză introdusă artificial pentru a forța cheia; sursă neadecvată obiectului/gradului/ediției; contraexemplu ce infirmă concluzia universală. Preservă `INTENDED_KEY_PROVISIONAL` distinct de `TECHNICAL_TRUTH`, `OFFICIAL_KEY_PROOF`, `USER_INTERPRETATION` și `INDEPENDENT_QA`.

## Execuții reale și limite
- Preflight script nou: **19/19 scenarii sintetice PASS**, inclusiv ELE128 și ELE222 ca exemple *de rutare*, zero/multiple variante potrivite, model inventat, absență sursă pozitivă, aprobări false și falsă semnătură QA.
- `python -m unittest discover -s .../tests`: **5/5 PASS**.
- Control ZIP: integritate `unzip -t` PASS; conținut exact 8 fișiere overlay dorite, fără modificare a scripturilor/fișelor anterioare; SHA256 `162e93ce0a0b0c73e5acf4e9304aef349b01f2428de34332901cd39b43c70874`.
- QA al pluginului: readback metadata/fișiere confirmat. **Benchmark end-to-end vechi `agent-benchmark`, execuția cu agenți independenți, verificarea efectivă a exactității sursei, testul ANRE HTML/APK: NU au fost rulate în această etapă.** Testele noi sunt **deterministe, structurale, pe intrări de test definite**, NU certifică semantica, validitatea baremului sau eficiența reală a unor agenți.
- Nu există o afirmație că regula este matematic suficientă pentru a deduce orice răspuns; verificarea cu sursă rămâne obligatorie.

## Stare ANRE și următorul pas
- **822 ID-uri / 568 unități QABC totale**; 114/568 unități și 139/822 ID-uri cu documentație contextuală (nicio unitate nouă prin acest CKPT); **0/822 aprobate pentru învățare**.
- **ELE-128:** A rămâne cheia importată. Utilizatorul a dedus intenția de model *pur inductiv* din variante; `R=X>0 ⇒ φ=45°` arată limita afirmației generale. Nu s-a înlocuit sensul științific generic.
- **ELE-222:** C rămâne cheia importată; modelul *pur reactiv* explică intenția didactică, dar `B=-X/(R²+X²)` în circuit mixt rămâne contraexemplul.
- Următoarele investigații aplică v0.4.6 și semnează sursele/edițiile, fără a transforma cercetarea în „aprobat pentru învățare” înainte de QA independent.
- **Nicio modificare la barem, enunțuri, A/B/C, master, HTML, APK; fără merge/main/release.**