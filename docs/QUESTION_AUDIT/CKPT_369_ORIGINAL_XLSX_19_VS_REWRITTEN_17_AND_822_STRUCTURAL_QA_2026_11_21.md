# CKPT-369 | Original XLSX source-first correction: 19 source candidates, 17 rewritten-canonical candidates, internal 822 preflight | 2026-11-21

## Important superseding correction (do not delete history)

**CKPT-366 / V279 conclusions for QABC-0362 and QABC-0386 are valid only against materially rewritten A/B/C in the application's canonical master, NOT against the original user-uploaded 2023 Excel.** V140 had previously recorded these exact source mutations. The claim that their original-Excel key conflicts were "false positives" was an authority/provenance error. Re-open **both** in the source-native evaluation without changing any keys or source material. The old boards remain immutable and directly traceable to this correction.

| QABC | Grade route | Imported key | Original XLSX vs modified app option | Research candidate from ORIGINAL (not scored key) |
|---|---|---|---|---|
| QABC-0362 | G1-NOR-048 | A | XLSX original A says **numai direct din tablou**; modified app A combines normal lighting, socket or board. XLSX original C says **dintr-un circuit de prize**, not **numai**. I7 2023 §5.4.13 explicitly permits all 3. | **C, preliminary**, actual allowable route but not an exhaustive summary |
| QABC-0386 | G1-NOR-072 | B | XLSX original B says **fără utilizarea unei scule**; modified app B says individual AND disconnectable **numai prin intermediul unei scule**. I7 2023 §5.5.2.3 requires BOTH individual and only-with-tool. XLSX original C states only the first requirement. | **C, preliminary** (necessary true condition, but incomplete; option uniqueness/wording still blocked) |

**Keep two denominators:** **17 QABC / 18 grade routes** are current candidates for the *rewritten-app A/B/C* in V279; **19 QABC / 20 grade routes** are research-stage source/key discrepancies for the *original uploaded XLSX A/B/C*. Neither figure means approved, genuine historical ANRE scored key, or an authorization to change the application.

## Read-only whole-bank structural QA

Cross-checked `V141_568_QABC_MASTER_WITH_7_SOURCE_FIDELITY_DELTAS_2026_11_19.csv` against two independent snapshots `V73_ALL_822_EVIDENCE_AND_RELEASE_GATES_MASTER.csv` and `V95_ALL_822_MASTER_AFTER_FOCUSED_RECHECKS_AND_SEPARATE_AI_QA.csv`:

- Exactly **568** QABC groups, **254** shared across grades, forming exactly **822 unique grade IDs**, with 0 duplicated grade IDs.
- Exactly 822 records in both V73 and V95, identical ID sets; **0 internal key mismatches**, **0 internal original-question/A/B/C text mismatches** versus V141.
- **0/822 independent approvals** and no unauthorized key edits in the audit.
- **WARNING:** Consistency between V141/V73/V95 does **not** establish fidelity to original Excel. The source-first delta register **V140** records **7 affected grade routes**: 5 **material** wording/answer changes across 4 QABC (G1-ELE-152, G1-ELE-247/G2-ELEC-383, G1-NOR-048, G1-NOR-072) and 2 number-cell-type-only differences (G1-ELE-154/G2-ELEC-292). They must be addressed as fidelity/release gates, not as seven separate new semantic problems.

## Original source trace

- Directly compared September 2026 and November 2026 Library copies of the two **original** ANRE XLSX documents; matching SHA256 across copies:
  - `NORME-TEHNICE-Gr.-1-05.2023 (1).xlsx`: `bed56a32f24d19774ec9dfff8c5b1438176078d0e9c4eb9e8fa1ff1fc98c3092`; relevant rows 55 and 79.
  - `ELECTROTEHNICA-09.2024-2.xlsx`: `2175d2c30ac8e2f149b28edd9ac00c233789bc0a3987ba779d6efed7afad920c`; relevant rows 159 and 254.
- The original A/B/C source workbooks do not, just by listing questions and alternatives, authenticate an official scoring key. Every imported key stays unchanged, but marked unverified.
- All I7 citations come from the original user PDF SHA256 `4bc3fc701cb71c937ad166462807423fa505c483783c5c93fe5b8ad03b20f431` (64 hex). V278/V279 stored an accidentally truncated 58-character string. See CKPT-368 / V281.

## Deliverables and prohibitions

- [V282 machine-readable reconciliation and complete seven-fidelity-delta list](./V282_ORIGINAL_XLSX_VS_CANONICAL_822_RECONCILIATION_TWO_FALSE_POSITIVES_REOPENED_2026_11_21.json)
- [V140 original-source fidelity comparison](./V140_7_SOURCE_XLSX_FIDELITY_DIFFERENCES_2026_11_19.csv)
- [V281 ten technical source checks](./V281_TEN_TECHNICAL_SOURCE_ABC_QA_AND_CORRECTED_I7_SHA_2026_11_21.json)
- [V280 seven legal source checks](./V280_LIVE_OFFICIAL_7_LEGAL_SOURCE_REOPEN_AND_TWO_CITATION_FIXES_2026_11_21.json)

**Still required:** qualified independent exact-source electrical/legal/linguistic A/B/C assessment for all 822 grade routes, exact current exam bibliography/edition, formal scored key evidence or approved remediation, full source-before/FOCUS/source-after card QA, then HTML/APK offline functional QA. **136/136 semantic root diagnoses remain known, 136 release-blocked, 0/822 learner approved.**

**No edits** to original ANRE Excel, canonic question/choices/grade keys, HTML/APK, main, PR Draft merge or release. This is a documentation-only checkpoint.
