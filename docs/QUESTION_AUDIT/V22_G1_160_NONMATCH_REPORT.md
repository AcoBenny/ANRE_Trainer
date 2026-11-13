# V22 | G1 remaining 160 non-exact-matching questions, linguistic and source-risk preflight

Date: 2026-11-09. Canonical GitHub HTML V10.29 blob `bc5b5a61954ba138cf83987bfc932eca517f3b21`. **160 unique G1 records** left after G1 first 50 manual technical screens V19 and 204 exact cross-grade matches V21. Source/option/key preserved in each CSV row. Class breakdown {"SPECIALIZED_ELECTRICAL_GATE":10,"LEGISLATIVE_CLAUSE_VERSION_GATE":45,"KEY_CONFLICT_LEGAL_REVIEW":5,"I7_NORMATIVE_PARAGRAPH_GATE":100}; automatic linguistic markers in 128 cases. **This is preflight, not full semantic, normative or independent QA.**

## Core source issue

- **100 Grade 1 Norme tehnice** questions often demand precise thresholds, insulation resistance, cable sections, protective devices or earthing. No numerical limit is approved merely from an old spreadsheet's answer letter. Source attribution should follow exact I7 provision and when applicable updated edition; official **Ordin nr. 959/2023**, which modified I7-2011, available at https://legislatie.just.ro/Public/DetaliiDocument/271142 . Distinguish applicability of changes to existing projects.
- **50 Grade 1 Legislație** source each question to law/ANRE regulation and edition. Five are already conflicts in V13/V14: G1-LEG-024,028,032,034,048; do not import a tentative proposed key into the application.
- **10 non-identical Grade 1 electrotechnics** require technical review. Special procedure/scheme risks: G1-ELE-125, G1-ELE-126, G1-ELE-137, G1-ELE-138, G1-ELE-249, G1-ELE-266, G1-ELE-267. One family of near-duplicate statements should be compared across grades, but not treated as exact.
- Historical ANRE question banks are exam examples, not didactic paragraphs. Source-version/paragraph fields remain `NOT_VERIFIED` for these 160, QA `NOT_RUN`. A 2023 source label is not proof of 2026 currency.

## Pedagogical and linguistic QA

Regex flags identify negative/absolute/conditional terms in the *full* question+options, and cannot determine a correct option alone. Where a value or procedure is safety-relevant, escalate to technical expert and primary norm version. Keep variants and letter order unchanged in this PR.

## Scope

G2: 408/408 with preliminary screens. G1: 50 individually discussed in V19 + 204 text matches to G2 in V21 + 160 current source-risk preflight = 414/414 with at least one evidence/review entry. **822/822 indexed and first-pass triaged, 0 independently fully approved**. This is not ANRE Trainer completion for release.
