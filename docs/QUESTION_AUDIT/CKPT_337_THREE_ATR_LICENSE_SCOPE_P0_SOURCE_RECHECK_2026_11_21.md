# CKPT-337 | 3 noi controale: contestații ATR, ATR temporar, vizarea autorizării | 2026-11-21

## Execuție și proveniență
- Parent HEAD: 1dd7f0c206cdd2d0778c0b426454b001a35a2f2b; PR #7 Draft. Enunțurile și toate A/B/C sunt cele documentate anterior din originalele ANRE XLSX în V207/V209 (nu s-a repetat citirea fizică a XLSX aici).
- Sursa 1 accesată efectiv: Ordinul ANRE 74/2014, art. 2 alin. (2)-(3), Portalul Legislativ https://legislatie.just.ro/Public/DetaliiDocument/243569 .
- Sursa 2 accesată efectiv: Regulamentul de racordare 59/2013, art. 2, 8, 22 și anexele, cu trimiteri la Ordinul 15/2026: https://legislatie.just.ro/Public/DetaliiDocumentAfis/310640 .
- Sursa 3 accesată efectiv: Regulamentul de autorizare aprobat prin Ordinul ANRE 66/2023, art. 30 și 37 (pagina indică și modificări 2024): https://legislatie.just.ro/Public/DetaliiDocument/288046 .

## QABC-0284 / G1-LEG-020 | Contestarea ATR
- Original rând 27: «Eventualele contestaţii ale avizelor tehnice de racordare se rezolvă de către:» A «organele ierarhice ale emitentului»; B «operatorul de distribuţie care a emis avizul»; C «ANRE». Barem importat A, păstrat.
- Art. 2 alin. (2): utilizatorul poate contesta ATR la **operatorul de rețea emitent** în 30 zile de la comunicare. Art. 2 alin. (3): contestația este soluționată în maximum 30 zile calendaristice de către **o comisie înființată la nivelul operatorului de rețea**. Context imediat: art. 2(1) despre conținutul-cadru al ATR; art. 2(4) abrogat.
- A nu este formularea exactă a mecanismului special: simpla expresie «organe ierarhice» poate crea suprapunere lingvistică neprecizată. B desemnează instituția la nivelul căreia funcționează comisia și este candidatul direct susținut. C (ANRE) nu este acea etapă inițială de contestație.
- **Candidat B**, cu rezervă pentru interpretarea semantică a lui A și ediție/examen. Status HOLD, nu regradat.

## QABC-0288 / G1-LEG-024 | ATR pentru un loc nou sau temporar
- Original rând 31: «Obţinerea avizului tehnic de racordare de către un utilizator:» A «nu este obligatorie pentru o durata mai mică de 6 luni»; B «nu este obligatorie pentru o putere ceruta sub 100 kW»; C «este obligatorie pentru orice loc de consum/producere nou». Barem importat A, păstrat.
- Regulamentul 59/2013 art. 2(1) include cererile pentru loc nou de consum/producere în sfera racordării la rețeaua publică; art. 8 organizează cererile pe competența operatorilor; art. 22 alin. (3) se referă expres la **avizul tehnic de racordare al locului temporar și expirarea valabilității lui**, deci nu oferă o excepție automată pentru durate sub șase luni.
- A nu are dovadă de exceptare bazată exclusiv pe 6 luni, iar art. 22(3) este contraindiciu. B nu rezultă din regula competențelor pe putere (50 MW în art. 8), care nu este o scutire de ATR. C este candidat doar pentru **locul nou racordat la rețele electrice de interes public, în domeniul regulamentului**; «orice» fără acest domeniu poate depăși textul.
- **Candidat C condiționat de domeniul public și de eventuale regimuri speciale**, nu A automat, dar unicitatea și actualitatea legală integrală sunt încă deschise.

## QABC-0296 / G1-LEG-032 | Vechimea autorizației ≠ contravenție dovedită
- Original rând 39: «ANRE poate aplica sancţiuni contravenţionale unui electrician autorizat pentru:» A «Comiterea unei fapte prevăzute în Regulamentul de autorizare ca fiind interzisă»; B «Desfăşurarea activităţii în baza unei adeverințe (legitimații) de electrician autorizat emisă în urmă cu 4 ani»; C «Proiectarea instalaţiei electrice a unei locuinţe în baza unei autorizaţii de tip II A». Barem importat B, păstrat.
- Regulamentul aprobat prin Ordinul 66/2023, art. 30(1): **vizarea autorizației de electrician se realizează în termen de 5 ani** de la emitere sau ultima vizare. Prin urmare, simpla dată de emitere de acum 4 ani nu dovedește depășirea intervalului. Art. 18 poate restrânge activitatea dacă există un motiv real de nevizare, care nu e enunțat.
- A: trebuie indicat temeiul contravențional specific pentru interdicția încălcată, nu presupus că orice interdicție este sancționabilă automat. B: vechimea de 4 ani în sine nu certifică o contravenție. C: tipul II A trebuie raportat la competența exactă și caracteristicile instalației, nu exclus doar pentru că este locuință.
- **Nicio variantă unică aprobată** din această evidență. Se păstrează HOLD și verificare expresă a încadrării contravenționale + competenței.

## Gate / QA
- Au fost reconsultate trei pagini normative oficiale și condițiile obiectului din enunț; nu s-au executat teste de aplicație. Acesta este review al aceluiași asistent, **NU un reviewer juridic/lingvistic independent**.
- Nu a fost probată ediția completă aplicabilă examenului ANRE 2026 ori cheia oficială pentru vreun ID. **136/136 semantic holds încă OPEN; 0/822 learner approved.**
- Cheile inițiale A/A/B pentru aceste trei cazuri nu au fost schimbate. Nicio editare a întrebărilor, HTML, APK, branch main; fără merge/release.
