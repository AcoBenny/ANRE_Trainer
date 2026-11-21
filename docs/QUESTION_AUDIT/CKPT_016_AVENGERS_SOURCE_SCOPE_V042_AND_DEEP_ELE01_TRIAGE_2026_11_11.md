# CKPT-016 | Avengers source-specificity fix v0.4.2 + DEEP-ELE-01 | 2026-11-11

**Repository:** AcoBenny/ANRE_Trainer, **PR #7 Draft**, branch `audit/anre-v8-priority-17-20261109`, continuation from CKPT015. Existing canonical bank of 822 and all historical audit work remain intact. No HTML/APK/key/ABC edits, no merge or release.

## 1. Avengers source-routing mistake corrected in the owned plugin (REAL UPDATE)
- The **owned private installed plugin** `avengers-asamble` (`plugins_6aeee75a94cc819195c0aeb3a9649391`) was modified through Plugin Creator from version **0.4.1 → 0.4.2**, release **`pluginrel_6af4563244c48191a027f863627fdb9c`**, and then the new release/files verified.
- Updated the actual installed skill documents `anre-source-audit`, `anre-question-bank-qa`, `qa-evidence-gate`, and `agent-router`. The rule now compares **exact physical/legal object, activity, operation, conditional case, exam-grade bibliography and edition** before mapping a source paragraph to an answer; no generic topical document may override a more specific applicable provision by keyword proximity alone.
- A new executable plugin script `skills/anre-source-audit/scripts/source_scope_gate.py` plus `tests/source_scope_cases.json` are included in the updated release. **6/6 deterministic fixture tests passed** in a real Python environment: NOR032 generic I7 mismatch (must block), NOR032 exact-scope PE155 source match (research-only), NOR027 PE102 grade-I exclusion, NOR027 contact naming equivalence, NOR029 unique maximum wording, and missing source/exam edition. Compilation succeeded.
- **Limitation honestly tested:** if someone intentionally falsifies the declarative source-object/rule tags, the structural preflight may pass despite the wrong real-world source. A separate reviewer must reopen the document, verify the true text and scope, and may block; `SCOPE_PREFLIGHT_PASS_NOT_ANSWER_APPROVAL` is never source truth, exam correctness or authorized learning.
- No model weights retrained; this is a **plugin workflow, skill and regression suite update**, not independently spawned agents or an exhaustive model benchmark.
- Plugin link: https://chatgpt.com/plugins/plugins_6aeee75a94cc819195c0aeb3a9649391

## 2. DEEP-ELE-01 research continued and saved
- **20/20 exact P0 source/ABC units**, mapped to **39 canonical IDs** (Grade I/II duplicates), have complete **pre-independent-review** technical/semantic/source triage; each contains exact original Q/A/B/C, preserved per-ID key and QABC SHA, candidate and classification, source citation, reason for every choice, physical scope and next gate.
- Source research used currently retrieved DOE, OpenStax, Schneider Electrical Installation Guide, IEEE, ABB, LibreTexts and previous V80–V99 / CKPT012 evidence. It did **not** claim a complete independent verification of every source. PDF/image verification remains separate where required.
- High-risk findings:
  - **G1-ELE-018/G2-ELEC-170:** identical QABC with conflicting keys A/C. Symmetrical interphase delta capacitance transforms to 3C per star arm, favoring A under the service-capacitance definition; specific Romanian `Cs` definition pending.
  - **G1-ELE-102/G2-ELEC-245:** second same-QABC conflict A/C; double-bus normal operation depends on actual scheme/operating instructions, no universal letter approved.
  - **G1-ELE-029/G2-ELEC-178:** "alternating current can arise ONLY via electromagnetic induction" has inverter counterexample (DOE). Original option C NOT universally correct; no clear option without scope revision.
  - **G1-ELE-073/G2-ELEC-218:** electric field E flux `q/epsilon0` vs electric displacement D flux `q`; original key B only under D convention. Do not use E Gauss law as direct proof of q.
  - **G1-ELE-104/G2-ELEC-247:** oil both electrically insulates and can quench arc (oil-breaker-specific), so A "doar izolare" is overly strong, B valid for oil breakers, not all electrical equipment.
  - **G1-ELE-128/G2-ELEC-268:** 90° voltage lead only for an **ideal pure inductor**, while generic "caracter inductiv" with resistance gives phase strictly between 0° and90°, so no universal offered angle.
  - **G1-ELE-043/G2-ELEC-189:** proportionality of generator current to voltage is regime-dependent, not universal. `S=sqrt3 U I` for 3phase implies inverse I(U) at fixed S.
  - **G1-ELE-049/G2-ELEC-195:** same-direction proximity concentration on outer faces is an **AC** phenomenon, not generic DC.
  - **G1-ELE-099/G2-ELEC-242:** motor auto-restart depends on control and protection, not simply rotor double-cage vs ordinary squirrel-cage.
  - **G1-ELE-028/G2-ELEC-177:** diagram still missing from canonical HTML; historical PDF figure previously located in Library and must be reused rather than requested from user.
- Source-triage CSV: `DEEP_EXECUTION_2026_11_11/DEEP_ELE_01_ALL_20_PRE_REVIEW_SOURCE_ABC_TRIAGE.csv`. **All classifications remain preliminary**.

## 3. Executed QA
After writing to GitHub, reopened `DEEP_ELE_01_ALL_20_PRE_REVIEW_SOURCE_ABC_TRIAGE.csv`, immutable `UNITS_568.csv` and V73 canonical ledger using connector reads, and checked all **20/20 units, 39/39 ID mappings**:
- Exact original question, A/B/C/order, per-ID key, batch routing, risk, unique unit IDs and SHA **MATCHED**, 22 CSV columns in every row.
- Source locator, preliminary ABC reasoning, next action present in every row.
- `independent_review=NOT_RUN`, `approved_for_learning=NO`, `key_change_authorized=NO` in every row.
- GitHub PR #7 remains Draft/unmerged, canonical HTML blob `bc5b5a61954ba138cf83987bfc932eca517f3b21` unchanged.
- Structural QA PASS for data integrity, **NOT domain truth**; the full batch JSON validator is not yet applicable because real independent review/source completeness is missing.

## 4. Overall actual position and handoff
- **Three initial batches** now have source/ABC **triage records**: NOR01 20 units (20 IDs), LEG01 20 (20 IDs), ELE01 20 (39 IDs), total **60 unique units / 79 canonical ID placements**, subject to the same final QA gates.
- **0 of 30 batches closed**, **0 of 822 approved** for training, **0 new independent AI reviewer executions** in this particular session. This is not a pass to use the trainer; due to key conflicts, ambiguous options and incomplete diagrams a full safety gate remains.
- Next: **DEEP-ELE-02** (20 further P0 units), source QA, then true independent reviewer for the 60 pre-reviewed cases and version-specific adjudication. Preserve earlier progress; don't redo source screening or count repeated evidence twice. When reviewer exists, create true batch JSON and run `deep_audit_execution.py validate` without invented signoffs.
- Any proposed canonical key/text/HTML/APK correction requires explicit user approval. Never merge, release, or deploy automatically.
