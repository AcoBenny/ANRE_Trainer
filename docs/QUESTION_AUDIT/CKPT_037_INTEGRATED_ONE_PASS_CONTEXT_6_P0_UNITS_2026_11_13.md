# CKPT-037 | Integrated final source+ABC+contextual map pilot | 2026-11-13

## Work scope and preservation
- Continues [CKPT-036](./CKPT_036_INTEGRATED_ONE_PASS_MAPPING_P0_START_2026_11_13.md) on `AcoBenny/ANRE_Trainer`, branch `audit/anre-v8-priority-17-20261109`, [PR #7 Draft](https://github.com/AcoBenny/ANRE_Trainer/pull/7) unmerged.
- **Research** and *contextual mapping* have been staged for **6/568 unique QABC units covering 12/822 grade-specific IDs**. **0/822 approved for learning**. Source edition, official ANRE bibliography match and independent expert QA remain unverified. No canonical answers, keys, main branch, HTML or APK altered.
- Central [568-unit master](./INTEGRATED_ADJUDICATION_2026_11_13/MASTER_UNIT_CARDS_568.csv) and [822-ID release ledger](./INTEGRATED_ADJUDICATION_2026_11_13/GRADE_RELEASE_LEDGER_822.csv) now contain all six contextual mapping records, with long **original Romanian paraphrases**, selectively **bold** technical phrases and 3 per-option justifications.

## New research since CKPT-036 (2 QABC / 4 IDs)
**G1-ELE-043 / G2-ELEC-189**, original both **A** unchanged, source [Schneider Electric *Definition of reactive power*](https://www.electrical-installation.org/enwiki/Definition_of_reactive_power), power triangle and 3-phase formula after paragraphs at §§ 'Definition', lines 51–92 (official publisher/manufacturer HTML OPENED and read). For balanced sinusoidal phase conditions: `S²=P²+Q²`, `S=√3 U_L I_L`, `I=√(P²+Q²)/(√3 U_L)`. The stem claims current grows *directly proportionally* with one of U, P alone or Q, with no stated constant variables. At fixed P,Q current falls when U grows; dependence on P/Q is not direct proportionality in general. No unique unqualified key supported. **BLOCKED / no proposed key**.

**G1-ELE-104 / G2-ELEC-247**, original both **A** unchanged. Original A states dielectric oil provides *only* insulation, B states it extinguishes arc in circuit breakers, C refers to lubrication of operation mechanism. Two actual manufacturer pages opened:
- [Gulf Oil, *Gulf Transcrest I*](https://me.gulfoilltd.com/en/products/gulf-transcrest-i), Application/Key Benefits: insulation **and** quenching of arc at switch contacts in oil-switchgear.
- [Bharat Petroleum, *MAK Hivoltol*](https://www.bharatpetroleum.in/our-businesses/mak-lubricants/industrial-lubricants/mak-hivoltol), Applications (web page last updated March 26 2026): oil as quenching medium in circuit breakers and switchgear.
Therefore **A's «doar» is too restrictive when including oil circuit breakers**; **B is a provisional candidate only for the specific oil-breaker type, not all vacuum/SF6 breakers**. No key change, no grade/edition matching or independent QA. Card contains all ABC and contextual paraphrase.

Evidence JSON: [P0 technical pilot](./INTEGRATED_ADJUDICATION_2026_11_13/P0_PILOT_2_TECHNICAL_CONTEXT_COUNTEREXAMPLES_2026_11_13.json).

## Prior 4 cards still blocked, not forgotten
- **G1-ELE-018/G2-ELEC-170** same QABC original contradictory keys A/C; mathematical 3C candidate under balanced 3-phase with earth neglected; University textbook PDF image/edition/ANRE match not signed.
- **G1-ELE-102/G2-ELEC-245** same QABC original contradictory keys A/C for two busbars; multiple normal operating variants, no unique source rule.
- **G1-ELE-029/G2-ELEC-178** categorical «numai prin inducție» contradicted by modern semiconductor inverter converting DC to AC; original C unchanged, no unique key in literal general scope.
- **G1-ELE-073/G2-ELEC-218** Gauss «electric flux» D-flux = q versus E-flux = q/epsilon0, original B supported only if D-flux definition intended.

Evidence JSON [P0 pair 1](./INTEGRATED_ADJUDICATION_2026_11_13/P0_PILOT_2_CONFLICTED_UNITS_FULL_CONTEXT_CARDS_2026_11_13.json) and [P0 pair 2](./INTEGRATED_ADJUDICATION_2026_11_13/P0_PILOT_2_MORE_TROUBLE_CASES_CONTEXT_CARDS_2026_11_13.json).

## Executed QA of central files
- After latest commits, fetched entire master and release ledger again, compared **all 568 QABC** questions, options and member-key objects with canonical V73; compared **all 822 grade-specific ID** original keys, unit IDs and hashes with ID_ROUTING_822 and master unit file.
- **0 deterministic mismatches**. 6/568 have complete 4–6 sentence contextual original paraphrases, exact source link/section, source access and short verbatim excerpt with attribution, plus distinct A/B/C arguments. 12/822 IDs show staged paragraphs. All learning approval values **NO**; 0 certified.
- Source QA, technical QA, linguistic QA, 2026 applied source editions, redistribution/offline rights and mobile UX testing **NOT_RUN**. Never claim they passed; links/provider HTML accessed but exam authority applicability not certified. The six investigations are **progress, not final adjudications**.

## Next tasks, with no rerun of research inventory
- Continue from remaining P0/P1 **G1-ELE-020, G1-ELE-057, G1-ELE-028, G1-ELE-099, G1-ELE-113**, followed by standards I7/PE155 grade-specific exact object/editions and legal changes, always adding contextual map in same source visit.
- When source truly fails or exact edition missing, stop that *case* with explicit blocker and proceed next; do not regress to repeated general web searches. User can add hypotheses, recorded as such.
- Only after evidence and *actual* independent reviewer gate may rows be promoted to `approved_for_learning=YES`. Never modify canonical answer key without explicit authorization or merge PR #7. No background process active.
