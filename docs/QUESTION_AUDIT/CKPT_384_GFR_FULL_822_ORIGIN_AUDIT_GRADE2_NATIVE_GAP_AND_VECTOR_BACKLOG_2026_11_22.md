# CKPT-384 | GFR: 822-route origin and integrity QA + Grade II original workbook reconciliation

Date: 2026-11-22. Branch: `audit/anre-v8-priority-17-20261109`. Parent CKPT-383. No canonical, key, HTML, APK, release or PR merge changes.

## Newly completed deterministic audits

**V294:** [full 568 QABC record structural matrix](./V294_GFR_568_ORIGIN_822_KEYS_415_XLSX_153_DIDACTIC_BIAS_11_SOURCE_ORPHANS_2026_11_22.json).
- All **568 QABC** map to **822 grade routes** with grade ID, imported letter, source class, queue and no missing question/A/B/C fields, duplicate options or cross-master imported-key mapping mismatches. V283 count remains **P0 27 + P1 2 + P2 793**.
- **415 original Excel-source QABC groups / 669 grade routes:** source-native questions + all three option texts were read directly from the original workbook files, compared with V141 after Unicode NFKD, case and whitespace normalization, per-field concatenation with a divider and a deterministic FNV32 digest. **411/415 fully matching** fingerprints; **4/415 materially different QABC groups** already known: `QABC-0143, QABC-0236, QABC-0362, QABC-0386`, representing **5 materially altered grade routes**. The `QABC-0145` numeric workbook options are natively numeric but text-display equivalent in both grade routes. Source workbook SHA256 pins and detailed original options in V292/CKPT-381. FNV32 is a compact integrity fingerprint, not a cryptographic signature or certified answer validation.
- **153 teaching-only, non-original-XLSX G2 QABC groups / 153 grade routes:** **all 153 imported keys equal A** (0 B, 0 C). This is a confirmed *answer-position distribution hazard in the source master*; actual UI option randomization NOT yet tested. No changes to barems or choices. These lessons should remain labeled **didactic, not authentic 2023 original question bank**.

**V295:** [full 304 native G2 workbook row matching index](./V295_GFR_NATIVE_G2_304_EXACT_ABC_AND_FUZZY_COVERAGE_2026_11_22.json).
- Physically reopened original **G2 legislation XLSX (103 rows)** and **G2 norms XLSX (201 rows)**; original-user-owned full A/B/C data is preserved in a *separate private session CSV*, **not uploaded to public GitHub**.
- Compared all **304 original G2 source rows** with G1 original worksheet A/B/C: **149 rows with exactly the same stem AND A/B/C**, **6 rows with same stem but different A/B/C** (candidate key scope can change), **149 rows without an exact stem match** in G1 sources. The latter have **136 distinct normalized stems (44 law, 92 technical norms)**.
- Secondary screen: compare the 149 G2 non-G1 matched original source stems against all **568 V141 QABC** via char-trigram Dice. **1 similarity ≥0.90; 4 in [0.75,0.90); 19 in [0.55,0.75); 125 below 0.55.** Similarity is not legal/technical equivalence; do NOT infer 149 proven missing exam questions or auto-merge. The 149-row **source-completeness investigation is distinct** from the 153 separately constructed G2 didactic questions.
- The 6 same-stem-but-different-ABC original G2 rows demand strict source-variant and correct-letter review. Do not deduplicate by stem.

**V296:** [11 unmapped source rows plus embedded vector drawing mapping](./V296_GFR_11_ELECTRO_NATIVE_ROWS_VECTOR_DRAWING_SOURCE_2026_11_22.json).
- The original Electrotehnică Excel has **275 original stem rows** (8..282), but only **264 distinct source rows** map to V141: **11 exact source-row omissions**, source rows `15,30,31,32,39,43,44,65,117,176,181`.
- **2 text-only (39,65)** and **9 figure dependent**. Three (30,31,32) have blank spreadsheet B/C/D cells because the option diagrams are vector drawings. Important correction: Excel archive has **zero bitmap files** but `xl/drawings/drawing1.xml` includes **477 true grouped vector shapes** distributed in **256 two-cell anchors**, with **330 shapes anchored to the nine figure-dependent unrepresented rows**. The diagrams exist, they are **not lost**, but `artifact_tool` render of A30:D30 and A31:D31 did not render vector alternatives, so the correct schematic/choice is NOT identified.
- Original Excel SHA-256 unchanged.

## Official 2026 fee/edition crosscheck, not new key certification

Two didactic source citations are time-mislabeled in V141:
- `QABC-0555` Grade II A/B tariff `250 lei`, imported A; and `QABC-0556` Grade II A+B `500 lei`, imported A. Their `source_workbook` metadata cites `ANRE Ordin 118/2023`, which regulated **2024**, not 2026.
- The ANRE official [spring 2026 exam notice](https://anre.ro/wp-content/uploads/2026/01/Anunt-sesiune-P2026-2.pdf) expressly identifies **Ordin 82/2025** as the **2026 fees authority**. The tariff amounts currently still match **250/500**, as reproduced on ANRE's [electrician page](https://anre.ro/participanti-la-piata-de-energie/persoane-fizice/energie-electrica/) and the [legal text](https://legislatie.just.ro/Public/DetaliiDocument/305643).
- **Research correction needed in citations/edition metadata, not answer letters**. No evidence of a 2026 *official scored question answer key* is implied.

## Gates to finish stage 1, without artificial completion

1. **Scope/content reconciliation**: reconcile the 149 G2 original rows without exact current bank stem-matches and the 11 electro original orphan rows, keeping all existing 822 unmodified. Discriminate variants/reformulations; determine whether adding new source-native examples is an appropriate *separately approved scope change*.
2. **Per-question source and edition technical/linguistic QA**: original text/order, same physical/legal object and action, before + bold focus + after, mandatory exceptions and negative tests for A/B/C, current Grade I/II bibliography and edition. Existing P0/P1/P2 research is not professional signoff.
3. **Actual independent qualified review + score authentication protocol**: obtain verifiable electrical/legal + linguistic reviewer evidence and a documented policy for absent or nonunique ANRE official keys, then move only genuinely cleared records to approved learning. Presently **0/822**.
4. **Didactic answer-position QA**: when checking the app in the later implementation phase, verify option shuffling and stable text-to-correct-option binding, eliminating trivial A-only position exploitation without mutating user-uploaded original A/B/C. Teach from generated questions but explicitly label them unofficial.

## Current completion matrix

- Structural grade-route integrity: **822/822 checked, no key mapping discrepancies**.
- Source-native original Q/A/B/C fidelity for 415 mapped source QABC: **415/415 fingerprint compared**; **411 match**, **4 known substantive rewritten source differences** (5 grade routes). **P1 numeric-type source subgate verified**.
- G2 original-source completeness triage: **304/304 original rows compared**, with 149 no exact G1 stem, 6 changed options; **not yet signed off**.
- Unrepresented original electrotechnics rows: **11 identified**, vector diagrams discovered; no answers inferred.
- Independent professional approvals: **0/822**. Grade II synthetic answer position risk: **153/153 keys A**.
- **PR #7 remains Draft**, no merge/release; no app/HTML/APK/key change.

**Critical accounting**: these are completed **data/source consistency subchecks**, not 822 fully validated answers. Do not subtract their counts from the 793 P2 professional QA queue.
