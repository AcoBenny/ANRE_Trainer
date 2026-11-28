# CKPT-228 | GFR 15 P2 legacy prelim electrotechnics circuit and magnetic exceptions | 2026-11-18

## Source and control
- Exact canonical V73 Git blob `c027d417a8e4e605c830b2016fb55b099b8d130b`, 15 prior `PREVIOUS_INDIVIDUAL_PRELIMINARY_NO_SIGNOFF` question records with no prior new focused evidence; all original A/B/C and imported keys copied mechanically. Scholarly + engineering public URLs are distinguished from **specific matched source evidence**, with missing direct proof explicitly blocked.
- New reasoning in single ChatGPT session only, not independent reviewer. No canonical mutation, no HTML/APK/app/main, no release or merge; learner approvals=0.

### G1-ELE-030 | CONDITIONAL_ALL_NETWORK_VOLTAGE_LEVELS
- Original: Scheme cu un sistem de bare colectoare şi un întreruptor pe circuit sunt folosite
- A: numai pentru staţii de conexiuni de 6 kV
- B: pentru toate treptele de tensiune din reţelele de distribuţie
- C: numai pentru staţii de conexiuni de medie tensiune până la 6o kV
- Imported key **B** untouched; source workbook `ELECTROTEHNICA-09.2024-2.xlsx` row `37`.
- Source (scope as qualified below): https://eepower.com/technical-articles/substation-componentspart-5-busbar-configurations/
- A/B/C physical model and negative-case reasoning: A only 6kV unjustifiably restricts configuration, B single-busbar/one-breaker usable at diverse distribution voltage levels, C only up to '6o' kV again absolute. No definitive evidence every distribution voltage uses this scheme in practice; 'toate' denotes applicability not deployment.
- `approved_for_learning=NO`, `independent_QA=NOT_RUN`, `ANRE_2026_OFFICIAL_KEY=NOT_VERIFIED`.

### G1-ELE-033 | CONDITIONAL_DRY_TRANSFORMER_FIRE_RATING
- Original: Comparativ cu cele imersate, transformatoarele uscate prezintă :
- A: o bună rezistenţă la foc;
- B: risc redus de poluare acustică a mediului ambiant;
- C: necesitatea unor amenajări speciale la instalare
- Imported key **A** untouched; source workbook `ELECTROTEHNICA-09.2024-2.xlsx` row `40`.
- Source (scope as qualified below): https://www.se.com/us/en/work/support/resources-and-tools/technical-faqs/
- A/B/C physical model and negative-case reasoning: A dry type typically avoids flammable oil so reduced fire burden, not inherently guaranteed fire-resistance of every design. B acoustics design-specific and may not always be lower; C oil containment tends to demand more environmental arrangements. Manufacturer link is a general help resource, *not directly pinpointed comparison*, so source verification not sufficient.
- `approved_for_learning=NO`, `independent_QA=NOT_RUN`, `ANRE_2026_OFFICIAL_KEY=NOT_VERIFIED`.

### G1-ELE-034 | DIRECT_IDEAL_ISOLATED_NEUTRAL_EARTH_FAULT
- Original: Daca la un circuit al unei staţii de 6 sau 20 kV care funcţionează cu neutrul izolat apare o punere monofazatã netã la pământ, tensiunea fata de pământ a celorlalte doua faze:
- A: scade de 1,41 ori
- B: rămâne constanta
- C: creste de 1,73 ori
- Imported key **C** untouched; source workbook `ELECTROTEHNICA-09.2024-2.xlsx` row `41`.
- Source (scope as qualified below): https://www.electrical-installation.org/enwiki/IT_system_-_Fault_protection
- A/B/C physical model and negative-case reasoning: For grounded one-phase fault in symmetrical isolated-neutral three-phase system, healthy phases' phase-to-earth voltage becomes line voltage, sqrt(3) approx 1.73 times previous phase-earth -> C. A reduction and B no change false; temporary transients and system symmetry required.
- `approved_for_learning=NO`, `independent_QA=NOT_RUN`, `ANRE_2026_OFFICIAL_KEY=NOT_VERIFIED`.

### G1-ELE-035 | CONDITIONAL_SWITCHGEAR_FAULT_COMPARTMENTALIZATION
- Original: Compartimentarea unei celule electrice se utilizează
- A: în scopul evitării extinderii avariilor;
- B: numai  în scopul protejării personalului de exploatare;
- C: protecţiei la supratensiuni
- Imported key **A** untouched; source workbook `ELECTROTEHNICA-09.2024-2.xlsx` row `42`.
- Source (scope as qualified below): https://www.se.com/us/en/work/support/resources-and-tools/technical-faqs/
- A/B/C physical model and negative-case reasoning: A partitioned cubicle can limit fault propagation to other cells, B 'numai' personnel safety excludes fault isolation, C overvoltage protection requires surge protective devices not internal partitions. Manufacturer exact compartment tested classification needed; generic source not proof of universal limit.
- `approved_for_learning=NO`, `independent_QA=NOT_RUN`, `ANRE_2026_OFFICIAL_KEY=NOT_VERIFIED`.

### G1-ELE-038 | DIRECT_POSITIVE_SEQUENCE_ROTATING_FIELD
- Original: Componenta simetrică directă produce, în cazul unui motor electric:
- A: cuplul util
- B: cuplul de frânare
- C: oscilaţii ale rotorului
- Imported key **A** untouched; source workbook `ELECTROTEHNICA-09.2024-2.xlsx` row `45`.
- Source (scope as qualified below): https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electro-Optics/Introduction_to_Electric_Power_Systems_%28Kirtley%29/04%3A_Introduction_to_symmetrical_components/4.06%3A_Unbalanced_Faults
- A/B/C physical model and negative-case reasoning: A positive-sequence symmetric component has forward rotating magnetic field and produces useful forward torque in standard 3phase motor; B reverse/negative sequence produces braking heating, C rotor oscillations aren't defined positive sequence effect. Source linked teaches symmetrical components rather than direct motor torque test; independent didactic exact page needed.
- `approved_for_learning=NO`, `independent_QA=NOT_RUN`, `ANRE_2026_OFFICIAL_KEY=NOT_VERIFIED`.

### G1-ELE-039 | DIRECT_COULOMB_INVERSE_SQUARE
- Original: Conform Legii lui Coulomb, forţa de atracţie sau de repulsie care se exercită între sarcinile electrice este:
- A: direct proporţională cu pătratul distanţei
- B: invers proporţională cu pătratul distanţei
- C: direct proporţională cu distanţa
- Imported key **B** untouched; source workbook `ELECTROTEHNICA-09.2024-2.xlsx` row `46`.
- Source (scope as qualified below): https://openstax.org/books/university-physics-volume-2/pages/5-key-equations
- A/B/C physical model and negative-case reasoning: Coulomb |F| = k |q1q2| / r² for fixed charges and medium. B inverse square. A r² and C r proportional wrong; if charges/medium change with distance, premise no longer fixed.
- `approved_for_learning=NO`, `independent_QA=NOT_RUN`, `ANRE_2026_OFFICIAL_KEY=NOT_VERIFIED`.

### G1-ELE-040 | DIRECT_RC_TAU
- Original: Constanta de timp a unui circuit format dintr-un rezistor de rezistenţă R înseriat cu un condensator de capacitate C, este:
- A: RC
- B: R/C
- C: 1/(RC)
- Imported key **A** untouched; source workbook `ELECTROTEHNICA-09.2024-2.xlsx` row `47`.
- Source (scope as qualified below): https://openstax.org/books/university-physics-volume-2/pages/10-5-rc-circuits
- A/B/C physical model and negative-case reasoning: Time constant tau=R*C seconds, A. B R/C different dimensions, C 1/RC has dimension 1/second (pole rate), not time constant.
- `approved_for_learning=NO`, `independent_QA=NOT_RUN`, `ANRE_2026_OFFICIAL_KEY=NOT_VERIFIED`.

### G1-ELE-041 | CONDITIONAL_SWITCHGEAR_PARTITION_INTENDED
- Original: Delimitările prin pereţi între celulele unei staţii electrice de interior se utilizează în principal în scopul:
- A: asigurării unui acces mai comod la aparataj;
- B: limitării zgomotului în corpul de conexiuni;
- C: evitării extinderii avariilor.
- Imported key **C** untouched; source workbook `ELECTROTEHNICA-09.2024-2.xlsx` row `48`.
- Source (scope as qualified below): https://eepower.com/technical-articles/substation-componentspart-5-busbar-configurations/
- A/B/C physical model and negative-case reasoning: C dividing indoor switchgear bays helps contain fault escalation, A easy access not main engineering fault purpose, B noise reduction not main fault containment. The linked general busbar article does not prove exact wall constructions and fire arc class, so specific engineering source still needed.
- `approved_for_learning=NO`, `independent_QA=NOT_RUN`, `ANRE_2026_OFFICIAL_KEY=NOT_VERIFIED`.

### G1-ELE-042 | DIRECT_AC_SERIES_IMPEDANCE
- Original: Curentul care circula printr-un circuit de curent alternativ, având rezistenta r=3 Ω, reactanţa x= 4 Ω si la bornele căruia se aplica o tensiune de 220 V este:
- A: 31,5 A
- B: 44 A
- C: 53,4 A
- Imported key **B** untouched; source workbook `ELECTROTEHNICA-09.2024-2.xlsx` row `49`.
- Source (scope as qualified below): https://openstax.org/books/university-physics-volume-2/pages/15-2-simple-ac-circuits
- A/B/C physical model and negative-case reasoning: For a single series linear R=3ohm, X=4ohm, |Z|=sqrt(9+16)=5ohm; I=220/5=44 A B. A31.5 and C53.4 fail. Assumes same-frequency AC RMS voltage and linear series impedance.
- `approved_for_learning=NO`, `independent_QA=NOT_RUN`, `ANRE_2026_OFFICIAL_KEY=NOT_VERIFIED`.

### G1-ELE-044 | CONDITIONAL_INCANDESCENT_VOLTAGE_LIFE
- Original: Durata de viata a lămpilor cu incandescenta:
- A: creste odată cu creşterea frecventei
- B: scade odată cu scăderea tensiunii
- C: scade odată cu creşterea tensiunii
- Imported key **C** untouched; source workbook `ELECTROTEHNICA-09.2024-2.xlsx` row `51`.
- Source (scope as qualified below): https://www.energy.gov/energysaver/lighting-choices-save-you-money
- A/B/C physical model and negative-case reasoning: Higher applied voltage makes filament hotter, usually shortens incandescent lifetime C. B voltage decrease typically lengthens life, A frequency increase by itself not universal life increase. Generic lighting source lacks exact measured lifespan vs voltage; status conditional.
- `approved_for_learning=NO`, `independent_QA=NOT_RUN`, `ANRE_2026_OFFICIAL_KEY=NOT_VERIFIED`.

### G1-ELE-045 | DIRECT_CONVECTION_CURRENT_MOVING_CHARGED_BODY
- Original: Curentul electric generat prin deplasarea cu viteza v a unui corp încărcat cu o sarcină electrică se numeşte:
- A: curent electric de conducţie
- B: curent electric de convecţie
- C: curent electric de deplasare (Maxwell)
- Imported key **B** untouched; source workbook `ELECTROTEHNICA-09.2024-2.xlsx` row `52`.
- Source (scope as qualified below): https://openstax.org/books/university-physics-volume-2/pages/16-key-equations
- A/B/C physical model and negative-case reasoning: Moving charged bulk material produces convection current B; A conduction refers transport of charge carriers in conducting medium, C Maxwell displacement current epsilon*dPhi_E/dt associated varying electric flux, not same as movement of charged body. Exact textbook nomenclature should be checked for 'curent de convecție'.
- `approved_for_learning=NO`, `independent_QA=NOT_RUN`, `ANRE_2026_OFFICIAL_KEY=NOT_VERIFIED`.

### G1-ELE-046 | CONDITIONAL_NONLINEAR_SINE_CURRENT
- Original: Curentul produs într-un circuit care conţine elemente neliniare şi care este alimentat cu o tensiune sinusoidală este:
- A: întotdeauna nesinusoidal
- B: întotdeauna sinusoidal
- C: nesinusoidal sau sinusoidal, depinde de natura elementelor neliniare
- Imported key **C** untouched; source workbook `ELECTROTEHNICA-09.2024-2.xlsx` row `53`.
- Source (scope as qualified below): https://openstax.org/books/university-physics-volume-2/pages/9-5-electrical-energy-and-power
- A/B/C physical model and negative-case reasoning: Nonlinear components can distort sinusoidal supply current via harmonics (A too universal), but current may remain sinusoidal if nonlinear contribution negligible, piecewise region linear or other cancellation. B always sinusoidal also false. C depends on nonlinearity/model, but cited general power textbook does not directly establish complete nonlinear circuit counterexample. Keep conditional.
- `approved_for_learning=NO`, `independent_QA=NOT_RUN`, `ANRE_2026_OFFICIAL_KEY=NOT_VERIFIED`.

### G1-ELE-047 | CONDITIONAL_HARMONIC_INDUCTOR_SMOOTHING
- Original: Curentul rezultat prin aplicarea unei tensiuni nesinusoidale la bornele unei bobine este:
- A: mai puţin deformat decât tensiunea care i-a dat naştere
- B: mult mai deformat decât tensiunea care i-a dat naştere
- C: sinusoidal
- Imported key **A** untouched; source workbook `ELECTROTEHNICA-09.2024-2.xlsx` row `54`.
- Source (scope as qualified below): https://openstax.org/books/college-physics-ap-courses/pages/23-11-reactance-inductive-and-capacitive
- A/B/C physical model and negative-case reasoning: Linear ideal inductor I_n=V_n/(n*omega*L), so higher-harmonic current attenuated relative to fundamental, *in many waveforms* current less distorted -> A intended. B greater usually wrong under lowpass inductor, C cannot become exactly sinusoidal if voltage has harmonics. The word 'mai puțin deformat' lacks distortion metric and initial current transients; conditionally only.
- `approved_for_learning=NO`, `independent_QA=NOT_RUN`, `ANRE_2026_OFFICIAL_KEY=NOT_VERIFIED`.

### G1-ELE-048 | CONDITIONAL_CAPACITOR_HARMONIC_ACCENTUATION
- Original: Curentul rezultat prin aplicarea unei tensiuni nesinusoidale la bornele unui condensator este:
- A: mult mai deformat decât tensiunea care i-a dat naştere
- B: sinusoidal
- C: mai puţin deformat decât tensiune care i-a dat naştere
- Imported key **A** untouched; source workbook `ELECTROTEHNICA-09.2024-2.xlsx` row `55`.
- Source (scope as qualified below): https://openstax.org/books/college-physics-ap-courses/pages/23-11-reactance-inductive-and-capacitive
- A/B/C physical model and negative-case reasoning: Ideal capacitor I_n=n*omega*C*V_n, higher harmonics proportionally emphasized -> A intended. B sinusoidal not generally from nonsinusoidal input, C less distorted only under special waveform/metric; 'mult mai deformat' not guaranteed quantitative without harmonic spectrum.
- `approved_for_learning=NO`, `independent_QA=NOT_RUN`, `ANRE_2026_OFFICIAL_KEY=NOT_VERIFIED`.

### G1-ELE-049 | BLOCKED_PROXIMITY_EFFECT_SOURCE_MISMATCH
- Original: Dacă două conductoare parcurse de curenţi în acelaşi sens sunt aşezate paralel, unul lângă altul:
- A: densitatea de curent crește în părţile apropiate ale conductoarelor
- B: densitatea de curent creşte în părţile mai depărtate ale conductoarelor
- C: densitatea de curent este uniformă pe ambele părţi ale conductoarelor
- Imported key **B** untouched; source workbook `ELECTROTEHNICA-09.2024-2.xlsx` row `56`.
- Source (scope as qualified below): https://openstax.org/books/university-physics-volume-2/pages/12-3-magnetic-force-between-two-parallel-currents
- A/B/C physical model and negative-case reasoning: B original source intends *proximity effect* higher current density on farther sides with same-direction AC current, but OpenStax source only proves attractive magnetic FORCE, not current-density geometry. At DC uniform conductor homogeneous carrying stationary current, no general near/far skin/proximity contrast; frequency, materials and cross sections unspecified. Do NOT infer B from attraction or certify it without dedicated AC proximity-effect didactic source.
- `approved_for_learning=NO`, `independent_QA=NOT_RUN`, `ANRE_2026_OFFICIAL_KEY=NOT_VERIFIED`.

## Cross-case exact math and countertests
- ELE034: U_LL=sqrt(3)*U_phase; neutral shift and ungrounded healthy phases in ideal isolated-neutral earth fault (not all earthing systems).
- ELE039: F(r)=k*q1*q2/r^2, fixed charges.
- ELE040: tau=RC; dimensions ohm*farad=seconds.
- ELE042: Z=(3+j4)ohm => |Z|=5ohm, I=220/5=44A.
- ELE047: for 3rd voltage harmonic, inductor current harmonic fundamental-normalized attenuated by factor 3 compared with voltage spectrum (linear L); ELE048 capacitor third harmonic 3-fold relative amplification, no universal 'much more' claim.
- ELE049: magnetic attractive force is **not evidence** for current density redistribution and user-safe current-bearing circuit sizing. Requires direct same-object AC proximity-effect source.

## Gate
15 existing prior preliminary cards; imported keys unchanged. Direct formula tests + conditional sources. Source-mismatch ELE049 remains explicitly blocked; weaker manufacturer generic links have `SOURCE_PINPOINT_MISSING` rather than verified. No new learner approvals. Continue 42 residual preliminary records with exact matched sources, and crossgrade equality/no double-count.
