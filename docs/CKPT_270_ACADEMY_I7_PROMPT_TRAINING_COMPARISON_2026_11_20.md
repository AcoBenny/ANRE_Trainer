# CKPT-270 | Academy prompt training v1 vs v2, actual I7 traces | 2026-11-20

## Actual executions
- First baseline vs training v1: 8/8 real model outputs [run 44756577552](https://github.com/AcoBenny/ANRE_Trainer/actions/runs/44756577552). Groq GPT-OSS-120B and Gemini 3.5 Flash-Lite, two genuine source-vs-trainer QABC 0362 and 0386, each run baseline and trained independently on identical original workbook options and identical 2023 user-provided I7 excerpts.
- Source-transfer instruction v2 changed but all original question text/keys remained untouched. Second actual 8/8 evaluation: [run 44757359918](https://github.com/AcoBenny/ANRE_Trainer/actions/runs/44757359918). All model calls finished and returned nonempty output; this does **not** mean technical correctness.
- 16 total model outputs across those two experiments. Neither a statistically powered benchmark nor proof of future model performance. Both used same primary models per role. **Model weights not modified** and no learned skill automatically released.
- All outputs and provider usage in temporary Actions artifacts. No API secret exposed. No paid OpenAI calls.

## Scoped manual source-logic QA of model output (not independent professional verification)
| Case | v1 defect visible | v2 observation | Gate |
| --- | --- | --- | --- |
| `QABC-0362`, I7 §5.4.13 (doorbell supply) | Both technical variants incorrectly treated original nonexclusive C `dintr-un circuit de prize` as false for not listing all three permitted supplies; trained skeptic also claimed no original choice matched | Trained technical A/B/C section now identifies original C as nonexclusive permitted example; still contradicts itself in PAIRS by treating C as effectively exclusive. Trained skeptic describes C as incomplete but does not explicitly certify it as source-supported | **FAIL for reliable semantic logic**, need no implied quantifier and affirmative allowance evidence |
| `QABC-0386`, I7 §5.5.2.3 (main earthing terminal) | Original B says `fără utilizarea unei scule` versus source `numai prin intermediul unei scule`; original C individually disconnectable is supported but partial. Baseline mixed good and unsupported-standard arguments | Trained technical recognizes original B negation but falsely says trainer B lacks evidence for only-with-tool even though this is expressly in supplied source. Skeptic recognizes original C as partially true but suggests original options all fail if they omit one additional requirement | **FAIL for unconditional semantic signoff**, distinguish true incomplete from false, and no refusal to accept exact supplied text |

## Validated narrow learning for next pilot
- **Improved structure is not improved truth**. Require both vertical stem ↔ A/B/C and horizontal A-B/A-C/B-C, with exact option quantifiers preserved.
- Logical training rule: nonexclusive permitted Y is not false because source permits X OR Y OR Z. An explicit `numai Y` contradicts permitted X/Z. `individual` requirement remains true even where the norm additionally specifies tool; explicit `fără sculă` is contradicted by `numai cu sculă`.
- The two excerpts are from a user-provided **2023** I7 PDF, not newly authenticated 2026 normative edition. No official scored key, no qualified independent expert signoff. **0 ANRE learner approvals**.
- Next P0 questions are triage only, and original source diagrams missing from the *queue* must block model execution even where prior CKPT-255 recovered a drawing. No original ANRE XLSX or question-bank text/key change; PR #13 and PR #7 Draft.

## Future specific tests
- Add a source-aware QA negative for fabricated word `ONLY` / `numai` in an original option that does not contain it.
- Do not mistake a source sentence omission for a contradiction; require comparing exact object, action, condition, qualifiers, previous/next context.
- Specialist skill training can be promoted only after a blind held-out source-grounded review, not this one-pilot comparison.
