# CKPT-105 | 20 unități P2 G2: măsurări, SI, curent, protecții, putere | 2026-11-17

## Baseline, adevăr și siguranță
- CKPT104 **342/568 unități, 422/822 ID-uri** contextual documentate. CKPT105 **+20 unități unice și +20 ID-uri** => **362/568, 442/822**, **206 unități P2 restante**, 0/822 approved.
- Sursă re-deschisă textual în această sesiune pentru familia fizică: OpenStax §9.3 rezistivitate/rezistență/conductanță, BIPM SI Brochure ediția 9 actualizată 2026; pentru măsurări Fluke detalii de conectare identificate în manuale, dar **nu s-a executat verificare vizuală PDF în această tură**, deci aceste cazuri păstrează `SOURCE_VISUAL_PDF_NOT_RUN`. Pentru RCD/RCBO există confirmare de la Schneider Electric: RCCB diferențial nu oferă automat protecție magnetotermică, RCBO include ambele.
- Nu se oferă instrucțiuni de intervenție electrică sub tensiune; explicațiile sunt strict conceptuale. Toate cheile A, origine ANRE exactă G2 necertificată; QA independent NOT_RUN, aprobări 0.

## G2-ELEC-033 | AU-410aeacd75cd8505
- sha256 410aeacd75cd850525962ad4fb6d11063835820886163124ab374ed448baa6bc; gradeID G2-ELEC-033; cheia originală {"G2-ELEC-033":"A"} păstrată.
- **Original:** Un multimetru setat pentru măsurarea tensiunii se conectează în mod normal:
  - A. în paralel cu elementul măsurat
  - B. în serie cu elementul
  - C. doar la pământ
- **Sursă de mecanism:** https://www.fluke.com/en/learn/blog/maintenance-monitoring/how-to-use-a-multimeter-guide; exact concept Voltmetrul se conectează între două borne, în paralel; tensiunea reprezintă diferență de potențial. Sursa este o referință de domeniu; nu afirmăm certificarea tuturor detaliilor de produs/normativ.
- **Context:** Identificăm mai întâi obiectul din enunț: un multimetru setat pentru măsurarea tensiunii se conectează în mod normal. Relația/definiția pozitivă este **Voltmetrul se conectează între două borne, în paralel; tensiunea reprezintă diferență de potențial**. A corespunde astfel: Măsurarea U între două borne cere instrument conectat în paralel.. B trebuie eliminată/condiționată separat: Voltmetrul serie cu impedanță mare poate perturba curentul și nu măsoară căderea dorită.. C trebuie eliminată/condiționată separat: O conexiune doar la pământ nu identifică diferența între borne.. Se păstrează ipotezele asupra aparatului și domeniului de aplicare; conceptele de siguranță nu justifică manevre practice fără calificare.
- **Vertical:** A Măsurarea U între două borne cere instrument conectat în paralel.; B Voltmetrul serie cu impedanță mare poate perturba curentul și nu măsoară căderea dorită.; C O conexiune doar la pământ nu identifică diferența între borne..
- **Orizontal ABC:** A versus B și A versus C se decid prin **Voltmetrul se conectează între două borne, în paralel; tensiunea reprezintă diferență de potențial**; B versus C descrie două obiecte/regimuri diferite, niciunul nu înlocuiește expresia afirmativă a lui A.
- **Reversie/contraexemplu:** Dacă schimbăm tipul de instrument, condiția circuitului ori mărimea fizică, concluzia poate diferi. Nu tratăm norma pentru ampermetru serie drept normă pentru voltmetru paralel, nici funcția RCD drept automat magnetotermică.
- **Stare:** A_PRELIMINARY_SUPPORTED_WITH_SCOPE; ORIGINAL_EXAM_KEY_NOT_CERTIFIED; INDEPENDENT_QA_NOT_RUN; LEARNER_APPROVAL_NO.

## G2-ELEC-034 | AU-3a69209e33d3bb91
- sha256 3a69209e33d3bb91df4b1ac43611e61e3dc885bc8c474caf5688871c3009b6c4; gradeID G2-ELEC-034; cheia originală {"G2-ELEC-034":"A"} păstrată.
- **Original:** Un ampermetru se conectează în mod normal:
  - A. în serie cu circuitul
  - B. în paralel pe sursă
  - C. doar între fază și PE
- **Sursă de mecanism:** https://www.fluke.com/en/learn/blog/maintenance-monitoring/how-to-use-a-multimeter-guide; exact concept Ampermetrul obișnuit se introduce în serie; cleștele de curent măsoară indirect. Sursa este o referință de domeniu; nu afirmăm certificarea tuturor detaliilor de produs/normativ.
- **Context:** Identificăm mai întâi obiectul din enunț: un ampermetru se conectează în mod normal. Relația/definiția pozitivă este **Ampermetrul obișnuit se introduce în serie; cleștele de curent măsoară indirect**. A corespunde astfel: Ampermetrul este introdus în serie pentru ca același curent să-l străbată.. B trebuie eliminată/condiționată separat: Montarea unui ampermetru cu rezistență mică direct pe sursă produce potențial scurtcircuit.. C trebuie eliminată/condiționată separat: Conexiunea fază–PE nu este configurația obișnuită de măsurare a curentului.. Se păstrează ipotezele asupra aparatului și domeniului de aplicare; conceptele de siguranță nu justifică manevre practice fără calificare.
- **Vertical:** A Ampermetrul este introdus în serie pentru ca același curent să-l străbată.; B Montarea unui ampermetru cu rezistență mică direct pe sursă produce potențial scurtcircuit.; C Conexiunea fază–PE nu este configurația obișnuită de măsurare a curentului..
- **Orizontal ABC:** A versus B și A versus C se decid prin **Ampermetrul obișnuit se introduce în serie; cleștele de curent măsoară indirect**; B versus C descrie două obiecte/regimuri diferite, niciunul nu înlocuiește expresia afirmativă a lui A.
- **Reversie/contraexemplu:** Dacă schimbăm tipul de instrument, condiția circuitului ori mărimea fizică, concluzia poate diferi. Nu tratăm norma pentru ampermetru serie drept normă pentru voltmetru paralel, nici funcția RCD drept automat magnetotermică.
- **Stare:** A_PRELIMINARY_SUPPORTED_WITH_SCOPE; ORIGINAL_EXAM_KEY_NOT_CERTIFIED; INDEPENDENT_QA_NOT_RUN; LEARNER_APPROVAL_NO.

## G2-ELEC-035 | AU-cc81794052a102ef
- sha256 cc81794052a102ef4a732fded5aeebb79d0b71d2139515fafdffe47baf494e8e; gradeID G2-ELEC-035; cheia originală {"G2-ELEC-035":"A"} păstrată.
- **Original:** Un ohmmetru se folosește corect pentru măsurarea unei rezistențe atunci când circuitul este:
  - A. deconectat de la alimentare
  - B. alimentat la tensiunea nominală
  - C. scurtcircuitat
- **Sursă de mecanism:** https://www.fluke.com/en/learn/blog/maintenance-monitoring/how-to-use-a-multimeter-guide; exact concept Ohmmetrul se folosește cu circuitul deconectat și elementele reactive descărcate. Sursa este o referință de domeniu; nu afirmăm certificarea tuturor detaliilor de produs/normativ.
- **Context:** Identificăm mai întâi obiectul din enunț: un ohmmetru se folosește corect pentru măsurarea unei rezistențe atunci când circuitul este. Relația/definiția pozitivă este **Ohmmetrul se folosește cu circuitul deconectat și elementele reactive descărcate**. A corespunde astfel: Ohmmetrul aplică sursa lui internă, deci circuitul se măsoară izolat de alimentare.. B trebuie eliminată/condiționată separat: Circuitul energizat poate deteriora aparatul și crea risc pentru persoană.. C trebuie eliminată/condiționată separat: Scurtcircuitarea completă a circuitului ar altera măsura rezistenței căutate.. Se păstrează ipotezele asupra aparatului și domeniului de aplicare; conceptele de siguranță nu justifică manevre practice fără calificare.
- **Vertical:** A Ohmmetrul aplică sursa lui internă, deci circuitul se măsoară izolat de alimentare.; B Circuitul energizat poate deteriora aparatul și crea risc pentru persoană.; C Scurtcircuitarea completă a circuitului ar altera măsura rezistenței căutate..
- **Orizontal ABC:** A versus B și A versus C se decid prin **Ohmmetrul se folosește cu circuitul deconectat și elementele reactive descărcate**; B versus C descrie două obiecte/regimuri diferite, niciunul nu înlocuiește expresia afirmativă a lui A.
- **Reversie/contraexemplu:** Dacă schimbăm tipul de instrument, condiția circuitului ori mărimea fizică, concluzia poate diferi. Nu tratăm norma pentru ampermetru serie drept normă pentru voltmetru paralel, nici funcția RCD drept automat magnetotermică.
- **Stare:** A_PRELIMINARY_SUPPORTED_WITH_SCOPE; ORIGINAL_EXAM_KEY_NOT_CERTIFIED; INDEPENDENT_QA_NOT_RUN; LEARNER_APPROVAL_NO.

## G2-ELEC-036 | AU-1ddf85c8f1a3d32d
- sha256 1ddf85c8f1a3d32d762bff9a4cf5c68a419d2262feead247ce0be0b81d5f2149; gradeID G2-ELEC-036; cheia originală {"G2-ELEC-036":"A"} păstrată.
- **Original:** Un scurtcircuit este caracterizat ideal prin:
  - A. impedanță foarte mică și curent foarte mare
  - B. impedanță foarte mare și curent nul
  - C. putere reactivă nulă obligatoriu
- **Sursă de mecanism:** https://openstax.org/books/university-physics-volume-2/pages/10-3-kirchhoffs-rules; exact concept Scurtcircuitul are impedanță mică și curent limitat de sursă + rețea. Secțiune didactică sau BIPM relevantă redeschisă textual pentru această familie.
- **Context:** Identificăm mai întâi obiectul din enunț: un scurtcircuit este caracterizat ideal prin. Relația/definiția pozitivă este **Scurtcircuitul are impedanță mică și curent limitat de sursă + rețea**. A corespunde astfel: La sursă cu impedanță finită, calea de scurt impedanță joasă duce la curent mare.. B trebuie eliminată/condiționată separat: Impedanța foarte mare cu curent zero ar fi o întrerupere, nu scurtcircuit.. C trebuie eliminată/condiționată separat: Puterea reactivă nu e obligatoriu zero pentru o sursă/linie de defect inductivă.. Se păstrează ipotezele asupra aparatului și domeniului de aplicare; conceptele de siguranță nu justifică manevre practice fără calificare.
- **Vertical:** A La sursă cu impedanță finită, calea de scurt impedanță joasă duce la curent mare.; B Impedanța foarte mare cu curent zero ar fi o întrerupere, nu scurtcircuit.; C Puterea reactivă nu e obligatoriu zero pentru o sursă/linie de defect inductivă..
- **Orizontal ABC:** A versus B și A versus C se decid prin **Scurtcircuitul are impedanță mică și curent limitat de sursă + rețea**; B versus C descrie două obiecte/regimuri diferite, niciunul nu înlocuiește expresia afirmativă a lui A.
- **Reversie/contraexemplu:** Dacă schimbăm tipul de instrument, condiția circuitului ori mărimea fizică, concluzia poate diferi. Nu tratăm norma pentru ampermetru serie drept normă pentru voltmetru paralel, nici funcția RCD drept automat magnetotermică.
- **Stare:** A_PRELIMINARY_SUPPORTED_WITH_SCOPE; ORIGINAL_EXAM_KEY_NOT_CERTIFIED; INDEPENDENT_QA_NOT_RUN; LEARNER_APPROVAL_NO.

## G2-ELEC-037 | AU-6eb04816474ac6ff
- sha256 6eb04816474ac6ffbcee2cef91b7f77c5f41802b497f7517eed9b792ff430114; gradeID G2-ELEC-037; cheia originală {"G2-ELEC-037":"A"} păstrată.
- **Original:** Legea lui Kirchhoff a curenților se aplică unui nod și exprimă că:
  - A. suma algebrică a curenților din nod este zero
  - B. toate tensiunile sunt zero
  - C. puterea activă este întotdeauna zero
- **Sursă de mecanism:** https://openstax.org/books/university-physics-volume-2/pages/10-3-kirchhoffs-rules; exact concept Kirchhoff nod: suma algebrică a curenților este zero, cu conservarea sarcinii. Secțiune didactică sau BIPM relevantă redeschisă textual pentru această familie.
- **Context:** Identificăm mai întâi obiectul din enunț: legea lui kirchhoff a curenților se aplică unui nod și exprimă că. Relația/definiția pozitivă este **Kirchhoff nod: suma algebrică a curenților este zero, cu conservarea sarcinii**. A corespunde astfel: Conservarea sarcinii într-un nod lumped: suma algebrică a curenților este zero.. B trebuie eliminată/condiționată separat: Legea nodului nu impune tuturor tensiunilor să fie zero.. C trebuie eliminată/condiționată separat: P în nod nu este prin definiție zero, ci balanța curenților.. Se păstrează ipotezele asupra aparatului și domeniului de aplicare; conceptele de siguranță nu justifică manevre practice fără calificare.
- **Vertical:** A Conservarea sarcinii într-un nod lumped: suma algebrică a curenților este zero.; B Legea nodului nu impune tuturor tensiunilor să fie zero.; C P în nod nu este prin definiție zero, ci balanța curenților..
- **Orizontal ABC:** A versus B și A versus C se decid prin **Kirchhoff nod: suma algebrică a curenților este zero, cu conservarea sarcinii**; B versus C descrie două obiecte/regimuri diferite, niciunul nu înlocuiește expresia afirmativă a lui A.
- **Reversie/contraexemplu:** Dacă schimbăm tipul de instrument, condiția circuitului ori mărimea fizică, concluzia poate diferi. Nu tratăm norma pentru ampermetru serie drept normă pentru voltmetru paralel, nici funcția RCD drept automat magnetotermică.
- **Stare:** A_PRELIMINARY_SUPPORTED_WITH_SCOPE; ORIGINAL_EXAM_KEY_NOT_CERTIFIED; INDEPENDENT_QA_NOT_RUN; LEARNER_APPROVAL_NO.

## G2-ELEC-038 | AU-4f89b0a15a51ad32
- sha256 4f89b0a15a51ad3228a29849a924a4de4a2103c06e7b10e6dfe69f8f49da8f48; gradeID G2-ELEC-038; cheia originală {"G2-ELEC-038":"A"} păstrată.
- **Original:** Legea lui Kirchhoff a tensiunilor exprimă, pe un contur închis, că:
  - A. suma algebrică a tensiunilor este zero
  - B. suma curenților este întotdeauna zero
  - C. toate rezistențele sunt egale
- **Sursă de mecanism:** https://openstax.org/books/university-physics-volume-2/pages/10-3-kirchhoffs-rules; exact concept Kirchhoff buclă: suma algebrică a tensiunilor este zero în model concentrat cvasistaționar. Secțiune didactică sau BIPM relevantă redeschisă textual pentru această familie.
- **Context:** Identificăm mai întâi obiectul din enunț: legea lui kirchhoff a tensiunilor exprimă, pe un contur închis, că. Relația/definiția pozitivă este **Kirchhoff buclă: suma algebrică a tensiunilor este zero în model concentrat cvasistaționar**. A corespunde astfel: KVL: suma algebrică a tensiunilor în jurul conturului închis este zero în model lumped.. B trebuie eliminată/condiționată separat: Suma curenților zero este legea nodului, nu relația pe contur.. C trebuie eliminată/condiționată separat: Rezistențele diferite pot exista într-o buclă Kirchhoff.. Se păstrează ipotezele asupra aparatului și domeniului de aplicare; conceptele de siguranță nu justifică manevre practice fără calificare.
- **Vertical:** A KVL: suma algebrică a tensiunilor în jurul conturului închis este zero în model lumped.; B Suma curenților zero este legea nodului, nu relația pe contur.; C Rezistențele diferite pot exista într-o buclă Kirchhoff..
- **Orizontal ABC:** A versus B și A versus C se decid prin **Kirchhoff buclă: suma algebrică a tensiunilor este zero în model concentrat cvasistaționar**; B versus C descrie două obiecte/regimuri diferite, niciunul nu înlocuiește expresia afirmativă a lui A.
- **Reversie/contraexemplu:** Dacă schimbăm tipul de instrument, condiția circuitului ori mărimea fizică, concluzia poate diferi. Nu tratăm norma pentru ampermetru serie drept normă pentru voltmetru paralel, nici funcția RCD drept automat magnetotermică.
- **Stare:** A_PRELIMINARY_SUPPORTED_WITH_SCOPE; ORIGINAL_EXAM_KEY_NOT_CERTIFIED; INDEPENDENT_QA_NOT_RUN; LEARNER_APPROVAL_NO.

## G2-ELEC-039 | AU-692ff60e01bca71a
- sha256 692ff60e01bca71a69d037b3a4b9822eb32abc39f1f91c037bee047baa67a843; gradeID G2-ELEC-039; cheia originală {"G2-ELEC-039":"A"} păstrată.
- **Original:** Conductanța electrică este inversul:
  - A. rezistenței
  - B. tensiunii
  - C. puterii
- **Sursă de mecanism:** https://www.bipm.org/en/publications/si-brochure/; exact concept Conductanța G=1/R, pentru R≠0, măsurată în siemens. Secțiune didactică sau BIPM relevantă redeschisă textual pentru această familie.
- **Context:** Identificăm mai întâi obiectul din enunț: conductanța electrică este inversul. Relația/definiția pozitivă este **Conductanța G=1/R, pentru R≠0, măsurată în siemens**. A corespunde astfel: Conductanța G=1/R pentru rezistență ohmică nenulă.. B trebuie eliminată/condiționată separat: Tensiunea nu este inversa conductanței.. C trebuie eliminată/condiționată separat: Puterea nu este inversa conductanței.. Se păstrează ipotezele asupra aparatului și domeniului de aplicare; conceptele de siguranță nu justifică manevre practice fără calificare.
- **Vertical:** A Conductanța G=1/R pentru rezistență ohmică nenulă.; B Tensiunea nu este inversa conductanței.; C Puterea nu este inversa conductanței..
- **Orizontal ABC:** A versus B și A versus C se decid prin **Conductanța G=1/R, pentru R≠0, măsurată în siemens**; B versus C descrie două obiecte/regimuri diferite, niciunul nu înlocuiește expresia afirmativă a lui A.
- **Reversie/contraexemplu:** Dacă schimbăm tipul de instrument, condiția circuitului ori mărimea fizică, concluzia poate diferi. Nu tratăm norma pentru ampermetru serie drept normă pentru voltmetru paralel, nici funcția RCD drept automat magnetotermică.
- **Stare:** A_PRELIMINARY_SUPPORTED_WITH_SCOPE; ORIGINAL_EXAM_KEY_NOT_CERTIFIED; INDEPENDENT_QA_NOT_RUN; LEARNER_APPROVAL_NO.

## G2-ELEC-040 | AU-001cd626e18f4238
- sha256 001cd626e18f4238f444d949bad82132b5762f4d3553590c458c3901ba859bdb; gradeID G2-ELEC-040; cheia originală {"G2-ELEC-040":"A"} păstrată.
- **Original:** Unitatea conductanței este:
  - A. siemens (S)
  - B. tesla (T)
  - C. henry (H)
- **Sursă de mecanism:** https://www.bipm.org/en/publications/si-brochure/; exact concept Unitatea conductanței este siemens (S), nu tesla ori henry. Secțiune didactică sau BIPM relevantă redeschisă textual pentru această familie.
- **Context:** Identificăm mai întâi obiectul din enunț: unitatea conductanței este. Relația/definiția pozitivă este **Unitatea conductanței este siemens (S), nu tesla ori henry**. A corespunde astfel: Siemens (S)=Ω^-1 măsoară conductanța electrică.. B trebuie eliminată/condiționată separat: Tesla (T) măsoară inducția magnetică.. C trebuie eliminată/condiționată separat: Henry (H) măsoară inductanța.. Se păstrează ipotezele asupra aparatului și domeniului de aplicare; conceptele de siguranță nu justifică manevre practice fără calificare.
- **Vertical:** A Siemens (S)=Ω^-1 măsoară conductanța electrică.; B Tesla (T) măsoară inducția magnetică.; C Henry (H) măsoară inductanța..
- **Orizontal ABC:** A versus B și A versus C se decid prin **Unitatea conductanței este siemens (S), nu tesla ori henry**; B versus C descrie două obiecte/regimuri diferite, niciunul nu înlocuiește expresia afirmativă a lui A.
- **Reversie/contraexemplu:** Dacă schimbăm tipul de instrument, condiția circuitului ori mărimea fizică, concluzia poate diferi. Nu tratăm norma pentru ampermetru serie drept normă pentru voltmetru paralel, nici funcția RCD drept automat magnetotermică.
- **Stare:** A_PRELIMINARY_SUPPORTED_WITH_SCOPE; ORIGINAL_EXAM_KEY_NOT_CERTIFIED; INDEPENDENT_QA_NOT_RUN; LEARNER_APPROVAL_NO.

## G2-ELEC-041 | AU-e92da5be976f5175
- sha256 e92da5be976f5175c01e72a3548c404fd80e84970711d3466ac515ac770b7762; gradeID G2-ELEC-041; cheia originală {"G2-ELEC-041":"A"} păstrată.
- **Original:** Capacitatea electrică se măsoară în:
  - A. farazi (F)
  - B. henry (H)
  - C. tesla (T)
- **Sursă de mecanism:** https://www.bipm.org/en/publications/si-brochure/; exact concept Capacitatea electrică se exprimă în farazi F; inductanța în H. Secțiune didactică sau BIPM relevantă redeschisă textual pentru această familie.
- **Context:** Identificăm mai întâi obiectul din enunț: capacitatea electrică se măsoară în. Relația/definiția pozitivă este **Capacitatea electrică se exprimă în farazi F; inductanța în H**. A corespunde astfel: Farad (F)=C/V este unitatea SI a capacității.. B trebuie eliminată/condiționată separat: Henry (H) este inductanță.. C trebuie eliminată/condiționată separat: Tesla (T) este densitatea fluxului magnetic.. Se păstrează ipotezele asupra aparatului și domeniului de aplicare; conceptele de siguranță nu justifică manevre practice fără calificare.
- **Vertical:** A Farad (F)=C/V este unitatea SI a capacității.; B Henry (H) este inductanță.; C Tesla (T) este densitatea fluxului magnetic..
- **Orizontal ABC:** A versus B și A versus C se decid prin **Capacitatea electrică se exprimă în farazi F; inductanța în H**; B versus C descrie două obiecte/regimuri diferite, niciunul nu înlocuiește expresia afirmativă a lui A.
- **Reversie/contraexemplu:** Dacă schimbăm tipul de instrument, condiția circuitului ori mărimea fizică, concluzia poate diferi. Nu tratăm norma pentru ampermetru serie drept normă pentru voltmetru paralel, nici funcția RCD drept automat magnetotermică.
- **Stare:** A_PRELIMINARY_SUPPORTED_WITH_SCOPE; ORIGINAL_EXAM_KEY_NOT_CERTIFIED; INDEPENDENT_QA_NOT_RUN; LEARNER_APPROVAL_NO.

## G2-ELEC-042 | AU-bfe150a96b7b57af
- sha256 bfe150a96b7b57afc9c07ca759d981202a976ef21433c31a0749dd555d5194cc; gradeID G2-ELEC-042; cheia originală {"G2-ELEC-042":"A"} păstrată.
- **Original:** Inductanța se măsoară în:
  - A. henry (H)
  - B. farad (F)
  - C. siemens (S)
- **Sursă de mecanism:** https://www.bipm.org/en/publications/si-brochure/; exact concept Inductanța L se măsoară în henry H; farad este capacitate. Secțiune didactică sau BIPM relevantă redeschisă textual pentru această familie.
- **Context:** Identificăm mai întâi obiectul din enunț: inductanța se măsoară în. Relația/definiția pozitivă este **Inductanța L se măsoară în henry H; farad este capacitate**. A corespunde astfel: Henry (H)=V·s/A măsoară inductanța.. B trebuie eliminată/condiționată separat: Farad (F) măsoară capacitatea.. C trebuie eliminată/condiționată separat: Siemens (S) măsoară conductanța.. Se păstrează ipotezele asupra aparatului și domeniului de aplicare; conceptele de siguranță nu justifică manevre practice fără calificare.
- **Vertical:** A Henry (H)=V·s/A măsoară inductanța.; B Farad (F) măsoară capacitatea.; C Siemens (S) măsoară conductanța..
- **Orizontal ABC:** A versus B și A versus C se decid prin **Inductanța L se măsoară în henry H; farad este capacitate**; B versus C descrie două obiecte/regimuri diferite, niciunul nu înlocuiește expresia afirmativă a lui A.
- **Reversie/contraexemplu:** Dacă schimbăm tipul de instrument, condiția circuitului ori mărimea fizică, concluzia poate diferi. Nu tratăm norma pentru ampermetru serie drept normă pentru voltmetru paralel, nici funcția RCD drept automat magnetotermică.
- **Stare:** A_PRELIMINARY_SUPPORTED_WITH_SCOPE; ORIGINAL_EXAM_KEY_NOT_CERTIFIED; INDEPENDENT_QA_NOT_RUN; LEARNER_APPROVAL_NO.

## G2-ELEC-043 | AU-2333f1797ed9c556
- sha256 2333f1797ed9c55640312d1b91a984efb6fcb8eaefae1d2c93fb08ac17b106bb; gradeID G2-ELEC-043; cheia originală {"G2-ELEC-043":"A"} păstrată.
- **Original:** Densitatea de curent este raportul dintre:
  - A. curent și aria secțiunii
  - B. tensiune și lungime
  - C. putere și timp
- **Sursă de mecanism:** https://openstax.org/books/university-physics-volume-2/pages/9-3-resistivity-and-resistance; exact concept Densitatea medie a curentului J=I/A, în A/m². Secțiune didactică sau BIPM relevantă redeschisă textual pentru această familie.
- **Context:** Identificăm mai întâi obiectul din enunț: densitatea de curent este raportul dintre. Relația/definiția pozitivă este **Densitatea medie a curentului J=I/A, în A/m²**. A corespunde astfel: Densitatea medie de curent J=I/A la repartizare uniformă.. B trebuie eliminată/condiționată separat: U/L are unitate V/m de câmp electric, nu A/m².. C trebuie eliminată/condiționată separat: P/t este rată de modificare a energiei pe timp², nu densitate de curent.. Se păstrează ipotezele asupra aparatului și domeniului de aplicare; conceptele de siguranță nu justifică manevre practice fără calificare.
- **Vertical:** A Densitatea medie de curent J=I/A la repartizare uniformă.; B U/L are unitate V/m de câmp electric, nu A/m².; C P/t este rată de modificare a energiei pe timp², nu densitate de curent..
- **Orizontal ABC:** A versus B și A versus C se decid prin **Densitatea medie a curentului J=I/A, în A/m²**; B versus C descrie două obiecte/regimuri diferite, niciunul nu înlocuiește expresia afirmativă a lui A.
- **Reversie/contraexemplu:** Dacă schimbăm tipul de instrument, condiția circuitului ori mărimea fizică, concluzia poate diferi. Nu tratăm norma pentru ampermetru serie drept normă pentru voltmetru paralel, nici funcția RCD drept automat magnetotermică.
- **Stare:** A_PRELIMINARY_SUPPORTED_WITH_SCOPE; ORIGINAL_EXAM_KEY_NOT_CERTIFIED; INDEPENDENT_QA_NOT_RUN; LEARNER_APPROVAL_NO.

## G2-ELEC-044 | AU-b85a9e6a9700960e
- sha256 b85a9e6a9700960e96a25569376d7884db1d57a956bfae49c09e945f03eff838; gradeID G2-ELEC-044; cheia originală {"G2-ELEC-044":"A"} păstrată.
- **Original:** Rezistența unui conductor omogen este proporțională cu:
  - A. lungimea și rezistivitatea
  - B. doar curentul
  - C. doar tensiunea
- **Sursă de mecanism:** https://openstax.org/books/university-physics-volume-2/pages/9-3-resistivity-and-resistance; exact concept Conductor omogen R=ρl/A, deci R proporțional cu ρ și l la A fix. Secțiune didactică sau BIPM relevantă redeschisă textual pentru această familie.
- **Context:** Identificăm mai întâi obiectul din enunț: rezistența unui conductor omogen este proporțională cu. Relația/definiția pozitivă este **Conductor omogen R=ρl/A, deci R proporțional cu ρ și l la A fix**. A corespunde astfel: R=ρL/A: rezistența crește cu lungimea și rezistivitatea la secțiune constantă.. B trebuie eliminată/condiționată separat: R nu depinde «doar de curent» pentru element ohmic cu temperatură fixă.. C trebuie eliminată/condiționată separat: R nu depinde «doar de tensiune» pentru conductor ohmic.. Se păstrează ipotezele asupra aparatului și domeniului de aplicare; conceptele de siguranță nu justifică manevre practice fără calificare.
- **Vertical:** A R=ρL/A: rezistența crește cu lungimea și rezistivitatea la secțiune constantă.; B R nu depinde «doar de curent» pentru element ohmic cu temperatură fixă.; C R nu depinde «doar de tensiune» pentru conductor ohmic..
- **Orizontal ABC:** A versus B și A versus C se decid prin **Conductor omogen R=ρl/A, deci R proporțional cu ρ și l la A fix**; B versus C descrie două obiecte/regimuri diferite, niciunul nu înlocuiește expresia afirmativă a lui A.
- **Reversie/contraexemplu:** Dacă schimbăm tipul de instrument, condiția circuitului ori mărimea fizică, concluzia poate diferi. Nu tratăm norma pentru ampermetru serie drept normă pentru voltmetru paralel, nici funcția RCD drept automat magnetotermică.
- **Stare:** A_PRELIMINARY_SUPPORTED_WITH_SCOPE; ORIGINAL_EXAM_KEY_NOT_CERTIFIED; INDEPENDENT_QA_NOT_RUN; LEARNER_APPROVAL_NO.

## G2-ELEC-045 | AU-b3a3d76388323d0c
- sha256 b3a3d76388323d0cc5e069b37641a3e9f9742ea99f3ede475a5d7e5b8064329d; gradeID G2-ELEC-045; cheia originală {"G2-ELEC-045":"A"} păstrată.
- **Original:** Rezistența unui conductor omogen este invers proporțională cu:
  - A. aria secțiunii transversale
  - B. lungimea
  - C. rezistivitatea
- **Sursă de mecanism:** https://openstax.org/books/university-physics-volume-2/pages/9-3-resistivity-and-resistance; exact concept Conductor omogen R=ρl/A, invers proporțional cu aria A. Secțiune didactică sau BIPM relevantă redeschisă textual pentru această familie.
- **Context:** Identificăm mai întâi obiectul din enunț: rezistența unui conductor omogen este invers proporțională cu. Relația/definiția pozitivă este **Conductor omogen R=ρl/A, invers proporțional cu aria A**. A corespunde astfel: La ρ și L fixe, R=ρL/A, invers proporțional cu aria.. B trebuie eliminată/condiționată separat: R crește direct cu L, nu invers.. C trebuie eliminată/condiționată separat: R crește direct cu rezistivitatea ρ, nu invers.. Se păstrează ipotezele asupra aparatului și domeniului de aplicare; conceptele de siguranță nu justifică manevre practice fără calificare.
- **Vertical:** A La ρ și L fixe, R=ρL/A, invers proporțional cu aria.; B R crește direct cu L, nu invers.; C R crește direct cu rezistivitatea ρ, nu invers..
- **Orizontal ABC:** A versus B și A versus C se decid prin **Conductor omogen R=ρl/A, invers proporțional cu aria A**; B versus C descrie două obiecte/regimuri diferite, niciunul nu înlocuiește expresia afirmativă a lui A.
- **Reversie/contraexemplu:** Dacă schimbăm tipul de instrument, condiția circuitului ori mărimea fizică, concluzia poate diferi. Nu tratăm norma pentru ampermetru serie drept normă pentru voltmetru paralel, nici funcția RCD drept automat magnetotermică.
- **Stare:** A_PRELIMINARY_SUPPORTED_WITH_SCOPE; ORIGINAL_EXAM_KEY_NOT_CERTIFIED; INDEPENDENT_QA_NOT_RUN; LEARNER_APPROVAL_NO.

## G2-ELEC-046 | AU-25db8edfbf54a339
- sha256 25db8edfbf54a3397e1ba254fb6bc3d1770456c698397d6b24c07ac71c94759c; gradeID G2-ELEC-046; cheia originală {"G2-ELEC-046":"A"} păstrată.
- **Original:** Pentru un conductor metalic, în intervale uzuale, creșterea temperaturii determină de regulă:
  - A. creșterea rezistenței
  - B. scăderea rezistenței la zero
  - C. inversarea polarității
- **Sursă de mecanism:** https://openstax.org/books/university-physics-volume-2/pages/9-3-resistivity-and-resistance; exact concept Pentru metale obișnuite α>0: R=R0(1+αΔT) în interval uzual. Secțiune didactică sau BIPM relevantă redeschisă textual pentru această familie.
- **Context:** Identificăm mai întâi obiectul din enunț: pentru un conductor metalic, în intervale uzuale, creșterea temperaturii determină de regulă. Relația/definiția pozitivă este **Pentru metale obișnuite α>0: R=R0(1+αΔT) în interval uzual**. A corespunde astfel: Pentru metal obișnuit coeficientul termic α>0 și R crește cu temperatura.. B trebuie eliminată/condiționată separat: Rezistența metalului nu scade în general la zero prin încălzire moderată.. C trebuie eliminată/condiționată separat: Polaritatea nu se inversează din simpla încălzire a conductorului.. Se păstrează ipotezele asupra aparatului și domeniului de aplicare; conceptele de siguranță nu justifică manevre practice fără calificare.
- **Vertical:** A Pentru metal obișnuit coeficientul termic α>0 și R crește cu temperatura.; B Rezistența metalului nu scade în general la zero prin încălzire moderată.; C Polaritatea nu se inversează din simpla încălzire a conductorului..
- **Orizontal ABC:** A versus B și A versus C se decid prin **Pentru metale obișnuite α>0: R=R0(1+αΔT) în interval uzual**; B versus C descrie două obiecte/regimuri diferite, niciunul nu înlocuiește expresia afirmativă a lui A.
- **Reversie/contraexemplu:** Dacă schimbăm tipul de instrument, condiția circuitului ori mărimea fizică, concluzia poate diferi. Nu tratăm norma pentru ampermetru serie drept normă pentru voltmetru paralel, nici funcția RCD drept automat magnetotermică.
- **Stare:** A_PRELIMINARY_SUPPORTED_WITH_SCOPE; ORIGINAL_EXAM_KEY_NOT_CERTIFIED; INDEPENDENT_QA_NOT_RUN; LEARNER_APPROVAL_NO.

## G2-ELEC-047 | AU-f590661ae91a6f35
- sha256 f590661ae91a6f35e96ce0ce8b4cdcf6e63c95922401a5ecafe8eda41fc3d677; gradeID G2-ELEC-047; cheia originală {"G2-ELEC-047":"A"} păstrată.
- **Original:** Scopul principal al unei protecții la supracurent este:
  - A. limitarea efectelor curenților excesivi
  - B. creșterea tensiunii de alimentare
  - C. mărirea rezistenței sarcinii
- **Sursă de mecanism:** https://www.electrical-installation.org/enwiki/Protection_of_circuits; exact concept Protecția la supracurent limitează efectele termice/electrodinamice ale curenților excesivi. Sursa este o referință de domeniu; nu afirmăm certificarea tuturor detaliilor de produs/normativ.
- **Context:** Identificăm mai întâi obiectul din enunț: scopul principal al unei protecții la supracurent este. Relația/definiția pozitivă este **Protecția la supracurent limitează efectele termice/electrodinamice ale curenților excesivi**. A corespunde astfel: Dispozitivul de supracurent limitează durata/efectul termic și electrodinamic al curentului excesiv.. B trebuie eliminată/condiționată separat: Protecția nu este destinată creșterii tensiunii.. C trebuie eliminată/condiționată separat: Protecția nu modifică intenționat rezistența sarcinii pentru a elimina defectul.. Se păstrează ipotezele asupra aparatului și domeniului de aplicare; conceptele de siguranță nu justifică manevre practice fără calificare.
- **Vertical:** A Dispozitivul de supracurent limitează durata/efectul termic și electrodinamic al curentului excesiv.; B Protecția nu este destinată creșterii tensiunii.; C Protecția nu modifică intenționat rezistența sarcinii pentru a elimina defectul..
- **Orizontal ABC:** A versus B și A versus C se decid prin **Protecția la supracurent limitează efectele termice/electrodinamice ale curenților excesivi**; B versus C descrie două obiecte/regimuri diferite, niciunul nu înlocuiește expresia afirmativă a lui A.
- **Reversie/contraexemplu:** Dacă schimbăm tipul de instrument, condiția circuitului ori mărimea fizică, concluzia poate diferi. Nu tratăm norma pentru ampermetru serie drept normă pentru voltmetru paralel, nici funcția RCD drept automat magnetotermică.
- **Stare:** A_PRELIMINARY_SUPPORTED_WITH_SCOPE; ORIGINAL_EXAM_KEY_NOT_CERTIFIED; INDEPENDENT_QA_NOT_RUN; LEARNER_APPROVAL_NO.

## G2-ELEC-048 | AU-469a92ef969989c2
- sha256 469a92ef969989c2d52810a84f23548cec51c7fe9e9318dad42130258455fbc2; gradeID G2-ELEC-048; cheia originală {"G2-ELEC-048":"A"} păstrată.
- **Original:** Un întreruptor automat poate asigura protecția la:
  - A. suprasarcină și scurtcircuit, în funcție de caracteristicile aparatului
  - B. doar iluminat natural
  - C. doar lipsa fazei în orice situație
- **Sursă de mecanism:** https://www.electrical-installation.org/enwiki/Protection_of_circuits; exact concept Întreruptorul cu protecții corespunzătoare poate detecta suprasarcină/scurtcircuit; depinde de caracteristicile aparatului. Sursa este o referință de domeniu; nu afirmăm certificarea tuturor detaliilor de produs/normativ.
- **Context:** Identificăm mai întâi obiectul din enunț: un întreruptor automat poate asigura protecția la. Relația/definiția pozitivă este **Întreruptorul cu protecții corespunzătoare poate detecta suprasarcină/scurtcircuit; depinde de caracteristicile aparatului**. A corespunde astfel: Un disjunctor cu declanșatoare potrivite poate proteja la suprasarcină și scurtcircuit.. B trebuie eliminată/condiționată separat: Iluminatul natural nu are legătură cu protecția electrică.. C trebuie eliminată/condiționată separat: Lipsa fazei nu este detectată obligatoriu de orice disjunctor standard.. Se păstrează ipotezele asupra aparatului și domeniului de aplicare; conceptele de siguranță nu justifică manevre practice fără calificare.
- **Vertical:** A Un disjunctor cu declanșatoare potrivite poate proteja la suprasarcină și scurtcircuit.; B Iluminatul natural nu are legătură cu protecția electrică.; C Lipsa fazei nu este detectată obligatoriu de orice disjunctor standard..
- **Orizontal ABC:** A versus B și A versus C se decid prin **Întreruptorul cu protecții corespunzătoare poate detecta suprasarcină/scurtcircuit; depinde de caracteristicile aparatului**; B versus C descrie două obiecte/regimuri diferite, niciunul nu înlocuiește expresia afirmativă a lui A.
- **Reversie/contraexemplu:** Dacă schimbăm tipul de instrument, condiția circuitului ori mărimea fizică, concluzia poate diferi. Nu tratăm norma pentru ampermetru serie drept normă pentru voltmetru paralel, nici funcția RCD drept automat magnetotermică.
- **Stare:** A_PRELIMINARY_SUPPORTED_WITH_SCOPE; ORIGINAL_EXAM_KEY_NOT_CERTIFIED; INDEPENDENT_QA_NOT_RUN; LEARNER_APPROVAL_NO.

## G2-ELEC-049 | AU-0db556b4db451200
- sha256 0db556b4db451200351d3b4c23c2bbcbdb9d960495e9b07ce28f4ce8f9ba039f; gradeID G2-ELEC-049; cheia originală {"G2-ELEC-049":"A"} păstrată.
- **Original:** Un dispozitiv diferențial detectează în principal:
  - A. un dezechilibru al curenților care indică un curent rezidual
  - B. doar supratensiunea
  - C. doar frecvența rețelei
- **Sursă de mecanism:** https://www.se.com/ro/ro/faqs/FAQ000261230/; exact concept RCD detectează diferența dintre curenții conductoarelor active, curent rezidual; nu este protecție universală la supracurent. Sursa este o referință de domeniu; nu afirmăm certificarea tuturor detaliilor de produs/normativ.
- **Context:** Identificăm mai întâi obiectul din enunț: un dispozitiv diferențial detectează în principal. Relația/definiția pozitivă este **RCD detectează diferența dintre curenții conductoarelor active, curent rezidual; nu este protecție universală la supracurent**. A corespunde astfel: RCD compară curenții conductorilor activi; diferența semnalează un curent rezidual.. B trebuie eliminată/condiționată separat: RCD nu este automat un detector de supratensiune.. C trebuie eliminată/condiționată separat: RCD nu este un frecvențmetru.. Se păstrează ipotezele asupra aparatului și domeniului de aplicare; conceptele de siguranță nu justifică manevre practice fără calificare.
- **Vertical:** A RCD compară curenții conductorilor activi; diferența semnalează un curent rezidual.; B RCD nu este automat un detector de supratensiune.; C RCD nu este un frecvențmetru..
- **Orizontal ABC:** A versus B și A versus C se decid prin **RCD detectează diferența dintre curenții conductoarelor active, curent rezidual; nu este protecție universală la supracurent**; B versus C descrie două obiecte/regimuri diferite, niciunul nu înlocuiește expresia afirmativă a lui A.
- **Reversie/contraexemplu:** Dacă schimbăm tipul de instrument, condiția circuitului ori mărimea fizică, concluzia poate diferi. Nu tratăm norma pentru ampermetru serie drept normă pentru voltmetru paralel, nici funcția RCD drept automat magnetotermică.
- **Stare:** A_PRELIMINARY_SUPPORTED_WITH_SCOPE; ORIGINAL_EXAM_KEY_NOT_CERTIFIED; INDEPENDENT_QA_NOT_RUN; LEARNER_APPROVAL_NO.

## G2-ELEC-050 | AU-007174eb14dedd2f
- sha256 007174eb14dedd2f411df576cfef96b8564f432fb79dbad922abdad60278c482; gradeID G2-ELEC-050; cheia originală {"G2-ELEC-050":"A"} păstrată.
- **Original:** Împământarea de protecție are ca scop principal:
  - A. reducerea riscului de electrocutare prin asigurarea unei căi de defect și a condițiilor de declanșare a protecției
  - B. creșterea consumului
  - C. eliminarea completă a tuturor defectelor
- **Sursă de mecanism:** https://www.electrical-installation.org/enwiki/Protection_against_electric_shock; exact concept PE/împământarea participă la protecția contra șocului împreună cu dispozitivul de declanșare în sistem TN/TT/IT. Sursa este o referință de domeniu; nu afirmăm certificarea tuturor detaliilor de produs/normativ.
- **Context:** Identificăm mai întâi obiectul din enunț: împământarea de protecție are ca scop principal. Relația/definiția pozitivă este **PE/împământarea participă la protecția contra șocului împreună cu dispozitivul de declanșare în sistem TN/TT/IT**. A corespunde astfel: Legarea de protecție asigură cale de curent de defect și sprijină deconectarea automată, reducând șocul.. B trebuie eliminată/condiționată separat: Nu urmărește creșterea consumului de energie.. C trebuie eliminată/condiționată separat: Împământarea nu elimină complet apariția defectelor electrice.. Se păstrează ipotezele asupra aparatului și domeniului de aplicare; conceptele de siguranță nu justifică manevre practice fără calificare.
- **Vertical:** A Legarea de protecție asigură cale de curent de defect și sprijină deconectarea automată, reducând șocul.; B Nu urmărește creșterea consumului de energie.; C Împământarea nu elimină complet apariția defectelor electrice..
- **Orizontal ABC:** A versus B și A versus C se decid prin **PE/împământarea participă la protecția contra șocului împreună cu dispozitivul de declanșare în sistem TN/TT/IT**; B versus C descrie două obiecte/regimuri diferite, niciunul nu înlocuiește expresia afirmativă a lui A.
- **Reversie/contraexemplu:** Dacă schimbăm tipul de instrument, condiția circuitului ori mărimea fizică, concluzia poate diferi. Nu tratăm norma pentru ampermetru serie drept normă pentru voltmetru paralel, nici funcția RCD drept automat magnetotermică.
- **Stare:** A_PRELIMINARY_SUPPORTED_WITH_SCOPE; ORIGINAL_EXAM_KEY_NOT_CERTIFIED; INDEPENDENT_QA_NOT_RUN; LEARNER_APPROVAL_NO.

## G2-ELEC-053 | AU-8bf5859656e32570
- sha256 8bf5859656e32570e8b91edacd6b9fa30c67f403ae881496558477adfee6886a; gradeID G2-ELEC-053; cheia originală {"G2-ELEC-053":"A"} păstrată.
- **Original:** Puterea activă într-un circuit rezistiv este transformată în principal în:
  - A. energie termică
  - B. energie magnetică stocată permanent
  - C. energie chimică în orice rezistor
- **Sursă de mecanism:** https://openstax.org/books/university-physics-volume-2/pages/9-5-electrical-energy-and-power; exact concept Rezistorul ideal transformă puterea activă în căldură: P=I²R. Secțiune didactică sau BIPM relevantă redeschisă textual pentru această familie.
- **Context:** Identificăm mai întâi obiectul din enunț: puterea activă într-un circuit rezistiv este transformată în principal în. Relația/definiția pozitivă este **Rezistorul ideal transformă puterea activă în căldură: P=I²R**. A corespunde astfel: Puterea activă absorbită de rezistor se disipă preponderent ca energie termică Joule.. B trebuie eliminată/condiționată separat: Rezistorul pur nu stochează permanent energie magnetică.. C trebuie eliminată/condiționată separat: Conversia în energie chimică nu apare în orice rezistor.. Se păstrează ipotezele asupra aparatului și domeniului de aplicare; conceptele de siguranță nu justifică manevre practice fără calificare.
- **Vertical:** A Puterea activă absorbită de rezistor se disipă preponderent ca energie termică Joule.; B Rezistorul pur nu stochează permanent energie magnetică.; C Conversia în energie chimică nu apare în orice rezistor..
- **Orizontal ABC:** A versus B și A versus C se decid prin **Rezistorul ideal transformă puterea activă în căldură: P=I²R**; B versus C descrie două obiecte/regimuri diferite, niciunul nu înlocuiește expresia afirmativă a lui A.
- **Reversie/contraexemplu:** Dacă schimbăm tipul de instrument, condiția circuitului ori mărimea fizică, concluzia poate diferi. Nu tratăm norma pentru ampermetru serie drept normă pentru voltmetru paralel, nici funcția RCD drept automat magnetotermică.
- **Stare:** A_PRELIMINARY_SUPPORTED_WITH_SCOPE; ORIGINAL_EXAM_KEY_NOT_CERTIFIED; INDEPENDENT_QA_NOT_RUN; LEARNER_APPROVAL_NO.

## G2-ELEC-054 | AU-68d55ceab5a81f7e
- sha256 68d55ceab5a81f7e96076c308b350e6117f3104f9474996c5be17637e9296088; gradeID G2-ELEC-054; cheia originală {"G2-ELEC-054":"A"} păstrată.
- **Original:** Într-un circuit ideal pur inductiv, puterea activă medie este:
  - A. zero
  - B. egală cu puterea aparentă
  - C. întotdeauna maximă
- **Sursă de mecanism:** https://openstax.org/books/university-physics-volume-2/pages/15-4-power-in-an-ac-circuit; exact concept Inductor pur ideal are defazaj 90° și putere activă medie zero în AC sinusoidal. Secțiune didactică sau BIPM relevantă redeschisă textual pentru această familie.
- **Context:** Identificăm mai întâi obiectul din enunț: într-un circuit ideal pur inductiv, puterea activă medie este. Relația/definiția pozitivă este **Inductor pur ideal are defazaj 90° și putere activă medie zero în AC sinusoidal**. A corespunde astfel: Inductorul ideal stochează și returnează energia în câmp; media P pe ciclu sinusoidal este zero.. B trebuie eliminată/condiționată separat: S=UI poate fi nenulă când P medie este zero.. C trebuie eliminată/condiționată separat: P activă maximă nu este specifică inductanței ideale pure.. Se păstrează ipotezele asupra aparatului și domeniului de aplicare; conceptele de siguranță nu justifică manevre practice fără calificare.
- **Vertical:** A Inductorul ideal stochează și returnează energia în câmp; media P pe ciclu sinusoidal este zero.; B S=UI poate fi nenulă când P medie este zero.; C P activă maximă nu este specifică inductanței ideale pure..
- **Orizontal ABC:** A versus B și A versus C se decid prin **Inductor pur ideal are defazaj 90° și putere activă medie zero în AC sinusoidal**; B versus C descrie două obiecte/regimuri diferite, niciunul nu înlocuiește expresia afirmativă a lui A.
- **Reversie/contraexemplu:** Dacă schimbăm tipul de instrument, condiția circuitului ori mărimea fizică, concluzia poate diferi. Nu tratăm norma pentru ampermetru serie drept normă pentru voltmetru paralel, nici funcția RCD drept automat magnetotermică.
- **Stare:** A_PRELIMINARY_SUPPORTED_WITH_SCOPE; ORIGINAL_EXAM_KEY_NOT_CERTIFIED; INDEPENDENT_QA_NOT_RUN; LEARNER_APPROVAL_NO.

## Regresii relevante
- Măsurarea rezistenței numai în circuit fără alimentare; verificarea măsurătorilor cu instrumente reale cere respectarea manualului și măsuri de siguranță, care nu sunt reproduse aici.
- RCCB ≠ RCBO, diferențial ≠ supracurent; «PE» singur nu garantează automat protecția la atingere în orice TN/TT/IT.
- Proveniența enunțurilor G2 ca XLSX oficial este un risc distinct de corectitudinea fizicii. Fără schimbări de chei/master/HTML/APK/main.
