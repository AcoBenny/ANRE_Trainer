# CKPT-263 | ANRE Academy next 12 exact-source QABC | preliminary technical triage | 2026-11-20

## Scope and safeguards
- Read-only triage of `docs/ACADEMY_NEXT_12_EXACT_SOURCE_QABC_QUEUE_2026_11_20.json`, generated from the **actual** audit V149 CSV (12 distinct QABC; 24 grade placements).
- **Not** an independently invoked model benchmark, source-authenticated normative audit, certified SME review, or approved exam answer key.
- All suggestions below are **conditional technical hypotheses**, not canonical key changes. No source workbook, original question, canonical A/B/C, HTML, APK, audit PR #7 or merge modified.
- The original copy-match in V149 establishes fidelity to a Library workbook copy, **not** official server provenance, correct exam key or source edition.

## First-pass triage, explicit A/B/C elimination and exceptions
| Unit | Provisional physical reasoning (NOT scored key) | Scope / negative-test risk |
|---|---|---|
| QABC-0001 | Shunt capacitive compensation often raises local voltage by reducing inductive reactive drop; C plausible | Not universal: regulation, loading, switching, network topology; B possible under regulated bus. Need circuit assumptions |
| QABC-0002 | Petersen/arc-suppression coils compensate capacitive earth-fault current; C plausible | Do not confuse reactive power factor correction with ground-fault neutral compensation |
| QABC-0003 | Permanent magnets and energized electromagnets both produce magnetic field; C plausible | A/B contain unjustified `numai`. General magnetic fields also arise from other moving charges, not only these two |
| QABC-0004 | Parallel capacitors add: 100+50+100 = **250 μF**, B mathematically supported | Formula presumes ideal capacitors connected in parallel, as stated. Direct arithmetic check |
| QABC-0005 | Independent KVL loop count for a connected network is `L−N+1`, B plausible | **Connectedness not stated**: with `k` connected components it is `L−N+k`. Need clarify implicit connected network |
| QABC-0006 | Automatic transfer of reserve supply (AAR) improves supply continuity; B plausible | Do not conflate with short-circuit limiting or line-loss reduction |
| QABC-0007 | Motoring asynchronous machine normal slip `0<s<1`; A plausible | Generator mode has negative slip; plugging/braking can have s>1. Original stem omits operating regime; flag ambiguous/generalized |
| QABC-0008 | Compensation reactor and tap-changing transformer are standard voltage regulation tools; resistor C plausible as exclusion | Resistive elements can change voltage in specific circuits; term `reglarea tensiunii în reţele` needs utility-grid context |
| QABC-0009 | Induction motors are widespread for auxiliary drives in power plants; C plausible | Empirical prevalence needs source by plant type and date, not mathematical certainty |
| QABC-0010 | Short-circuit limiting reactors rely on high inductive reactance; B plausible | A high resistance is not the usual power-reactor mechanism; distinguish L from R |
| QABC-0011 | Electric-field intensity E is a valid descriptor of electrostatic field; A plausible | Original question ends `descris` and A starts `prin:`, a **split-stem formatting hazard**. B has `numai`, C names magnetic induction. Preserve exact source while flagging UI rendering |
| QABC-0012 | Oil-immersed transformers may require oil containment/fire/environmental provisions; C plausible | Dry vs liquid-immersed installations differ by oil type, size, location and fire rules. A is contrary to ordinary mineral-oil risk; B depends on construction and measurements |

## What is actually resolved
- **12/12 original QABC read and provisionally reasoned**, including explicit alternative rejection and physical assumptions.
- **0/12 independently source-authenticated or SME-approved**. No user-facing learning approval.
- Four priority semantic flags for next adversarial review: **QABC-0001** (regulated voltage), **QABC-0005** (connectedness), **QABC-0007** (slip regime), **QABC-0011** (split-stem display). Other scope flags in table remain open.
- The tentative letter labels above must **not** be written into any canonical key. They are reviewer hypotheses only.

## Next gate
1. Obtain primary-source paragraphs/edition for each, plus official exam-sample original and scoring provenance. Verify 2026 applicability where relevant.
2. Have two separate blind API reviewers challenge **the full exact QABC** with no imported answer letters, then score outputs against independent source/physics rubric; preserve full trace and finish reason.
3. Independent qualified electrical SME and language QA resolve exceptions before approval. Keep original wording for exam-mode; didactic annotations may be added only after approved source decisions.

PR #13 remains Draft. Audit PR #7 remains Draft. No release.
