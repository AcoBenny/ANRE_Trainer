# CKPT-137 | ANRE Trainer: source-context coverage complete, final integrity QA and release blockers | 2026-11-17

## Results actually executed
**Documentation is complete; independent educational approval is NOT complete.**

- Repo `AcoBenny/ANRE_Trainer`, branch `audit/anre-v8-priority-17-20261109`, PR #7 DRAFT, never merged. Input HEAD `426af481b0bf2dbace667f6b2f452a992fb0c90d`.
- Last 17 unique contextual cards: `CKPT_135_LAST17_BATCH15_ELE026_046_051_129_131_225_233_240_243_244_246_247_248_264_265_2026_11_17.json` (15, commit `f5b239a78c556e16a7ffe2a7aa86b0a2d86c6c08`, ledger commit `5e669b383ced85f2ee47fd19ac35f2647f3b314b`) and `CKPT_136_FINAL2_SF6_ELE269_270_2026_11_17.json` (2, commit `1ac2a75e0cef20cbce6b21ec7325c766914aec4a`, ledger commit `426af481b0bf2dbace667f6b2f452a992fb0c90d`).
- **All 568/568 unique QABC units** have `contextual_card_present=YES_PRELIMINARY`, mapping to **822 distinct exam grade IDs** (**414 G1 + 408 G2**). Zero orphan member IDs or duplicate unit IDs in the ledger. **0/822 approved_for_learning**.
- The final 17 cards: 17/17 distinct IDs, original question + A/B/C text, member IDs, unit SHA256 and imported keys unchanged; every card has source(s), affirmative context, A/B/C rationales, warning/counterexample, explicit learner gate.
- **Full source-to-ledger integrity regression** performed on all 30 deep execution source CSV files: 300/300 (first 15 files) and 268/268 (next 15) matched exact unit ID, QABC hash, member IDs, complete present A/B/C fields and imported key map. **568/568 PASS, 0 missing or changed source mappings.** CSV parser handles quoted embedded newlines: G1-NOR-037 and G1-NOR-074 were initially false positives from a naïve line-split; both reconcile after full CSV parsing. Source document rows 300 + 268 = 568.
- Full source content matching is **structural provenance**, NOT evidence that each technical answer is correct or its source clause is authoritative for the exam. There is no performed real 822-item independent expert source/linguistics QA.
- Ledger review states: **565** units mark independent technical/source/linguistic QA as `NOT_RUN`; three older units G1-ELE-001/002/006 have non-`NOT_RUN` descriptive reviewer markers. Those three markers are prior recorded claims, **not newly re-executed independent QA**; none is approved for learning. All 568 have exam bibliography 2026, exact normative paragraph, official question provenance NOT independently verified/signed.

## Two genuine cross-grade conflicting imported answer keys: DO NOT normalize automatically
1. `G1-ELE-018` stored **A** vs `G2-ELEC-170` stored **C** for exactly the same original QABC. Topic: overhead line service capacitance `Cs` with pairwise `C12=C23=C31=C`; precise Romanian `Cs` definition, circuit and neutral reference to be source-verified. Technical hypothesis favors A under delta-to-star assumption; **not signed off**.
2. `G1-ELE-102` stored **A** vs `G2-ELEC-245` stored **C** for exactly the same original QABC. Topic: double-busbar station with one breaker per circuit, which busbars energized and transverse coupler reserve. Need genuine station topology and source procedure. **No justified common key yet.**
Both mismatches are faithfully preserved in source files and ledger; **they are genuine conflicting keys, not import errors**. Neither can be used safely for graded learning.

## Critical disputed source/wording cases to adjudicate with independent experts
- `ELE-026` multifunction bus coupler (imported C) versus `ELE-246` longitudinal-transverse bus coupler (imported B): cost vs continuity tradeoff requires authentic and distinct single-line schemes, not a topic-only switchgear article.
- `ELE-051` imported B (reciprocal transfer) lacks the linear/bilateral/reciprocal premise: Berkeley Niknejad 2000, §2.1.2 explicitly reports passive nonreciprocal gyrator. Reciprocity **cannot be deduced from passivity alone**. PDF text available; screenshot attempt failed with cache miss. 
- `ELE-046` imported C is model-dependent; test true nonlinearity versus unexcited nonlinear circuit branch.
- `ELE-141` Ohm law “indiferent de natura circuitului” contradicted by nonohmic element counterexample.
- `ELE-172` generic “materialele magnetice” includes linear dia-/paramagnetics, so nonlinearity is not universal.
- `ELE-129/131/243` switching sequence or disconnector operational question: general isolator/interlocks are NOT an approved local switching procedure. Require certified exact station diagram/norm and authorized expert; do not circulate an operational instruction from the imported key.
- `ELE-244` VT secondary short danger vs CT open secondary danger, explicit manufacturer safety evidence. Safety not an operation guide.
- `ELE-225/233/240/247/248/264/265`: source-scope or absolute-language caveats remain in CKPT-135. Grounding, topology, transformer accessory, charge induction, withdrawable breaker and autotransformer context matter.
- `ELE-269/270`: distinguish historical SF6 compact insulation/arc quenching and reduced routine maintenance (imported C/B) from Regulation (EU) 2024/573 Article 13(9), 13(14) **2026+ commissioning restrictions** and exemptions. For new MV switchgear <=24kV prohibition from **1 Jan 2026**, subject to derogations; >24kV <=52kV from **1 Jan 2030**, other HV classes from 2028/2032. Neither historical physical property should be claimed as universal modern legal permission.
- Earlier contested normative I7/PE155 item NOR032: exact source-object/edition comparison mandatory, never reuse I7 generic conduit clause to override exact service-branch-column provision.

## Source era and authority
- Official ANRE page https://anre.ro/participanti-la-piata-de-energie/persoane-fizice/energie-electrica/ lists historical/current downloadable examples including `ELECTROTEHNICA-09.2024`, `LEGISLATIE GR.1-05.2023`, `NORME TEHNICE Gr.1-05.2023`, and bibliography labelled 2023. This verifies a public index **only**, not each present imported question's official 2026 applicability or answer key.
- Berkeley nonreciprocal passive gyrator dissertation: https://www2.eecs.berkeley.edu/Pubs/TechRpts/2000/Archive/ERL-00-31.pdf p17 §2.1.2 (PDF text retrieved, screenshot cache miss).
- EU SF6 regulator and network operator explanation: https://eur-lex.europa.eu/eli/reg/2024/573/oj/eng and https://www.esbnetworks.ie/services/get-connected/renewable-connection/f-gas-regulation
- Manufacturer shorted VT secondary safety: ABB IOMM cited within CKPT-135 source references.

## Immutable safety / remaining sign-off
- This pass changed **only audit documents + worklist context flags**. No original question, alternative, key, HTML, APK or MASTER content changed. PR #7 remains Draft, no merge, no release, no study authorization.
- **Final requested task still open:** independent option-by-option electrical, exact-source-and-edition and linguistic adjudication of 822 grade IDs, with official exam provenance, beginning with contradictory key pairs and demonstrable source-object failures. Preserve contested items in a quarantine list; no forced approvals.
- No independent subagent runtime or background work was available or executed. All source fetches/reconciliations and structural checks above genuinely ran in this ChatGPT/GitHub session. Do not imply real expert signoff.

## Suggested handoff
Now source-context complete, change phase to adjudication, not repeated context-card generation. Resolve the two conflicting identical QABC key pairs first; then critical exact-scope problem list, followed by independent QA of remaining nonconflicting items. Only after all 822 passed separate signoff should trainer be cleared for learning. No merge or deployment until user approval.
