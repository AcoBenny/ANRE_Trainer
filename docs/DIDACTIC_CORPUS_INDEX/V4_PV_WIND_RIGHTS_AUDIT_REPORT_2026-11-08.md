# ANRE Trainer | Audit didactic V4: racordare PV/eolian, protecții și drepturi offline

Data controlului: 8 noiembrie 2026. Status: **AUDIT_ONLY**, fără implementare în HTML/APK și fără schimbarea celor 822 de întrebări sau bareme. Ultimul checkpoint oficial: **CKPT-002**.

## Ce am verificat

Am aprofundat lacunele SUB-005 și SUB-006 din registrul V3. Am înregistrat **14 repere documentare** pentru funcționarea instalațiilor fotovoltaice și eoliene, racordarea la rețea, protecții, proceduri și tipuri de teste. Unele sunt articole ANRE citibile direct, altele doar rezumate publice ale standardelor IEC, deci nu pot primi același nivel de încredere. Am adăugat **10 fișe de drepturi** și **7 blocaje explicite**.

### Constatarea esențială: protecțiile prosumatorilor

Norma aprobată prin **Ordinul ANRE nr. 228/2018**, astfel cum este modificată prin **Ordinul nr. 132/2020**, conține la **art. 14** protecții de interfață pentru funcționare insularizată, ieșirea din limitele de tensiune/frecvență și supracurent, alături de condiții de comutație. **Art. 18** tratează protecția ansamblului și coordonarea cu operatorul. Nu am declarat validate praguri universale, o schemă de proiect sau o configurație completă fără cunoașterea tipului de racordare. Surse: https://legislatie.just.ro/Public/DetaliiDocumentAfis/227152 și https://legislatie.just.ro/Public/DetaliiDocumentAfis/227966.

**Ordinul 19/2022** și pagina actualizată ANRE despre prosumatori clarifică procedurile de racordare și verificare. ANRE explică și documentele de conformitate pentru invertor/unitatea generatoare, cu trimitere la **Ordinul 51/2019** și **Ordinul 228/2018**. Surse: https://legislatie.just.ro/Public/DetaliiDocumentAfis/260077 ; https://anre.ro/consumatori/energie-electrica/cum-devin-prosumator/ ; https://anre.ro/informare-cu-privire-la-verificarea-conformitatii-tehnice-a-echipamentelor-din-instalatiile-de-producere-a-energiei-electrice-din-surse-regenerabile-cu-puterea-instalata-de-cel-mult-400-kw-pe-loc-de-c/.

### Edițiile standardelor

- **IEC 60364-7-712:2025** a înlocuit ediția din 2017 și descrie domeniul instalațiilor PV, inclusiv teme de stocare. Pagina IEC publică numai domeniul și metadatele, nu textul tehnic complet. **Adoptarea aplicabilă SR/națională nu a fost certificată.** https://webstore.iec.ch/en/publication/65748
- **IEC 62116:2014** se referă la metoda de testare a măsurilor de prevenire a insularizării în invertoarele PV. Nu echivalează cu setări naționale prestabilite. https://webstore.iec.ch/en/publication/6479
- **IEC 61400-21-1:2019** se referă la măsurarea și evaluarea caracteristicilor electrice ale turbinelor eoliene conectate la rețea. Textul integral este cu plată. https://webstore.iec.ch/en/publication/29528
- **Ordinul ANRE 208/2018** aprobă norma pentru module și centrale generatoare, inclusiv categorii distincte și cerințe diferențiate; nu generalizăm setările de la categoria C/D la toate instalațiile. https://legislatie.just.ro/Public/DetaliiDocument/211640

### Drepturi și utilizare offline

- **OpenStax University Physics 2**: CC BY-NC-SA 4.0, cu condiții explicite de atribuire, necomercialitate și ShareAlike, plus mențiune de permisiune prealabilă pentru folosirea conținutului în aplicații/ofertări de AI sau antrenarea modelelor. **NU aprobăm automat copierea în aplicație.** https://openstax.org/books/university-physics-volume-2/pages/preface
- **MIT OpenCourseWare**: CC BY-NC-SA 4.0, inclusiv cerințe privind materialele terților; reutilizarea depinde de condiții. https://ocw.mit.edu/pages/privacy-and-terms-of-use/
- **DOE**: conținutul creat de guvernul federal este în mod tipic domeniu public, însă imaginile/documentele furnizate de terți pot avea drepturi separate. Recunoașterea sursei este recomandată. https://www.energy.gov/web-policies
- **IEC și standarde SR EN**: nu republicăm textul integral sau materiale din standarde cu acces comercial; folosim numai referințe publice și explicații originale. Versiunile SR actuale necesită verificare.
- **Manualele încărcate și scanul OCR**: utilizarea în analiza privată nu dovedește licență de redistribuire în APK/GitHub. Aceste fișiere rămân în afara repository-ului public.
- **Acte oficiale ANRE și legislație**: păstrăm trimiterea la articol și ediția aplicabilă; publicarea gratuită nu dovedește automat dreptul de copiere integrală.

## Stare măsurabilă

- 14 repere de surse PV/eolian, dintre care **3** înregistrate la nivel de articol ANRE specific, iar **3** sunt doar rezumate comerciale de standard IEC.
- 10 surse/tipuri de materiale clasificate pentru reutilizare offline.
- 7 verificări prioritare încă deschise, inclusiv schemă completă PV, aplicabilitatea edițiilor SR, setări/funcții, documentație practică de turbine, permisiuni offline și control independent.
- **0/44 categorii didactice cu aprobare independentă finală.** Niciun model-agent specialist distinct nu a rulat un benchmark valid și niciun test Android/HTML de acceptanță nu a fost efectuat în această etapă.

## Următorul pas

1. Căutăm documentație gratuită, cu drepturi verificabile, pentru schema completă de protecții PV și arhitectura de racordare eoliană, fără să inventăm text din norme IEC/SR.
2. Verificăm la nivel de articol aplicabilitatea reglementărilor și diferențele de categorii de module generatoare, urmate de audit tehnic independent când devine efectiv disponibil.
3. Continuăm validarea celorlalte concepte din biblioteca didactică, **înainte** de orice mapare finală a celor 822 de întrebări.

**Nicio implementare; niciun barem modificat; cost API suplimentar 0 RON; niciun checkpoint nou.**
