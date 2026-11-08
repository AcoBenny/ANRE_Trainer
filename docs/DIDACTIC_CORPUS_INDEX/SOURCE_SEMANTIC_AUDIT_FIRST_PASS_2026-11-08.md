# 1MAiN / Avengers Asamble | ANRE Trainer: audit semantic al bibliotecii, prima trecere

**Data:** 8 noiembrie 2026  
**Tip:** registru de audit al surselor, **NU** mapare întrebare-răspuns şi **NU** lansare aplicaţie.  
**Regulă:** documentaţie didactică complet verificată înainte de cele 822 de întrebări. HTML, APK, datele întrebărilor şi baremele rămân îngheţate.  
**Checkpoint:** CKPT-002 rămâne curent; acest rezultat este un registru intermediar, nu CKPT-003.

## Rezultat măsurat

- **42 verificări de principii / navigare**, repartizate pe toate **11 lucrări canonice** (14 PDF-uri brute minus duplicate).
- În **42/42 cazuri** este localizat un reper textual pe pagina PDF respectivă; acesta **nu dovedeşte singur propoziţia exactă**.
- **9 verificări asociate cu 8 pagini PDF inspectate vizual** (paginile 52, 63, 90, 132 în PREG; 66, 67, 88 în UTCN; 99 în AUT_1995). Unele pagini sunt folosite de mai multe verificări.
- **6 formule/concepte tehnice au fost confirmate din imaginea originală**, deşi în unele cazuri extragerea automată a textului era coruptă. Acestea sunt spotcheck-uri ale aceleiaşi asistenţe, **nu verificări independente**.
- **0 aprobări finale independente** pentru utilizarea unui paragraf drept dovadă oficială în ANRE Trainer.

### Probleme concrete de calitate

**1. Terminologie incorectă în materialul didactic PREG p.52 (CONFIRMAT VIZUAL).** Formula efectului Joule-Lenz este prezentată ca `Q = I²·R·t`, însă legenda numeşte `R` „rezistivitate electrică” şi îi dă unitatea `Ω`. Corect: `R` = rezistenţa electrică în ohmi; rezistivitatea `ρ` are unitatea `Ω·m`. Formula rămâne validă dacă `R` e rezistenţă. **Nu vom prelua legenda greşită în explicaţiile ANRE.**

**2. Convenţie incompletă la inducţia Faraday-Lenz, PREG p.63 (NECESITĂ PRECIZARE).** Manualul scrie `e = ΔΦ/Δt`, fără semnul minus în formularea vizibilă. Pentru un circuit orientat, forma completă include semnul lui Lenz; expresia pozitivă poate descrie modulul dacă este precizat. Se marchează `SIGN_CONVENTION_MISSING`, nu se afirmă că orice utilizare fără semn este greşită.

**3. Eroare de OCR, nu de manual, la transformatoare în AUT_1995 p.99 (CONFIRMAT VIZUAL).** Ecuaţia raportului de transformare este lizibilă în scanul original (`w1/w2 = U1/U2` pentru raportul ideal), dar transcrierea OCR este deteriorată. Pentru formule se va consulta pagina originală, nu OCR-ul.

**4. Context care poate schimba răspunsul:** MAS p.66 foloseşte `p` pentru **perechi de poli**, nu numărul total de poli; MAS p.82 dă formula alunecării pentru maşină, dar intervalul de motorizare nu este universal. PREG p.184 confirmă reostate în reglajul excitaţiei generatorului, ceea ce nu dovedeşte că rezistoarele sunt dispozitive uzuale pentru reglajul tensiunii într-o reţea electrică.

**5. Formule autentificate vizual:** PREG p.63 `W = 1/2 LI²`, p.90 `cosφ=P/S` şi `cosφ=R/Z` (RLC serie), p.132 `f=1/T`; UTCN p.66 conexiune Y cu `U_l=√3 U_f`, p.67 conexiune Δ cu `I_l=√3 I_f`, p.88 puterea trifazată `P=√3 U_l I_l cosφ`, în **regim simetric/echilibrat**. Nu extindem aceste relaţii fără condiţiile specificate.

**6. Distincţii între tipurile de surse:** I7-2011 consolidat 2023 descrie protecţia la defect şi cerinţele DDR, dar versiunea juridică aplicabilă în 2026 se verifică separat. Manualul IEC 2007 şi STATII istoric servesc drept didactică tehnică, nu drept legislaţie actuală. Cataloagele Finder/Schneider24 sunt legate de modele comerciale; instrucţiunea SSM încărcată este internă, nu regulament ANRE.

## Audit al taxonomiei de 45 categorii

- Indexul iniţial are 45 coduri, dar `produs_referinte_coduri` e metadată comercială, **nu concept didactic**: rămân **44 categorii curriculare** în acea clasificare, care oricum trebuie extinsă.
- 13 categorii au fost marcate pentru revizuire prioritară a acoperirii sau a autorităţii sursei; niciuna nu este aprobată prin simpla identificare a cuvintelor.
- `legislatie_autorizare` găseşte cuvinte în manuale istorice, **nu** într-un regulament în vigoare. Este nevoie de portal ANRE şi Portalul Legislativ, cu data versiunii.
- `incarcare_vehicule_electrice` apare doar într-un catalog Schneider 2024, fără manual teoretic suficient în biblioteca actuală.
- `camp_electric` are potriviri doar în PREG, deci necesită verificare de acoperire, nu concluzia că e absent în rest.
- Domeniile `linii_aeriene`, `r_l_c_impedanta`, `camp_magnetic`, `instalatii_situatii_speciale` trebuie despărţite în concepte mai precise. Nu sunt încă coduri separate pentru GIS individual, vector Poynting, tranzitorii RC/RL, capacitate de serviciu LEA şi efectul Corona.

**Concluzie:** „toate cele 45 au cel puţin un keyword hit” **nu înseamnă** „toate domeniile ANRE sunt acoperite şi validate”.

## Validitatea normativă şi drepturile

- ANRE afişează tematica/bibliografia şi exemplele de întrebări pe pagina sa de autorizare: https://anre.ro/participanti-la-piata-de-energie/persoane-fizice/energie-electrica/
- I7-2011 este modificat prin Ordinul 959/2023: https://legislatie.just.ro/Public/DetaliiDocument/271142 ; textul de bază şi unele dispoziţii tranzitorii sunt la https://legislatie.just.ro/Public/DetaliiDocument/286763 . Aceste referinţe **nu** certifică automat PDF-ul consolidat încărcat pentru orice situaţie din 2026.
- Manualele utilizatorului nu sunt republicate pe GitHub. Drepturile de integrare offline a textelor sau paginilor din cărţile unor terţi sunt **NEVERIFICATE**.

## Registru individual al celor 42 de verificări

**Legendă:** `TEXT_LOCATOR` = lectura textului extras şi confirmarea unui reper, verificare asistată, nu QA extern; `VISUAL_PDF_PAGE` = imaginea originală inspectată; ambele rămân fără confirmare de la un al doilea evaluator. Pagini = numerotare fizică PDF, de la 1. Toate rândurile au `independent_qa=NOT_RUN` şi `rights_to_embed=NOT_VERIFIED`.

| ID | Lucrare / pagina PDF | Concept | Constatare | Limită importantă |
|---|---|---|---|---|
| SQA-001 | PREG p.40 | Legea lui Ohm | PRINCIPLE_LOCATED | Confirmare independentă şi contextuală încă necesară. |
| SQA-002 | PREG p.45 | Kirchhoff I | PRINCIPLE_LOCATED | Confirmare independentă şi contextuală încă necesară. |
| SQA-003 | PREG p.46 | Kirchhoff II | PRINCIPLE_LOCATED | Confirmare independentă şi contextuală încă necesară. |
| SQA-004 | PREG p.52 | Joule-Lenz | SOURCE_TERMINOLOGY_ERROR | Formula se vede corect în pagină, dar R e definit greșit drept rezistivitate (unitate Ω). Corect: rezistență R în Ω; rezistivitate ρ în Ω·m. |
| SQA-005 | PREG p.63 | Energie câmp magnetic | FORMULA_VISUALLY_CONFIRMED | Extragerea formulei în PDF este coruptă, dar expresia este lizibilă în imagine. |
| SQA-006 | PREG p.63 | Inducție Faraday-Lenz | SIGN_CONVENTION_MISSING | Manualul afișează e=ΔΦ/Δt fără semnul minus în formularea generală; necesară precizarea sensului de referință/Lenz sau că se folosește doar modulul. |
| SQA-007 | PREG p.68 | Rezistențe în serie | PRINCIPLE_LOCATED | Confirmare independentă şi contextuală încă necesară. |
| SQA-008 | PREG p.69 | Rezistențe paralel | PRINCIPLE_LOCATED | Confirmare independentă şi contextuală încă necesară. |
| SQA-009 | PREG p.70 | Rezistențe paralel | PRINCIPLE_LOCATED | Confirmare independentă şi contextuală încă necesară. |
| SQA-010 | PREG p.87 | Rezistor în curent alternativ | PRINCIPLE_LOCATED | Confirmare independentă şi contextuală încă necesară. |
| SQA-011 | PREG p.88 | Bobină ideală CA | PRINCIPLE_LOCATED | Confirmare independentă şi contextuală încă necesară. |
| SQA-012 | PREG p.88 | Condensator ideal CA | PRINCIPLE_LOCATED | Confirmare independentă şi contextuală încă necesară. |
| SQA-013 | PREG p.89 | Reactanțe CA | PRINCIPLE_LOCATED | Confirmare independentă şi contextuală încă necesară. |
| SQA-014 | PREG p.90 | Factorul de putere | FORMULA_VISUALLY_CONFIRMED | Textul extras este deteriorat, dar imaginea arată cosφ=P/S și cosφ=R/Z pentru RLC serie. |
| SQA-015 | PREG p.128 | Ohmmetru | PRINCIPLE_LOCATED | Confirmare independentă şi contextuală încă necesară. |
| SQA-016 | PREG p.132 | Frecvență și perioadă | FORMULA_VISUALLY_CONFIRMED | Formula f=1/T și definiția perioadei au fost confirmate în imaginea originală. |
| SQA-017 | PREG p.133 | Voltmetru | PRINCIPLE_LOCATED | Confirmare independentă şi contextuală încă necesară. |
| SQA-018 | PREG p.136 | Ampermetru | PRINCIPLE_LOCATED | Confirmare independentă şi contextuală încă necesară. |
| SQA-019 | PREG p.184 | Reglajul excitației | CONTEXT_SENSITIVE | Nu dovedește că un rezistor este element tipic de reglare a tensiunii din rețeaua electrică; nu transfera automat între domenii. |
| SQA-020 | PREG p.251 | Rezistența unui conductor | PRINCIPLE_LOCATED | Confirmare independentă şi contextuală încă necesară. |
| SQA-021 | MAS p.4 | Conversie energetică | PRINCIPLE_LOCATED | Confirmare independentă şi contextuală încă necesară. |
| SQA-022 | MAS p.7 | Transformator | PRINCIPLE_LOCATED | Confirmare independentă şi contextuală încă necesară. |
| SQA-023 | MAS p.14 | Raport transformare | PRINCIPLE_LOCATED | Confirmare independentă şi contextuală încă necesară. |
| SQA-024 | MAS p.66 | Viteză sincronism | PARAMETER_DEFINITION_REQUIRED | Nu confunda perechi de poli cu numărul total de poli. |
| SQA-025 | MAS p.82 | Alunecarea motorului | OPERATING_MODE_REQUIRED | Regimul generator/contra-curent poate ieși din intervalul uzual al alunecării motorului. |
| SQA-026 | UTCN p.66 | Tensiuni și curenți Y | FORMULA_VISUALLY_CONFIRMED | Radicalul √3 nu este păstrat în extragerea textului din PDF; imaginea originală este corectă. |
| SQA-027 | UTCN p.67 | Tensiuni și curenți Δ | FORMULA_VISUALLY_CONFIRMED | Radicalul √3 trebuie preluat din imagine, nu din textul extras. |
| SQA-028 | UTCN p.84 | Putere complexă CA | PRINCIPLE_LOCATED | Confirmare independentă şi contextuală încă necesară. |
| SQA-029 | UTCN p.88 | Puteri trifazate | FORMULA_VISUALLY_CONFIRMED | Pagină cu formule și scheme grafice; extragerea textului este goală. |
| SQA-030 | I7 p.23 | Protecție la defect | NORM_VERSION_PENDING | Nu implica că PE singur asigură protecția în orice regim; se aplică regulile TN/TT/IT și deconectare. |
| SQA-031 | I7 p.25 | Protecție DDR | NORM_VERSION_PENDING | Necesită text normativ aplicabil la data și configurația cerută. |
| SQA-032 | I7 p.37 | Supracurenți | NORM_VERSION_PENDING | Documentul încărcat este versiunea consolidată 2023, nu verdict de valabilitate în 2026. |
| SQA-033 | IEC p.224 | Armonici | LEGACY_GUIDE | Manual comercial/tehnic datat; nu autoritate legislativă actuală. |
| SQA-034 | IEC p.306 | Compensare reactivă | LEGACY_GUIDE | Propoziția e utilă didactic, ediția și condițiile trebuie notate. |
| SQA-035 | STATII p.373 | Limitare curent scurtcircuit | HISTORICAL_DIDACTIC | Relevant principial, dar terminologia și echipamentele sunt din ediție istorică. |
| SQA-036 | STATII p.302 | Descărcătoare | DEVICE_GENERATION_SENSITIVE | Textul istoric nu confirmă caracteristici specifice ZnO moderne. |
| SQA-037 | AUT_1995 p.99 | Transformatoare | OCR_FORMULA_CORRUPTED | În scanul original formula raportului apare lizibilă, dar textul OCR o transcrie greșit. Ediție istorică 1995. |
| SQA-038 | AUT_1995 p.101 | Transformatoare în paralel | HISTORICAL_DIDACTIC | Limitele numerice și cerințele actuale trebuie verificate din standarde curente. |
| SQA-039 | SCHNEIDER24 p.421 | RCD/RCBO | VENDOR_PRODUCT_NOT_NORM | Nu este normativ de proiectare; specificațiile variază pe familie și ediție. |
| SQA-040 | FINDER p.33 | Relee | VENDOR_PRODUCT_NOT_NORM | Catalog de produs; nu justifică generalizarea schemelor tuturor releelor. |
| SQA-041 | SSM p.2 | Lucru în siguranță | INTERNAL_NOT_ANRE_LEGISLATION | Nu se transformă în obligație generală ANRE prin simpla citare a unui regulament intern. |
| SQA-042 | I7OLD p.50 | Legături echipotențiale | HISTORICAL_NORM_DO_NOT_PROMOTE | Nu se citează ca reglementare actuală fără verificare față de I7 actual. |

## Următoarea etapă (fără modificări ale aplicaţiei)

1. Extinderea taxonomiei cu subiectele specializate lipsă şi maparea lor la capitole specifice; **nu** trecem încă la cele 822 de întrebări.
2. Validarea vizuală/inginerească a formulelor şi diagramelor care au fost doar localizate prin text (inclusiv blocajele din rubricile avansate). Actualizarea reperelor şi a stării de QA pentru fiecare paragraf, nu doar pentru fiecare capitol.
3. Controlul versiunilor normative şi surselor oficiale + stabilirea condiţiilor de reutilizare offline, pe fiecare document.
4. Numai după surse didactice validate: auditul întrebărilor, baremelor, duplicatelor şi formulărilor-capcană prin AGENT-031 şi QA independent. APK / HTML / baza de 822 rămân neatinse până la aprobarea utilizatorului.

**Cost suplimentar:** 0 RON. **Independent electrical reviewer:** NOT_RUN. **Independent language agent:** NOT_RUN. **App build/E2E:** NOT_RUN. **Checkpoint:** nu a fost generat unul nou.
