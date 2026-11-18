# CKPT-216 | GFR 15 new P1 electrotechnics unique QABC source/negative check | 2026-11-18

## Scope
- 15 selected previously unfocused P1 ID cards copied exactly from V73 822 master, Git blob c027d417a8e4e605c830b2016fb55b099b8d130b; 10 Grade I + 5 Grade II, original keys unchanged. Other grade-specific exact duplicated QABC placements linked by equality, not counted as new unique units. Primary sources are manufacturer manuals, textbooks, open scholarly articles, and cited indexed technical source where marked; not authenticated ANRE examination answer keys.
- Evidence reopened in this session 2026-11-18 via publicly retrieved technical publications; exact technical object vs model; for safety-related HV questions no operational switching instructions derived. No source author claimed as a separately running independent QA reviewer.

### G1-ELE-020 | CONDITIONAL_ABSOLUTE_PHASE_FAULT
- **Original:** Capsularea monopolară conduce la :
- **A:** eliminarea totală a posibilităţii apariţiei unui scurtcircuit între faze;
- **B:** micşorarea riscului unor pierderi de gaz izolant;
- **C:** reducerea cheltuielilor de realizare a instalaţiilor.
- **Original key:** A, unchanged. Source: ELECTROTEHNICA-09.2024-2.xlsx row 27.
- **Other grade members with exact same QABC:** G1-ELE-020=A, G2-ELEC-172=A.
- **Technical/scope A-B-C evaluation:** Independent metal enclosures for each phase can preclude an interphase flashover *within that segregated enclosed volume*, unlike tripolar common enclosure. A says total elimination of possibility anywhere, overbroad given terminations/external interconnections. B gas losses not necessarily lower solely because of monopolar construction; C cost generally not demonstrably lower.
- **Source and access:** IEC 62271-203 GIS phase-enclosure type definition; https://www.iteh.eu/catalog/standards/clc/ccb96c43-abf5-44c0-9d92-e98de80c9187/en-62271-203-2004?reviews=true.
- **Gate:** CONDITIONAL_ABSOLUTE_PHASE_FAULT, independent review NOT_RUN, exam key NOT_VERIFIED, learner approval NO.

### G1-ELE-089 | DIRECT_FUNCTIONAL_MATCH_WITH_SPECIFIC_ASSEMBLY
- **Original:** Împărţirea fiecărei faze a unei instalaţii capsulate într-un anumit număr de compartimente atrage după sine:
- **A:** numai limitarea posibilităţilor de producere a unui defect în instalaţie;
- **B:** localizarea unor eventuale scăpări de gaz, precum şi a unor defecte interne,
- **C:** mărirea cantităţilor de gaz ce trebuie manipulate în cazul intervenţiei la un compartiment
- **Original key:** B, unchanged. Source: ELECTROTEHNICA-09.2024-2.xlsx row 96.
- **Other grade members with exact same QABC:** G1-ELE-089=B.
- **Technical/scope A-B-C evaluation:** A 'numai' excludes the additional practical containment/leak-location benefit; B separate gas compartments allow locating leakage/internal failure; C increasing gas to handle on a compartment intervention does not follow segmentation, typically reduces isolated gas volume. Actual design and pressure barriers required.
- **Source and access:** IEC 62271-203 GIS gas compartment/partitions and handling-loss scope; https://www.iteh.eu/catalog/standards/clc/ccb96c43-abf5-44c0-9d92-e98de80c9187/en-62271-203-2004?reviews=true.
- **Gate:** DIRECT_FUNCTIONAL_MATCH_WITH_SPECIFIC_ASSEMBLY, independent review NOT_RUN, exam key NOT_VERIFIED, learner approval NO.

### G1-ELE-090 | CONDITIONAL_IDEAL_RESONANCE_MODEL
- **Original:** În cazul apariţiei fenomenului de rezonanţă într-un circuit de curent alternativ, alimentat de la o sursă, aceasta furnizează circuitului:
- **A:** numai energie activă
- **B:** energie activă şi reactivă
- **C:** numai energie reactivă
- **Original key:** A, unchanged. Source: ELECTROTEHNICA-09.2024-2.xlsx row 97.
- **Other grade members with exact same QABC:** G1-ELE-090=A, G2-ELEC-234=A.
- **Technical/scope A-B-C evaluation:** For steady sinusoidal RLC at resonance XL=XC, net input Q=0 and generator supplies real/active P; B wrongly requires net reactive power, C excludes real dissipative power. However 'numai' is not a universal statement about every nonlinear/resonant topology or transients; requires specified model.
- **Source and access:** OpenStax University Physics Vol2 §15.5 Resonance; https://openstax.org/books/university-physics-volume-2/pages/15-5-resonance-in-an-ac-circuit.
- **Gate:** CONDITIONAL_IDEAL_RESONANCE_MODEL, independent review NOT_RUN, exam key NOT_VERIFIED, learner approval NO.

### G1-ELE-091 | DIRECT_INSTANTANEOUS_KIRCHHOFF
- **Original:** În cazul circuitelor de curent alternativ, teoremele lui Kirchhoff sunt întotdeauna satisfăcute pentru:
- **A:** valorile instantanee ale tensiunilor şi curenţilor
- **B:** valorile efective ale tensiunilor şi curenţilor
- **C:** modulele fazorilor asociaţi tensiunilor şi curenţilor
- **Original key:** A, unchanged. Source: ELECTROTEHNICA-09.2024-2.xlsx row 98.
- **Other grade members with exact same QABC:** G1-ELE-091=A, G2-ELEC-235=A.
- **Technical/scope A-B-C evaluation:** A signed instantaneous currents KCL and signed instantaneous voltages KVL hold for ordinary lumped circuits; B effective/RMS values omit relative phase, cannot be summed algebraically in general; C absolute values of phasors omit direction/phase. Phasor complex sums (not magnitude sums) also satisfy steady-state linear circuit laws, but not offered.
- **Source and access:** IEC 60375 Kirchhoff circuit reference directions; standard lumped-circuit principle; https://www.iteh.eu/catalog/standards/clc/8f705dcb-b17b-49a6-9d24-627a618d4f77/en-iec-60375-2018.
- **Gate:** DIRECT_INSTANTANEOUS_KIRCHHOFF, independent review NOT_RUN, exam key NOT_VERIFIED, learner approval NO.

### G1-ELE-094 | DIRECT_MOTOR_PROTECTION_ROLE
- **Original:** În cazul în care echiparea circuitelor electrice de alimentare a motoarelor electrice se face cu siguranţă fuzibilă şi contactor cu relee termice:
- **A:** releele termice realizează protecţia la suprasarcină;
- **B:** releele termice realizează protecţia la scurtcircuit;
- **C:** releele termice realizează protecţia la supratensiuni;
- **Original key:** A, unchanged. Source: ELECTROTEHNICA-09.2024-2.xlsx row 101.
- **Other grade members with exact same QABC:** G1-ELE-094=A.
- **Technical/scope A-B-C evaluation:** A thermal overload relay protects motor against sustained overcurrent/overload; B short circuit clearing requires fuse or proper breaker (relay alone not short-circuit protection); C overvoltage unrelated to thermal overload relay.
- **Source and access:** Schneider Electric thermal overload relays catalog and product; https://productinfo.se.com/9065ct9701_catalog/9065ct9701-overload-relays-and-thermal-units-catalog/English/9065CT9701%20Overload%20Relays%20and%20Thermal%20Units_0000354340.xml/%24/ThermalOverloadRelay-2A726FD8.
- **Gate:** DIRECT_MOTOR_PROTECTION_ROLE, independent review NOT_RUN, exam key NOT_VERIFIED, learner approval NO.

### G1-ELE-152 | DIRECT_PROPAGATION_CONSTANT_NAME
- **Original:** Mărimea caracteristică care reprezintă variaţia pe care o suferă amplitudinea şi faza undei de tensiune sau curent când parcurge 1 km de linie (lungă ) se numeşte:
- **A:** constanta de propagare a liniei
- **B:** constanta de atenuare a liniei
- **C:** constanta de distorsiune a liniei
- **Original key:** A, unchanged. Source: ELECTROTEHNICA-09.2024-2.xlsx row 159.
- **Other grade members with exact same QABC:** G1-ELE-152=A.
- **Technical/scope A-B-C evaluation:** Complex gamma=alpha+j beta contains both attenuation of amplitude and phase change per unit length, so A names it; B alpha describes only amplitude, not phase; C 'distortion constant' is not the complex gamma. Gamma has dimension inverse length (e.g. 1/km), gamma*1 km is dimensionless; original question does not claim gamma itself dimensionless.
- **Source and access:** Engineering LibreTexts Transmission Line Theory gamma units; https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Microwave_and_RF_Design_II_-_Transmission_Lines_%28Steer%29/02%3A_Transmission_Lines/2.02%3A_Transmission_Line_Theory.
- **Gate:** DIRECT_PROPAGATION_CONSTANT_NAME, independent review NOT_RUN, exam key NOT_VERIFIED, learner approval NO.

### G1-ELE-165 | DIRECT_SELECTIVITY_SCOPE
- **Original:** O protecţie este selectivă atunci când:
- **A:** deconectează numai consumatorul defect
- **B:** deconectează toţi consumatorii
- **C:** deconectează o jumătate dintre consumatori
- **Original key:** A, unchanged. Source: ELECTROTEHNICA-09.2024-2.xlsx row 172.
- **Other grade members with exact same QABC:** G1-ELE-165=A, G2-ELEC-303=A.
- **Technical/scope A-B-C evaluation:** A describes selectivity in radial protection as tripping only the closest relevant protective device and thus isolating affected circuit, not healthy load; B disconnect all loads defeats selectivity; C an arbitrary half is unrelated. 'Consumer defect' simplified compared with faulted feeder/zone; no real settings certified.
- **Source and access:** Schneider selectivity principle; https://blog.se.com/infrastructure-and-grid/power-management-metering-monitoring-power-quality/2020/04/15/circuit-breaker-selectivity-for-power-availability/.
- **Gate:** DIRECT_SELECTIVITY_SCOPE, independent review NOT_RUN, exam key NOT_VERIFIED, learner approval NO.

### G1-ELE-199 | BLOCKED_EXCLUSIVITY_ROTOR_DOUBLE_GROUND
- **Original:** Producerea dublei puneri la pământ a bobinajului rotoric al unui generator sincron are ca efect negativ
- **A:** numai creșterea foarte mare a curentului prin circuitul rotoric
- **B:** faptul că tensiunile electromotoare nu mai sunt sinusoidale
- **C:** apar scântei la periile colectorului
- **Original key:** A, unchanged. Source: ELECTROTEHNICA-09.2024-2.xlsx row 206.
- **Other grade members with exact same QABC:** G1-ELE-199=A, G2-ELEC-335=A.
- **Technical/scope A-B-C evaluation:** Two field-to-earth points can short part of rotor field winding and lead to circulating fault current, heating, insulation damage and magnetic asymmetry/vibration. A 'numai creșterea curentului' wrongly denies other effects; B EMF nonsinusoidal may or may not follow imbalance, not categorically established; C collector sparks is not a universal direct effect. No literally unique general option certified.
- **Source and access:** EPRI generator rotor defect report (indexed only); GE field rotor issue reports; independently corroborated by generator lessons-learned article; https://www.ccj-online.com/generators-lessons-learned-best-practices-shared-at-gug-2017-part-2/.
- **Gate:** BLOCKED_EXCLUSIVITY_ROTOR_DOUBLE_GROUND, independent review NOT_RUN, exam key NOT_VERIFIED, learner approval NO.

### G1-ELE-266 | CONDITIONAL_GUARANTEE_AND_INTERLOCK
- **Original:** Utilizarea întreruptoarelor debroşabile:
- **A:** asigură eliminarea unor greşeli de manevră datorate separatoarelor;
- **B:** nu asigură scurtarea duratei reviziilor la celule;
- **C:** nu asigură izolarea personalului care lucrează la întreruptor, de restul instalaţiei aflată sub tensiune.
- **Original key:** A, unchanged. Source: ELECTROTEHNICA-09.2024-2.xlsx row 273.
- **Other grade members with exact same QABC:** G1-ELE-266=A.
- **Technical/scope A-B-C evaluation:** A withdrawable breaker replaces some separate isolator manipulations and appropriate interlocks prevent unsafe racking, thus can reduce corresponding errors, but 'asigură eliminarea' must not be interpreted as all procedural errors gone. B denies shortened cell maintenance despite withdrawability; C denies operator isolation even when rack/disconnected positions and barriers correctly used; personal isolation must never be assumed without verified safe switching.
- **Source and access:** Schneider Masterclad MV switchgear drawout interlock instructions; https://productinfo.se.com/masterclad_mv_switchgear_ib/6055-40-27-kv-metal-clad-switchgear-instruction-bulletin/English/6055-40%20Masterclad%20MV%20Switchgear%20Indoor%20%28bookmap%29_DD00645165.xml/%24/Introduction-5EA6013E.
- **Gate:** CONDITIONAL_GUARANTEE_AND_INTERLOCK, independent review NOT_RUN, exam key NOT_VERIFIED, learner approval NO.

### G1-ELE-267 | CONDITIONAL_PERSONNEL_ISOLATION
- **Original:** Utilizarea întreruptoarelor debroşabile:
- **A:** asigură izolarea personalului care lucrează la întreruptor, de restul instalaţiei aflată sub tensiune.
- **B:** asigură numai scurtarea duratei reviziilor la celule;
- **C:** nu asigură eliminarea unor greşeli de manevră datorate separatoarelor;
- **Original key:** A, unchanged. Source: ELECTROTEHNICA-09.2024-2.xlsx row 274.
- **Other grade members with exact same QABC:** G1-ELE-267=A.
- **Technical/scope A-B-C evaluation:** A captures design purpose of withdrawable unit: electrical separation for maintenance under defined safe procedures, but the machine itself cannot *guarantee personnel safety* while rest remains live without barriers/interlocks/earthing/permitted approach. B says only shorten revision, denies other use; C falsely denies reduction of isolator misoperations. Classify conditionally, not a practical instruction.
- **Source and access:** Schneider Masterclad drawout isolation interlocks; https://productinfo.se.com/masterclad_mv_switchgear_ib/6055-40-27-kv-metal-clad-switchgear-instruction-bulletin/English/6055-40%20Masterclad%20MV%20Switchgear%20Indoor%20%28bookmap%29_DD00645165.xml/%24/Introduction-5EA6013E.
- **Gate:** CONDITIONAL_PERSONNEL_ISOLATION, independent review NOT_RUN, exam key NOT_VERIFIED, learner approval NO.

### G2-ELEC-030 | DIRECT_DC_TRANSFORMER_PHYSICS
- **Original:** Un transformator ideal nu poate funcționa în regim normal alimentat exclusiv cu:
- **A:** curent continuu constant
- **B:** curent alternativ
- **C:** tensiune alternativă
- **Original key:** A, unchanged. Source: Tematica și bibliografia ANRE pentru examenul de autorizare electricieni 2023, pct. 1 row 1.
- **Other grade members with exact same QABC:** G2-ELEC-030=A.
- **Technical/scope A-B-C evaluation:** Steady constant DC produces no sustained time-varying flux and hence no normal transformer output (apart from switching transient); B alternating current and C alternating voltage are normal transformer excitation. An ideal mathematical transformer has limited DC interpretation; real core saturates.
- **Source and access:** OpenStax College Physics Transformers section; https://openstax.org/books/college-physics-2e/pages/23-7-transformers.
- **Gate:** DIRECT_DC_TRANSFORMER_PHYSICS, independent review NOT_RUN, exam key NOT_VERIFIED, learner approval NO.

### G2-ELEC-051 | DIRECT_NOMINAL_VOLTAGE
- **Original:** Tensiunea nominală a unei instalații reprezintă:
- **A:** valoarea de referință pentru care instalația și echipamentele sunt destinate să funcționeze
- **B:** curentul maxim permanent
- **C:** rezistența conductorului PE
- **Original key:** A, unchanged. Source: Tematica și bibliografia ANRE pentru examenul de autorizare electricieni 2023, pct. 1 row 1.
- **Other grade members with exact same QABC:** G2-ELEC-051=A.
- **Technical/scope A-B-C evaluation:** A is voltage equipment/design reference; B has unit amperes (current), C ohms (PE resistance), dimensional distractor checks. 'Rated/nominal voltage' may have standard-specific Uo/U definitions, but generic formulation fits A.
- **Source and access:** IEC 60375 circuit quantity definition context and standard nominal rating concept; https://www.iteh.eu/catalog/standards/clc/8f705dcb-b17b-49a6-9d24-627a618d4f77/en-iec-60375-2018.
- **Gate:** DIRECT_NOMINAL_VOLTAGE, independent review NOT_RUN, exam key NOT_VERIFIED, learner approval NO.

### G2-ELEC-052 | DIRECT_CONDUCTION_LOOP
- **Original:** Un circuit electric închis este necesar pentru:
- **A:** circulația continuă a curentului într-un circuit alimentat
- **B:** măsurarea exclusivă a rezistenței
- **C:** anularea tensiunii sursei
- **Original key:** A, unchanged. Source: Tematica și bibliografia ANRE pentru examenul de autorizare electricieni 2023, pct. 1 row 1.
- **Other grade members with exact same QABC:** G2-ELEC-052=A.
- **Technical/scope A-B-C evaluation:** A a closed conducting path normally needed for sustained current from a supply; B measuring resistance exclusively isn't what 'closed circuit' means; C short-circuiting or closing does not cancel source EMF. Distinguish displacement current/dielectric circuits from pedagogical conduction example.
- **Source and access:** OpenStax intro electrical circuits (Kirchhoff) theoretical circuit convention; https://openstax.org/books/college-physics-2e/pages/20-2-electromotive-force-terminal-voltage.
- **Gate:** DIRECT_CONDUCTION_LOOP, independent review NOT_RUN, exam key NOT_VERIFIED, learner approval NO.

### G2-ELEC-063 | CONDITIONAL_B_AND_C_WORDING
- **Original:** La măsurarea unei tensiuni cu multimetrul, selectarea domeniului trebuie să fie:
- **A:** adecvată valorii estimate și categoriei de măsurare
- **B:** întotdeauna cea mai mică posibilă
- **C:** aleasă fără conectarea sondelor
- **Original key:** A, unchanged. Source: Tematica și bibliografia ANRE pentru examenul de autorizare electricieni 2023, pct. 1 row 1.
- **Other grade members with exact same QABC:** G2-ELEC-063=A.
- **Technical/scope A-B-C evaluation:** A correct range based on expected voltage and meter CAT rating. B always lowest possible range can overload/damage or error; C 'aleasă fără conectarea sondelor' may describe a desirable safety step (select range before probing), so can also be literally true; C alone says nothing about proper range but not logically false. Keep linguistic overlap blocked for strict unique choice.
- **Source and access:** Keysight Digital Multimeters safety selection/CAT guidance; https://www.keysight.com/us/en/products/digital-multimeters.html.
- **Gate:** CONDITIONAL_B_AND_C_WORDING, independent review NOT_RUN, exam key NOT_VERIFIED, learner approval NO.

### G2-ELEC-158 | CONDITIONAL_CONNECTED_GRAPH_ASSUMPTION
- **Original:** A doua teoremă a lui Kirchhoff, pentru o reţea electrică cu N noduri şi L laturi (L diferit de N), ne furnizează, pentru analiza unui circuit electric:
- **A:** L+N-1 ecuaţii distincte
- **B:** L-N +1 ecuaţii distincte
- **C:** N-L+1 ecuaţii distincte
- **Original key:** B, unchanged. Source: ELECTROTEHNICA-09.2024-2.xlsx row 12.
- **Other grade members with exact same QABC:** G1-ELE-005=B, G2-ELEC-158=B.
- **Technical/scope A-B-C evaluation:** For one connected network, a spanning tree has N-1 branches, each extra chord adds independent loop: L-(N-1)=L-N+1 -> B; A L+N-1 is not independent loop count; C N-L+1 has wrong sign except accidental equality. Stem gives L!=N but does NOT say network connected: for K connected components number cycles L-N+K, so B requires K=1. Careful note also KVL loop equations are not all network equations.
- **Source and access:** IEEE Transactions on Circuits and Systems 1991 abstract on independent Kirchhoff equations (index only); direct derivation from spanning tree; https://www.researchgate.net/publication/3184434_Proof_of_the_number_of_independent_Kirchhoff_equations_in_an_electrical_circuit.
- **Gate:** CONDITIONAL_CONNECTED_GRAPH_ASSUMPTION, independent review NOT_RUN, exam key NOT_VERIFIED, learner approval NO.

## QA gates and handoff
- 15 selected **unique** QABC units, 21 associated grade-ID occurrences across entire V73. Source-compatible direct statuses require no answer key edits but still no independent reviewer or official 2026 ANRE exam key. Material traps: 199 `numai`, 063 multimeter C can be safe, 158 connected graph missing; phase GIS fault claim absolute, withdrawable breaker safety is conditional.
- No main merge, no app, no release, no APK, no canonical keys changed. PR #7 Draft.
