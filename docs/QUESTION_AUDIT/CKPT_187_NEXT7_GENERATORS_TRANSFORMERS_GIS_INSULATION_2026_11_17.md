# CKPT-187 | Seven blocked generators/transformers, insulation, GIS and distribution questions | 2026-11-17

Continuation from CKPT186, branch HEAD `d1dcc4fb8c6742f259b73e8ea5414c0052aea3f0`. This is **seven existing source/wording rechecks**, not new QABC units or an answer-key publication. Original imported keys/grades/QABC unchanged, PR #7 Draft. Same assistant performs technical/source/linguistic checklist; no independent reviewer. Source access failures expressly preserved.

## Seven original items

### G1-ELE-178 | REACTIVE_POWER_NOT_LITERAL_DDT_STORED
- Existing unit `AU-2ad66252f57dac02`; original QABC SHA `2ad66252f57dac0252edab9783996d098f73798a3e73ffb2919497db6e5efe41`; original grade keys G1-ELE-178=C, G2-ELEC-314=C **unchanged**.
- **Question:** Puterea electrică reactivă:
- **A:** permite definirea limitelor de utilizare ale unui aparat electric
- **B:** produce transformarea energiei electrice în energie mecanică
- **C:** este variaţia în timp a energiei magnetice şi electrice
- **Each option, model/terminology:** A reactive power Q alone is not the apparent-power current-rating limit of equipment. B mechanical useful energy conversion associates active power, not purely reactive Q. C reactive energy oscillates between magnetic and electric storage in sinusoidal AC; but Q (VAr) is a cycle-level quantity, not universally identical at each instant to the derivative of storage.
- **Exact-source leads and access:** Schneider Electrical Installation Guide https://www.electrical-installation.org/enwiki/Definition_of_reactive_power (HTML_DIRECT_OPENED; S,P,Q,cos phi); academic explicit stored-energy time-domain exact instantaneous equality NOT sourced
- **Exam intent only:** C intended field-energy exchange, not exact instantaneous identity. **Blocker:** Original C plausible didactic shorthand only, without a specific idealized capacitor/inductor model it cannot be singularly asserted.
- `approved_for_learning=NO`, independently audited source/technical/linguistic QA NOT_RUN; official ANRE 2026 grade key/edition not independently verified.

### G1-ELE-199 | SECOND_EARTH_FAULT_MULTIPLE_EFFECTS
- Existing unit `AU-0cf2f9bbd6d9e798`; original QABC SHA `0cf2f9bbd6d9e79856109a7a140330c6b2dd4277546c7f9ca1039caa479179cd`; original grade keys G1-ELE-199=A, G2-ELEC-335=A **unchanged**.
- **Question:** Producerea dublei puneri la pământ a bobinajului rotoric al unui generator sincron are ca efect negativ
- **A:** numai creșterea foarte mare a curentului prin circuitul rotoric
- **B:** faptul că tensiunile electromotoare nu mai sunt sinusoidale
- **C:** apar scântei la periile colectorului
- **Each option, model/terminology:** A second rotor field ground can short a segment, and can cause high local current but «numai» rules out other important consequences (rotor field asymmetry, bearing stress, vibration). B non-sinusoidal induced voltage could be a consequence of field distortion in some designs, not universal. C brush arcing is contingent on slip-ring/brush design, not general.
- **Exact-source leads and access:** Hydro-protection university source https://iitr.ac.in/Departments/Hydro%20and%20Renewable%20Energy%20Department/static/Modern_hydroelectric_engg/vol_2/Chapter-3_Electrical_Protection_System.pdf (PDF search excerpt only, NOT visually verified); MDPI paper https://www.mdpi.com/1996-1073/11/10/2524 (SEARCH_EXCERPT ONLY, direct 429); independent HTML/book source https://fliphtml5.com/osspz/bcye/Electrical_Equipment_Handbook_-_Troubleshooting_and_Maintenance/ (INDEXED)
- **Exam intent only:** A «numai curent» disproved by magnetic asymmetry/vibration. **Blocker:** A is demonstrably not exhaustive; B/C lack universally necessary effects. No unique answer asserted and no procedural rotor-ground fault advice.
- `approved_for_learning=NO`, independently audited source/technical/linguistic QA NOT_RUN; official ANRE 2026 grade key/edition not independently verified.

### G1-ELE-214 | CONSERVATOR_MULTIFUNCTION_AND_MODEL
- Existing unit `AU-d8e0bccaca041e45`; original QABC SHA `d8e0bccaca041e45c82149a1f5992cdb3ff04a347c787027cd96cceedf2c4478`; original grade keys G1-ELE-214=A, G2-ELEC-350=A **unchanged**.
- **Question:** Rolul conservatorului de ulei la transformatoarele de forţa este:
- **A:** de a asigura o suprafaţa de contact a uleiului cu aerul mai mica
- **B:** numai  de a asigura spaţiul necesar dilatării si contractării uleiului
- **C:** de a face posibila umplerea cu ulei a transformatorului
- **Each option, model/terminology:** A conservator isolates the main tank oil and confines/reduces its contact with air (direct contact may vanish with bladder), although 'smaller area' depends geometry and design. B the word «numai» excludes moisture/air interface control, despite expansion being major purpose. C it can assist oil filling/monitoring but is not defining design function.
- **Exact-source leads and access:** ABB transformer user manual HTML mirror https://www.manualsnet.com/abb/1zcl000001eg (SEARCH_EXCERPT); transformer components source https://transformergrid.com/technical-library/transformer-conservator-bladder-breather-silica-gel-oil-level-guide/ (HTML_INDEXED); transformer installation https://www.cnrockwill.com/technical/oil-immersed-transformer-installation-operation-manual (HTML_INDEXED)
- **Exam intent only:** A conventional small oil-air interface intended; B «numai» false. **Blocker:** Original A source-compatible only for standard breathing/air-cell configuration. A cannot be unconditionally universal for all sealed bladder designs absent model.
- `approved_for_learning=NO`, independently audited source/technical/linguistic QA NOT_RUN; official ANRE 2026 grade key/edition not independently verified.

### G1-ELE-198 | CREEPAGE_VS_AIR_CLEARANCE_SCOPE_MISMATCH
- Existing unit `AU-735af908a7b436b4`; original QABC SHA `735af908a7b436b4093637f904e71cd240665b9dd61afe43ebb2dc8a105a5a56`; original grade keys G1-ELE-198=B, G2-ELEC-334=B **unchanged**.
- **Question:** Printre măsurile de reducere a distanţelor de izolare pot fi:
- **A:** folosirea dispozitivelor de limitare a curenţilor de scurtcircuit;
- **B:** aplicarea unui strat protector pe izolatoare pentru micşorarea efectelor poluării din marile oraşe sau de pe unele platforme industriale;
- **C:** micşorarea densităţii dielectricilor gazoşi.
- **Each option, model/terminology:** A limiting short-circuit current changes thermal/electrodynamic stress not a dielectric air-gap requirement per se. B surface anti-pollution coating helps leakage/creepage in service, but does not by itself reduce minimum air clearance; only tested system-specific conditions may affect permitted creepage distance. C reducing gas density generally worsens withstand for fixed geometry.
- **Exact-source leads and access:** IEC TS 60815-3:2025 summaries https://www.iteh.eu/catalog/standards/iec/2fedf8cd-a56a-4c91-993d-2411376709e1/iec-ts-60815-3-2025 (INDEX ONLY); conformal PCB coatings https://www.conformalcoating.co.uk/knowledge-hub/technical-articles/conformal-coating-design-hub/conformal-coating-clearance-creepage/ (HTML_DIRECT_OPENED, PCB scope not same as outdoor insulator)
- **Exam intent only:** B coatings improve polluted surface performance but clearance reduction not established. **Blocker:** Original B is plausible pollution-performance strategy, but no exact product/IEC class allowing reduced specified insulating distance. Preserve SOURCE_SCOPE_MISMATCH rather than universal rule.
- `approved_for_learning=NO`, independently audited source/technical/linguistic QA NOT_RUN; official ANRE 2026 grade key/edition not independently verified.

### G1-ELE-210 | GIS_FOOTPRINT_COMPARATIVE_RATING_MISSING
- Existing unit `AU-5263065f82c0ae73`; original QABC SHA `5263065f82c0ae73a6fa5300a5faeec2b703b56e8d915f2e8209d65a7c96b1a8`; original grade keys G1-ELE-210=C, G2-ELEC-346=C **unchanged**.
- **Question:** Spaţiul ocupat de o instalaţie capsulată depinde în principal de:
- **A:** curentul nominal al legăturilor electrice;
- **B:** mediul de stingere a arcului electric;
- **C:** realizarea capsulării: capsulare tripolară sau monopolară.
- **Each option, model/terminology:** A rated current changes busbar/conductor thermal dimension. B interruption medium may influence breaker size, but not every overall GIS design. C mono vs three-pole encapsulation influences phase spacing, enclosure count and station footprint, but «în principal» cannot be proven from non-matched catalogue dimensions.
- **Exact-source leads and access:** Hitachi GIS BLF/PASS single-phase enclosure with rated data https://www.hitachienergy.com/in/en/products-and-solutions/high-voltage-switchgear-and-breakers/gas-insulated-switchgear/gis-for-72-5-1200-kv/gis-blf-pass-up-to-170-kv (HTML_DIRECT_OPENED)
- **Exam intent only:** C mono vs tripolar enclosure footprint intended, main-variable unsupported. **Blocker:** Comparative equal-rating triple and mono pole plans absent; cannot rank variables or approve C universally.
- `approved_for_learning=NO`, independently audited source/technical/linguistic QA NOT_RUN; official ANRE 2026 grade key/edition not independently verified.

### G1-ELE-030 | ALL_DISTRIBUTION_VOLTAGES_UNSUPPORTED
- Existing unit `AU-4dde5fbb638cf178`; original QABC SHA `4dde5fbb638cf17897cf53fcc19686a4840bc1ed1198655d72962c2ba07eca4f`; original grade keys G1-ELE-030=B, G2-ELEC-179=B **unchanged**.
- **Question:** Scheme cu un sistem de bare colectoare şi un întreruptor pe circuit sunt folosite
- **A:** numai pentru staţii de conexiuni de 6 kV
- **B:** pentru toate treptele de tensiune din reţelele de distribuţie
- **C:** numai pentru staţii de conexiuni de medie tensiune până la 6o kV
- **Each option, model/terminology:** A single busbar one breaker scheme is not restricted solely to connection substations at 6kV. B broad use is technically credible but «pentru toate treptele» requires scope of Romanian distribution levels, not a single manufacturer catalogue. C «numai ... până la 60kV» likewise cannot be universal across substation design.
- **Exact-source leads and access:** General substation busbar topology HTML https://eepower.com/technical-articles/substation-componentspart-5-busbar-configurations/ (HTML_DIRECT_OPENED). Multiple utility configurations depend voltage/reliability. No official Romanian 2026 evidence that this design is in use/acceptable at ALL distribution levels.
- **Exam intent only:** B intended breadth of distribution levels, «toate» unverified. **Blocker:** Candidate B only intended in broad textbook model; demand exact exam source before final release.
- `approved_for_learning=NO`, independently audited source/technical/linguistic QA NOT_RUN; official ANRE 2026 grade key/edition not independently verified.

### G1-ELE-053 | OPEN_PHASE_TRANSFORMER_NOT_MOTOR_SINGLE_PHASING
- Existing unit `AU-1a3686e6131c6fe4`; original QABC SHA `1a3686e6131c6fe4b413d125f3e9b91d6539467de2b30a2bebe6547e572d2db9`; original grade keys G1-ELE-053=A, G2-ELEC-199=A **unchanged**.
- **Question:** Funcţionarea în doua faze a unui transformator trifazat are ca efect:
- **A:** supraîncălzirea acestuia
- **B:** suprasarcina
- **C:** reducerea puterii tranzitate
- **Each option, model/terminology:** A an open phase can cause abnormal currents, circulating paths and heating depending winding and load. B remaining components/paths may be overloaded depending system. C lost phase can reduce available transmitted power. All three can hold in some physical configurations, but none is a necessary sole consequence for all 3φ transformer winding/core arrangements.
- **Exact-source leads and access:** Peer-reviewed journal abstract «Alternative approaches and dynamic analysis ... open phase conductors in three phase power systems» https://www.sciencedirect.com/science/article/pii/S0378779618301482 (SEARCH_EXCERPT ONLY direct 403), source explicitly says outcome dependent on winding connections/loading. No motor single-phasing source substitution.
- **Exam intent only:** A overheating possible, B overload/C reduced transferred power may overlap. **Blocker:** No exact transformer connection and loading, no single uniquely correct outcome. Preserve original A until evidence gate and expert signoff.
- `approved_for_learning=NO`, independently audited source/technical/linguistic QA NOT_RUN; official ANRE 2026 grade key/edition not independently verified.

## QA and handoff
- **7 existing unique / 14 grade-ID placements** exactly matched all-822 V73 canonical source for original question/each A,B,C/imported grade key, 0 mismatches. Source ID/hash preserved, not recomputed.
- Scope gates: rotor double ground ≠ 'only high current'; transformer open phase ≠ motor single-phasing; oil conservator volume/air multiple roles; external polluted insulator ≠ PCB conformal dielectric clearance; busbar topology cannot be generalized across all voltages; GIS enclosures must be compared at matching ratings.
- Running session cumulative CKPT182 10 + 183 6 +184 7 +185 6 +186 8 +187 7 = **44 unique EXISTING items rechecked**, not approved nor removed from original 50 blocked official list. NOR066 was separately rechecked in preceding turn CKPT181. No canonical edits, app edits, main, release or merge. PR remains Draft.
- Next: reconcile remaining candidates in original 50 blocked tally and flag any status-card mismatch; do not equate 44 reassessments with 44 independently signed certifications.
