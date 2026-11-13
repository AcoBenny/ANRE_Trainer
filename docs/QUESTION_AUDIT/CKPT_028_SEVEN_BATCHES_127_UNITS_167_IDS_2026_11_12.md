# CKPT-028 | Seven researched batches, 127 QABC units, 167 ID placements | 2026-11-12

**Repo**: AcoBenny/ANRE_Trainer, audit branch `audit/anre-v8-priority-17-20261109`, PR #7 Draft. No merge, no release, no canonical question/ABC/key changes, no HTML/APK edits.

## What was actually completed in this in-chat execution
From CKPT-026 (11/30, 220/568 units, 285/822 placements), performed preliminary source- and ABC-specific triage in seven **new batches**, without repeating historical checks:
1. `DEEP-ELE-05`: **20 units, 40 placements**. File `DEEP_EXECUTION_2026_11_11/DEEP_ELE_05_ALL_20_SOURCE_AWARE_PRE_QA_2026_11_12.csv`; 13 topical technical source links, 7 exact-source gaps. `G1-ELE-051` passive reciprocity theorem wording is too broad without bilateral/linear assumptions, requires technical QA.
2. `DEEP-ELE-06`: **20 units, 40 placements**. File `DEEP_EXECUTION_2026_11_11/DEEP_ELE_06_ALL_20_FORMULA_PRE_QA_2026_11_12.csv`; 19 topical source links, 1 exact-source gap (`G1-ELE-074` bundled conductor/corona); dimensional and physical premises flagged. Some educational sources were not directly reopened in this session and do not constitute independent proof.
3. `DEEP-NOR-04`: **20 units, 20 placements**. File `DEEP_EXECUTION_2026_11_11/DEEP_NOR_04_ALL_20_SOURCE_SCOPE_ABC_TRIAGE_2026_11_12.csv`; exact I7 paragraph matching, **five candidate key conflicts** `G1-NOR-058 B→C`, `G1-NOR-060 B→C`, `G1-NOR-061 A→B`, `G1-NOR-062 A→B`, `G1-NOR-066 B→A`, and `G1-NOR-071` potential PE/PEN wording trap. Detailed register `QA_RULES/NOR04_FIVE_SOURCE_KEY_CONFLICTS_2026_11_12.csv`. These are NOT changes or approvals, the current normative edition and real expert QA remain gates.
4. `DEEP-LEG-05`: **20 units, 20 placements**. File `DEEP_EXECUTION_2026_11_11/DEEP_LEG_05_ALL_20_OFFICIAL_BIBLIOGRAPHY_ABC_TRIAGE_2026_11_12.csv`, 5 groups x4 original QABC; official ANRE May2023 bibliography PDF, Grade II DA, category Legislație, points3,4,7,8,10 with orders5/2023,59/2013,128/2008,46/2021,66/2023.
5. `DEEP-LEG-06`: **12 units, 12 placements**. File `DEEP_EXECUTION_2026_11_11/DEEP_LEG_06_ALL_12_ANRE_BIBLIOGRAPHY_PRE_QA_2026_11_12.csv`, points11,12,13 with orders134/2021,102/2015,128/2020, all Grade II DA, category Legislație.
6. `DEEP-NOR-06`: **15 units, 15 placements**. File `DEEP_EXECUTION_2026_11_11/DEEP_NOR_06_ALL_15_SOURCE_ABC_TRIAGE_2026_11_12.csv`; 3 exact I7 technical-source and 12 ANRE official bibliography/Grade II placement checks. **`G1-NOR-100`** B=50kΩ intended, but I7 §4.1.5.5.6 says resistance `nu trebuie să fie mai mică` (>=50 kΩ), original stem says `mai mare de` (>50 kΩ). No alteration until linguistic and source-edition QA.
7. `DEEP-NOR-05`: **20 units, 20 placements**. File `DEEP_EXECUTION_2026_11_11/DEEP_NOR_05_ALL_20_SOURCE_ABC_TRIAGE_2026_11_12.csv`; 20 original A/B/C and I7 scoped clause references, including high-confidence I7 §5.4.1 separate lighting/socket, §5.5.7.11 protective earth <=4Ω, §5.2.12.3.7 vertical junction boxes. Four precise source-locator gaps (`G1-NOR-079, 080, 086, 088`) remain unresolved. **`G1-NOR-081` and `G1-NOR-082`** deliberate candidate responses each give only one attribute, whereas I7 §3.0.3.7 on direct contact with combustible material requires BOTH fire-resistant AND flame-retardant cable; source/relevance and conjunction condition require serious linguistic/technical QA. Preserve the intended existing C and B as NOT APPROVED; do not simplify stems/options.

## Anchored sources, with specific limitations
- 2011 I7 published regulation, official Portal Legislativ https://legislatie.just.ro/Public/DetaliiDocument/286763 , indexed and corroborated with searchable ARYA HTML mirror https://www.arya.ro/legislatie/document.php?slug=normativ-i7-2011 . **The amendment chain/current applicability to examination in Nov2026 has not been independently certified**. We did not claim a separate professional reviewer or complete current edition.
- Official ANRE May2023 bibliography document https://anre.ro/wp-content/uploads/2023/05/Tematica-si-bibliografie-pentru-examenul-de-autorizare-electricieni-2023-.pdf ; PDF pages 0/1/2 visually inspected in web source screenshots in this session; official ANRE site linked this bibliography when searched. **Do not claim that this proves it is unchanged for the next exam**, mandatory independent current-edition gate.
- Formula sources include OpenStax, Schneider Electric and IEEE web pages. Their relevance is topical/conditional and links were not exhaustively re-opened one-by-one. **Do not label all 40 electrical theory units as independently verified**.
- Safety-critical distinctions: `PE` versus protective bonding, **conductors** versus underground cables, **joints** versus passing through a building element, **recommended** versus mandatory, **required both conditions** versus one partial attribute, <= versus <.

## Deterministic readback and evidence ledger
Re-fetched all seven CSVs, canonical V73 master, ID_ROUTING_822 and UNITS_568. Checked every original stem, A/B/C text, original key, unit membership, unit hash, routing batch, individual A/B/C preliminary reasoning and explicit no-approval flags. **127/127 rows and 167/167 original placements; zero schema/content mismatches.** This is **deterministic integrity QA only**, not independent technical/source correctness QA. All source/technical/linguistic independent review fields `NOT_RUN` and all `approved_for_learning=NO`.

An early checker expected a single `original_question` field, but two source-aware files used `question_original`. Corrected QA checker to read either explicit schema without changing canonical data; reran and obtained zero errors.

## Cumulative exact progress
- Fully covered for *preliminary ABC/source research* **18/30 deep batches**.
- **347/568** unique QABC units.
- **452/822** original ID placements.
- **0/822** approved for learning by independent source/technical/linguistic QA.
- **12 batches** remain untouched in full deep triage, plus separate edition-source/independent QA for all 822. `DEEP-ELE-07` is next high-efficiency full batch. Do not imply background execution between turns.

## Next action / human collaboration gate
1. Continue clear DEEP-ELE-07 and DEEP-ELE-08 formula questions in follow-up live run; avoid duplicating the seven saved batches.
2. Perform current I7 edition and source QA targeted on the five NOR04 candidate conflicts, NOR05 compound AND condition, NOR06 50kΩ boundary and ELE05 reciprocity assumptions.
3. **Only ask user** to interpret a genuinely undecidable stem after reopening actual source and comparing both meanings; record the response as `USER_HYPOTHESIS`, not a signed-off answer.
