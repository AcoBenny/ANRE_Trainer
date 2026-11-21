# CKPT-351 | 8 additional original questions diagnosed as nonunique or incomplete | 2026-11-21

## Measurable decision movement (no fake approvals)
- Prior CKPT-350: **12/136 source-semantic adjudications, 124/136 still source-undecided**.
- Now CKPT-351: **20/136 source-semantic adjudications, 116/136 still source-undecided**. Composition: **9** documented 2023 source-versus-imported-key conflicts; **3** source-consistent imported keys; **8** original-choice nonuniqueness / missing cumulative source requirements.
- **All 136 QABC remain release-blocked; 0/822 grade routes independently learner-approved.** No answer keys or question wording changed.
- Original I7 user PDF SHA256 `4bc3fc701cb71c937ad166462807423fa505c483783c5b8ad03b20f431`, snapshot 2023-09-22. Actual local source passages reopened at pages 13,61,65,70,71,162. 2026 in-force certification remains outstanding.

| QABC / grade | Source reason original question is unsafe for unique ANRE scoring | Exact I7 text scope |
|---|---|---|
| QABC-0316 | MIN_VALUE_VS_SUFFICIENT_HIGHER: For nominal voltage >500 V, minimum insulation resistance >=1 MΩ, so >=2 MΩ also meets the norm. Option B is the minimum threshold; C is a compliant stronger result. | §8.1.1.3.3, Table 8.1, p162 |
| QABC-0339 | MIN_DISTANCE_VS_SAFER_CLEARANCE: I7 requires 15 mm minimum air clearance between live fixed parts and earth metal; 20mm is above that minimum. B identifies the minimum; C is also compliant with 'at least'. | §5.3.3.19.1, p65 |
| QABC-0343 | RESIDENTIAL_CEILING_VS_LOWER_ALSO_PERMITTED: General board upper-edge limit 2.3m, residence exception up to 2.5m. Original 'nu depășească' leaves smaller values 2.0 and 2.3 compliant, but source-specific maximum in residences is 2.5m. | §5.3.3.21, p65 |
| QABC-0368 | RECOMMENDED_RANGE_VS_VALUES_INSIDE_RANGE: I7 recommends switches/buttons 0.6–1.5m. Original choices A=1m and C=1.5m are examples within range while B explicitly states the range; source uses 'Se recomandă' not a compulsory height. | §5.4.22, p70 |
| QABC-0376 | RECOMMENDED_CHILD_SOCKET_MIN_VS_MUST_AND_HIGHER_SUBSET: I7 recommends children's room sockets above 1.5m; original says must and C 'above 2m' also satisfies recommended >1.5m. Imported A >1m is not a reliably normative threshold. | §5.4.25, p71 |
| QABC-0395 | FIRE_RESISTANT_AND_FLAME_DELAY_CONJUNCTION_MISSING: Direct contact with combustibles permitted only for cables fire-resistant AND with flame-propagation delay (plus other specified material/device classes). Option C has delay only, omits fire resistance. | §3.0.3.7, p13 |
| QABC-0396 | FIRE_RESISTANT_AND_FLAME_DELAY_CONJUNCTION_MISSING: The same fire-resistant AND flame-delay conditions apply. B includes fire resistance alone, not flame-propagation delay. PVC is not categorically permitted. | §3.0.3.7, p13 |
| QABC-0404 | METAL_CONDUIT_DIRECT_PERMISSION_CONTEXT_OVERLAPS_WITH_CONDITIONAL: Metal tubes may be mounted directly on combustible building materials under §5.2.12.2.12, but for surface-mounted metal tubes in AD3/AD4/AF2b/AF3/AF4 zones §5.2.12.2.11 requires >=3cm stand-off; B conditional and C direct overlap by omitted environment. | §5.2.12.2.11–13 plus 3.0.3.7, p61 |

## False-positive controls
- No original problem is rewritten. For the examination, preserve the original stem and A/B/C verbatim, while showing the linguistic trap and underlying I7 context. The separate didactic reformulation fixes only a *practice exercise*, never pretends to be original ANRE wording.
- A stronger numeric measurement (2 MΩ or 20 mm) can satisfy a lower numerical floor while not being the **specified minimum**; the quiz must clearly ask which it wants.
- A recommendation `Se recomandă` must not silently be upgraded to a legal mandatory `Trebuie`, including height 0.6–1.5 m for switches and >1.5 m for children's room sockets.
- For cable contact with combustible materials source §3.0.3.7 explicitly requires *fire resistance AND flame-spread delay*. One property alone does not certify the pair.
- In metal-conduit mounting source §5.2.12.2.12 generally permits direct mounting on combustible materials but §5.2.12.2.11 imposes a 3 cm spacing requirement for specified AD/AF rooms when surface-mounted: without context B and C overlap.

## Controls and next work
- [Complete V263 immutable-previous-ledger supersession](V263_ALL_136_HOLDS_8_NONUNIQUE_SOURCE_DIAGNOSES_20_DECIDED_116_OPEN_2026_11_21.json), all 136 source IDs/200 grade routes retained, all 136 blocked for learning, zero keys changed.
- `V262`/`CKPT-350` preserved unchanged; these eight were previously `NOT_YET_ADJUDICATED`, now source-based `QUESTION_WORDING_REPAIR_REQUIRED` status. No grade-specific 2026 exam/official score certification.
- Next focus source-first triage of **116 remaining semantic-unknown cases** and separate *9 exact I7 keys in conflict* for later authorized correction. No HTML/APK, main, merges or releases.
