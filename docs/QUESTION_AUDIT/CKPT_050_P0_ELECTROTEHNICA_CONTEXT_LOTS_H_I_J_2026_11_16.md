# CKPT-050 | P0 ELE context audit | loturi H/I/J | 2026-11-16

## Limitări obligatorii

- Baza: commit `82f277080ab5450e8294f158bd0349398610090d`, PR #7 Draft; 102/568 unități cu context anterior, 116/822 ID-uri de grad.
- Acest checkpoint adaugă **12 unități P0 distincte**, **23 de ID-uri** de grad (11 perechi G1/G2 + o unitate doar G2): 114/568 și 139/822 documentate contextual, dacă sunt publicate fără concurență.
- **0 aprobări pentru învățare**, 0 modificări de barem, întrebări, HTML sau APK. Sursele sunt dovezi de cercetare tehnică, **nu** verificarea ediției ANRE aplicabile în 2026; QA independent sursă/tehnic/lingvistic **NOT_RUN**.
- Fișele anterioare și avertismentele rămân intacte; nu există reclasificare automată sau aprobare.

## Mini-loturi și dovezi

### Lot H: Termeni fizici și dependenta de frecvență

#### G1-ELE-014 | AU-2c324f18fe2143ed | barem C (intact) | CONDITIONAL

**Original:** Câmp fără surse este

- **A.** numai un câmp de curenţi de conducţie în regim staţionar
- **B.** câmpul electric
- **C.** câmpul de inducţie electromagnetică

**Context extins:** Un «câmp fără surse» impune precizarea mărimii și a operatorului matematic. Din ∇·B=0 rezultă lipsa surselor de divergență pentru inducția magnetică B, nu pentru orice «inducție electromagnetică»; câmpul E poate avea sarcini ca surse.

**Analiza A/B/C și eliminare:**

- A: «numai» face afirmația exclusivă; în regim staționar ∇·J=0 poate fi posibil, dar nu definește unicul câmp fără surse.
- B: câmpul electric are ∇·E=ρ/ε0 în vid, deci nu este în general fără surse.
- C: plauzibil dacă termenul «inducţie electromagnetică» desemnează de fapt câmpul B; echivalarea terminologică cere sursa didactică românească.

**Surse și domeniu:**

- [OpenStax, University Physics vol.2, Ch.16 Key Equations, Gauss magnetism + Gauss electric](https://openstax.org/books/university-physics-volume-2/pages/16-key-equations) | ∮B·dA=0 versus ∮E·dA=Q/ε0. Limită: technical background, not Grade-I glossary.

**Blocaj rămas:** Definiția precisă a sintagmei «câmp de inducţie electromagnetică» și dacă se urmărește ∇·B=0; revizie terminologică în română.

**ID-uri corespondente:** G1-ELE-014, G2-ELEC-166. **QA:** neexecutat independent.

#### G1-ELE-049 | AU-cb4eef5092065cab | barem B (intact) | CONDITIONAL

**Original:** Dacă două conductoare parcurse de curenţi în acelaşi sens sunt aşezate paralel, unul lângă altul:

- **A.** densitatea de curent crește în părţile apropiate ale conductoarelor
- **B.** densitatea de curent creşte în părţile mai depărtate ale conductoarelor
- **C.** densitatea de curent este uniformă pe ambele părţi ale conductoarelor

**Context extins:** Pentru două conductoare apropiate cu curenți ALTERNATIVI în același sens, efectul de proximitate împinge densitatea spre fețele externe. Pentru curent continuu ideal, argumentul dispare, iar lipsa mențiunii frecvenței face grila incompletă.

**Analiza A/B/C și eliminare:**

- A: concentrarea spre fețele apropiate este tipică pentru curenți alternativi opuși, nu concordanți.
- B: susținut pentru AC și configurația paralelă cu sens identic.
- C: pentru AC nu este uniform din cauza proximității; poate fi idealizat ca uniform în DC.

**Surse și domeniu:**

- [IEEE Technology Navigator, Proximity effect](https://technav.ieee.org/topic/proximity-effect/) | section Electromagnetic Mechanism, same-direction currents crowd outer faces under AC. Limită: exact frequency/sense match, not DC.

**Blocaj rămas:** Frecvență AC/DC nespecificată; necesară confruntarea cu convenția didactică ANRE pentru «curenţi» în această familie.

**ID-uri corespondente:** G1-ELE-049, G2-ELEC-195. **QA:** neexecutat independent.

#### G1-ELE-057 | AU-84185dba0d7b87f1 | barem A (intact) | BLOCKED

**Original:** Două funcţii periodice sinusoidale sunt armonice între ele dacă:

- **A.** raportul perioadelor lor este un număr întreg oarecare
- **B.** au aceeaşi perioadă
- **C.** raportul perioadelor lor este egal cu 1/2

**Context extins:** Armonicile au frecvențe multiplu întreg ale fundamentalei, dar raportul perioadelor depinde de ordinea aleasă; întrebarea nu precizează ordinea și permite exemple în care B sau C descriu tot relații armonice.

**Analiza A/B/C și eliminare:**

- A: un raport întreg poate descrie armonice, dar sensul raportului trebuie definit; n=1 include fundamentala.
- B: dacă perioadele coincid, raportul este 1, întreg; poate fi aceeași armonică, depinzând de sensul «între ele».
- C: raportul T1/T2=1/2 indică raport de frecvență 2, astfel poate fi armonic în sens invers.

**Surse și domeniu:**

- [OpenStax, University Physics vol.1, §17.4](https://openstax.org/books/university-physics-volume-1/pages/17-4-normal-modes-of-a-standing-sound-wave) | harmonics as integer multiples of fundamental, including first harmonic. Limită: mathematical relation transferable, acoustic example not exam source.

**Blocaj rămas:** Trebuie o definiție ANRE de «armonice între ele», dacă include n=1 și ce raport T1/T2 este urmărit; fără răspuns exclusiv din A/B/C.

**ID-uri corespondente:** G1-ELE-057, G2-ELEC-203. **QA:** neexecutat independent.

#### G1-ELE-113 | AU-9c9c2de62a042f6a | barem C (intact) | CONDITIONAL

**Original:** Temperatura înfăşurărilor statorice ale generatoarelor electrice este determinată:

- **A.** numai de temperatura mediului ambiant
- **B.** de tensiunea între faze
- **C.** de pierderile Joule-Lenz

**Context extins:** Pierderile Joule–Lenz în înfășurare sunt o sursă de încălzire, însă temperatura finală depinde și de temperatură ambiantă, circulația fluidului de răcire, alte pierderi și rezistență termică. Expresia «determinată de» nu înseamnă neapărat «exclusiv de».

**Analiza A/B/C și eliminare:**

- A: «numai» temperatura ambiantă exclude încălzirea internă, fals.
- B: tensiunea între faze poate influența funcționarea, dar singură nu determină direct temperatura înfășurării.
- C: pierderile I²R sunt o cauză directă verificată; răspuns intenționat, dar nu explică toate condițiile termice.

**Surse și domeniu:**

- [EPRI, Main Generator, §5.4.1 winding temperature / cooling water](https://restservice.epri.com/publicdownload/000000000001007423/0/Product) | stator winding I²R losses versus cooling water flow. Limită: generator-specific source; section text accessed as searchable extract.

**Blocaj rămas:** Verificare independentă a domeniului generatorului și a formulării «este determinată», fără confuzia cu motor.

**ID-uri corespondente:** G1-ELE-113, G2-ELEC-255. **QA:** neexecutat independent.

### Lot I: Circuite AC, marimi reactive, admittanta

#### G1-ELE-128 | AU-14fb0886051fa595 | barem A (intact) | BLOCKED

**Original:** Într-un circuit electric monofazat cu caracter inductiv tensiunea este defazata fata de curent:

- **A.** înainte cu 90 de grade
- **B.** cu zero grade (sunt în faza)
- **C.** cu 90 de grade în urma

**Context extins:** În circuit R+L cu R>0 și X_L>0, defazajul tensiunii față de curent este φ=arctan(X_L/R), strict între 0 și 90°. Exact 90° rezultă numai pentru reactanță inductivă pură, nu din «caracter inductiv» generic.

**Analiza A/B/C și eliminare:**

- A: corect doar pentru inductiv PUR, nu pentru circuit RL generic.
- B: zero numai când reactanța netă este zero (rezistiv/rezonanță), nu pentru inductiv net.
- C: tensiunea rămâne în urmă pentru capacitiv net, nu inductiv.

**Surse și domeniu:**

- [OpenStax University Physics vol.2, §15.3 RLC AC](https://openstax.org/books/university-physics-volume-2/pages/15-3-rlc-series-circuits-with-ac) | φ=atan((X_L-X_C)/R), with pure L boundary. Limită: exact physical circuit/phase relation.

**Blocaj rămas:** Enunțului îi lipsește «pur». Contraexemplu calculabil R=X_L → 45°, fără opțiune exactă.

**ID-uri corespondente:** G1-ELE-128, G2-ELEC-268. **QA:** neexecutat independent.

#### G1-ELE-178 | AU-2ad66252f57dac02 | barem C (intact) | CONDITIONAL

**Original:** Puterea electrică reactivă:

- **A.** permite definirea limitelor de utilizare ale unui aparat electric
- **B.** produce transformarea energiei electrice în energie mecanică
- **C.** este variaţia în timp a energiei magnetice şi electrice

**Context extins:** În model sinusoidal, puterea reactivă scalară Q=UI·sinφ (var) exprimă amplitudinea componentei instantanee reactive oscilante; derivata energiei stocate descrie o rată instantanee, nu direct valoarea constantă Q.

**Analiza A/B/C și eliminare:**

- A: limita de utilizare a unui aparat se exprimă de regulă prin puterea aparentă/ratinguri, nu prin Q singură.
- B: conversia în lucru mecanic are componentă activă, nu Q drept mărime definitorie.
- C: reflectă schimbul oscilant de energie în câmpuri E/B, dar confundă Q cu rata instantanee a energiei.

**Surse și domeniu:**

- [IEEE 1459:2010, §3.1.1, historic power definitions](https://ieeexplore.ieee.org/document/5439063/) | Q=VI·sinθ and p_q=-Q sin(2ωt), exchange of field energy. Limită: official IEEE record is paywalled; source text was cross-checked only in external excerpts, 2025 revision different.

**Blocaj rămas:** Definiția didactică exactă folosită de ANRE și raportul dintre Q scalar și p_q(t); standardele istorice și recente pot folosi tratare diferită.

**ID-uri corespondente:** G1-ELE-178, G2-ELEC-314. **QA:** neexecutat independent.

#### G1-ELE-222 | AU-ca89b1b43e098b0f | barem C (intact) | BLOCKED

**Original:** Susceptanţa unui circuit de curent alternativ sinusoidal este inversul:

- **A.** impedanţei
- **B.** rezistenţei
- **C.** reactanţei

**Context extins:** Susceptanța este partea imaginară a admitanței Y=1/(R+jX)=(R-jX)/(R²+X²). Pentru R≠0, B=-X/(R²+X²), nu 1/X. Chiar la R=0 există o convenție de semn pentru B.

**Analiza A/B/C și eliminare:**

- A: inversul impedanței complexe este admitanța Y, nu susceptanța scalară B.
- B: inversul rezistenței este conductanța G (pentru componentă pur rezistivă).
- C: inversul reactanței este relevant pentru componentă pur reactivă ca modul/convenție, nu orice circuit AC sinusoidal.

**Surse și domeniu:**

- [All About Circuits, Alternating Current, Ch.5, Susceptance and Admittance](https://www.allaboutcircuits.com/textbook/alternating-current/chpt-5/susceptance-and-admittance/) | 1/X under pure reactance; mixed R/X need complex admittance. Limită: textbook didactic, details signed B under convention.

**Blocaj rămas:** Necesită condiția «pur reactiv» și convenția semnului. Contraexemplu R=3Ω, X=4Ω: |B|=4/25=0,16 S versus 1/X=0,25 S.

**ID-uri corespondente:** G1-ELE-222, G2-ELEC-358. **QA:** neexecutat independent.

#### G1-ELE-231 | AU-62bf06e215a53d51 | barem B (intact) | BLOCKED

**Original:** Singurele mărimi fizice reale în curent alternativ sunt:

- **A.** mărimile efective de curent sau de tensiune
- **B.** mărimile instantanee de curent sau de tensiune
- **C.** valorile medii de curent sau de tensiune

**Context extins:** i(t) și u(t) sunt mărimile reale instantanee ale undei. Valorile RMS/medii sunt mărimi reale fizic cuantificabile rezultate din semnal, de aceea «singurele mărimi fizice reale» este excesiv dacă «reale» nu distinge semnalul în timp de reprezentarea complexă fazorială.

**Analiza A/B/C și eliminare:**

- A: RMS este calculat pe o durată, dar are efect termic fizic măsurabil; nu poate fi considerat ireal în sens larg.
- B: descrie unda instantanee fizică, susține sensul probabil al autorului.
- C: media poate fi zero pentru sinus ideal simetric, dar media ca valoare este tot o mărime reală derivată.

**Surse și domeniu:**

- [IEC 80000-6:2022, §0.4.3–0.4.4 (public catalog excerpt)](https://standards.theiteh.com/catalog/standards/clc/f8bc5b5a-c33d-4675-a80f-03a79199f39d/en-iec-80000-6-2022) | real instantaneous representation i(t), RMS and complex phasors explicitly distinguished. Limită: engineering terminology, current text scope older ISO/IEC.

**Blocaj rămas:** Sensul exact al expresiei «fizice reale» versus reale/complexe, instantaneu/RMS; nicio semnătură lingvistică independentă.

**ID-uri corespondente:** G1-ELE-231, G2-ELEC-367. **QA:** neexecutat independent.

### Lot J: Supratensiuni, putere, flux, propagare

#### G1-ELE-236 | AU-491d11b487748842 | barem B (intact) | CONDITIONAL

**Original:** Supratensiunile de trăsnet pot fi:

- **A.** numai directe
- **B.** induse
- **C.** de rezonanta sau de ferorezonanţa

**Context extins:** Supratensiunile provocate de trăsnet includ mecanisme prin lovituri directe și prin inducție/cuplaj electromagnetic de la descărcări indirecte. Aceasta exclude «numai directe»; rezonanța/ferorezonanța sunt alt mecanism de supratensiune.

**Analiza A/B/C și eliminare:**

- A: «numai directe» este fals, există induse/indirecte.
- B: induse este afirmativ susținut de surse tehnice de protecție la supratensiune.
- C: rezonanța și ferorezonanța sunt mecanisme distincte, nu clasificarea supratensiunilor de trăsnet.

**Surse și domeniu:**

- [Schneider Electric engineering blog, Types of lightning strikes and transients](https://blog.se.com/infrastructure-and-grid/power-management-metering-monitoring-power-quality/2013/02/26/arresting-the-surges-in-lightning-strikes/) | lightning direct vs indirect induced overvoltages. Limită: industry source, no exam edition signoff.
- [Phoenix Contact, The basics of surge protection §1.2](https://www.phoenixcontact.com/assets/d7cbab8b-a703-4279-9e74-3c52a84e0327/index.html) | indirect lightning can induce surge voltage. Limită: manufacturer guide.

**Blocaj rămas:** Candidat B susținut în domeniul efectelor indirecte; ediția bibliografică pentru examen și QA separat rămân deschise.

**ID-uri corespondente:** G1-ELE-236, G2-ELEC-372. **QA:** neexecutat independent.

#### G1-ELE-245 | AU-bd60af52c290f7af | barem A (intact) | BLOCKED

**Original:** Un circuit de curent alternativ, pentru care factorul de putere este egal cu 1, este un circuit:

- **A.** pur rezistiv
- **B.** pur inductiv
- **C.** pur capacitiv

**Context extins:** Factorul de putere 1 înseamnă curent și tensiune în fază, deci circuit cu impedanță echivalent rezistivă la frecvența testului. Nu demonstrează că elementele circuitului sunt exclusiv rezistoare: un RLC la rezonanță conține L și C, dar PF=1.

**Analiza A/B/C și eliminare:**

- A: adevărat pentru circuit pur R, dar prea restrictiv dacă este cerut din condiția PF=1 în general.
- B: pur inductiv are PF≈0, nu 1.
- C: pur capacitiv are PF≈0, nu 1.

**Surse și domeniu:**

- [OpenStax, College Physics 2e, §23.12](https://openstax.org/books/college-physics-2e/pages/23-12-rlc-series-ac-circuits) | RLC resonance gives cosφ=1 as pure R does. Limită: exact circuit, no Grade-I didactic wording.

**Blocaj rămas:** Precizarea «pur rezistiv» față de «cu caracter echivalent rezistiv»; contraexemplu de rezonanță validează PF=1 cu L și C prezente.

**ID-uri corespondente:** G1-ELE-245, G2-ELEC-381. **QA:** neexecutat independent.

#### G1-ELE-257 | AU-23d536ba936f2f33 | barem B (intact) | BLOCKED

**Original:** Unitatea de măsură a fluxului electric este:

- **A.** V/m
- **B.** Coulombul
- **C.** Faradul

**Context extins:** Dacă «flux electric» înseamnă fluxul deplasării electrice Ψ=∫D·dS, unitatea este C; dacă înseamnă fluxul câmpului E, Φ_E=∫E·dS, unitatea este V·m (echivalent N·m²/C). Sintagma neterminată nu specifică ce flux se cere.

**Analiza A/B/C și eliminare:**

- A: V/m este unitatea intensității câmpului E, nu a fluxului integral.
- B: Coulombul este corect pentru fluxul deplasării electrice D, nu pentru fluxul integrat al câmpului E.
- C: Faradul este unitatea capacității, nu a fluxului.

**Surse și domeniu:**

- [NIST, Guide to SI, Ch.4](https://www.nist.gov/pml/special-publication-811/nist-guide-si-chapter-4-two-classes-si-units-and-si-prefixes) | electric displacement D measured C/m²; electric field E V/m. Limită: authoritative dimensions.
- [OpenStax, University Physics vol.1, Appendix A Units](https://openstax.org/books/university-physics-volume-1/pages/a-units) | E electric flux has N·m²/C. Limită: university physics glossary.

**Blocaj rămas:** Necesită definiție/simbol din manualul electrotehnic românesc ANRE; fără precizarea E versus D, unitatea nu este univocă.

**ID-uri corespondente:** G1-ELE-257, G2-ELEC-392. **QA:** neexecutat independent.

#### G2-ELEC-290 | AU-fd7d308698e05c41 | barem A (intact) | CONDITIONAL

**Original:** Mărimea adimensională care reprezintă variaţia pe care o suferă amplitudinea şi faza undei de tensiune sau curent când parcurge 1 km de linie (lungă ) se numeşte:

- **A.** constanta de propagare a liniei
- **B.** constanta de atenuare a liniei
- **C.** constanta de distorsiune a liniei

**Context extins:** Constanta complexă de propagare γ=α+jβ are dimensionalitatea 1/lungime. Produsul γ·l este adimensional și descrie atenuarea și defazajul pe segmentul de lungime l. Sintagma «mărime adimensională ... când parcurge 1 km» poate ascunde convenția unui segment fix 1 km, dar nu transformă γ însăși într-o constantă fără unitate.

**Analiza A/B/C și eliminare:**

- A: conceptul de atenuare+fază indică propagarea γ; interpretare posibilă ca γ·(1 km).
- B: constanta de atenuare α nu descrie singură deplasarea de fază, deci incompletă.
- C: constanta de distorsiune nu este definiția standard a mărimii complexe γ.

**Surse și domeniu:**

- [Ansys HFSS Help, Complex Propagation Constant](https://ansyshelp.ansys.com/public/Views/Secured/Electronics/v242/en/Subsystems/Circuit/Content/HFSS/ComplexPropagationConstant.htm) | α Np/m and β rad/m for γ. Limită: engineering software reference, not Romanian course definition.

**Blocaj rămas:** Clarificarea dacă autorul definește propagarea unei SECȚIUNI de 1 km (γl adimensional), versus coeficientul γ per-unitate de lungime.

**ID-uri corespondente:** G2-ELEC-290. **QA:** neexecutat independent.

## Teste și verificare

- 12/12 QABC cu cheia originală identice față de copia canonică ANRE `ANRE_Trainer_MAPPING_FINAL_V1.csv` și confirmate textual pe `V73...` prin citire directă GitHub în această sesiune. 23/23 ID-uri și 12/12 unități unice.
- Pentru fiecare fișă: cele trei variante sunt în câmpurile A/B/C corespunzătoare, explicațiile încep cu A:/B:/C: și sursele au URL separat de analiza variantei; nu s-au detectat deplasări de câmp.
- Teste matematice explicite: RL R=X → φ=45°, susceptanță R=3,X=4 → |B|=0,16S ≠ 1/X=0,25S; RLC rezonant la50Hz cu L=10mH → C≈1013,2μF, PF=1 în prezența L și C.
- QA tehnic independent, ediție/examen2026, autenticitate documente externe, surse cu acces limitat: **NECONFIRMATE**.

## Următorul pas

Continuare pe următoarele unități P0 fără fișă contextuală, întâi contradicții cu potențial de transfer; sursă originală și review separate obligatorii. Nu solicita utilizatorului interpretări de rutină. Dacă o ambiguitate nu poate fi rezolvată și aportul lui schimbă decisiv analiza, arată enunțul/ABC și paragraful cu contextul dinainte și de după.