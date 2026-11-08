# ANRE Trainer | V7: verificarea prealabilă a surselor înaintea celor 822 de întrebări

**Data:** 8 noiembrie 2026  
**Proiect:** `AcoBenny/ANRE_Trainer`  
**Mod:** numai inventar, control de surse, audit al informației și pregătirea intrării în auditul întrebărilor.  
**Nu s-au modificat:** întrebările, variantele A/B/C, baremele, fișierele HTML/APK și regulile aplicației.  
**Ultimul checkpoint rămâne:** `CKPT-ANRE-20261108-02`.

## Concluzie de lucru

Am finalizat **prima examinare cu dovadă de pagină a tuturor celor 44 de categorii** din taxonomia inițială, plus raportarea la tematica publicată oficial de ANRE pentru gradul I și II. Nu este echivalent cu o **aprobare semantică completă** a tuturor propozițiilor din fiecare categorie. Niciun revizor tehnic distinct nu a executat verificarea finală. Această diferență este centrală pentru a nu falsifica progresul.

- **11 surse canonice**, 3.464 pagini și 3.374 pagini cu text căutabil după OCR, conform inventarului precedent.
- **44/44 categorii examinate țintit** la nivel de pagină/fragment selectat; **43** au cel puțin o pagină locală cu text relevant, iar la încărcarea vehiculelor electrice există **doar identificarea oficială de domeniu** a `SR HD 60364-7-722:2019`, fără paragraf didactic local disponibil pentru verificare.
- **20 de constatări de QA** sunt consemnate, inclusiv imagini PDF originale inspectate. Semnale dure: formula OCR denaturată a transformatorului din manualul din 1995, radicalul √3 în circuitele trifazate, eroarea `R=rezistivitate` la Joule-Lenz, semnul Lenz omis la inducție, regimuri specifice pentru TN-C/TN-C-S și diferența dintre teorie electrică și aplicabilitate juridică.
- **0/44 categorii aprobate independent**; **7/7 blocaje istorice rămân formal deschise**, cu impact diferențiat. Nu declarăm o verificare independentă imaginară.

### Delimitare nouă: cerința reală pentru grad I/II

Tematica ANRE accesibilă pe website este documentul **„Tematica și bibliografie ... 05.2023”**. Acesta conține 29 de poziții bibliografice numerotate, **10 indicate DA pentru gradul I** și **13 indicate DA pentru gradul II**. Există cerințe avansate marcate *NU* pentru ambele grade I/II, care sunt relevante pentru grade III/IV, nu condiții universale pentru aplicația actuală. Un rezumat pe 29 de rânduri cu indicatoare DA/NU se află în `V7_OFFICIAL_ANRE_G1_G2_2023_BIBLIOGRAPHY.csv`. PDF-ul a fost consultat textual și vizual pentru paginile 1–3.

Sursa oficială: <https://anre.ro/wp-content/uploads/2023/05/Tematica-si-bibliografie-pentru-examenul-de-autorizare-electricieni-2023-.pdf>. Pagina ANRE afișează acest document din 2023 la momentul verificării; **nu am confirmat o ediție separată 2026 a tematicii**. Ediția documentului bibliografic nu dovedește ediția în vigoare a fiecărei reglementări nominalizate.

### Categorii care necesită atenție înaintea unei decizii despre un răspuns

- **Legislație autorizare:** manualul din 1995 este istoric. Se folosesc Ordinul 66/2023 și modificarea 65/2024, cu revizia articolelor potrivite întrebării.
- **Racordare/furnizare/contracte:** Ordinul 59/2013 prezintă o consolidare indicată la **25 mai 2026**. Regulile de contract din manualul 1995 nu sunt dovadă juridică actuală. Din bibliografia oficială fac parte și Ordinul 5/2023, Ordinul 102/2015 și, numai gradul II, Ordinul 128/2020.
- **SSM:** documentul `125473032-...` este un regulament intern, nu lege națională sau regulament de examinare ANRE. Sursă legală: Legea 319/2006, mai ales art. 7 și 20, cu verificare la articol.
- **Vehicule electrice:** doar catalogul SR HD 60364-7-722:2019 a fost localizat la nivelul domeniului; textul tehnic integral nu este liber accesibil. Prezența categoriei în taxonomie nu demonstrează că ea reprezintă un capitol separat obligatoriu în bibliografia I/II.
- **PV/eolian:** I7 §7.11 PDF pp136–138 acoperă principii PV și scheme, în forma sintetizată 22.09.2023. Eolienele și configurațiile avansate sunt documentate parțial extern, iar cerințele pentru generatoare depind de categoria A/B/C/D. Nu sunt condiții generale suplimentare de absolvire pentru tot auditul G1/G2.
- **Calcul cădere de tensiune, scurtcircuit, aparataj/transformatoare:** sursele prezintă principiile, dar exercițiile specifice necesită verificarea formulelor din pagină, a ipotezelor și a versiunilor normelor, la momentul verificării fiecărei întrebări.

### Criterii de trecere la verificarea întrebărilor (separat de implementare)

**A. Pregătire pentru TRIEREA întrebărilor, read-only:** este fezabilă pe baza dosarului V7. Pentru fiecare întrebare viitoare se va cere o propoziție tehnică exactă, gradul, forma A/B/C originală, sursa bibliografică potrivită și paragraful sau figura. Rezultatele se vor clasifica `CONFIRMAT_CU_DOVADA`, `CONDIȚIONAT`, `CONFLICT`, `FARA_SURSA` sau `SURSA_NEACTUALA`. **Aceasta nu reprezintă încă aprobarea baremului.** Este necesară decizia de trecere a utilizatorului, conform regulii de înghețare.

**B. Rectificare de BAREM / explicație finală:** `NO_GO` până la controlul independent al afirmației sensibile și al normei aplicabile, sau până la un acord explicit de operare cu clasificare a incertitudinii și fără eticheta „validat independent”. Niciun răspuns nu este schimbat tacit. Nu este necesar să obținem un drept de redistribuire a tuturor PDF-urilor pentru a **consulta** sursele și a verifica privat întrebări; este obligatoriu înaintea includerii documentelor și figurilor în aplicația publicată.

### Cele 7 blocaje, cu impact practic

1. PV: schema DC/AC și selectarea condițională SPD/RCD/selectivitate: blocaj pentru afirmații de proiectare PV, **nu** pentru legea lui Ohm.
2. PV: anti-insularizare, testare și setări: blocaj doar pentru afirmații specifice, nu pentru definiția conceptului.
3. PV: edițiile SR și articolele tehnice plătite: identificatori de catalog există, lipsesc anumite paragrafe accesibile pentru concluzii numerice.
4. Eolian: topologii și protecție convertor/generator: schemă didactică parțială; lipsesc surse definitive pentru proiect concret.
5. Eolian: cerințe A/B/C/D: surse ANRE și clasificare găsite, revizia pe fiecare situație este neterminată.
6. **QA independent: `NOT_RUN`**, blochează emiterea unei etichete de certificare finală.
7. **Drepturi offline: `NOT_CLEARED`**, blochează republicarea cărților/figurilor protejate în APK, **nu** auditul privat al întrebărilor.

## Dovezi și fișiere

- `V7_44_TOPIC_SEMANTIC_SCREENING.csv`: 44 rânduri, cărți, pagini originale, propoziție rezumată, grad de încredere, probleme și starea QA.
- `V7_OFFICIAL_ANRE_G1_G2_2023_BIBLIOGRAPHY.csv`: 29 de poziții din documentul ANRE 2023, cu DA/NU pe grad I și II și pagina oficială.
- `V7_FORMULA_SOURCE_AND_GATE_QA_20.csv`: 20 de observații și riscuri concrete.
- `V7_7_BLOCKERS_SCOPE_AND_HANDOFF.csv`: 7 blocaje și dacă împiedică toate întrebările sau numai subiecte specifice.
- `ANRE_Registru_Validare_Concepte_V7_2026-11-08.xlsx`: păstrează V1–V6, adaugă V7 și panou cu formule; nu conține PDF-uri sau paragrafe comerciale reproduse integral.

### Limite de proveniență și drepturi

Toate verificările din acest lot au fost asistate de modelul din această conversație; **nu au fost lansate sesiuni ale unui agent independent AGENT-029/030/005**, nici verificări Windows/Android și nici modele externe plătite. Principiile fizice sunt documentate la nivel de eșantioane; nu am verificat individual toate propozițiile din 3.464 pagini. Nu am copiat standarde SR/IEC comerciale, scheme ori manuale protejate în GitHub. Dreptul de a citi un fișier încărcat pentru analiză nu este egal cu dreptul de distribuire publică a lui.

**Verdict:** `SOURCE_PRELIMINARY_SCREENING_COMPLETED`, dar `INDEPENDENT_QA_NOT_RUN`; *nu* `MANUALS_FULLY_CERTIFIED`. Pregătire suficientă pentru planificarea trierii întrebărilor fără corecții tacite; **nu** pentru a afirma că toate baremele au fost verificate.
