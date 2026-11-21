# CKPT-289 | Bounded GFR: exact Cs service-capacitance source and cross-grade key conflict | 2026-11-20

## Inputs and non-duplication
- Reopened actual user-supplied `ELECTROTEHNICA-09.2024-2(2).xlsx`, SHA-256 `2175d2c30ac8e2f149b28edd9ac00c233789bc0a3987ba779d6efed7afad920c`, exact source `Sheet1!A25:D25`.
- Exact QABC-0017 `Capacitatea de serviciu Cs a unei linii electrice aeriene simetrice, având capacităţile C12=C23=C31 =C şi neglijînd influenţa pământului, este:` with original **A `Cs=3 C`**, B `Cs=C/3`, C `Cs=C`.
- V149 original registry Git blob `ee2ac5536c78eb06a0461243be34c117e257188f` has grade members **G1-ELE-018=A** and **G2-ELEC-170=C** (two imported conflicting keys for **one exact QABC**). This conflict is **NOT NEW**: previously documented in CKPT-256 and V144 and researched at V80. Only new evidence here is a more directly worded teaching-source formula plus independent numerical derivation. Do not count as a newly discovered unit, new AI run or a resolved official key.

## Source-specific proof, not merely answer elimination
- Reopened public electrical-network notes `Retele-electrice-note-de-curs.pdf` at https://consultform.ro/anre/wp-content/uploads/2021/09/Retele-electrice-note-de-curs.pdf . The indexed/parsed course text at material around printed page numbers 35–37, after showing delta-to-star equivalence, states **`C_stea=3 C_ff`** and, in balanced positive-sequence operation, **`C_s^+=3 C_ff+C_p`** (labeled `(2.24)`). It separately states the zero-sequence identity **`C_s^0=C_p`**, a useful countermodel showing this is not a universal formula for every sequence regime.
- The original question explicitly says symmetric line, equal phase-to-phase capacitances `C_ff=C`, and **neglect Earth** `C_p≈0`. Under the standard balanced positive-sequence model, this gives `C_s=3C`: **option A** is affirmatively supported. The numerical statement does not require the candidate original exam key to be supplied.
- **Independent deterministic check actually executed:** set `C=1`, balanced complex potentials `V1=1∠0°, V2=1∠−120°, V3=1∠+120°`; `q1=C(V1−V2)+C(V1−V3)=3+0j`, giving `C_s=q1/V1=3`. Exactly confirms **3C**, not C or C/3, for those physical assumptions. No LLM/API usage or training claim.
- **Source QA limitation:** tool parsed the PDF text including equation and neighboring definitions, but the required remote screenshot of the applicable PDF page failed (cache miss) and a direct binary download failed. Therefore visual original-page verification is **NOT_DONE**. No claim that page typography/equation is visually authenticated from the official lecture copy. The file is a third-party didactic source, not an official ANRE scored key. It has no direct server-sha comparison to the user's Excel.
- Corroborating **unofficial** educational material also displays `Cs=C12+C23+C31=3C` at https://ro.scribd.com/presentation/633373385/Prezentare-examen-si-Intrebari-electrotehnica-2020; this is not separate original grading proof.

## Bidirectional A/B/C and possible countermodels
- Stem ↔ A: **SUPPORT** under symmetric positive-sequence and neglecting earth (course `C_s^+=3C_ff+C_p`).
- Stem ↔ B: **CONTRADICTED** for that model. B could only arise by a different meaning of symbol C or a different circuit; neither is supplied in the original.
- Stem ↔ C: **CONTRADICTED** for that model. A phase-to-phase partial C is not the same quantity as the equivalent single-phase service C in a balanced three-phase triangular-capacitance model.
- A vs B and A vs C: incompatible numeric results when C nonzero; B vs C: also incompatible. All three equal at degenerate C=0, which is not the meaningful line-capacitance scenario.
- Limitation: the **sequence/definition of service capacity** is a necessary interpretive scope; a zero-sequence or unsymmetrical operating state does not follow the same formula. This is not a reason to accept the imported G2 C without its own original authority.

## Provisional outcome and remaining gates
- `QABC-0017 / G1-ELE-018=A, G2-ELEC-170=C`: **SOURCE_SUPPORTED_A_UNDER_STATED_MODEL / CROSSGRADE_IMPORTED_KEY_CONFLICT_STILL_OPEN / EXACT_2026_ANRE_SCORING_NOT_AUTHENTICATED / QUALIFIED_INDEPENDENT_QA_NOT_RUN / VISUAL_PDF_NOT_VERIFIED / NO_LEARNER_APPROVAL**.
- **Never rewrite either stored imported key.** An exam-source key or edition-appropriate primary teaching material could change the intended context; preserve conflict before app use.
- The earlier 6 release-blocker classification stays unchanged: no double count. **No original QABC, grade keys, HTML, APK, app, main, merge or release changes. PR #7 and PR #13 remain Draft.**

## Next bounded triage
1. Continue in existing V149, prioritizing **remaining distinct strict blockers** QABC-0094, QABC-0143, QABC-0236, QABC-0362, QABC-0386, without redoing QABC-0017 arithmetic; every prior claim of a scored key must still be authenticated.
2. Prioritize authentic old-versus-current regulation/source scope, and stop attempting unchanged failing fetch paths; an unavailable PDF screenshot is a marked gate, not a reason to stall.
3. Maintain the exact 568 QABC/822 placement audit workqueue and keep all learner releases closed until qualified review and provenance.
