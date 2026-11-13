# CKPT-036 | Start validare finală integrată + mapare contextuală + QA | 2026-11-13

## Obiectiv și ramură
- Continuare **fără reluarea cercetării preliminare** de la [CKPT-035](./CKPT_035_ALL_30_BATCHES_GLOBAL_CANONICAL_INTEGRITY_READBACK_2026_11_13.md).
- Repo `AcoBenny/ANRE_Trainer`, branch `audit/anre-v8-priority-17-20261109`, [PR #7 Draft](https://github.com/AcoBenny/ANRE_Trainer/pull/7), fără merge.
- **Nicio schimbare** a QABC, baremelor originale, HTML, APK, main/master, release.

## Noul model de muncă și fișierele create
- [ONE_PASS_VALIDATION_MAPPING_PROTOCOL_V1](./INTEGRATED_ADJUDICATION_2026_11_13/ONE_PASS_VALIDATION_MAPPING_PROTOCOL_V1_2026_11_13.md), audit sursă+ABC+explicație contextuală+evidențiere+condiții/ediție+QA independent efectiv+release **într-o singură fișă per QABC distinct**. Recenzia independentă nu este echivalată cu autoverificarea.
- [MASTER_UNIT_CARDS_568.csv](./INTEGRATED_ADJUDICATION_2026_11_13/MASTER_UNIT_CARDS_568.csv), **568/568 unități exacte**, întrebări A/B/C complete, SHA originale, toate cheile canonice pe ID păstrate; referință către unicul lot documentar preliminar.
- [GRADE_RELEASE_LEDGER_822.csv](./INTEGRATED_ADJUDICATION_2026_11_13/GRADE_RELEASE_LEDGER_822.csv), **822/822 ID-uri originale**, grade și bareme inițiale, SHA și referință la unitatea QABC; porțile de ediție, sursă, A/B/C, licență offline, QA tehnic/lingvistic/surse separat. **Toate `approved_for_learning=NO`**.
- [P0 pilot set A: 2 unități / 4 ID-uri](./INTEGRATED_ADJUDICATION_2026_11_13/P0_PILOT_2_CONFLICTED_UNITS_FULL_CONTEXT_CARDS_2026_11_13.json), două bareme contradictorii între grade.
- [P0 pilot set B: 2 unități / 4 ID-uri](./INTEGRATED_ADJUDICATION_2026_11_13/P0_PILOT_2_MORE_TROUBLE_CASES_CONTEXT_CARDS_2026_11_13.json), două probleme de definire/absolutizare.
- Cele patru unități P0 au deja în **master** document/locație, sursă accesată, explicație *parafrază originală contextuală de 4–6 propoziții* cu **bold** selectiv, termenii de evidențiat, A/B/C analizate, citat scurt atribuit, drepturi încă de verificat, riscuri și status blocat. Cele opt grade-ID corespunzătoare sunt actualizate în ledger, fără bareme modificate.

## Probleme efectiv investigate / 0/8 aprobări
**P0-A: G1-ELE-018 / G2-ELEC-170**
- Stem identic (capacitatea de serviciu a LEA trifazate simetrice fără influența pământului), **chei incompatibile A versus C**.
- University source: Mihai Puiu–Berizințu, `Bazele Electrotehnicii` 2013, §1.3.3 «Capacități în serviciu», [publisher-hosted academic PDF](https://cadredidactice.ub.ro/mihaipuiuberzuntiu/files/2012/05/BethSLP.pdf), excerpt retrieved; web PDF screenshot **CACHE_MISS**. Independent mathematical derivation `q1=C(u1-u2)+C(u1-u3)=3Cu1` for balanced positive sequence gives **candidate A=3C**, with conditions. This is *not* independent-source edition signoff nor user-learning approval.
- Original C on G2 unchanged; requires 2026 grade-bibliography verification and independent expert adjudication.

**P0-B: G1-ELE-102 / G2-ELEC-245**
- Stem identical double-busbar one-breaker station, original G1=A versus G2=C.
- [Technical page](https://schema-electrica.blogspot.com/2015/03/scheme-de-conexiuni-pentru-statii-si.html), §2.1.2.4 and fig 2.1.4/2.1.5, **re-opened HTML**: allows TWO normal operating patterns with one bus in working service and second warm energized through tie, OR circuits distributed on both bars and tie open/closed. Official [regulation for operational states](https://legislatie.just.ro/Public/DetaliiDocument/122751) **index only, page returned HTTP502**; no specific rule for universally preferred topology verified.
- This is **BLOCKED_MULTIPLE_PLAUSIBLE_MODES**, **no defensible unique correct key yet**. Do not propose A/B/C change without original edition and preference criterion/diagram.

**P0-C: G1-ELE-029 / G2-ELEC-178**
- Original C claims AC **only** from electromagnetic induction. [US DOE](https://www.energy.gov/cmei/systems/solar-integration-inverters-and-grid-services-basics) official open HTML explains modern electronic inverters convert DC to AC via controlled semiconductor switching. **Counterexample to unqualified «numai»** in an electric system; needs exam object narrowing to rotating generator or stem rewrite. No key change/approval.

**P0-D: G1-ELE-073 / G2-ELEC-218**
- Original B claims total «flux electric» = q. [UPB official course](https://www.elth.pub.ro/~petrescu/1.Energetica%20-%20IIB/Curs2.pdf), §1.3 and printed pp. 7–8, accessed PDF text, web screenshot **NOT_ENABLED**: electric flux `Ψ=∮D·dS=q`, measured in C. [OpenStax §6.2](https://openstax.org/books/university-physics-volume-2/pages/6-2-explaining-gausss-law) (HTML opened) uses electric field flux `Φ_E=∮E·dS=q/ε0`. **Original B provisionally supported only under Romanian electrotechnics D-flux definition**; linguistic ambiguity E vs D preserved. Neither grade signed off.

## Actual QA performed
- Created and read back the complete 568-unit and 822-grade ledgers; exact QABC, A/B/C, SHA, stored key(s) and routing compared against `V73_ALL_822_EVIDENCE_AND_RELEASE_GATES_MASTER.csv` and `ID_ROUTING_822.csv`. After pilot updates, deterministic recheck: **568 unit rows and 822 ID rows, 0 data mismatches, 0 illicit learner approvals**.
- **4/568 integrated contextual source cards researched and staged**, covering **8/822 ID placements**. Each has source URL, contextual highlight, per-option reasoning and blocker. ALL 4 cases continue `NOT_RUN` for independent technical, source and linguistic review. These 8 IDs are **NOT APPROVED**, not final map QA pass.
- Two arbitrary balanced phasor numeric tests confirmed derived `3C` equivalence (`3u1` charges), NOT an ANRE answer signoff.
- No independently isolated reviewer was executed, no 2026 exam edition fully certified, and no offline app popup was tested in this phase.
- For protected external sources, long passages are **ORIGINAL AUTHOR PARAPHRASES**, not fabricated verbatim quotes. Only brief exact quotes and link/locator are stored; after permission/rights verification a true longer fragment may be included. Thus the pilot demonstrates the user's contextual paragraph + bold highlight requirement safely.

## Milestone accounting
| Measure | Value |
|---|---:|
| Preliminary structural coverage | **30/30 batches, 568/568 units, 822/822 IDs** |
| Central units ledger/grade index | **568/568, 822/822** |
| **Integrated full contextual research cards** | **4/568 units / 8/822 IDs** |
| Real independent review completed | **0** |
| Grade-specific IDs approved for learning | **0/822** |
| Open source/ambiguity/edition gates | **YES** |
| PR #7 status | **Draft, unmerged** |

## Next (same algorithm, no reselection loop)
Continue prioritized remaining P0/P1, then P2: source-original, scope and editions, A/B/C, *context 4–6 sentences and key bold*, media rights/offline map, then truly independent QA (human or distinct mechanism), and status per ID. Consider G1-ELE-020 (absolute impossibility), G1-ELE-043 (generator stator current dependencies), G1-ELE-057 (definition of harmonics), G1-ELE-104 (dielectric oil arc interruption) as next risks. Do not ask repeated authorizations to begin batches. Ask user only for material ambiguity/hypothesis requiring expertise or unavailable copyrighted source. No persistent/background worker started.
