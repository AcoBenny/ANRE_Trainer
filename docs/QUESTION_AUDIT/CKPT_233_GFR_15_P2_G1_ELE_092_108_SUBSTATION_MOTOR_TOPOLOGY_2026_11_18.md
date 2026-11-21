# CKPT-233 | 15 GFR P2 source-focused power-systems questions | 2026-11-18

Exact canonical QABC, imported keys and workbook provenance were copied from V73 Git blob c027d417a8e4e605c830b2016fb55b099b8d130b. All are existing P2 unique Grade I units, no key or original card change. Sources are technical and manufacturer evidence, NOT ANRE scored keys. No independent model/human QA. Substation explanations are not switching instructions.

## G1-ELE-092 | CONDITIONAL_LIQUID_TRANSFORMER_URBAN
- Original: În posturi de transformare se folosesc transformatoare răcite cu lichide neinflamabile atunci când:
- A: sunt restricţii de poluare a mediului;
- B: sunt restricţii de toxicitate pentru personalul de exploatare;
- C: amplasarea postului se face în zone aglomerate.
- Imported key C preserved. Source ELECTROTEHNICA-09.2024-2.xlsx row 99; exact Grade II mate G2-ELEC-236.
- Technical A/B/C and qualifiers: Non-flammable or high-fire-point insulating liquids can help when substations are installed in crowded areas (C). A pollution restrictions might also motivate special biodegradable fluids, so selection is not exclusively about population density; B personnel toxicity is liquid-specific.
- Source: https://www.electrical-installation.org/enwiki/Choice_of_MV/LV_transformer
- Gate: single-assistant source review only, no official exam key, no independent QA, approved_for_learning=NO.

## G1-ELE-093 | DIRECT_FUSE_SHORT_CIRCUIT_WITH_THERMAL_RELAY
- Original: În cazul în care echiparea circuitelor electrice de alimentare a motoarelor electrice se face cu siguranţă fuzibilă şi contactor cu relee termice:
- A: siguranţa fuzibilă realizează protecţia la suprasarcină;
- B: siguranţa fuzibilă realizează protecţia la scurtcircuit;
- C: siguranţa fuzibilă realizează protecţia la supratensiuni;
- Imported key B preserved. Source ELECTROTEHNICA-09.2024-2.xlsx row 100; exact Grade II mate G2-ELEC-237.
- Technical A/B/C and qualifiers: B fuse is assigned short-circuit protection in a fuse+contactor+thermal relay starter, relay handles thermal overload; A can be true for other all-range fuse arrangements but this question expressly includes the thermal relay; C overvoltage a different hazard.
- Source: https://www.se.com/uk/en/product-range/1271-tesys-d
- Gate: single-assistant source review only, no official exam key, no independent QA, approved_for_learning=NO.

## G1-ELE-095 | DIRECT_ZERO_SEQUENCE_FORTESCUE
- Original: În cazul în care rezultanta unui sistem de fazori (de tensiune sau de curent) este nulă:
- A: sistemul nu are componentă simetrică inversă (negativă)
- B: sistemul nu are componentă simetrică homopolară (zero)
- C: sistemul nu are are componentă simetrică directă (pozitivă)
- Imported key B preserved. Source ELECTROTEHNICA-09.2024-2.xlsx row 102; exact Grade II mate G2-ELEC-238.
- Technical A/B/C and qualifiers: For three phase phasors, zero sequence X0=(X1+X2+X3)/3. Sum zero implies no zero-sequence component (B). Positive and negative symmetrical sequences may remain, so A/C are not proven by zero sum.
- Source: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electro-Optics/Introduction_to_Electric_Power_Systems_%28Kirtley%29/04%3A_Introduction_to_symmetrical_components/4.02%3A_The_Symmetrical_Component_Transformation
- Gate: single-assistant source review only, no official exam key, no independent QA, approved_for_learning=NO.

## G1-ELE-096 | DIRECT_STAR_DELTA_START_CURRENT
- Original: În cazul pornirii stea triunghi a motoarelor asincrone, curentul de pornire la conexiunea stea este:
- A: 1/3 din curentul de pornire la conexiunea triunghi
- B: de 3 ori curentul de pornire la conexiunea triunghi
- C: de 2 ori curentul de pornire la conexiunea triunghi
- Imported key A preserved. Source ELECTROTEHNICA-09.2024-2.xlsx row 103; exact Grade II mate G2-ELEC-239.
- Technical A/B/C and qualifiers: Same three-phase motor and supply with delta-rated windings: Y line starting current about one-third of direct Δ starting line current, A. B 3 times and C 2 times do not fit. Motor must be suited for Y-Δ and line vs phase currents must not be confused.
- Source: https://fuse.etigroup.eu/media-center/eti-blog/star-delta-switch-a-smarter-way-to-start-three-phase-motors?lang=en-GB
- Gate: single-assistant source review only, no official exam key, no independent QA, approved_for_learning=NO.

## G1-ELE-097 | CONDITIONAL_DRY_TYPE_CROWDED_SITE
- Original: În posturi de transformare se preferă folosirea transformatoarelor răcite cu aer atunci când:
- A: sunt restricţii de teren;
- B: sunt restricţii privitoare la zgomot;
- C: amplasarea postului se face în zone aglomerate.
- Imported key C preserved. Source ELECTROTEHNICA-09.2024-2.xlsx row 104; exact Grade II mate G2-ELEC-240.
- Technical A/B/C and qualifiers: Dry transformer lacks mineral insulating oil/fire spill hazard and is often preferred indoors in populated areas C. A restricted land may be relevant to compact siting, B sound emissions vary, and thermal ventilation requirements remain.
- Source: https://new.abb.com/news/detail/5787/home-and-dry
- Gate: single-assistant source review only, no official exam key, no independent QA, approved_for_learning=NO.

## G1-ELE-098 | DIRECT_ISOLATED_NEUTRAL_EARTH_FAULT
- Original: În cazul punerii nete la pământ a fazei S         într-o reţea de 20 kV cu neutrul izolat:
- A: tensiunea pe fazele R si T rămâne neschimbata , iar tensiunea fazei defecte S se apropie de 0
- B: tensiunea pe fazele R si T creste la valoarea tensiunii de linie iar pe faza S se apropie de 0
- C: cresc tensiunile pe fazele R si T, iar pe faza defecta S rămâne neschimbata
- Imported key B preserved. Source ELECTROTEHNICA-09.2024-2.xlsx row 105; exact Grade II mate G2-ELEC-241.
- Technical A/B/C and qualifiers: Bolted line-to-earth fault of isolated-neutral phase S shifts healthy R/T voltage to ground up to line-to-line nominal voltage, S-earth drops near zero; B. A/C miss healthy rise or fault voltage drop. Steady ideal model; arcing earth fault transient not captured.
- Source: https://www.electrical-installation.org/enwiki/IT_system_-_Fault_protection
- Gate: single-assistant source review only, no official exam key, no independent QA, approved_for_learning=NO.

## G1-ELE-099 | BLOCKED_AUTO_RESTART_CONTROL_NOT_ROTOR
- Original: În cazul scăderii sau întreruperii tensiunii de alimentare, motoarele asincrone se pot opri, iar la restabilirea tensiunii:
- A: ele autopornesc, indiferent de tipul constructiv al rotorului în scurtcircuit
- B: pentru a reporni necesită dispozitiv de pornire
- C: ele autopornesc numai dacă au rotor în dublă colivie
- Imported key A preserved. Source ELECTROTEHNICA-09.2024-2.xlsx row 106; exact Grade II mate G2-ELEC-242.
- Technical A/B/C and qualifiers: A claims all short-circuit-rotor induction motors restart autonomously on voltage return, false without a self-holding or auto-restart control and may be unsafe. B says all need a starter, not true for all controls. C incorrectly limits auto-start to double-cage rotor. Contactor, undervoltage protection and safety conditions absent. Key A NOT certified.
- Source: https://www.se.com/us/en/faqs/FA175133/
- Gate: single-assistant source review only, no official exam key, no independent QA, approved_for_learning=NO.

## G1-ELE-100 | BLOCKED_DOUBLE_BUS_SCHEME_UNDERSPECIFIED
- Original: În cazul schemelor cu două sisteme de bare colectoare şi un întreruptor pe circuit, funcţionarea cu ambele sisteme de bare sub tensiune este avantajoasă deoarece permite:
- A: scurtarea duratei manevrelor în caz de ocolire a unui întreruptor;
- B: micşorarea daunelor de nealimentare a consumatorilor în caz de scurtcircuit pe unul dintre sistemele de bare;
- C: scurtarea duratei manevrelor în caz de revizie a unuia dintre sistemele de bare colectoare.
- Imported key A preserved. Source ELECTROTEHNICA-09.2024-2.xlsx row 107; exact Grade II mate G2-ELEC-243.
- Technical A/B/C and qualifiers: Both main buses energized may reduce some transfer operations, but original A specifically assumes breaker bypass possibility without defining bypass bus/coupler. B avoiding loss on a busbar fault depends on load distribution; C busbar maintenance transfer likewise topology-specific. No single unconditional truth without SLD.
- Source: https://eepower.com/technical-articles/substation-componentspart-5-busbar-configurations/
- Gate: single-assistant source review only, no official exam key, no independent QA, approved_for_learning=NO.

## G1-ELE-101 | CONDITIONAL_COLD_RESERVE_TRANSFER
- Original: În cazul schemelor cu două sisteme de bare colectoare şi un întreruptor pe circuit, funcţionarea cu unul dintre sistemele de bare în rezervă rece ( fără tensiune) este avantajoasă
- A: numai atunci când se doreşte scurtarea duratei manevrelor în caz de ocolire a unui întreruptor;
- B: atunci când se doreşte micşorarea daunelor de nealimentare a consumatorilor în caz de scurtcircuit pe unul dintre sistemele de bare;
- C: atunci când se doreşte scurtarea duratei manevrelor în caz de revizie a unuia dintre sistemele de bare colectoare.
- Imported key B preserved. Source ELECTROTEHNICA-09.2024-2.xlsx row 108; exact Grade II mate G2-ELEC-244.
- Technical A/B/C and qualifiers: Cold reserve bus can reduce busbar-fault outage impact if healthy bus transfer path and source exist, B. A only breaker-bypass is too restrictive, C maintenance transfer may also be relevant. Needs switchgear single-line and protection details; no operational instructions.
- Source: https://eepower.com/technical-articles/substation-componentspart-5-busbar-configurations/
- Gate: single-assistant source review only, no official exam key, no independent QA, approved_for_learning=NO.

## G1-ELE-103 | CONDITIONAL_AAR_COUPLER_READY
- Original: În cazul unei staţii cu un sistem de bare colectoare secţionat longitudinal şi prevăzut cu o cuplă longitudinală cu întreruptor şi AAR, cupla se menţine:
- A: în rezervă caldă;
- B: în rezervă rece;
- C: În funcţiune
- Imported key A preserved. Source ELECTROTEHNICA-09.2024-2.xlsx row 110; exact Grade II mate G2-ELEC-246.
- Technical A/B/C and qualifiers: With divided busbar and automatic reserve transfer, bus coupler often normally open but armed/ready for automatic transfer, matching A warm standby. B cold reserve and C always closed do not reflect intended arrangement. Exact definition of warm standby and protection permissives topology-dependent.
- Source: https://www.phasetophase.nl/book/book_1_2.html
- Gate: single-assistant source review only, no official exam key, no independent QA, approved_for_learning=NO.

## G1-ELE-104 | BLOCKED_DIELECTRIC_OIL_ALSO_QUENCHES_ARC
- Original: În echipamentul electric, uleiul electroizolant, din punct de vedere electric:
- A: asigură doar izolarea părților sub tensiune între ele si fatã de masã
- B: stinge arcul electric care apare in întrerupătoare
- C: asigura ungerea mecanismelor de acţionare
- Imported key A preserved. Source ELECTROTEHNICA-09.2024-2.xlsx row 111; exact Grade II mate G2-ELEC-247.
- Technical A/B/C and qualifiers: A includes restrictive doar (only dielectric insulation), but in oil circuit breakers the oil also quenches electric arc. B holds for oil circuit breaker but not all oil-insulated transformers. C lubrication mechanical is not generic electrical role. Equipment unspecified -> cannot certify A as only answer.
- Source: https://www.electrical-installation.org/enwiki/Choice_of_MV/LV_transformer
- Gate: single-assistant source review only, no official exam key, no independent QA, approved_for_learning=NO.

## G1-ELE-105 | SOURCE_COMPATIBLE_BREAKER_AND_HALF
- Original: Într-o schemă cu 1,5 întreruptoare pe circuit:
- A: este necesară o cuplă de ocolire;
- B: este necesară o cuplă transversală;
- C: nu sunt necesare circuite de cuplă transversală şi de ocolire
- Imported key C preserved. Source ELECTROTEHNICA-09.2024-2.xlsx row 112; exact Grade II mate G2-ELEC-248.
- Technical A/B/C and qualifiers: One-and-a-half breaker arrangement connects two feeders through three breakers between two main busbars. No separate bypass (A) or transverse bus coupler (B) inherently necessary; C is usual topology. Product/configuration-dependent engineering safeguards.
- Source: https://eepower.com/technical-articles/substation-componentspart-5-busbar-configurations/
- Gate: single-assistant source review only, no official exam key, no independent QA, approved_for_learning=NO.

## G1-ELE-106 | CONDITIONAL_TRANSFER_BYPASS_BUS
- Original: Într-o schemă de conexiuni bara şi cupla de ocolire servesc la:
- A: scoaterea în revizie a unui întreruptor, cu două scurte întreruperi;
- B: scoaterea în revizie a unei bare colectoare;
- C: scoaterea în revizie a unui întreruptor, fără întreruperea alimentării pe circuitul respectiv.
- Imported key C preserved. Source ELECTROTEHNICA-09.2024-2.xlsx row 113; exact Grade II mate G2-ELEC-249.
- Technical A/B/C and qualifiers: Transfer/bypass bus and coupler intended to allow circuit breaker maintenance while preserving feeder energization where switching arrangement permits, C. A two short interruptions are not intrinsic, B busbar revision not primary role. No switching sequence provided.
- Source: https://eepower.com/technical-articles/substation-componentspart-5-busbar-configurations/
- Gate: single-assistant source review only, no official exam key, no independent QA, approved_for_learning=NO.

## G1-ELE-107 | DIRECT_DRY_TRANSFORMER_CROWDED_SITE
- Original: În posturi de transformare se folosesc transformatoare uscate atunci când:
- A: amplasarea postului se face în zone aglomerate;
- B: nu sunt restricţii de teren;
- C: nu este posibilă asigurarea unei răciri corespunzătoare a bobinajelor.
- Imported key A preserved. Source ELECTROTEHNICA-09.2024-2.xlsx row 114; exact Grade II mate G2-ELEC-250.
- Technical A/B/C and qualifiers: Dry-type safer near populated / indoor sites where oil fire and leaks problematic, intended A. B no land restrictions irrelevant; C insufficient ability to cool windings would be unsafe for any transformer.
- Source: https://new.abb.com/news/detail/5787/home-and-dry
- Gate: single-assistant source review only, no official exam key, no independent QA, approved_for_learning=NO.

## G1-ELE-108 | SOURCE_COMPATIBLE_RING_BUSBAR
- Original: Într-o schemă poligon cu patru laturi:
- A: este necesară o cuplă de ocolire;
- B: este necesară o cuplă transversală;
- C: nu este necesară o cuplă transversală.
- Imported key C preserved. Source ELECTROTEHNICA-09.2024-2.xlsx row 115; exact Grade II mate G2-ELEC-251.
- Technical A/B/C and qualifiers: Four-side ring bus uses its circuit breakers as interconnected ring; separate transverse coupler not necessary C, A bypass coupler not required, B transverse coupler not required. Real arc-fault protection and operational reliability vary by ring state.
- Source: https://eepower.com/technical-articles/substation-componentspart-5-busbar-configurations/
- Gate: single-assistant source review only, no official exam key, no independent QA, approved_for_learning=NO.

## Count and handoff
15 unique original QABC, 15 exact cross-grade occurrences, 0 imported key edits, 0 learning approvals. Material blockers ELE099 autorestart, ELE100 bypass topology, ELE104 dielectric oil 'only'. GFR continue on remaining P2. PR7 Draft, no app, APK or HTML edits.
