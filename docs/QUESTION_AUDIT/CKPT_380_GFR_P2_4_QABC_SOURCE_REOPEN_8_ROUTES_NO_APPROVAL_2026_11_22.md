# CKPT-380 | GFR P2: four exact QABC textbook source reopenings, eight grade routes (not qualified approvals)

Date: 2026-11-22. Audit branch: `audit/anre-v8-priority-17-20261109`. Parent: CKPT-379 / V291; PR #7 must stay Draft.

## Scope and anti-duplication

Exact canonical historical source is V141 (`docs/QUESTION_AUDIT/V141_568_QABC_MASTER_WITH_7_SOURCE_FIDELITY_DELTAS_2026_11_19.csv`), derived from workbook `ELECTROTEHNICA-09.2024-2.xlsx`. Original physical XLSX bytes were **NOT** available / reopened in this session. Source text and A/B/C below are **registry-native (V141)**, not independently re-extracted from raw XLSX.

Before declaring progress, inspected prior `CKPT_229_GFR_15_LEGACY_P2_G1_ELE_019_042_MATH_SWITCHGEAR_2026_11_18.md` and `CKPT_230_GFR_15_P2_ELE_044_062_HARMONICS_PROXIMITY_SKIN_2026_11_18.md`. All four were previously researched, and three previously cited the **same OpenStax chapter now reopened**. Thus: **0 previously unresearched QABC**, **4 source-context and A/B/C rechecks**, **8 grade routes touched**, **1 useful fresh distinct matching university source (TU Delft E×H)**, **0 independent qualified reviewer approvals**, **0 new canonical or examination-key authentication**, **0 learning approvals**. Do not subtract 8 from the 793 P2 pending professional-reviews queue.

## Exact candidate, three alternatives, scope and external source

### QABC-0023 | G1-ELE-027, G2-ELEC-176 | imported B/B retained

V141 original: „Care este energia consumata de o rezistenta electrica r = 10 Ω, prin care trece un curent de 2 A timp de 10 ore:”
- A `200 Wh` – contradicts E=I²Rt for stated numbers (would be 5 hours at 40 W).
- B `400 Wh` – affirmative E=(2A)² × (10Ω) × (10h) = 400 Wh.
- C `800 Wh` – would be 20 hours at same power.
- Pair checks A/B, A/C, B/C: unequal and no conditional simultaneous correctness with specified constant current/resistance/time. 40 W × 10 h, not 400 W.
- Physical scope: resistive loss and specified **constant** 2 A over 10 h, energy in Wh; not the generic energy of a reactive circuit with time-varying current.
- Reopened: OpenStax *University Physics 2*, §9.5, `P=I²R`, context before law of energy balance/Ohm, after alternative `V²/R` and thermal dissipation. https://openstax.org/books/university-physics-volume-2/pages/9-5-electrical-energy-and-power
- New research delta vs CKPT-229: independently recomputed distractor equivalents 5h/20h, not a new distinct primary educational reference.

### QABC-0032 | G1-ELE-039, G2-ELEC-185 | imported B/B retained

V141 original: „Conform Legii lui Coulomb, forţa de atracţie sau de repulsie care se exercită între sarcinile electrice este:”
- A `direct proporţională cu pătratul distanţei` – inverse-squared law contradicts.
- B `invers proporţională cu pătratul distanţei` – supported `|F| = k |q1q2|/r²`.
- C `direct proporţională cu distanţa` – contradicted.
- Pair checks: at nonzero point charges and fixed medium, B excludes A and C as functional dependencies; sign affects attraction/repulsion **direction**, not inverse-squared magnitude.
- Physical scope: two **pointlike** charges or equivalent applicable model with fixed charges and permittivity, electrostatic regime; do not generalize to arbitrary extended charge distributions without integration.
- Reopened: OpenStax *University Physics 2*, §5.3, preceding experimental inverse-square discussion, following signed charges and point charge scope. https://openstax.org/books/university-physics-volume-2/pages/5-3-coulombs-law
- New research delta vs CKPT-229: precise sign-versus-magnitude linguistic trap, not a new distinct reference.

### QABC-0033 | G1-ELE-040, G2-ELEC-186 | imported A/A retained

V141 original: „Constanta de timp a unui circuit format dintr-un rezistor de rezistenţă R înseriat cu un condensator de capacitate C, este:”
- A `RC` – affirmative `τ=RC`, units seconds (`Ω·F=s`).
- B `R/C` – dimensional units not seconds; false.
- C `1/(RC)` – reciprocal time / rate, not time; false.
- Pair checks: at finite positive R,C, these expressions can coincide numerically under arbitrary chosen unit-scaled values, but **not dimensionally / as universal physical equations**; A only time constant.
- Regime: single first-order ideal lumped RC loop; effective resistance rather than literal R if other nonideal or load resistances matter. An illustrative RC=2000Ω·10μF=0.02 s.
- Reopened: OpenStax *University Physics 2*, §10.5, charging/discharging context, `τ=RC`, time exponential. https://openstax.org/books/university-physics-volume-2/pages/10-5-rc-circuits
- New research delta vs CKPT-229: explicit dimensional negative tests and nonideal effective-R qualifier, not new distinct reference.

### QABC-0043 | G1-ELE-050, G2-ELEC-196 | imported C/C retained

V141 original: „Energia transmisă de undele electromagnetice cu intensitatea câmpului electric E şi intensitatea câmpului magnetic H se propagă după un vector:”
- A `S=E+H` – vector sum with physically incompatible field dimensions and does not encode energy-flux propagation.
- B `S=HxE` – negative of the properly oriented vector (`H×E = −E×H`); for nonzero waves points opposite propagation.
- C `S=ExH` – affirmative `S=E×H`, Poynting vector in W/m².
- Pair checks: A is not an electromagnetic power-flux vector, B has reversed direction vs C, and E×H is nonzero in propagating plane-wave regimes; degenerate zero-field values do not alter the intended law.
- New exact-notation university source **TU Delft, Basic Electromagnetic and Wave Optics**, §Electromagnetic Energy, Eq. (77), preceding energy density context and following oriented surface flux Eq. (78), explicitly `S(r,t)=E(r,t)×H(r,t)` and the time average for phasors only later. https://interactivetextbooks.tudelft.nl/tn2421/content/Chap1_Basics/Basics_2022_01Clean.html
- Existing prior source reopened: OpenStax *University Physics 2*, §16.3, Eq 16.28 `S=E×B/μ0` **in vacuum**. https://openstax.org/books/university-physics-volume-2/pages/16-3-energy-carried-by-electromagnetic-waves
- Source-scope check: H here is magnetic field strength (A/m), **not** B flux density (T). The TU Delft source closes the important exact E/H notation gap that OpenStax's E/B vacuum relation by itself leaves.
- Additional Warwick university PDF search exposed `S=E×H` eq. (5.19), but a mandatory PDF visual screenshot fetch **failed**; **not counted as visually verified PDF evidence**, and no passage copied or used as primary proof.

## Scope gate / exact-source QA

All four are physics/didactic, not legislative prescriptions. Exact physical object, action, unit, assumptions and alternative-by-alternative tests above match OpenStax/TU Delft. Current **2026 ANRE exam bibliography, original physical XLSX provenance and scored answer key remain NOT authenticated**. This is a single-assistant technical/linguistic recheck, **not** genuinely independent qualified technical and linguistic professional signoff. No word-for-word lengthy copyrighted paragraphs are reproduced; any final offline card quoting before/focus/after must be rights-cleared and source-original contextual text reopened.

## Release and queue invariants

- 568 QABC / 822 mapped grade routes retained.
- V283 queue counts unchanged: 27 P0 + 2 P1 + 793 P2 = 822. V291 all unapproved remains correct.
- This report adds **evidence, not new approvals**. P2 pending final independent reviewer still 793.
- No answer letter, canonical bank, XLSX, HTML, APK, learner gate, PR merge or release changed.
- Best next productive work: obtain an actually different qualified reviewer or a truly source-original XLSX; prioritize P0 disagreement and 2026 edition verification rather than repeating the same four OpenStax formula checks.
