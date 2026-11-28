# CKPT-185 | 6 more blocked equipment/model cases: GIS, motors, oil, busbar separator, eddy currents | 2026-11-17

Continuation after CKPT-184 HEAD `a526ba113a195d85fe10e9ec5280d5ff0643935b`. Preserve all 568 research units / 822 grade-ID canonicals and source history. Six **existing** flagged items; no new question count. Technical, linguistic and source rereview in one assistant, **not independent reviewer QA**. All exam keys remain unchanged and not learner-approved.

## Six source/scope cards

### G1-ELE-020 | ABSOLUTE_TOTAL_PHASE_FAULT
- Existing unit `AU-2cde95d7e7d5db22`; SHA256 `2cde95d7e7d5db224bab9db349a454498374a13032a45a8c74984d62f3008b21`; original grade entries: G1-ELE-020=A, G2-ELEC-172=A **UNCHANGED**.
- **Original question:** Capsularea monopolară conduce la :
- **A:** eliminarea totală a posibilităţii apariţiei unui scurtcircuit între faze;
- **B:** micşorarea riscului unor pierderi de gaz izolant;
- **C:** reducerea cheltuielilor de realizare a instalaţiilor.
- **Exact three-option and model analysis:** A single-pole encapsulation isolates each phase inside its own enclosure and can physically reduce internal phase-phase fault exposure; «eliminarea totală» cannot be shown for whole installation incl. bushings, external terminals or damaged equipment. B reducing gas leaks isn't guaranteed by pole separation. C initial/maintenance cost is design-dependent.
- **Source(s), access mode:** Hitachi Energy single-phase GIS BLF/PASS: https://www.hitachienergy.com/in/en/products-and-solutions/high-voltage-switchgear-and-breakers/gas-insulated-switchgear/gis-for-72-5-1200-kv/gis-blf-pass-up-to-170-kv (HTML_DIRECT_OPENED)
- **Provisional intent:** A interpreted as within fully enclosed apparatus, universal total false. **Remaining blocker:** No exact model specification or 2026 Romanian curriculum source establishing absolute elimination; keep original A only as intended model.
- `approved_for_learning=NO`; independent technical/source/linguistic QA NOT_RUN; official 2026 exam grade/key NOT_VERIFIED.

### G1-ELE-088 | GIS_PARTITIONING_OCCURRENCE_VS_EFFECTS
- Existing unit `AU-d9b2acc9d5918419`; SHA256 `d9b2acc9d5918419d33407eede73f37aceafef41c4bc637015f13723c505fd52`; original grade entries: G1-ELE-088=A, G2-ELEC-233=A **UNCHANGED**.
- **Original question:** Împărţirea fiecărei faze a unei instalaţii capsulate într-un anumit număr de compartimente atrage după sine:
- **A:** limitarea posibilităţilor de producere a unui defect în instalaţie;
- **B:** mărirea riscului de producere a unor scăpări de gaz;
- **C:** mărirea cantităţilor de gaz ce trebuie manipulate în cazul intervenţiei la un compartiment.
- **Exact three-option and model analysis:** A partitions limit size/impact and propagation of a compartment fault but do not prove decrease of primary initiation likelihood. B more joints/seals may change leak opportunities, not automatic measured higher risk. C evacuating only a compartment usually handles a smaller rather than larger gas volume than one giant compartment, but exact volumes unknown.
- **Source(s), access mode:** IEC 62271-203 informed HTML discussion of compartment effects and service: https://switchgearcontent.com/2019/05/23/494/requirements-for-enclosure-partitioning-in-gis-design-according-to-iec-standard/ (HTML_DIRECT_OPENED, SECONDARY summary, official full IEC not opened)
- **Provisional intent:** A intended only if «possibilities» means consequences/propagation. **Remaining blocker:** Questions says «posibilităţilor de producere a unui defect» rather than containment, so negative counterexample matters. Manufacturer-specific compartments/fault frequency missing.
- `approved_for_learning=NO`; independent technical/source/linguistic QA NOT_RUN; official 2026 exam grade/key NOT_VERIFIED.

### G1-ELE-099 | AUTORESTART_NOT_ROTOR_TYPE_INVARIANT
- Existing unit `AU-314df2294abc59d6`; SHA256 `314df2294abc59d60451a7a17d3874d416f928c8dd8ad8813e357435b4a4c54c`; original grade entries: G1-ELE-099=A, G2-ELEC-242=A **UNCHANGED**.
- **Original question:** În cazul scăderii sau întreruperii tensiunii de alimentare, motoarele asincrone se pot opri, iar la restabilirea tensiunii:
- **A:** ele autopornesc, indiferent de tipul constructiv al rotorului în scurtcircuit
- **B:** pentru a reporni necesită dispozitiv de pornire
- **C:** ele autopornesc numai dacă au rotor în dublă colivie
- **Exact three-option and model analysis:** A «indiferent» de rotor and implicit automatic restart ignores undervoltage lockout/contactors/operator sequence. B an explicit starter might be needed in certain control arrangements, not all. C double-cage rotor is not a prerequisite to electric re-start, though rotor design affects torque.
- **Source(s), access mode:** Schneider Electric Motor protection functions https://www.electrical-installation.org/enwiki/Motor_protection_functions (HTML_DIRECT_OPENED, motor reclosing separately configured), https://productinfo.se.com/tesys_tera_ug/tesys-tera-motor-management-system-user-guide/EN/TeSys-Tera-User%20Guide-DOCA0257EN-02.xml/%24/W2_TeSys_Tera_UG_Automatic_Restart_0001016455 (SEARCH_EXCERPT_ONLY_DIRECT_CACHE_MISS)
- **Provisional intent:** No universal A/B/C, restart is control-dependent. **Remaining blocker:** Needs declared self-start circuit/control design, motor rotor details insufficient. This is a safety-relevant operational model, not a universal rotor-only rule.
- `approved_for_learning=NO`; independent technical/source/linguistic QA NOT_RUN; official 2026 exam grade/key NOT_VERIFIED.

### G1-ELE-104 | OIL_MULTIROLE_EQUIPMENT_SCOPE
- Existing unit `AU-f7f04edda7082ffb`; SHA256 `f7f04edda7082ffbc8860e80ffdfaa556a83e46b96c1419997ada2cd1a56bf73`; original grade entries: G1-ELE-104=A, G2-ELEC-247=A **UNCHANGED**.
- **Original question:** În echipamentul electric, uleiul electroizolant, din punct de vedere electric:
- **A:** asigură doar izolarea părților sub tensiune între ele si fatã de masã
- **B:** stinge arcul electric care apare in întrerupătoare
- **C:** asigura ungerea mecanismelor de acţionare
- **Exact three-option and model analysis:** A insulating oil indeed electrically isolates live components, but «doar» denies its additional role in oil CB. B true in an oil circuit breaker where oil quenches arc, not necessarily in transformer where oil is primarily dielectric/cooling. C lubrication is not the principal electrical purpose.
- **Source(s), access mode:** National Institute of Technology Karnataka Virtual Labs university teaching HTML: https://sa-nitk.vlabs.ac.in/exp/simulation-transformer/theory.html (HTML_DIRECT_OPENED; confirms oil CB dielectric and arc quenching)
- **Provisional intent:** B supported specifically in oil circuit-breakers, A «doar» too strong. **Remaining blocker:** Stem says general «în echipamentul electric», not «în întreruptor cu ulei»; different equipment means no universally true choice. Wrong A is documented but not replaced with B universally.
- `approved_for_learning=NO`; independent technical/source/linguistic QA NOT_RUN; official 2026 exam grade/key NOT_VERIFIED.

### G1-ELE-122 | BUS_DISCONNECTOR_MULTIROLE_NO_UNIVERSAL_ONLY
- Existing unit `AU-dac8a21bd3faca36`; SHA256 `dac8a21bd3faca36f265a1fb2834735d1476c8c95e4f5b5db3684f800544f235`; original grade entries: G1-ELE-122=A, G2-ELEC-264=A **UNCHANGED**.
- **Original question:** Într-o schemă electrică prevăzută cu mai multe sisteme de bare colectoare, separatorul de bare
- **A:** asigură doar selectarea sistemului de bare pe care urmează a fi conectat circuitul;
- **B:** asigură izolarea unei părţi a circuitului de bara colectoare aflată sub tensiune;
- **C:** comutaţia curentului în regim normal de funcţionare.
- **Exact three-option and model analysis:** A separatorul de bare selects a bus, but «doar» ignores the isolation function. B isolates part of a circuit from busbar, plausibly true with proper de-energized / permitted switching conditions. C a simple isolator should not be treated as a load-breaking circuit breaker; switch-disconnector (special class) may carry different rated duties.
- **Source(s), access mode:** Schneider direct isolator distinction https://www.se.com/ae/en/faqs/FA381456/ (HTML_DIRECT_OPENED, low voltage/general isolating principle; not exact double-busbar MV/HV diagram)
- **Provisional intent:** A and B describe different disconnector functions, C unsupported load-breaking. **Remaining blocker:** Exact busbar separator model and admissible load-switching capability still absent. Generic source supports function distinction but not exam's exact topology.
- `approved_for_learning=NO`; independent technical/source/linguistic QA NOT_RUN; official 2026 exam grade/key NOT_VERIFIED.

### G1-ELE-180 | MULTIPLE_TRUE_EDDY_CURRENT_REMEDIES
- Existing unit `AU-e96a54cfe693a32b`; SHA256 `e96a54cfe693a32b24e57e80fc3b3520ffae0eeadff030e7b8e2c4cc265f6c90`; original grade entries: G1-ELE-180=B, G2-ELEC-316=B **UNCHANGED**.
- **Original question:** Pentru micşorarea pierderilor de putere prin curenţi turbionari în piesele metalice mari parcurse de fluxuri magnetice variabile:
- **A:** se limitează dimensiunile pieselor
- **B:** se execută piesele metalice din tole de oţel  cu adaus de siliciu pentru mărirea rezistivităţii, subţiri și izolate între ele
- **C:** se evită plasarea pieselor metalice masive în câmpuri magnetice variabile
- **Exact three-option and model analysis:** A geometrical reduction of conductor path/loop may limit eddy-current loss under fixed field. B thin, mutually insulated high-resistivity silicon-steel laminations directly reduce induced loops and losses, textbook method. C removing massive metal parts from changing magnetic flux also reduces losses. Thus A/B/C need exclusive object or «most effective practical method», absent from stem.
- **Source(s), access mode:** IEEE Technology Navigator eddy currents https://technav.ieee.org/topic/eddy-currents/ (INDEXED_SUMMARY), Wiley 'Laminated Cores' https://onlinelibrary.wiley.com/doi/10.1002/9781118717806.ch6 (SEARCH_EXCERPT_ONLY, DIRECT_403)
- **Provisional intent:** B direct standard method, A/C may also reduce actual losses. **Remaining blocker:** Candidate B is conceptually standard method, but alternatives are not necessarily wrong. Do not force unique grade key on incomplete experimental conditions.
- `approved_for_learning=NO`; independent technical/source/linguistic QA NOT_RUN; official 2026 exam grade/key NOT_VERIFIED.

## QA / immutable boundaries
- Strict original question, original A/B/C, imported key equality against 822-row V73 for **6 unique units / 12 grade IDs**: 0 mismatches. Units and their SHA256 strings inherited from CKPT141/142 (not recalculated cryptographically).
- Scope tests are **context-sensitive**: internal GIS pole separation vs whole power installation, GIS compartment containment vs fault probability, automatic restart control logic vs rotor type, oil breaker vs transformer, isolated busbar vs switch-disconnector capability, reductions from laminations vs alternative safe configurations.
- This session's additive fresh rereviews: CKPT182 ten + CKPT183 six + CKPT184 seven + CKPT185 six = **29 pre-existing units** (not 29 final source/answer authorizations). Prior CKPT181 separate. No original key edits, HTML/APK edits, main merge, or release. All study gates remain NO. Do not treat exact source retrieval failure or synthetic checks as signoff.
- Next: source-targeted resolution of remaining blocked items in CKPT141/142/145/148/153 and official 2026 question-key provenance. Escalate only truly irreducible user-choice semantic questions with full original QABC and neighborhood.
