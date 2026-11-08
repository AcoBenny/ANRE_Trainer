# ANRE Trainer | Audit complet al inventarului și navigării manualelor didactice

**Data:** 8 noiembrie 2026  
**Mod:** numai audit și indexare. Implementarea HTML/APK și baremele existente rămân înghețate.  
**Control:** metadate, pagini, cuprinsuri, coduri de concepte și duplicări. Nu redistribuim manualele.

## Rezultatul realizat în această etapă

| Indicator | Număr | Ce reprezintă |
|---|---:|---|
| PDF-uri originale | **14** | Inclusiv trei variante duplicate / parțial duplicate |
| Pagini în toate fișierele | **4.120** | Paginile enumerate în PDF-uri, inclusiv duplicatele |
| Lucrări/surse canonice distincte | **11** | Unificare pe sursă, nu ștergerea originalelor |
| Pagini ale surselor canonice | **3.464** | Fiecare are înregistrare de navigare în CSV |
| Pagini canonice cu text căutabil | **3.050** | Analizate automat în indexul pe concepte |
| Pagini fără text căutabil | **414** | 332 în manualul scanat din 1995, alte 82 în pagini mixte/grafice/goale |
| Repere de secțiune/capitol | **2.010** | 880 ancore din marcaje/cuprins + 1.130 candidați din text, cu status diferențiat |
| Categorii urmărite | **45** | Taxonomie de căutare tehnică; NU 45 domenii validate complet |
| Asocieri între surse și concepte | **289** | 271 localizări prin termeni + 18 navigări prin cuprinsul scanat |
| Rânduri de corespondență între copii | **656** | Arată sursa canonică și pagina echivalentă |
| Mapări exacte aprobate independent | **0** | Urmează auditul semantic pe paragrafe și actualitatea normelor |

## Identificarea corectă a celor trei variante duplicate

1. **I7-2011 (2023), două copii × 249 pagini:** hash identic; aceeași pagină 1..249.
2. **Curs Electrotehnică, 258 pagini** și **Pregătirea tehnică, 257 pagini:** cele 257 pagini aliniate sunt vizual aproape identice; ultima pagină din exemplarul mai lung este aproape goală. Sursa canonică este cea de 257 pagini, cu text parțial căutabil.
3. **Manual autorizare scanat, 149 pagini** reprezintă un fragment foto cu câte două pagini din **Manual pentru autorizarea electricienilor instalatori, 332 pagini (1995)**. Am confruntat visual exemplare din cele 11 poziții eșantionate și am confirmat corespondențele fotografiate inclusiv la paginile 45, 80 și 120. Formula de navigare inferată: pagina PDF foto n corespunde paginilor PDF 2n+32 și 2n+33 în sursa canonică (n=1..149). Nu afirmăm că fiecare dintre cele 149 fotografii a fost verificată individual.

## Inventarul surselor canonice

| Cod | Titlu/scop | Paginile PDF | Index |
|---|---|---:|---|
| PREG | Pregătirea tehnică pentru autorizarea electricienilor | 257 | Text + cuprins; teoria de bază |
| MAS | Mașini electrice | 309 | Text + cuprins/bookmark; transformatoare și mașini |
| UTCN | Circuite electrice trifazate (2021) | 114 | Text + tematică slides; verificare pagini pentru formule |
| STATII | Cartea electricianului din stații și PT-uri | 609 | Text + cuprins; istoric, util pentru schemă și protecții |
| IEC | Manualul instalațiilor electrice Schneider/CEI | 432 | Text + 371 repere bookmark valide; ghid tehnic, ediție 2007 |
| I7 | Normativ I7-2011, formă sintetizată la 22.09.2023 | 249 | Text indexat; validitatea în 2026 trebuie verificată |
| I7OLD | Normativ I7-02 / instalații până la 1000 V | 271 | Text indexat; **istoric, nu normativ curent** |
| AUT_1995 | Manual de autorizare instalatori, ediție istorică | 332 | Cuprins vizual și repere de pagini; fără text integral căutabil |
| SCHNEIDER24 | Ghidul electricianului Schneider 2024 | 794 | Categorii și pagini; **catalog produse, nu manual normativ** |
| FINDER | Scheme de legătură, relee și automatizări Finder | 86 | Cuprins și pagini; **catalog de soluții** |
| SSM | Instrucțiune internă pentru autorizarea electricienilor SSM | 11 | Text; **regulă internă, nu regulament ANRE** |

## Ce conține pachetul

- `MANUAL_SOURCE_MANIFEST_2026_11_08.json`: toate cele 14 fișiere, rol, pagini, SHA-256, autoritate și blocaje.
- `MANUAL_CHAPTER_SECTION_INDEX_2026_11_08.csv`: 2.010 repere pagină/capitol cu metoda de extragere și nivelul de încredere. 1.130 sunt detectate automat și **nu pot fi considerate titluri confirmate** fără revizuire.
- `MANUAL_ALL_PRIMARY_PAGES_NAVIGATION_2026_11_08.csv`: 3.464 rânduri, câte unul pentru fiecare pagină canonică, cu capitolul navigabil și codurile tematice detectate.
- `MANUAL_CONCEPT_LOCATOR_ALL_2026_11_08.csv`: 289 mapări sursă–concept și listele exacte ale paginilor candidate, distingând text căutabil de cuprins vizual.
- `MANUAL_45_CONCEPT_COVERAGE_MATRIX_2026_11_08.csv`: matricea pe 45 de concepte și 11 surse, destinată identificării lacunelor.
- `MANUAL_DUPLICATE_PAGE_CROSSWALK_2026_11_08.csv`: cele 656 de pagini din cele trei copii, legate de sursele canonice.
- `MANUAL_PAGE_TOPIC_INDEX_2026_11_08.json.gz`: index comprimat de pagini, fără textul integral al cărților.
- `MANUAL_COVERAGE_GAPS_2026_11_08.csv`: lacunele și verificările restante.

## Ce NU înseamnă „indexat”

- Nu înseamnă că fiecare dintre cele 3.464 pagini a fost citită și aprobată semantic de un specialist independent.
- Nu înseamnă că toate cele 822 de întrebări au fost asociate cu paragrafe exacte sau că răspunsurile lor sunt corecte.
- Nu înseamnă că PDF-urile sunt licențiate pentru redistribuire offline în aplicație.
- Nu înseamnă că ediția 2023 a normativului I7 reflectă toate modificările aplicabile în noiembrie 2026.
- Manualul scanat AUT_1995 are toate paginile localizate la nivel de capitol, nu la nivel de paragraf OCR. OCR complet nu a fost rulat, evitând introducerea unor erori de recunoaștere în sursa tehnică.

## Etapa de audit rămasă înainte de întrebări

1. **QA al indexului didactic**: validăm reperele automate cu risc ridicat, formulele și paginile de interes, fără a modifica întrebările.
2. **Analiza lacunelor de surse**: completăm domeniile fără tratament exact, folosind materiale publice/autorizate, normative în ediții în vigoare și fragmentare corectă.
3. **Drepturi offline**: stabilim ce poate fi stocat integral, ce poate fi citat contextual și ce trebuie explicat în text propriu cu trimitere la sursă.
4. **Abia apoi** începem maparea și auditul celor 822 de întrebări și al colecțiilor din Lotul 2, cu specialist lingvistic AGENT-031 și auditor tehnic.

**Statut proiect:** biblioteca este inventariată și navigabilă integral la nivel de fișier/pagină, **dar maparea didactică exactă, aprobată, nu este încheiată**. Acesta este un registru de lucru fundamentat, nu acceptarea finală pentru implementare. CKPT-002 rămâne ultimul checkpoint; raportul este un jurnal de progres, nu checkpoint nou. Cost suplimentar: 0 lei.
