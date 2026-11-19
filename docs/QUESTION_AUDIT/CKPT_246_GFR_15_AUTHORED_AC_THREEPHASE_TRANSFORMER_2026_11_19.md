# CKPT-246 | 15 întrebări create pentru trainer: CA, trifazat și transformatoare | 2026-11-19

## Clasificare corectă a provenienței
- 15 itemi G2-ELEC în V63 sunt `TRAINER_AUTHORED_NOT_OFFICIAL_QUESTION_SAMPLE`, nu întrebări ANRE autentificate. Dovada: V63 blob `18029444b21ad0cd805d69f1ae9ea9e1747ee170`; original V73 `c027d417a8e4e605c830b2016fb55b099b8d130b`.
- Bază V124 blob `c246440d2144fca872224f3cf438620b993c031c`. Source research via OpenStax, Monolithic Power Systems, NIST; verificare conceptuală a formulării, A/B/C și a ipotezelor specifice; NU autentificare cheie oficială.
- Toate cele 15 răspunsuri importate A au rămas intacte. Sunt notițe didactice compatibile cu modelele indicate, nu QA independent de la un examinator certificat.

### G2-ELEC-016 / probă de lecție, nu item oficial ANRE
- **Enunț:** Într-un condensator ideal, curentul este înaintea tensiunii cu:
- A: 90°
- B: 0°
- C: 180°
- **Răspuns importat nemodificat:** A
- **Analiză și contraexemple:** Într-un condensator ideal și sinusoidal, curentul precedă tensiunea cu π/2, deci A. B 0° este R pur, C 180° nu descrie elementul capacitiv. Condiție: capacitate ideală sinusoidală.
- **Sursă tehnică recitită:** https://openstax.org/books/university-physics-volume-2/pages/15-2-simple-ac-circuits
- Proveniență V63: TRAINER_AUTHORED_NOT_OFFICIAL_QUESTION_SAMPLE. QA independent NOT_RUN.

### G2-ELEC-017 / probă de lecție, nu item oficial ANRE
- **Enunț:** Reactanța inductivă a unei bobine ideale este:
- A: XL = 2πfL
- B: XL = 1/(2πfL)
- C: XL = R/I
- **Răspuns importat nemodificat:** A
- **Analiză și contraexemple:** A: XL=ωL=2πfL. B este formula reactanței capacitive dacă L ar fi C, C R/I nu are dimensiunea corectă. Bobină liniară și frecvență definită.
- **Sursă tehnică recitită:** https://openstax.org/books/university-physics-volume-2/pages/15-2-simple-ac-circuits
- Proveniență V63: TRAINER_AUTHORED_NOT_OFFICIAL_QUESTION_SAMPLE. QA independent NOT_RUN.

### G2-ELEC-018 / probă de lecție, nu item oficial ANRE
- **Enunț:** Reactanța capacitivă este:
- A: XC = 1/(2πfC)
- B: XC = 2πfC
- C: XC = R·C
- **Răspuns importat nemodificat:** A
- **Analiză și contraexemple:** A: |XC|=1/(ωC)=1/(2πfC) pentru f>0. B 2πfC reprezintă susceptanță capacitivă (S), nu reactanță (Ω). C R·C are dimensiune de timp (s), nu Ω. Semnul impedanței este -jXC.
- **Sursă tehnică recitită:** https://openstax.org/books/university-physics-volume-2/pages/15-2-simple-ac-circuits
- Proveniență V63: TRAINER_AUTHORED_NOT_OFFICIAL_QUESTION_SAMPLE. QA independent NOT_RUN.

### G2-ELEC-019 / probă de lecție, nu item oficial ANRE
- **Enunț:** Puterea aparentă într-un circuit monofazat este:
- A: S = U·I
- B: S = U/I
- C: S = R·I
- **Răspuns importat nemodificat:** A
- **Analiză și contraexemple:** A S=Urms·Irms în circuit monofazat, în VA. B U/I exprimă ohmi, C R·I tensiune, nu putere. Necesită valori efective, nu orice produse arbitrare de valori instantanee.
- **Sursă tehnică recitită:** https://openstax.org/books/college-physics-2e/pages/23-section-summary
- Proveniență V63: TRAINER_AUTHORED_NOT_OFFICIAL_QUESTION_SAMPLE. QA independent NOT_RUN.

### G2-ELEC-020 / probă de lecție, nu item oficial ANRE
- **Enunț:** Unitatea puterii aparente este:
- A: VA
- B: W
- C: var
- **Răspuns importat nemodificat:** A
- **Analiză și contraexemple:** A volt-amperul VA pentru puterea aparentă. B W este putere activă, C var este putere reactivă. Nomenclatura specială VA pentru mărimea aparentă.
- **Sursă tehnică recitită:** https://www.nist.gov/pml/special-publication-811/nist-guide-si-chapter-4-two-classes-si-units-and-si-prefixes
- Proveniență V63: TRAINER_AUTHORED_NOT_OFFICIAL_QUESTION_SAMPLE. QA independent NOT_RUN.

### G2-ELEC-021 / probă de lecție, nu item oficial ANRE
- **Enunț:** Puterea reactivă se exprimă în:
- A: var
- B: W
- C: VAh
- **Răspuns importat nemodificat:** A
- **Analiză și contraexemple:** A var (volt-amper reactiv) pentru putere reactivă; B W pentru putere activă, C VAh unitate de energie aparentă, nu putere. Domeniu sinusoidal periodic.
- **Sursă tehnică recitită:** https://www.nist.gov/pml/special-publication-811/nist-guide-si-chapter-4-two-classes-si-units-and-si-prefixes
- Proveniență V63: TRAINER_AUTHORED_NOT_OFFICIAL_QUESTION_SAMPLE. QA independent NOT_RUN.

### G2-ELEC-022 / probă de lecție, nu item oficial ANRE
- **Enunț:** Factorul de putere în regim sinusoidal este:
- A: cos φ
- B: sin φ
- C: tan φ
- **Răspuns importat nemodificat:** A
- **Analiză și contraexemple:** A cosφ este factorul de putere în regim sinusoidal. B sinφ corespunde componentei reactive normalizate, C tanφ raportului Q/P. Pentru forme deformate, factorul de putere global poate diferi de cosφ.
- **Sursă tehnică recitită:** https://openstax.org/books/college-physics-2e/pages/23-section-summary
- Proveniență V63: TRAINER_AUTHORED_NOT_OFFICIAL_QUESTION_SAMPLE. QA independent NOT_RUN.

### G2-ELEC-023 / probă de lecție, nu item oficial ANRE
- **Enunț:** Pentru o sarcină pur rezistivă, factorul de putere este:
- A: 1
- B: 0
- C: -1
- **Răspuns importat nemodificat:** A
- **Analiză și contraexemple:** A factor de putere 1 într-o sarcină pur rezistivă ideală: φ=0. B 0 în sarcină ideal reactivă, C -1 nu corespunde acestei convenții de consum. Nu trebuie inversată implicația: PF=1 nu implică circuit exclusiv rezistiv.
- **Sursă tehnică recitită:** https://openstax.org/books/college-physics-2e/pages/23-section-summary
- Proveniență V63: TRAINER_AUTHORED_NOT_OFFICIAL_QUESTION_SAMPLE. QA independent NOT_RUN.

### G2-ELEC-024 / probă de lecție, nu item oficial ANRE
- **Enunț:** Într-un sistem trifazat echilibrat, suma vectorială a curenților de fază este:
- A: zero
- B: egală cu curentul de linie
- C: întotdeauna 3 A
- **Răspuns importat nemodificat:** A
- **Analiză și contraexemple:** A Ia+Ib+Ic=0 pentru trei curenți echilibrați cu module egale și defazaj ±120°. B curentul de linie nu este suma fasorială, C «3 A» dimensional și fizic arbitrar.
- **Sursă tehnică recitită:** https://www.monolithicpower.com/en/learning/mpscholar/ac-power/theory-and-analysis/three-phase-systems-and-applications
- Proveniență V63: TRAINER_AUTHORED_NOT_OFFICIAL_QUESTION_SAMPLE. QA independent NOT_RUN.

### G2-ELEC-025 / probă de lecție, nu item oficial ANRE
- **Enunț:** Pentru un sistem trifazat echilibrat, puterea activă se poate calcula cu:
- A: P = √3·UL·IL·cosφ
- B: P = UL/IL
- C: P = 3·UL·IL
- **Răspuns importat nemodificat:** A
- **Analiză și contraexemple:** A P=√3·U_L·I_L·cosφ pentru sistem trifazat sinusoidal echilibrat. B U_L/I_L este impedanță, C 3U_LI_L fără cosφ și factor geometric corect nu este formula totală generală.
- **Sursă tehnică recitită:** https://www.monolithicpower.com/en/learning/mpscholar/ac-power/theory-and-analysis/three-phase-systems-and-applications
- Proveniență V63: TRAINER_AUTHORED_NOT_OFFICIAL_QUESTION_SAMPLE. QA independent NOT_RUN.

### G2-ELEC-026 / probă de lecție, nu item oficial ANRE
- **Enunț:** În conexiunea stea, tensiunea de linie este:
- A: √3 ori tensiunea de fază
- B: egală cu zero
- C: jumătate din tensiunea de fază
- **Răspuns importat nemodificat:** A
- **Analiză și contraexemple:** A la stea trifazată simetrică U_linie=√3·U_fază. B zero contrazice alimentarea, C jumătate contrazice geometria fazorială. Necesită fazori simetrici.
- **Sursă tehnică recitită:** https://www.monolithicpower.com/en/learning/mpscholar/ac-power/theory-and-analysis/three-phase-systems-and-applications
- Proveniență V63: TRAINER_AUTHORED_NOT_OFFICIAL_QUESTION_SAMPLE. QA independent NOT_RUN.

### G2-ELEC-027 / probă de lecție, nu item oficial ANRE
- **Enunț:** În conexiunea triunghi, tensiunea de linie este:
- A: egală cu tensiunea de fază
- B: √3 ori tensiunea de fază
- C: jumătate din tensiunea de fază
- **Răspuns importat nemodificat:** A
- **Analiză și contraexemple:** A în triunghi fiecare ramură este conectată între două linii, deci U_linie=U_fază. B √3 este pentru stea, C 1/2 fals. Relația tensiunilor depinde de topologie; nu presupune automat curenți echilibrați.
- **Sursă tehnică recitită:** https://www.monolithicpower.com/en/learning/mpscholar/ac-power/theory-and-analysis/three-phase-systems-and-applications
- Proveniență V63: TRAINER_AUTHORED_NOT_OFFICIAL_QUESTION_SAMPLE. QA independent NOT_RUN.

### G2-ELEC-028 / probă de lecție, nu item oficial ANRE
- **Enunț:** Transformatorul electric funcționează pe baza:
- A: inducției electromagnetice
- B: efectului fotoelectric
- C: efectului Hall exclusiv
- **Răspuns importat nemodificat:** A
- **Analiză și contraexemple:** A transformatorul electromagnet clasic utilizează inducția prin flux magnetic variabil și două înfășurări. B efect fotoelectric și C efect Hall nu fundamentează transformatorul de putere.
- **Sursă tehnică recitită:** https://openstax.org/books/university-physics-volume-2/pages/15-6-transformers
- Proveniență V63: TRAINER_AUTHORED_NOT_OFFICIAL_QUESTION_SAMPLE. QA independent NOT_RUN.

### G2-ELEC-029 / probă de lecție, nu item oficial ANRE
- **Enunț:** Într-un transformator ideal, raportul tensiunilor este egal cu raportul:
- A: numărului de spire
- B: rezistențelor de sarcină
- C: frecvențelor
- **Răspuns importat nemodificat:** A
- **Analiză și contraexemple:** A pentru transformator ideal Vs/Vp=Ns/Np din legea inducției, cu același flux prin înfășurări. B raportul rezistențelor de sarcină și C raportul frecvențelor nu determină acest raport de transformare. În realitate există abateri la sarcină.
- **Sursă tehnică recitită:** https://openstax.org/books/university-physics-volume-2/pages/15-6-transformers
- Proveniență V63: TRAINER_AUTHORED_NOT_OFFICIAL_QUESTION_SAMPLE. QA independent NOT_RUN.

### G2-ELEC-031 / probă de lecție, nu item oficial ANRE
- **Enunț:** Motorul electric transformă în principal:
- A: energia electrică în energie mecanică
- B: energia mecanică în energie electrică exclusiv
- C: energia termică în energie electrică
- **Răspuns importat nemodificat:** A
- **Analiză și contraexemple:** A motorul convertește în principal energie electrică în lucru mecanic la arbore. B reprezintă direcția generică a unui generator și are «exclusiv» fals pentru motor, C nu este conversia principală. Mașinile electrice reversibile pot funcționa în regim de frânare/generator, deci «în principal» contează.
- **Sursă tehnică recitită:** https://openstax.org/books/university-physics-volume-2/pages/13-1-faradays-law
- Proveniență V63: TRAINER_AUTHORED_NOT_OFFICIAL_QUESTION_SAMPLE. QA independent NOT_RUN.

## Integritate și restricții
- 15/15 ID-uri legate la noile fișe, 94 -> **79** fără verificare focalizată în registru. Original 822 ID-uri și ordinea neschimbate; fără modificare a întrebărilor, alternativelor, baremurilor sau priorităților.
- Atenție G2-ELEC-018: reactanța capacitivă este mărimea |X_C| în A; semnul impedanței complexe e separat. G2-ELEC-023: PF=1 pentru R pur, dar implicația inversă este falsă.
- Proveniența autentică de examen rămâne neverificată pentru itemii anexați bibliografiei ANRE; nu-i prezenta ca subiecte oficiale.
- 50 rânduri preexistente cu CSV neuniform au rămas byte-identice, niciun conținut de sursă originală nu a fost suprascris.
- 0 aprobări pentru învățare; independent technical/linguistic QA NOT_RUN, PR #7 Draft/unmerged, fără merge/release sau modificare HTML/APK.
