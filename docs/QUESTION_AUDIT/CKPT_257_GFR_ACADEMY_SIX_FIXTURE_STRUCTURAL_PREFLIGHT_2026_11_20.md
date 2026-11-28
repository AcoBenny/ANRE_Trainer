# CKPT-257 | GFR | Deterministic Academy negative-fixture preflight | 2026-11-20

## Scope and unchanged release gate
- Resume exactly from CKPT-256 / V149, PR #7 Draft, previous HEAD `c55b386df38e754bc2af2c92c0518af394195625`.
- Inputs opened from this same branch: `V144_SIX_RELEASE_BLOCKERS_SOURCE_VERSUS_CANONICAL_ADJUDICATION_2026_11_20.csv`, `V148_153_NONWORKBOOK_QABC_ALL_A_BIAS_TARIFF_CURRENCY_2026_11_20.csv`, and `ACADEMY_CKPT256_SIX_NEGATIVE_REGRESSION_FIXTURES_2026_11_20.json`.
- In-session executable CSV parser used quote-aware field parsing, preserved exact text/diacritics, compared original-versus-imported options and ID/key fields. **No data repair, no canonical edits.**

## Observed tests (actual execution; structural only)
- PASS `SIX_BLOCKERS_EXACT`
- PASS `ACADEMY_FIXTURE_COVERAGE`
- PASS `ACA-ANRE-001_NOR072_REVERSAL`
- PASS `ACA-ANRE-002_NOR048_ALL_OPTIONS`
- PASS `ACA-ANRE-003_CHARGE_MECHANISM`
- PASS `ACA-ANRE-004_CAPACITANCE_CROSSGRADE`
- PASS `ACA-ANRE-005_COUPLER_CROSSGRADE`
- PASS `ACA-ANRE-006_ALL_A_BIAS`
- PASS `NONWORKBOOK_AUTHORED_NOT_GUESSED`
- PASS `UNCHANGED_RELEASE_GATES`

Results: **10/10 PASS**, 6 distinct strict blockers, 6 registered negative scenarios, 153 out-of-workbook items with imported A keys. Authored-tag subclasses count only where the provenance field explicitly says TRAINER_AUTHORED; do not infer all other items' original author.

**Limits:** These tests prove consistency of the current registry fields, not the truth of sources or answers. No baseline-versus-skill model comparison was executed. No qualified independent electrical/legal/linguistic reviewer was run. The six Academy fixtures remain REGISTERED_NOT_BENCHMARKED, not promoted to measured skill improvement.

## Recheck leads and exact-source access limits
- `QABC-0362/G1-NOR-048`: I7 §5.4.13 lists lighting circuit, socket circuit or distribution board; original C is permissive, imported C adds `numai`. Indexed official source: https://legislatie.just.ro/Public/DetaliiDocumentAfis/286763 . Fresh direct Portal page access returned 502 in this session; the already documented local-I7 verification in CKPT-256 remains the direct-text basis, not a fabricated new official re-read.
- `QABC-0386/G1-NOR-072`: original B explicitly says `fără utilizarea unei scule`; imported B says `numai prin intermediul unei scule`. Local I7 §5.5.2.3 wording was documented in CKPT-256; independent public indexed parallel print references also contain the tool condition. Official portal direct read returned 502, so no new official full-paragraph signoff.
- `QABC-0017`: an outside publicly indexed teaching sheet also shows `Cs = 3C`, but this is not an authenticated official exam key and does not independently prove the workbook's exact Romanian term definition. Conditional algebra from CKPT-256 remains provisional.
- `QABC-0094`: NTE 009/10/00 distinguishes coupler operational contexts. An indexed regulation example allows a disconnected transverse/longitudinal coupler under short-circuit constraints, supporting **non-universality**, not a single preferred letter A/C. Link: https://legislatie.just.ro/Public/DetaliiDocument/122751 .

## Remaining work, no automatic approvals
1. The two cross-grade key conflicts (`QABC-0017`, `QABC-0094`) require same-scope source/original pedagogical definition and independent technical adjudication.
2. The four source-fidelity mutations (`QABC-0143`, `QABC-0236`, `QABC-0362`, `QABC-0386`) require source-exact exam representation kept distinct from proposed didactic corrections, plus qualification/signoff.
3. Reuse the 408 exact-workbook units' existing source fingerprint; proceed with **independent option-by-option QA and current edition checks**, and separately review all 153 non-workbook items. No learner content approval before every gate passes.

**Immutable:** 822 IDs, 568 QABC units, all original Q/A/B/C/keys, HTML and APK unchanged. PR Draft; no merge/release; 0/822 approved for learning.
