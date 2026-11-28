# CKPT-003 | ANRE Trainer handoff V24 | 2026-11-09

## Identitate, starea proiectului
- Repository: `AcoBenny/ANRE_Trainer`
- **PR #7 Draft:** https://github.com/AcoBenny/ANRE_Trainer/pull/7
- Branch: `audit/anre-v8-priority-17-20261109` -> base `main`, **OPEN / DRAFT / NOT MERGED**. Fără release.
- Sursa canonică a aplicației: `app/src/main/assets/anre_trainer.html` blob GitHub `bc5b5a61954ba138cf83987bfc932eca517f3b21`, V10.29 conform jurnalului proiectului, 822 ID-uri distincte (414 Grad I, 408 Grad II).
- Politică utilizator: audit/documentație/checkpoint pe branch și PR Draft, **NU** modifica barem, enunț, variante, HTML, APK; **NU** merge/deploy/release fără aprobare explicită.
- Echipa/roluri: Romanian Language Reviewer (`anre-question-bank-qa`), Electrical Engineer + Normative Source Auditor (`anre-source-audit`), Data QA, QA independent și testare HTML/APK. **Rolurile au fost coordonate prin checklist-ul aceluiași model; nu există dovezi că au rulat subagenți independenți.** `INDEPENDENT_QA=NOT_RUN`.
- Keep memory budget: read THIS checkpoint, V23 full ledger and active risk files, NOT all chat/project; fetch exact canonical file only for requested IDs.

## Progres efectiv și limitele lui
- **822/822 ID-uri inventariate și atribuite unui nivel de screening în V23**. Nu înseamnă 822 răspunsuri validate.
- **381** întrebări: audit tehnic/lingvistic preliminar asistat de model (incl. 408 G2 except 77 și 50 G1).
- **77** G2 legislație/norme: verificare preliminară a provenienței, ediției, structurii și capcanelor, **nu** validare per articol.
- **204** G1 electrotehnică: identitate textuală exactă cu G2 plus opțiuni A/B/C, reutilizare doar a dovezilor preliminare. Nu aprobare nouă; 1 conflict în aceste 204.
- **160** G1 fără corespondent identic: 100 norme, 50 legislație, 10 electrotehnică, doar preflight lingvistic/surse.
- **0/822** aprobări QA independent și **0/822** complete pentru release, până la surse didactice exacte, legislație/standard actualizat, verdict tehnic independent și E2E HTML/APK.
- Deterministic: V23 ledger 822 înregistrări, V21 204 + V22 160 exact umplu cele 364 rămase după 458 examinate anterior; zero ID-uri duplicate în aceste fișiere, zero goluri. În QA un caz `G2-ELEC-292` avea JSON numeric A=1/B=0 vs șiruri CSV, *false-positive* de tip, nu incompatibilitate de date.

## Descoperiri/release blockers
1. V20: **254 grupe de duplicate exacte** (între Gradele 1/2); repetarea unor itemi între grade poate fi intenționată. Două perechi cu variante și enunț identice, dar răspuns semantic diferit:
   - `G1-ELE-018` A=Cs=3C versus `G2-ELEC-170` C=Cs=C. Definiție exactă `Cs` de investigat din manual/sursa autoritativă. Unele cursuri secundare derivă `Cs=3C` în ipoteze specifice, nu este adjudecare.
   - `G1-ELE-102` A=bară rece versus `G2-ELEC-245` C=ambele bare energizate/cupla în rezervă caldă. Depinde de schema și scopul operării. **Nu** corecta automat.
2. V13/V14: șase conflicte între tracker V9 și canonical V10.29: `G1-LEG-024,028,032,034,048` și `G2-ELEC-170`. Audit lingvistic a evidențiat modificatori cu sens juridic. Unele texte normative favorizează tracker, dar fără semnătura independentă; toate rămân în carantină.
3. V24 verificare XLSX originale: `LEGISLATIE-GR.-1-05.2023 (1).xlsx` col I are **I31=1,I34=2,I35=3,I46=4,I54=5**, adnotări numerice în secvență, **NU** chei A/B/C. G1-LEG-032/034/048 nu au valoare în I. `ELECTROTEHNICA-09.2024-2.xlsx` rândul 25 are variante Cs dar **nu** o cheie independentă în A:D. Nu interpreta automat aceste adnotări.
4. G2-ELEC-358 susceptanță `-X/(R²+X²)` în circuit mixt, nu generic invers X; G2-ELEC-392 diferență între flux E și flux D; G2-ELEC-381 cosφ=1 nu implică numai rezistoare; `G1-ELE-028` și `G2-ELEC-177` fac trimitere la scheme absente learner-facing; blochează aprobarea.
5. Barem predictibil: **77/77** din subsetul G2 Leg+Norm și **50/50** G2-ELEC-001..050 au cheia A; testare pedagogică compromisă prin simpla repetare A. Necesită modificări de prezentare aprobate separat.
6. Multe întrebări I7 trebuie verificate în lumina Ordinului **959/2023** privind actualizarea I7-2011; tarifele ANRE sunt dependente de dată; întrebările istorice nu echivalează cu norme curente.
7. `anre-question-bank-qa` și `anre-source-audit` conțin reguli, dar executantul QA independent și testarea fizică HTML/APK nu au fost executate. `VERIFICAT TEHNIC` în HTML istoric nu înseamnă aprobare curentă.

## Dovezile de pornire în PR #7
- `docs/QUESTION_AUDIT/ANRE_LINGUISTIC_REVIEW_GATE.md`
- `docs/QUESTION_AUDIT/V13_SIX_KEY_CONFLICTS.csv`
- `docs/QUESTION_AUDIT/V14_TRAP_REVIEW_REPORT.md`
- `docs/QUESTION_AUDIT/V15_G2_ELEC_328_377_LING_TECH_SCREEN.csv`, `V15_G2_ELEC_328_377_REPORT.md`
- `docs/QUESTION_AUDIT/V16_G2_ELEC_378_408_LING_TECH_SCREEN.csv`, `V16_G2_ELEC_378_408_REPORT.md`
- `docs/QUESTION_AUDIT/V17_G2_LEG_NORM_77_LINGUISTIC_VERSION_PREFLIGHT.csv`, `V17_G2_LEG_NORM_77_REPORT.md`
- `docs/QUESTION_AUDIT/V18_G2_EARLY_33_SCREEN.csv`, `V18_G2_EARLY_33_REPORT.md`
- `docs/QUESTION_AUDIT/V19_G1_ELEC_FIRST50_LING_TECH_SCREEN.csv`, `V19_G1_ELEC_FIRST50_REPORT.md`
- `docs/QUESTION_AUDIT/V20_ALL_822_RECONCILED_QA_LEDGER.csv`, `V20_254_EXACT_DUPLICATE_GROUPS.csv`
- `docs/QUESTION_AUDIT/V21_G1_204_CROSSGRADE_PARITY.csv`, `V21_G1_CROSSGRADE_PARITY_REPORT.md`
- `docs/QUESTION_AUDIT/V22_G1_160_NONMATCH_LING_SOURCE_PREFLIGHT.csv`, `V22_G1_160_NONMATCH_REPORT.md`
- `docs/QUESTION_AUDIT/V23_ALL_822_FULL_COVERAGE_CHECKPOINT.csv`, `V23_FULL_COVERAGE_QA_GATE_REPORT.md`
- `docs/QUESTION_AUDIT/V24_ORIGINAL_XLSX_KEY_PROVENANCE_CHECK.md`
- `PROJECT_JOURNEY.md` to be updated with this checkpoint.

## Următoarea muncă, fără loop cu utilizatorul
1. Auditează întâi sursa primară, ediția și definiția `Cs` și schema celor două bare, plus 6 conflicte V13; verifică dacă întrebarea e capcană lingvistică validă ori barem inconsistent.
2. Prioritizează cele 100 G1 norme (I7 actualizat), siguranța electrica, condiții ascunse, scheme lipsă; mapează **paragraf didactic exact, ediție, pagină și link offline permis** pentru fiecare.
3. Fă QA independent real când un executant separat este disponibil; până atunci `NOT_RUN`. Rulează teste HTML/APK offline numai când accesul la runtime o permite; păstrează CI/probe.
4. Continuă în loturi cu dovezi verificabile, actualizări PROJECT_JOURNEY/PR Draft, fără merge și fără a altera baremul/aplicația.
5. Dacă conversația se apropie de limita de context, pregătește checkpoint nou înainte să fie atinsă limita, cu progres, blocaje, PR și next actions.

**Această etapă este completă ca TRIERE / INVENTAR; NU este completă ca validare tehnică și didactică finală.**
