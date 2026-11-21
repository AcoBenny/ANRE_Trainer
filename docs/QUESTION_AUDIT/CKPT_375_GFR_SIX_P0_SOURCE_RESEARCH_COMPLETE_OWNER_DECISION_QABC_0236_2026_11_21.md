# CKPT-375 | GFR autonom până la poarta unde este necesară intervenția utilizatorului | 2026-11-21

## Stare la închiderea lucrului autonom din această rundă

- Bază păstrată: **822** trasee G1/G2, **568** QABC; 136/136 cauze semantice cunoscute; 0/822 aprobări independente pentru învățare.
- În **CKPT-371 / V284 / V285** sunt **23 QABC P0 (27 trasee)**, fiecare cu originalul și analiza A/B/C.
- În **CKPT-373** utilizatorul a ales **A** la QABC-0094 cu motivul exact **„siguranta exploatari”**; ipoteza rămâne salvată separat de un barem.
- În **CKPT-374** s-a completat demonstrația lui **Cs=3C** pentru QABC-0017; rămâne conflictul între G1=A și G2=C, **chei doar importate**.
- În această rundă au fost cercetate toate cele **6 cazuri dificile rămase (7 trasee)** în [V286](./V286_GFR_SIX_REMAINING_P0_SOURCE_SPECIFIC_RESEARCH_ORIGINAL_ABC_AND_NO_TRUE_OPTION_2026_11_21.json); reconcilierea celor **8 cazuri dificile** este în [V287](./V287_GFR_ALL_8_P0_DEEP_SOURCE_RECONCILIATION_QABC_0236_HISTORIC_VARIANT_DIFF_2026_11_21.json).
- Rezultat pe cele **8 QABC dificile**: **6** au o alternativă originală preferabilă din literatura cercetată, cu caveate; **QABC-0094** nu are o preferință universală; **QABC-0236** nu are o opțiune originală exact corectă științific. Aceste date NU sunt aprobări ANRE sau de specialist.
- **Corecție metrică:** expresia `complete_original_scientifically_wellformed_option_QABC:5` din V286 este o numărătoare greșit etichetată. Ea înseamnă **5 opțiuni favorizate de sursă din cele 6 cazuri recercetate**, nu „5 întrebări originale ireproșabile”. V287 păstrează amendamentul fără a rescrie fișierele istorice.

## Noutate cheie: versiuni diferite ale variantei B la QABC-0236

- Sursa oficială ANRE publică în continuare în pagina de exemple `ELECTROTEHNICA-09.2024` (pagina instituției: https://anre.ro/participanti-la-piata-de-energie/persoane-fizice/energie-electrica/).
- **Excel original utilizator, rând 254:** „Un corp conductor situat într-un câmp electric de intensitate E se încarcă cu electricitate:”
  - A „prin conducţie”
  - B „prin inducţie electromagnetică”
  - C „prin magnetizare”
- **Material vechi reprodus public** `Rezolvări Subiecte Electrotehnica Examen Autorizare Electricieni` păstrează **B „prin inducţie”**, fără „electromagnetică”. Textul la https://ro.scribd.com/doc/7620850/Rezolvari-Subiecte-Electrotehnica-Examen-Autorizare-Electricieni, rânduri de pagină web 88–99; aceeași formă în repostarea https://stoianconstantin.wordpress.com/2008/01/23/.
- **Sursa de fizică OpenStax:** https://openstax.org/books/university-physics-volume-2/pages/6-4-conductors-in-electrostatic-equilibrium și https://openstax.org/books/physics/pages/20-3-electromagnetic-induction ; E static -> polarizare/inducție electrostatică (când se completează condițiile); inducția electromagnetică -> câmp magnetic variabil.
- **Verdict responsabil:** B este **intensitatea intenției istorice** a autorului în acele reproduceri (cu „prin inducție”), dar Excel 2024 are **„electromagnetică”**: acel B din Excel nu devine științific exact doar fiindcă o versiune mai veche era acceptabilă. Nici A/C originale nu devin corecte.

## Celelalte cinci cazuri noi cercetate

| ID | Alternativă susținută din sursa cercetată, cu rețineri | Pasul final rămas |
|---|---|---|
| QABC-0143 | A, constanta complexă de propagare. NIST/NBS §1.3.12 explică γ=α+jβ, în 1/lungime. *Doar γ·l este adimensional*, contrar originalului | Adnotare a erorii dimensionale și QA lingvistic calificat |
| QABC-0288 | C pentru racordarea obișnuită a unui loc nou: ANRE Ordin59/2013 art.5+11+25, cerere obligatorie indiferent de timp/putere | Confirmare juridică a cuantificatorului „orice” pentru ATR, distinct de cerere |
| QABC-0341 | A literal în PE102 §4.6.3, plus I7 original PDF p67 §5.3.4.3.1.2 (contact central) | PE102 nu figurează pentru Grad I; verificare de corespondență din I7 și grad aplicabil |
| QABC-0367 | C raportat la PE155 §§1.2.1–2, pentru limita branșamentului; exact la *bornele de ieșire* din contor | Original C spune doar „bornele contorului”; verificare de precizie și ediție |
| QABC-0386 | C literal corect din I7 PDF p72 §5.5.2.3: deconectabil individual; original B **fără** sculă e fals, norma **numai cu** sculă | În aplicația rescrisă B a devenit și ea adevărată; înainte de integrare trebuie aprobată remedierea fidelității |

## Calitatea dovezilor / limitările recunoscute

- **NIST** PDF https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nbsspecialpublication250-32.pdf §1.3.12: textul și formula au fost citite prin web; încercare screenshot PDF a eșuat cu `Cache miss`.
- **PE102** PDF https://electrician365.ro/wp-content/uploads/2019/04/Normativ-instalatii-electrice-ORDIN-PE-102-1986.pdf, §4.6.3: index text PDF citit exact la pagina index 10, screenshot a eșuat cu `Cache miss`, copie terță, deci nu se afirmă autenticitate vizuală.
- **PE155** PDF https://www.baluna.ro/wp-content/uploads/2018/02/pe_155_92.pdf §§1.2.1–2: index PDF text citit, screenshot eșuat; copie terță.
- **I7 din Library original utilizator** SHA256 `4bc3fc701cb71c937ad166462807423fa505c483783c5c93fe5b8ad03b20f431`: re-citite exact paginile PDF 67 (siguranțe cu filet) și 72 (borna principală PE) în această rundă.
- **Portal Legislativ**: https://legislatie.just.ro/Public/DetaliiDocument/310640, art5(1), 11(1), 25(1), recitit prin extragere focalizată; diferența `cerere de racordare` vs `emitere ATR` rămâne esențială.
- **ANRE oficial** https://anre.ro/participanti-la-piata-de-energie/persoane-fizice/energie-electrica/ încă listează tematica/bibliografia „2023” și setul „ELECTROTEHNICA-09.2024” de întrebări la 21.11.2026. Prezența pe site NU este confirmarea baremelor importate.
- Nicio recenzie independentă calificată juridică/electrotehnică/lingvistică certificată pentru aceste ID-uri; orice AI adițional nu poate fi raportat ca persoană calificată.

## Punct de decizie al utilizatorului

**QABC-0236 / G1-ELE-247 și G2-ELEC-383**: pentru că niciun răspuns original din Excel 2024 nu este fizic exact, trebuie decis **cum pregătim ulterior cardul de învățare**, fără a schimba întrebarea sau cheia în această etapă:

- **Opțiunea 1 (preferabilă conservator):** menținem întrebarea **BLOCATĂ pentru învățare** până când se poate clarifica / corecta pe baze autentificate oficial; păstrăm în dosar că istoric B generic „prin inducție” era intenția probabilă.
- **Opțiunea 2 (didactic diferențiat):** păstrăm întrebarea originală integral, în viitor afișăm un **avertisment explicit** că B «electromagnetică» nu este științific corect și explicăm separat efectul electrostatic; nu declarăm un B corect în barem și nu eliberăm acum aplicația.

Aceasta este o alegere de **politică editorială pentru învățare**, nu o solicitare de a arbitra o lege a fizicii. Utilizatorul poate alege oricând după citirea literaturii. Nu se modifică automat nimic.

## GFR respectare

- **No original XLSX, source, canon A/B/C or imported-key edits.**
- **No HTML/APK changes.**
- **PR #7 remains Draft, unmerged.**
- **0/822 approved for learning.**
