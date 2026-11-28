# CKPT-248 | 15 G2 questions: protection, meters and conceptual physics with two provenance levels | 2026-11-19

## No authenticity inflation
- 7/15 (G2-ELEC-047..050, 053..055) have *explicit* V63 flag `TRAINER_AUTHORED_NOT_OFFICIAL_QUESTION_SAMPLE`, V63 blob `18029444b21ad0cd805d69f1ae9ea9e1747ee170`.
- 8/15 (G2-ELEC-056..062, 064) are **not included in V63**. V73 has `source_file` «Tematica ... ANRE 2023», but this is a topic/bibliography label and does NOT establish exam-question authorship or official status. Their provenance stays `ORIGINAL_PROVENANCE_UNVERIFIED` pending exact source.
- V73 canonical blob `c027d417a8e4e605c830b2016fb55b099b8d130b`, V126 baseline `1a2c5efe89cbf39582fa73f20bd5e1e5e9e9bbed`. Source guidance includes Schneider Electric, Eaton electrical safety, Fluke, NI, and OpenStax. These are technical corroboration, not official exam answer keys.

### G2-ELEC-047
- **Întrebarea:** Scopul principal al unei protecții la supracurent este:
- A: limitarea efectelor curenților excesivi
- B: creșterea tensiunii de alimentare
- C: mărirea rezistenței sarcinii
- **Cheia importată nemodificată:** A
- **Proveniență:** V63 explicit TRAINER_AUTHORED_NOT_OFFICIAL_QUESTION_SAMPLE.
- **Verificare model și A/B/C:** A limitează efectele supracurenților prin declanșarea/întreruperea alimentării potrivit curbei și coordonării protecțiilor. B creșterea tensiunii nu este funcția dispozitivului, C schimbarea rezistenței sarcinii nu constituie scopul. Limitarea curentului instantaneu nu este garantată de orice protecție.
- **Sursă tehnică candidat:** https://www.se.com/sg/en/product-subcategory/4670-overcurrent-protection/. Ediție ANRE2026 și QA independent neverificate.

### G2-ELEC-048
- **Întrebarea:** Un întreruptor automat poate asigura protecția la:
- A: suprasarcină și scurtcircuit, în funcție de caracteristicile aparatului
- B: doar iluminat natural
- C: doar lipsa fazei în orice situație
- **Cheia importată nemodificată:** A
- **Proveniență:** V63 explicit TRAINER_AUTHORED_NOT_OFFICIAL_QUESTION_SAMPLE.
- **Verificare model și A/B/C:** A întreruptorul automat adecvat poate proteja la suprasarcină și scurtcircuit în funcție de declanșatoare și setări. B iluminatul natural este irelevant, C lipsa de fază nu e detectată universal de orice întreruptor. Nu se implică automat protecție diferențială.
- **Sursă tehnică candidat:** https://www.electrical-installation.org/enwiki/Fundamental_characteristics_of_a_circuit-breaker. Ediție ANRE2026 și QA independent neverificate.

### G2-ELEC-049
- **Întrebarea:** Un dispozitiv diferențial detectează în principal:
- A: un dezechilibru al curenților care indică un curent rezidual
- B: doar supratensiunea
- C: doar frecvența rețelei
- **Cheia importată nemodificată:** A
- **Proveniență:** V63 explicit TRAINER_AUTHORED_NOT_OFFICIAL_QUESTION_SAMPLE.
- **Verificare model și A/B/C:** A RCD compară vectorial curenții prin conductoarele active și detectează curent rezidual. B supratensiunea și C frecvența nu sunt funcțiile primare. Nu se confundă RCCB cu RCBO; RCCB de regulă nu oferă protecție de supracurent.
- **Sursă tehnică candidat:** https://www.se.com/nz/en/faqs/FAQ000210095/. Ediție ANRE2026 și QA independent neverificate.

### G2-ELEC-050
- **Întrebarea:** Împământarea de protecție are ca scop principal:
- A: reducerea riscului de electrocutare prin asigurarea unei căi de defect și a condițiilor de declanșare a protecției
- B: creșterea consumului
- C: eliminarea completă a tuturor defectelor
- **Cheia importată nemodificată:** A
- **Proveniență:** V63 explicit TRAINER_AUTHORED_NOT_OFFICIAL_QUESTION_SAMPLE.
- **Verificare model și A/B/C:** A împământarea de protecție și legarea la PE contribuie la reducerea tensiunilor de atingere și la funcționarea deconectării automate în sistemul potrivit. B creșterea consumului nu este scop; C nu elimină orice defect. Funcționarea exactă diferă între TN, TT și IT; nu e suficient doar electrodul.
- **Sursă tehnică candidat:** https://www.eaton.com/content/dam/eaton/markets/buildings/how-we-drive-building-efficiency-and-safety/eaton-guide-fundamentals-of-electrical-safety-in-lv-installations-buildings-en-us.pdf. Ediție ANRE2026 și QA independent neverificate.

### G2-ELEC-053
- **Întrebarea:** Puterea activă într-un circuit rezistiv este transformată în principal în:
- A: energie termică
- B: energie magnetică stocată permanent
- C: energie chimică în orice rezistor
- **Cheia importată nemodificată:** A
- **Proveniență:** V63 explicit TRAINER_AUTHORED_NOT_OFFICIAL_QUESTION_SAMPLE.
- **Verificare model și A/B/C:** A în rezistor, puterea activă P=I²R este disipată preponderent termic; B stocarea magnetică permanentă și C transformarea chimică în orice rezistor sunt false. Nu toate componentele rezistive sunt încălzitoare utile, dar căldura este conversia principală.
- **Sursă tehnică candidat:** https://openstax.org/books/university-physics-volume-2/pages/9-5-electrical-energy-and-power. Ediție ANRE2026 și QA independent neverificate.

### G2-ELEC-054
- **Întrebarea:** Într-un circuit ideal pur inductiv, puterea activă medie este:
- A: zero
- B: egală cu puterea aparentă
- C: întotdeauna maximă
- **Cheia importată nemodificată:** A
- **Proveniență:** V63 explicit TRAINER_AUTHORED_NOT_OFFICIAL_QUESTION_SAMPLE.
- **Verificare model și A/B/C:** A pentru inductor pur ideal curentul întârzie cu 90°, cosφ=0 și puterea activă medie P=UIcosφ=0. B S este pozitivă la valori nenule, C puterea activă nu este maximă. Energie alternantă stocată și returnată, nu consum activ net.
- **Sursă tehnică candidat:** https://openstax.org/books/university-physics-volume-2/pages/15-4-power-in-an-ac-circuit. Ediție ANRE2026 și QA independent neverificate.

### G2-ELEC-055
- **Întrebarea:** Într-un circuit ideal pur capacitiv, puterea activă medie este:
- A: zero
- B: egală cu puterea aparentă
- C: egală cu energia stocată
- **Cheia importată nemodificată:** A
- **Proveniență:** V63 explicit TRAINER_AUTHORED_NOT_OFFICIAL_QUESTION_SAMPLE.
- **Verificare model și A/B/C:** A pentru condensator pur ideal curentul precedă tensiunea cu 90°, deci P medie=0. B S este diferită de zero pentru curent/tensiune nenule și C are unități de energie, nu putere. Dielectric real cu pierderi poate avea P>0.
- **Sursă tehnică candidat:** https://openstax.org/books/university-physics-volume-2/pages/15-4-power-in-an-ac-circuit. Ediție ANRE2026 și QA independent neverificate.

### G2-ELEC-056
- **Întrebarea:** Într-un sistem trifazat echilibrat, conductorul de nul poate avea curent:
- A: nul, pentru sarcină perfect echilibrată și condițiile corespunzătoare
- B: întotdeauna egal cu curentul de fază
- C: întotdeauna dublu față de curentul de fază
- **Cheia importată nemodificată:** A
- **Proveniență:** V73 indică domeniul tematic ANRE 2023, DAR proveniența întrebării originale nu este confirmată.
- **Verificare model și A/B/C:** A într-un sistem trifazat sinusoidal perfect echilibrat curentul conductorului neutru poate fi zero (suma fasorială curenți =0). B și C «întotdeauna» sunt false. Armonicile triplen și dezechilibrele pot produce curent în nul, chiar dacă fazele fundamentale sunt apropiate.
- **Sursă tehnică candidat:** https://www.monolithicpower.com/en/learning/mpscholar/ac-power/theory-and-analysis/three-phase-systems-and-applications. Ediție ANRE2026 și QA independent neverificate.

### G2-ELEC-057
- **Întrebarea:** Eficiența/randamentul unui echipament este raportul dintre:
- A: puterea utilă și puterea absorbită
- B: puterea absorbită și pierderi
- C: tensiune și curent
- **Cheia importată nemodificată:** A
- **Proveniență:** V73 indică domeniul tematic ANRE 2023, DAR proveniența întrebării originale nu este confirmată.
- **Verificare model și A/B/C:** A randamentul η=Putilă/Pabsorbită pentru bilanț energetic al echipamentului (0..1 pasiv). B Pabsorbită/pierderi nu definește eficiența, C U/I are unitatea ohm, nu raport adimensional.
- **Sursă tehnică candidat:** https://openstax.org/books/university-physics-volume-2/pages/9-5-electrical-energy-and-power. Ediție ANRE2026 și QA independent neverificate.

### G2-ELEC-058
- **Întrebarea:** Pierderile Joule într-un conductor cresc cu:
- A: I²·R
- B: I/R
- C: U/R²
- **Cheia importată nemodificată:** A
- **Proveniență:** V73 indică domeniul tematic ANRE 2023, DAR proveniența întrebării originale nu este confirmată.
- **Verificare model și A/B/C:** A pierderile Joule sunt P_J=I²R pentru rezistor ohmic la R constant. B I/R și C U/R² nu au dimensiunea W. R poate varia cu temperatura și frecvența, deci relația se aplică local parametrilor corecți.
- **Sursă tehnică candidat:** https://openstax.org/books/university-physics-volume-2/pages/9-5-electrical-energy-and-power. Ediție ANRE2026 și QA independent neverificate.

### G2-ELEC-059
- **Întrebarea:** Într-o linie electrică, creșterea tensiunii pentru aceeași putere transmisă determină, ideal, un curent:
- A: mai mic
- B: mai mare de patru ori
- C: neschimbat obligatoriu
- **Cheia importată nemodificată:** A
- **Proveniență:** V73 indică domeniul tematic ANRE 2023, DAR proveniența întrebării originale nu este confirmată.
- **Verificare model și A/B/C:** A pentru P și factorul de putere constante, creșterea tensiunii liniei scade curentul I=P/(√3 U cosφ) în trifazat echilibrat. B creștere de patru ori și C neschimbat sunt false în modelul precizat; topologia și pierderile pot modifica rezultatul real.
- **Sursă tehnică candidat:** https://openstax.org/books/university-physics-volume-2/pages/9-5-electrical-energy-and-power. Ediție ANRE2026 și QA independent neverificate.

### G2-ELEC-060
- **Întrebarea:** Un wattmetru este destinat măsurării:
- A: puterii electrice
- B: rezistenței de izolație exclusiv
- C: frecvenței exclusiv
- **Cheia importată nemodificată:** A
- **Proveniență:** V73 indică domeniul tematic ANRE 2023, DAR proveniența întrebării originale nu este confirmată.
- **Verificare model și A/B/C:** A wattmetrul măsoară puterea electrică, în mod uzual cea activă în watt; B testerul de rezistență de izolație și C frecvențmetrul au alte funcții. Aparatele moderne multifuncționale pot avea mai multe măsurători, dar numele funcției rămâne clar.
- **Sursă tehnică candidat:** https://www.ni.com/en/shop/electronic-test-instrumentation/digital-multimeters/dmm-measurement-fundamentals.html. Ediție ANRE2026 și QA independent neverificate.

### G2-ELEC-061
- **Întrebarea:** Un frecvențmetru este destinat măsurării:
- A: frecvenței
- B: rezistenței
- C: inductanței
- **Cheia importată nemodificată:** A
- **Proveniență:** V73 indică domeniul tematic ANRE 2023, DAR proveniența întrebării originale nu este confirmată.
- **Verificare model și A/B/C:** A frecvențmetrul măsoară frecvența semnalului, exprimată în Hz; B rezistența și C inductanța nu sunt mărimile sale specifice. Frecvența necesită un semnal periodic adecvat.
- **Sursă tehnică candidat:** https://www.ni.com/en/shop/electronic-test-instrumentation/digital-multimeters/dmm-measurement-fundamentals.html. Ediție ANRE2026 și QA independent neverificate.

### G2-ELEC-062
- **Întrebarea:** Un megohmetru este utilizat în principal pentru măsurarea:
- A: rezistenței de izolație la tensiuni de încercare specifice
- B: puterii active de rețea
- C: curentului de scurtcircuit al rețelei
- **Cheia importată nemodificată:** A
- **Proveniență:** V73 indică domeniul tematic ANRE 2023, DAR proveniența întrebării originale nu este confirmată.
- **Verificare model și A/B/C:** A megohmetrul este destinat verificării rezistenței izolației cu tensiune de încercare DC selectată adecvat. B puterea activă și C curentul de scurtcircuit nu sunt scopurile testului. Testul poate implica tensiuni periculoase, necesită deconectarea obiectului și descărcare conform manualului.
- **Sursă tehnică candidat:** https://www.fluke.com/en/learn/blog/electrical/how-to-choose-an-insulation-resistance-tester. Ediție ANRE2026 și QA independent neverificate.

### G2-ELEC-064
- **Întrebarea:** Simbolul electric pentru rezistență este în mod uzual:
- A: R
- B: C
- C: L
- **Cheia importată nemodificată:** A
- **Proveniență:** V73 indică domeniul tematic ANRE 2023, DAR proveniența întrebării originale nu este confirmată.
- **Verificare model și A/B/C:** A simbolul convențional al rezistenței electrice este R. B C capacitate electrică, C L inductanță. A nu se confunda simbolul variabilei R cu unitatea Ω.
- **Sursă tehnică candidat:** https://openstax.org/books/university-physics-volume-2/pages/9-4-ohms-law. Ediție ANRE2026 și QA independent neverificate.

## QA/release gates
- Exactly 15 Grade-II ID source-scope checks; 64 -> **49** records without focused recheck; 822 IDs unique, same order. 807 untouched lines byte-identical.
- Safety: RCD is not automatically overcurrent protection; protective earth doesn't eliminate all risks; megohmeter tests can apply hazardous voltage and require safe de-energizing.
- Both types of provenance are segregated; no case marked officially ANRE-certified. Independent technical/linguistic QA NOT_RUN, 0 learning approvals, key modifications zero.
- 50 previously non-standard serialized CSV rows carried unchanged; proper CSV reconciliation separate.
- PR #7 remains Draft; no QABC edits/HTML/APK/merge/release.
