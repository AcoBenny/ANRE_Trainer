# CKPT-238 | 12 newly checked QABC / 23 previously unfocused grade rows | 2026-11-18

Baseline V116 blob 8eda72be398a78d2859bd8254ef8d7ec6524a22e; canonical V73 c027d417a8e4e605c830b2016fb55b099b8d130b. Exactly 12 original Grade I QABC checked with technical references and 12 exact Grade II full QABC/key matches confirmed. One Grade II counterpart G2-ELEC-316 had prior V82 evidence and was not overwritten or double counted. Grade II exact-match reference is NOT an independent source check.

## G1-ELE-154 / G2-ELEC-292
- Original: Mărimea periodică alternativă este o mărime a cărei valoare medie în decursul unei perioade este egală cu:
- A: 1
- B: 0
- C: 1,5
- Key unchanged: B
- A/B/C evidence and exceptions: The algebraic mean of an alternating AC quantity without a DC component over a period is zero; alternatives A and C are arbitrary numbers. A general sign-changing periodic wave with DC offset is a scope exception.
- Source: https://openstax.org/books/college-physics-2e/pages/20-5-alternating-current-versus-direct-current
- Risk qualifier: ALTERNATING_MEAN_ZERO; no independent grade-II source review and no exam-key approval.

## G1-ELE-157 / G2-ELEC-295
- Original: Metoda transfigurării reţelelor electrice este folosita pentru a:
- A: reduce pierderile de putere activa în reţea
- B: simplifica structura reţelelor echivalente pentru a reduce volumul de calcule
- C: diminua consumul specific de material conductor
- Key unchanged: B
- A/B/C evidence and exceptions: Mathematical network transformation simplifies equivalent circuit computation B; neither A physical loss reduction nor C metal material saving is entailed by an equivalent network transformation.
- Source: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/AC_Electrical_Circuit_Analysis%3A_A_Practical_Approach_%28Fiore%29/05%3A_Analysis_Theorems_and_Techniques/5.4%3A_Thevenin%27s_and_Norton%27s_Theorems
- Risk qualifier: EQUIVALENT_NETWORK_SIMPLIFICATION; no independent grade-II source review and no exam-key approval.

## G1-ELE-162 / G2-ELEC-300
- Original: O linie electrică foarte lungă se comportă ca o linie adaptată:
- A: dacă alimentează un receptor cu impedanţă egală cu impedanţa sa caracteristică
- B: dacă funcţionează  în scurtcircuit
- C: dacă funcţionează în gol
- Key unchanged: A
- A/B/C evidence and exceptions: A long line is matched when receiver impedance equals line characteristic impedance A; B short circuit and C open circuit are mismatches for finite Zc.
- Source: https://www.hsmuniversity.org/us/course/ele-380-power-systems-analysis/lesson-4-transmission-line-models
- Risk qualifier: MATCHED_LINE_ZC; no independent grade-II source review and no exam-key approval.

## G1-ELE-163 / G2-ELEC-301
- Original: O linie electrică lungă funcţionând în gol:
- A: produce putere reactivă
- B: absoarbe putere reactivă
- C: nu produce şi nu absoarbe putere reactivă
- Key unchanged: A
- A/B/C evidence and exceptions: At no load an ordinary high voltage AC line has charging capacitance and produces capacitive reactive power A; B and C neglect line capacitance or reverse the dominant regime. Sign convention and AC assumption apply.
- Source: https://www2.iea.lth.se/publications/MS-Theses/Full%20document/5330_full_document.pdf
- Risk qualifier: OPEN_LINE_CAPACITIVE_REACTIVE; no independent grade-II source review and no exam-key approval.

## G1-ELE-164 / G2-ELEC-302
- Original: O linie electrică lungă funcţionând în scurtcircuit:
- A: absoarbe putere reactivă
- B: produce putere reactivă
- C: nu produce şi nu absoarbe putere reactivă
- Key unchanged: A
- A/B/C evidence and exceptions: In standard non-resonant short-circuited AC line approximations inductive series impedance absorbs reactive power A; capacitive shunt and resonant long-line cases prevent universal extrapolation. B and C are not the intended standard circuit model.
- Source: https://www.hsmuniversity.org/us/course/ele-380-power-systems-analysis/lesson-4-transmission-line-models
- Risk qualifier: SHORT_LINE_INDUCTIVE_REACTIVE_CONDITIONAL; no independent grade-II source review and no exam-key approval.

## G1-ELE-170 / G2-ELEC-307
- Original: Între două noduri oarecare A şi B ale unei reţele electrice active, o sursă de tensiune de tensiune electromotoare E şi  fără impedanţă interioară, dar legată în serie cu o impedanţă Z, poate fi înlocuită cu o sursă de curent, de intensitate J şi fără admitanţă interioară, şuntată cu admitanţa Y, fără ca parametrii electrici la bornele A şi B  - tensiunea la borne şi curentul debitat prin aceste borne- să se schimbe,  dacă sunt îndeplinite condiţiile:
- A: Z Y = 1                                        J=YE
- B: J=YE                                         Z=Y
- C: Z Y = 1                                       Z=Y
- Key unchanged: A
- A/B/C evidence and exceptions: Voltage source E with series Z converts to current source J=E/Z with shunt Y=1/Z, so ZY=1 and J=YE A. B and C equate quantities with different dimensions.
- Source: https://www.sciencedirect.com/topics/engineering/norton-equivalent-circuit
- Risk qualifier: NORTON_Y_EQUALS_INVZ; no independent grade-II source review and no exam-key approval.

## G1-ELE-172 / G2-ELEC-309
- Original: Pentru materialele magnetice, relaţia dintre inducţia magnetică şi intensitatea câmpului magnetic:
- A: este liniară
- B: este o egalitate
- C: este neliniară
- Key unchanged: C
- A/B/C evidence and exceptions: Ferromagnetic B-H dependence exhibits saturation and hysteresis C; A only local approximation and B equality is dimensionally invalid.
- Source: https://link.springer.com/chapter/10.1007/978-981-95-8090-3_2
- Risk qualifier: FERROMAGNETIC_BH_NONLINEAR; no independent grade-II source review and no exam-key approval.

## G1-ELE-173 / G2-ELEC-310
- Original: Pierderea de putere activa într-un element de reţea (transformator, LEA, LEC) , la aceeaşi putere aparentã vehiculatã, este direct proportionalã cu:
- A: pătratul frecventei
- B: pătratul tensiunii reţelei
- C: pătratul curentului
- Key unchanged: C
- A/B/C evidence and exceptions: For fixed equivalent resistance copper/Joule load loss is proportional to current squared C; not directly frequency squared A or voltage squared B at fixed apparent power. Total transformer loss includes core no-load components and is NOT universally I squared.
- Source: https://openstax.org/books/university-physics-volume-2/pages/9-5-electrical-energy-and-power
- Risk qualifier: RESISTIVE_LOAD_LOSS_I_SQUARED; no independent grade-II source review and no exam-key approval.

## G1-ELE-180 / G2-ELEC-316
- Original: Pentru micşorarea pierderilor de putere prin curenţi turbionari în piesele metalice mari parcurse de fluxuri magnetice variabile:
- A: se limitează dimensiunile pieselor
- B: se execută piesele metalice din tole de oţel  cu adaus de siliciu pentru mărirea rezistivităţii, subţiri și izolate între ele
- C: se evită plasarea pieselor metalice masive în câmpuri magnetice variabile
- Key unchanged: B
- A/B/C evidence and exceptions: Thin mutually insulated silicon-steel laminations reduce eddy currents and losses B. A cutting piece size and C avoiding large metal parts are not the general construction solution; the older grade-II row already contains evidence so do not count it as new.
- Source: https://www.allaboutcircuits.com/technical-articles/eddy-current-loss-what-it-is-and-how-to-reduce-it-with-laminated-cores/
- Risk qualifier: LAMINATED_SILICON_STEEL; no independent grade-II source review and no exam-key approval.

## G1-ELE-181 / G2-ELEC-317
- Original: Pentru o linie electrică lungă care alimentează un receptor ce are impedanţa egală cu impedanţa caracteristică a liniei, puterea activă la extremitatea receptoare:
- A: se numeşte putere caracteristică sau putere naturală
- B: depinde de lungimea liniei
- C: este independentă de tensiunea liniei
- Key unchanged: A
- A/B/C evidence and exceptions: At load equal Zc the received power in ideal line is natural/characteristic power A; depends on voltage squared and Zc, so C is wrong. B may depend on lossy-line model but not definition of natural power.
- Source: https://www.hsmuniversity.org/us/course/ele-380-power-systems-analysis/lesson-4-transmission-line-models
- Risk qualifier: SURGE_IMPEDANCE_LOADING; no independent grade-II source review and no exam-key approval.

## G1-ELE-182 / G2-ELEC-318
- Original: Pentru o linie electrică care alimentează un receptor ce are impedanţa egală cu impedanţa caracteristică a liniei:
- A: energiile reactive, inductivă şi capacitivă, se compensează
- B: energia reactivă inductivă este mai mare decât cea capacitivă
- C: energia reactivă capacitivă este mai mare decât cea inductivă
- Key unchanged: A
- A/B/C evidence and exceptions: At surge impedance loading with lossless line its capacitive reactive production balances inductive absorption A; B and C incorrectly assert imbalance. Real line losses require qualification.
- Source: https://eepowerschool.com/tools/transmission-line-parameters/
- Risk qualifier: SIL_REACTIVE_BALANCE; no independent grade-II source review and no exam-key approval.

## G1-ELE-183 / G2-ELEC-319
- Original: Pentru o putere aparenta data puterea activa are valoarea maxima:
- A: când factorul de putere =1
- B: când factorul de putere = 0
- C: când U = U max
- Key unchanged: A
- A/B/C evidence and exceptions: At fixed S power P=S*PF is maximized at PF=1 A; B PF=0 gives zero active power and C alone is insufficient. Standard passive steady-state meaning.
- Source: https://openstax.org/books/university-physics-volume-2/pages/15-4-power-in-an-ac-circuit
- Risk qualifier: ACTIVE_POWER_FACTOR_UNITY; no independent grade-II source review and no exam-key approval.

## Data and release gate
- New source-scope notes 12; new ID-row links 23. 299 previously unfocused -> 276 remaining.
- 822 original IDs, original keys and question text unchanged; zero learning approvals.
- ELE-164 resonance/line assumptions and ELE-173 distinction between resistive Joule loss and total transformer loss remain explicit cautions. All 12 require independent source/edition and option review.
- No canonical text, keys, HTML, APK, merge or release edits. PR #7 Draft.
