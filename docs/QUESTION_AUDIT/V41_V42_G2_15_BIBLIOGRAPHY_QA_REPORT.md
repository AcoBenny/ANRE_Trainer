# ANRE Trainer | V41–V42 | 15 înregistrări Grade II derivate din bibliografie
Data: 2026-11-11. Baza canonică: V10.29 blob `bc5b5a61954ba138cf83987bfc932eca517f3b21`.

## Sursă originală inspectată efectiv
**ANRE, `Tematica şi bibliografie pentru examenul de autorizare electricieni`, mai 2023**, paginile **2 şi 3**, la punctele 14 (I7), 22 (PE 102/1986), 29 (PE 155/1992), inclusiv coloana de aplicabilitate Grad II (DA):
https://anre.ro/wp-content/uploads/2023/05/Tematica-si-bibliografie-pentru-examenul-de-autorizare-electricieni-2023-.pdf
PDF-ul oficial a fost atât citit textual, cât şi inspectat prin captură vizuală a paginilor 2 şi 3. Pentru I7, actul de aprobare este Ordinul MDRT **2741/2011**: https://legislatie.just.ro/Public/DetaliiDocumentAfis/287131 . Pentru PE102 și PE155 documentul ANRE afișează **indicativele**, nu acte de aprobare echivalente cu acestea.

## Audit
- **15/15** ID-uri reale: `G2-NORM-001–003` plus `G2-NOR-136–147`; toate păstrează exact A/B/C, cheile A, fişierul/rândul canonic.
- **12/15** întrebări de recunoaștere a unui cod, aplicabilității sau a domeniului "Norme tehnice" sunt concordante cu **tabelul bibliografic 2023**, dar NU reprezintă o verificare a conținutului normativ şi **nu există dovadă că provin din exemplele oficiale ANRE de întrebări grilă**.
- **3/15 conțin o eroare de categorie logică, fără variantă corectă:**
  1. `G2-NOR-137`: „Prin ce act este aprobat ... I7?” A/B/C oferă `I7-2011`, `PE102`, `PE155`, niciuna nu oferă **Ordinul 2741/2011**;
  2. `G2-NOR-141`: „Prin ce act este aprobat ... PE102?” A/B/C oferă doar **indicative de normative**, nu un act aprobator;
  3. `G2-NOR-145`: aceeași problemă pentru **PE155**.
- Toate cele 15 au **cheia A**; acest tipar este un indiciu de construcție sintetică, NU o probă de proveniență oficială. Ele trebuie marcate `DERIVED_BIBLIOGRAPHY_ONLY`, fără a fi livrate ca întrebări de examen verificate până la controlul originalului.
- Registrul integral cu toate formulările originale și toate variantele: `V41_V42_G2_15_BIBLIOGRAPHY_QA.csv`.

## Ce nu a fost verificat
Nu s-au descărcat/analizat fişierele oficiale XLSX `NORME-TEHNICE-Gr.-2-05.2023.xlsx` în această sesiune; legătura oficială este publică, dar accesul la binar a eșuat în mediul curent. QA independent electrotehnic/lingvistic `NOT_RUN`; 2026 bibliografie actualizată exhaustiv `NOT_DONE`. Nu se schimbă cheile; raportul este **evidență de audit**, nu finalizare a lotului pentru release.
