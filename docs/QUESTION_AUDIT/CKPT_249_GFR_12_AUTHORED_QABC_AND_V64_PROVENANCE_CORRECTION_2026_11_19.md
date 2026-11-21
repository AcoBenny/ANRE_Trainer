# CKPT-249 | 12 întrebări noi și rectificare de proveniență V64 pentru alte 8 | 2026-11-19

## Rectificare explicită a clasificării anterioare
- La CKPT-248, 8 întrebări (G2-ELEC-056..062 și 064) au rămas etichetate `ORIGINAL_PROVENANCE_UNVERIFIED` deoarece atunci fusese inspectat doar V63. **Acea clasificare a fost incompletă.** V64 are dovada `TRAINER_AUTHORED_NOT_OFFICIAL_QUESTION_SAMPLE` și o aliniere exactă între Q+A+B+C+cheie pentru toate cele 8.
- Sursa V64 `caab11e8e0816766e651e211912aff9cc620ad4d`, V73 `c027d417a8e4e605c830b2016fb55b099b8d130b`, registrul V127 `ec1da2ed022c144ab4640adef14a166cf638bc33`. Sunt **8 rectificări ale metadatelor, 0 noi verificări focalizate din rectificare**. Evidența CKPT-248 a fost păstrată, iar fișa aceasta îl supersedează numai pentru proveniență.
- V64 identifică explicit 21 exemple autorate G2-ELEC-056..076; împreună cu cele 55 din V63, **76 exemple didactice neoficiale identificate explicit**, nu subiecte autentificate ANRE. V64 conține și 34 alte itemuri marcate `ELECTROTEHNICA_2024_XLSX_SOURCED`, dar această clasificare nu substituie baremul oficial.

## 12 analize QABC noi în lot

### G2-ELEC-065 | exemplu creat pentru trainer
- Original: Simbolul uzual pentru inductanță este:
- A: L
- B: R
- C: G
- Barem importat păstrat: A
- Model, A/B/C și contraexemple: A L este simbolul standard al inductanței; B R rezistența electrică, C G conductanța. Nu se confundă simbolul de mărime cu unitatea henry.
- Sursă de fizică: https://www.nist.gov/pml/special-publication-811/nist-guide-si-chapter-4-two-classes-si-units-and-si-prefixes
- Proveniență V64: TRAINER_AUTHORED_NOT_OFFICIAL_QUESTION_SAMPLE; QA independent NOT_RUN.

### G2-ELEC-066 | exemplu creat pentru trainer
- Original: Simbolul uzual pentru capacitate este:
- A: C
- B: L
- C: I
- Barem importat păstrat: A
- Model, A/B/C și contraexemple: A C simbolul uzual al capacității electrice; B L inductanță, C I curent electric. Unități distincte F, H și A.
- Sursă de fizică: https://www.nist.gov/pml/special-publication-811/nist-guide-si-chapter-4-two-classes-si-units-and-si-prefixes
- Proveniență V64: TRAINER_AUTHORED_NOT_OFFICIAL_QUESTION_SAMPLE; QA independent NOT_RUN.

### G2-ELEC-067 | exemplu creat pentru trainer
- Original: Într-un circuit rezistiv pur alimentat în curent alternativ sinusoidal, factorul de putere este: 
- A: 1
- B: 0
- C: -1 în orice situație
- Barem importat păstrat: A
- Model, A/B/C și contraexemple: A sarcină pur rezistivă sinusoidală are φ=0 și PF=cosφ=1; B=0 caracterizează element pur reactiv, C=-1 nu descrie consumator pasiv în convenția uzuală. Nu deduceți implicația inversă PF=1 ⇒ toate componentele rezistive.
- Sursă de fizică: https://openstax.org/books/university-physics-volume-2/pages/15-4-power-in-an-ac-circuit
- Proveniență V64: TRAINER_AUTHORED_NOT_OFFICIAL_QUESTION_SAMPLE; QA independent NOT_RUN.

### G2-ELEC-068 | exemplu creat pentru trainer
- Original: Într-un circuit inductiv pur, curentul este defazat față de tensiune astfel încât: 
- A: curentul rămâne în urmă față de tensiune cu 90°
- B: curentul este în fază cu tensiunea
- C: curentul este înainte cu 180°
- Barem importat păstrat: A
- Model, A/B/C și contraexemple: A pentru element L ideal curentul întârzie exact 90° față de U; B φ=0 pentru R ideal, C 180° nu este defazajul inductiv sinusoidal. Calificativul «pur» este esențial.
- Sursă de fizică: https://openstax.org/books/university-physics-volume-2/pages/15-2-simple-ac-circuits
- Proveniență V64: TRAINER_AUTHORED_NOT_OFFICIAL_QUESTION_SAMPLE; QA independent NOT_RUN.

### G2-ELEC-069 | exemplu creat pentru trainer
- Original: Într-un circuit capacitiv pur, curentul este: 
- A: înaintea tensiunii cu 90°
- B: în urmă cu 90°
- C: în fază cu tensiunea
- Barem importat păstrat: A
- Model, A/B/C și contraexemple: A curentul prin C ideal conduce tensiunea cu 90°; B este sensul invers de fazare, C zero este cazul rezistiv. Regim sinusoidal, fără rezistența parazită.
- Sursă de fizică: https://openstax.org/books/university-physics-volume-2/pages/15-2-simple-ac-circuits
- Proveniență V64: TRAINER_AUTHORED_NOT_OFFICIAL_QUESTION_SAMPLE; QA independent NOT_RUN.

### G2-ELEC-070 | exemplu creat pentru trainer
- Original: Într-un circuit serie R-L-C, rezonanța apare când: 
- A: reactanța inductivă și cea capacitivă se compensează
- B: rezistența devine infinită
- C: curentul devine obligatoriu zero
- Barem importat păstrat: A
- Model, A/B/C și contraexemple: A rezonanța RLC serie apare când XL=XC astfel reactanțele se compensează; B R nu devine infinit, C curentul nu este zero obligatoriu; la sursă cu U dat poate fi maxim la rezonanță.
- Sursă de fizică: https://openstax.org/books/university-physics-volume-2/pages/15-5-resonance-in-an-ac-circuit
- Proveniență V64: TRAINER_AUTHORED_NOT_OFFICIAL_QUESTION_SAMPLE; QA independent NOT_RUN.

### G2-ELEC-071 | exemplu creat pentru trainer
- Original: Într-un circuit serie R-L-C la rezonanță ideală, impedanța este determinată de: 
- A: rezistența R
- B: numai reactanța capacitivă
- C: suma XL + XC
- Barem importat păstrat: A
- Model, A/B/C și contraexemple: A impedanța RLC serie la rezonanță este Z=R în model ideal, deoarece XL−XC=0. B doar XC fals, C XL+XC nu se însumează ca mărimi pozitive în impedanța serie deoarece au semne opuse.
- Sursă de fizică: https://openstax.org/books/university-physics-volume-2/pages/15-5-resonance-in-an-ac-circuit
- Proveniență V64: TRAINER_AUTHORED_NOT_OFFICIAL_QUESTION_SAMPLE; QA independent NOT_RUN.

### G2-ELEC-072 | exemplu creat pentru trainer
- Original: Legea lui Ohm pentru o porțiune de circuit poate fi exprimată ca: 
- A: U = R·I
- B: U = R/I
- C: U = I/R
- Barem importat păstrat: A
- Model, A/B/C și contraexemple: A U=R·I la rezistor ohmic (și condiții termice constante). B R/I și C I/R nu au dimensiunile tensiunii. Materiale neohmice necesită relație U-I specifică.
- Sursă de fizică: https://openstax.org/books/university-physics-volume-2/pages/9-4-ohms-law
- Proveniență V64: TRAINER_AUTHORED_NOT_OFFICIAL_QUESTION_SAMPLE; QA independent NOT_RUN.

### G2-ELEC-073 | exemplu creat pentru trainer
- Original: Într-un circuit cu rezistențe în serie, curentul este: 
- A: același prin toate rezistențele
- B: zero prin prima rezistență
- C: diferit în mod obligatoriu prin fiecare rezistență
- Barem importat păstrat: A
- Model, A/B/C și contraexemple: A curentul este identic prin rezistoare în serie fără ramificații; B zero doar dacă întrerupere/alte condiții, C «diferit în mod obligatoriu» contrazice continuitatea sarcinii în model concentrat.
- Sursă de fizică: https://openstax.org/books/university-physics-volume-2/pages/10-2-resistors-in-series-and-parallel
- Proveniență V64: TRAINER_AUTHORED_NOT_OFFICIAL_QUESTION_SAMPLE; QA independent NOT_RUN.

### G2-ELEC-074 | exemplu creat pentru trainer
- Original: Într-o conexiune paralelă ideală, tensiunea pe ramuri este: 
- A: aceeași
- B: întotdeauna zero
- C: diferită în mod obligatoriu
- Barem importat păstrat: A
- Model, A/B/C și contraexemple: A două ramuri conectate la aceleași două noduri au aceeași tensiune; B «întotdeauna zero» fals dacă există alimentare, C «obligatoriu diferită» falsă. Ignorăm inductanțele parazite la regim rapid.
- Sursă de fizică: https://openstax.org/books/university-physics-volume-2/pages/10-2-resistors-in-series-and-parallel
- Proveniență V64: TRAINER_AUTHORED_NOT_OFFICIAL_QUESTION_SAMPLE; QA independent NOT_RUN.

### G2-ELEC-075 | exemplu creat pentru trainer
- Original: Puterea activă într-un circuit monofazat sinusoidal poate fi exprimată prin: 
- A: P = U·I·cosφ
- B: P = U/I
- C: P = U·I·sinφ în orice circuit
- Barem importat păstrat: A
- Model, A/B/C și contraexemple: A P=U_rms I_rms cosφ în monofazat sinusoidal. B U/I are unități de rezistență; C U I sinφ este Q (valoarea reactivei în convenții), nu P universal. Nu se generalizează direct la forme deformate.
- Sursă de fizică: https://openstax.org/books/university-physics-volume-2/pages/15-4-power-in-an-ac-circuit
- Proveniență V64: TRAINER_AUTHORED_NOT_OFFICIAL_QUESTION_SAMPLE; QA independent NOT_RUN.

### G2-ELEC-076 | exemplu creat pentru trainer
- Original: Unitatea de măsură SI pentru rezistența electrică este: 
- A: ohmul (Ω)
- B: faradul (F)
- C: henry-ul (H)
- Barem importat păstrat: A
- Model, A/B/C și contraexemple: A ohmul Ω unitate pentru rezistență electrică. B faradul F pentru capacitate și C henry H pentru inductanță; OHM nu trebuie confundată cu simbolul R al mărimii.
- Sursă de fizică: https://www.nist.gov/pml/special-publication-811/nist-guide-si-chapter-4-two-classes-si-units-and-si-prefixes
- Proveniență V64: TRAINER_AUTHORED_NOT_OFFICIAL_QUESTION_SAMPLE; QA independent NOT_RUN.

## Verificare structurală și limite
- 12 ID-uri au primit legături de verificare focalizată noi; 8 au primit **numai corecția de proveniență**, fără credit numeric dublu. 49 -> **37** fără evidență focalizată în registru.
- 822 ID-uri păstrate, exact aceeași ordine și chei importate. 802 rânduri byte-identice, 20 numai în coloanele documentare autorizate.
- Condiții speciale: G2-ELEC-067 PF=1 nu implică invers circuit numai rezistiv; G2-ELEC-070/071 regim serie și model ideal; G2-ELEC-072 legea Ohm limitată la rezistoare ohmice.
- 50 de rânduri CSV preexistente neuniforme au rămas exact intacte. Fără validare de sursă originală examen/barem, fără QA lingvistic și tehnic independent sau semnătură umană; approved_for_learning=NO pentru toate.
- PR #7 Draft, fără merge/release, fără modificări canonical QABC, HTML, APK sau main.
