# CKPT-427 | 400/822 ANRE educational-content validations

2026-11-25 | Parent CKPT-426 = 350/822 | audit branch `audit/anre-v8-priority-17-20261109` | [PR #7 Draft](https://github.com/AcoBenny/ANRE_Trainer/pull/7).

**TARGET 400/822 reached in educational content ledgers, +50 NEW grade-specific routes from 33 new distinct QABC groups.** This is not official ANRE scored-answer certification or an application release.

## Batch and classification
- **19 ORIGINAL QABC**, **36 grade routes**: 17 groups common G1/G2 and two G1-only original groups. Exact stem, all A/B/C alternatives, original imported key, source workbook row and original legacy card SHA preserved. [Original evidence](CLOSURE_PILOT/CKPT_427_19_ORIGINAL_QABC_36_GRADE_ROUTES_EVIDENCE_2026_11_25.json).
- **14 DIDACTIC QABC**, **14 G2 grade routes**: supplemental trainer-authored exercises, explicitly NOT original ANRE examination questions. Individual A/B/C + references, all source provenance preserved. [Didactic evidence](CLOSURE_PILOT/CKPT_427_14_DIDACTIC_QABC_14_ROUTES_EVIDENCE_2026_11_25.json).
- New 33 QABC have no overlap with previously validated 203 groups. **236 validated, 136 historical hold, 196 awaiting = 568 groups**. **400 validated, 200 historical hold, 222 awaiting = 822 grade routes**.
- Cumulative validated groups: **172 original + 64 supplemental didactic = 236**. Both types are included in the existing 822 educational-route denominator, but retain their own explicit origin classification.

## Evidence and independent review
Independent external AI reviewer research actually ran through Parallel, plus source checks through public engineering and teaching sources (World Bank, NIST, OpenStax, Schneider, EirGrid, electrical equipment manufacturers, power-system courses). Exact original ABC and all option-specific reasons are linked and recorded in each JSON evidence record with reviewer session IDs and legacy card blob SHAs. These are independent **AI** checks, not qualified human signoff, official 2026 ANRE bibliography/key certification, or proof the app has passed offline tests.

**Source-context limitation:** the source section/topic and teacher-authored before/highlight/after explanations are mapped, but the original surrounding paragraph word-for-word is **NOT** fully authenticated across all cases. Do not mark offline paragraph-popup/rights/source-edition QA complete. Verbatim original clauses, correct edition, copyright/rights and real HTML/APK integration remain separate gates. Do not replace these paraphrases with allegedly original source quotations.

## Counterexamples, exact-scope rules
- Original **QABC-0001**: shunt capacitor normally raises local feeder voltage, while a very stiff source or active voltage regulator can suppress observed rise.
- **QABC-0106**: coil inductance uses the **linked flux** (NΦ), not necessarily a single-turn flux Φ.
- **QABC-0145**: alternative periodic quantity has zero algebraic mean by the chosen convention, unlike an arbitrary periodic wave with DC offset.
- **QABC-0166**: series air-core reactors are a documented fault-current limiting solution, not the only construction that can exist.
- **QABC-0197**: line current = √3 × phase current only in the balanced delta model; the original approximate phrasing "mai mare de 1,73 ori" is preserved, annotated, not rewritten.
- **QABC-0203**: conservator also takes oil expansion; the distractor says **"numai"** and is therefore false.
- **QABC-0232**: conceptual separator operation at no load, NOT a live switching instruction; any real operation requires licensed safety procedures.
- **QABC-0241**: parallel equivalent of identical DC sources assumes the same polarity.
- **QABC-0257**: rapid replacement benefit requires compatible spare and a failure of replaceable parts, not guaranteed for every cubicle fault.
- **QABC-0054**: reactive inductive magnetization is one true application; capacitor reactive energy also exists. Never treat the original A as an exhaustive general definition.
- **GIS QABC-0081**: gas-tight compartment separation/localization is technical evidence, NOT authorization to install restricted new F-gas switchgear under [EU Regulation 2024/573](https://eur-lex.europa.eu/eli/reg/2024/573/oj).

**Not counted / remain pending**: QABC-0165 (sequence model exception), QABC-0064 (exact damping terminology not established), QABC-0028 (dry/immersed fire comparison not unconditional), QABC-0206 (symmetrical-component scheme wording), QABC-0093 (double bus cold-reserve scheme source/interpretation), QABC-0510 (short-circuit ambiguity), QABC-0537 (competing reasonable option about meter range selection). Historical holds unchanged.

## GitHub safeguards and QA
Original question/key source files, HTML, APK, released artifacts, and main branch untouched. The changes on Draft PR #7 must be exactly six audit documentation/state files: the two evidence JSONs, the new 568/822 ledgers, this report and `ACTIVE_HANDOFF.md`. Both ledgers must read back exact totals and every newly promoted grade route must point to its individual evidence packet. No CI/paid GitHub Actions needed for this source/data ledger audit. No merge or release without explicit owner approval.

**Next:** CKPT-428 target 450/822 using **only** new currently awaiting 222 grade routes, while handling historical 200 in a separately adjudicated queue. Preserve edition flags and source countermodels. Offline source context and app functional QA are subsequent independent gates after question bank closure.
