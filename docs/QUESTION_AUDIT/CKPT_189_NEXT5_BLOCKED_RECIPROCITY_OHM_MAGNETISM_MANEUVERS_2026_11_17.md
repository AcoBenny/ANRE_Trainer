# CKPT-189 | Five still-blocked CKPT138 questions: passive reciprocity, Ohm nonlinearity, magnetic matter, two HV maneuver sequences | 2026-11-17

Non-destructive recheck of **five existing units** (ten grade-ID placements). This is **not new question research credit** and not permission to change original keys or operate electrical equipment. Original CKPT138 preserved, no official 2026 ANRE answer-key proof or independent expert review.

## Original QABC with negative and intended models

### G1-ELE-051 | PASSIVITY_NOT_SUFFICIENT_FOR_RECIPROCITY
- Unit ID `AU-21064933b66a7f13` original SHA `21064933b66a7f132dec38688307460deaf86c7f3aec7502c8efcb1899a13273`; unchanged grade keys G1-ELE-051=B, G2-ELEC-197=B.
- **Original question:** Dacă o tensiune electromotoare E, montată în latura AB a unei reţele pasive, produce în latura CD a reţelei un curent I, montarea t.e.m. E în latura CD va produce în latura AB:
- **A:** un curent - (minus) I
- **B:** un curent I
- **C:** un curent I/2
- **A/B/C analysis and counterexample:** A sign reversal possible in nonreciprocal passive networks with gyrator and oriented references, not universally. B the intended reciprocity theorem requires a linear bilateral reciprocal network and defined current reference directions, which word «pasive» alone does not guarantee. C half-current not generally implied.
- **Source and access mode:** Oregon State University ECE580 notes including gyrator https://classes.engr.oregonstate.edu/eecs/fall2023/ece580/Lecture%20Notes/PrintableLectureNotes.pdf (INDEXED_PDF_NO_VISUAL_CONFIRMATION); University of Illinois passive gyrator anti-reciprocal transmission model https://jontallen.ece.illinois.edu/uploads/403-source-S17/LabManual/LabManual.pdf (INDEXED_PDF_NOT_VISUALLY_CHECKED)
- **Provisional intended interpretation:** B only in reciprocal networks with compatible reference orientations. **Blocker:** Do not infer all passive devices reciprocal. Ordinary linear RLC bilateral network may have intended B, but counterexample exists outside implicit model.
- `approved_for_learning=NO`, independent technical/linguistic/source QA NOT_RUN, 2026 exam official key NOT_VERIFIED.

### G1-ELE-141 | OHM_NONOHMIC_COUNTEREXAMPLE
- Unit ID `AU-7f920d09fda666bc` original SHA `7f920d09fda666bc9970583b31f677dd4a4c7b84d5df03c79004d20000da5395`; unchanged grade keys G1-ELE-141=C, G2-ELEC-279=C.
- **Original question:** Legea lui Ohm pentru o porţiune de circuit este valabila:
- **A:** doar în curent continuu
- **B:** doar în curent alternativ
- **C:** indiferent de natura circuitului
- **A/B/C analysis and counterexample:** A DC-only excludes an ohmic AC resistor, false. B AC-only excludes DC ohmic resistor, false. C if applies 'indiferent de natura circuitului' to arbitrary nonlinear circuit, diode I-V relation violates constant-R Ohm law; within ohmic linear components regardless excitation DC/AC, intended C.
- **Source and access mode:** OpenStax University Physics 2 §9.4 https://openstax.org/books/university-physics-volume-2/pages/9-4-ohms-law (SEARCH_CONFIRMED_OPEN_ACCESS, direct source text includes nonohmic diode)
- **Provisional intended interpretation:** C only if «natura circuitului» means DC versus AC within ohmic model. **Blocker:** The word «natura» ambiguously refers to excitation AC/DC versus material linearity; official syllabus definition of target law needed.
- `approved_for_learning=NO`, independent technical/linguistic/source QA NOT_RUN, 2026 exam official key NOT_VERIFIED.

### G1-ELE-172 | GENERIC_MAGNETIC_SCOPE_FALSE_UNIVERSAL
- Unit ID `AU-5cba109346b5399e` original SHA `5cba109346b5399eafa4933fe29da4311a0f0f4e643936a2d8a0d6bc8d826e68`; unchanged grade keys G1-ELE-172=C, G2-ELEC-309=C.
- **Original question:** Pentru materialele magnetice, relaţia dintre inducţia magnetică şi intensitatea câmpului magnetic:
- **A:** este liniară
- **B:** este o egalitate
- **C:** este neliniară
- **A/B/C analysis and counterexample:** A linear relation B≈μH fits dia-/paramagnetic weak-field regimes. B equality of B and H is dimensionally incorrect in SI (T vs A/m). C nonlinear/hysteretic B(H) fits ferromagnets, not every magnetic material. Stem says all «materiale magnetice» without category qualification.
- **Source and access mode:** OpenStax University Physics 2 §12.7 https://openstax.org/books/university-physics-volume-2/pages/12-7-magnetism-in-matter (SEARCH_CONFIRMED_OPEN_ACCESS, dia/para/ferro contrasted)
- **Provisional intended interpretation:** C for ferromagnetic nonlinear B(H), A for linear dia/paramagnets. **Blocker:** Intended C depends on restricting material to ferromagnet; absent in original statement. Keep unresolved until official educational definition.
- `approved_for_learning=NO`, independent technical/linguistic/source QA NOT_RUN, 2026 exam official key NOT_VERIFIED.

### G1-ELE-129 | SITE_SPECIFIC_SWITCHING_ORDER_NOT_DEDUCIBLE
- Unit ID `AU-2835f4d5d0cd454f` original SHA `2835f4d5d0cd454f0e6ed2b1cfc4dddc4daeee5fda0065df9b085dd04a1049e1`; unchanged grade keys G1-ELE-129=C, G2-ELEC-269=C.
- **Original question:** La conectarea unui circuit de linie se recomandă următoarea  ordine a manevrelor:
- **A:** separatorul de linie, separatorul de bare, întreruptorul;
- **B:** separatorul de bare, întreruptorul, separatorul de linie;
- **C:** separatorul de bare, separatorul de linie, întreruptorul .
- **A/B/C analysis and counterexample:** A line-side isolator then bus-side isolator then breaker, but actual sequence/allowed isolator energization depends exact topology, previous condition and interlocks. B breaker closed before last isolator can violate ordinary off-load duty. C bus-side then line-side isolator, breaker last is intended didactic sequence in a standard deenergized bay. Without diagram, A and C are not exhaustively disambiguated.
- **Source and access mode:** Official Romanian NTE 009/10/00 maneuvers https://legislatie.just.ro/Public/DetaliiDocument/122751 (SEARCH_OPENED_OFFICIAL_REGULATION; site-specific equipment, operative conditions govern).
- **Provisional intended interpretation:** C theoretical exam sequence conditional, A also ends breaker last. **Blocker:** This QABC is ONLY academic exam discussion; not an authorized HV switching instruction. Neither operating state nor isolator duties specified.
- `approved_for_learning=NO`, independent technical/linguistic/source QA NOT_RUN, 2026 exam official key NOT_VERIFIED.

### G1-ELE-131 | SITE_SPECIFIC_DEENERGIZATION_SEQUENCE
- Unit ID `AU-4e84ba50de6e8429` original SHA `4e84ba50de6e8429d7f3082c27525620b95770336f1869dd7bf0b1f8548443cc`; unchanged grade keys G1-ELE-131=C, G2-ELEC-271=C.
- **Original question:** La deconectarea unui circuit de linie se recomandă următoarea  ordine a manevrelor:
- **A:** separatorul de linie, întreruptorul, separatorul de bare;
- **B:** separatorul de bare, întreruptorul, separatorul de linie;
- **C:** întreruptorul, separatorul de  linie, separatorul de bare.
- **A/B/C analysis and counterexample:** A opens line isolator before breaker, unacceptable for ordinary isolator switching load. B bus isolator before breaker, similarly conflicts with ordinary duty. C breaker before the two isolators is conventional core pattern, but line-versus-bus order after interruption may depend actual network and control procedure.
- **Source and access mode:** Official Romanian NTE 009/10/00 https://legislatie.just.ro/Public/DetaliiDocument/122751; station maneuver plan required, not supplied by question or source.
- **Provisional intended interpretation:** C conventional exam sequence breaker first, A/B generally hazard under load. **Blocker:** C as theoretical intent; do not apply in the field or learner-certified key without equipment states, official study source and expert QA.
- `approved_for_learning=NO`, independent technical/linguistic/source QA NOT_RUN, 2026 exam official key NOT_VERIFIED.

## QA, safety and handoff
- Strict canonical V73 equality: **5/5 existing units and 10/10 grade IDs** matching question, options and per-grade original answer key. No canonical original modifications, no SHA recomputation or claim to have certified the complete legal edition.
- Reciprocity requires more than passivity; Ohm depends on what «natura» includes; generic magnetic material is not automatically nonlinear; HV switching choices are schematic/conditions dependent. Keep this nuance rather than record independent final key approval.
- Prior CKPT188 superseding course analysis preserved. No grade changes, main, HTML, APK, merge or release. PR #7 Draft. Independent technical+source+linguistic review still necessary before any learner approval.
