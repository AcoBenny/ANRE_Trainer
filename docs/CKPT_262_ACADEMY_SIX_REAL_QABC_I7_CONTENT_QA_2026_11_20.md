# CKPT-262 | Six REAL source-vs-trainer QABC cases: 12 model traces + original I7 check | 2026-11-20

**Source materials actually inspected:** (a) the full 12 original model outputs in the [GitHub Actions artifact](https://github.com/AcoBenny/ANRE_Trainer/actions/runs/44733533497), (b) exact original vs trainer options and source workbook cells in audit [V144](https://github.com/AcoBenny/ANRE_Trainer/blob/audit/anre-v8-priority-17-20261109/docs/QUESTION_AUDIT/V144_SIX_RELEASE_BLOCKERS_SOURCE_VERSUS_CANONICAL_ADJUDICATION_2026_11_20.csv) and V140, (c) **user-provided** `803493174-I7-2011-completat2023.pdf`, PDF pages 70 and 72, visually inspected in this review. This PDF declares *forma sintetică pentru 2023-09-22*. The online official Portal Legislativ returned HTTP 502 in this session, so **2026 authoritative applicability remains open**.

## Measured actual execution
- Separate Groq GPT-OSS-120B technical and Gemini 3.5 Flash-Lite skeptic: **12/12 API responses**, all with positive termination statuses `stop` / `STOP`, 0 OpenAI paid calls; run [44733533497](https://github.com/AcoBenny/ANRE_Trainer/actions/runs/44733533497).
- Source ledger six distinct exact QABC groups (nine grade placements) was pinned to Git blob `0fae5c2e3653c4cea2ced456ca768ddb01db733e`.
- Original official question/answer score key **not authenticated**. At most preliminary source/technical judgments: **0/822 approved**, 0 professional independently approved.

## Evidence-based correction matrix

| Case | Source-vs-trainer fidelity | Actual model problem | Evidence-based QA |
| --- | --- | --- | --- |
| `QABC-0017` G1-ELE-018/G2-ELEC-170 | Q/A/B/C **identical**, grade keys A/C collide | Groq incorrectly asserts B `Cs=C/3` by unspecified “series-parallel” mechanism; Gemini recognizes 3C as alternative but does not authenticate textbook meaning | Balanced `Va+Vb+Vc=0` with each interphase C gives `q_a=C(Va-Vb)+C(Va-Vc)=3C Va`. Candidate A **conditional** on per-phase service-capacitance definition. Needs exact Romanian text & qualified review. |
| `QABC-0094` G1-ELE-102/G2-ELEC-245 | Q/A/B/C **identical**, grade keys A/C collide | Groq declares cold-standby A a universal preferred setup and cites irrelevant/unverified normative names; Gemini correctly recognizes missing operating criteria | Do **not** select a universal preferred topology without explicit dispatcher/operation scheme and exact transverse-coupler source. |
| `QABC-0143` G1-ELE-152 | Source stem `adimensională` vs trainer `caracteristică`; ABC same | Groq incorrectly treats attenuation coefficient α in Np/km as dimensionless and suggests B for original, then A for trainer; Gemini identifies inverse-length dimension | Propagation constant γ=α+jβ has units inverse length; product γL is dimensionless. Restoring exact stem is a provenance decision, **not** automatic source-truth approval. |
| `QABC-0236` G1-ELE-247/G2-ELEC-383 | B source `inducţie electromagnetică`; trainer B `inducţie electrostatică` | Groq asserts original A conduction is uniquely correct from absent contact conditions; Gemini properly challenges net charge of isolated conductor | Static electric field polarizes isolated neutral conductor but does not give net charge without additional process. No unconditional original exam key. |
| `QABC-0362` G1-NOR-048 | Raw textual differences stem,A,B,C; **material lexical changes A,C**, stem/B mainly spaces | Groq fabricates exclusive STAS-like panel-only rule, calls trainer's three choices noncompliant, contrary to the user I7 | **Actual source opened and visually checked:** I7 PDF p70 §5.4.13 explicitly permits normal lighting circuit, socket circuit **or** direct distribution board. Workbook original C `dintr-un circuit de prize` technically allowed; trainer A enumerates all three; trainer C adds `numai`, falsely exclusive. Official scored workbook answer not verified. |
| `QABC-0386` G1-NOR-072 | Raw changes stem,B; **material lexical B only**, stem whitespace | Groq says tool not mandatory and rejects trainer B, a repeat of the original false-negative source error; skeptic does not quote primary evidence | **Actual source opened and visually checked:** I7 PDF p72 §5.5.2.3 requires each conductor individually disconnectable and the connection secure and disconnectable **only using a tool**. Original workbook B says `fără utilizarea unei scule`, trainer B corrects to `numai prin intermediul unei scule`. No transfer of trainer B to original workbook B. |

### Special QA lessons
1. **Source-scope hallucination is the blocker, not network API availability.** Groq gave several fluent but unsupported or demonstrably contradictory claims. Gemini acted as a useful skeptic but did not substitute for independently opening the sources.
2. **Field-level correctness:** compare both verbatim and whitespace-normalized original A/B/C to avoid labeling spaces as material semantic mutations. Never alter the original field while scoring.
3. **Two-stage approval:** technical plausibility + source paragraph, grade/edition/exceptions + exact A/B/C + independent qualified review. AI consensus and `finish_reason=STOP` only prove response completion, **not** learner correctness.

## Academy fixes implemented after failures
- Provider adapter records completion reason and rejects truncated responses.
- Source version and trainer version are separately presented, no old key or candidate hidden hints shown to the reviewer.
- Whitespace-normalized difference report added; raw text kept exact.
- Genuine regression examples now include false universal answer, invented STAS citation, wrong dimension of α, contradiction with I7 paragraphs 5.4.13/5.5.2.3.

## Release posture
PR #13 remains Draft, PR #7 (audit) Draft; no QABC, official answer key, HTML or APK edits; no merge/release. Source I7 PDF is user-provided 2023 synthetic text, **not independently confirmed to be all 2026 consolidated amendments**. Proceed next with other flagged original-copy-match questions under same source-verbatim/fidelity discipline.
