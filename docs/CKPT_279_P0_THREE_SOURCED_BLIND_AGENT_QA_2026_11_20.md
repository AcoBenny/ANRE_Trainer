# CKPT-279 | P0 ANRE original QABC + direct source-physics conditions | 2026-11-20

## Progress and original provenance
- **Three original workbook-copy matched questions**: QABC-0036, QABC-0050, QABC-0065 (6 grade placements) exactly pulled from pinned `ACADEMY_P0_NEXT_12_EXACT_QABC_2026_11_20.json`; original source workbook references are the 09/2024 Electrotehnica material. Original question text and A/B/C were **not edited**.
- ANRE official page **currently links** [ELECTROTEHNICA-09.2024-2.xlsx](https://anre.ro/wp-content/uploads/2024/11/ELECTROTEHNICA-09.2024-2.xlsx) under 'Exemple întrebări': https://anre.ro/participanti-la-piata-de-energie/persoane-fizice/energie-electrica/ . The official XLSX link was opened but binary retrieval was unsuccessful in this session, so **the official worksheet cell values and any official scoring cells have NOT been compared byte-for-byte**. Current exact-original fidelity remains to the versioned user Library workbook copy; do not pretend direct official workbook validation occurred.
- The public [ANRE examination syllabus/bibliography, edition May 2023](https://anre.ro/wp-content/uploads/2023/05/Tematica-si-bibliografie-pentru-examenul-de-autorizare-electricieni-2023-.pdf) page 1 (printed) lists basic electrotechnics, measuring and machines as material for I and II, with specialist textbooks possible; public PDF does **not** provide unique scored answer letters to the three analyzed QABC. The page listing 2024 workbook does not prove its answer letters are certified exam keys in 2026.
- Pinned external engineering source summary and exact QABC in `docs/ACADEMY_P0_THREE_SOURCED_PHYSICS_CASES_2026_11_20.json`, Git blob `66a3fe0f35694fda732a177214b55f328da5849d`; 2026 ANRE key status **NOT VERIFIED**.

## Separately reopened original source references; do not promote to exam scored keys

### QABC-0036: generator stator current 'direct proportional'
- Public Schneider Electrical Installation Guide https://www.electrical-installation.org/enwiki/Definition_of_reactive_power
- `S²=P²+Q²` and (balanced sinusoidal 3-phase) `S=√3·U·I` => `I=√(P²+Q²)/(√3·U)`.
- Direct proportionality with isolated P or Q requires specifying constraints (e.g., reactive/active component, U fixed and P=0) and does not universally follow from original stem. Counterexamples must keep actual operating conditions; **A/B/C not scored**.

### QABC-0050: pair of harmonic sinusoids
- UNSW Physics https://newt.phys.unsw.edu.au/jw/harmonics.html describes `f_n=n f_1` and `T_n=T_1/n`. For n=2, fundamental-to-harmonic period ratio is 2 while reverse is 1/2. Fundamental is the lowest harmonic in that source (n=1).
- A is generic integer period ratio; B equal periods can mean n=1; C a 1/2 period ratio can be valid in the **reverse order**. Without defining numerator direction and whether n=1 counts as a harmonic, more than one alternative can appear true. Do not silently treat A/B/C as exclusive. Mark **SOURCE_SCOPE_AMBIGUITY**.

### QABC-0065: enclosed 'total electric flux'
- OpenStax https://openstax.org/books/university-physics-volume-2/pages/6-2-explaining-gausss-law has `∮E·dA=q/ε0` in SI vacuum, while Virginia Tech Electromagnetics https://publishing.vt.edu/en/books/71/files/089f0317-2cfd-4eb5-ad14-d7f101a9e4b2.pdf section 5.5 uses `∮D·dA=q_enclosed` (for correct interpretation of charge).
- Original stem does not say **E**, **D**, unit system or whether q is free charge; option B `q` is justified only for `D` flux/convention, not by silently replacing original E flux. Original A/C are numeric multiples but no verified key.
- Require exact original ANRE course definition and grade/edition before scoring.

## Independent Academy work
- `scripts/academy_p0_source_conditioned_review.py` sends identical original QABC + source-derived paraphrases/equations to **two independent blind reviewer roles**, Groq GPT-OSS-120B and Gemini 3.5 Flash-Lite, each with at most one pinned Requesty Gemma free fallback. User data and original answer keys are never sent; original question texts are ANRE examples, not confidential key records.
- Output is raw text and model IDs with format/independence gates only. Not an automated semantic truth or professional SME certificate.
- **10/10 offline source-grounded QA tests PASS**, including source-QABC comparison to the original pinned queue, E vs D flux, harmonic ratio, missing-source fail-closed, blind data, copied-only A/B/C false-positive, duplicate model fallback, dry-run zero calls. GitHub Actions: https://github.com/AcoBenny/ANRE_Trainer/actions/runs/44770814245 .
- This explicit **[p0-source]** commit launches exactly 3 QABC × 2 specialist roles, maximum 12 free provider requests with per-case artifact persistence. No paid OpenAI calls; real model outputs to be inspected before expanding.

## Safety gates
- No 2026 official question/answer key provenance certified. No independent qualified examiner or SME signoff. **0 new learner approvals**, no question/answer-key/HTML/APK/main changes, no merge/release; audit PR #7 and Academy PR #13 both Draft.
- Next: inspect actual individual model output and counterexamples; add negative semantic QA rules where models produce unsupported E/D substitutions, scalar ratio interpretation or unjustified proportionalities. Recovered original 22-shape QABC-0024 drawing must be accurately attached to model prompt before evaluation.
