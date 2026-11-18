# CKPT-195 | G1-LEG-020: historical 100 kW exception + newer ATR appeals jurisdiction | 2026-11-18

## Canonical scope and no-change boundary
- Grade ID: `G1-LEG-020`; unit `AU-2b80efe97e6ae326`; SHA256 QABC: `2b80efe97e6ae32672b740fa344c26466eb2ef2efc14078ac8e1694fda1b2b39`.
- Original question: `Eventualele contestaţii ale avizelor tehnice de racordare se rezolvă de către:`
- A: `organele ierarhice ale emitentului`
- B: `operatorul de distribuţie care a emis avizul`
- C: `ANRE`
- Original imported key **A**, unchanged; provisional candidate **NOT_DETERMINED**. Not learner approved.
- Previous research CKPT-164, CKPT-190, reconciliation CKPT-191; do NOT double-count as newly processed unit.

## Specific primary legal evidence (source-era split)
1. **2003 historical regulation**, approved by HG 867/2003, `Articolul 31`, directly at https://legislatie.just.ro/Public/DetaliiDocument/45406 . It makes **hierarchical issuer bodies** responsible for handling objections to ATRs **for requested power <=100 kW**; **for >100 kW** the competent authority resolves them. The original QABC question *omits* the `<=100 kW` qualifier. This is a distinct old-legal-edition condition, not a universal A. The immediately preceding `art.30` and following `art.32` should be viewed in the official source for context (art.32 starts contract of connection procedure). Same historical regulation is also published in Monitorul Oficial 559/2003.
2. **Later scope rule**, Ordin ANRE nr. 74/2014, `Articolul 2` alin. (1)–(4), official consolidated portal https://legislatie.just.ro/Public/DetaliiDocument/310641 . Alin.(2) allows user to challenge an ATR **at the issuing network operator** within 30 days, and alin.(3) assigns resolution to **a commission within the network operator**, within 30 calendar days. The immediately preceding `Art.1` approves ATR templates; `Art.3` covers ANRE monitoring of compliance. Search-result extraction verified text; direct official HTML fetch returned 502. Text also checked via dated 2023 consolidated PDF (https://www.distributieoltenia.ro/resources/ckfinder/core/connector/php/connector.php?command=Proxy&currentFolder=%2FDO%2FCERTIFICARI+SI+PREVEDERI+LEGALE%2FLegislatie+secundara%2F2023%2F18.01.2023%2F&fileName=Ordinul+nr_+74_2014+pentru+aprobarea+con%C5%A3inutului-cadru+al+avizelor+tehnice+de+racordare.pdf&hash=24460cc7b9aefcd5&lang=en&type=Files); this PDF's page screenshot returned cache miss, **visual PDF QC not successful**.
3. Recent official portal index reflects `Ordinul nr. 15/21 mai 2026` amendments in the 2014 regulatory act; no independent comprehensive 2026 exam bibliography/key validation was done. Do not assume all 2003 conditions are applicable today.

## Semantic and adversarial option assessment
- A historical legal text supports option A **only with omitted power qualifier <=100 kW**. Its lack of qualifier in the current QABC is crucial: old art.31 has a different body at >100kW. Must not certify A universally.
- B modern art.2 jurisdiction is to a `comisie la nivelul operatorului de rețea`, not literally `operatorul de distribuție care a emis avizul` for every type of network operator. B is a closer approximation in ordinary distribution cases, not exact general statutory identity.
- C ANRE as `autoritatea competentă` for higher-than-100-kW cases in older regulation is a plausible role, but historical art.31 uses `autoritatea competentă`; identity as ANRE requires separate definition/era validation. Current 2014 procedure explicitly has initial resolution by network operator commission, with ANRE monitoring, not initial art.2 resolution.
- Flags: `MISSING_POWER_QUALIFIER`, `SOURCE_ERA_CONFLICT`, `OPERATOR_RETEA_VS_OPERATOR_DISTRIBUTIE`, `COMPETENT_AUTHORITY_NOT_SAME_AS_INITIAL_APPEAL_COMMISSION`.

## User presentation requirement
- Show **source before analysis**, with original wording intact within quote rights; show at least one preceding and one following article/paragraph by pinpoint links, not synthesized text falsely labeled original. Explain any reproduction limitation. Highlight missing qualifier `100 kW` only AFTER the original quotations. Do not ask the user to repeat already-resolved LEG017 or LEG024.

## Status / release gates
- `user_review=NOT_YET_REQUESTED`; `candidate_answer=UNDETERMINED`; `historical_A_conditionally_supported=YES`; `newer_B_near_match_with_operator_scope_difference=YES`.
- `edition_2026_and_official_exam_key=NOT_VERIFIED`; `independent_legal_and_linguistic_QA=NOT_RUN`; `approved_for_learning=NO`; `no_canonical_modification=YES`; `no_HTML_APK_or_merge=YES`.
- Next: ask user to inspect art.30–32 2003 and art.1–3 2014 from authentic links; capture new insight, keep category blocked for official-edition adjudication.
