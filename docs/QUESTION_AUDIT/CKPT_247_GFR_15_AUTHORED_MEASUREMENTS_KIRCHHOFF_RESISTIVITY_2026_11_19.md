# CKPT-247 | 15 întrebări didactice: măsurări, Kirchhoff, unități și rezistivitate | 2026-11-19

## Autenticitate și bază
- Întrebările G2-ELEC-032..046 sunt 15/15 tip `TRAINER_AUTHORED_NOT_OFFICIAL_QUESTION_SAMPLE` conform V63 blob `18029444b21ad0cd805d69f1ae9ea9e1747ee170`; nu sunt subiecte autentificate ANRE. V73 canonical blob `c027d417a8e4e605c830b2016fb55b099b8d130b`, V125 baseline blob `19ee3dbb038ff37a443ccf9b6936c72d62b10fff`.
- 15 verificări de fizică cu surse OpenStax, National Instruments/NI, NIST, Fluke; fiecare card conține originalul A/B/C, limita modelului și dovada legată de obiectul său.
- **A nu se confunda 55 de exerciții didactice create pentru trainer, dovedite explicit de V63, cu întrebările originale oficiale sau cu cele 136 încadrate în tematica ANRE 2023 în V73.** Proveniența nu se stabilește doar din denumirea `source_file`.

### G2-ELEC-032
- **Întrebarea originală:** Generatorul electric transformă în principal:
- **A:** energia mecanică în energie electrică
- **B:** energia electrică în căldură
- **C:** energia chimică în lumină
- **Barem importat, nemodificat:** A
- **Analiză A/B/C și limite:** A generatorul convertește predominant energie mecanică în energie electrică prin inducție; B transformarea în căldură este o pierdere, C conversia chimică-lumină nu descrie mașina. «În principal» permite pierderile și regimurile reversibile.
- **Sursă tehnică:** https://openstax.org/books/university-physics-volume-2/pages/13-1-faradays-law
- Proveniență V63: TRAINER_AUTHORED_NOT_OFFICIAL_QUESTION_SAMPLE. Nu este întrebare oficială ANRE autentificată; QA independent NOT_RUN.

### G2-ELEC-033
- **Întrebarea originală:** Un multimetru setat pentru măsurarea tensiunii se conectează în mod normal:
- **A:** în paralel cu elementul măsurat
- **B:** în serie cu elementul
- **C:** doar la pământ
- **Barem importat, nemodificat:** A
- **Analiză A/B/C și limite:** A voltmetrul/multimetrul pe tensiune se conectează în paralel la bornele elementului; B în serie este conexiunea tipică pentru curent și poate modifica circuitul; C doar la pământ nu măsoară diferența între borne. Aparatul și domeniul de măsură trebuie alese după categorie și tensiune.
- **Sursă tehnică:** https://www.ni.com/en/shop/electronic-test-instrumentation/digital-multimeters/dmm-measurement-fundamentals.html
- Proveniență V63: TRAINER_AUTHORED_NOT_OFFICIAL_QUESTION_SAMPLE. Nu este întrebare oficială ANRE autentificată; QA independent NOT_RUN.

### G2-ELEC-034
- **Întrebarea originală:** Un ampermetru se conectează în mod normal:
- **A:** în serie cu circuitul
- **B:** în paralel pe sursă
- **C:** doar între fază și PE
- **Barem importat, nemodificat:** A
- **Analiză A/B/C și limite:** A ampermetrul convențional se introduce în serie în ramura măsurată; B legarea directă în paralel peste sursă poate produce scurtcircuit periculos; C legarea între fază și PE nu este procedura de măsurare a curentului. Excepție: cleștele ampermetric neintruziv măsoară fără întreruperea conductoarelor, nu este montajul convențional cerut.
- **Sursă tehnică:** https://www.ni.com/en/shop/electronic-test-instrumentation/digital-multimeters/dmm-measurement-fundamentals.html
- Proveniență V63: TRAINER_AUTHORED_NOT_OFFICIAL_QUESTION_SAMPLE. Nu este întrebare oficială ANRE autentificată; QA independent NOT_RUN.

### G2-ELEC-035
- **Întrebarea originală:** Un ohmmetru se folosește corect pentru măsurarea unei rezistențe atunci când circuitul este:
- **A:** deconectat de la alimentare
- **B:** alimentat la tensiunea nominală
- **C:** scurtcircuitat
- **Barem importat, nemodificat:** A
- **Analiză A/B/C și limite:** A ohmmetrul pe circuit deconectat și verificat fără tensiune; B sub tensiune nu este permis deoarece afectează rezultatul și poate avaria instrumentul; C scurtcircuitarea poate masca rezistența reală. Pentru măsurări precise elementele se pot izola de căile paralele.
- **Sursă tehnică:** https://www.fluke.com/en-us/learn/blog/digital-multimeters/how-to-measure-resistance
- Proveniență V63: TRAINER_AUTHORED_NOT_OFFICIAL_QUESTION_SAMPLE. Nu este întrebare oficială ANRE autentificată; QA independent NOT_RUN.

### G2-ELEC-036
- **Întrebarea originală:** Un scurtcircuit este caracterizat ideal prin:
- **A:** impedanță foarte mică și curent foarte mare
- **B:** impedanță foarte mare și curent nul
- **C:** putere reactivă nulă obligatoriu
- **Barem importat, nemodificat:** A
- **Analiză A/B/C și limite:** A scurtcircuitul are impedanță de defect mică și curent potențial mare, limitat de impedanța sursei/rețelei; B mare impedanță și curent nul descriu circuit deschis, nu scurt; C Q=0 nu este o consecință generală. „Foarte mare” depinde de sursă și protecții.
- **Sursă tehnică:** https://openstax.org/books/university-physics-volume-2/pages/10-3-kirchhoffs-rules
- Proveniență V63: TRAINER_AUTHORED_NOT_OFFICIAL_QUESTION_SAMPLE. Nu este întrebare oficială ANRE autentificată; QA independent NOT_RUN.

### G2-ELEC-037
- **Întrebarea originală:** Legea lui Kirchhoff a curenților se aplică unui nod și exprimă că:
- **A:** suma algebrică a curenților din nod este zero
- **B:** toate tensiunile sunt zero
- **C:** puterea activă este întotdeauna zero
- **Barem importat, nemodificat:** A
- **Analiză A/B/C și limite:** A KCL afirmă suma algebrică a curenților într-un nod =0 (conservarea sarcinii în model concentrat); B nu impune tensiuni zero, C nici putere activă zero. Pentru condiții electromagnetice distribuite se ține cont de curentul de deplasare.
- **Sursă tehnică:** https://openstax.org/books/university-physics-volume-2/pages/10-3-kirchhoffs-rules
- Proveniență V63: TRAINER_AUTHORED_NOT_OFFICIAL_QUESTION_SAMPLE. Nu este întrebare oficială ANRE autentificată; QA independent NOT_RUN.

### G2-ELEC-038
- **Întrebarea originală:** Legea lui Kirchhoff a tensiunilor exprimă, pe un contur închis, că:
- **A:** suma algebrică a tensiunilor este zero
- **B:** suma curenților este întotdeauna zero
- **C:** toate rezistențele sunt egale
- **Barem importat, nemodificat:** A
- **Analiză A/B/C și limite:** A KVL în aproximația circuitului concentrat: suma algebrică a tensiunilor pe un contur închis este zero; B suma curenților nu este KVL, C egalitatea rezistențelor nu rezultă. Dacă există flux magnetic variabil ce străbate conturul, formularea simplă necesită includerea fem induse și poate fi incompletă.
- **Sursă tehnică:** https://openstax.org/books/university-physics-volume-2/pages/10-3-kirchhoffs-rules
- Proveniență V63: TRAINER_AUTHORED_NOT_OFFICIAL_QUESTION_SAMPLE. Nu este întrebare oficială ANRE autentificată; QA independent NOT_RUN.

### G2-ELEC-039
- **Întrebarea originală:** Conductanța electrică este inversul:
- **A:** rezistenței
- **B:** tensiunii
- **C:** puterii
- **Barem importat, nemodificat:** A
- **Analiză A/B/C și limite:** A conductanța G a unui rezistor ohmic =1/R în siemens; B inversul tensiunii nu este conductanță, C inversul puterii nici atât. Pentru componente AC complexe inversul impedanței este admitanța Y=1/Z, nu conductanța pură.
- **Sursă tehnică:** https://openstax.org/books/university-physics-volume-2/pages/9-3-resistivity-and-resistance
- Proveniență V63: TRAINER_AUTHORED_NOT_OFFICIAL_QUESTION_SAMPLE. Nu este întrebare oficială ANRE autentificată; QA independent NOT_RUN.

### G2-ELEC-040
- **Întrebarea originală:** Unitatea conductanței este:
- **A:** siemens (S)
- **B:** tesla (T)
- **C:** henry (H)
- **Barem importat, nemodificat:** A
- **Analiză A/B/C și limite:** A siemens (S) unitate de conductanță; B tesla (T) este unitatea inducției magnetice, C henry (H) inductanței. 1 S=1/Ω.
- **Sursă tehnică:** https://www.nist.gov/pml/special-publication-811/nist-guide-si-chapter-4-two-classes-si-units-and-si-prefixes
- Proveniență V63: TRAINER_AUTHORED_NOT_OFFICIAL_QUESTION_SAMPLE. Nu este întrebare oficială ANRE autentificată; QA independent NOT_RUN.

### G2-ELEC-041
- **Întrebarea originală:** Capacitatea electrică se măsoară în:
- **A:** farazi (F)
- **B:** henry (H)
- **C:** tesla (T)
- **Barem importat, nemodificat:** A
- **Analiză A/B/C și limite:** A capacitatea se măsoară în farazi F=C/V; B henry este inductanță, C tesla inducție magnetică. Faradul nu este coulombul (unitate de sarcină).
- **Sursă tehnică:** https://www.nist.gov/pml/special-publication-811/nist-guide-si-chapter-4-two-classes-si-units-and-si-prefixes
- Proveniență V63: TRAINER_AUTHORED_NOT_OFFICIAL_QUESTION_SAMPLE. Nu este întrebare oficială ANRE autentificată; QA independent NOT_RUN.

### G2-ELEC-042
- **Întrebarea originală:** Inductanța se măsoară în:
- **A:** henry (H)
- **B:** farad (F)
- **C:** siemens (S)
- **Barem importat, nemodificat:** A
- **Analiză A/B/C și limite:** A inductanța se măsoară în henry H=V·s/A; B farad măsoară capacitatea, C siemens conductanța. Formula U=L di/dt în convenție pasivă.
- **Sursă tehnică:** https://www.nist.gov/pml/special-publication-811/nist-guide-si-chapter-4-two-classes-si-units-and-si-prefixes
- Proveniență V63: TRAINER_AUTHORED_NOT_OFFICIAL_QUESTION_SAMPLE. Nu este întrebare oficială ANRE autentificată; QA independent NOT_RUN.

### G2-ELEC-043
- **Întrebarea originală:** Densitatea de curent este raportul dintre:
- **A:** curent și aria secțiunii
- **B:** tensiune și lungime
- **C:** putere și timp
- **Barem importat, nemodificat:** A
- **Analiză A/B/C și limite:** A densitatea medie a curentului J=I/A prin suprafața transversală în conductor uniform; B U/l exprimă intensitate de câmp E în V/m, C putere/timp nu este densitate. Pentru distribuții neuniforme, J este locală și I=∫J·dA, nu doar simplul raport uniform.
- **Sursă tehnică:** https://openstax.org/books/university-physics-volume-2/pages/9-3-resistivity-and-resistance
- Proveniență V63: TRAINER_AUTHORED_NOT_OFFICIAL_QUESTION_SAMPLE. Nu este întrebare oficială ANRE autentificată; QA independent NOT_RUN.

### G2-ELEC-044
- **Întrebarea originală:** Rezistența unui conductor omogen este proporțională cu:
- **A:** lungimea și rezistivitatea
- **B:** doar curentul
- **C:** doar tensiunea
- **Barem importat, nemodificat:** A
- **Analiză A/B/C și limite:** A R=ρl/A pentru conductor omogen la temperatură constantă: direct proporțională cu lungimea l și rezistivitatea ρ; B numai curentul și C numai tensiunea nu determină R în model ohmic. Secțiunea A și temperatura contează și ele, iar «proporțională» ține ceilalți parametri constanți.
- **Sursă tehnică:** https://openstax.org/books/university-physics-volume-2/pages/9-3-resistivity-and-resistance
- Proveniență V63: TRAINER_AUTHORED_NOT_OFFICIAL_QUESTION_SAMPLE. Nu este întrebare oficială ANRE autentificată; QA independent NOT_RUN.

### G2-ELEC-045
- **Întrebarea originală:** Rezistența unui conductor omogen este invers proporțională cu:
- **A:** aria secțiunii transversale
- **B:** lungimea
- **C:** rezistivitatea
- **Barem importat, nemodificat:** A
- **Analiză A/B/C și limite:** A din R=ρl/A rezultă dependența inversă de aria secțiunii A, la l,ρ fixate. B lungimea produce proporționalitate directă, C rezistivitatea tot directă. Unitățile trebuie să fie compatibile.
- **Sursă tehnică:** https://openstax.org/books/university-physics-volume-2/pages/9-3-resistivity-and-resistance
- Proveniență V63: TRAINER_AUTHORED_NOT_OFFICIAL_QUESTION_SAMPLE. Nu este întrebare oficială ANRE autentificată; QA independent NOT_RUN.

### G2-ELEC-046
- **Întrebarea originală:** Pentru un conductor metalic, în intervale uzuale, creșterea temperaturii determină de regulă:
- **A:** creșterea rezistenței
- **B:** scăderea rezistenței la zero
- **C:** inversarea polarității
- **Barem importat, nemodificat:** A
- **Analiză A/B/C și limite:** A pentru majoritatea metalelor obișnuite în intervalul normal, ρ(T)≈ρ0(1+αΔT) cu α>0, deci rezistența crește (la geometrie aproximativ fixă). B scade la zero este fals în intervalul dat și C inversarea polarității nu rezultă din temperatură. Materiale speciale și superconductivitatea nu sunt în domeniu.
- **Sursă tehnică:** https://openstax.org/books/university-physics-volume-2/pages/9-3-resistivity-and-resistance
- Proveniență V63: TRAINER_AUTHORED_NOT_OFFICIAL_QUESTION_SAMPLE. Nu este întrebare oficială ANRE autentificată; QA independent NOT_RUN.

## Blocaje / QA
- G2-ELEC-034: ampermetrul convențional se conectează în serie, dar un clește ampermetric funcționează fără deschiderea ramurii; diferența trebuie păstrată.
- G2-ELEC-035: măsurare rezistență doar după deconectare, verificarea lipsei tensiunii și descărcarea eventuală a condensatoarelor, conform procedurii de siguranță.
- G2-ELEC-038: KVL cere regimul circuitului concentrat sau fem de inducție inclusă la câmpuri variabile.
- 15 rânduri originale documentate; **79 -> 64 fără verificare focalizată**; 822 unice, păstrate în aceeași ordine, numai metadate de evidență actualizate. Alte 807 rânduri identice ca text.
- 50 rânduri CSV preexistente neuniform serializate au rămas byte-identice, fără normalizare ireversibilă.
- Nu există QA independent pe acest lot, nicio ediție/barem oficial ANRE2026 autentificat, niciun rând aprobat pentru învățare; originalele, baremurile, HTML, APK, main și PR #7 Draft sunt păstrate.
