# CKPT-379 | P1 QABC-0145 source-cell triage + V291 professional validation matrix

Date: 2026-11-22. Branch: `audit/anre-v8-priority-17-20261109`. Parent reference: CKPT-378, HEAD at resume `d7870c23727b97a5e22b33515494a90aa8b1f8db`.

## 1. Actual recheck of P1 (one QABC / two grade routes)

- IDs: `QABC-0145` -> `G1-ELE-154`, `G2-ELEC-292`.
- Source: `ELECTROTEHNICA-09.2024-2.xlsx`, sheet row 161, previously recorded SHA256 `2175d2c30ac8e2f149b28edd9ac00c233789bc0a3987ba779d6efed7afad920c`.
- Exact question in V282 and V141: **Mărimea periodică alternativă este o mărime a cărei valoare medie în decursul unei perioade este egală cu:**
- A = `1`; B = `0`; C = `1,5`. Imported key (both grade routes) = **B**, unchanged.
- Earlier workbook-type evidence V140 records source cells `A161=text, B161=number, C161=number, D161=text`. Numeric 1 and 0 were serialized to display strings `"1"` and `"0"` in the app/canonical master. V282 records equality of the source and current displayed stem and three options for both grade IDs. The **only recorded delta is numeric cell type**, not content or answer-letter mutation.
- **Independent limitation of this session**: original binary XLSX was NOT reopened. The source-cell-type claim is cross-checked against historical V140 and V282, NOT independently remeasured now. Native XLSX cell types and UI rendering remain a fidelity confirmation gate. Do not mark `original_source_XLSX_restored=true` on this evidence alone.

## 2. Technical and linguistic research, not independent professional approval

- Technical terminology: IEC 60050-103:2009, IEV `103-06-03`, defines an *alternating* quantity by **zero mean over a period**. IEV `103-06-05` identifies the direct component as a periodic quantity's mean; IEV `103-06-07` distinguishes a pulsating quantity with both a nonzero alternating component and a nonzero mean.
- Primary educational corroboration, source reopened in this session: [OpenStax, College Physics 2e §20.5](https://openstax.org/books/college-physics-2e/pages/20-5-alternating-current-versus-direct-current), which explains the zero mean of AC and the distinction from RMS and mean power.
- Source access caveat: text for IEC `103-06-03` was located in a publicly indexed reproduction of IEC 60050-103:2009; PDF visual screenshot fetch failed. Direct official Electropedia entry and 2026 exam bibliography/version match remain to be independently verified.
- Stem-to-option: A (`1`) contradicts zero mean; B (`0`) is directly supported; C (`1,5`) contradicts zero mean. Pairwise A/B, A/C, B/C: all three numeric constants are mutually distinct, no simultaneous equalities. **Research-supported candidate: B**, without claiming authentication of a scored ANRE answer key.
- Counterexample/semantic trap: an arbitrary periodic waveform may contain a nonzero DC component; do not expand the technical term *alternating quantity* to all periodic waveforms. Distinguish the arithmetic mean from RMS and mean power. This is a terminology qualification, not a reason to change the original text/key.

## 3. Outcome and open gates

- `P1_DATA_TYPE_TRIAGE`: **NO MATERIAL DISPLAY-TEXT DIFFERENCE IN THE PREVIOUSLY RECORDED SOURCE COMPARISON** for both routes.
- `P1_ORIGINAL_BINARY_AND_UI_GATE`: **PENDING** (original XLSX row 161 types independently reopened, app rendering or export tested as appropriate).
- `TECHNICAL_SOURCE_RESEARCH`: **SUPPORTED PROVISIONALLY** for B from IEC terminology + OpenStax; `INDEPENDENT_PROFESSIONAL_REVIEW`: **NOT DONE**.
- `LINGUISTIC_INDEPENDENT_REVIEW`, `2026_APPLICABLE_EDITION`, `OFFICIAL_SCORED_KEY`, `APPROVED_FOR_LEARNING`: **NOT DONE**.
- Nothing in this checkpoint changes source workbooks, imported keys, canonical question/ABC, HTML, APK, release or PR state.

## 4. V291: future review matrix

[V291_822_ROUTE_PROFESSIONAL_APPROVAL_MATRIX_AFTER_P1_TRIAGE_2026_11_22.csv](./V291_822_ROUTE_PROFESSIONAL_APPROVAL_MATRIX_AFTER_P1_TRIAGE_2026_11_22.csv) provides a row for each of the 822 grade routes, grouped into 568 distinct QABC and preserving imported key. The matrix retains the V283 priority breakdown **27 P0, 2 P1, 793 P2** and intentionally separates historical source research, a blind AI research pass, professional technical/legal and linguistic approval, applicable edition, scored key authentication and learning approval. All final learning approvals remain **NO**.

Do not treat a prior research record or an AI-to-AI agreement as a qualified professional signoff. P2 research may continue in risk order; P0 is not reopened merely for activity.

## 5. Independent QA of this checkpoint

- V283 counted: 822 grade-route rows, 568 QABC, 20 P0 source disputes + 7 P0 other strict + 2 P1 numeric-type + 793 P2.
- The V291 row-generation guard stopped on an initial unsafe missing-category summation; it was corrected before writing. The successful generated file contains **822 rows**, not a sample. No release gate advanced.
- Remaining: physical original XLSX verification when available, source and edition audits on P2, qualified independent professional review and approvals. A completed schema/row count is **not a verified answer bank**.

**Status: RESEARCH/TYPOGRAPHY TRIAGE ONLY.** PR #7 must remain Draft and unmerged.
