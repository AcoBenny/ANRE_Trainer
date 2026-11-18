# CKPT-230 | GFR 15 P2 Grade I electromagnetic and power-frequency model cards | 2026-11-18

Original V73 822 master Git blob `c027d417a8e4e605c830b2016fb55b099b8d130b`; 15 original previously only preliminary G1-ELE P2 cards, exact three original alternatives preserved. Sources include OpenStax, peer-reviewed corona paper and I7 primary, alongside explicitly **generic non-exact sources**. One assistant analysis, not genuine independent reviewer. No 2026 ANRE exam score-key verification, no learner approvals, no app/HTML/APK/main/merge work.

### G1-ELE-060 | CONDITIONAL_SKIN_EFFECT_INDUCTION_HEATING
- Question: Efectul pelicular al curentului alternativ este utilizat în:
- A: încălzirea materialelor prin inducţie
- B: eliminarea dezechilibrelor din reţeaua electrică
- C: eliminarea distorsiunilor undelor de curent
- Imported key **A** UNCHANGED, source workbook ELECTROTEHNICA-09.2024-2.xlsx:67.
- Evidence URL: https://www.energy.gov/energysaver/induction-cooking
- Technical and linguistic A/B/C reasoning and counterexample: Alternating magnetic fields induce surface eddy currents heating materials, with skin effect helping high-frequency power concentration in material: A intended. B power-grid balancing not skin effect; C waveform distortion elimination not its function. Source is household induction example, not specific industrial metal treatment; full exact-source QA still needed.
- Status not independently approved, `approved_for_learning=NO`, `official_ANRE_2026_key=NOT_VERIFIED`.

### G1-ELE-061 | CONDITIONAL_SKIN_EFFECT_CAUSAL_EXPLANATION
- Question: Efectul pelicular al unui curent alternativ care străbate un conductor masiv se datorează:
- A: unor curenţi paraziţi induşi în conductor, simetrici faţă de axa acestuia
- B: numai unor forţe electromotoare induse datorită variaţiei curentului
- C: capacităţii conductorului faţă de pământ
- Imported key **A** UNCHANGED, source workbook ELECTROTEHNICA-09.2024-2.xlsx:68.
- Evidence URL: https://openstax.org/books/university-physics-volume-2/pages/13-4-induced-electric-fields
- Technical and linguistic A/B/C reasoning and counterexample: Time-varying conduction current causes nonuniform self-induced electric fields / eddy-related currents that redistribute current density toward surface of massive conductor. A mentions symmetric eddies (ideal uniform cylindrical case) but not complete general constitutive explanation; B 'numai' changing-current induced emf may actually be alternative/partial mechanism; C earth capacitance unrelated. Ambiguous causal overlap A vs B not certified.
- Status not independently approved, `approved_for_learning=NO`, `official_ANRE_2026_key=NOT_VERIFIED`.

### G1-ELE-071 | DIRECT_VOLTMETER_SERIES_MULTIPLIER
- Question: Extinderea domeniului de măsurare la voltmetre se realizează cu:
- A: shunturi
- B: rezistente adiţionale
- C: condensatoare montate în paralel
- Imported key **B** UNCHANGED, source workbook ELECTROTEHNICA-09.2024-2.xlsx:78.
- Evidence URL: https://openstax.org/books/college-physics/pages/21-4-dc-voltmeters-and-ammeters
- Technical and linguistic A/B/C reasoning and counterexample: Adding series multiplier resistance to galvanometer extends DC voltmeter voltage range B. A parallel shunt chiefly extends ammeter, C parallel capacitor frequency-dependent not general voltmeter range extension. Different modern measuring instruments may use voltage dividers electronically.
- Status not independently approved, `approved_for_learning=NO`, `official_ANRE_2026_key=NOT_VERIFIED`.

### G1-ELE-072 | CONDITIONAL_RL_DECAY_CONSTANT_CONVENTION
- Question: Factorul de atenuare al unui circuit format dintr-un rezistor de rezistenţă R înseriat cu o bobină de inductanţă L, alimentate de o tensiune electromotoare constantă este egal cu:
- A: R/L
- B: L/R
- C: 1
- Imported key **A** UNCHANGED, source workbook ELECTROTEHNICA-09.2024-2.xlsx:79.
- Evidence URL: https://openstax.org/books/university-physics-volume-2/pages/14-4-rl-circuits
- Technical and linguistic A/B/C reasoning and counterexample: Series RL with DC step: homogeneous current transient e^(-R*t/L); *attenuation coefficient* alpha=R/L [1/s] A, whereas time constant tau=L/R [s] B. Without definition 'factor de atenuare', some traditions mean multiplicative e-factor or inverse time constant; explicit alpha required.
- Status not independently approved, `approved_for_learning=NO`, `official_ANRE_2026_key=NOT_VERIFIED`.

### G1-ELE-074 | DIRECT_BUNDLED_CORONA
- Question: Folosirea conductoarelor jumelate în construcţia LEA are ca scop principal:
- A: reducerea pierderilor Corona
- B: reducerea solicitărilor mecanice ale stâlpilor
- C: reducerea curenţilor de scurtcircuit
- Imported key **A** UNCHANGED, source workbook ELECTROTEHNICA-09.2024-2.xlsx:81.
- Evidence URL: https://www.mdpi.com/1996-1073/14/20/6612
- Technical and linguistic A/B/C reasoning and counterexample: Bundle/jumelate conductors increase effective radius and reduce surface electric-field stress/corona in HV/EHV LEA -> A. B reducing tower mechanical stress not principal (bundle may increase load); C short-circuit current limitation reactor/system protection, not bundle.
- Status not independently approved, `approved_for_learning=NO`, `official_ANRE_2026_key=NOT_VERIFIED`.

### G1-ELE-075 | DIRECT_SYNCHRONOUS_GENERATOR_FREQUENCY
- Question: Formula de calcul a frecventei produsa în sistemul electroenergetic de un generator cu n [rot/min] si p perechi de poli este:
- A: f =n p / 60
- B: f = 60 n / p
- C: f = 60 p / n
- Imported key **A** UNCHANGED, source workbook ELECTROTEHNICA-09.2024-2.xlsx:82.
- Evidence URL: https://openstax.org/books/university-physics-volume-2/pages/13-6-electric-generators-and-back-emf
- Technical and linguistic A/B/C reasoning and counterexample: p pairs poles produces p electrical cycles per mechanical revolution, n rotations/min -> f=np/60 Hz -> A. B 60n/p and C 60p/n dimensional/physical wrong. Source demonstrates mechanical rotation to AC emf but pole-pairs multiplier is standard synchronous machine relation not page exact.
- Status not independently approved, `approved_for_learning=NO`, `official_ANRE_2026_key=NOT_VERIFIED`.

### G1-ELE-076 | DIRECT_MOTIONAL_EMF_FARADAY
- Question: Formula e = B l v, unde e este tensiune electromotoare, B este inducţia magnetică, l este lungimea unui conductor, v este viteza de deplasare a acestuia, reprezintă o forma particulară a:
- A: teoremelor Biot-Savart
- B: legii inducţiei electromagnetice
- C: legii circuitului magnetic
- Imported key **B** UNCHANGED, source workbook ELECTROTEHNICA-09.2024-2.xlsx:83.
- Evidence URL: https://openstax.org/books/university-physics-volume-2/pages/13-key-equations
- Technical and linguistic A/B/C reasoning and counterexample: Special case motional emf e=B*l*v for perpendicular conductor motion / magnetic field is Faraday induction B. A Biot-Savart magnetic field of steady currents, C magnetic-circuit laws distinct.
- Status not independently approved, `approved_for_learning=NO`, `official_ANRE_2026_key=NOT_VERIFIED`.

### G1-ELE-078 | DIRECT_PARALLEL_CURRENT_ELECTRODYNAMIC_FORCE
- Question: Forţa care se exercită între două conductoare străbătute de curenţi electrici se numeşte:
- A: forţă electrocinetică
- B: forţă electrodinamică
- C: forţă magnetomotoare
- Imported key **B** UNCHANGED, source workbook ELECTROTEHNICA-09.2024-2.xlsx:85.
- Evidence URL: https://openstax.org/books/university-physics-volume-2/pages/12-3-magnetic-force-between-two-parallel-currents
- Technical and linguistic A/B/C reasoning and counterexample: B electrodynamic force between current-carrying conductors. A 'electrokinetic' nonstandard term here; C magnetomotive force NI is a magnetic circuit excitation, not mechanical force between conductors.
- Status not independently approved, `approved_for_learning=NO`, `official_ANRE_2026_key=NOT_VERIFIED`.

### G1-ELE-079 | CONDITIONAL_FARADAY_DERIVATIVE_VS_TOTAL_CHANGE
- Question: Tensiunea electromotoare indusă într-un circuit închis, prin variaţia fluxului magnetic, este:
- A: direct proporţională cu variaţia în timp a fluxului magnetic
- B: invers proporţională cu variaţia în timp a fluxului magnetic
- C: dependentă de modul în care este produs fluxul magnetic
- Imported key **A** UNCHANGED, source workbook ELECTROTEHNICA-09.2024-2.xlsx:86.
- Evidence URL: https://openstax.org/books/university-physics-volume-2/pages/13-1-faradays-law
- Technical and linguistic A/B/C reasoning and counterexample: A intended Faraday EMF magnitude proportional to time RATE of change of linked flux, |e|=N*|dPhi/dt|; B inverse variation false, C source method of flux change irrelevant to instantaneous flux linkage rate. Original says 'variația în timp', could refer derivative or ΔΦ rather than ΔΦ/Δt; annotate derivative distinction.
- Status not independently approved, `approved_for_learning=NO`, `official_ANRE_2026_key=NOT_VERIFIED`.

### G1-ELE-080 | DIRECT_PARALLEL_WIRE_FORCE_INVERSE_DISTANCE
- Question: Forţa electrodinamică exercitată între două conductoare filiforme, paralele, lungi, aflate la distanţa r, străbătute de câte un curent:
- A: este direct proporţională cu distanţa r dintre conductoare
- B: este invers proporţională cu distanţa r dintre conductoare
- C: nu depinde de distanţa r dintre conductoare
- Imported key **B** UNCHANGED, source workbook ELECTROTEHNICA-09.2024-2.xlsx:87.
- Evidence URL: https://openstax.org/books/university-physics-volume-2/pages/12-3-magnetic-force-between-two-parallel-currents
- Technical and linguistic A/B/C reasoning and counterexample: For long, parallel, thin wires F/length=mu0*I1*I2/(2pi*r), B inverse r at fixed currents and medium. A directly proportional and C independent false. Assumes lengths >> separation, DC/quasi-static, air/mu constant.
- Status not independently approved, `approved_for_learning=NO`, `official_ANRE_2026_key=NOT_VERIFIED`.

### G1-ELE-081 | DIRECT_ELECTRIC_FORCE_QE
- Question: Forţa F care se exercită asupra unei sarcini electrice q aflată într-un câmp electric de intensitate E are expresia:
- A: F=E/q
- B: F=qE
- C: F=q/E
- Imported key **B** UNCHANGED, source workbook ELECTROTEHNICA-09.2024-2.xlsx:88.
- Evidence URL: https://openstax.org/books/college-physics/pages/18-4-electric-field-concept-of-a-field-revisited
- Technical and linguistic A/B/C reasoning and counterexample: Electric force F(vector)=qE(vector) -> B. A E/q incorrect dimensions; C q/E incorrect. Negative q reverses force direction, vector relation still true.
- Status not independently approved, `approved_for_learning=NO`, `official_ANRE_2026_key=NOT_VERIFIED`.

### G1-ELE-082 | DIRECT_FREQUENCY_INVERSE_PERIOD
- Question: Frecvenţa unei mărimi periodice este inversul:
- A: amplitudinii
- B: perioadei
- C: fazei
- Imported key **B** UNCHANGED, source workbook ELECTROTEHNICA-09.2024-2.xlsx:89.
- Evidence URL: https://openstax.org/books/university-physics-volume-2/pages/13-6-electric-generators-and-back-emf
- Technical and linguistic A/B/C reasoning and counterexample: Frequency f=1/T => B period. A amplitude and C phase not time interval; for periodic nonsinusoidal signal fundamental f same inverse fundamental T.
- Status not independently approved, `approved_for_learning=NO`, `official_ANRE_2026_key=NOT_VERIFIED`.

### G1-ELE-083 | DIRECT_INDUCTION_METER_EDDY_CURRENTS
- Question: Funcţionarea contoarelor de inducţie are la baza:
- A: curenţii turbionari
- B: efectul termic al curentului electric
- C: forţa electrostatica
- Imported key **A** UNCHANGED, source workbook ELECTROTEHNICA-09.2024-2.xlsx:90.
- Evidence URL: https://www.electrical4u.com/induction-type-energy-meter/
- Technical and linguistic A/B/C reasoning and counterexample: Induction disc energy meter electromechanical torque involves induced eddy currents in aluminium disc interacting with alternating field -> A; B thermal heating not primary operation; C electrostatic force not driver. Exact meter class specified implicitly by term 'contor de inducţie'.
- Status not independently approved, `approved_for_learning=NO`, `official_ANRE_2026_key=NOT_VERIFIED`.

### G1-ELE-084 | DIRECT_PROTECTIVE_EARTHING_PERSONNEL
- Question: În instalaţiile de joasa tensiune, legarea la pământ este justificatã:
- A: din motive economice
- B: pentru diminuarea suprasolicitărilor echipamentelor electrice
- C: pentru securitatea muncii
- Imported key **C** UNCHANGED, source workbook ELECTROTEHNICA-09.2024-2.xlsx:91.
- Evidence URL: https://legislatie.just.ro/Public/DetaliiDocument/286763
- Technical and linguistic A/B/C reasoning and counterexample: I7 §5.5.1 and Chapter2 PE definition protects persons/animals against electric shock, so C safety at work; A economics not main objective, B equipment over-stress is not primary reason for protection earthing. Earthing function includes equipment/EMC contexts, but 'instalatii joasa tensiune' focus shock prevention.
- Status not independently approved, `approved_for_learning=NO`, `official_ANRE_2026_key=NOT_VERIFIED`.

### G1-ELE-085 | CONDITIONAL_TEMPORARY_OVERLOAD_TRANSFORMER
- Question: Funcţionarea în suprasarcinã a unui transformator reprezintă:
- A: un regim de avarie
- B: un regim temporar admisibil
- C: un regim inadmisibil
- Imported key **B** UNCHANGED, source workbook ELECTROTEHNICA-09.2024-2.xlsx:92.
- Evidence URL: https://www.se.com/us/en/work/support/resources-and-tools/technical-faqs/
- Technical and linguistic A/B/C reasoning and counterexample: Transformer overload temporarily admissible within manufacturer/IEC thermal loading cycle and temperature ageing limits B. A not automatically a failure, C not always prohibited; but sustained overload beyond limit is inadmissible and manufacturer FAQ cited only generic. Needs matched IEC60076-7 loading table, ambient/history.
- Status not independently approved, `approved_for_learning=NO`, `official_ANRE_2026_key=NOT_VERIFIED`.

## Explicit math test gates
- RL decay: i(t)~exp(-Rt/L), attenuation coefficient R/L [s^-1], characteristic time L/R [s].
- Generator n=1500 rpm, p=2 pairs: f=1500*2/60=50Hz; check n=3000,p=1 50Hz.
- Parallel long-wire F/l=mu0*I1*I2/(2πr), twice distance halves force.
- Lorentz electric force F=q E, negative sign reverses direction.
- Faraday emf requires flux derivative, not change alone.
- Existing overlap with G2 same QABC must be matched before downstream grade reuse, not double-counted. Documented conditional source gaps at ELE061/072/079/085. Do not produce practical switching or field steps.

## Next
- 15 existing cards newly source reviewed, 0 new questions, 0 changes of imported score keys, 0 user approvals. Continue leftover legacy (now 12) with precise source and historical evidence reuse. PR#7 Draft.
