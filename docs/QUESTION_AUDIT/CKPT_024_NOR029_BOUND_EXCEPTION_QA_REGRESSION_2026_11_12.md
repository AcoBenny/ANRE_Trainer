# CKPT-024 | G1-NOR-029 | Correct normative max-bound vs allowed-height QA | 2026-11-12

**Decision:** prior single-assistant inference `AMBIGUOUS_MULTIPLE_TRUE` was a **false positive**. The stem asks to **fill the legal upper bound**, not select an arbitrary compliant installation height. It explicitly states **locuințe**; I7 §5.3.3.21 is 2.3m general, exception **2.5m** dwellings; hence **C candidate** vs stored **B**. This looks like a legitimate exam-scope exception trap, not a reason to rewrite the stem. Source edition/grade and independent reviewer still pending; **NOT_APPROVED**.

**Traceable supersession:** `QA_RULES/SEMANTIC_SUPERSESSION_INDEX_2026_11_12.csv`; preserved the original `DEEP_NOR_01_ALL_20_PRE_REVIEW_SOURCE_ABC_TRIAGE.csv` unchanged, and documented the corrected logic in `QA_RULES/NORMATIVE_LIMIT_SCOPE_SEMANTICS_V1_2026_11_12.md`.

**Prototype:** `tools/qa_normative_threshold.mjs` + 11-case `tools/tests/qa_normative_threshold.test.mjs`. The identical JS function logic was executed as synthetic fixtures in tool JS runner; first 2/11 PASS due to a brittle Romanian string pattern `pardosel`, fixed to `pardose`, reran **11/11 PASS**. Node/CI actual suite not run. No claims of independent expert/source QA.

**Control:** canonical question, A/B/C, stored B, HTML, APK and main untouched; PR #7 Draft, not merged. Grade I question candidate C remains proposed only. Global bank counts unchanged: 10/30 preliminary batches, 200/568 QABC units, 265/822 ID placements, 0/822 approved for learning.
