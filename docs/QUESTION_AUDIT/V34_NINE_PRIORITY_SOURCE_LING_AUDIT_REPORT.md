# ANRE Trainer | V34 | 9 conflicte prioritare verificate pe surse și logică (fără modificări de barem)

**Data:** 2026-11-11. **PR:** #7 Draft, `audit/anre-v8-priority-17-20261109`. **Bază canonică:** V10.29, blob GitHub `bc5b5a61954ba138cf83987bfc932eca517f3b21`; **822 ID-uri**, întrebări, A/B/C și chei originale nemodificate. Acest audit adaugă **9 cazuri** după cele 4 din V33, total **13 cazuri cu un nou control individual**. Acestea **NU** sunt 13 aprobări independente.

## Metoda / verificările efective
- Am reextras cele 9 înregistrări din blobul canonic (exact `ID`, enunț, `A/B/C`, cheie, fișier și rând original) și am confruntat cu cele șase dezacorduri V13 și analiza istorică V25.
- Pentru legislație am căutat exact articolele pe Portalul Legislativ și, unde sunt disponibile, versiunile din 2023 și ediția din 2026. Accesul integral la `legislatie.just.ro` este intermitent (502/timeouts); textele oficiale indexate au susținut majoritatea prevederilor de mai jos, dar **nu se pretinde auditul exhaustiv al tuturor modificărilor**.
- Pentru electrotehnică am refăcut deducția matematică și am consultat un manual tehnic de producător și NTE 009/10/00. PDF-ul academic Pearșică (2004) a dat HTTP 502 în accesarea nouă; pagina PDF-ului ABB a fost citită textual, însă captura/screenshot a returnat `cache miss`. **Nu afirmăm QA vizual pe acele pagini.**
- Am inclus un audit lingvistic de text (condiții, cuantificatori, „este de preferat”, „chiar dacă”, „în cazul în care”), **nu un lingvist uman sau agent independent executat**.
- **Nicio cheie, întrebare, variantă, explicație HTML, APK sau fișier main nu a fost modificat**.

## 1. Legislație, Grad I (5 întrebări)

### G1-LEG-024 | actual A | candidat C, dar numai provizoriu
**Original:** „Obținerea avizului tehnic de racordare de către un utilizator”; A: „nu este obligatorie pentru o durată mai mică de 6 luni”; B: „nu este obligatorie pentru o putere cerută sub 100 kW”; C: „este obligatorie pentru orice loc de consum/producere nou”.

**Sursă:** Regulamentul de racordare, Ordin ANRE 59/2013, art. 9 și 11, https://legislatie.just.ro/Public/DetaliiDocumentAfis/297330; istoric oficial cu modificări până la **25 mai 2026**. Regula principală pentru racordarea unui loc nou nu introduce, în fragmentele consultate, o scutire generală pentru durata sub 6 luni/putere sub 100 kW. **Lipsă:** verificare exhaustivă a tuturor excepțiilor de racordare temporară și a versiunii exact aplicabile în mai 2023. Nu certificăm absolutul „orice” doar printr-un articol general. **STATUS: `HOLD_TEMPORARY_EXCEPTION_VERSION_QA`.**

### G1-LEG-028 | actual B | candidat C susținut de textul oficial
**Original:** pentru un „ansamblu de blocuri de locuințe” unde se poziționează grupurile de măsurare individuale? B = limita de proprietate în exterior; C = la parter sau pe palier.

**Sursă:** Ordin 59/2013, Regulament, **Anexa 3, pct. 2.2–2.3**: https://legislatie.just.ro/Public/FormaPrintabila/00000G274VNG8B51XKX3UZLHX8NOAPLU . Textul separă ansamblurile de *blocuri* (contoare centralizat, la parter/palier) de locuințele *individuale* (limită de proprietate). **STATUS: `DIRECT_OFFICIAL_TEXT_SUPPORTS_C_PRELIMINARY`.** Necesită QA de ediție și reviewer independent înainte de corecție.

### G1-LEG-032 | actual B | candidat A, condiționat de temeiul juridic concret
**Original:** când poate ANRE sancționa contravențional un electrician? A comiterea unei fapte interzise prin regulament; B exercitarea activității cu adeverință/legitimație emisă de 4 ani; C proiectarea unei instalații de locuință cu autorizație IIA.

**Sursa I:** Regulament ANRE 66/2023 art. **18(1)** și **30(1)**, https://legislatie.just.ro/Public/DetaliiDocumentAfis/288046 : calitatea se vizează la **5 ani**. Simplul fapt că documentul are **4 ani** nu este contravenție.
**Sursa II:** Legea 123/2012 art. **93(1)**, pct. 5^3 și conexe, https://legislatie.just.ro/Public/FormaPrintabila/00000G12J5P7C0HD82V2KWJDW0ZKWG0D : nerespectarea ordinelor/deciziilor ANRE poate constitui contravenție; Regulament 66/2023 **art. 41** stabilește procedura de constatare și sancționare. Existența unei norme de interdicție în regulament nu demonstrează automat că **orice** faptă este sancționabilă fără identificarea elementului contravențional și a competenței.
**STATUS: `A_MORE_PLAUSIBLE;_LEGAL_ELEMENT_QA_PENDING`.**

### G1-LEG-034 | actual B | candidat A susținut direct
**Original:** electrician autorizat care execută lucrări; A obligat să respecte proiectul; B obligat să participe la recepție/PIF **chiar dacă nu i se solicită**.
**Sursă:** Ordin 66/2023 art. **37 lit. e/h**, https://legislatie.just.ro/Public/DetaliiDocumentAfis/288046 . Lit. e: respectarea proiectului este obligație. Lit. h: participarea la recepție/PIF **în cazul în care i se solicită**. B schimbă nepermis condiția; A reproduce obligația.
**STATUS: `DIRECT_OFFICIAL_TEXT_SUPPORTS_A_PRELIMINARY`.**

### G1-LEG-048 | actual A | candidat B susținut direct
**Original:** A posibilitatea de a impune orice modalitate de plată neofertată; B alegerea oricărei metode puse la dispoziție de furnizor.
**Sursă:** Legea 123/2012 art. **57(2)**, https://legislatie.just.ro/Public/DetaliiDocument/280321 : clientul casnic poate selecta dintre metodele oferite de furnizor. Nu rezultă dreptul de a impune metode neofertate.
**STATUS: `DIRECT_OFFICIAL_TEXT_SUPPORTS_B_PRELIMINARY`.**

## 2. Electrotehnică, perechi duplicate Grad I/II (4 înregistrări)

### G1-ELE-018 (A) vs G2-ELEC-170 (C)
**Original, identic la ambele:** linie electrică aeriană trifazată simetrică, C12=C23=C31=C, influența pământului neglijată; opțiunile sunt A: `Cs=3C`, B: `Cs=C/3`, C: `Cs=C`. Ambele provin din `ELECTROTEHNICA-09.2024-2.xlsx`, **rând 25**. Chei diferite pentru text, variante și rând **identice** => contradicție demonstrabilă fără expertiză suplimentară.

**Calcul propriu** sub ipoteza sistemului trifazat simetric echilibrat:
`q1 = C(U1-U2)+C(U1-U3)=C(2U1-U2-U3)`. Din `U1+U2+U3=0` rezultă `q1=3CU1`, deci `Cs=3C`. În această convenție **A** este susținut, C nu. Un chestionar web reproduce 3C dar **NU** este bază didactică independentă. Trebuie localizată definiția explicită a `Cs` în cursul universitar (Pearsică 2004, pag. tipărită 70), care nu a fost inspectat vizual în această sesiune: https://www.afahc.ro/ro/facultate/cursuri/electro_b.pdf (HTTP 502).
**STATUS: `DUPLICATE_OPPOSITE_KEYS + MATH_A_PRELIMINARY;_TEXTBOOK_PAGE_AND_SME_QA_PENDING`.**

### G1-ELE-102 (A) vs G2-ELEC-245 (C)
**Original, identic la ambele:** schema cu două bare colectoare și un întreruptor/circuit; opțiunile A: o bară sub tensiune, cealaltă rezervă rece; B: ambele alimentate cu cupla conectată; C: ambele alimentate, cupla transversală în rezervă caldă. Sursă comună `ELECTROTEHNICA-09.2024-2.xlsx`, **rând 109**. Identitate textuală+ABC+rând, dar chei A vs C: dezacord factual automat detectabil.

**Dovezi didactice și de exploatare:** ABB *Distribution Automation Handbook*, §**3.14.1.4**, pag. 8–9, spune că, într-un mod uzual de operare cu **două bare**, cupla este **deschisă**, iar circuitele sunt distribuite pe ambele bare. Cupla servește transferului între bare. https://library.e.abb.com/public/7dca4ffad2206d36c1257be30048d4be/DAHandbook_Section_3_Power_distribution_systems_757959_ENa.pdf . NTE 009/10/00 definește `rezervă caldă` și admite configurații în funcție de schema normală: https://legislatie.just.ro/Public/DetaliiDocument/122751 . 
**Interpretare:** configurația uzuală a sursei ABB este **compatibilă cu C**, dar „este de preferat” fără criterii de fiabilitate, regim protecții, nivel de tensiune, schemă și automatizări **nu stabilește universal o singură cheie**. Screenshot PDF ABB a eșuat (`cache miss`), a fost inspectat **numai textul**, nu figura. 
**STATUS: `EXACT_DUPLICATE_OPPOSITE_KEYS + C_DIDACTIC_CANDIDATE;_TECH_SCOPE/DIAGRAM_SME_PENDING`.**

## Sinteză numerică V34
- **9/9 ID-uri** confruntate cu surse oficiale sau calcule / materiale didactice relevante.
- **3** întrebări de legislație cu contradicții foarte clare față de textul oficial: `G1-LEG-028`, `034`, `048`.
- **2** întrebări legislative cu risc/excepții încă deschise: `024`, `032`.
- **2 perechi** identice Grad I/II cu bareme contradictorii: **4** înregistrări, fără corectare încă.
- Împreună cu V33 (4 ID-uri), acum există **13** ID-uri prioritare reevaluate individual prin surse/raționament. **0 aprobări QA independente** și **0 corecții automate**. Celelalte **809** ID-uri rămân la nivelurile existente ale triajului preliminar, fără audit nou la aceeași profunzime.

## Gate de aprobare
1. Auditor de surse juridice: confirmarea edițiilor la data întrebării (mai 2023) și prezent (noiembrie 2026), plus derogările pentru ATR și elementele sancțiunii.
2. Expert electrotehnic: definirea `Cs` dintr-o sursă academică verificată și schema de exploatare cu două bare; QA lingvistic independent pentru „numai”, „orice”, „este de preferat”.
3. QA aplicație: verificare cheie+explanations+persistent mistakes+local anchors după **aprobarea explicită** a utilizatorului. Nu schimba `HTML`, `APK`, întrebări, opțiuni sau chei în această etapă.

**Politică GitHub:** numai documente `docs/QUESTION_AUDIT` și jurnal în PR #7 Draft, fără merge în `main`, fără release/build Actions inutile.
