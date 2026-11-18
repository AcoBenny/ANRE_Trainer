# CKPT-231 | GFR 15 legacy P2 physical laws and analog instrument equations | 2026-11-18

## Provenance and gates
- Source exact original V73 822-grade inventory blob `c027d417a8e4e605c830b2016fb55b099b8d130b`; 15 previous-individual-precheck P2 G1 original QABC, same workbook `ELECTROTEHNICA-09.2024-2.xlsx`. No duplicate focus from 227,229,230 or historic 184/189/217; all imported keys and original variants preserved. Grade II paired by exact question + A/B/C + answer key, **never numeric offset** (CKPT-228).
- Linked textbook OpenStax, vendor and engineering references for exact physical model; no ANRE official exam key and no truly independent second expert or human review. Model limitations matter for circuits and synchronous machines.
- Formula verification: W_L=½ L i²; W_C=½qV; I=U/R in Ohmic regime; RL decay α=R/L inverse seconds vs τ=L/R seconds; f=np/60 (1500 rpm, 2 pole pairs -> 50Hz); F=B I l for orthogonal vectors; e=-dΦ/dt.

### G1-ELE-063 | DIRECT_MAGNETIC_ENERGY_QUADRATIC
- Original: Energia magnetostatică produsă de curentul i care parcurge un circuit care conţine o inductanţă L este egală cu:
- A: 1/2 L i
- B: 1/2 Li2
- C: Li
- Original imported key **B** unchanged; source workbook row 70; exact counterpart G2-ELEC-208.
- A/B/C proof and model boundary: Inductor magnetic field stored energy W_L=∫0^i L i' di'=½ L i², B, assuming constant L linear magnetic core. A ½ L i and C Li are not Joules dimensionally (H·A versus J).
- Technical source: https://openstax.org/books/university-physics-volume-2/pages/14-3-energy-in-a-magnetic-field
- Evidence verdict: `DIRECT_MAGNETIC_ENERGY_QUADRATIC`, no independent technical or linguistic review, no official current ANRE exam key, `approved_for_learning=NO`.

### G1-ELE-064 | DIRECT_ELECTROSTATIC_ENERGY
- Original: Energia electrostatică a unui conductor izolat în spaţiu, încărcat cu o sarcină q şi aflat la un potenţial V este egală cu:
- A: 1/2 q V
- B: q V
- C: 2 q V
- Original imported key **A** unchanged; source workbook row 71; exact counterpart G2-ELEC-209.
- A/B/C proof and model boundary: Charged isolated conductor effective capacitance C=q/V has electrostatic field stored energy W=∫0^q (q'/C)dq'=½qV, A. B qV overstates double and C 2qV fourfold. Requires linear relation q=CV, constant geometry and zero infinity reference.
- Technical source: https://openstax.org/books/university-physics-volume-2/pages/8-3-energy-stored-in-a-capacitor
- Evidence verdict: `DIRECT_ELECTROSTATIC_ENERGY`, no independent technical or linguistic review, no official current ANRE exam key, `approved_for_learning=NO`.

### G1-ELE-065 | CONDITIONAL_SHORT_CIRCUIT_PRETRIP
- Original: În cazul producerii unui scurtcircuit într-o instalaţie, are loc următorul fenomen:
- A: creste tensiunea de alimentare a instalaţiei
- B: creste impedanţa echivalenta a instalaţiei
- C: creste curentul de alimentare a instalaţiei
- Original imported key **C** unchanged; source workbook row 72; exact counterpart G2-ELEC-210.
- A/B/C proof and model boundary: A low-impedance fault usually raises supply/fault current C up to source impedance and protection, whereas equivalent fault-path impedance decreases not increases (B), upstream voltage at fault may sag rather than rise (A). After fast protection trip supply current can fall to zero: time interval/relay state not specified, so standard moment-of-fault intended only.
- Technical source: https://www.mdpi.com/1996-1073/16/2/811
- Evidence verdict: `CONDITIONAL_SHORT_CIRCUIT_PRETRIP`, no independent technical or linguistic review, no official current ANRE exam key, `approved_for_learning=NO`.

### G1-ELE-066 | DIRECT_CHARGE_CONSERVATION
- Original: Enunţul "sarcinile electrice nu pot fi create și nici distruse, ci doar mutate" reprezintă o consecință pentru:
- A: legea conservării sarcinii electrice
- B: legea lui Coulomb
- C: legea lui Laplace
- Original imported key **A** unchanged; source workbook row 73; exact counterpart G2-ELEC-211.
- A/B/C proof and model boundary: Statement 'charges cannot be created/destroyed, only moved' is conservation of electric charge A. B Coulomb law governs forces between charges; C Laplace's law unrelated to global charge conservation. Modern particle processes can create paired +q and -q but net charge conserved; wording about individual charges is didactic shorthand.
- Technical source: https://openstax.org/books/university-physics-volume-2/pages/10-3-kirchhoffs-rules
- Evidence verdict: `DIRECT_CHARGE_CONSERVATION`, no independent technical or linguistic review, no official current ANRE exam key, `approved_for_learning=NO`.

### G1-ELE-067 | DIRECT_KIRCHHOFF_VOLTAGE
- Original: Enunţul "suma algebrică a tensiunilor electromotoare dintr-o buclă a unei reţele electrice este egală cu suma algebrică a căderilor de tensiune din buclă" reprezintă:
- A: Prima lege a lui Kirchhoff
- B: a doua lege a lui Kirchhoff
- C: Legea Joule -Lenz
- Original imported key **B** unchanged; source workbook row 74; exact counterpart G2-ELEC-212.
- A/B/C proof and model boundary: Algebraic sum of EMFs and voltage drops in a circuit loop is Kirchhoff second law, B. A first law is current conservation at node; C Joule-Lenz concerns heat I²Rt. Normal lumped-quasi-static circuit assumption for KVL, excludes strong time-variable external magnetic flux unless induced emf included.
- Technical source: https://openstax.org/books/university-physics-volume-2/pages/10-3-kirchhoffs-rules
- Evidence verdict: `DIRECT_KIRCHHOFF_VOLTAGE`, no independent technical or linguistic review, no official current ANRE exam key, `approved_for_learning=NO`.

### G1-ELE-068 | DIRECT_LORENTZ_FORCE_WIRE
- Original: Expresia B x i x l , unde i este intensitatea curentului care străbate un conductor de lungime l, situat perpendicular pe câmpul de inducţie magnetică de mărime B, reprezintă:
- A: o forţă
- B: o tensiune
- C: o rezistenţă
- Original imported key **A** unchanged; source workbook row 75; exact counterpart G2-ELEC-213.
- A/B/C proof and model boundary: A force magnitude F=B·i·l·sinθ, θ=90° by stem, so F=B i l (newtons), A. B voltage and C resistance have incompatible dimensions. Homogeneous magnetic field perpendicular to straight wire.
- Technical source: https://openstax.org/books/university-physics-volume-2/pages/11-4-magnetic-force-on-a-current-carrying-conductor
- Evidence verdict: `DIRECT_LORENTZ_FORCE_WIRE`, no independent technical or linguistic review, no official current ANRE exam key, `approved_for_learning=NO`.

### G1-ELE-069 | CONDITIONAL_OHMIC_CONDUCTOR
- Original: Expresia matematica a legii lui Ohm pentru o porţiune de circuit este:
- A: I = U / R
- B: I = UxR
- C: I = U - R
- Original imported key **A** unchanged; source workbook row 76; exact counterpart G2-ELEC-214.
- A/B/C proof and model boundary: For a linear Ohmic resistance R, I=U/R, A. B U·R wrong units; C U−R subtracts incompatible physical units. The stem 'porțiune de circuit' might include nonlinear element, but resistance as Ohmic parameter presumes fixed R in stated range; don't claim all semiconductor devices are Ohmic.
- Technical source: https://openstax.org/books/university-physics-volume-2/pages/9-4-ohms-law
- Evidence verdict: `CONDITIONAL_OHMIC_CONDUCTOR`, no independent technical or linguistic review, no official current ANRE exam key, `approved_for_learning=NO`.

### G1-ELE-070 | DIRECT_AMMETER_ANALOG_MULTIRANGE
- Original: Extinderea domeniului de măsurare la ampermetre se realizează cu:
- A: rezistente adiţionale
- B: shunturi
- C: bobine înseriate
- Original imported key **B** unchanged; source workbook row 77; exact counterpart G2-ELEC-215.
- A/B/C proof and model boundary: Shunt low resistor in parallel with ammeter movement bypasses additional current and extends measurement range, B. A series multiplier is voltmeter technique; C series inductors not generic extension for DC ammeter. Applies to conventional moving-coil/analogue instruments; modern clamp/current transformers are another technique.
- Technical source: https://openstax.org/books/college-physics-2e/pages/21-4-dc-voltmeters-and-ammeters
- Evidence verdict: `DIRECT_AMMETER_ANALOG_MULTIRANGE`, no independent technical or linguistic review, no official current ANRE exam key, `approved_for_learning=NO`.

### G1-ELE-071 | DIRECT_VOLTMETER_MULTIPLIER
- Original: Extinderea domeniului de măsurare la voltmetre se realizează cu:
- A: shunturi
- B: rezistente adiţionale
- C: condensatoare montate în paralel
- Original imported key **B** unchanged; source workbook row 78; exact counterpart G2-ELEC-216.
- A/B/C proof and model boundary: Series additional high resistance limits meter movement current at higher voltages, thus extends range B. A parallel shunts apply ammeters; C capacitors in parallel not generic voltmeter multiplier. Traditional analogue galvanometer context, not necessarily all modern electronic meters.
- Technical source: https://openstax.org/books/college-physics-2e/pages/21-4-dc-voltmeters-and-ammeters
- Evidence verdict: `DIRECT_VOLTMETER_MULTIPLIER`, no independent technical or linguistic review, no official current ANRE exam key, `approved_for_learning=NO`.

### G1-ELE-072 | DIRECT_RL_DECAY_COEFFICIENT
- Original: Factorul de atenuare al unui circuit format dintr-un rezistor de rezistenţă R înseriat cu o bobină de inductanţă L, alimentate de o tensiune electromotoare constantă este egal cu:
- A: R/L
- B: L/R
- C: 1
- Original imported key **A** unchanged; source workbook row 79; exact counterpart G2-ELEC-217.
- A/B/C proof and model boundary: For L di/dt+R i=E constant, transient e^{-t R/L}; exponential attenuation rate α=R/L (s^-1), A. B L/R is time constant τ (s), not attenuation rate; C dimensionless 1 cannot equal R/L generally. Note 'factor de atenuare' may be ambiguous label but conventional decay coefficient rate.
- Technical source: https://openstax.org/books/university-physics-volume-2/pages/14-4-rl-circuits
- Evidence verdict: `DIRECT_RL_DECAY_COEFFICIENT`, no independent technical or linguistic review, no official current ANRE exam key, `approved_for_learning=NO`.

### G1-ELE-074 | DIRECT_BUNDLED_CORONA_MITIGATION
- Original: Folosirea conductoarelor jumelate în construcţia LEA are ca scop principal:
- A: reducerea pierderilor Corona
- B: reducerea solicitărilor mecanice ale stâlpilor
- C: reducerea curenţilor de scurtcircuit
- Original imported key **A** unchanged; source workbook row 81; exact counterpart G2-ELEC-219.
- A/B/C proof and model boundary: Bundled/jumelate overhead transmission conductors increase equivalent radius, reduce surface electric field gradients and Corona discharge losses A. B mechanical post force reduction not primary (more conductors can increase weight/drag), C short circuit current limited by network impedance not bundle split. Bundles also affect reactance/capacity/noise, not sole objective.
- Technical source: https://ctcglobal.com/wp-content/uploads/2023/05/Engineering_Transmission_Lines_with_ACCC_Conductor.pdf
- Evidence verdict: `DIRECT_BUNDLED_CORONA_MITIGATION`, no independent technical or linguistic review, no official current ANRE exam key, `approved_for_learning=NO`.

### G1-ELE-075 | DIRECT_ALTERNATOR_RPM_POLE_PAIRS
- Original: Formula de calcul a frecventei produsa în sistemul electroenergetic de un generator cu n [rot/min] si p perechi de poli este:
- A: f =n p / 60
- B: f = 60 n / p
- C: f = 60 p / n
- Original imported key **A** unchanged; source workbook row 82; exact counterpart G2-ELEC-220.
- A/B/C proof and model boundary: Mechanical speed n rpm and p POLE PAIRS gives electrical frequency f=n p /60 Hz, A. B f=60n/p and C f=60p/n invert units. Example n=1500rpm,p=2 -> f=50Hz, consistent with 4-pole synchronous alternator.
- Technical source: https://www.pjm.com/-/media/DotCom/training/nerc-certifications/trans-exam-materials/bet/bet-lesson6-generator-theory.ashx
- Evidence verdict: `DIRECT_ALTERNATOR_RPM_POLE_PAIRS`, no independent technical or linguistic review, no official current ANRE exam key, `approved_for_learning=NO`.

### G1-ELE-076 | DIRECT_MOTIONAL_EMF_FARADAY
- Original: Formula e = B l v, unde e este tensiune electromotoare, B este inducţia magnetică, l este lungimea unui conductor, v este viteza de deplasare a acestuia, reprezintă o forma particulară a:
- A: teoremelor Biot-Savart
- B: legii inducţiei electromagnetice
- C: legii circuitului magnetic
- Original imported key **B** unchanged; source workbook row 83; exact counterpart G2-ELEC-221.
- A/B/C proof and model boundary: Motional emf |e|=B l v when moving rod of length l perpendicular to both field and movement, Faraday induction in moving conductor, B. A Biot-Savart determines B from current, C magnetic-circuit law different relation. Correct orientation is crucial, not universal formula for arbitrary angles.
- Technical source: https://openstax.org/books/university-physics-volume-2/pages/13-3-motional-emf
- Evidence verdict: `DIRECT_MOTIONAL_EMF_FARADAY`, no independent technical or linguistic review, no official current ANRE exam key, `approved_for_learning=NO`.

### G1-ELE-078 | DIRECT_FORCE_BETWEEN_CURRENTS
- Original: Forţa care se exercită între două conductoare străbătute de curenţi electrici se numeşte:
- A: forţă electrocinetică
- B: forţă electrodinamică
- C: forţă magnetomotoare
- Original imported key **B** unchanged; source workbook row 85; exact counterpart G2-ELEC-223.
- A/B/C proof and model boundary: Magnetic interaction between two current-carrying conductors is electrodynamic force, B. A electrocinetic is nonstandard/other designation and C magnetomotive force is NI in ampere-turns, not mechanical force.
- Technical source: https://openstax.org/books/university-physics-volume-2/pages/12-3-magnetic-force-between-two-parallel-currents
- Evidence verdict: `DIRECT_FORCE_BETWEEN_CURRENTS`, no independent technical or linguistic review, no official current ANRE exam key, `approved_for_learning=NO`.

### G1-ELE-079 | DIRECT_FARADAY_TIME_DERIVATIVE
- Original: Tensiunea electromotoare indusă într-un circuit închis, prin variaţia fluxului magnetic, este:
- A: direct proporţională cu variaţia în timp a fluxului magnetic
- B: invers proporţională cu variaţia în timp a fluxului magnetic
- C: dependentă de modul în care este produs fluxul magnetic
- Original imported key **A** unchanged; source workbook row 86; exact counterpart G2-ELEC-224.
- A/B/C proof and model boundary: Faraday e=-dΦ/dt for single turn (or -N dΦ/dt coil), A intended 'variația în timp' means time derivative, not just total Φ. B inverse change false, C dependence on how flux was produced false at fixed dΦ/dt; minus sign denotes Lenz polarity.
- Technical source: https://openstax.org/books/university-physics-volume-2/pages/13-3-motional-emf
- Evidence verdict: `DIRECT_FARADAY_TIME_DERIVATIVE`, no independent technical or linguistic review, no official current ANRE exam key, `approved_for_learning=NO`.

## Handoff
- Existing 15 Grade I QABC / 30 paired Grade I+II entries, but not 30 unique source reviews. 2 explicitly conditional model cases; no imported-key corrections, no new bank entries and no approved-for-learning states. Next 8 remaining historical P2 G1 records; older G1-ELE-014/051/053/057 remain previously analyzed, to be linked not recounted. PR7 remains Draft, no app or release.
