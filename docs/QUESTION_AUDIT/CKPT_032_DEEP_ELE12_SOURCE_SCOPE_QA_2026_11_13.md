# CKPT-032 | DEEP-ELE-12 source-scope triage (20 units/40 IDs) | 2026-11-13

## Guardrails / repository
- Repo `AcoBenny/ANRE_Trainer`, branch `audit/anre-v8-priority-17-20261109`, PR [#7 Draft](https://github.com/AcoBenny/ANRE_Trainer/pull/7), **unmerged** at live GitHub readback.
- Continued from [CKPT-031](./CKPT_031_DEEP_ELE11_PRE_QA_SOURCE_TRIAGE_2026_11_13.md), without duplicating previous batches.
- New [DEEP-ELE-12 preliminary source & ABC register](./DEEP_EXECUTION_2026_11_11/DEEP_ELE_12_ALL_20_SCOPED_SOURCE_ABC_TRIAGE_2026_11_13.csv), commit `5296972c2fc6ad26d78191a86a6fb46c59a48d94`.
- 20 original exact QABC units / 40 per-grade canonical IDs; same QABC, A/B/C order, keys, unit hashes and routing. No changes to application, barem, source bank, HTML, APK or main; no merge/release.
- All row states are `independent_technical_QA=NOT_RUN`, `independent_source_QA=NOT_RUN`, `independent_linguistic_QA=NOT_RUN`, `edition_verified=NO`, `approved_for_learning=NO`.

## Critical research blockers, **NOT** adjudicated errors
1. **G1-ELE-219 / G2-ELEC-355** (three-phase earth short with arc). Canonical A inserts **three times** arc impedance into the positive-sequence network. [EEP 3-phase/earth symmetrical fault](https://electrical-engineering-portal.com/resources/knowledge/fault-calculations) shows positive sequence only for a symmetric solid 3-phase fault; [ScienceDirect components discussion](https://www.sciencedirect.com/topics/engineering/symmetrical-component) references **3 Zf in zero-sequence for single-phase-earth**. This is a serious **source-object/defect-type and topology mismatch risk**, not proof of corrected key. Need authentic Romanian fault-network derivation for exactly *three-phase and earth through arc*, including arc impedances and grounding node. Barem A unchanged.
2. **G1-ELE-221 / G2-ELEC-357**: stem concerns **minimum insulating clearance in AIR**, original A says personnel safety; B refers dielectric insulation/operational reliability. IEC 61936-1 §5.4 distinction between insulating clearances and §7 safety distances indicates possible conflation. Edition and exact Romanian norm/grade not verified, no key change.
3. **G1-ELE-226 / G2-ELEC-362**: Budeanu distortion power `D=sqrt(S²−P²−Q²)` is a nonnegative scalar; its *direction* is not defined merely by the scalar. Original A (generator → saturated iron-core reactor) cannot be certified without the intended power theory and signed harmonic-flow convention. [Overview of classical power definitions](https://www.mdpi.com/1996-1073/14/8/2177), [Budeanu research](https://www.degruyterbrill.com/document/doi/10.1515/ijeeps-2017-0002/pdf) (PDF retrieved as search excerpt only; no visual screenshot performed). `UNDEFINED_DIRECTION` escalation; no proposed key approved.
4. **G1-ELE-216**: voltage-transformer vs current-transformer distinction; [official IEC 61869-3](https://webstore.iec.ch/en/publication/6051) covers VT frequency range and general insulation; [IEC 61869-2 CT definition](https://standards.iteh.ai/catalog/standards/iec/22825143-3f87-4234-a841-e778bd57dbe9/iec-61869-2-2012) includes rated dynamic short-time current for CT. Current original B is a research candidate, not final proof against all VT tests.
5. **G1-ELE-223**: CT **open secondary with energized primary is dangerous**; [Schneider manufacturer's safety notice](https://www.se.com/nz/en/faqs/FA125574/) directly opened. Distinguish energized CT from deenergized handling; no unsafe operational instructions inferred.
6. **G1-ELE-240**: Conservator **with breather/desiccant** can limit but not eliminate moisture; conservator alone does not guarantee dry air. [Hitachi Energy manufacturer explanation](https://www.hitachienergy.com/ca/en/products-and-solutions/insulation-and-components/transformer-insulation-components/measurement-and-safety-devices/dehydrating-breathers/conventional).
7. **G1-ELE-234**: [IEC 61869-3:2011 public extract §5.301.2](https://standards.iteh.ai/catalog/standards/iec/301e2161-babf-44ad-9132-b85514d36f62/iec-61869-3-2011) lists **100V** and 110V European standard alternatives; 100V candidate C is one allowed nominal option, not universal global requirement.
8. **G1-ELE-224/225**: bus sectionalization may improve continuity or limit short-circuit current **conditionally on source topology, isolating coupling and selectivity**; circuit diagram lacking.
9. **G1-ELE-232**: symmetrical components are mathematically constructed sets ([Phase to Phase ch7.5](https://www.phasetophase.nl/book/book_2_7.html)); negative/zero components still have physical observable effects. Original B is preliminary interpretation, not a claim that effects are fictitious.
10. Remaining ELE12 records each include independent ABC explanations, source/access provenance and explicit caveats in CSV. No answer certified.

## Actually executed QA
- Refetched CSV after commit; compared **all 20/20 original QABC units, 40/40 canonical ID placements** against GitHub `V73_ALL_822_EVIDENCE_AND_RELEASE_GATES_MASTER.csv`, `UNITS_568.csv`, `ID_ROUTING_822.csv`. Validated original stem and options, original key, SHA, ID membership, exact batch routing, 3 option explanations, source/limitation fields and all non-approval flags. **0 deterministic integrity errors**.
- Ran **JavaScript translation of Python `source_scope_gate.py` six bundled synthetic regression fixtures** (NOR032 negative+positive, NOR027 grade/terminology, NOR029 context, edition unknown): **6/6 PASS**. This was *not* execution of original Python CLI, nor verification of physical truth; it does not validate this batch's answers.
- Independent second AI reviewer, external expert, source original for every item, 2026 ANRE exam bibliographic applicability, and offline app QA: **NOT_RUN**. For PDFs mentioned via search only, visual screenshot verification **NOT_RUN**; no restricted standard redistributed.

## Cumulative and handoff
| Metric | State |
|---|---:|
| Complete **PRELIMINARY** source/ABC triage batches | **24/30** |
| Distinct exact QABC units with preliminary triage | **467/568** |
| Canonical grade-specific ID placements with preliminary triage | **692/822** |
| Batches remaining preliminary | **6** |
| Units / placements remaining preliminary | **101 / 130** |
| Independently approved for learning | **0/822** |

Next NEW batch `DEEP-ELE-13`, followed by ELE14–18; do not repeat prior triage. Parallel separate mandatory phase: source editions and current ANRE bibliography, object-specific primary paragraphs, independent AI/human scrutiny, linguistic key adjudication and aggregate 822 QA. User can supply semantic `USER_HYPOTHESIS` if genuinely needed. No background worker launched. PR remains Draft; no canonical or app edits without explicit consent.
