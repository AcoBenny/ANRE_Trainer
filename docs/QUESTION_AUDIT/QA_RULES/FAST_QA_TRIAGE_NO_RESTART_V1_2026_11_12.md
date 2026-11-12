# Fast QA triage v1 | no restart | 2026-11-12

## Decision
Do NOT restart 822 ANRE questions after the CKPT-024 false ambiguity fix. **Evidence and prior unit classification remain valid as historical research** except where the corrected semantic interpretation directly changes a candidate verdict. Do not silently overwrite CKPT-022 or canonical barems.

## Exact scan facts (script-style screening, not total proof)
- Canonical bank: **822 IDs**, **568 distinct QABC units** in `UNITS_568.csv`, i.e. **254 repeat ID placements**. Research each exact unit once while checking grade and original stored key individually across placements.
- CKPT-023 baseline: **10/30 deep batches pretriaged, 200/568 units, 265/822 ID placements, 0/822 approved**. Do not count research completion as signoff.
- A deliberately narrow numeric bound screening (markers `maximum/minimum/nu depășească/depășește/cel puțin/până la`, plus numeric answer with units) surfaced **7 IDs / 7 distinct units**. **6** warrant targeted normative bound/intention inspection and **1** (`G1-NOR-005`) is a false positive: `cel puțin` modifies **three measurements**, but the answer blanks ask a **distance**. Only **6 out of 7** should enter a *bound-specific* recheck; not a claim that these are the only questions possibly affected by context errors.
- An independent lexical scan found **33 ID instances/24 units** containing selected absolute/trap markers (`numai/întotdeauna/obligatoriu/fără/excepție` etc). These are *candidate traps*, not 33 proven problems. A separate rough V95 label scan found **29 IDs/25 units** containing markers `AMBIGU/MULTIPLE/NO_OPTION/REWRITE/CONDITIONAL` in preliminary labels. These sets may overlap, and V95 label scan is incomplete and need not reflect newest CKPTs. DO NOT sum them or treat count as number of true errors.

Queue: [targeted limit triage CSV](TARGETED_SEMANTIC_BOUND_RECHECK_2026_11_12.csv). No source certifications or key changes.

## Lightweight pipeline
1. **Reuse existing evidence** by exact `unit_id` and source-object/edition, do not search the same question again solely due to CKPT-024; compare all linked grade IDs for key differences.
2. **Classify intent before A/B/C:** requested *normative bound* => compare exact threshold after applying matched exceptions; requested *compliant examples* => test inequalities; minimum/maximum can point in opposite direction; bind every quantifier to the exact measured noun/target (example NOR005: "cel puțin" applies to measurement count, NOT answer distance). Never infer answer via word-only regex.
3. **Fast-track source-backed deterministic cases** (series capacitor arithmetic, formulas with stated assumptions) with explicit small calculation and source/second-method cross-check. Reviewer checks only evidence and alternatives rather than doing a fresh broad search. Source version and scenario conditions must match.
4. **Escalate only flagged conflicts:** missing figures, contradictory grade keys, genuine multiple-answer uncertainty, changed laws, ambiguous object/scope/edition. Preserve original exam-style questions and traps; store proposed key as `NOT_APPROVED`; do not auto-rewrite canonical stem.
5. **Closure ledger** per exact ID: `CLEAR_PENDING_INDEPENDENT_QA`, `KEY_CONFLICT_PENDING_INDEPENDENT_QA`, `TRAP_VALID_SUPPORTED`, `TRUE_AMBIGUITY_UNRESOLVED`, `BLOCKED_SOURCE_SCOPE`; switch to `APPROVED_FOR_LEARNING` only with sufficient distinct reviewer evidence and correct 2026 applicable bibliography. Do not certify actual agent independence unless independently invoked/reopened. Report **number resolved + number blocked + exact blockers**, not only `lots researched`.
6. **Sample-check risk**: run full ABC QA on every key conflict; for fast-tracked clear answers check exact source and use additional sampled regression tests to detect routing mistakes. Sampling does NOT replace final per-question reviewer signoff where required.

## Safe status
This change is a **routing proposal / candidate shortlist**, not an executable change to the canonical bank, no full rerun of all 822; `Perplexity` remains paused. `tools/qa_normative_threshold.mjs` is a narrow proof of concept with 11 synthetic PASS cases, not a general semantic engine or a source validator. `CKPT-024` has the original error and full explanation. No HTML/APK/main/merge/release changes.
