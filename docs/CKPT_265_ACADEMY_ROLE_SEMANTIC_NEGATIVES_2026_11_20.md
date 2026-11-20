# CKPT-265 | ANRE Avengers Academy: first four real-QABC role trials and adverse findings | 2026-11-20

## Execution evidence
- 4 distinct original QABC = 8 grade placements, original source choices preserved verbatim from V149. Run [44736791421](https://github.com/AcoBenny/ANRE_Trainer/actions/runs/44736791421): 9/9 live model responses across Groq/Gemini/OpenRouter, **no paid OpenAI call**. The workflow correctly returned `failure` because the sceptic on QABC-0004 omitted explicit review of original A and C; network success is not source correctness.
- Targeted **only-role** retest QABC-0004 skeptic: run [44737794130](https://github.com/AcoBenny/ANRE_Trainer/actions/runs/44737794130), 2 real Gemini calls (first still incomplete A/B/C, second correct format). Neither the other 3 cases nor the technical model were repeated. QA status `ROLE_RETEST_PRESENT_NOT_RECONCILED`, **not** a substitute for two independent reviewers.
- The original technical model response for QABC-0004 was preserved in the earlier artifact and does not have to be repeated. Both artifacts expire after retention period; this checkpoint retains conclusions, not raw secrets.

## Independent content QA findings, NOT an approval
| Unit | Observed model weakness | What separate source/physics evidence suggests |
| --- | --- | --- |
| QABC-0001 | Three models responded, but grid voltage increase is context-dependent; model speculation cannot prove an official key | Compare fixed-network compensation with regulated voltage counterexample. Primary source/edition and exam grade not authenticated |
| QABC-0002 | Technical model fabricated `PSI = Presiune, Securitate, Izolație` and conflated arc-suppression Petersen coils with generic shunt-reactors/power-factor correction. Skeptic disagreed and correctly discussed ground-fault capacitive current | `PSI` ordinarily stands for `prevenirea și stingerea incendiilor`. Need exact-scope primary source; do not accept fluent general reactor talk |
| QABC-0003 | Both discussed A/B/C, but reviewer overgeneralized physical exclusivity and quibbled about sources beyond the non-exclusive original C | Original A/B have `numai`, original C lists two valid field sources without claiming these are exhaustive |
| QABC-0004 | Technical model supported B=250 μF but invented implausible fault counterexamples. Skeptic first omitted A/C; later retest **explicitly said B=250 μF and then that none of A/B/C matches 250 μF**. This is direct self-contradiction, not an unresolved capacitance calculation | Three parallel capacitors add `100+50+100=250 μF`, original B=250 μF. Formal official ANRE scored key remains unverified |

## Academy lessons registered as **unpromoted candidates**
- Full A/B/C review required, not mere mentions; targeted re-ask at most once per role and preserve both responses.
- Validate exact physical object and correct acronym, not a related term or fabricated expansion.
- Search for internal numeric contradictions after structured-looking answers. A/B/C headings do not ensure truth.
- Role outputs are independent only if separately invoked and actual serving-model IDs are not the same; provider fallback may reduce diversity.
- Positive model response and even 9/9 role calls **do not constitute verified content QA**, source authentication or professional signoff.

## Controls and next step
- New conservative QA regression flags for QABC-0002 `POSSIBLE_PSI_ACRONYM_HALLUCINATION` and QABC-0004 `POSSIBLE_NUMERIC_SELF_CONTRADICTION`; both **require human follow-up** and don't directly certify a wrong official key.
- Offline regression suite verified in [GitHub Actions](https://github.com/AcoBenny/ANRE_Trainer/actions/runs/44738234473); current exact branch and all test work in PR #13 Draft.
- Next free API evidence batches: QABC-0005–0008 then QABC-0009–0012. The next gated workflow runs both sequentially and records each separately without silently skipping a later group if earlier model QA is incomplete.
- **Zero original QABC/answer key/HTML/APK changes; 0/822 learner-approved**, audit PR #7 remains Draft.
