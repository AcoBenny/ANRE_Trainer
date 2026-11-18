# CKPT-220 | Source-specific erratum G1-NOR-021: exact I7 corrosion clause located | 2026-11-18

## Superseded result
CKPT-218 marked G1-NOR-021 as `BLOCKED_EXACT_CORROSION_OBJECT_SOURCE_NOT_FOUND` after failing to find the exact phrasing in a text search. That was a **search miss, not absence from normative source**. Preserve original CKPT-218 for audit trace, **supersede only its provisional source-not-found classification**; do not duplicate source-case counts.

## Exact original case and answer
- Canonical ID: `G1-NOR-021`, original question: **Căile de curent ce nu se pot realiza în execuţie etanşă, în încăperi şi în spaţii din exterior cu mediu coroziv, pot fi realizate întotdeauna din:**
- A: `Cu`
- B: `Al`
- C: `otel`
- Imported key: **A**, unchanged.

## Exact primary source / adjacent qualifier
- Source: I7/2011, consolidated with **Ordin 959/2023**, §**5.1.7.2(b)** in [Portalul Legislativ](https://legislatie.just.ro/Public/DetaliiDocument/286763), HTTP 200 and exact relevant paragraph reopened 2026-11-18.
- I7 says copper conductors are to be provided in corrosive indoor and outdoor spaces **when aluminium or steel chemical stability is inadequate AND the installations cannot be protected with suitable coatings or gas-tight/effective enclosures**.
- Source immediately preceding §5.1.7.1 permits copper, aluminium and steel generally; §5.1.7.2 lists special instances requiring copper.
- Thus **A Cu is the source-intended answer conditional on the explicit chemical stability and inability to protect metals**, B Al and C steel fail the source's special conditions.
- The original question omits the chemical-stability prerequisite and says **`întotdeauna`**. Copper is not guaranteed chemically unaffected by any possible corrosive chemical. The literal universal still has a wording caveat. Distinguish an exam-intended correct answer A from universally valid material selection.
- **Revised evidence status**: `SOURCE_MATCH_A_WITH_OMITTED_CORROSION_CONDITIONS`, not approved for learning, not an official scored key or new independently executing QA.

## QA and restrictions
- No canonical QABC or key change, no HTML/APK/test work, no main merge/release.
- `existing_units_reclassified=1`; `new_QABC_units=0`; `learner_approvals=0`; `independent_QA=NOT_RUN`, `official_2026_exam_edition=NOT_VERIFIED`.
- Update only new overlay progress metadata in next V102 version, never rewrite CKPT-218 original file. PR #7 remains Draft.
