# CKPT-237 | 10 original electrotechnical QABC plus 10 exact grade-II references | 2026-11-18

Baseline V115 Git blob 002c0541b549cf5ba4f304a7c1e697d19a0730b3. Original V73 canonical QABC and key read for each of 20 IDs. Ten Grade I source/interpretation checks plus exactly ten Grade II matching full QABC and imported key links; Grade-II links are evidence reuse ONLY, not independent source research.

## G1-ELE-133 / G2-ELEC-273
- Q: La generatorul sincron viteza de rotaţie a câmpului magnetic al statorului fata de viteza de rotaţie a rotorului maşinii este:
- A: mai mare
- B: mai mica
- C: egala
- Imported key (unchanged): C
- Scoped A/B/C reasoning: At a synchronized steady generator the stator rotating magnetic field and rotor have equal mechanical speed. A higher and B lower would entail sustained relative slip and contradict synchronous operation. Transient oscillations are excluded by the steady-operation reading.
- Research source: https://www.ece.lsu.edu/mendrela/EE3410Electricgenerators.pdf
- Preliminary flag: SYNC_GENERATOR_FIELD_ROTOR_MATCH. Not an authenticated ANRE-2026 exam key, not an independent expert review.

## G1-ELE-136 / G2-ELEC-276
- Q: La maşina sincrona turaţia variază în funcţie de sarcina astfel:
- A: creste când sarcina creste
- B: scade când sarcina scade
- C: rămâne constanta la variaţia sarcinii
- Imported key (unchanged): C
- Scoped A/B/C reasoning: Steady-state grid-connected synchronous-machine speed follows grid frequency and pole count, n=120f/P and does not normally vary with load; load changes torque angle. A and B confuse speed with torque/load adjustment. Frequency excursions or loss of synchronism are explicit exceptions.
- Research source: https://electrical-engineering-portal.com/res/res5/Synchrounous-Generators-and-Motors.pdf
- Preliminary flag: SYNCHRONOUS_SPEED_LOAD_QUALIFIED. Not an authenticated ANRE-2026 exam key, not an independent expert review.

## G1-ELE-141 / G2-ELEC-279
- Q: Legea lui Ohm pentru o porţiune de circuit este valabila:
- A: doar în curent continuu
- B: doar în curent alternativ
- C: indiferent de natura circuitului
- Imported key (unchanged): C
- Scoped A/B/C reasoning: Imported C intends AC or DC application of U=RI for an ohmic section. A only-DC and B only-AC are false. However 'indiferent de natura circuitului' is not universally true for diodes and other nonlinear nonohmic elements. Flag ambiguous rather than certify C universally.
- Research source: https://openstax.org/books/university-physics-volume-2/pages/9-4-ohms-law
- Preliminary flag: OHM_LAW_NONOHMIC_AMBIGUITY. Not an authenticated ANRE-2026 exam key, not an independent expert review.

## G1-ELE-144 / G2-ELEC-282
- Q: La o maşina electrica asincrona turaţia variază:
- A: cu curentul de excitaţie
- B: cu frecventa
- C: numai cu sarcina
- Imported key (unchanged): B
- Scoped A/B/C reasoning: Induction speed n=(120f/P)*(1-s); B frequency affects speed. A excitation current is not primary speed law. C 'only load' is false; speed varies with load-induced slip as well, so B is true but not complete or exclusive.
- Research source: https://www.ibiblio.org/kuphaldt/electricCircuits/AC/AC_13.html
- Preliminary flag: INDUCTION_MOTOR_FREQUENCY_AND_SLIP. Not an authenticated ANRE-2026 exam key, not an independent expert review.

## G1-ELE-145 / G2-ELEC-283
- Q: La pornirea motoarelor electrice asincrone se urmăreşte:
- A: reducerea vibraţiilor rotorului
- B: reducerea curentului electric absorbit de motor
- C: reducerea tensiunii la bornele de alimentare ale motorului
- Imported key (unchanged): B
- Scoped A/B/C reasoning: Induction-motor start current can greatly exceed rated; reduced-voltage starters and VFD address current B. A vibrations may be another objective and C reduced terminal voltage is one possible method rather than universal goal. Torque and acceleration must remain sufficient.
- Research source: https://library.e.abb.com/public/1fd380f8ca8b4934ae3fa609d764fd33/21043_ABB_Motor_Guide_REV_D.pdf
- Preliminary flag: INDUCTION_STARTING_CURRENT_OBJECTIVE. Not an authenticated ANRE-2026 exam key, not an independent expert review.

## G1-ELE-147 / G2-ELEC-285
- Q: Materialele feromagnetice au permeabilitatea relativa:
- A: mai mica decât 1
- B: puţin mai mare decât 1
- C: mult mai mare decât 1
- Imported key (unchanged): C
- Scoped A/B/C reasoning: Ordinary ferromagnets in unsaturated operating range have high relative permeability compared with unity; C represents textbook regime. A mu_r<1 describes diamagnetism; B near-unity is not typical low-field ferromagnetic response. Under saturation and frequency-dependent conditions mu_r is not universally much greater than one.
- Research source: https://www.sciencedirect.com/topics/engineering/material-loss
- Preliminary flag: FERROMAGNETIC_HIGH_MU_R_NOT_UNIVERSAL. Not an authenticated ANRE-2026 exam key, not an independent expert review.

## G1-ELE-148 / G2-ELEC-286
- Q: Ecuația constitutivă a bobinei ideale are forma:
- A: u = R i
- B: u= L di/dt
- C: du = i/C dt
- Imported key (unchanged): B
- Scoped A/B/C reasoning: For an ideal lumped linear inductor in passive sign convention u=L di/dt B. A is resistor constitutive law; C is a capacitor relation and its differential notation is incomplete. Different terminal polarity changes sign; avoid confusing induced EMF sign with terminal voltage.
- Research source: https://openstax.org/books/university-physics-volume-2/pages/15-2-simple-ac-circuits
- Preliminary flag: IDEAL_INDUCTOR_PASSIVE_SIGN. Not an authenticated ANRE-2026 exam key, not an independent expert review.

## G1-ELE-149 / G2-ELEC-287
- Q: Legea lui Coulomb exprimã:
- A: forţa de interacţiune dintre corpuri punctuale încărcate cu sarcini electrice
- B: fluxul electric printr-o suprafaţa sferica
- C: diferenţa de potenţial între doua puncte
- Imported key (unchanged): A
- Scoped A/B/C reasoning: Coulomb law states electrostatic interaction force between ideal point charges A with magnitude k|q1q2|/r^2. B describes electric flux/Gauss law and C potential difference not Coulomb's force law. Static-point-charge approximation matters.
- Research source: https://openstax.org/books/university-physics-volume-2/pages/5-3-coulombs-law
- Preliminary flag: COULOMB_POINT_CHARGES. Not an authenticated ANRE-2026 exam key, not an independent expert review.

## G1-ELE-153 / G2-ELEC-291
- Q: Mărimea caracteristică circuitelor magnetice şi care este analoagă cu rezistenţa circuitelor electrice se numeşte:
- A: impedanţă
- B: reluctanţă
- C: permeanţă
- Imported key (unchanged): B
- Scoped A/B/C reasoning: Magnetic reluctance is analogous to electric resistance B with flux versus current and magnetomotive force versus voltage. A impedance is an AC electrical quantity; C permeance is reciprocal of reluctance and corresponds to conductance.
- Research source: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electro-Optics/Electromagnetic_Field_Theory%3A_A_Problem_Solving_Approach_%28Zahn%29/06%3A_Electromagnetic_Induction/6.02%3A_Faraday%27s_Law_for_Moving_Media
- Preliminary flag: MAGNETIC_RELUCTANCE_ANALOGY. Not an authenticated ANRE-2026 exam key, not an independent expert review.

## G1-ELE-158 / G2-ELEC-296
- Q: Miezul magnetic al rotorului unei maşini electrice asincrone se realizează din tole pentru:
- A: reducerea curenţilor turbionari
- B: reducerea tensiunii electromotoare induse
- C: numai din motive constructive
- Imported key (unchanged): A
- Scoped A/B/C reasoning: Laminated iron rotor core helps impede circulating eddy currents and reduces their losses A. B reduction in intended induced EMF is not the objective; C only construction is disproved by electrodynamic loss mitigation. Steel grade and lamination thickness matter.
- Research source: https://coefs.charlotte.edu/mnoras/files/2013/03/Transformer-and-Inductor-Design-Handbook_Chapter_3.pdf
- Preliminary flag: ROTOR_LAMINATION_EDDY_LOSS. Not an authenticated ANRE-2026 exam key, not an independent expert review.

## QA and limitations
- 10/10 exact crossgrade question+A+B+C+key comparisons passed against V73 source.
- 20 ID-level evidence links, no canonical text/answer/key edits and no key change authorized.
- V115 P2 unfocused 319 -> V116 P2 unfocused 299.
- G1-ELE-141 expressly ambiguous if nonohmic circuits are admitted; no blanket learning approval.
- Educational/manufacturer external sources and same-assistant derivations are preliminary. NOT direct authentication of ANRE 2026 bibliographic editions or official exam keys; independent technical/linguistic source QA NOT_RUN.
- PR #7 should remain Draft with no merge and no HTML/APK/application edits.
