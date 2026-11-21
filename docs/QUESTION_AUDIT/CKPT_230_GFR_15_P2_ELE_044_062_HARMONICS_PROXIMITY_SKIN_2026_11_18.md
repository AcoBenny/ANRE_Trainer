# CKPT-230 | GFR third 15 P2 legacy electrotechnics QABC, harmonic AC and protection | 2026-11-18

## Scope and exact-source requirement
- V73 822 grade IDs, Git blob `c027d417a8e4e605c830b2016fb55b099b8d130b`, Grade I 15 source rows `ELECTROTEHNICA-09.2024-2.xlsx`; each original QABC/key copied from registry. Selected skip prior G1-ELE-014 (CKPT-184), 051 (CKPT-189), 053 (G2-ELEC-199 CKPT-217), 057 (CKPT-184) to avoid repeat source work. No claim of official 2026 ANRE exam scoring keys and no human or separate independent specialists. Materials: peer-reviewed articles, OpenStax/LibreTexts, Schneider and IEEE technology pages.
- Negative scope gates: same-direction wire proximity requires AC, not unspecified DC; inductor vs capacitor harmonic response requires ideal linear reactances and Fourier fundamental; reactive power is net oscillatory exchange, not usable work.

### G1-ELE-044 | DIRECT_INCANDESCENT_VOLTAGE_LIFESPAN
- Original: **Durata de viata a lămpilor cu incandescenta:**
- A: creste odată cu creşterea frecventei
- B: scade odată cu scăderea tensiunii
- C: scade odată cu creşterea tensiunii
- Imported key **C** untouched; workbook row `ELECTROTEHNICA-09.2024-2.xlsx`:`51`. Exact Grade II counterpart: `G2-ELEC-190`, key `C`.
- A/B/C factual, counterexample and wording: Incandescent filament temperature and evaporation rise with increased supply voltage, life decreases (C). A mains frequency increase not the determining relation; B reduced voltage generally increases life, not decreases it. Source uses ~voltage to -12..-16 exponent for specified lamp families, not universal constants for LEDs.
- Relevant technical source: https://www.mdpi.com/1996-1073/17/22/5590
- Verdict: `DIRECT_INCANDESCENT_VOLTAGE_LIFESPAN`, official current exam key NOT_VERIFIED, independent review NOT_RUN, learner approval NO.

### G1-ELE-045 | DIRECT_CONVECTION_CURRENT_OBJECT
- Original: **Curentul electric generat prin deplasarea cu viteza v a unui corp încărcat cu o sarcină electrică se numeşte:**
- A: curent electric de conducţie
- B: curent electric de convecţie
- C: curent electric de deplasare (Maxwell)
- Imported key **B** untouched; workbook row `ELECTROTEHNICA-09.2024-2.xlsx`:`52`. Exact Grade II counterpart: `G2-ELEC-191`, key `B`.
- A/B/C factual, counterexample and wording: Movement of physically charged macroscopic body at velocity v transports charge and is convection current B. A conduction refers drift due to electric field in conducting material; C Maxwell displacement current ∂D/∂t is not charge-body transport, even though both participate in Ampère-Maxwell equation. Wording 'corp încărcat' material transport matters.
- Relevant technical source: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electro-Optics/Book%3A_Electromagnetics_I_%28Ellingson%29/06%3A_Steady_Current_and_Conductivity/6.01%3A_Convection_and_Conduction_Currents
- Verdict: `DIRECT_CONVECTION_CURRENT_OBJECT`, official current exam key NOT_VERIFIED, independent review NOT_RUN, learner approval NO.

### G1-ELE-046 | CONDITIONAL_NONLINEAR_ELEMENT_MODE
- Original: **Curentul produs într-un circuit care conţine elemente neliniare şi care este alimentat cu o tensiune sinusoidală este:**
- A: întotdeauna nesinusoidal
- B: întotdeauna sinusoidal
- C: nesinusoidal sau sinusoidal, depinde de natura elementelor neliniare
- Imported key **C** untouched; workbook row `ELECTROTEHNICA-09.2024-2.xlsx`:`53`. Exact Grade II counterpart: `G2-ELEC-192`, key `C`.
- A/B/C factual, counterexample and wording: A 'întotdeauna nesinusoidal' false: nonlinear element can operate in a small locally linear regime, or the nonlinear component may be inactive. B 'întotdeauna sinusoidal' false: rectifiers and magnetic saturation produce harmonics. C either sine/non-sine depending actual nonlinear law and operating region. Real source confirms typical nonlinear loads distort but does not by itself prove all allowed cancellation/pathological cases.
- Relevant technical source: https://www.allaboutcircuits.com/industry-articles/harmonic-current-in-power-supplies-and-iec-61000-3-2/
- Verdict: `CONDITIONAL_NONLINEAR_ELEMENT_MODE`, official current exam key NOT_VERIFIED, independent review NOT_RUN, learner approval NO.

### G1-ELE-047 | DIRECT_PURE_INDUCTOR_HARMONIC_FILTER
- Original: **Curentul rezultat prin aplicarea unei tensiuni nesinusoidale la bornele unei bobine este:**
- A: mai puţin deformat decât tensiunea care i-a dat naştere
- B: mult mai deformat decât tensiunea care i-a dat naştere
- C: sinusoidal
- Imported key **A** untouched; workbook row `ELECTROTEHNICA-09.2024-2.xlsx`:`54`. Exact Grade II counterpart: `G2-ELEC-193`, key `A`.
- A/B/C factual, counterexample and wording: For an ideal L, each nth voltage harmonic U_n leads to I_n=U_n/(nωL); high-frequency harmonics suppressed versus fundamental, so A current usually less distorted than applied voltage. B more distorted describes an ideal C under same assumptions; C purely sinusoidal unsupported when applied waveform has nonzero harmonics. Assumes ideal linear L and steady periodic source with fundamental.
- Relevant technical source: https://openstax.org/books/college-physics-2e/pages/23-11-reactance-inductive-and-capacitive
- Verdict: `DIRECT_PURE_INDUCTOR_HARMONIC_FILTER`, official current exam key NOT_VERIFIED, independent review NOT_RUN, learner approval NO.

### G1-ELE-048 | DIRECT_PURE_CAPACITOR_HARMONIC_WEIGHT
- Original: **Curentul rezultat prin aplicarea unei tensiuni nesinusoidale la bornele unui condensator este:**
- A: mult mai deformat decât tensiunea care i-a dat naştere
- B: sinusoidal
- C: mai puţin deformat decât tensiune care i-a dat naştere
- Imported key **A** untouched; workbook row `ELECTROTEHNICA-09.2024-2.xlsx`:`55`. Exact Grade II counterpart: `G2-ELEC-194`, key `A`.
- A/B/C factual, counterexample and wording: For ideal C, i=C dv/dt, nth harmonic amplitude I_n=nω C U_n, hence higher n harmonics enhanced relative to fundamental, intended A. B purely sinusoidal cannot hold generally for non-sinusoidal v, C less distorted matches ideal inductor not capacitor. Assumes ideal capacitance and comparable harmonic spectrum; nonlinear dielectric/ESR modify.
- Relevant technical source: https://openstax.org/books/college-physics-2e/pages/23-11-reactance-inductive-and-capacitive
- Verdict: `DIRECT_PURE_CAPACITOR_HARMONIC_WEIGHT`, official current exam key NOT_VERIFIED, independent review NOT_RUN, learner approval NO.

### G1-ELE-049 | CONDITIONAL_AC_PROXIMITY_MISSING
- Original: **Dacă două conductoare parcurse de curenţi în acelaşi sens sunt aşezate paralel, unul lângă altul:**
- A: densitatea de curent crește în părţile apropiate ale conductoarelor
- B: densitatea de curent creşte în părţile mai depărtate ale conductoarelor
- C: densitatea de curent este uniformă pe ambele părţi ale conductoarelor
- Imported key **B** untouched; workbook row `ELECTROTEHNICA-09.2024-2.xlsx`:`56`. Exact Grade II counterpart: `G2-ELEC-195`, key `B`.
- A/B/C factual, counterexample and wording: For two nearby parallel conductors with **AC currents of same direction**, proximity effect shifts current density toward the outer, farther edges, B. A near sides typical of opposite directions. C uniform can be approximately true for ideal steady DC with homogeneous geometry, so **original stem does not specify AC/frequency** and B cannot be certified universally. Manufacturer/primary paper supports AC regime only.
- Relevant technical source: https://www.mdpi.com/1996-1073/16/17/6341
- Verdict: `CONDITIONAL_AC_PROXIMITY_MISSING`, official current exam key NOT_VERIFIED, independent review NOT_RUN, learner approval NO.

### G1-ELE-050 | DIRECT_POYNTING_VECTOR_ORIENTATION
- Original: **Energia transmisă de undele electromagnetice cu intensitatea câmpului electric E şi intensitatea câmpului magnetic H se propagă după un vector:**
- A: S=E+H
- B: S=HxE
- C: S=ExH
- Imported key **C** untouched; workbook row `ELECTROTEHNICA-09.2024-2.xlsx`:`57`. Exact Grade II counterpart: `G2-ELEC-196`, key `C`.
- A/B/C factual, counterexample and wording: Electromagnetic energy flux vector is S=E×H in SI (W/m²), direction propagation for plane wave, C. B H×E reverses vector sign, A adds incompatible E and H vectors with different units.
- Relevant technical source: https://openstax.org/books/university-physics-volume-2/pages/16-3-energy-carried-by-electromagnetic-waves
- Verdict: `DIRECT_POYNTING_VECTOR_ORIENTATION`, official current exam key NOT_VERIFIED, independent review NOT_RUN, learner approval NO.

### G1-ELE-052 | DIRECT_CAPACITOR_PHASE_90
- Original: **Dacă printr-un condensator circulă un curent alternativ sinusoidal, la bornele sale se produce o cădere de tensiune:**
- A: defazată cu 90 de grade în urma curentului
- B: defazată cu 90 de grade înaintea curentului
- C: în fază cu curentul
- Imported key **A** untouched; workbook row `ELECTROTEHNICA-09.2024-2.xlsx`:`59`. Exact Grade II counterpart: `G2-ELEC-198`, key `A`.
- A/B/C factual, counterexample and wording: In ideal capacitor under sinusoidal AC, current leads voltage by 90° hence voltage lags current 90°, A. B reverse direction, C in-phase for resistor. ESR/leakage not ideal 90°, but prompt assumes condensator pure model.
- Relevant technical source: https://openstax.org/books/university-physics-volume-2/pages/15-2-simple-ac-circuits
- Verdict: `DIRECT_CAPACITOR_PHASE_90`, official current exam key NOT_VERIFIED, independent review NOT_RUN, learner approval NO.

### G1-ELE-054 | DIRECT_ZNO_OVERVOLTAGE
- Original: **Descărcătoarele cu oxid de zinc protejează echipamentele din reţele împotriva:**
- A: supratensiunilor
- B: supracurenţilor
- C: solicitărilor mecanice
- Imported key **A** untouched; workbook row `ELECTROTEHNICA-09.2024-2.xlsx`:`61`. Exact Grade II counterpart: `G2-ELEC-200`, key `A`.
- A/B/C factual, counterexample and wording: ZnO surge arrester clamps transient overvoltage (A); B overcurrent protective fuse/CB different; C mechanical loads outside arrester function. Long-duration overvoltage can overheat arrester, no blanket guarantee.
- Relevant technical source: https://productinfo.se.com/0100db2301_elecdistfunddesignguide/0100db2301-electrical-distribution-fundamentals-design-guide/English/0100DB2301%20Electrical%20Distribution%20Fundamentals%20Design%20Guide%20%28bookmap%29_DD00648155.xml/%24/SystemProtection-A4A695C5
- Verdict: `DIRECT_ZNO_OVERVOLTAGE`, official current exam key NOT_VERIFIED, independent review NOT_RUN, learner approval NO.

### G1-ELE-055 | DIRECT_ZNO_OVERVOLTAGE
- Original: **Descărcătoarele cu oxizi de zinc sunt echipamente destinate:**
- A: protecţiei personalului de exploatare împotriva electrocutării
- B: protecţiei împotriva supratensiunilor
- C: protecţiei împotriva supracurenţilor
- Imported key **B** untouched; workbook row `ELECTROTEHNICA-09.2024-2.xlsx`:`62`. Exact Grade II counterpart: `G2-ELEC-201`, key `B`.
- A/B/C factual, counterexample and wording: Same protected object as 054 but A/B/C permuted: B overvoltage is ZnO arrester purpose; A no universal shock protection by itself and C excessive current requires other protective device. Manufacturer identifies ZnO MOV as surge clamping element.
- Relevant technical source: https://www.se.com/us/en/faqs/FA301291/
- Verdict: `DIRECT_ZNO_OVERVOLTAGE`, official current exam key NOT_VERIFIED, independent review NOT_RUN, learner approval NO.

### G1-ELE-056 | DIRECT_SERIES_CAPACITOR_KVL
- Original: **Diferenţa de potenţial la bornele a n baterii de condensatoare montate în serie este egală cu:**
- A: suma diferenţelor de potenţial la bornele fiecărui condensator
- B: diferenţa de potenţial la bornele fiecărui condensator în parte
- C: diferenţa de potenţial a unui condensator împărţită la n
- Imported key **A** untouched; workbook row `ELECTROTEHNICA-09.2024-2.xlsx`:`63`. Exact Grade II counterpart: `G2-ELEC-202`, key `A`.
- A/B/C factual, counterexample and wording: Total terminal voltage across n series capacitors is the algebraic sum of individual capacitor voltages, A, by Kirchhoff voltage law. B one element voltage only if n=1 or other voltages zero; C V_element/n false for equal nonzero elements, true total is n·V_element for equal identical elements.
- Relevant technical source: https://openstax.org/books/university-physics-volume-2/pages/8-2-capacitors-in-series-and-in-parallel
- Verdict: `DIRECT_SERIES_CAPACITOR_KVL`, official current exam key NOT_VERIFIED, independent review NOT_RUN, learner approval NO.

### G1-ELE-059 | DIRECT_THREE_PHASE_WYE_BALANCED
- Original: **În cazul conexiunii în stea la transformator:**
- A: tensiunea de linie este egala cu tensiunea de faza
- B: curentul de linie este egal cu ~1,73 x curentul de faza
- C: tensiunea de linie este egala cu ~1,73 x tensiunea de faza
- Imported key **C** untouched; workbook row `ELECTROTEHNICA-09.2024-2.xlsx`:`66`. Exact Grade II counterpart: `G2-ELEC-204`, key `C`.
- A/B/C factual, counterexample and wording: In balanced Y/star system line voltage magnitude sqrt(3) times phase (line-neutral) voltage, C. A equality is delta voltage relation, B sqrt3 line current to phase current is delta, not Y. If unbalanced, individual line voltages not a single sqrt3 of arbitrary phase magnitude; standard balanced regime implied.
- Relevant technical source: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electro-Optics/Introduction_to_Electric_Power_Systems_%28Kirtley%29/03%3A_Polyphase_Networks/3.03%3A_Line-Line_Voltages
- Verdict: `DIRECT_THREE_PHASE_WYE_BALANCED`, official current exam key NOT_VERIFIED, independent review NOT_RUN, learner approval NO.

### G1-ELE-060 | DIRECT_INDUCTION_HEATING_SKIN
- Original: **Efectul pelicular al curentului alternativ este utilizat în:**
- A: încălzirea materialelor prin inducţie
- B: eliminarea dezechilibrelor din reţeaua electrică
- C: eliminarea distorsiunilor undelor de curent
- Imported key **A** untouched; workbook row `ELECTROTEHNICA-09.2024-2.xlsx`:`67`. Exact Grade II counterpart: `G2-ELEC-205`, key `A`.
- A/B/C factual, counterexample and wording: Skin effect concentrates AC/induced eddy current near surface, supporting localized induction heating A. B grid imbalance removal and C harmonic distortion elimination unrelated. Skin depth depends on frequency, permeability and conductivity; effect alone isn't the induction heating power supply.
- Relevant technical source: https://technav.ieee.org/topic/skin-effect/
- Verdict: `DIRECT_INDUCTION_HEATING_SKIN`, official current exam key NOT_VERIFIED, independent review NOT_RUN, learner approval NO.

### G1-ELE-061 | CONDITIONAL_SKIN_INDUCED_EDDIES
- Original: **Efectul pelicular al unui curent alternativ care străbate un conductor masiv se datorează:**
- A: unor curenţi paraziţi induşi în conductor, simetrici faţă de axa acestuia
- B: numai unor forţe electromotoare induse datorită variaţiei curentului
- C: capacităţii conductorului faţă de pământ
- Imported key **A** untouched; workbook row `ELECTROTEHNICA-09.2024-2.xlsx`:`68`. Exact Grade II counterpart: `G2-ELEC-206`, key `A`.
- A/B/C factual, counterexample and wording: Skin effect occurs from time-varying magnetic fields and induced counter EMF/eddy current redistribution; for axially symmetric solid conductor current distribution changes with radius, matches intended A. B 'numai FEM induse' refers to cause but omits induced current effects and is not cleanly false; C capacitance to ground unrelated. Original 'simetrici faţă de axa' assumes homogeneous cylindrical geometry, not arbitrary massive conductor cross section.
- Relevant technical source: https://technav.ieee.org/topic/skin-effect/
- Verdict: `CONDITIONAL_SKIN_INDUCED_EDDIES`, official current exam key NOT_VERIFIED, independent review NOT_RUN, learner approval NO.

### G1-ELE-062 | DIRECT_REACTIVE_EXCHANGE_WITH_WORDING_QUALIFICATION
- Original: **Energia electrica reactiva:**
- A: este o energie electrica complementara, care serveşte la magnetizarea bobinajelor
- B: se poate transforma în energie mecanica
- C: se poate transforma în energie luminoasa
- Imported key **A** untouched; workbook row `ELECTROTEHNICA-09.2024-2.xlsx`:`69`. Exact Grade II counterpart: `G2-ELEC-207`, key `A`.
- A/B/C factual, counterexample and wording: Reactive power/current required to magnetize inductive windings and establish fields; A matches common textbook description. B/C mechanical and light output represent net active power conversions, not oscillatory reactive exchange. But 'energie electrică reactivă' is metered exchange term not separately consumable work, and capacitive elements exchange electric field energy too, so A describes common role, not full definition.
- Relevant technical source: https://technav.ieee.org/topic/reactive-power/
- Verdict: `DIRECT_REACTIVE_EXCHANGE_WITH_WORDING_QUALIFICATION`, official current exam key NOT_VERIFIED, independent review NOT_RUN, learner approval NO.

## Results and continuation
- 15 G1 original grade-ID source passes, 15 distinct QABC units, 30 grade occurrences, but not 30 distinct analyses. Direct matches and explicitly conditional regimes kept disjoint. **Major new trap** G1-ELE-049 omits AC: in ideal steady DC no proximity redistribution, so C is not universally false and imported B is only AC-regime intended. ELE-061 B can be semantically adjacent/partial cause; ELE-046 depends on nonlinearity operation; ELE-047 and 048 are frequency-dependent ratios.
- No canonical answer changes, no app, no HTML/APK or release, PR#7 Draft. Next P2 legacy source work and exact-text grade-pair reconciliation; no inferred numeric mapping.
