# CKPT-017 | Avengers v0.4.2 source-scope enforcement + DEEP-ELE-02 source triage | 2026-11-11

**Repository:** `AcoBenny/ANRE_Trainer`; **PR #7 Draft**; branch `audit/anre-v8-priority-17-20261109`. Continues CKPT016 and preserves older V8–V99 plus CKPT011 exact routing. **Documentary research only, not answer approval or a closed batch.**

## Actual change to Avengers tooling
- Owned PRIVATE Avengers Asamble plugin `plugins_6aeee75a94cc819195c0aeb3a9649391` was **really updated** from v0.4.1 to **v0.4.2**, release `pluginrel_6af4563244c48191a027f863627fdb9c`. New rule in four installed skills verifies exact equipment/legal object, action, rule type, constraints, source edition and ANRE grade bibliography **before accepting a clause as proof**. Plugin code: `skills/anre-source-audit/scripts/source_scope_gate.py`; fixtures `skills/anre-source-audit/tests/source_scope_cases.json`; six deterministic negative/positive cases actually PASSed.
- NOR032 regression: I7 generic §5.2.12.3.10 (tube pulling boxes25m) **must not** override PE155/1992 specific §3.2.10 (horizontal service-line columns, crossing box after15m). The verified fixture rejects wrong-object mapping; correct PE155 scope yields **research preflight only, not answer approval**.
- New check has **declaration-level limitation**: a false input label can fool preflight; reviewer must reopen real primary source and compare what it governs. This is process training, not model-weight retraining or real independent agent execution.

## DEEP-ELE-02 continued, actual data
- Produced `DEEP_EXECUTION_2026_11_11/DEEP_ELE_02_ALL_20_PRE_REVIEW_SOURCE_ABC_TRIAGE.csv` with **20/20 P0 units covering36 canonical IDs**. Each record preserves per-grade keys, exact Q/A/B/C, unit ID/SHA, source locator, all three option rationales, candidate NOT approved, conditions and next gate.
- Earlier `DEEP-ELE-01` is **20 P0 units covering39 IDs**, already in CKPT016. Total four first-priority batch researches: NOR01(20 units/20 IDs), LEG01(20/20), ELE01(20/39), ELE02(20/36) = **80 units /115 canonical ID placements**, **0 validated batches**. These cover the preplanned 66 priority-P0 units and72 P0 IDs in those initial manifests; do not confuse research with an accepted answer verdict.
- High-risk ELE02 examples:
  - `G1-ELE-222/G2-ELEC-358`: for general sinusoidal impedance `Z=R+jX`, susceptance `B=-X/(R²+X²)`; cannot categorically call it `1/X` absent pure-reactive and sign conventions.
  - `G1-ELE-245/G2-ELEC-381`: PF=1 may arise in RLC resonance, not only a physically purely resistive circuit.
  - `G2-ELEC-290`: complex line propagation constant `γ` has units inverse-length; `γ×length` is dimensionless. Original question confuses the two.
  - `G1-ELE-199/G2-ELEC-335`: double rotor-winding ground fault consequences require exact technical document, not generic manufacturer root URL.
  - `G1-ELE-155/G2-ELEC-293`: deep-bar vs double-cage starting current and torque need source specifically comparing motor rotors.

## **New QA correction: enforce source specificity on the two ELE files**
After drafting the preliminary technical cards, checked each source against the **actual claimed physical object**. **Eight** too-generic references were demoted to `BLOCKED_SOURCE_SCOPE_*` and exact missing locator set to `NOT_LOCATED_EXACT_SOURCE`, not treated as technical proof:
- ELE01: `G1-ELE-020` gas leakage monitoring vs monopolar encapsulation, `G1-ELE-109` generic present-value explanation vs specific PIF/fund actualizare, `G1-ELE-122` generic electrical protection vs busbar disconnector operations.
- ELE02: `G1-ELE-155` generic induction motor vs deep-bar/double-cage torque, `G1-ELE-160` induction vs synchronous motors, `G1-ELE-180` generic inductance vs laminated silicon-steel core, `G1-ELE-199` manufacturer manuals homepage vs rotor double earth fault, `G1-ELE-220` transformer circuit protection vs instrument transformers.
- `G1-ELE-249` circuit breaker source preserved but explicitly marked `SOURCE_SCOPE_PARTIAL_BREAKER_NOT_DRAWOUT_DESIGN`, since a generic circuit breaker standard does not prove what withdrawable construction itself guarantees. **Total 9 source-scope corrections** (8 fully blocked, 1 downgraded partial). No canonical answer altered.

## Actually executed QA, after last GitHub writes
1. Reopened the **updated** ELE01/ELE02 CSVs via GitHub plus immutable V73/UNITS568 manifests.
2. Parsed quoted CSV structure; validated 20+20 unique units, 39+36 canonical ID mappings, SHA/routing, per-ID original question and all ABC/key exactly equal, `independent_review=NOT_RUN`, `approved_for_learning=NO`, `key_change_authorized=NO` for all records.
3. Checked all `NOT_LOCATED_EXACT_SOURCE` have `BLOCKED_SOURCE_SCOPE` classification; all 8 blockers preserved. **PASS 40 units/75 IDs, 0 mismatches**. Previous temporary QA parser false failure was diagnosed, corrected and rerun PASS; no CSV repair was needed.
4. PR still Draft, unmerged; canonical HTML blob SHA remains `bc5b5a61954ba138cf83987bfc932eca517f3b21` unchanged.
5. **Not run:** qualified expert/electrical review, independent AI agent source reopening, full batch JSON `deep_audit_execution.py validate` (cannot honestly pass final gates), APK/runtime QA. Source and reasoning statuses remain preliminary.

## Next handoff / no false close
- Real independent source+technical+linguistic review is needed, specifically for **NOR032, NOR027, ELE029, ELE104, ELE128, ELE222, ELE245, ELE290** and all other opened units, before constructing complete batch JSONs. Reviewer must verify exact edition and object, ABC, conditions and ambiguities.
- Find actual exact missing sources for the 8 blocked items; do not fake a locator or accept generic document/page as substitute.
- Continue source/ABC triage for next risk-ranked lots `DEEP-ELE-03`, `DEEP-NOR-02`, `DEEP-LEG-02` once required reviewer/source QA is routed appropriately. All 30 batches remain **not closed**; **0/822 approved for learning**.
- Never edit original keys, A/B/C, canonical bank, HTML, APK, nor merge or release without user approval. Preserve cumulative evidence and previous wrong-source analysis as negative regression fixtures.
