# CKPT-294 | Audit + explanatory cards in one pass, before final content approval | 2026-11-20

## User direction, and conservative execution boundary
- **Decision:** while source-auditing each ANRE question, also map the eventual explanatory card and reformulation-resilient teaching principle. This avoids two separate passes on the same source paragraph.
- Unofficial/supplemental examples are useful in **learning and transfer of concepts**, not false "official ANRE key" evidence. **Keep 153 nonworkbook didactic records** in a clearly marked **practice/training** lane; review their actual technical content and de-bias answer positions before any user-facing release. Do not delete them just because unofficial.
- **No app implementation yet**, no modification of the original question text, answer letters, import, HTML, APK, main or existing `audit_patch.js`. This checkpoint is a data contract + review workflow ahead of final signoff and app integration.
- Data sources are pinned V149 (Git blob `ee2ac5536c78eb06a0461243be34c117e257188f`), V151 and V154 final validation gates, V150 strict key issues, V152 eight technical preflight research cards, V155 same-stem groups, historical analysis files, and original uploaded `ELECTROTEHNICA-09.2024-2(2).xlsx` when exact source-text QA is needed. **V149 is an immutable imported snapshot, not an authenticated answer key**.

## Card identity and versioning
- **568 reusable evidence cards** indexed by `QABC-XXXX`, one card per unique normalized question + exact original A/B/C semantics; `822 grade-ID routes` link these cards to exact G1/G2 placements.
- **Never merge** cards because the same `enunț` repeats: V155 has 18 same-stem groups (40 QABC, 47 grade placements) with changed alternatives; these require distinct option-level reviews.
- Cards with any source-vs-trainer word mutation (six strict V150) must carry an explicit `version_dispute` status; do **not** display a single "original official answer" when the original source and the trainer choose different wording.
- A card references an official-looking XLSX **question only**, while actual answer grading originates from `imported_key_UNVERIFIED` until source-specific ANRE score provenance and professional QA.
- 153 original-not-matched practice items: `source_origin=TRAINER_DIDACTIC_NOT_PUBLISHED_SAMPLE`, `learner_track=PRACTICE`, `is_official_exam_question=false`. They can teach physics, law and error analysis; a practice item must not impersonate an official sample.

## Explanation-card data model
Each `QABC` evidence-card draft has:
1. **Identity and frozen source:** QABC; grade ID(s); original source workbook + worksheet row; exact imported stem/A/B/C; per-grade imported answer letters preserved separately; current question-versus-source fidelity flags, date/edition, source-type (published example copy / didactic-created / regulatory derived).
2. **Meaning and response analysis:** exact physical/legal object and action; scope and exceptions; candidate answer **only when positively source-supported**; `why_candidate`; `why_A`, `why_B`, `why_C`; each option's evidence state (SUPPORTS / CONTRADICTS / CONDITIONAL / UNKNOWN); mutual option relations; original language traps such as `numai`, `cel mult`, `de regulă`; a model-based counterexample.
3. **Learning transfer:** principle that remains true if numbers/phrasing change; quick mental model/formula/units; 1–2 **what-if reformulations** that reverse an assumption or change an exception; pitfalls; optional memory cue; wording can be in Romanian without requiring the AI review model to think in Romanian.
4. **Offline documentary locator:** typed source family, exact authoritative article/paragraph/edition, URL, whether the full source context was reopened, short permissible paraphrase, local I7 key/paragraph anchor if present (else **null**), figure link/OOXML anchor if applicable (else **null**). Never fabricate an exact paragraph, quote, inaccessible paywall text, legal applicability or local asset.
5. **Gates:** technical reviewer, linguistic reviewer, exact-source/edition verifier, human signoff, official-key proof, user-facing learning approval, all separate. A generated card is `PRELIMINARY_DRAFT` and **must never automatically become approved** based on the presence of a URL or an answer letter.

**Recommended after-answer UI**, once app implementation is authorized:
- Row 1: **concept/principiu** (short), answer status marked `imported/unverified` if unresolved, and optional official-vs-practice label.
- Row 2: **De ce A/B/C** (each specific, not generic "nu corespunde").
- Row 3: **Capcană / ce se schimbă dacă...?** (model/assumption counterexample, rewording prompts).
- Row 4: **Documentație**: source edition, exact paragraph, tiny relevant context excerpt or local offline I7 anchored popup, only if permitted and actually indexed; picture/schematic only when faithful local copy exists.
- No card is used to show or imply a guaranteed correct answer **before user responds**. Preserve existing `Repetă greșelile`, `Reținut`, randomization and offline behavior; version-specific actual app UI QA belongs **after** final content approval.

## Single-pass workflow for each QABC
1. **Original object:** load exact A/B/C, grade/member keys, source workbook row and version; compare last evidence checkpoint, dedup only by exact QABC identity. If published sample and trainer versions differ, lock both separately.
2. **Source and reasoning:** same source read supports **two outputs at once**: (a) answer truth/scope card incl. source edition and A/B/C for final adjudication, (b) learner card with principle, misconceptions, "what if?" negative tests and exact local anchor where possible. Expand to preceding/following paragraph for definitions/exceptions. Create only a *draft* when proof incomplete.
3. **Independent gates:** source-version reviewer + independent technical/linguistic reviewers independently challenge the reasoning and each other's counterexamples. No automatic status upgrades from one research assistant or model role. Authentic official grading key and human final approval remain separate. Approved data may only be shipped after user authorizes a versioned edit and real HTML/APK offline QA.

## Regression suite requirements
- Confirm **568 cards, 822 ID routes, all grade IDs unique**, keys/wording/sources exactly equal V149, and **0 learning approvals**.
- For each QABC with multiple grades, do not assume equal letters. Confirm the **two known cross-grade conflicts** preserved, no auto-reconciliation.
- Confirm **153 unofficial learning-track** routes, all not scored as published exam originals and all subject to position-bias QA.
- Confirm **18 same-stem choice-different** groups have distinct QABC cards and no dedup; six strict blockers are marked immutable and unresolved.
- **Adversarial card-content gate:** missing source paragraph or null anchor stays null and does not get fake `offline_ready`; source link existence is not source-specificity proof. Never populate generic per-option filler as a valid explanation.
- **Row/field alignment gate:** source locator may not contain the A-option rationale, A rationale may not be shifted into B, etc. Build exact ID->option consistency assertions and human-review remaining gate.
- Document regression code/tests separately if code is implemented; the checkpoint itself is **design/read-only**, not a claim that UI behavior was tested.

## Next
Produce a **568-card schema-compliant draft map and 822 per-grade links**, seed only the eight V152 cases for which explicit prior A/B/C and negative tests exist, and include all older QA/status flags without claiming completion. Future batches should fill these cards **during** actual source-specific answer validation, not in a separate repeat pass.
