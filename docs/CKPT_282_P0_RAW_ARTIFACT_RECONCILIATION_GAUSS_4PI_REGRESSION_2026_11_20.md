# CKPT-282 | Raw original-agent artifact reconciliation + newly observed Gauss 4pi error | 2026-11-20

## Scope and provenance
- Continuation of CKPT-281, **no new LLM API requests**. Re-opened real GitHub Actions ZIP contents:
  - [44771173694](https://github.com/AcoBenny/ANRE_Trainer/actions/runs/44771173694), artifact `14647426681` (`results.json`): three valid nonempty outputs, 7 attempts
  - [44772123757](https://github.com/AcoBenny/ANRE_Trainer/actions/runs/44772123757), artifact `14647492614` (three `results.json` files): two valid nonempty outputs, 4 attempts.
- Fixed canonical originals: `docs/ACADEMY_P0_NEXT_12_EXACT_QABC_2026_11_20.json` blob `db189edd918f5f780bb0ea75192b391deb165723`; exact supporting research blob `66a3fe0f35694fda732a177214b55f328da5849d`.
- Method: re-read all **five actual** role texts, compare each A/B/C against each other, source statements, exact original question and independently recomputed arithmetic. Two distinct AI model outputs are **not human-independent professional signoff**, source authentication, or an exam scored key.

## Case-by-case reconciliation (original QABC unchanged)

### QABC-0036 (G1-ELE-043 / G2-ELEC-189), generator stator current
- Gemini skeptic + Groq technical are both physically conditional and broadly reject unconditional direct proportionality to one variable. This is a **conditional model interpretation**, not universal generator behavior and not a determination of official answer letter.
- The **actual** Groq technical raw text says `P=10 kW, Q=8 kVAr, U=400 V => I=12.8 kA`; incorrect **both arithmetic and scale**. In balanced 3-phase sinusoidal regime, `I = sqrt(P^2+Q^2)/(sqrt(3)*U)`, thus **18.484 A**, then **14.787 A** for 500 V (P/Q fixed), **45.644 A** for Q=30 kVAr at 400 V. `P=10 kW, Q=0, U=400 V` gives **14.434 A**. The raw text also says `31.6 A` when Q=30 kVAr; **31.623 kVA is apparent power, not line current**.
- Additional issue in raw Groq: “B is sufficient only if Q constant and negligible” is an **approximation**, not exact direct proportionality for nonzero Q. “Q negligible” and “Q=0” must never be conflated. An engineering guide's balanced three-phase formula is not a source-authenticated generator operating mode.
- Sources: Schneider Electric https://www.electrical-installation.org/enwiki/Definition_of_reactive_power .
- **Status: TWO_AI_ROLE_TEXTS_READ / MATH_DEFECTS / PHYSICAL_AND_EXAM_SCOPE_UNRESOLVED / NOT_APPROVED**.

### QABC-0050 (G1-ELE-057 / G2-ELEC-203), harmonic periods
- Both real role texts are present. `f_n = n f_1` and `T_n=T_1/n`; second harmonic yields `T_2/T_1=1/2` while reversed ratio is 2. Third harmonic demonstrates **C not necessary**, not that **C is false as a sufficient special case**.
- Actual Groq text calls equal-period B “necessary but not sufficient”, and its attempted counterexample only shows that it is **not necessary**: incorrect quantifier logic. If `n=1` is admissible, equal periods are sufficient for that case but not necessary for n>1; if only nontrivial n>=2 counts, equal-period B is not a sufficient harmonic case. Do not silently choose between conventions.
- Actual Groq A says generic integer ratio is “necessary and sufficient” but doesn't define which period is numerator, whether the ratio is `n>=1`, or whether equal-frequency sinusoidal components qualify. Source alone cannot turn A/B/C into unique, exclusive choices.
- Actual Gemini text argues that the n=3 counterexample “contradicts” C's 1/2, a **necessary-versus-sufficient** error when used to dismiss its n=2 validity. It does show C is non-exhaustive.
- Source: UNSW https://newt.phys.unsw.edu.au/jw/harmonics.html .
- **Status: TWO_AI_ROLE_TEXTS_READ / QUANTIFIER_CONFLICT / TERMINOLOGY_SCOPE_UNRESOLVED / NOT_APPROVED**.

### QABC-0065 (G1-ELE-073 / G2-ELEC-218), flux of enclosed charge
- Groq technical **one model response only**; independent skeptic failed (Gemini 503; Requesty network timeout). Do not claim two reviews.
- Gauss flux of **E**: `integral(E·dA)=q/epsilon0` (SI vacuum). Flux of **D**: `integral(D·dA)=q_free` (SI with proper distinction of free charge). Original question only says `flux electric total` and does not specify E, D, units or q type. Thus B=q is source-dependent, **not an authenticated exam key**.
- Self-contradiction confirmed in real technical text: it cites `D=q_free` then asserts no source supports unscaled q.
- **New numeric error not yet in CKPT-281:** technical model writes `q=1 C => E-flux ~8.99 x 10^9 V·m`. NIST CODATA 2022 `epsilon0=8.8541878188e-12 F/m`; therefore **`q/epsilon0=1.1294090666 x 10^11 V·m`**. `8.98755 x 10^9` is **`1/(4*pi*epsilon0)`**, Coulomb's constant, erroneously substituted for a closed-surface E-flux. The missing `4*pi` cancels under the surface integral, as OpenStax explains.
- Source: OpenStax https://openstax.org/books/university-physics-volume-2/pages/6-2-explaining-gausss-law ; NIST https://physics.nist.gov/cgi-bin/cuu/Value?ep0 .
- **Status: ONE_AI_ROLE_ONLY / MATH_AND_SELF_CONTRADICTION / DEFINITION_AND_2ND_REVIEW_BLOCKED / NOT_APPROVED**.

## Regression enhancement / safety
- Updated `scripts/academy_p0_source_conditioned_review.py`: NIST-backed numeric **reference only** for q=1 C; conservative observed-error flag `GAUSS_E_FLUX_CONFUSED_WITH_COULOMB_CONSTANT`. Does not infer an answer letter.
- Updated `tests/test_academy_p0_source_conditioned_review.py` with two new tests: flux formula vs Coulomb constant and a positive-negative-unrelated check to avoid mistaking normal references to Coulomb's constant for wrong flux answers.
- The earlier 17/17 pass applies **only to prior commit**; these newly added regressions have **not yet received a verified current-head CI green run** in this checkpoint. No invented test counts. No external API rerun, no human signoff.
- Do **not** silently merge old first-run artifact status and retry-run status in the live pilot program: reconciliation here is a **documented audit of evidence**, not a change to the scoring or automatic certification.

## Priority after this checkpoint
1. Validate code changes with full offline regression at current HEAD, preserving 0 API cost; flag any failures.
2. Recover authentic official ANRE Electrotehnica workbook **bytes** / bibliography and answer-key provenance; the official XLSX link is visible but binary download was still unsuccessful. Without it, original key cannot be declared official in 2026.
3. QABC-0065 second independent review only on a materially different working free route or quota reset, and genuine source/definition review. QABC-0024 requires verified original drawing transfer, not reconstruction.
4. Keep exact source scope, A/B/C alternatives, textual ambiguity and human professional signoff **distinct gates**.

**NO learner approvals; NO original QABC/key/HTML/APK/main edits; NO merge or release. PR #7/#13 remain Draft.**
