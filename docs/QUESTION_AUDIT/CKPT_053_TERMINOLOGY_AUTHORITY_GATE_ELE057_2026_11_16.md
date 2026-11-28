# CKPT-053 | Regula contextului terminologic, a bibliografiei și autorității sursei | ELE-057

Data: 2026-11-16. Continuă CKPT-052 fără rescrierea analizei originale. Ramură: \`audit/anre-v8-priority-17-20261109\`; PR #7 Draft. Nu modificați textul, ordinea A/B/C, baremul, HTML/APK, main, merge/release. Este o **schimbare de protocol**, nu o fișă nouă: rămân 114/568 unități și 139/822 ID-uri cu documentație contextuală. Aprobări pentru învățare: **0**.

## Descoperire din discuția cu utilizatorul

Utilizatorul a propus B pe baza faptului că două sinusoide de aceeași perioadă/frecvență pot fi adunate într-o altă sinusoidă de aceeași frecvență și pot fi reprezentate într-un sistem comun de fazori. A reconsiderat apoi **A ca variantă utilizată de testul ANRE**, explicând diferența prin posibile convenții terminologice între epoci. Contribuția identifică necesitatea să separăm **obiectul, operația, sensul termenului și epoca/autoritatea sursei**.

**Atenție la demonstrație:** interpretarea B este valabilă pentru sinusoide sincrone, dar această proprietate nu stabilește singură definiția expresiei „armonice între ele”. Din sursele accesate nu avem o comparație *diacronică* a aceleiași definiții care să dovedească înlocuirea terminologiei vechi cu una nouă. Această explicație temporală se păstrează ca **ipoteză de verificat**, NU ca fapt istoric certificat.

## Straturile obligatorii ale verdictului

1. \`CANONICAL_QUESTION_AND_KEY\`: exact enunțul și A/B/C/cheia sursei importate, versiunea și ID-urile, fără editare.
2. \`EXAM_AUTHORITY\`: **întrebare oficial publicată**, **cheie oficial verificată direct** și **soluție istorică neoficială** sunt trei probe diferite. Nu se transformă o întrebare de pe site-ul ANRE într-o confirmare oficială a răspunsului.
3. \`SEMANTIC_TECHNICAL_TRUTH\`: definiția precisă, obiectul, activitatea întrebată și condițiile matematice/fizice. Verifică reciproca raportului, cazul-limită și contradicții între A/B/C.
4. \`BIBLIOGRAPHY_AND_EDITION\`: gradul, domeniul și ediția aplicabilă. **Data mai recentă nu înlocuiește automat o sursă mai veche**, iar o sursă veche nu câștigă automat. Pentru o normă juridică dovedit abrogată aplici sursa în vigoare; pentru convenții didactice verifici domeniul/definiția/autoritatea testului.
5. \`USER_INTERPRETATION\`: motivele utilizatorului rămân vizibile, separate de verificarea independentă. Poate ridica o ambiguitate chiar dacă baremul istoric rămâne intact.
6. \`REVIEW_AND_RELEASE\`: o interpretare plauzibilă sau un test sintetic PASS nu înseamnă răspuns aprobat; QA independent sursă/tehnic/lingvistic și poarta de aprobare rămân separate.

## Aplicare concretă ELE-057

- \`G1-ELE-057\` / \`G2-ELEC-203\`, unitate \`AU-84185dba0d7b87f1\`. Întrebare: „Două funcţii periodice sinusoidale sunt armonice între ele dacă:”. Barem canonic **A** pentru ambele grade.
- \`ANRE\` publică setul **ELECTROTEHNICA-09.2024** ca întrebări exemplu: https://anre.ro/participanti-la-piata-de-energie/persoane-fizice/energie-electrica/ ; fișierul sursă: https://anre.ro/wp-content/uploads/2024/11/ELECTROTEHNICA-09.2024-2.xlsx . Confirmarea publicării **nu certifică litera A ca barem oficial direct**.
- Culegere rezolvată istorică 2010 (sursă neoficială, nu e barem legal): https://tomaradu.yolasite.com/resources/30749113-Subiecte-rezolvate-examen-autorizare-ANRE-electricieni-2010-Electrotehnica.pdf ; indică A pentru grila istorică 67. Interpretează ca indiciu despre intenția baremului, nu dovadă incontestabilă.
- Bibliografia oficială ANRE 05.2023 precizează la Electrotehnică „manualele și cărțile din literatura tehnică de specialitate” pentru toate gradele, **fără a impune o anumită ediție veche**: https://anre.ro/wp-content/uploads/2023/05/Tematica-si-bibliografie-pentru-examenul-de-autorizare-electricieni-2023-.pdf (paginile PDF 1 și 4, inspectate vizual).
- **A**: relația fundamentală–armonică de ordin întreg în ordinea potrivită a frecvențelor/perioadelor, interpretarea propusă de baremul istoric.
- **B**: aceeași frecvență și defazaj constant caracterizează sinusoide sincrone/fazorial compatibile, dar nu sunt o condiție necesară pentru fundamentală+armonică superioară.
- **C**: inversarea ordinii perioadelor produce 1/2 în cazuri armonice, ceea ce expune ambiguitatea formulării.
- Stare \`HISTORICAL_KEY_PROVISIONAL_NOT_OFFICIAL\`, \`SEMANTIC_AMBIGUITY\`, \`USER_B_HYPOTHESIS_PRESERVED\`, \`NOT_APPROVED_FOR_LEARNING\`. **A nu a fost schimbat în B**.

## Regula operațională (de aplicat la TOATE domeniile)

\`Question, scope, grade, era\` → \`examine the source's definition before/after\` → \`distinguish official question/official key/unofficial solution\` → \`evaluate exact A/B/C under both definitions\` → \`verify that chronology change is actually documented\` → \`record technical truth and intended exam answer separately\` → \`independent QA\` → \`no automatic key change/release\`.

Dacă regula dintr-un curs recent este din alt context (de exemplu, calcul fazorial versus raporturi armonice), clasifică \`ADJACENT_SCOPE\`, nu contradicție sau „corecție modernă”. Dacă lipsește dovada unui răspuns oficial, folosește \`HISTORICAL_KEY_PROVISIONAL_NOT_OFFICIAL\`, nu \`OFFICIAL_CONFIRMED\`.

## Testare și dovezi

Plugin **Avengers Asamble v0.4.5**, skill \`context-expansion-reasoning\`, modulul \`terminology_authority_gate.py\`, împreună cu verificările din \`agent-router\` și \`qa-evidence-gate\`. Publicare plugin raportată ca \`pluginrel_6afb15e06cf88191a4a31b9cf4bb050d\`; plugin URL: https://chatgpt.com/plugins/plugins_6aeee75a94cc819195c0aeb3a9649391 .

**Executat local:** 14/14 teste sintetice de rutare PASS: ELE057 A istoric/B utilizator, întrebare oficială fără cheie oficială, sursă cu alt grad, sursă adiacentă fazorială, scope necunoscut, cheie direct oficială verificată dar QA deschisă, ipoteză cronologică neverificată, conflict barem și versiune, etc. Aceste teste verifică **logica etichetării**, NU sensul real verificat în cărți și NU sunt un benchmark de modele sau audit independent.

Test după modificarea pluginului: \`python skills/context-expansion-reasoning/scripts/terminology_authority_gate.py selftest\`.

## Continuare

Restul blocajelor \`ELE-128\` și \`ELE-222\` sunt în coada prioritară. Regula de mai sus se aplică automat la contraexemplele lor de circuit ideal versus mixt și la terminologia susceptanță/admitanță, fără a transforma cele două grile în răspunsuri aprobate. Nu cere utilizatorului repetarea unei interpretări deja oferite; intervine doar dacă o definiție autentică rămasă ambiguă nu poate fi adjudecată din context.
