# CKPT-409 | GFR ONE PASS v2: inventory reconciliation + recovered prior research pointers

Date: 2026-11-23. Parent: CKPT-408. Branch: `audit/anre-v8-priority-17-20261109`; PR #7 Draft, no merge or release. **This checkpoint is data/provenance reconciliation, NOT final scored-key/technical approval.**

## 1. Actually executed and read back in repository

- [V369 reconciled evidence master](./ONEPASS_V2_PILOT/V369_ONEPASS_V2_RECONCILED_568_822_157_11_EVIDENCE_MASTER_2026_11_23.json) newly created and GitHub-blob read back (`905c7c9b4a8515ae74bf94ba2b928fc1263b1e55`), from existing V141/V241/V360/V363/V364/V367/V368. Contains all **568 distinct QABC, 822 grade routes, 157 quarantined original Grade-II candidates, and 11 original Electro source orphans** without altering original question/options/keys or importing new rows. **14/14 deterministic join assertions passed**: exact V141 source metadata/QABC grade IDs, V241 draft file and SHA, V360 imported grade keys, V364 route mapping, stage/orphan identity, preexisting holds, and two focused overlay checks.
- [V370 historical research-pointer index](./ONEPASS_V2_PILOT/V370_ONEPASS_V2_ALL_822_PRIOR_RESEARCH_POINTERS_456_URL_GROUPS_112_REPORT_ONLY_2026_11_23.json) newly created and GitHub-blob read back (`0b306e1bfbf8e0480aff175b581c45a4facaecf5`), from existing V141 and the actual 1,015 changed-file paths in PR #7. **8/8 deterministic pointer assertions passed**. Historical per-grade analysis file references resolve **822/822** to actual paths in the audit PR. **600/822 grade routes have URL-like candidate strings**, spanning **456/568 distinct QABC**. The **112/568 QABC** without any URL-like string still have historical analysis files. This is traceable historical *research*, not direct official source certification. A raw URL string is not proof it was opened or that the quoted clause/edition applies.
- Total **22/22 dataset/checkpoint structural assertions passed**, all single-session deterministic QA, NOT independent specialist/content signoff. Preexisting CKPT-408 24 real source/register checks + 11 synthetic guards are not miscounted as new QA here.

## 2. Exact reconciled inventory

| Category | Count | Meaning |
|---|---:|---|
| Canonical QABC distinct | 568 | Exact V141 ↔ V241 ↔ V360 ↔ V364 join |
| Grade routes | 822 | G1 414, G2 408, original imported keys unchanged |
| Existing full A/B/C editorial DRAFTS | 568 | No certified full official before/focus/after 2026 card implied |
| Source-native canonical | 415 | Of which 4 material source-vs-Trainer variants remain source-fidelity holds |
| Trainer-created, explicitly UNOFFICIAL didactic units | 153 | All imported A in historical registry; shuffle/identity must be tested before learning |
| Explicit source research evidence indexed in V364 | 37 | Older partial matrix, NOT all prior research |
| New V367 real legal text+context packet | +1 | QABC-0265 added to derived source index; qualified review pending |
| Distinct units now explicitly tagged by V364+V367 | 38 | 530 without *this* specific proof index; 530 != never researched |
| Historical semantic/source holds | 136 | Includes 6 historical strict holds; not 142 independent |
| Source-original vs Trainer material variants | 4 | QABC-0143, 0236, 0362, 0386 |
| G2 quarantined source-native candidate rows | 157 | 149 missing stem + 8 same stem different original options; previously researched 47+110; NOT in 822 |
| Original Electro orphan source rows | 11 | 9 DrawingML/diagram and 2 text, NOT in 822 |
| Final independent professional/content approvals | **0/822** | No official exam-key proof or learner go-live |

## 3. Corrections and proof boundaries

1. **QABC-0265 / G1-LEG-001:** V364 had no indexed source overlay, but V367 includes the original canonical A/B/C, the official Law 123/2012 Article 3(21–23) legal context and a candidate C. The exact V367 question+three options and imported key C were re-checked against V141/V360. Put in **SOURCE_CONTEXT_DRAFT_READY_FOR_QUALIFIED_REVIEW**, not `APPROVED_FOR_LEARNING`. Current Grade-I 2026 bibliography, independent legal/linguistic adjudication, user rights and actual offline display still unverified.
2. **QABC-0236 / G1-ELE-247 + G2-ELEC-383:** V364/V241 pointed to V194 original-source editorial, whereas V368 explicitly distinguishes the Trainer's altered B option and supplies the correct effective Trainer editorial from V240. V369 preserves **both** source/original and Trainer editorial file/SHA references; no original workbook, imported key, HTML or APK changed.
3. **V141 source/research pointers:** 822 report-path matches in actual PR files are **research discovery**, not 822 finished clauses. 600 URL-pattern route refs are not 600 authenticated normative/technical sources. 530 records without the narrow indexed V364/V367 evidence MUST search their original CKPT/V141 pointers before opening fresh searches. No missing-research conclusions from incomplete index.
4. **Original XLSX bytes** were not reopened in this checkpoint. Earlier recovered SHA/structural assertions are not new binary authentication. Official 2026 exam bibliography, full before/focus/after source text where permitted, source-context rights, option uniqueness, professional review, and Android/HTML runtime tests remain gated.

## 4. NEXT GFR ACTION: source-readiness queue without repeated batches

- **A.** Generate V371, a non-repeating source-readiness queue by exact QABC and grade: use V370's verified existing analysis-file pointers FIRST; sort critical 136 historical holds / four material variants / grade-specific 2026 legal scope, then normal units. Distinguish `DIRECT_URL_UNREOPENED` (456 groups) from `REPORT_POINTER_ONLY` (112 groups) and `SPECIFIC_SOURCE_PACKET_PRESENT` (V364/V367; 38 distinct, overlapping other buckets). Deduplicate by QABC and source clause; no false evidence promotion. Progress requires a newly resolved gate.
- **B.** Finish one real positive end-to-end context-card example: QABC-0265 legal original context and 3 A/B/C reasoning with exact source locator, edition/rights and adversarial review. Preserve `READY_FOR_QUALIFIED_REVIEW` pending actual qualified signoff. An AI challenge is NOT a licensed reviewer.
- **C.** Freeze scope separately for 157+11 and identify which original variants/graphics may be included after source, diagram-pixel, option, rights and grade QA. Do not replace 822 or infer a new final target until individually adjudicated.

**Interaction rule:** user input only for a named, source-backed irresolvable choice or approval of bank-scope/key changes. For every new GFR batch, report **old status → new status** and unique IDs advanced; a repeated unchanged investigation counts as **zero progress**. No merge/release of PR #7 and no modification to original answers, web app or APK without explicit permission.

## 5. Rollback and reproducibility

This step created only V369, V370 and this markdown checkpoint under `docs/QUESTION_AUDIT/` on the existing audit branch. Reversing these new docs commits does not affect QABC data or application. Input blob SHA references and all mapped report paths are embedded in the JSON files. Re-run each assertion against the referenced blob version after any upstream data change; no assertion permits source/legal approval. Status: **inventory and prior-pointer recovery COMPLETE; final source+answer+card approval NOT STARTED**.
