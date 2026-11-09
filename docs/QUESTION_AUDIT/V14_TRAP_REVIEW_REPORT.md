# V14 | ANRE trap-language audit: six historical canonical/tracker conflicts

Date 2026-11-09. Scope: `G1-LEG-024/028/032/034/048`, `G2-ELEC-170`. Reviewed exact questions and A/B/C from canonical V10.29 GitHub blob `bc5b5a61954ba138cf83987bfc932eca517f3b21` alongside keys in `V13_SIX_KEY_CONFLICTS.csv`. Applied installed `anre-question-bank-qa` and `anre-source-audit` specialist checklists; **no autonomous independent linguistic reviewer was executed**. All results are model-assisted and subject to independent QA.

## The trap distinction

A *legitimate trap* tests a legally/technically decisive modifier under an unambiguous rule. A *broken item* presents no unambiguous correct option or attaches the key to a false clause. **A trap label never licenses an unsupported answer.** Compare each option's exact words with the governing norm and its edition.

| ID | Canonical / V9 tracker | Decisive clause | Evidence-based provisional result |
|---|---|---|---|
| G1-LEG-024 | A / C | „nu ... mai mică de 6 luni”; „orice loc ... nou” | NO_CONCLUSIVE_EXCEPTION_FOUND |
| G1-LEG-028 | B / C | „ansamblu de blocuri”; „la parter sau pe palier” versus „la limita proprietății” | OFFICIAL_TEXT_SUPPORTS_TRACKER_C |
| G1-LEG-032 | B / A | „emisă în urmă cu 4 ani”; „comiterea unei fapte ... interzisă” | OFFICIAL_TEXT_DISPROVES_AGE_AS_AUTOMATIC_OFFENCE |
| G1-LEG-034 | B / A | „chiar dacă nu i se solicită” versus obligația de a respecta proiectul | OFFICIAL_TEXT_SUPPORTS_TRACKER_A |
| G1-LEG-048 | A / B | „orice ... chiar dacă nu ... pusă la dispoziție” versus „pe care furnizorul o pune la dispoziție” | OFFICIAL_TEXT_SUPPORTS_TRACKER_B |
| G2-ELEC-170 | C / A | „capacitate de serviciu Cs”; „C12=C23=C31”; „neglijând influența pământului” | CONFLICTING_PRIOR_AUDIT_AND_UNVERIFIED_DEFINITION |

## Source excerpts and findings

### G1-LEG-028
Official 2013 Regulation annex 2.3 states for **an ensemble of apartment blocks** that individual meters are placed **centrally, on ground floor or on landing**. This is option C (tracker); canonical B offers a different property-boundary setting. The words „ansamblu de blocuri” are essential. Source https://legislatie.just.ro/Public/FormaPrintabila/00000G35R333SFHRDTH1XD6JRTZOZBPD , annex pct 2.3. Status: official-source support for C; **not authorization to change answer**.

### G1-LEG-032
ANRE says authorization is unlimited but requires renewal/visa at **5 years**, so document issued **4 years ago** is not automatically invalid: https://anre.ro/participanti-la-piata-de-energie/persoane-fizice/energie-electrica/electricieni/examene/ . Option B's number 4 is the trap. Option A (an act prohibited under authorization rules) is the defensible candidate, pending exact sanctions article and version. Canonical B is questionable; independently adjudicate.

### G1-LEG-034
Order 66/2023 regulation art.37(e) obliges electricians to **respect the project** (A); art.37(h) requires participation at reception and commissioning **if requested**. Canonical B instead says „chiar dacă nu i se solicită”. Exactly inverted legal condition. Source https://legislatie.just.ro/Public/DetaliiDocumentAfis/288046 . Strong provisional support for tracker A.

### G1-LEG-048
Law 123/2012 art.57(2) lets consumers select **among payment options provided**. Option A incorrectly permits imposing arbitrary unoffered methods. Source https://legislatie.just.ro/Public/DetaliiDocument/280321 . Strong provisional support for tracker B.

### G1-LEG-024
Option A contains **„sub 6 luni”** exception while C has **„orice”** new connection; no exact authoritative paragraph proving the 6-month exemption was identified in this check. Need original May 2023 rule and exceptions before deciding. Useful background https://legislatie.just.ro/Public/DetaliiDocument/160289 . Do not assume A/C solely from words.

### G2-ELEC-170
The canonical HTML audit claims A→C correction on a secondary external cross-reference, but does not identify a precise didactic paragraph. The earlier V9 physical derivation gives Cs=3C in one equivalent model, but the *definition of service capacitance* and whether C12 etc are partial capacitances require the original reference. Not resolved by language screening alone; classify **DEFINITION_DEPENDENT**.

## Why the earlier application badge is insufficient

All six in V10.29 have status `VERIFICAT TEHNIC` or historical badges. Yet the embedded justification of LEG-024/032/034/048 mostly asserts the selected letter without citing a legal article. Prior `capcana_lingvistica` flags were empty in **five** of the six, despite decisive modifier traps; for G1-LEG-028 the app already flags a condition but selects B even though cited official context supports C. These flags are **not an independent certification**.

## Gate / next actions

- [x] Exact A/B/C and historical key from canonical HTML inspected; compared against V9 tracker.
- [x] Legal text identified for 028, 032 (5-year interval), 034, 048 with direct public references.
- [ ] Edition-specific 2023 sanctions wording, ATR exceptions, and the technical definition of Cs.
- [ ] Independent electrical and legal/linguistic QA.
- [ ] Original workbook answer-key provenance and historical correction trace.
- [ ] Any change to HTML, question, answer key, APK, main or release requires explicit user approval.

No answers or app files changed. The 6 entries remain in quarantine for adjudication. This V14 is a focused re-audit, **not an additional 50 screened questions**.
