# CKPT-394 | GFR preimplementation: numeric source issue closed, P0 key escalated, 157 source-stage screened, 28-priority review packet

Date: 2026-11-22. Continues CKPT-393. Audit branch `audit/anre-v8-priority-17-20261109`, PR #7 Draft. Existing original workbook, canonical QABC, answer keys, HTML and APK must remain unchanged.

## 1. What was really executed

### V323 | Physical XLSX percentage format regression CLOSED at *source* layer
- Reopened user-uploaded original Grade II XLSX binaries via `artifact_tool`; independently traversed physical OOXML `xl/worksheets/sheet1.xml` and `xl/styles.xml`. Calculated source file SHA256 to match history. All 5 mismatching option cells (G2 Leg row75 B75,D75 and G2 Norme row77 B77,C77,D77) have true numeric type `t=n`, format `numFmtId=9`, built-in **`0%`** and style 15.
- Raw 0.05 => 5%; 0.12 => 12%; 0.20 => 20%; 0.25 => 25%; 0.12 => 12%. All five computed displays **match the independently fetched official ANRE 2023 online XLSX rendered cell strings**, already recorded in V321. This resolves numeric *source style* uncertainty, NOT actual rendered HTML/APK fidelity.
- [V323 evidence](./V323_5_G2_NATIVE_PERCENT_CELLS_BINARY_STYLE_AND_ANRE_DISPLAY_QA_2026_11_22.json) with physical cells and source hashes.

### V324 | Material legal answer-key risk elevated (research queue only)
- Reopened original V141 source exact stem and A/B/C for `QABC-0281 / G1-LEG-017`, and historical V283 which had route incorrectly still at **P2** despite documented key concern. Imported unchanged key is **B** (illegal grid connection). Original option **A** expressly says electricity theft established by final judgment; supplier regulation ANRE Ord.5/2023 **Art.18(3)(a)** explicitly permits contract **termination** on that fact. Article 18(3)(b) allows nonpayment with procedure, and `(c)` other statutory situations. Original option C refusal to give financial guarantee specifically supports supplier *interruption* under Art.26(2)(b), which is NOT the same as termination.
- Thus source-affirms original A, but **B cannot be declared categorically false** without checking any other applicable law under Art.18(3)(c); no certified original scoring key/independent legal reviewer. **Do NOT change imported B.** Add `G1-LEG-017` as P0 via V324 addendum only, preserve historical V283 and all stored keys.
- [V324 legal P0 overlay](./V324_G1_LEG_017_P0_RECLASSIFY_OVERLAY_ART18_SOURCE_KEY_2026_11_22.json). Source: https://legislatie.just.ro/Public/DetaliiDocumentAfis/264611.

### V325 | Source-bank and future migration collision preflight
- Reopened V141 + V283 + V298 + V321/V322/V323/V324 and ran deterministic first-pass structural assertions. **568 QABC groups/822 unique existing grade routes**: 415 source-original XLSX QABC (669 grade routes), **153 didactic authored G2 QABC** (153 grade routes). All 153 didactic imported correct answer positions are A, a positional learning bias, not evidence their key is false.
- **157 G2 original candidates** from V298: 157 unique source-row staging IDs, nonblank original stem and all A/B/C; **0 exact stem-plus-ordered-ABC collisions**, **0 stem-plus-permuted-ABC collisions** with existing 568; 8 overlapping stems but materially different choice sets. This **does not prove 157 semantically unique concepts** or authorize enlarging learning bank.
- V321 online ANRE content parity 157/157 still holds; 5 native percent cells proven via V323; existing source-original G1 options rewritten in **G1-NOR-048** and **G1-NOR-072** must be separated from didactic explanations (see CKPT393/V322). The current `audit_patch.js` runtime displays a pill for official documentary origin but may not convey *score approval*: review phrasing once app integration is actually authorized.
- [V325 bank source preflight](./V325_G2_RECOVERY_BANK_MIGRATION_READONLY_PREFLIGHT_2026_11_22.json).

### V326 | An expert-ready P0 source packet
- Generated **28 grade routes across 24 distinct QABC groups** with original canonical question and all ordered options, frozen imported key, source grade route, source ID/row, known options rewritten/fidelity risks, specific source locator, required independent technical/legal and linguistic signoff fields.
- Historical V283 has **27 P0 + 2 P1 + 793 P2**. After additive V324 new risk (one previously P2), current *operational triage only* is **28 P0 + 2 P1 + 792 P2**. No old priority CSV/JSON rewritten.
- [V326 human independent review packet](./V326_28_P0_GRADE_ROUTE_INDEPENDENT_REVIEW_PACK_UNAPPROVED_2026_11_22.json). **No real independent human/professional signoff occurred.**

### V327 | Reference randomized-choice scorer, 4,932 deterministic cases
- Simulated **all six displayed option permutations for all 822 existing grade routes**, with score keyed to stable SOURCE OPTION identity rather than visible A/B/C button label. 822 x 6 = **4,932 PASS** in a pure, isolated algorithmic preflight. The 153 didactic imported A answers, across all six permutations, become 306 displayed A, 306 displayed B and 306 displayed C, eliminating position-only leakage **for this reference algorithm**.
- **Not** a test of the actual current HTML, WebView, APK or integration data; none were executed. Source-current scoring keys can still be wrong despite passing permutation selftests.
- [V327 reference scorer simulation](./V327_822_ROUTES_4932_STABLE_OPTION_ID_SHUFFLE_SIMULATION_2026_11_22.json).

### V328 | Motor semantics, negative source-scope checks
- Reopened exact user I7/2011 2023-consolidated PDF physical pages 62–63. G2 Norme row55: §5.3.1.7.2.1 first says disconnect all active conductors, then expressly says neutral disconnection on overload is not mandatory. Original A repeats an overly broad first condition, C says phases; C is technically favored when respecting the adjacent exception but **no uniquely certified exam key**. G2 Norme row180: §5.3.1.1 permits **shared SHORT-CIRCUIT protection** for multiple similar loads under **15kW**. Original choices discuss absence of common OVERLOAD protection or a **16kW** trigger; the I7 clause does not prove a unique answer. Both held for contextual qualified review.
- [V328 exact object/action source negative checks](./V328_G2_NOR55_180_MOTOR_PROTECTION_SOURCE_OBJECT_NEGATIVE_QA_2026_11_22.json).

## 2. Status / explicit noncompletions
- Original 822 grade routes remain frozen in canonical app database; **0/822 independent qualified learning approvals**. Additional 157 G2 candidate source-row records remain quarantined with **0/157 approvals and no scored official answer keys authenticated**.
- Preimplementation source technical QA progressed: **numeric physical-format gate is now closed for 5 cells**, user-approved source-original recovery still staged and its 157 rows have first-pass research, source content online ANRE matching and no exact source duplicate in canonical. But source **semantic overlap**, applicable 2026 norm/legislation for every item, all P0 risk adjudications, independent technical/legal and linguist approval are still **OPEN**.
- Need subsequent **real HTML and APK runtime/regression** after authorizing import; 4,932 permutation unit simulations do NOT substitute for UI testing.
- No human/licensed reviewer was involved during these steps. No app code, stored key, original XLSX, HTML, APK, main, or merge/release changed. PR #7 stays Draft.

## 3. Next productive, finite task
1. Use V326 to conduct independent **source-exact P0 legal/electrical + linguistic review**, starting with G1-LEG-017, two G1 Norme original-vs-didactic rewrites and existing 27 priority routes. Escalate only genuinely disputed cases to user with full original A/B/C plus adjacent cited source.
2. Review 157 original G2 staged source questions for **semantic concept duplicates**, source year/edition/exception, official scored key vs explicitly nonofficial learning; safe original-exam/teaching separation. Do not declare any stage question learner-ready based on source text matching alone.
3. Once qualified approval exists, prepare actual migration to HTML+APK with stable IDs/choice keys, display-formatted percents, didactic shuffle and offline contextual cards. User approval still required for release, branch merge or modifying a frozen canonical exam key.
