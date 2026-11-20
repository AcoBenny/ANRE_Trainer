# CKPT-305 | GFR G1-NOR-031–045 | 2026-11-21
## Snapshot
- Previous HEAD `778a7f307dcef00291da32c367a01166c050c11e`; exact 15 QABC-0345..0359 / G1-NOR-031..045 / source workbook rows 38..52, matching original normalized workbook stem/A/B/C via V149 and V175.
- New layer `V216_NOR031_045_PE155_I7_EXACT_ABC_NEUTRAL_AND_SELECTIVITY_HOLDS_2026_11_21.json`, blob `0aab15db05fa999a968b733fdc0c66012ce0c1a0`: 15 complete A/B/C explanatory drafts = 45 option rationales and 15 unofficial reformulations; no original key changed.
- New manifest `V217_568_QABC_358_FULL_ABC_CARD_COVERAGE_822_GRADE_ROUTES_2026_11_21.json`: **358/568 editorial cards**, **612/822 grade routes**, **210 cards pending**, **101 explicit semantic/source-model holds** (+4); 6 historical strict source/key blockers preserved separately, categories may overlap. **0/822 learning approvals**.
## New explicit holds
- NOR033 QABC-0347: question says «trebuie» whereas PE155/1992 §2.2.4 says «se recomandă» two fuse-rating steps. «At least» is minimum, and actual selectivity depends on curves.
- NOR035 QABC-0349: wording «masă (echipament sau element de construcție)» extends the exact equipment definition; C retained as imported, but scope not certified.
- NOR041 QABC-0355: imported B has correct 16 mm² Cu /25 mm² Al polypase threshold but adds monophase THREE-wire. I7 §5.2.4.6.1(a) explicitly mentions TWO-wire monophase. No forced fix.
- NOR042 QABC-0356: imported B includes THREE-wire mono and erroneous 25 Cu/35 Al thresholds; I7 §5.2.4.6.1(a) affirmatively supports candidate A for TWO-wire monophase. Key B left unchanged; requires independent adjudication. Not counted as a new one of six historical strict conflicts without independent gate.
## Source and scope
- PE155 §3.2.3 in historical third-party copy https://www.baluna.ro/wp-content/uploads/2018/02/pe_155_92.pdf distinguishes PE earth bar at service box versus dedicated terminal on consumer distribution board (NOR031).
- PE155 §3.2.10 gives **15m straight horizontal column** plus vertical-straight exception and bend conditions (NOR032). Generic I7 tube pull-box limits must NOT substitute for service-column rules.
- I7 §3.0.2.2–5, chapter 2 definitions and §5.2.4.1–6 references reused from CKPT218, CKPT219, V77, V90.
- Current I7 official portal request returned HTTP 502; PE155 historical PDF screenshot failed with cache miss. Do not claim authentic official current source, real independently qualified reviewer or authenticated 2026 answer key. All explanations are drafts.
## Structural QA / change control
- Before push: 15/15 distinct workbook-matched QABC source rows, 45/45 separate option rationales, 15/15 reformulations, 4/4 new holds, 568 unique QABC, 822 grade IDs, 358 draft cards and 612 draft-covered grade IDs, approvals 0.
- Append-only three files under docs/QUESTION_AUDIT. No barem, original question/choice, HTML or APK edits. PR #7 stays Draft, no merge or release.
## Next exact queue
- Resume **QABC-0360 / G1-NOR-046** from V217 key next_25_source_text_exact_not_yet_fully_editorialized. Exclude four altered-original candidates until separate source-version reconciliation. Final certification remains independent technical/linguistic/current-edition gate.
