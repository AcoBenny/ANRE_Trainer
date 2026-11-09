# ANRE Trainer | Official-law-first source and temporal QA gate
**Date:** 2026-11-09. **Scope:** protocol change only on Draft PR #7. No changes to question text, A/B/C choices, keys, HTML, APK, or main.

## Finding and reason
V26–V29 G1-NOR reviews primarily used the user's Library PDF `803493174-I7-2011-completat2023.pdf`, a synthetic I7 consolidation dated 2023-09-22, and in limited historical comparisons an old PE102 PDF. These are useful *offline research aids*, not the final current-law authority for a 2026 verdict. Previous reports explicitly noted this limitation. Do not silently promote their preliminary source matches to final technical or legal approval.

**Official consolidated I7-2011 technical regulation:** https://legislatie.just.ro/Public/DetaliiDocument/286763 (portal displayed consolidated-history date **12.07.2023** at consultation 2026-11-09).
**Official change order:** Ordin MDLPA 959/18.05.2023, https://legislatie.just.ro/Public/DetaliiDocument/271142 , published Monitorul Oficial 512/12.06.2023; art. III states entry into force 30 days after publication (12.07.2023); art. II has transitional carve-outs for qualifying pre-existing projects.
**Original approval:** Ordin 2741/2011, https://legislatie.just.ro/Public/DetaliiDocumentAfis/287131 .

### Mandatory source priority by category
1. **Current legal/normative content:** exact consolidated regulation/law on `legislatie.just.ro`, current official ANRE/competent-authority act, Monitorul Oficial when required. Verify applicable edition/date, amendments, exceptions, repeal and scope; do not assume the portal's latest displayed consolidation date guarantees no later acts without checking the act history.
2. **Original/historical-exam wording:** retain the archived original question, answer choices, stored key, and date/version of the syllabus; map *historical* applicable source separately. Do not force a 2026 rule into a historical exam key without documenting this difference.
3. **Local PDFs and manuals:** locate pages and support offline learning only after text/version parity and redistribution/license checks. For pure electrotechnics, official law may not address the concept; use a credible didactic/academic or standard source, with exact page/definition and a source-rights gate.

### Per-question evidence contract (QA)
Record: stable ID; grade/category; canonical original question + A/B/C/order/key; canonical source SHA; official act identifier; exact official URL and paragraph/article/annex; amendment/consolidation and review date; applicable effective date and temporal exceptions; exact limited excerpt or accurate paraphrase; edition difference versus local PDF; technical justification; linguistic quantifier/condition/trap check; candidate key with status (NOT_FINAL); separate QA reviewer status; hyperlink checked status; local material rights; final action gate. **Never call preliminary model screening an independent engineering/linguistic QA approval.**

Required dispositions: `OFFICIAL_TEXT_MATCH`, `OFFICIAL_CONFLICT`, `HISTORICAL_EDITION_CONFLICT`, `MISSING_OPTION`, `AMBIGUOUS_OR_CONDITIONAL`, `OUTSIDE_I7_SCOPE`, `SOURCE_UNAVAILABLE`, `OFFICIAL_RECHECK_PENDING`. If official source is inaccessible, leave it PENDING rather than copying an unofficial assertion. Only change a canonical answer or application after separate expert QA and explicit user approval.

### Priority rechecks (not yet independently adjudicated)
- **G1-NOR-010** (V26): official I7 section 8.1.1.3.3, insulation-test circuit wording, provisional source/answer disagreement.
- **G1-NOR-012** (V27): section 5.1.7.2(a), 'intotdeauna cupru' versus conditional use; inspect related sector-specific rules.
- **G1-NOR-029** (V28): section 5.3.3.21, apartment/house distribution board 2.5 m exception versus 2.3 m general rule.
- **G1-NOR-032** (V29): official consolidated I7 section 5.2.12.3.10 states standard pulling-box maximum spacing **25 m straight path** versus **15 m for at most three bends**; the **following sentence provides an increased-conduit-diameter rule for greater distances**. Re-read entire relevant paragraph, the exact question stem and possible exception before finalizing a `MISSING_OPTION` or any app correction. Stored options 10, 15, 20 m, key B: no automatic key correction.

Other V26–V29 source-matched questions remain *preliminarily* mapped and should receive official URL+article/version QA before final signoff. Prior V25 primary-source cases should be checked for applicable legislation at the relevant time.

### Operational guardrails
- On every new batch: official source lookup -> currentness/effectivity/exception gate -> compare original A/B/C -> technical reviewer -> Romanian Language Reviewer -> independent source+QA -> only then proposal for user approval.
- A source lookup is not a technical QA signoff; link accessibility is checked separately and reported honestly. The official portal's pages were discoverable through indexed text during this session; some direct fetch attempts returned 502, so not every live 2026 paragraph/history was fully inspected. The official I7 section 5.2.12.3.10 and its next sentence were discoverable in indexed official print-form text. **Do not assert all 2026 amendments exhausted.**
- Preserve separate current-rule and historical-exam semantics, offline snapshot hashes and URLs where lawful. Do not redistribute local copyrighted PDFs. No merges, releases, grading/HTML/APK edits without explicit user approval.

## Resumption checklist
1. Reconcile V26–V29 (G1-NOR-001–040) official-portal URLs, article versions, exceptions; prioritize 010, 012, 029, 032.
2. If online source fails, record link/crawl error and defer official adjudication; do not present a secondary copy as official proof.
3. Extend the official-first gate to all legislative/normative ANRE question groups; document every remaining conflict individually and keep PR #7 Draft.
