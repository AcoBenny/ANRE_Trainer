# CKPT-395 | GFR ANRE: 157 semantic triage, live official-law P0 rechecks

Date: 2026-11-22. Continues CKPT-394, PR #7 Draft. Read-only source review; no key, original workbook, canonical master, HTML, APK, main, or release change.

## 1. Actual work and saved evidence

**V329** [157-stage lexical/option comparison](./V329_G2_157_CROSS_BANK_INTERNAL_SIMILARITY_AND_LEGAL_P0_RECHECK_2026_11_22.json)
- Parsed immutable V298 (157 G2 source candidates) and V141 (568 canonical QABC groups).
- Performed **89,176** stage↔master stem comparisons and **12,246** pairwise comparisons within staging. Unicode/diacritic/case/punctuation normalization plus explicit stopword-set and token-Jaccard thresholds documented in V329. These are **algorithmic lexical leads only**.
- Stage↔master threshold 0.55: **12 staged source records** warrant comparison. Eight already known same-stem cases from V325; four additional related records are now included. Key new lead: **ANRE-G2-NOR-XLSX-R0040 ↔ QABC-0338/G1-NOR-024**. Its original A/B/C normalize to the same ordered text, with stem difference *aparate de comutație* vs *aparate de conectare*. Qualified exact object/source check remains required.
- Other three related-but-not-assumed-duplicate leads: G2-LEG-R0069 ↔ QABC-0300/0301 (type A design vs execution authorization), G2-NOR-R0194 ↔ QABC-0413 (independent earth electrode vs general earth electrode), G2-LEG-R0109 ↔ authored QABC-0421 (issuing authority vs grade applicability).
- **22** within-staging pairs at Jaccard ≥0.70, **14** with exact normalized stems and **8** only similar lexical stems. A preliminary alternate normalization flagged 18; the reproduced, explicitly documented final method yielded 22. No deletion, semantic uniqueness assertion or answer-key assignment.
- The 157 source candidates remain quarantined. Distinct original questions with shared stems and altered options may intentionally probe alternative facts and must be reviewed option-by-option.

**V330** [four legal P0 source-text rechecks](./V330_4_G1_LEGAL_P0_EXACT_ART92_93_ART18_OFFICIAL_PORTAL_RECHECK_2026_11_22.json)
- Fetched live Portal Legislativ HTML HTTP 200 on 2026-11-22: [Law 123/2012](https://legislatie.just.ro/Public/DetaliiDocumentAfis/307058) and [ANRE supply regulation Ord.5/2023](https://legislatie.just.ro/Public/DetaliiDocumentAfis/264611); examined exact relevant clauses, adjacent statutory classification and option A/B/C.
- **G1-LEG-015** (frozen B): Legea 123 Art.93(1)28 directly supports original **A** (refusal of metering access is a contravention); Art.92(1) calls unauthorized modification of power installations an *infracțiune*, not the proposed B as contravention. C not exhaustively adjudicated.
- **G1-LEG-019** (frozen C): Art.93(1)3 directly supports **B** (ANRE technical norms violation = contravention), rather than broad C *abatere*.
- **G1-LEG-026** (frozen C): Art.92(2) directly supports **B** (clandestine installations for direct grid connection = infracțiune) for exact stated action.
- **G1-LEG-017** (frozen B): ANRE regulation Art.18(3)(a) explicitly supports **A** (court-confirmed electricity theft => supplier termination). Art.26(2)(b) supports supply interruption for lack of guarantee, **not direct contract termination**. Art.18(3)(c) permits other legal grounds, so alternative B must be checked under other statutes before declaring a unique answer. This corroborates V324.
- These four are **affirmative same-scope source findings**, NOT authenticated historical ANRE scored keys, NOT 2026 bibliography signoff, NOT human/licensed independent review or approval to change stored answers. Preserve imported original keys.

## 2. Checks and noncompletions
- V329 row-ID invariants passed: 157 unique staged IDs, 568 unique QABC IDs. Both full candidate-pair loops completed. One normalization sensitivity found and recorded transparently.
- 4 / 28 operational P0 routes source-rechecked in this session, **0 / 28 qualified independent adjudications closed**.
- **0/822 current grade-route qualified final approvals** and **0/157 new source candidate approvals**. All 157 candidates still not learner-active. Existing 28 P0 and 2 P1 open as before; 4,932 earlier permutation cases remain *reference simulation only*, not actual HTML/APK tests.
- PR #7 stays Draft; no merges, original keys, HTML or APK touched.

## 3. Next finite GFR tasks
1. Continue P0 same-scope source preflight for G1-LEG-024/028/034/048, normative routes and duplicated G1/G2 imported key conflicts, with original A/B/C and adjacent exception context. Do not adopt a technical candidate as scored key.
2. Review V329 12 cross-stage candidates and 22 intra-stage pairs, distinguish genuine semantic duplicates, alternate-question traps, edition and grade regime differences. No deletion on lexical score.
3. Obtain distinct qualified legal/electrical review plus independent linguist and official-key provenance where possible, then prepare reversible, explicit, user-approved integration with real HTML and offline APK tests.

**Gate:** Source researched ≠ independently approved ≠ exam answer key authenticated ≠ app release. PR remains draft.
