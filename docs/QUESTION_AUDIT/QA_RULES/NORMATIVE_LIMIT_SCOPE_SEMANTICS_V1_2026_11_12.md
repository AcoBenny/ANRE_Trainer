# QA Avengers | Normative bound vs admissible value | v1 | 2026-11-12

## Why this exists
**G1-NOR-029** exposed a false-positive ambiguity classification in CKPT-022 and `DEEP_NOR_01_ALL_20_PRE_REVIEW_SOURCE_ABC_TRIAGE.csv`: the old reasoning accepted that 2m and 2.3m were individually permitted and inferred that all A/B/C could answer the normative **limit** question. This was a **question-intent / quantifier error**, *not* a demonstrated defect of the exam wording.

Historical claim `AMBIGUOUS_MULTIPLE_TRUE` + automatic rewrite proposal is **SUPERSEDED for this specific ID** by `LEGITIMATE_NORMATIVE_EXCEPTION_TRAP + CANONICAL_KEY_CONFLICT_TO_REVIEW`. Preserve the old historical file as evidence of the failed inference; do not silently overwrite it.

## Source and exact canonical question
- Stable ID `G1-NOR-029`, Grade I, stored key **B**, original options A=**2m**, B=**2.3m**, C=**2.5m**.
- Stem: “Tablourile de distribuţie **din locuinţe** se pot instala astfel încât **înălţimea laturii de sus** a tablourilor faţă de pardoseala finită **să nu depăşească:**”
- Source **I7-2011 §5.3.3.21**, Romanian Legislative Portal print-page indexed result, https://legislatie.just.ro/Public/FormaPrintabila/00000G1AGLK3X9HXIS43LTLA4TCXTBR4 . Text observed: **general upper-bound 2.3m**, **explicit special upper-bound 2.5m for dwelling boards**.
- Source access in this review: official Portal **search-index excerpt** exposed both rule and exception; **direct Portal opening failed**. Do **not** claim full amendment-chain/2026 exam edition or independent source reviewer verified.

## Correct semantic reduction
1. **Asked quantity = regulatory maximum**, because the blank completes **să nu depăşească [threshold]**; it is **not** “at which of these arbitrary heights may one install a board?”
2. **Match exact regulated object and metric**: upper edge of distribution board measured above finished floor; location **locuinţe**. The specific dwelling exception overrides general 2.3m. Mathematically `max_height_for_dwelling=2.5m`.
3. Compare **equality with required limit**, not “candidate is less than limit”: `2 == 2.5: false`, `2.3 == 2.5: false`, `2.5 == 2.5: true`; therefore candidate **C**. A 2.4m board in a dwelling is permitted by this particular height rule, so filling the normative threshold as 2.0m or 2.3m would falsely disallow the 2.4m installation. This eliminates the alleged multiple correct answers.

**Critical distinction**: For a question explicitly asking “Which of these heights **are permitted**?”, candidates <= 2.5m may all be examples of permissible heights; then multiple options can indeed be correct. The intent and quantifier must be resolved **before** arithmetic.

## Audit-only deterministic implementation
- `tools/qa_normative_threshold.mjs` exports `evaluateNormativeBound({ question, options, rule })`; it recognizes a small supported subset of **maximum threshold** stems and a structured authoritative rule with an explicit context exception.
- Normalizes Romanian diacritics, decimals (2,5 -> 2.5) and length units (m/cm/mm). First checks object/metric and branch scope; only then recognizes whether the question requests **normative bound** or **permitted examples**. A source locator is mandatory.
- Outputs statuses: `SINGLE_NORMATIVE_BOUND_CANDIDATE`, `MULTIPLE_ADMISSIBLE_EXAMPLES`, `MULTIPLE_EQUIVALENT_BOUND_CHOICES`, `SOURCE_OR_OPTIONS_MISMATCH`, or explicit `BLOCKED/NOT_EXPLICIT_BOUND` statuses. No unsupported case is silently approved.
- `tools/tests/qa_normative_threshold.test.mjs` contains **11 deterministic synthetic regression cases**: original dwelling, general case, diacritics, admissible-value question, duplicate equivalent options, missing norm value, metric conversion, wrong object, unparseable text, missing source locator and other quantifier.
- Executed a **pure JS equivalent of the committed helper in this conversation**: **11/11 deterministic cases PASS** after correcting a brittle Romanian stem normalizer: `pardosel` failed to match `pardoseala`; now checks `pardose`. First run 2/11 falsely passed, corrected and reran 11/11 PASS. The persisted node:test suite was **written but not separately executed by CI or Node** in this session. Preserve the failed-first-run regression lesson.
- **Important:** `approved_for_learning=false` and `source_edition_verified=false` by construction. The helper does **not** parse normative text from random links, certify authority, check editions, infer grade or replace independent technical and linguistic review. A self-declared locator does not equal genuine source verification.

## Why the algorithm will be lighter
Only genuinely undecidable questions enter manual ambiguity escalation. A common false-positive pattern (`lower-than-limit => alternative answer`) becomes a precise check of **target variable equality**. The rule can extend to **minimums**, **ranges**, **exceptions for building type**, **voltage class**, etc. only after separate regression fixtures and verified source-object gates.

## Classification recommendation (NOT approval)
`G1-NOR-029: INTENT=MAX_NORMATIVE_BOUND; SCOPE=LOCUINTE_EXCEPTION; ISSUE=STORED_KEY_B_VS_C; CANDIDATE=C; AMBIGUITY_FALSE_POSITIVE_SUPERSEDED; INDEPENDENT_QA=NOT_RUN; APPROVED_FOR_LEARNING=NO`.

No canonical changes to stem/ABC/barem, no HTML/APK modifications, no merge/release.
