# CKPT-186 | 8 blocked source cases: skin effect, 3 bus-coupler, 2 switching, H inferior/superior source rescue | 2026-11-17

Continuity: 568 unique units already inventoried; 8 existing flagged units, **no new credit**. All original keys/QABC retained. Sources are linked with actual access modes, no external switching sequence is operational advice. User-approved immutable boundaries: no application, keys, HTML, APK, main or merge. An independent expert model/human review was **NOT_RUN**.

## Important new source recovery
**G1-ELE-167** and **G1-ELE-168** are now matched by *two Romanian descriptions* of the exact H bridge topology: H inferior (punte spre transformator) for more frequent line operations, H superior (punte spre linie) for more frequent transformer operations. The second 2015-course PDF was text-retrieved, but the PDF screenshot request FAILED, so do not represent visual schematic authentication. Older CKPT153 'not located exact source' is preserved as superseded history, original answer keys untouched.

## Eight original option checks

### G1-ELE-061 | SKIN_EFFECT_A_VS_B_MODEL
- Original unit `AU-8b49c420c2cfe045`, QABC hash `8b49c420c2cfe045195bf16be9f6d9e0171f09908e24a7be4f8c3146d688ec4d`, per-grade unchanged keys: G1-ELE-061=A, G2-ELEC-206=A.
- **Question:** Efectul pelicular al unui curent alternativ care străbate un conductor masiv se datorează:
- **A:** unor curenţi paraziţi induşi în conductor, simetrici faţă de axa acestuia
- **B:** numai unor forţe electromotoare induse datorită variaţiei curentului
- **C:** capacităţii conductorului faţă de pământ
- **ABC and model:** A eddy-current picture is compatible with AC skin effect; however symmetry axis of the particular currents and field needs definition and geometry. B changing-current induced EMF is essential but «numai» oversimplifies electromagnetic current redistribution. C earth capacitance is not cause of skin effect.
- **Sources and access:** IEEE Technology Navigator Skin effect https://technav.ieee.org/topic/skin-effect/ and https://technav.ieee.org/topic/proximity-effect/ (INDEXED_SUMMARIES)
- **Technical intended status:** A compatible with self-induced eddy current explanation. **Gate:** Textbook derives skin-depth from magnetic self-field, requires same physical conditions to rule out B outright; no certified exclusive choice.
- `approved_for_learning=NO`, independent technical/source/linguistic QA NOT_RUN, official ANRE 2026 key/edition NOT_VERIFIED.

### G1-ELE-124 | TIE_COUPLER_EXACT_TOPOLOGY
- Original unit `AU-9ad47849152dd1ab`, QABC hash `9ad47849152dd1ab6b37eee33a7ad703861d878a1209963d357c4538c968b515`, per-grade unchanged keys: G1-ELE-124=A, G2-ELEC-266=A.
- **Question:** Într-o staţie cu două sisteme de bare colectoare, cupla transversală:
- **A:** se poate utiliza numai pentru cuplarea în paralel a celor două sisteme de bare colectoare care sunt sub tensiune;
- **B:** nu se poate utiliza pentru ocolirea unui întreruptor de linie pe durata unei revizii sau reparaţii;
- **C:** se poate utiliza pentru verificarea stării izolaţiei unui sistem de bare colectoare, care până în momentul respectiv a fost scos de sub tensiune.
- **ABC and model:** A ties/parallelizes live busbars under proper synchronism/interlocks, but «numai» excludes other functions. B claims no line-breaker bypass, which is true for ordinary 2-main-bus without transfer path yet false for designed main+transfer or bypass arrangement. C energizing a previously isolated busbar for testing may be possible through coupler with approved test and protection program.
- **Sources and access:** EEPower double-bus main+transfer busbar family https://eepower.com/technical-articles/substation-componentspart-5-busbar-configurations/ (HTML_DIRECT_OPENED); ABB double-bus+transfer https://www.manualslib.com/manual/3220821/Abb-Relion-670-Series.html?page=136 (SEARCH_INDEX_ONLY)
- **Technical intended status:** A original «numai» conflicts with additional uses; C possible under topology. **Gate:** No exact single-line diagram for original ANRE stem; never conflate regular transverse coupler with bypass/transfer coupler.
- `approved_for_learning=NO`, independent technical/source/linguistic QA NOT_RUN, official ANRE 2026 key/edition NOT_VERIFIED.

### G1-ELE-125 | COUPLER_BYPASS_SCHEMATIC_REQUIRED
- Original unit `AU-9688f38d9257eb2b`, QABC hash `9688f38d9257eb2b1a9ce8194ceb27480138dd617f37e83957407afa230657ca`, per-grade unchanged keys: G1-ELE-125=B.
- **Question:** Într-o staţie cu două sisteme de bare colectoare, cupla transversală:
- **A:** nu se poate utiliza pentru cuplarea în paralel a celor două sisteme de bare colectoare care sunt sub tensiune;
- **B:** se poate utiliza pentru ocolirea unui întreruptor de linie pe durata unei revizii sau reparaţii;
- **C:** se poate utiliza numai pentru verificarea stării izolaţiei unui sistem de bare colectoare, care până în momentul respectiv a fost scos de sub tensiune.
- **ABC and model:** A categorical ban on tying energized buses contradicts coupler use when allowed and synchronized. B bypassing a line breaker during maintenance requires transfer bus or bypass separator and compatible protection; not assumed in all 2-bus schemes. C «numai» for insulation testing excludes parallel tie or transfer roles.
- **Sources and access:** EEPower main+transfer vs double-bus family https://eepower.com/technical-articles/substation-componentspart-5-busbar-configurations/ (HTML_DIRECT_OPENED); generic 2-bus images not exam schematic
- **Technical intended status:** B may be possible with transfer path; not universal for all double-bus. **Gate:** C key cannot be substituted, original B is conditional on exact topology. Keep blocked even if distractors obvious.
- `approved_for_learning=NO`, independent technical/source/linguistic QA NOT_RUN, official ANRE 2026 key/edition NOT_VERIFIED.

### G1-ELE-126 | PARALLELING_AND_BYPASS_OPTION_OVERLAP
- Original unit `AU-c9c9ff229afe157a`, QABC hash `c9c9ff229afe157a2f55a7e5f8e62db4c5c5df4bdc0e92aa4bee4d5747850796`, per-grade unchanged keys: G1-ELE-126=A.
- **Question:** Într-o staţie cu două sisteme de bare colectoare, cupla transversală:
- **A:** se poate utiliza pentru cuplarea în paralel a celor două sisteme de bare colectoare care sunt sub tensiune;
- **B:** nu se poate utiliza pentru ocolirea unui întreruptor de linie pe durata unei revizii sau reparaţii;
- **C:** nu se poate utiliza pentru verificarea stării izolaţiei unui sistem de bare colectoare, care până în momentul respectiv a fost scos de sub tensiune.
- **ABC and model:** A a bus coupler can tie buses in parallel subject to synchronism/protection. B 'cannot bypass line breaker' can also be true for ordinary double main bus without transfer path, not necessarily for transfer bus configuration. C no inspection/re-energization cannot be asserted universally without operator procedure.
- **Sources and access:** EEPower double busbar topology https://eepower.com/technical-articles/substation-componentspart-5-busbar-configurations/ (HTML_DIRECT_OPENED)
- **Technical intended status:** A plausible but B also true in ordinary non-bypass scheme. **Gate:** Potential multiple-true A/B in ordinary non-bypass layout. Need exact topology diagram, cross-grade key proof and separate review.
- `approved_for_learning=NO`, independent technical/source/linguistic QA NOT_RUN, official ANRE 2026 key/edition NOT_VERIFIED.

### G1-ELE-137 | OPERATING_SEQUENCES_NOT_A_GENERAL_RECIPE
- Original unit `AU-2aaa2d87c22ca0ab`, QABC hash `2aaa2d87c22ca0ab5e185befcaf940a37dd0197ada56c0b9b8e714c6d8ca7c1b`, per-grade unchanged keys: G1-ELE-137=B.
- **Question:** La conectarea unui circuit de linie se recomandă următoarea  ordine a manevrelor:
- **A:** separatorul de bare, întreruptorul, separatorul de linie;
- **B:** separatorul de bare, separatorul de linie, întreruptorul;
- **C:** întreruptorul, separatorul de linie, separatorul de bare.
- **ABC and model:** A circuit breaker before final line disconnector may leave isolator to operate in load current conditions. B disconnectors before breaker is a possible normalized theoretical sequence *only when appropriate de-energization and interlocking conditions hold*. C energizing breaker before configuring isolators is not acceptable as blanket sequence.
- **Sources and access:** Schneider separation of isolation and switching functions https://www.se.com/ae/en/faqs/FA381456/ (HTML_DIRECT_OPENED; LV model not exactly HV operator manual)
- **Technical intended status:** B is typical theoretical intent under circuit offline state. **Gate:** An actual maneuver requires station-specific authorized switching program and proof of zero current for disconnector operations. Report theoretical exam key only; not field instructions.
- `approved_for_learning=NO`, independent technical/source/linguistic QA NOT_RUN, official ANRE 2026 key/edition NOT_VERIFIED.

### G1-ELE-138 | DISCONNECTOR_ORDER_DEPENDS_ON_BAY
- Original unit `AU-dd065a31756323cf`, QABC hash `dd065a31756323cf48efe1c6c99c80506d0b5f71ed5b1a1cc9a6cb921158dc00`, per-grade unchanged keys: G1-ELE-138=B.
- **Question:** La deconectarea unui circuit de linie se recomandă următoarea  ordine a manevrelor:
- **A:** separatorul de linie, întreruptorul, separatorul de bare;
- **B:** întreruptorul, separatorul de linie, separatorul de bare;
- **C:** întreruptorul, separatorul de bare, separatorul de linie.
- **ABC and model:** A opening line disconnector before load-interrupting breaker is unsafe for an ordinary off-load isolator. B breaker before line-side and bus-side disconnectors is theoretically correct pattern in a typical scheme. C breaker before bus and line disconnectors likewise starts by removing load but remaining sequence could depend on the local station/interlocks.
- **Sources and access:** Schneider device isolation versus breaker https://www.se.com/ae/en/faqs/FA381456/ (HTML_DIRECT_OPENED, generic function only)
- **Technical intended status:** B intended; B/C ordering of post-breaker isolators depends station plan. **Gate:** B/C cannot be distinguished as universal from the vague stem alone. Not advice for operating high-voltage equipment.
- `approved_for_learning=NO`, independent technical/source/linguistic QA NOT_RUN, official ANRE 2026 key/edition NOT_VERIFIED.

### G1-ELE-167 | H_INFERIOR_EXACT_SCHEME_VERIFIED_TEXT
- Original unit `AU-b157329216a487e9`, QABC hash `b157329216a487e9fbcd346a89f15d2f9f6aede38636269735352a288244a52f`, per-grade unchanged keys: G1-ELE-167=A, G2-ELEC-305=A.
- **Question:** O schemă cu două blocuri linie-transformator cu punte între ele de tip ,, H " inferior este de preferat unei scheme de tip ,, H " superior atunci când:
- **A:** se fac manevre dese cu circuitele de linie;
- **B:** se fac manevre dese cu circuitele de transformator;
- **C:** pe legătura dintre blocuri circulă un curent mic.
- **ABC and model:** A more frequent line operations favor H inferior (bridge toward transformers), with branch breaker placement optimizing line maneuvers. B more frequent transformer maneuvers favor H superior, not this variant. C low interbridge current not the compared switching-frequency criterion in the teaching source.
- **Sources and access:** Romanian stations course HTML §3.2.3.10 https://www.scrigroup.com/tehnologie/electronica-electricitate/Statii-Si-Posturi-De-Tansforma34188.php (HTML_DIRECT_OPENED); Romanian 2015 course §5.2.5.1.2 and Fig6.17 https://stoianconstantin.wordpress.com/wp-content/uploads/2024/11/1.e-ip-71-2015-statii-de-conexiuni-si-de-transformare.pdf (PDF_TEXT_RETRIEVED; screenshot failed cache miss, therefore diagram visually NOT_VERIFIED).
- **Technical intended status:** A expressly source-supported for H inferior. **Gate:** Unambiguously matches course context of H inferior/line maneuvers, original key A can now be marked SOURCE_SUPPORTED_FOR_INTENDED_MODEL, NOT learner approval. Must still verify ANRE 2026 bibliography/official key and independent QA.
- `approved_for_learning=NO`, independent technical/source/linguistic QA NOT_RUN, official ANRE 2026 key/edition NOT_VERIFIED.

### G1-ELE-168 | H_SUPERIOR_EXACT_SCHEME_VERIFIED_TEXT
- Original unit `AU-914d53da0bed681e`, QABC hash `914d53da0bed681e565f24c7c840cdfa527ac1864eff3f0c488c4fc01fac2c81`, per-grade unchanged keys: G1-ELE-168=B, G2-ELEC-306=B.
- **Question:** O schemă cu două blocuri linie-transformator cu punte între ele de tip ,, H " superior este de preferat unei scheme de tip ,, H " inferior atunci când:
- **A:** se fac manevre dese cu circuitele de linie;
- **B:** se fac manevre dese cu circuitele de transformator;
- **C:** pe legătura dintre blocuri circulă un curent mic.
- **ABC and model:** A frequent line operations instead favor H inferior; B frequent transformer maneuvers are the explicit intended H superior use. C low bridge current not the switching-frequency criterion.
- **Sources and access:** Romanian stations course HTML §3.2.3.10 https://www.scrigroup.com/tehnologie/electronica-electricitate/Statii-Si-Posturi-De-Tansforma34188.php (HTML_DIRECT_OPENED); 2015 course §5.2.5.1.2 Fig6.17 https://stoianconstantin.wordpress.com/wp-content/uploads/2024/11/1.e-ip-71-2015-statii-de-conexiuni-si-de-transformare.pdf (PDF_TEXT_ONLY; screenshot failed cache miss)
- **Technical intended status:** B expressly source-supported for H superior. **Gate:** Same exact H topology/source-object for intended key B. This is a source-rescue of previous CKPT153 source absence, not a new unit or final release.
- `approved_for_learning=NO`, independent technical/source/linguistic QA NOT_RUN, official ANRE 2026 key/edition NOT_VERIFIED.

## QA and handoff
- Exact readback against 822 V73 IDs, including text, every A/B/C and original key: **8/8 existing unique units and 12/12 grade-ID placements PASS**, 0 differences. QABC hashes/IDs preserved from CKPT142/145/148/153 (not cryptographically recalculated).
- Total additive source/context rereviews this session: CKPT182 10 + CKPT183 6 + CKPT184 7 + CKPT185 6 + CKPT186 8 = **37 pre-existing unique units**, not 37 learner approvals. CKPT181 separately from earlier turn.
- H source rescue affects two cases, not a universal approval. All release gates remain NO. No source gate/linguistic check was an independent reviewer; PR #7 Draft, no merge/release.
- Remaining must be reconciled from existing 50 blocked inventory and 45 legacy-only cases, without treating 37 rechecks as 37 closed approvals.
