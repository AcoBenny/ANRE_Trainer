# CKPT-030 | DEEP-ELE-09 + DEEP-ELE-10: source-aware QABC triage, 2026-11-12

## Repo / safety contract
- Repo `AcoBenny/ANRE_Trainer`; branch `audit/anre-v8-priority-17-20261109`, [PR #7](https://github.com/AcoBenny/ANRE_Trainer/pull/7) **Draft, unmerged** checked before and after each batch.
- Continued after [CKPT-029](./CKPT_029_ELE07_ELE08_RESUMED_AFTER_INTERRUPTION_2026_11_12.md) with **2 NEW fully triaged preliminary lots**, no rework of previous finished source triage.
- [DEEP-ELE-09 (20 units/40 canonical IDs)](./DEEP_EXECUTION_2026_11_11/DEEP_ELE_09_ALL_20_SOURCE_SCOPE_ABC_TRIAGE_2026_11_12.csv), commit `b87c465d010eb50479c4ff763dedf2d91099695f`.
- [DEEP-ELE-10 (20 units/40 canonical IDs)](./DEEP_EXECUTION_2026_11_11/DEEP_ELE_10_ALL_20_TECHNICAL_SOURCE_ABC_TRIAGE_2026_11_12.csv), commit `0b3bee3f3619d45cad932c0da56101f0f7d3fa0a`.
- Each CSV contains immutable question/ABC/key and unit/hash/members, A/B/C-specific preliminary reasoning, source URI/locator/access classification, limitations, **NOT_RUN** technical/source/linguistic independent reviews, `edition_verified=NO`, `approved_for_learning=NO`. **No key/QABC/HTML/APK/main/merge/release changes.**

## Risk findings: not adjudicated
- `G1-ELE-141`: canonical answer C (“indiferent de natura circuitului”) can be true when “natura” means AC versus DC in linear ohmic models, **not** for nonlinear elements. Reopened exact HTML [OpenStax 9.4 Ohm's Law](https://openstax.org/books/university-physics-volume-2/pages/9-4-ohms-law) confirms nonohmic exceptions. Flag `AMBIGUITY_SCOPE`; do not force a key change.
- `G1-ELE-156`: current-transformer position with canonical B (“busbar disconnect to breaker”) is **not uniquely preferred in all schemes**. Siemens [SIPROTEC 7SS52 manual §4 printed p90](https://cache.industry.siemens.com/dl/files/494/109743494/att_995924/v1/7SS52xx_Manual_A8_V047401_en.pdf) describes **both B and C** as physical configuration options. External document defines permissible locations, **not what Romanian exam prefers**. Text fetch/search worked but PDF screenshot failed `CACHE_MISS`; no visual assertion. Requires exact bay drawing, protection zones, Romanian source/edition, reviewer.
- `G1-ELE-146`: HV on-load tap changer frequently convenient for current, but [Hitachi UZE OLTC](https://www.hitachienergy.com/in/en/products-and-solutions/insulation-and-components/transformer-insulation-components/tap-changers/conventional-on-load-tap-changers/on-load-tap-changers-type-uze) also indicates alternate placement. No universalization of B.
- `G1-ELE-167/168`: H inferior/H superior: Romanian [topical secondary scheme source](https://www.scrigroup.com/tehnologie/electronica-electricitate/Statii-Si-Posturi-De-Tansforma34188.php) aligns line-vs-transformer frequent operations, but authentic diagram not visually opened, source specificity and expert QA outstanding.
- `G1-ELE-172`: “materialele magnetice” is broader than ferromagnetic; B-H nonlinearity cannot be universalized to paramagnetic and diamagnetic media.
- `G1-ELE-177`: official [IEEE C57.16-2025 public scope](https://standards.ieee.org/ieee/C57.16/6696/) matches *series dry air-core current-limiting reactors*, but allows outdoor and three-phase equipment too. Original A is a possible type, not exclusive without grade/scheme.
- `G1-ELE-164/171/181/182/187`: physical premises important: short vs no-load line, subdivision with electrical isolation, ideal characteristic impedance/natural power, loss models, current/voltage invariants.
- Remaining ELE09/10 QABC all carry source-scope/edition flags as needed. **Index snippets, thematic URLs, and engineering derivations are not equivalent to exact primary-source proof.**

## Real executed structural QA
- Re-fetched both saved CSVs. Compared originals with canonical V73 master, `UNITS_568.csv`, `ID_ROUTING_822.csv`; checked text, option order, canonical key, unit SHA/member IDs, batch membership, 3 option explanations, presence of blockers and non-approval fields.
- ELE09: **20/20 units / 40/40 placements**, 0 canonical mismatches.
- ELE10: **20/20 units / 40/40 placements**, 0 canonical mismatches.
- These are **deterministic data integrity checks performed by the same session**, not independent source/technical review.
- This session did **NOT** perform an external second-model reviewer, human professional review, verified ANRE exam bibliography current for November 2026, or the `source_scope_gate.py` regression. It did **not** approve any answer for learning.

## Cumulative status after CKPT-030
| Research-only metric | Count |
|---|---:|
| Deep batches with preliminary QABC research | **22/30** |
| Exact QABC units with preliminary research | **427/568** |
| Canonical ID placements with preliminary research | **612/822** |
| Batches still lacking full preliminary source triage | **8** |
| QABC units / IDs still lacking full preliminary triage | **141 / 210** |
| Questions approved for learning | **0/822** |

## Next
Continue `DEEP-ELE-11` then remaining ELE batches. Separately run genuinely independent option-by-option source and edition QA for every unit/grade, prioritize the above scope issues, preserve user-supplied reasoning as `USER_HYPOTHESIS`, ask user only for legitimate unresolved interpretation after own research. No autonomous alteration of canonical QABC, key or trainer; PR remains Draft.
