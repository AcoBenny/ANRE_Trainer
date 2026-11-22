# CKPT-388 | GFR: G2 source-original expansion direction approved, 157 quarantined, 9 technical I7 rechecks

**Date:** 2026-11-22. Continuation of CKPT-387. Audit branch: `audit/anre-v8-priority-17-20261109`; PR #7 stays Draft.

## 1. User decision incorporated without premature app integration

The user explicitly **accepted** the prior CKPT-387 recommendation to recover missing Grade II original ANRE source questions **after validating them**, while retaining the **153 existing authored didactic questions in a visibly separate educational layer**. This authorizes expansion as a project direction and preparation, **not unqualified automatic promotion of 157 unscored source rows** to a releasable learner bank or replacement of all original keys.

Source-specific original candidate intake is now physically staged:

- [V298: 157 G2 native Excel recovery candidates, source stem and raw ordered A/B/C](./V298_G2_ORIGINAL_157_RECOVERY_CANDIDATES_QUARANTINE_2026_11_22.csv).
- [V299: 9 provisionally researched G2 Norme ABC cards using actual user I7 PDF 2023](./V299_G2_9_NORME_ORIGINAL_I7_PRELIMINARY_ABC_REVIEW_2026_11_22.json).
- [V300: 157-row staging integrity / quarantine QA](./V300_G2_RECOVERY_157_STAGING_INVARIANTS_QA_2026_11_22.json).
- Previous evidence [V296](./V296_G2_304_SOURCE_NATIVE_TRIAGE_EXACT_AND_FUZZY_NO_KEYS_2026_11_22.csv) and [V297](./V297_G2_304_NATIVE_VS_822_COVERAGE_149_ABSENT_8_VARIANTS_2026_11_22.json).

### Why 157 and not instantly 979?

Original source G2: **304** workbook rows = **147** exact canonical A/B/C matches + **8** same-stem but differently ordered or worded A/B/C + **149** whose stem has no exact match anywhere in current 568 QABC groups. The **157 (149+8)** are **candidate additions** only, assigned stable IDs `ANRE-G2-LEG-XLSX-Rnnnn` or `ANRE-G2-NOR-XLSX-Rnnnn`. **53 legislation** and **104 norm-based** candidates.

These 157 candidate source rows have no blank option, no duplicate full Q/A/B/C within the candidate intake, and no duplicated staging ID. Each `source_file`, SHA256, physical row and original A/B/C string matches the physical-source-derived V296 exactly, with no reordering or assigned official score. The source original raw binaries had been reopened in earlier checkpoints.

If literally every candidate eventually became one separate new grade route, 822+157 would be **979**, but that is **only an arithmetical ceiling under that assumption**. Semantic overlaps, same-concept alternative wording, score gaps and outdated legal contexts can reduce eligible candidate count. No unique *actual final* new total is asserted.

## 2. Nine new source-specific G2 Norme checks

Using the user's exact I7 `803493174-I7-2011-completat2023(1).pdf` SHA256 `4bc3fc701cb71c937ad166462807423fa505c483783c5c93fe5b8ad03b20f431`, reopened both page text and visual page images 4,5,7,62,63,66,68 (earlier 9), and separately checked every original A/B/C:

| Staged ID source row | Provisional answer **not official** | Exact 2023 I7 locus | Critical negative/scope QA |
|---|---|---|---|
| G2 NOR 8 | C | §5.3.1.7.3 p63 | Undervoltage protection **may** be delayed when safe, not always immediate/delayed |
| G2 NOR 12 | A | §5.3.3.29 p66 | Panel corridor >10m implies end accesses, **but exception** if corridor width >3m; source stem omits exception |
| G2 NOR 15 | C | §5.3.1.2 p62 | Protective device choice considers **normal and starting load**, not only one |
| G2 NOR 17 | C | §5.3.1.2 p62 | Same principle, different object: **conductor sizing**, not protection selection; do not deduplicate by A/B/C |
| G2 NOR 31 | C | §5.3.1.7–7.2 p62–63 | Short-circuit and overload protection; conditional `de regulă`, fire-pump no-trip exception |
| G2 NOR 33 | C | §5.3.1.1 p62 | 15kW maximum aggregate same-purpose feeder under shared short-circuit protection |
| G2 NOR 40 | B | §5.3.4.5.1.2 p68 | PE/PEN not interrupted via switch; do not confuse PE with active neutral N; related G1 variant |
| G2 NOR 119 | A | §1.1(e), §1.2(b,d) p4–5 | Prefabricated buildings included, mines/explosives excluded; G1 has different original options |
| G2 NOR 127 | A | I7 chapter 2 terminology p7, §4.1.1 p9 | Basic insulation of dangerous active parts differs from fault/supplementary insulation; G1 ABC differs |

The V299 JSON records **exact original source Q/A/B/C**, a separate rationale for each alternative, paragraph plus before/after context, critical exceptions, previous QABC overlaps, provisional intended answer, and absent human certification. These are **9 of 157 preliminary A/B/C source-object research passes**, **not 9 final exam-scored or independently qualified approvals**. **148** remain without this bounded review (including all **53 legislation** candidates), while every one of the 157 still lacks final approval.

## 3. Source-era and official publication gate

Current official [ANRE electricieni examination page](https://anre.ro/participanti-la-piata-de-energie/persoane-fizice/energie-electrica/) lists:
- `LEGISLATIE GR. 2-05.2023` and `NORME TEHNICE Gr. 2-05.2023` as **ANRE example XLSX** files.
- 2023 published minimum exam bibliography, and current **Autumn 2026** session announcements.
- The original 2023 electrician regulation `Ordin 66/2023` and the amendment `Ordin 65/2024`.

The exact publicly linked model workbook XLSX downloads were identified at:
`https://anre.ro/wp-content/uploads/2023/05/LEGISLATIE-GR.-2-05.2023.xlsx`
`https://anre.ro/wp-content/uploads/2023/05/NORME-TEHNICE-Gr.-2-05.2023.xlsx`.

**Warning:** Fetching binary official files for an independent live-server SHA256 match **failed** (binary content unsupported through the browser tool and direct download failure). Therefore the user's original workbook hashes were verified against historical local originals, **NOT verified against the public ANRE server**. Official *publication listings* do not prove ANRE issued a scored answer key in those XLSX files, nor that no legal amendment since 2023 changes an answer.

The existing authored 153 Grade II didactic answers all import correct key A; prior issue noted and later renderer display-shuffle/scoring QA still required, but not addressed by editing canonical keys now. Prior example about ANRE 2026 fee order [2026 ANRE exam announcement](https://anre.ro/wp-content/uploads/2026/01/Anunt-sesiune-P2026-2.pdf) references **Ordin 82/2025**, while older ANRE landing pages still display historical tariff orders; dynamic tariff questions must be reviewed against the current effective norm, not prior page text alone.

## 4. QA, limits, rollback

- **PASS** V300: 157 raw source Q/A/B/C line/option matches V296, ID uniqueness, no 157 new official keys, no blank A/B/C, no learner-approved field, no source-only duplicates, all 157 quarantined.
- **NOT DONE:** current 2026 exact normative validity for all nine candidate answers, independent technical and linguistic professional review, official scored key authentication, original-workbook direct server binary hash parity, and source-specific examination-grade mapping.
- All preexisting 568 canonical QABC, 822 grade occurrences, 153 didactic questions, existing P0/P1/P2 27/2/793 **remain unchanged**. The 157 staged IDs **are not** active Grade II question IDs and must not be counted as finalized/approved exam problems.
- No changes to source XLSX, canonical IDs/keys, HTML, APK, app build, PR release, or merge. PR #7 remains Draft. Source snapshots and V298-V300 are audit-only and reversible by branch history.

## 5. Next GFR priority

1. **Proceed with remaining 148 G2 candidates**, starting with law/edition-sensitive Grade II legislation (53) and conditional/dangerous Norme wording (95). Distinguish original question text, original row, 2026 current normative source, source candidate letter, and official scored key.
2. Finish the **8 original G2 option-variant crossgrade conflicts**. V299 covered two G2 NOR rows (119,127); six still need exact primary clause rechecks. Do not copy keys between similar stems.
3. Only after all source-original items pass exact source, applicability, semantic-deduplication and independent review gates, **propose** the final bank size, merge plan, didactic category separation, and risk-controlled application test. Nothing enters a learning-enabled build prematurely.

**Stage result:** approved expansion direction **implemented as audited quarantine/staging**, not yet production-bank enlargement or qualified certification.
