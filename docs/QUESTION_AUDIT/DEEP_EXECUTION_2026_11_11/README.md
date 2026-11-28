# Execuție aprofundată ANRE | 11 noiembrie 2026

Ținta utilizatorului: închiderea verificării tuturor întrebărilor **astăzi**, Europe/Bucharest. Este o țintă de lucru, nu o promisiune că dovezile lipsă vor deveni accesibile până la o anumită oră. Pregătirea prezentă nu adaugă răspunsuri validate.

## Rezultatul urmărit, în trei etape
| Etapă | Lucru concret | Condiție de închidere |
|---|---|---|
| 1. Verificare aprofundată | Paragraf didactic primar, ediție și domeniu; fiecare A/B/C; toate ID-urile și gradele asociate | Un singur răspuns demonstrat sau corecție exactă propusă; sursă și raționament verificabile |
| 2. Adjudecare și corecții | Conflicte, ambiguități, scheme, lipsuri; propuneri înainte/după pentru text/ABC/cheie și explicație | Reviewer distinct confirmă raționamentul și sursa; niciun blocaj documentar/semantic rămas pentru închiderea integrală |
| 3. QA final al băncii | Reconciliere 822 ID-uri, toate deciziile, toate variantele, duplicatelor și edițiilor; dosar agregat de corecții | 822 decizii complete + dovezi QA separat; corecțiile de implementat rămân pentru aprobarea utilizatorului |

Regula existentă rămâne: nu modifica bareme, texte canonice, HTML sau APK. Nicio integrare/merge/release fără acordul cerut. Pregătirea și auditul pot continua autonom; nu cerem aprobări pentru fiecare lot. Nu este necesară aprobarea utilizatorului pentru simpla constatare sau documentarea unei corecții propuse.

## Pornire exactă
1. Citește CKPT010, V95 și `EXECUTION_2026_11_11_SOURCE_REQUIREMENTS.md`. Verifică live PR7 HEAD și ramura înainte de scriere. Scriptul blochează ramura greșită și deriva blobului canonic.
2. Folosește `UNITS_568.csv`, `BATCHES_30.csv`, `ID_ROUTING_822.csv`. Cele 568 unități reprezintă exact Q+A+B+C, fără normalizare lingvistică. Cele 254 grupuri duplicate reduc repetarea cercetării; **fiecare dintre 822 ID-uri are propria decizie**, iar gradele/cheile nu se transferă automat. Cele două grupuri cu chei contradictorii sunt marcate și prioritizate. Nu pot fi închise ca VERIFIED_AS_STORED; o unitate QABC exactă cere aceeași cheie propusă adjudecată. Contexte realmente divergente cer o separare explicită, verificată, înaintea închiderii.
3. Primele loturi simultane: `DEEP-ELE-01`, `DEEP-NOR-01`, `DEEP-LEG-01`; apoi `DEEP-ELE-02`. Împreună includ toate cele 66 unități cu risc P0, aferente celor72 ID-uri P0. Restul loturilor continuă în ordinea riscului din manifest. Lotul este unitate de alocare; o întrebare poate fi trimisă la QA imediat ce are dovezi complete.

```bash
python docs/QUESTION_AUDIT/deep_audit_execution.py batch DEEP-ELE-01
python docs/QUESTION_AUDIT/deep_audit_execution.py validate /absolute/path/DEEP-ELE-01.json
python docs/QUESTION_AUDIT/deep_audit_execution.py final-check /absolute/path/completed_batches
```

Exportul furnizează textul original, toate opțiunile, cheile și explicațiile originale per ID, grade/sursă/rând și dovezile existente din V95. Pentru o unitate deja cercetată, se completează exact lacuna rămasă și se reutilizează dovezile confirmate. Nu se reface inventarul sau screeningul pentru a raporta progres nou.

## Echipă și succesiune
| Responsabilitate | Alocare în sesiunea de execuție | Dovadă obligatorie |
|---|---|---|
| Electrotehnică | 1 autor | Formule/ipoteze, manual universitar/autori/fabricanți; locator precis |
| Norme | 1 autor | Text normativ, amendamente/tranziții și aplicabilitate |
| Legislație | 1 autor | Articol exact și formă temporală aplicabilă; comparație cu banca istorică |
| QA independent | 2 revieweri distincți de autori | Propria consultare a sursei, verificarea ABC/capcanelor și verdict argumentat |
| Coordonare/date | 1 coordonator | Alocare fără suprapunere, reconciliere, commit și checkpoint |

Acestea sunt roluri de executat în audit, nu afirmația că30 loturi ori noi agenți au fost deja executați. QA include control lingvistic explicit: numai/orice/poate/trebuie, negații, referent, excepții și comparații. Pentru dispută tehnică, reviewerul nu acceptă concluzia autorului prin simpla recitire; reconstruiește dovada. Review AI separat se etichetează ca atare, fără expertiză umană sau aprobare oficială inventată.

## Criterii per unitate și per ID
1. **Sursă:** locator exact, ediție, domeniu și aplicabilitate la examen; acces primar real și referință durabilă. O grilă veche sau un rezultat de căutare nu constituie justificare didactică. Derivarea este permisă dacă baza primară și ipotezele sunt explicite.
2. **Decizie:** raționament pentru A, B și C; unicitate demonstrată în formularea originală ori într-o propunere exactă de corectare; verificarea fiecărui ID/grad, a cheii originale și a explicației existente. Ambiguitatea se rezolvă prin dovadă/formulare precisă, nu prin alegerea automată a altei litere.
3. **QA:** reviewer distinct, sursă redeschisă, rezultat și dovada review-ului. `BLOCKED_*` este rezultat de cercetare, dar nu întrebare închisă. Nicio rată de acoperire nu înlocuiește aceste criterii.

Rezultatele se salvează ca JSON per lot: `batch_id`, `results` cu un rând per `unit_id`. Câmpurile obligatorii sunt implementate în validator: `qabc_sha256`, `author`, `reviewer`, `review_status`, `status`, `members`. Pentru închidere: `ABC` cu A/B/C argumentate, `source_reference`, `exact_locator`, `edition`, `source_kind`, `source_opened`, `edition_verified`, `exam_applicability_verified`, `reviewer_reopened_source`, `single_answer_demonstrated`, `reviewer_evidence_ref`, `linguistic_findings`, `technical_adjudication`. Fiecare membru are `ID`, `original_key`, `proposed_key`, `grade_applicability`, `explanation_assessment`, `key_change_authorized: NO`, `approved_for_learning: NO`; corecțiile au suplimentar `exact_correction_before_after` și `proposed_explanation` susținută de sursă. Cazurile blocate au `blocker` și `next_action`.

Statusuri admise: `VERIFIED_AS_STORED`, `CORRECTION_READY_REVIEWED`, `BLOCKED_SOURCE`, `BLOCKED_EDITION`, `BLOCKED_DIAGRAM`, `BLOCKED_AMBIGUITY`. Rezultatul `CORRECTION_READY_REVIEWED` înseamnă propunere verificată, încă neaplicată; aplicația veche nu devine sigură prin existența propunerii. Validatorul verifică structura și consistența, **nu adevărul fizic/juridic sau autenticitatea declarațiilor reviewerului**.

## Ritm pentru ținta de astăzi
1. Prima serie de loturi stabilește capacitatea reală de închidere. Se măsoară întrebări decise și acceptate de QA, nu numai pagini citite ori fișe create. Nu se inventează acum o estimare de ore/întrebare fără această măsurare.
2. Flux continuu autor→QA→adjudecare. Sursele din aceeași familie se consultă împreună; disputa/lipsa unei surse se trimite imediat într-o coadă separată, în timp ce restul întrebărilor continuă. Salvare după fiecare lot încheiat sau blocaj important, pe ramura auditului.
3. La sfârșit se publică dosarul agregat de decizii și corecții pentru aprobare. Dacă o dovadă obligatorie rămâne lipsă, banca integrală rămâne neînchisă; termenul nu justifică aprobarea unei întrebări neverificate. Se solicită intervenție doar pentru un document indispensabil nerecuperabil sau aprobarea unei modificări concrete.

Fără worker persistent configurat, lucrul are loc în sesiuni active. Nu a fost creată o automatizare și nu se promite execuție după încheierea răspunsului. Acest pachet permite pornirea directă, fără altă etapă de organizare.
