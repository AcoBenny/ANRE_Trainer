# CKPT-244 | GFR 15 QABC distincte + reutilizare exactă între grade | 2026-11-19

## Proveniență și limite
- **Sursa originală:** V73 blob `c027d417a8e4e605c830b2016fb55b099b8d130b`. **Registru inițial:** V122 blob `2bc29bddbe6db3fc1026b96b247153e5b8e030c0`.
- **15 analize originale G1** pe enunț + A/B/C, cu interpretare contextuală, alternative, excepții și surse documentate.
- 15 potriviri Grade II exacte pentru întrebare+A+B+C+barem, dintre care 5 aveau deja dovezi și au fost lăsate byte-identic: G2-ELEC-252 (V92); G2-ELEC-298 (V92); G2-ELEC-350 (V87); G2-ELEC-358 (V82); G2-ELEC-372 (V87). Alte 10 au primit numai referință la analiza G1, **nu revizuire de sursă independentă**.
- **25 rânduri cu metadate nou documentate**, 134 -> 109 fără verificare focalizată; 822 ID-uri canonice intacte.
- Acces real la surse: 8 pagini HTML deschise; 7 doar rezultate indexate. Nu au fost accesate paginile integrale ale acestora din urmă. Niciuna dintre acestea nu reprezintă autentificarea baremului oficial ANRE 2026.
- 50 de rânduri de CSV serializate neuniform deja moștenite în V122 rămân byte-identice. Nu se corectează automat fără validare de parser și conținut.

## Fișe și legături verificabile

### G1-ELE-109 / G2-ELEC-252
- **Enunț original:** În sens general, actualizarea unui fond reprezintă:
- **A:** calculul valorii acestui fond la un anumit an ales ca referinţă;
- **B:** calculul valorii acestui fond la N ani înainte de PIF;
- **C:** calculul valorii acestui fond la N ani după PIF.
- **Barem importat nemodificat:** A
- **Analiză A/B/C și contraexemplu:** A descrie actualizarea financiară la un an de referință ales, nu obligatoriu exact N ani înainte sau după PIF. B și C impun momente particulare și nu definesc sensul general. Sursa tratează fluxuri financiare, nu explică independent terminologia «fond» din item; calificare de vocabular rămasă.
- **Sursă candidat:** https://www.treasury.act.gov.au/capital-framework/prove/detailed-technical-guidance/economic-appraisal/appraisal-methodology
- **Locator:** Appraisal methodology > base year and discounting future cashflows
- **Acces real:** HTML_OPENED; nu constituie cheie ANRE2026 certificată sau QA independent.

### G1-ELE-114 / G2-ELEC-256
- **Enunț original:** Inductanţa de serviciu ( lineică) a unei linii electrice lungi este definită prin:
- **A:** inductanţa uniform răspândită l, definită prin puterea reactivă absorbită într-un element de linie infinit mic
- **B:** inductanţa uniform răspândită l, definită prin  puterea reactivă produsă de un element de linie infinit mic
- **C:** pierderile Joule disipate într-un element de linie infinit mic
- **Barem importat nemodificat:** A
- **Analiză A/B/C și contraexemplu:** În modelul liniei CA, inductanța linică L′ este un parametru serie, care absoarbe Q_L≈ωL′·dx·I²: interpretarea A. B «produce» este atribuibilă capacității linice în convenția uzuală; C definește disiparea rezistivă. Însă L′ nu se definește riguros numai prin putere reactivă fără I, frecvența și elementul dx; marcaj MODEL_CONDITIONAL.
- **Sursă candidat:** https://www.electronicsguide.net/systems-and-technologies/power-electronics/power-system-analysis/transmission-and-distribution-lines/
- **Locator:** Per unit length series inductance reactive consumption and shunt capacitance reactive production
- **Acces real:** SEARCH_INDEX_ONLY; nu constituie cheie ANRE2026 certificată sau QA independent.

### G1-ELE-150 / G2-ELEC-288
- **Enunț original:** O reţea electricã trifazatã de medie tensiune are neutrul transformatoarelor tratat prin bobina. Pentru regimul normal de funcţionare sa se precizeze efectul bobinei:
- **A:** deplasarea neutrului
- **B:** creşterea curenţilor de scurtcircuit
- **C:** nici un efect
- **Barem importat nemodificat:** C
- **Analiză A/B/C și contraexemplu:** C «nici un efect» este intenția pentru rețea trifazată sănătoasă/simetrică: bobina Petersen intervine decisiv la defect monofazat la pământ. A deplasarea neutrului poate totuși apărea în funcționare normală din dezechilibre de capacități, mai ales aproape de rezonanță; B «creșterea curenților de scurtcircuit» contrazice scopul compensării. Deci C nu este universal în condiții reale dezechilibrate.
- **Sursă candidat:** https://www.a-eberle.de/en/info-letter/info-brief-nr-3/
- **Locator:** Neutral-Point Treatment and E-Coil Settings; passages §105-120
- **Acces real:** HTML_OPENED; nu constituie cheie ANRE2026 certificată sau QA independent.

### G1-ELE-160 / G2-ELEC-298
- **Enunț original:** Motoarele sincrone se utilizează rar pentru antrenarea mecanismelor de servicii proprii din centralele electrice
- **A:** deoarece nu permit variaţia turaţiei în limite largi
- **B:** numai deoarece excitatoarea cu colector din circuitul acestora este un element puţin fiabil
- **C:** deoarece au randament mai mic decât al celorlalte tipuri de motoare
- **Barem importat nemodificat:** A
- **Analiză A/B/C și contraexemplu:** A explică de ce mașina sincronă tradițională alimentată la frecvență fixă nu oferă variație largă de turație fără convertizor. B «numai excitatoarea» e o exclusivitate falsă și nu acoperă mașini fără perii; C randamentul mai mic nu este general adevărat. Cu VFD există variație largă, astfel descriere istorică/condiționată.
- **Sursă candidat:** https://www.festo.com/gb/en/e/blog/in-practice/synchronous-motors-types-benefits-applications-id_3727625
- **Locator:** Classic Synchronous Motor and Constant Speed Under Load
- **Acces real:** HTML_OPENED; nu constituie cheie ANRE2026 certificată sau QA independent.

### G1-ELE-161 / G2-ELEC-299
- **Enunț original:** Nivelul de tensiune în sistem se reglează
- **A:** încărcarea generatoarelor cu putere activa
- **B:** numai prin încărcarea generatoarelor cu putere reactiva
- **C:** prin utilizare de compensatoare
- **Barem importat nemodificat:** C
- **Analiză A/B/C și contraexemplu:** C compensatoarele (capacitive/inductive, SVC/STATCOM) pot modifica schimbul Q și susține tensiunea. A încărcarea activă afectează și căderi de tensiune în rețele rezistive, dar nu este metoda principală în rețele de transport. B «numai» prin încărcarea Q a generatoarelor exclude alte dispozitive. Sursa IEC este doar indexată, nu se certifică ediția ANRE.
- **Sursă candidat:** https://www.iteh.fr/catalog/standards/iec/17415040-a9d5-4255-8b4d-90a612c4702a/iec-tr-63575-2025
- **Locator:** Reactive power shunt compensators and voltage control
- **Acces real:** SEARCH_INDEX_ONLY; nu constituie cheie ANRE2026 certificată sau QA independent.

### G1-ELE-171 / G2-ELEC-308
- **Enunț original:** Pentru limitarea curenţilor de scurtcircuit, puterea totalã instalatã într-o staţie trebuie:
- **A:** mărită
- **B:** micşorată
- **C:** divizatã în mai multe unităţi
- **Barem importat nemodificat:** C
- **Analiză A/B/C și contraexemplu:** C împărțirea aportului de putere pe secții/transformatoare poate limita curentul de scurtcircuit dacă și conexiunile electrice sunt separate/operate cu cuple deschise. A mărirea puterii conectate crește în general contribuțiile, B micșorarea puterii totale ar putea reduce curentul dar este o altă măsură ce face formularea «trebuie divizată» discutabilă. Divizarea nominală fără separare fizică nu reduce Isc.
- **Sursă candidat:** https://www.sciencedirect.com/topics/engineering/bus-section-circuit-breaker
- **Locator:** Splitting transformer-fed busbars and open sectionalizing breaker limits fault level
- **Acces real:** SEARCH_INDEX_ONLY; nu constituie cheie ANRE2026 certificată sau QA independent.

### G1-ELE-207 / G2-ELEC-343
- **Enunț original:** Comparativ cu un transformator, autotransformatorul are tensiunea de scurtcircuit:
- **A:** mai mare
- **B:** egală
- **C:** mai mică
- **Barem importat nemodificat:** C
- **Analiză A/B/C și contraexemplu:** C un autotransformator comparabil are de regulă impedanță/tensiune de scurtcircuit mai mică decât un transformator cu două înfășurări pentru raport, bază și proiect echivalente. A și B nu sunt caracteristice modelului comparat. Tensiunea procentuală de scurtcircuit depinde de bază și de proiect, deci nu este comparație absolută între dispozitive arbitrare.
- **Sursă candidat:** https://eepower.com/technical-articles/constructing-and-operating-an-autotransformer/
- **Locator:** Low Impedance section, formula Z_A=Z×(Vp−Vs)/Vp
- **Acces real:** HTML_OPENED; nu constituie cheie ANRE2026 certificată sau QA independent.

### G1-ELE-214 / G2-ELEC-350
- **Enunț original:** Rolul conservatorului de ulei la transformatoarele de forţa este:
- **A:** de a asigura o suprafaţa de contact a uleiului cu aerul mai mica
- **B:** numai  de a asigura spaţiul necesar dilatării si contractării uleiului
- **C:** de a face posibila umplerea cu ulei a transformatorului
- **Barem importat nemodificat:** A
- **Analiză A/B/C și contraexemplu:** A reducerea suprafeței de contact ulei/aer este un rol real al conservatorului. B «numai» dilatare/contractare este fals exclusiv, conservatorul are și rol de protecție; C umplerea inițială nu este scopul său definitoriu. Expansiunea există totuși, de aceea explicația nu trebuie să nege această funcție.
- **Sursă candidat:** https://www.cnrockwill.com/technical/oil-immersed-transformer-installation-operation-manual
- **Locator:** Conservator section §381-392: reduced oil-air contact, expansion, moisture breather
- **Acces real:** HTML_OPENED; nu constituie cheie ANRE2026 certificată sau QA independent.

### G1-ELE-222 / G2-ELEC-358
- **Enunț original:** Susceptanţa unui circuit de curent alternativ sinusoidal este inversul:
- **A:** impedanţei
- **B:** rezistenţei
- **C:** reactanţei
- **Barem importat nemodificat:** C
- **Analiză A/B/C și contraexemplu:** C «inversul reactanței» poate fi menționat informal ca susceptanță a unui element pur reactiv, dar în general B=-X/(R²+X²), nu 1/X; pentru R=0 este -1/X, deci lipsește și convenția de semn. A inversul impedanței este admitanța complexă, B inversul rezistenței (pur rezistive) conductanța. Se marchează SOURCE_CONCEPT_CONFLICT; nu se aprobă cheia C universal.
- **Sursă candidat:** https://phys.libretexts.org/Bookshelves/Electricity_and_Magnetism/Electricity_and_Magnetism_%28Tatum%29/13%253A_Alternating_Current/13.06%253A_Admittance
- **Locator:** Admittance Y=1/(R+jX)=G+jB; B=-X/(R²+X²)
- **Acces real:** SEARCH_INDEX_ONLY; nu constituie cheie ANRE2026 certificată sau QA independent.

### G1-ELE-232 / G2-ELEC-368
- **Enunț original:** Sistemele simetrice de fazori în care se descompun sistemele de tensiuni sau de curenţi dezechilibraţi:
- **A:** corespund unor realităţi fizice
- **B:** reprezintă artificii de calcul
- **C:** numai sistemul direct corespunde unei realităţi fizice
- **Barem importat nemodificat:** B
- **Analiză A/B/C și contraexemplu:** B componentele simetrice sunt o transformare matematică utilă pentru reprezentarea sistemului dezechilibrat, nu trei sisteme de conductoare separate. A «realități fizice» poate fi înțeles ca moduri fizic măsurabile/de observat prin efectele negative-sequence, deci termenii sunt filosofic ambigui; C «numai sistemul direct» este prea exclusiv. Candidat B, nu semnătură finală.
- **Sursă candidat:** https://www.dacpol.eu/en/knowledge-base/post/symmetrical-components-method-positive-negative-and-zero-sequence.html
- **Locator:** Positive/negative/zero-sequence mathematical decomposition of three phase phasors
- **Acces real:** SEARCH_INDEX_ONLY; nu constituie cheie ANRE2026 certificată sau QA independent.

### G1-ELE-233 / G2-ELEC-369
- **Enunț original:** Sistemul de tensiuni al unei reţele racordate la un generator electric care produce tensiuni electromotoare simetrice:
- **A:** este întotdeauna simetric
- **B:** este simetric chiar dacă fazele sunt neegal încărcate
- **C:** este simetric dacă fazele sunt egal încărcate
- **Barem importat nemodificat:** C
- **Analiză A/B/C și contraexemplu:** C faze egal încărcate susțin tensiuni simetrice în modelul generatorului și impedanțelor interne/rețelei simetrice. A «întotdeauna» fals, B «chiar dacă fazele sunt neegal încărcate» poate deveni fals prin căderi inegale; C nu este suficient dacă însăși rețeaua/impedanțele de fază sunt asimetrice. Condiție model nonexplicită.
- **Sursă candidat:** https://www.sandroronca.it/SistemiTrifase/ThreePhaseSystems.html
- **Locator:** Symmetrical three-phase generation and balanced loads; phase voltage drops
- **Acces real:** SEARCH_INDEX_ONLY; nu constituie cheie ANRE2026 certificată sau QA independent.

### G1-ELE-234 / G2-ELEC-370
- **Enunț original:** Transformatoarele de măsurare de tensiune se construiesc pentru tensiuni în secundar de:
- **A:** 10 V
- **B:** 50 V
- **C:** 100 V
- **Barem importat nemodificat:** C
- **Analiză A/B/C și contraexemplu:** C 100 V este standard industrial întâlnit la transformatoare de tensiune; A 10V și B 50V nu sunt opțiunile standard din setul dat. Nu este singura valoare admisă: 110 V sau 100/√3 V apar în alte configurări, deci formularea nu are exclusivitate generală.
- **Sursă candidat:** https://www.bticino.com/products/ime-measurement-solutions/transformers/features-and-benefits
- **Locator:** Voltage transformers: secondary standard 100V; other values on request
- **Acces real:** HTML_OPENED; nu constituie cheie ANRE2026 certificată sau QA independent.

### G1-ELE-236 / G2-ELEC-372
- **Enunț original:** Supratensiunile de trăsnet pot fi:
- **A:** numai directe
- **B:** induse
- **C:** de rezonanta sau de ferorezonanţa
- **Barem importat nemodificat:** B
- **Analiză A/B/C și contraexemplu:** B supratensiuni induse sunt posibile prin descărcări atmosferice din apropiere. A «numai directe» este fals, C rezonanță/ferorezonanță nu constituie clasificarea trăsnetului. Există și trăsnet direct, deci nu se deduce că B este singura formă posibilă.
- **Sursă candidat:** https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/iet-gtd.2014.1129
- **Locator:** Lightning overvoltages are due to direct and indirect nearby strokes; induced surges
- **Acces real:** SEARCH_INDEX_ONLY; nu constituie cheie ANRE2026 certificată sau QA independent.

### G1-ELE-240 / G2-ELEC-376
- **Enunț original:** Transformatoarele cu ulei prevăzute cu conservator prezintă următoarele caracteristici:
- **A:** dilatarea lichidului este compensată prin deformarea elastică a pereţilor cuvei;
- **B:** împiedică, dar nu elimină, pătrunderea umidităţii în interiorul rezervorului de expansiune;
- **C:** asigură facilităţi în modul de dispunere a bornelor şi deci de racordare la reţea.
- **Barem importat nemodificat:** B
- **Analiză A/B/C și contraexemplu:** B sistemul de conservator cu respirator/silica-gel reduce umezeala care intră odată cu aerul, dar nu garantează absență absolută. A deformarea pereților cuvei ar caracteriza un design etanș flexibil, nu conservatorul obișnuit; C nu este rolul său principal. Variantele cu membrană schimbă contactul direct aer/ulei și impun precizarea tipului.
- **Sursă candidat:** https://www.cnrockwill.com/technical/oil-immersed-transformer-installation-operation-manual
- **Locator:** Conservator breathes via dehydrating breather; reduces air moisture ingress
- **Acces real:** HTML_OPENED; nu constituie cheie ANRE2026 certificată sau QA independent.

### G1-ELE-241 / G2-ELEC-377
- **Enunț original:** Transformatoarele de măsurare a curenţilor se construiesc pentru curenţi secundari de:
- **A:** 1 sau 5 A
- **B:** 5 sau 10 A
- **C:** 1 sau 10 A
- **Barem importat nemodificat:** A
- **Analiză A/B/C și contraexemplu:** A 1 A sau 5 A sunt valori secundare uzuale standard pentru transformatoare de curent. B 5/10 și C 1/10 implică 10A care nu este valoare standard comună la produsele analizate. Alte standarde speciale pot include alte valori; afirmația nu este universal exhaustivă.
- **Sursă candidat:** https://www.bticino.com/products/ime-measurement-solutions/transformers/features-and-benefits
- **Locator:** Current transformers CT: 5 A or 1 A rated secondary per IEC 61869
- **Acces real:** HTML_OPENED; nu constituie cheie ANRE2026 certificată sau QA independent.

## Rețineri și blocaje
- G1-ELE-150: în regim ideal normal bobina nu are efect, dar dezechilibrele capacitive pot influența punctul neutru, chiar fără defect.
- G1-ELE-171: simpla divizare administrativă a puterii instalate nu reduce curentul de scurtcircuit; este necesară separare electrică adecvată.
- G1-ELE-222: baremul C este discutabil la nivelul definiției susceptanței generale și al semnului; B=-X/(R²+X²) pentru Z=R+jX.
- G1-ELE-234: 100 V este nominal uzual, nu singurul standard din toate sistemele.
- Pentru toate fișele: QA tehnic/lingvistic independent, ediția oficială ANRE, semnătură calificată NOT_RUN/UNVERIFIED; approved_for_learning=NO; key_change_authorized=NO.
- Fără modificări QABC/HTML/APK, main, merge/release. PR #7 trebuie să rămână Draft.
