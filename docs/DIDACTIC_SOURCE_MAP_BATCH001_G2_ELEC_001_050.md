# Batch 001 | Didactic-source page mapping | G2-ELEC-001..050

**Date:** 2026-11-08  
**Source app:** user-provided V10.29 standalone HTML, SHA-256 `50c44b2798c2324121647ee5f24592fc2c1e049e827edb734c61dcf65d7f4b9c`.  
**Source corpus:** user's 14 PDFs, 4,120 pages, stored in original uploads and **not** in GitHub. Complete source filenames/hashes in [manual manifest](./CHECKPOINTS/manuals_manifest_2026-11-08.json).

## Important definitions

- `P`: a ChatGPT source-page inspection identified the actual principle described by the question. **NOT independently verified**.
- `C`: candidate chapter/page with matching technical keywords or general topic. The page **does not yet prove** the exact technical statement.
- A keyword hit is not an approved source or confirmed answer. Every final learner-facing page/paragraph requires an independent technical check and rights review.
- Page numbers below are **1-based physical PDF page numbers**, not necessarily printed book numbers.
- Source codes: `PREG` = 257-page *Pregătirea tehnică pentru autorizarea electricienilor*; `UTCN` = 114-page *Circuite electrice trifazate* (UTCN, 24 March 2021); `MAS` = 309-page *Mașini electrice*; `I7` = 249-page I 7-2011 consolidated as of 22 September 2023. See manifest for full filenames.
- Existing word flags originate from ANRE Trainer's `Audit.capcana_lingvistica` field; **not confirmed intentional traps**.

## Mapping table, 50/50 candidate PDF pages

| G2-ELEC ID | PDF page | Didactic topic | State | Linguistic flag |
|---|---|---|---|---|
| 001 | PREG 40 | Ohm's law | P | |
| 002 | PREG 11 | Resistance, SI unit Ω | C | |
| 003 | PREG 35 | Current, SI unit A | C | |
| 004 | PREG 11 | Voltage, SI unit V | C | |
| 005 | PREG 36 | Electrical power P=UI | C | |
| 006 | PREG 36 | Energy and time E=Pt, precise statement pending | C | |
| 007 | PREG 68 | Series, equivalent resistance | P | |
| 008 | PREG 71 | Parallel, equivalent resistance | P | |
| 009 | PREG 66 | Series, same branch current | P | |
| 010 | PREG 69 | Parallel, common voltage | P | |
| 011 | PREG 11 | Hertz, frequency unit | C | |
| 012 | PREG 86 | Period/frequency, T=1/f pending | C | |
| 013 | PREG 86 | RMS thermal meaning pending | C | |
| 014 | PREG 87 | Pure resistor phase relation | C | |
| 015 | PREG 88 | Ideal inductor current lags voltage | C | |
| 016 | PREG 88 | Ideal capacitor current leads voltage | C | |
| 017 | PREG 88 | Inductive reactance | C | |
| 018 | PREG 88 | Capacitive reactance | C | |
| 019 | UTCN 84 | Monophase apparent power S=UI | C | |
| 020 | UTCN 84 | Apparent power unit VA | P | |
| 021 | UTCN 84 | Reactive power unit var | P | |
| 022 | PREG 90 | Power factor cos φ | C | |
| 023 | PREG 87 | Pure resistive power factor 1 | C | |
| 024 | UTCN 66 | Balanced three-phase current sum | P | |
| 025 | UTCN 88 | Three-phase power √3 UL IL cos φ | P | |
| 026 | UTCN 66 | Star connection line/fase voltage | P | |
| 027 | UTCN 67 | Delta connection line/fase voltage | P | |
| 028 | MAS 7 | Transformer electromagnetic induction | P | |
| 029 | MAS 17 | Transformer turn/voltage ratio; exact equation pending | C | COMPARATIE |
| 030 | MAS 6 | Conventional AC transformer; constant DC exclusion pending | C | NEGATIE, EXCLUSIVITATE |
| 031 | MAS 4 | Motor energy conversion | C | |
| 032 | MAS 4 | Generator energy conversion | C | |
| 033 | PREG 133 | Voltmeter parallel measurement; proof pending | C | |
| 034 | PREG 136 | Ammeter series measurement; proof pending | C | |
| 035 | PREG 139 | Resistance measurement with supply disconnected; safety proof pending | C | CONDITIE |
| 036 | I7 38 | Short-circuit and protective devices; definition pending | C | |
| 037 | PREG 45 | Kirchhoff current law | C | |
| 038 | PREG 46 | Kirchhoff voltage law | C | |
| 039 | PREG 70 | Conductance as inverse resistance | C | |
| 040 | PREG 11 | Siemens unit | C | |
| 041 | PREG 11 | Farad unit | C | |
| 042 | PREG 11 | Henry unit | C | |
| 043 | PREG 41 | Current density | C | |
| 044 | PREG 40 | Conductor resistance with length/resistivity; full relation pending | C | |
| 045 | PREG 40 | Conductor resistance vs cross-section; formula pending | C | |
| 046 | PREG 41 | Metallic resistance vs temperature; source not yet adequate | C | |
| 047 | I7 37 | Overcurrent protection | P | |
| 048 | PREG 163 | Automatic breaker thermal/magnetic behavior; scope pending | C | |
| 049 | I7 25 | Residual-current protection, exact operating principle pending | C | |
| 050 | I7 23 | Protective earthing; combines with fault disconnection | P | |

## Audit results

- **50/50** IDs have a page candidate and matching keyword/heading in the actual uploaded PDF. This does **not** mean 50/50 independently verified explanations.
- **14/50** direct page-principle observations (`P`), reviewed by the same ChatGPT assistant only. **36/50** candidate topical mappings (`C`) still require exact principle or formula checking.
- **17 IDs** called out for higher-risk follow-up (006, 011, 012, 013, 023, 029, 030, 033, 034, 035, 036, 044, 045, 046, 048, 049, 050). `050` has a relevant fault-protection passage, but the teaching explanation must avoid presenting earthing alone as a complete protective measure.
- **3/50** linguistic-warning records pre-exist: 029 `COMPARATIE`, 030 `NEGATIE, EXCLUSIVITATE`, 035 `CONDITIE`. The language reviewer `AGENT-031` must adjudicate meaning and trap status separately.
- **76/76** conceptual questions G2-ELEC-001..076 have original correct-answer key `A`. The present UI shuffles **question order**, but it displays choices in fixed `['A','B','C']` order. Track the position-leakage defect in [issue #2](https://github.com/AcoBenny/ANRE_Trainer/issues/2). This does not imply wrong answer keys.
- Original `DATA` and all answer keys untouched. Previous quarantine of 76 erroneous question-bank candidate cards remains in place. No new trainer version, APK, or PDF redistribution.
- I7 source edition is a 2023 synthetic/consolidated snapshot and **not yet certified current for 2026**. No claims of verified legality or permissions to redistribute the uploaded PDFs.
- Independent semantic specialist QA: `NOT_RUN`; native Android and offline `file://` acceptance: `NOT_TESTED`; externally invoked AGENT-030 model/paired benchmark: `NOT_RUN`.
- Extra cost: **0 RON**.

## Next acceptance gate

1. Review the 17 high-risk candidate page mappings first, checking actual formulas, definitions and modality/negation. Extend source search to the 2007 Schneider technical handbook where relevant.
2. Independently adjudicate all 50 against the *correct question and answer proposition*, with exact chapter and paragraph/page; only then may any be labeled verified learner evidence.
3. Keep separate `TECHNICAL_DIDACTIC`, `NORMATIVE_TEXT`, `QUESTION_BANK_ORIGIN` labels. No source-card promotion based only on common keywords.
4. Continue `G2-ELEC-051..100`, then remaining topics, while importing historical exam questions only after document inventory and duplicate checks.

**Resume:** start at [checkpoint LATEST](./CHECKPOINTS/LATEST.md), read this batch and the uploaded manual manifest, then process the 17 priority follow-ups. Preserve original 822 IDs and keys.
