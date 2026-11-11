# V79 | ANRE Trainer | 18 P0 recontrol pe surse + noua coada 72 P0
**Data:** 2026-11-11. **Intrare:** V73 822-Q immutable, V74 71 P0, V76 verificare deterministă și 18 familii de enunțuri reciclate. **Ieșiri:** V77 (18 controlate cu sursă/raționament) și V78 (72 P0; nou `G1-NOR-042`).
## Verdicturi preliminare care cer acțiune, NU schimbări de barem automate
1. **8 candidați de altă literă susținuți de textul primar sau actualizările acestuia**:
   - G1-LEG-015 **A** (Legea 123/2012 art93(1) pct28 vs art92(1)).
   - G1-LEG-019 **B** (art93(1) pct3).
   - G1-LEG-020 **B** (Ordin 74/2014 art2 alin2–3, operator emitent).
   - G1-LEG-026 **B** (Legea 123/2012 art92(2)).
   - G1-LEG-048 **B** (Legea 123/2012 art57(2)).
   - G1-NOR-029 **C** (I7 art5.3.3.21: excepție locuințe 2,5m).
   - **G1-NOR-042 A** (I7 art5.2.4.6.1(a): 2 conductoare monofazat, indiferent de secțiune; original B citează greșit 25Cu/35Al față de prag I7 16Cu/25Al pentru polifazat). **NOU P0** față de V74.
   - G1-NOR-089 **B** (I7 art5.1.4.3.3, o culoare la faze cu marcaj la extremități).
2. **4 fără opțiune validă potrivit enunțului și sursei indicate:** G1-NOR-032 (art5.2.12.3.10: maximum 25m pe traseu drept, iar variantele sunt 10/15/20m; există și alternativa tub supradimensionat); G2-NOR-137/141/145 (se cere act de aprobare, dar opțiunile sunt indicative normative).
3. **2 duplicate cu afirmație universală demonstrabil falsă:** G1-ELE-029/G2-ELEC-178 conțin „numai” inducție electromagnetică; US DOE arată producerea AC și prin invertoare electronice DC/AC. Formula poate fi restrânsă la generatoare rotative, dar acest context lipsește.
4. **2 duplicate cu ambiguitate de mărime și unități:** G1-ELE-073/G2-ELEC-218. Fluxul câmpului E este q/epsilon0 (OpenStax §6.2), fluxul D=q_free (în condițiile lui Gauss pentru deplasare). Nu există o singură cheie fără clarificarea noțiunii „flux”.
5. **2 alte delimitări:** G1-NOR-041 conține „monofazat cu trei conductoare” în opțiunea B fără suport explicit în subpunctul I7 citat; G2-ELEC-290 numește `gamma` „adimensională” deși gamma [m^-1], conform Engineering LibreTexts. Ambele necesită revizia formulării.
## Surse primare/didactice inspectate
- Legea 123/2012, art57(2),92(1–2),93(1) pct3,28: https://legislatie.just.ro/Public/DetaliiDocument/300063
- Ordin 74/2014 art2(2–3): https://legislatie.just.ro/Public/DetaliiDocument/243569
- I7 art5.1.4.3.3;5.2.4.6.1;5.2.12.3.10;5.3.3.21: https://legislatie.just.ro/Public/DetaliiDocumentAfis/287132 ; https://legislatie.just.ro/Public/DetaliiDocument/286763
- US DOE: https://www.energy.gov/cmei/systems/solar-integration-inverters-and-grid-services-basics
- OpenStax University Physics 2 §6.2: https://openstax.org/books/university-physics-volume-2/pages/6-2-explaining-gausss-law
- Engineering LibreTexts (Steer), propagation constant dimensional analysis: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Fundamentals_of_Microwave_and_RF_Design_%28Steer%29/03%3A_Transmission_Lines/3.02%3A_Transmission_Line_Theory
- **Source URLs** identify the actual public pages used for the corresponding article or principle. Definitive application to a specific examination edition and all later 2026 amendments is not certified by these links alone. A few Portal URLs returned 502; fallback public indexed fragments need to be reconciled to a dated consolidated act before expert signoff.
## QA performed versus not performed
- **PASS data integrity:** V76 examined all 822 V73 records; no missing IDs, no option/key mismatch with `canonical_answer`, no approvals accidentally set; exactly 254 identical Q+ABC groups, two crossgrade key conflicts. 18 same-stem/different-option groups were reviewed as a separate risk (not auto-deduplicated).
- **PASS draft evidence control:** V77 18 distinct canonical ID+ABC copied without edits, each with source/reason/gate; V78 72 unique P0 IDs, prior 71 preserved, new G1-NOR-042 appended.
- **NOT RUN:** independent electrical/domain SME, human linguist, legal signoff, complete dated 2026 amendments review, source offline rights clearance, real Android test. 822/822 have *audit passports*, **0/822 independent approvals**; cannot certify app ready for learning.
- **No edits** to question bank, keys, HTML, APK, main or merge/release.
## Continuare fără duplicare
- Recontrol pe toate 72 P0 cu figuri și versiuni, apoi 229 P1 + P2, nivel de sursă exactă per ID și QA independent. Inspectează imediat V78 la reluare, nu V74; V73 rămâne baseline istoric și nu a fost rescris.
