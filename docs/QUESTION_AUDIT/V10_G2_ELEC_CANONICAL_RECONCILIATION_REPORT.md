# ANRE Trainer | V10 canonical reconciliation: G2-ELEC-178–227

Date: 2026-11-09. Branch `audit/anre-v8-priority-17-20261109`; PR #7 Draft. Compare actual embedded `const DATA` JSON arrays extracted from older user-library `ANRE_Trainer_FINAL_EVIDENCE_V10_4.html` (822 entries) and GitHub `app/src/main/assets/anre_trainer.html` blob `bc5b5a61954ba138cf83987bfc932eca517f3b21` (822 entries, V10.29 designated by project history).

- **50/50 identical** for fields `Intrebare,A,B,C,Raspuns,Rand_sursa,Sursa,Categorie,Versiune`, JSON decoded exact equality for corresponding ID. No semantic normalization or fuzzy matching.
- **50/50** canonical answers/source rows/source labels match V9 822-question backlog.
- Discrepant version fields: 0. Backlog mismatches: 0. Overall V9 tracker discrepancies across 822: 6; see caution below for expected special source metadata.
- QA run: deterministic exact field comparison. **This does not validate answer correctness, normative editions, source paragraph, UI runtime or independent electrical review**. Existing V10 model screening remains provisional; the prior `NOT_VERIFIED_V10_4_LEGACY_TEXT` status is superseded by this reconciliation (do not erase audit history).
- Reproducibility: extract JSON between `const DATA=` and next `];` in each HTML, map by `ID`, assert 822 and unique ID, compare the nine named fields for 178..227; compare `Raspuns/Rand_sursa/Sursa` with the V9 backlog rows.
- Source fidelity control: canonic blob fetched directly from GitHub content address. **No source document was republished or altered.**

Gate for V10 content: linked didactic paragraphs and real independent SME review still NOT_RUN/NOT_VERIFIED; no modification to answers or app; no merge.
