# CKPT-387 | GFR phase 1: physical G2 original workbook vs all 822 routes; scope gap established and triaged

**Date:** 2026-11-22. **Branch:** `audit/anre-v8-priority-17-20261109`. Continue from CKPT-386, unchanged PR #7 Draft. No merge or release.

## Actual new independent, deterministic source coverage work

- **Inputs:** physically recovered original XLSX binary `LEGISLATIE-GR.-2-05.2023(1)(2).xlsx` SHA256 `725323d136481e7ad5643251e2b89a19bd57a471527cbeec847a5fe7f32f2662` (103 source question rows); and `NORME-TEHNICE-Gr.-2-05.2023(1)(2).xlsx` SHA256 `2183a362a9d22fad79052f7981238aa15b56cc8972ebfb87e86bd9d86a939613` (201 source rows).
- **Current canonical:** V141, 568 QABC and 822 grade routes (V283/V291). Compared **all 304 physical G2 source question+three option cells** to the **entire** V141, not just original Grade I workbook.
- **Normalization only for matching:** Unicode accents canonicalized, whitespace collapsed, case folded; never changed actual source text, original answer option order, or learner content.
- Results, independently crosschecked in both a Python artifact_tool workbook analysis and in GitHub-connected JavaScript CSV V141↔V296 reconciliation:

| G2 original vs current canonical 822 | Total | G2 legislation | G2 norms |
|---|---:|---:|---:|
| Exactly same question and ordered A/B/C | **147** | 50 | 97 |
| Same question, **different ordered alternatives** | **8** | 4 | 4 |
| **No exact matching question text** anywhere in the 822 | **149** | 49 | 100 |
| **Total** | **304** | **103** | **201** |

- The 149 absent-source texts form **136 distinct normalized stem groups**, because **12 same-stem clusters contain 13 extra option variants**; none of these variants should be deduplicated by stem alone.
- Within the 8 same-stem but different-answer sets: two represent **known material app rewrites** (`QABC-0362` source G2 Norme row 79 and `QABC-0386` source G2 Norme row 116); six are G2 original alternative sets distinct from existing Grade I canonical QABC. Their precise original A/B/C and matched QABC IDs are in V297. **Do not transfer a correct letter between these different ordered variants.**

## The most important integrity conclusion

**The existing target 822 is NOT a complete literal representation of all supplied Grade II legislation/norms original Excel rows.** The 149 G2 source rows that do not appear verbatim may be technically covered as concepts by other reformulations; exact-text absence is **NOT** proof of 149 technically unique concepts. Do not claim they are exam-certified or immediately add 149 grade routes without an explicit scope decision and separate original-key/edition/source analysis.

Current original source-compatible QABC are 415 groups (669 grade occurrences), plus **153 Grade II didactic authored QABC** (153 occurrences) to total 568 groups/822 occurrences. The **153 didactic correct answers are ALL letter A** in V141. This is an observable answer-position bias (not a wrong-answer proof). Anti-bias remediation belongs to later renderer test after user permission: preserve stable options and grade keys internally while shuffling answer display and scoring accordingly; DO NOT rewrite stored answer keys now.

## Three source-specific normative results, new targeted research on G2 originals

### G2 Norme row 119, previously unlisted G2 source option set

- Original stem: `Prevederile normativului I 7 – 2011 se aplică la proiectarea, execuţia şi exploatarea instalaţiilor electrice aferente:`
- A = `clădirilor prefabricate`; B = `minelor şi carierelor`; C = `depozitelor de materiale pirotehnice şi explozive`.
- **Direct user I7 2011 consolidated 2023**, page 4 `§1.1(e)` **includes prefabricated buildings**. Immediately following, page 5 `§1.2(b)` **excludes mines/quarries** and `§1.2(d)` **excludes pyrotechnic/explosive material warehouses**. This affirmative source-versus-option test supports **A as research-only candidate**, not a scored original source key nor an authenticated 2026 edition; G1 canonical `QABC-0369` with *same stem* has *different option A* (agroindustrial buildings) and imported A, so do not conflate the letters.
- Immediate before/after context and article scope: applicability §1.1 has a broad enumerated building list; §1.2 separately enumerates excluded equipment/locations and prohibits a careless universal reading.

### G2 Norme row 127, previously unlisted G2 source option set

- Original stem `În cazul instalațiilor electrice de joasă tensiune, izolaţia de bază reprezintă:`
- A `Izolaţia care asigură protecţia de bază.`; B `Izolaţia care asigură protecţia de defect`; C `izolaţia maselor`.
- **Direct user I7**, p7 terminology immediately after “instalaţie de legare la pământ” and before definitions of double/reinforced/supplementary insulation: basic insulation insulates **hazardous live parts and supplies basic protection**. Later p9 explicitly differentiates `protecţie de bază` in absence of fault from `protecţie în caz de defect`. A affirmatively supported, B confuses supplementary/fault protection, C not the defined object. G1 `QABC-0392` with identical stem has different option A/B/C and imported B; do not carry G1 B to source G2. **Research-only candidate A**, no official scored-key verification.

### G2 Norme row 40: near-identical G1 source, not source-native exact

- Original G2 stem `Întreruperea conductorului de protecţie prin aparate de comutație`, while G1 source row 31 says `Întreruperea conductorului de protecţie prin aparate de conectare:`; **the original three ordered A/B/C are identical**.
- User I7 p68 **§5.3.4.5.1.2** explicitly forbids interruption of PE and protective conductors in all networks; negative alternatives A (`este permisă`) and C (`de regula nu este permisă, cu excepţia anumitor cazuri`) over/underclaim. Original option **B `nu este permisă`** is **research-supported**, not official authenticated.
- This near-duplicate (93.8% textual similarity) should be a **deduplication candidate for shared teaching content only after exact-object terminology QA**; do not automatically remove it or overwrite original source variants.

## Extra current-edition flag (didactic, not answer-error finding)

- Didactic QABC-0555 and QABC-0556 cite **Ordinul ANRE nr. 118/2023** as source for authorization fees (imported choices **250 lei** for type A or B and **500 lei** for A+B). ANRE's [2026 exam notice](https://anre.ro/wp-content/uploads/2026/01/Anunt-sesiune-P2026-2.pdf) instead specifically cites **Ordinul nr. 82/2025** for fees in 2026.
- More recent fee publications also show 250/500 numeric values; this means **source-era citation is outdated / needs scope-specific update**, NOT proof the two answer numbers are wrong. Do not change keys or release without reopening the applicable current norm and confirming its effective 2026 version.
- Main ANRE 2023 electrician bibliography remains linked by official website on 2026-11-22, but that does not authenticate each 2026 legal clause or scored exam answer.

## Exact artifacts and tests

- [V296 physical G2 original question/ABC evidence, 304 rows](./V296_G2_304_SOURCE_NATIVE_TRIAGE_EXACT_AND_FUZZY_NO_KEYS_2026_11_22.csv), with source SHA256, match/near-match, first-pass triage, original variants, **NO official keys**. Reconciled against previous V295 and all 568 canonical V141 rows.
- [V297 304-source vs 822 full exact comparisons and 149 source gap/8 variant index](./V297_G2_304_NATIVE_VS_822_COVERAGE_149_ABSENT_8_VARIANTS_2026_11_22.json).
- Source file unchanged. **All 153 didactic keys A** confirmed structurally. The single high-similarity example does not imply 148 remaining are semantically unique.
- All **822 grade-route learning approvals still 0**; P0/P1/P2 counts **27/2/793** unchanged from V283/V291. The new G2 candidate source rows are **NOT inserted** or scored, so they do not change these denominators.
- PR #7 remains Draft, no merge; original XLSX, canonical answer keys, HTML/APK untouched.

## Finite next priorities

1. **Decision gate for scope**: should 149 original G2 rows be added to the exam-original question bank (after source-key and edition validation), with 153 didactic cards as separately labeled exercises? Preserve original A/B/C and their row IDs. The current 822 target otherwise lacks literal source coverage of many Grade II items. This cannot be silently resolved by the auditor.
2. Independently check applicable **2026 bibliographic grade/legal edition**, run option-by-option review of 149 gap rows plus 8 alternative sets, with a separate qualified reviewer. Prioritize changed legal rules, then I7 and technical norms.
3. After source-signoff, safe bank migration plan + didactic display shuffle regression. No current approval to modify keys, production learning data, APK, or release.

**Status: phase 1 is materially advanced but NOT complete. This report is scope reconciliation and provisional research, not certification.**
