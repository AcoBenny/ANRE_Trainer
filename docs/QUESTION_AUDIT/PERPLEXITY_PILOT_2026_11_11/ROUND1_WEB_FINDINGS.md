# Research round 1 (of 4) | ANRE P0 vs Perplexity pilot | 2026-11-11

**STATUS:** 5/5 pilot inputs explored by THIS ChatGPT web research, **0 Perplexity runs**. NOT independent expert QA, NOT validation for learning. Existing deep batch triage was reused and no original content was changed.

## What changed vs previous evidence
- **G1-ELE-018 / G2-ELEC-170:** re-derived the 3-phase balanced delta capacitance equivalence (charge per conductor `Q_a=C(V_a-V_b)+C(V_a-V_c)=3CV_a` given `V_a+V_b+V_c=0`). Conflicting stored grade-I A and grade-II C remain; `capacitate de serviciu` precise definition and independent review missing. Prior LibreTexts page fetch returned cache miss. This is **not new external proof**.
- **G1-ELE-028 / G2-ELEC-177:** revisited historical user-uploaded PDF page 10 WITH IMAGE. Diagram shows generator/branches/fault but learner app still lacks it; do not redistribute the document. New specific manufacturer lead: **GE Vernova, Reducing Fault Currents in Power Systems with Air Core Series Reactors, pp2–3**, which details a network case where series reactance reduced available short-circuit current. Supports existing conditional B, without asserting same network or optimality. GE PDF text opened, `web.screen` failed cache miss.
- **G1-ELE-029 / G2-ELEC-178:** DOE inventoried earlier and reopened, confirming that a DC-to-AC electronic inverter contradicts the unrestricted word `numai` before induction. No automatic rewrite.
- **G1-ELE-088 / G2-ELEC-233:** Hitachi HTML page reopened. CED Engineering third-party educational GIS chapter pp98–99 adds an explicit gas-compartment vs gas-zone **trade-off**; **not a first-party replacement for the exact per-phase design**. The extra source is secondary, and PDF screenshot failed. Still no clearly established unique answer.
- **G1-ELE-102 / G2-ELEC-245:** ABB Distribution Automation Handbook §3.14.1.4 text opened: typical double bus arrangement uses both buses, bus coupler open, feeders shared. §3.14.1.3 with dedicated TRANSFER bus permits breaker service. Contradicts unqualified preference for cold standby (G1 A) and favors candidate hot-standby C conditionally, but not a universal mandatory practice. Figure 3.7 PDF screenshot failed; no claim of visual verification. Already known source in CKPT-019, now exact section reread.

## Evidence and controls
Detailed A/B/C, URLs, access and blockers in [ROUND1_WEB_EVIDENCE_5.csv](ROUND1_WEB_EVIDENCE_5.csv).
- Source handling: web PDF-text extraction is **not PDF screenshot verification**. ABB/Hitachi/CED/GE screenshot attempts all cache misses; links are real search/open results but PDF visual content not validated this session.
- GE paper is a **specific first-party manufacturer lead** for current-limiting reactors; the additional CED paper is **secondary engineering education**. DOE, ABB and Hitachi are already in prior ledger. Do not market this as 5 new sources.
- Existing source/app reconciliation: 5 unique QABC units correspond to 10 canonical IDs across Grade I/II (duplicated cases). No new deep batches triaged. No changes to canonical questions/options/keys/HTML/APK.
- Scope and edition gate: none of these non-ANRE sources establish by themselves the applicable exam bibliography. No distinct AI agent or engineer reviewed these records.
- **QA structural, not answer truth:** preserved QABC unit IDs and original stored keys from `INPUT_20_P0.csv`; `independent_QA=NOT_RUN`; `perplexity_run=NOT_RUN`, `approved_for_learning=NO`.

## External Perplexity still unresolved
Perplexity is not connected as a plugin/session; no token provided or used, and this chat does not have its browser/computer workflow. The external experiment remains 0/20. To obtain a genuine comparative score, run the published `PROMPT_PERPLEXITY_4X5.md` externally and return response links/exports. Do not treat this web-source research as Perplexity performance.

## Next
Process remaining rounds (2–4) as source discovery while waiting for external Perplexity response if the user initiates one; prioritize primary source/edition/diagram QA, then compare identical 20-case outputs. Existing staged bank: **7/30 prelim batches; 0/822 approvals**. No merge/release.
