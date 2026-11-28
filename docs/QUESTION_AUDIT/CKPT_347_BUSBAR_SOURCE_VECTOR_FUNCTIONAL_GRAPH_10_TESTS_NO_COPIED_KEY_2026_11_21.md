# CKPT-347 | 10/10 topology tests for two original ANRE coupler diagrams, no scored keys | 2026-11-21

## What was executed
- Parent HEAD `91ae67cc5e8f8f20c3bc7917b23df280b7751b19` (PR #7 Draft). Two **manual source-graph abstractions** were derived from 2024 ANRE XLSX original DrawingML preview from V257/V258; each was enumerated with a real Python test script, testing all four selector pairs and the single circuit-breaker controlled path. **10/10 CONDITIONAL GRAPH tests PASS**. Because the graphs are manually extracted, not automatically verified full wire-netlists, this does **NOT** prove official correct answer or exact native Excel visual fidelity.
- Source-original vector SHA256 remains `2175d2c30ac8e2f149b28edd9ac00c233789bc0a3987ba779d6efed7afad920c`. Earlier source structural 18/18 pass continues unchanged.

## Breaker-path reachability results, under standard section/level labels
| Source image | From left/right breaker hubs | Can provide (ALTERNATIVELY) | Cannot provide through same breaker |
|---|---|---|---|
| **A, identical in EL30, EL31, EL32** | left upper/lower and right upper/lower | **2 longitudinal**, **2 diagonal** (one of four selected terminal pairs at a time) | **0 transversal** |
| **C, identical in EL31 and EL32** | outer upper-level selectors vs inner lower-level selectors | **2 transversal**, **2 diagonal** | **0 longitudinal** |

Categorization assumes: longitudinal links join equal-level busbars across two sections; transversal links join upper and lower busbar levels within a section; diagonal cross-links join opposite-level bars across sections. These names reflect standard Romanian substation textbooks, but exact source line/junction integrity and protective operation are not independently signed off.

## Implications and negative cases
- **EL30 diagonal:** source **A** yields two *selectable* diagonal paths. Options B and EL30.C were NOT netlist-modelled, so uniqueness is **UNPROVEN**.
- **EL31 longitudinal:** source **A** yields two selectable longitudinal paths. Source C does not yield one through breaker under this model; source B unmodelled, so uniqueness is **UNPROVEN**.
- **EL32 transversal:** source **C** yields two selectable transversal paths. A does not offer through-breaker transversal coupling. Source B unmodelled, so uniqueness is **UNPROVEN**.
- **BLOCK** the false inference that a *single breaker* implements two **simultaneously independent** coupler circuits. In all model states only one breaker-controlled path exists. Likewise, if you close two selectors from the same shared hub, you short busbars **without going through the breaker**: do NOT count this as a proper interruptible coupler.

## Evidence and safety
- Technical model, input topology, all ten named test results and remaining limitations: [V259_EL30_EL31_EL32_CONDITIONAL_BUSBAR_BREAKER_REACHABILITY_10_OF_10_NOT_EXAM_KEY_2026_11_21.json](./V259_EL30_EL31_EL32_CONDITIONAL_BUSBAR_BREAKER_REACHABILITY_10_OF_10_NOT_EXAM_KEY_2026_11_21.json).
- Reproducible package exists as conversation artifact `ANRE_CKPT347_modele_cuple_testate_QA.zip`, checksum `5320f0053fce4974333e22ddef1abf305b652a2a151ed9578286d90d6dd3c9d4`.
- Zero new QABC integrated into 822, zero key changes, no HTML/APK/main/merge/release changes. **136 known semantic holds remain, six historical strict conflicts included, 0/822 learner-approved**. Before any exam answer signoff: model all graphical options (B and EL30.C), check exact real junctions in native Excel, test alternative meanings of 'două circuite', review by qualified independent engineer and verify official 2026 source/key.
