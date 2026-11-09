# V17 | G2 legislation and normative bibliography first-pass QA

Date 2026-11-09. Canonical V10.29 `const DATA` from blob `bc5b5a61954ba138cf83987bfc932eca517f3b21`. Total **77** distinct entries: {"Legislație":62,"Norme tehnice":15}. All question IDs and ABC/key/source preserved exactly. Review distribution: {"BIBLIOGRAPHY_VERSION_GATE":60,"AUTHORIZATION_REGULATION_GATE":15,"TARIFF_DATE_GATE":2}. No independent linguistic/legislative agent; model-assisted linguistic/version screen only, `independent_QA=NOT_RUN`.

## Structural defect detected

**77/77 questions have original key A**: the entire G2 legislative + normative subset, not a randomized answer distribution. A learner can get 100% in this subset by always selecting the first response; this invalidates the subset as a discrimination test even if content is factually correct. **Do not silently shuffle answer choices or rewrite keys; require user approval to implement corrections.** Test only/evidence is permitted.

## Source audit and provenance

- 62 legislation questions; many ask about titles, regulation numbers, category or applicability *per ANRE 2023 bibliography*, rather than actual obligations. 15 norms likewise mostly ask whether I7/PE documents are on the list. These are **trainer-authored study questions**, not proof that they were issued in an ANRE exam. They must not be labeled `official exam questions` without distinct publication evidence.
- ANRE currently lists 2023 bibliography and official examples under https://anre.ro/participanti-la-piata-de-energie/persoane-fizice/energie-electrica/ . This only validates existence of a section, not per-question match to a precise bibliography row or current edition.
- ANRE official general info https://anre.ro/participanti-la-piata-de-energie/persoane-fizice/energie-electrica/ contains certificate/authorization procedures, 5-year visa and other policy details. Exact relevant article/date remains needed per item.
- **G2-LEG-081/082**: all values 250/500/125 RON appear plausible in tariff tables but a date-appropriate official source is mandatory; older ANRE pages cite different tariff orders. These question wordings omit the date and are especially vulnerable to future legal changes. Source labels cite ANRE Order 118/2023; exact act/edition is NOT fully independently audited.
- `G2-NOR-136–147` and `G2-NORM-001..003`: I7-2011/PE102/1986/PE155/1992 questions should cite precise 2023 ANRE bibliography rows and any applicable later replacements; **bibliography inclusion does not prove a norm is currently in force**.

## Language / tech / QA gates

- Linguistic: independently assess distractors `doar/numai` against genuine conditions; an easy absolute-word distractor is not necessarily a valid learning test.
- Technical/Legal: distinction between historical `conform bibliografiei 2023` and current law must be prominent. No keys altered.
- Independent QA: NOT_RUN. Exact source paragraph for all 77: NOT_VERIFIED. App runtime: NOT_RUN.
- Suggested improvement requiring approval: balance answer positions only in actual quiz delivery without changing the meaning or key mapping, and ensure explanation shows not just list membership but didactic substance. No implementation in this PR.

Next: G2 early unreviewed 33 IDs 001–050 (after excluding the 17 V8 priorities); then G1 414.
