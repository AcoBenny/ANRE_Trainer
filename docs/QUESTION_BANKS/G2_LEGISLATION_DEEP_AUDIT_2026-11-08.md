# Grad II legislation | Second-pass audit and highlighted-choice validation | 2026-11-08

**Interim report, NOT checkpoint #3.** The canonical project checkpoint remains CKPT-002. All 822 question records and stored keys remain unchanged. The 18 uploaded historical PDFs remain outside GitHub; this file is metadata and QA findings only.

## Evidence inputs
- 733260591-Intrebari-LEGISLATIE-GRADUL-2-2023.pdf: 32 PDF pages, 196 table rows with full question and A/B/C, 85 distinct normalized question stems; SHA-256 `e5d4e04c25158038bf3cba2452445bc8611251d27fb78c1aa85f8bd700fc731a`.
- 668467690-SubiecteLegislateGradulII01-20221.pdf: 37 PDF pages, 329 rows, 225 distinct stems; SHA-256 `65335b0d7809e7be22cd6a56ab8f9570fce4a55d79d77f217e4c77d3715b96ce`.
- 525 rows across the two, **235 normalized distinct stems**, of which **75 stems appear in both**. Counts refer to extracted table rows, not 525 novel questions.
- Target: user-supplied ANRE Trainer V10.29 standalone embedded DATA, 822 stable questions, G2-LEG category 62 entries.

## Classification against the 822 application records
- 127 rows: exact normalized stem AND A/B/C in the same order.
- 22: identical stem, choices differ; source citations, annotations or alternate options require manual review.
- 9: near-match at >=85 text similarity, semantic equivalence NOT confirmed.
- 367: no high-score app stem, **not** automatically novel/ready to import.
- All 62 current G2-LEG category questions have key A, and 0 of these 62 stems exactly matches the two historical files. 45 are bibliography/tematica, 15 regulation, 2 tariffs questions. This is a pedagogical coverage gap *candidate*, not proof of invalidity.

## Extracting legacy highlighted answer choices
- Inspected visual PDF page 3 in 2023 document and page 6 in earlier document to confirm yellow fill on selected answer cells; then deterministically detected fill rectangles overlapping table option cells.
- A single yellow A/B/C option cell was detected on **426 of 525** extracted rows. Remaining 99 had no detected yellow cell (all in the 2023 document). Such fills indicate the *PDF author's marked answer*, NOT an official/current correct key.
- On rows with identical stem and identical ordered options, 72 marked choices agreed with the app's stored key, while **10 row instances disagreed**, collapsing to **6 stable app IDs**.
- Six candidate key conflicts: `G1-LEG-017` (app B / PDFs A), `G1-LEG-019` (C / B), `G1-LEG-020` (A / C), `G1-LEG-026` (C / B), `G1-LEG-040` (C / A), `G1-LEG-042` (B / A).
- Two preliminary legal contradiction findings supported by current official legislation text:
  - `G1-LEG-019`: text "Nerespectarea normelor tehnice emise de către ANRE constituie:"; app key C ("Abatere"), source marks B ("Contravenție"). Legea 123/2012 art. 93 alin. (1) pct. 3 expressly includes the conduct among contravenții. **Requires independent QA before correction.**
  - `G1-LEG-026`: text "Executarea sau folosirea de instalații clandestine în scopul racordării directe la rețea constituie:"; app key C ("contravenție sau infracțiune, după caz"), source marks B ("infracțiune"). Legea 123/2012 art. 92 alin. (2) expressly designates infracțiune. **Requires independent QA before correction.**
- The remaining 4 source-vs-app disagreements are `CURRENT_LAW_REVIEW_PENDING`. Some are sensitive to year, exact word choice or regulation scope. No auto key updates.

## Official legal cross-check
- ANRE Ordin 99/2021 was abrogated by Ordin 66/2023 (art. 2): https://legislatie.just.ro/Public/DetaliiDocumentAfis/288045
- ANRE Ordin 66/2023 was amended by Ordin 65/2024: https://legislatie.just.ro/Public/DetaliiDocumentAfis/288327
- Legea 123/2012 articles 92 and 93 consolidated versions: https://legislatie.just.ro/Public/DetaliiDocument/249550
- Exam topic and official question access: https://anre.ro/participanti-la-piata-de-energie/persoane-fizice/energie-electrica/electricieni/examene/

This is an article-specific check for these issues, **not a 2026 legal-currentness approval of the entire historical corpus**.

## Outputs and provenance
The user can download a local detailed CSV with all 525 extracted rows, A/B/C/source-page/mark, comparison status, a cross-source CSV, 6-case conflict CSV, JSON summaries and this report in the in-chat ZIP. Avoid committing raw historic question texts or the uploaded PDF files to GitHub without licensing review.

## Next QA gates
1. Independently verify `G1-LEG-019` and `G1-LEG-026` with the exact question wording, statutory text, and original Excel answer key provenance. Mark `FIX_APPROVED` only after review.
2. Review other four source-key disagreements and all 22 changed-choice rows, distinguishing permutations from legal changes.
3. AGENT-031 flags traps (e.g. "abatere" vs "contravenție", "după caz"); human/technical legality adjudication must remain distinct from linguistic flag.
4. Expand to remaining Grade I/II historical PDFs and ensure no Grade III/IV spillover. Preserve all 822 original keys until release gate.
5. Do not create CKPT-003 until 2–3 substantial validated batches/release/handoff. No extra API costs (0 RON).

**QA status:** deterministic extraction+PDF color comparison executed; sample visual inspection executed; 2 article-specific official source comparisons executed; independent specialist review NOT_RUN; mobile/browser runtime NOT_RUN; no model-vs-baseline agent benchmark; no APK release.
