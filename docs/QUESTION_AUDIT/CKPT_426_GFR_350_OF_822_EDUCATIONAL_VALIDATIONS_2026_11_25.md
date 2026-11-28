# CKPT-426 | 350/822 educational-content validations
Date: 2026-11-25 | Parent CKPT-425 (250/822) | branch `audit/anre-v8-priority-17-20261109` | [Draft PR #7](https://github.com/AcoBenny/ANRE_Trainer/pull/7).

**TARGET 350/822 REACHED in this checkpoint's source/ABC-ledger workflow: +100 NEW validated G1/G2 grade routes from 75 unique QABC groups.**
- **25 ORIGINAL QABC** (50 G1/G2 routes): existing canonical ANRE-worded electrotechnics original questions with exact unchanged original stem/A/B/C and per-grade key.
- **50 DIDACTIC QABC** (50 single G2 routes): supplemental, trainer-authored practice exercises, **NOT original ANRE exam questions**. This distinction is retained on every record and is not an assertion of official exam-key validation.
- Counts: **203 validated, 136 historical-held, 229 awaiting** = 568 distinct groups; **350 validated, 200 historical-held, 272 awaiting** = 822 grade routes.
- Historical hold queue **unchanged 200/822**, historical source/semantic issues are not implicitly approved. No earlier approval counted again.

## Evidence, sources and independent AI review
1. [25 ORIGINAL, 50 routes](CLOSURE_PILOT/CKPT_426_25_ORIGINAL_QABC_50_GRADE_ROUTE_EVIDENCE_2026_11_25.json): exact original question/ABC/grade key and source workbook identity, source locator and technical URL, separate A/B/C explanations with physical assumptions and reviewer session IDs. QABC-0233 received a source-scope correction: a voltage-transformer secondary short-circuit question must be supported by a voltage-transformer manual, not an unrelated current-transformer source.
2. [50 DIDACTIC, 50 routes](CLOSURE_PILOT/CKPT_426_50_UNOFFICIAL_DIDACTIC_QABC_50_ROUTES_EVIDENCE_2026_11_25.json): precise canonical practice question/ABC/key, technical textbook/manufacturer source and per-option reasoning; declared `trainer_authored_not_original_ANRE=true`.
3. [568 QABC master](CLOSURE_PILOT/CKPT_426_568_QABC_MASTER_2026_11_25.json) and [822 grade master](CLOSURE_PILOT/CKPT_426_822_GRADES_MASTER_2026_11_25.json): change only 75 previously-pending QABC and exactly 100 previously-pending grade routes to VALIDATED_FOR_LEARNING_CONTENT; all approved and historical-held previous states preserved.

Independent technical AI web research ran and reviewer session IDs are in both JSON evidence packets. These are **separate AI checks, not qualified human signoff**, and are NOT an authenticated official ANRE scored key or exam-standard edition approval. Actual live-fetched original source paragraphs **before / highlighted central rule / after are NOT all verified**, so teaching card contextual fields are explicitly **paraphrases**, requiring exact-source contextual/rights validation during offline implementation. A source URL or simulated QA must never be claimed as tested mobile UI.

## Notable ambiguous / scope-sensitive cases
- **QABC-0510/G2-ELEC-036** excluded from this batch due to ambiguity in short-circuit current/reactive-power wording; didactic **QABC-0530/G2-ELEC-056** was separately source-reviewed instead, with zero-neutral-current limited to a suitably balanced sinusoidal condition and triplen harmonics caveat.
- Original technical traps retained: QABC-0146 option B says **„numai”** about double-cage rotors, while high-bar rotors also exist (canonical C); QABC-0007 slip motor 0..1 is normal motoring regime; 0085 fuse/thermal relay are role-specific; 0233 is voltage transformer (TT) rather than current transformer (TC).
- QABC-0259 SF6: historic low-maintenance property is educational context, **not permission to commission new restricted F-gas switchgear** under [EU Regulation 2024/573, Art. 13](https://eur-lex.europa.eu/eli/reg/2024/573/oj). 2026 application/edition must be checked per equipment and jurisdiction.

## GitHub / release safeguards
Only audit evidence, new versioned ledgers, this report and `ACTIVE_HANDOFF.md` are changed on the Draft PR branch; **no original QABC/answer keys/XLSX, HTML, APK, main, merge or release**. Approval for use as an educational training app is still a separate future product/content-integration gate. Tests listed are evidence/ledger integrity and independent AI conceptual review, not real APK/HTML runtime tests.

**Next target: 400/822**. From 272 eligible unflagged routes, review new source-grade cases only; keep 200 historical-held separate. Do not re-review any of the **203** validated QABC without material contrary evidence. 
