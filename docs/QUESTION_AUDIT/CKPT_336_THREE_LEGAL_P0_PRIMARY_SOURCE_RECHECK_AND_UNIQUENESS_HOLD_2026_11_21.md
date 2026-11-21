# CKPT-336 | 3 verificări juridice noi, fără aprobări sau modificări de barem | 2026-11-21

## Proveniență
- Bază: PR #7 Draft, HEAD anterior 393505b17478dcb83453a86df08adc9da84851ec. Fișele canonice originale au fost recitite din V206/V207, reconciliate anterior cu sursele XLSX în V246. Binarele XLSX nu au fost re-descrise/reverificate în acest pas.
- Surse guvernamentale efectiv accesate: Legea 123/2012, https://legislatie.just.ro/Public/FormaPrintabila/00000G0CDOUQ5TXYOEU0X4Y9QAXWNAF7 ; Regulamentul pentru racordare aprobat prin Ordin 59/2013, formă publică indicând inclusiv Ordinul 15/21.05.2026, https://legislatie.just.ro/Public/DetaliiDocumentAfis/310640 .
- Ediția legală complet consolidată la 21.11.2026 și baremul oficial ANRE de examen nu sunt certificate. Sursele citite sunt o doveză tehnico-juridică focalizată, nu verdict de barem.

## 1. QABC-0279 / G1-LEG-015 | Legea 123 art. 92 vs art. 93
- Original XLSX, rândul 22: «Constituie contravenţie:» A «refuzul clienţilor finali de a permite accesul la grupurile de măsurare»; B «modificarea fără drept a componentelor instalaţiilor energetice»; C «sustragerea de energie electrica». Cheie importată B, NEMODIFICATĂ.
- Context înainte: art. 93(1) pct. 27 descrie alte contravenții, privind nepublicarea/neactualizarea unor date tehnice/comerciale. Focal: art. 93(1) pct. 28 descrie refuzul accesului la grupuri de măsurare ca **o contravenție**. După: pct. 29 tratează săpături/lucrări în zone de protecție fără aviz.
- Verificare A/B/C: A se potrivește contravenției specificate expres la pct. 28. B este clasificată ca **infracțiune** de art. 92 alin. (1), deci nu dovedește categoria cerută. C trebuie verificată în legislația penală aplicabilă; sursa citită nu o instituie aici drept contravenție.
- Candidat juridic: A, nu cheia B. Stare: HOLD. Verificator juridic/lingvistic independent: NOT_RUN.

## 2. QABC-0281 / G1-LEG-017 | Reziliere versus deconectare
- Original XLSX, rândul 24: «Furnizorul de energie electrică este îndreptăţit sã rezilieze contractul de furnizare a energiei electrice în caz de:» A «sustragerea de energie electrică constatată prin hotărâre judecătorească definitivă»; B «racordare ilegală la reţeaua de distribuţie»; C «refuz al clientului final de a constitui garanţia solicitată de furnizor atunci când acesta constată acţiuni menite să denatureze în orice fel indicaţiile echipamentelor de măsurare». Cheie importată B, NEMODIFICATĂ.
- Context: art. 58 alin. (3) este abrogat; alin. (4) enumeră temeiurile de reziliere, inclusiv lit. a) pentru sustragerea constatată prin hotărâre definitivă și lit. c) pentru alte situații prevăzute de lege; alin. (5) reglementează constituirea garanțiilor; alin. (6) tratează solicitarea **deconectării** pentru refuzul garanției.
- Verificare A/B/C: A este **afirmativ susținut** de art. 58(4)a. B nu apare explicit acolo, dar NU poate fi exclusă fără verificarea legilor/reglementărilor incluse în art. 58(4)c. C confundă deconectarea cu rezilierea, care au obiect juridic distinct.
- Concluzie: **A are suport direct, dar unicitatea nu a fost demonstrată**. Nu prezentăm B drept imposibilă și nu declarăm A barem oficial. Stare: HOLD, investigație obligatorie a lit. c.

## 3. QABC-0292 / G1-LEG-028 | Ansamblu de blocuri, nu locuință individuală
- Original XLSX, rândul 35: «În cazul unui ansamblu de blocuri de locuinţe, grupurile de măsurare individuale se poziţionează» A «pe tablourile din apartamente»; B «centralizat, la limita zonei de proprietate asupra terenului, in exteriorul construcţiei»; C «centralizat, la parter sau pe palier». Cheie importată B, NEMODIFICATĂ.
- Context înainte: Anexa nr. 3 pct. 2.2 descrie rețeaua din interiorul ansamblului și locul contoarelor individuale. Focal: pct. 2.3 precizează exact că «grupurile de măsurare individuale se poziționează centralizat, la parter sau pe palier». După: pct. 3 tratează excepția pentru drumurile interioare ce constituie domeniu public.
- Verificare A/B/C: A nu este soluția centralizată din pct. 2.3; B importă condiția de la un obiect diferit (limită de proprietate/locuințe individuale); C coincide cu prevederea specifică ansamblurilor de blocuri.
- Candidat sursă: C, nu cheia B. Stare: HOLD, ediția și baremul oficial încă neverificate.

## QA și limitele execuției
- A fost efectuată recitirea directă a actelor oficiale și confruntarea individuală a obiectului/contexului cu enunțurile și fiecare opțiune. Controlul automat de generare JSON a fost oprit de erori de delimitare/sintaxă; nicio aprobare nu este revendicată din acele încercări.
- **Nu există reviewer juridic sau lingvistic independent în acest pas.** Nu s-au refăcut hashurile binare originale și nu se pretinde audit exhaustiv al tuturor modificărilor normative din 2026.
- 136/136 blocaje semantice rămân deschise; 0/822 aprobări pentru învățare. Cele trei cazuri au dovezi mai puternice, nu sunt închise.
- Numai acest fișier nou de audit trebuie să fie adăugat. Nicio modificare de chei, formulări canonice, HTML, APK, main, merge sau release.
