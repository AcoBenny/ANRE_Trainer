# ANRE Trainer | Audit didactic prioritar V2 | 8 noiembrie 2026

**Faza:** audit exclusiv al documentatiei didactice si normative. **Nicio modificare** a bazei de 822 de intrebari, baremului, HTML-ului sau APK-ului. **Nu este un nou checkpoint**.

## Rezultate masurabile

- **13 din 13 categorii prioritare (P1) au fost inspectate in aceasta trecere** la nivel de dovezi posibile, lacune si tip de sursa. Acest lucru NU inseamna 13 categorii complet validate.
- **19 subteme distincte** au fost clasificate individual si primesc pagina, sursa externa, metoda si conditia pentru inchiderea auditului, unde exista.
- **9 din 19** au cel putin o referinta catre o pagina locala cu informatie potential utila, de calitati diferite: formule vizual confirmate, descrieri partiale, derivari conditionate si surse istorice. Aceste 9 NU inseamna 9 concepte definitiv aprobate.
- **4 din 19** au referinta oficiala externa identificata (EV, autorizare, racordare, SSM), dar verificarea articol cu articol sau reproducerea in offline necesita evaluare separata.
- **6 din 19** raman fara o proba locala suficient de precisa in cautarile executate (camp magnetic fara surse, Poynting, eolian, fasciculare, PV ca teorie didactica, RC). Unele dintre cele 9 cu localizare raman doar partial demonstrate.
- **0/44 categorii** au QA tehnic independent final, exact ca in V1. Niciuna nu a fost promovata automat la statusul APROBAT.

## Constatari prin inspectarea manualelor originale

| Tema / ID | Pagini PDF fizice (1-index) | Constatare | Limita |
|---|---|---|---|
| Legea Gauss (SUB-001) | PREG p.32 | Fluxul inductiei electrice prin suprafata inchisa este legat de sarcina electrica inchisa. Pagina si figura au fost inspectate vizual. | Precizati mediu / permitivitate; a nu folosi formula in E fara ipoteze. |
| Faraday-Lenz (SUB-004) | PREG p.63 | Este explicata variatia fluxului si f.e.m. | Semnul minus si conventia de orientare nu sunt clarificate integral. |
| Corona (SUB-010) | PREG p.120 | Este indicata rotunjirea muchiilor clemelor/armaturilor pentru reducerea descarcarilor prin efluvii. Verificat in imaginea paginii. | Nu explica fascicularea conductoarelor, formula pierderilor sau toate conditiile de retea. |
| Capacitati LEA (SUB-011) | PREG p.89 + UTCN pp.66,68 | O posibila derivare pentru Cs=3C din relatii trifazate si capacitive. | Doar derivare sub ipoteze. Nu este o citare directa a formulei din manual. |
| Regimuri masina asincrona (SUB-013) | MAS pp.94, 104, 106 | Motor 0<s<1, generator s<0, franare prin contracurent s>1; pagina 104 a fost vizual verificata. | Nu toate tipurile de franare se reduc la acelasi interval de alunecare. |
| Descarcatoare (SUB-014) | STATII pp.302,305,310; I7 p.78 | Literatura istorica descrie descarcatoare cu coarne si rezistente variabile. | Nu valideaza automat modelele moderne ZnO. |
| Tranzitoriu RL (SUB-016) | MAS p.202 | **Te=L_e/R_e** la circuitul de excitatie al generatorului de c.c. + raspuns exponential la treapta de tensiune. Verificat in imaginea PDF original. | Caz specific circuitului de excitatie; generalizarea cere explicatie separata. |
| Scheme si relee (SUB-018) | PREG p.12, STATII p.428 | Simboluri grafice si definitia operationala a protectiei prin relee; anclansari/deconectari automate. | Schemele grafice individuale nu au fost toate auditate tehnic. |
| Situatii speciale (SUB-008) | I7 pp.115,117,119,121 | Bai/dusuri, piscine, saune si masuri de protectie localizate ca paragrafe. | PDF-ul este versiune sintetica 22.09.2023; aplicabilitate 2026 si exceptii necesita verificare oficiala. |

## Referinte normative/oficiale externe identificate

- **Autorizarea electricienilor:** Ordin ANRE 66/2023 si modificarea 65/2024, Portal Legislativ: https://legislatie.just.ro/Public/DetaliiDocumentAfis/288327 . Nu s-a certificat ca acestea sunt toate modificarile ce trebuie aplicate fiecarui caz in 2026.
- **Racordarea utilizatorilor:** regulamentul aprobat prin Ordinul 59/2013, Portal Legislativ cu forma consolidata listata la **25.05.2026**: https://legislatie.just.ro/Public/DetaliiDocumentAfis/297330 . Orice intrebare se verifica la articolul si data aplicabila, nu prin comparare cu pdf-uri istorice.
- **SSM:** HG 1425/2006 aproba normele metodologice pentru Legea 319/2006: https://legislatie.just.ro/Public/DetaliiDocument/76337 . Instructiunea interna de 11 pagini din corpus NU este substitut pentru legislatia oficiala.
- **Incarcarea EV:** IEC 60364-7-722:2018 descrie domeniul de aplicare pentru circuitele ce alimenteaza vehicule electrice, https://webstore.iec.ch/en/publication/29958 ; textul integral este cu acces restrictionat, iar referinta NU ofera automat un curs didactic sau drept de redistribuire offline.
- **I7:** Ordin 959/2023 a modificat I7-2011, https://legislatie.just.ro/Public/DetaliiDocument/271142 . La compararea cu PDF-ul sintetic din 2023 trebuie verificata forma efectiva si domeniul aplicarii.

## Lacune si cele mai importante urmatoare actiuni

1. **Didactica tehnica:** obtinerea unor surse exacte, permise pentru studiu offline, despre vectorul Poynting, div B=0, curba RC si constanta de timp tau=RC, Corona pentru fascicularea conductoarelor, fotovoltaice si eoliene, moduri de incarcare EV si protectiile specifice.
2. **Audit tehnic al formulelor:** delimitarea derivarii Cs=3C, semnul Faraday-Lenz, regimurile de franare asincrona si surse actuale despre descarcatoare ZnO. Verificare distincta a figurilor si schemelor electrice.
3. **Norme si licente:** verificare punctuală pentru versiunea I7 2026 si articolele ANRE; drepturi de utilizare offline pentru manualele istorice, IEC si cataloage. QA independent inca **NOT_RUN**.

**Regula de masurare:** 13/13 inseamna verificarea celor 13 riscuri prioritare la nivel de trasabilitate, **nu** 100% din audit. Cele 44 de categorii initiale raman numitorul provizoriu; numai 0/44 sunt aprobate independent. Cele 19 subteme nu au fost adaugate artificial la numitor.

## Fisiere

- `ANRE_CATEGORII_PRIORITARE_13_AUDIT_V2.csv`: rezumat pe cele 13 categorii prioritare.
- `ANRE_SUBTEME_19_AUDIT_P1_V2.csv`: registrul de surse concrete sau lacune pentru cele 19 subteme.
- `ANRE_Registru_Validare_Concepte_V2_2026-11-08.xlsx`: registrul V1 pastrat, plus trei foi noi cu progresul V2, fara schimbare a aprobarilor.

**Nu s-au importat intrebari sau raspunsuri. Nu s-a creat un checkpoint nou. Cost suplimentar 0 RON.**
