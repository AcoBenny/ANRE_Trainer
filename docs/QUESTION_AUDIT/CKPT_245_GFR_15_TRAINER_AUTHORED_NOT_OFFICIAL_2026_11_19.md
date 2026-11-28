# CKPT-245 | GFR 15 întrebări didactice autorate pentru trainer, NU extrase oficiale ANRE | 2026-11-19

## Proveniență importantă
- V63 original `18029444b21ad0cd805d69f1ae9ea9e1747ee170` marchează explicit aceste 15 ca **TRAINER_AUTHORED_NOT_OFFICIAL_QUESTION_SAMPLE**, fapt constatat prin citirea directă a coloanei `provenance_type`. Nu se permite să fie prezentate drept întrebări oficiale de examen sau ca barem ANRE autentificat.
- 55 de rânduri V63 au această proveniență. Faptul că 136 rânduri V73 au ca `source_file` «Tematica și bibliografia ANRE ... 2023, pct. 1» nu dovedește proveniența oficială a întrebărilor; aceasta este tema din bibliografie, nu sursa originală a fiecărui item. Celelalte 81 necesită audit de proveniență separat.
- Bază inițială V123 `bed77e39b94f3add79132f9c8734b0885d4f68a1`, sursă canonică V73 `c027d417a8e4e605c830b2016fb55b099b8d130b`. 15 ID-uri au primit **fișe tehnice didactice**, nu certificat ANRE. Fără verificator independent.
- Referințe redeschise: OpenStax (Ohm, P=UI, rezistențe serie/paralel, componente CA) și NIST (unități SI); context fizic, definiții, contraexemple. Nu s-a reutilizat dovada ca examinare oficială.

### G2-ELEC-001
- **Proveniență explicită V63:** TRAINER_AUTHORED_NOT_OFFICIAL_QUESTION_SAMPLE (nu întrebare ANRE oficială verificată)
- **Întrebare:** Ce relație exprimă legea lui Ohm pentru un rezistor?
- A: U = R·I
- B: P = U·I
- C: Q = U/R
- **Barem importat păstrat:** A
- **Analiză A/B/C:** U=R·I pentru un rezistor ohmic în condiții fixe. B P=UI descrie puterea și nu relația cerută; C Q=U/R are dimensiunea unui curent dar simbolul Q este neadecvat pentru curent/sarcină. Condiție: rezistor liniar; nu atribui universal diodei.
- **Sursă tehnică deschisă:** https://openstax.org/books/university-physics-volume-2/pages/9-4-ohms-law
- **Ediție ANRE/cheie autentificată:** NOT_APPLICABLE_OFFICIAL_QUESTION_NOT_PROVEN; QA independent: NOT_RUN.

### G2-ELEC-002
- **Proveniență explicită V63:** TRAINER_AUTHORED_NOT_OFFICIAL_QUESTION_SAMPLE (nu întrebare ANRE oficială verificată)
- **Întrebare:** Unitatea SI pentru rezistența electrică este:
- A: ohmul (Ω)
- B: voltul (V)
- C: wattul (W)
- **Barem importat păstrat:** A
- **Analiză A/B/C:** A ohmul Ω măsoară rezistența R. B voltul V măsoară tensiunea; C wattul W puterea.
- **Sursă tehnică deschisă:** https://www.nist.gov/pml/owm/si-units-electric-current
- **Ediție ANRE/cheie autentificată:** NOT_APPLICABLE_OFFICIAL_QUESTION_NOT_PROVEN; QA independent: NOT_RUN.

### G2-ELEC-003
- **Proveniență explicită V63:** TRAINER_AUTHORED_NOT_OFFICIAL_QUESTION_SAMPLE (nu întrebare ANRE oficială verificată)
- **Întrebare:** Unitatea SI pentru intensitatea curentului electric este:
- A: amperul (A)
- B: ohmul (Ω)
- C: joule (J)
- **Barem importat păstrat:** A
- **Analiză A/B/C:** A amperul A măsoară intensitatea curentului. B ohmul Ω rezistența, C joule J energia.
- **Sursă tehnică deschisă:** https://www.nist.gov/pml/owm/si-units-electric-current
- **Ediție ANRE/cheie autentificată:** NOT_APPLICABLE_OFFICIAL_QUESTION_NOT_PROVEN; QA independent: NOT_RUN.

### G2-ELEC-004
- **Proveniență explicită V63:** TRAINER_AUTHORED_NOT_OFFICIAL_QUESTION_SAMPLE (nu întrebare ANRE oficială verificată)
- **Întrebare:** Unitatea SI pentru tensiunea electrică este:
- A: voltul (V)
- B: amperul (A)
- C: wattul (W)
- **Barem importat păstrat:** A
- **Analiză A/B/C:** A voltul V este unitatea diferenței de potențial electric. B A curent, C W putere.
- **Sursă tehnică deschisă:** https://www.nist.gov/pml/owm/si-units-electric-current
- **Ediție ANRE/cheie autentificată:** NOT_APPLICABLE_OFFICIAL_QUESTION_NOT_PROVEN; QA independent: NOT_RUN.

### G2-ELEC-005
- **Proveniență explicită V63:** TRAINER_AUTHORED_NOT_OFFICIAL_QUESTION_SAMPLE (nu întrebare ANRE oficială verificată)
- **Întrebare:** Puterea electrică activă într-un circuit de curent continuu se poate calcula cu:
- A: P = U·I
- B: P = U/I
- C: P = R/I
- **Barem importat păstrat:** A
- **Analiză A/B/C:** A P=UI pentru puterea la borne în curent continuu cu convenția de semn pasivă; B U/I are unitatea Ω; C R/I nu este relație dimensional coerentă pentru W. Pentru generatoare convenția de semn se inversează.
- **Sursă tehnică deschisă:** https://openstax.org/books/university-physics-volume-2/pages/9-5-electrical-energy-and-power
- **Ediție ANRE/cheie autentificată:** NOT_APPLICABLE_OFFICIAL_QUESTION_NOT_PROVEN; QA independent: NOT_RUN.

### G2-ELEC-006
- **Proveniență explicită V63:** TRAINER_AUTHORED_NOT_OFFICIAL_QUESTION_SAMPLE (nu întrebare ANRE oficială verificată)
- **Întrebare:** Energia electrică consumată într-un interval de timp se poate exprima prin:
- A: E = P·t
- B: E = P/t
- C: E = U/R
- **Barem importat păstrat:** A
- **Analiză A/B/C:** A E=P·t pentru P constantă sau Pmedie pe interval; B P/t nu reprezintă energie, C U/R reprezintă curent, nu energie. Pentru P variabilă E=∫P(t)dt, calificare obligatorie.
- **Sursă tehnică deschisă:** https://openstax.org/books/university-physics-volume-2/pages/9-5-electrical-energy-and-power
- **Ediție ANRE/cheie autentificată:** NOT_APPLICABLE_OFFICIAL_QUESTION_NOT_PROVEN; QA independent: NOT_RUN.

### G2-ELEC-007
- **Proveniență explicită V63:** TRAINER_AUTHORED_NOT_OFFICIAL_QUESTION_SAMPLE (nu întrebare ANRE oficială verificată)
- **Întrebare:** Pentru două rezistențe în serie, rezistența echivalentă este:
- A: R1 + R2
- B: R1·R2
- C: R1/R2
- **Barem importat păstrat:** A
- **Analiză A/B/C:** A Req=R1+R2 pentru rezistoare ideale în serie. B produs R1R2 are Ω², C raport R1/R2 este adimensional. Condiție: legare strict în serie fără ramificări.
- **Sursă tehnică deschisă:** https://openstax.org/books/university-physics-volume-2/pages/10-2-resistors-in-series-and-parallel
- **Ediție ANRE/cheie autentificată:** NOT_APPLICABLE_OFFICIAL_QUESTION_NOT_PROVEN; QA independent: NOT_RUN.

### G2-ELEC-008
- **Proveniență explicită V63:** TRAINER_AUTHORED_NOT_OFFICIAL_QUESTION_SAMPLE (nu întrebare ANRE oficială verificată)
- **Întrebare:** Pentru două rezistențe în paralel, rezistența echivalentă este:
- A: R1·R2/(R1+R2)
- B: R1+R2
- C: R1-R2
- **Barem importat păstrat:** A
- **Analiză A/B/C:** A Req=R1R2/(R1+R2) pentru R1,R2 finite pozitive în paralel. B suma R1+R2 este regula seriei, C diferența nu definește paralel.
- **Sursă tehnică deschisă:** https://openstax.org/books/university-physics-volume-2/pages/10-2-resistors-in-series-and-parallel
- **Ediție ANRE/cheie autentificată:** NOT_APPLICABLE_OFFICIAL_QUESTION_NOT_PROVEN; QA independent: NOT_RUN.

### G2-ELEC-009
- **Proveniență explicită V63:** TRAINER_AUTHORED_NOT_OFFICIAL_QUESTION_SAMPLE (nu întrebare ANRE oficială verificată)
- **Întrebare:** Într-un circuit serie, curentul prin elementele conectate în serie este:
- A: același
- B: zero în toate elementele
- C: diferit obligatoriu în fiecare element
- **Barem importat păstrat:** A
- **Analiză A/B/C:** A același curent prin elementele unei căi serie (fără noduri de ramificare). B zero nu este necesar dacă circuitul e închis și alimentat, C diferit obligatoriu e incompatibil cu conservarea sarcinii într-un model concentrat.
- **Sursă tehnică deschisă:** https://openstax.org/books/university-physics-volume-2/pages/10-2-resistors-in-series-and-parallel
- **Ediție ANRE/cheie autentificată:** NOT_APPLICABLE_OFFICIAL_QUESTION_NOT_PROVEN; QA independent: NOT_RUN.

### G2-ELEC-010
- **Proveniență explicită V63:** TRAINER_AUTHORED_NOT_OFFICIAL_QUESTION_SAMPLE (nu întrebare ANRE oficială verificată)
- **Întrebare:** Într-un circuit paralel, tensiunea pe ramurile conectate în paralel este:
- A: aceeași
- B: zero
- C: întotdeauna diferită
- **Barem importat păstrat:** A
- **Analiză A/B/C:** A aceeași diferență de potențial între două noduri comune pentru ramuri paralele. B zero doar într-un caz particular, C «întotdeauna diferită» contrazice conectarea paralelă ideală.
- **Sursă tehnică deschisă:** https://openstax.org/books/university-physics-volume-2/pages/10-2-resistors-in-series-and-parallel
- **Ediție ANRE/cheie autentificată:** NOT_APPLICABLE_OFFICIAL_QUESTION_NOT_PROVEN; QA independent: NOT_RUN.

### G2-ELEC-011
- **Proveniență explicită V63:** TRAINER_AUTHORED_NOT_OFFICIAL_QUESTION_SAMPLE (nu întrebare ANRE oficială verificată)
- **Întrebare:** Frecvența unei mărimi sinusoidale este măsurată în:
- A: hertzi (Hz)
- B: ohmi (Ω)
- C: farazi (F)
- **Barem importat păstrat:** A
- **Analiză A/B/C:** A hertz Hz=s⁻¹ este unitatea frecvenței. B Ω rezistență, C F capacitate.
- **Sursă tehnică deschisă:** https://www.nist.gov/pml/special-publication-811/nist-guide-si-chapter-4-two-classes-si-units-and-si-prefixes
- **Ediție ANRE/cheie autentificată:** NOT_APPLICABLE_OFFICIAL_QUESTION_NOT_PROVEN; QA independent: NOT_RUN.

### G2-ELEC-012
- **Proveniență explicită V63:** TRAINER_AUTHORED_NOT_OFFICIAL_QUESTION_SAMPLE (nu întrebare ANRE oficială verificată)
- **Întrebare:** Perioada T și frecvența f sunt legate prin:
- A: T = 1/f
- B: T = f
- C: T = f²
- **Barem importat păstrat:** A
- **Analiză A/B/C:** A T=1/f pentru f pozitiv și semnal periodic; B T=f nu are unități compatibile (secunde vs s⁻¹), C T=f² și mai nepotrivit. Sursa descrie frecvența ω și perioada, relația dedusă pentru sinusoide.
- **Sursă tehnică deschisă:** https://openstax.org/books/university-physics-volume-2/pages/15-2-simple-ac-circuits
- **Ediție ANRE/cheie autentificată:** NOT_APPLICABLE_OFFICIAL_QUESTION_NOT_PROVEN; QA independent: NOT_RUN.

### G2-ELEC-013
- **Proveniență explicită V63:** TRAINER_AUTHORED_NOT_OFFICIAL_QUESTION_SAMPLE (nu întrebare ANRE oficială verificată)
- **Întrebare:** Valoarea efectivă a unei tensiuni sinusoidale este folosită pentru:
- A: evaluarea efectului echivalent în regim energetic/termic
- B: determinarea directă a frecvenței
- C: înlocuirea rezistenței
- **Barem importat păstrat:** A
- **Analiză A/B/C:** A RMS oferă curent/tensiune echivalente energetic termic pentru rezistor; B frecvența nu se determină direct din RMS și C RMS nu înlocuiește rezistența. Temperatura/pierderea depind de rezistența specifică și de forma semnalului.
- **Sursă tehnică deschisă:** https://openstax.org/books/university-physics-volume-2/pages/15-2-simple-ac-circuits
- **Ediție ANRE/cheie autentificată:** NOT_APPLICABLE_OFFICIAL_QUESTION_NOT_PROVEN; QA independent: NOT_RUN.

### G2-ELEC-014
- **Proveniență explicită V63:** TRAINER_AUTHORED_NOT_OFFICIAL_QUESTION_SAMPLE (nu întrebare ANRE oficială verificată)
- **Întrebare:** Într-un circuit pur rezistiv de c.a., defazajul dintre tensiune și curent este:
- A: 0°
- B: 90°
- C: 180°
- **Barem importat păstrat:** A
- **Analiză A/B/C:** A într-un rezistor ideal R pur, tensiunea și curentul sunt în fază φ=0°, B 90° bobină sau condensator ideal, C 180° nu este regimul pasiv rezistiv cu referințe coerente.
- **Sursă tehnică deschisă:** https://openstax.org/books/university-physics-volume-2/pages/15-2-simple-ac-circuits
- **Ediție ANRE/cheie autentificată:** NOT_APPLICABLE_OFFICIAL_QUESTION_NOT_PROVEN; QA independent: NOT_RUN.

### G2-ELEC-015
- **Proveniență explicită V63:** TRAINER_AUTHORED_NOT_OFFICIAL_QUESTION_SAMPLE (nu întrebare ANRE oficială verificată)
- **Întrebare:** Într-o bobină ideală, curentul este în urmă față de tensiune cu:
- A: 90°
- B: 0°
- C: 180°
- **Barem importat păstrat:** A
- **Analiză A/B/C:** A în bobină ideală L curentul rămâne în urma tensiunii cu 90°. B 0° pur rezistiv, C 180° nu este defazajul inductorului sinusoidal. Diferențiați acest item explicit «bobină ideală» de ELE-128, doar «caracter inductiv».
- **Sursă tehnică deschisă:** https://openstax.org/books/university-physics-volume-2/pages/15-2-simple-ac-circuits
- **Ediție ANRE/cheie autentificată:** NOT_APPLICABLE_OFFICIAL_QUESTION_NOT_PROVEN; QA independent: NOT_RUN.

## QA, numărări și restricții
- 15 ID-uri G2 nou documentate: 109 -> **94** rămase fără verificare focalizată; 822 ID-uri originale intacte și cu aceeași ordine.
- Proveniența `TRAINER_AUTHORED_NOT_OFFICIAL_QUESTION_SAMPLE` este metadată distinctă de adevărul tehnic și de statutul cheii oficiale; nu există aprobare pentru învățare pentru niciun ID în acest lot.
- 50 rânduri CSV serializate neuniform în V123 rămân byte-identice. Originalele, baremurile, riscurile, HTML/APK/main, PR Draft/merge/release sunt nemodificate.
- Grade II G2-ELEC-001..015 nu sunt echivalente exact QABC cu alt item G1, deci nu se pretinde deduplicare sau reutilizare între grade.
