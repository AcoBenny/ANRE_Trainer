# ANRE Trainer | Audit V10: G2-ELEC-178–227 (screening preliminar, sursa canonica nevalidata)

Data: 2026-11-09. Branch: `audit/anre-v8-priority-17-20261109`; PR #7 **Draft**. Mandat: documentare si QA, fara modificari in barem, HTML sau APK, fara merge.

## Metoda si limite

- Exact 50 ID-uri reale 178..227 inventariate in `V9_ALL_822_AUDIT_BACKLOG.csv`, cu cheile si randurile originale din `ELECTROTEHNICA-09.2024-2.xlsx` (conform tracker-ului V9). Cheile originale au ramas intacte.
- Textul intrebarilor, optiunile A/B/C si raspunsurile folosite in examinarea preliminara provin dintr-o **versiune mai veche incarcata in biblioteca conversatiilor, `ANRE_Trainer_FINAL_EVIDENCE_V10_4.html`**, nu din snapshotul canonic V10.29. Accesul la HTML V10.29 (SHA-256 `50c44b2798c2324121647ee5f24592fc2c1e049e827edb734c61dcf65d7f4b9c`) nu a permis in aceasta runda citirea intregului fisier. Pana la compararea integrala bit-cu-bit, **nu se afirma ca textul sau optiunile V10.4 si V10.29 coincid**.
- Notele tehnice sunt **screening asistat de model**, nu control semnat de electrician autorizat, specialist ANRE sau agent QA independent. Toate 50 au `independent_QA=NOT_RUN`, `canonical_V10_29_text_match=NOT_VERIFIED`, iar paginile sursei exacte raman `NOT_VERIFIED`.
- Pentru o sursa didactica externa, OpenStax, *University Physics Vol. 2*, §6.2, prezinta fluxul lui E = q/epsilon0; aceasta NU stabileste singura terminologia intrebarii 218. https://openstax.org/books/university-physics-volume-2/pages/6-2-explaining-gausss-law

## Rezultate screening (50 cazuri)

- `AMBIGUITY`: 5
- `SOURCE_GAP`: 2
- `CONDITIONAL`: 11
- `FORMULA_CHECK`: 20
- `PRINCIPLE`: 12

Clasele reflecta modul de control necesar, nu certitudinea corectitudinii baremului. Nu exista aprobari independente ori texte normative/paragrafe exacte validate in acest lot.

## Prioritate QA

1. **G2-ELEC-189 (critic):** „curentul generatorului creste direct proportional cu tensiunea intre faze”, cheia A. Formula trifazata `I=S/(sqrt(3)*U)` arata relatie inversa la S constant; fara sarcina/regim specificat enuntul nu poate fi acceptat general.
2. **G2-ELEC-218 (critic):** fluxul electric prin suprafata inchisa: pentru E, `Phi_E=q/epsilon0`; pentru D, `Phi_D=q`. Cheia B = q poate necesita precizarea marimii/ conventiei si unitatilor.
3. **G2-ELEC-203:** A implica raport intreg; dar optiunea C propune raport 1/2, compatibil cu armonici in unele conventii. Posibil multiplu raspuns/definitie insuficienta.
4. **G2-ELEC-178:** „numai prin inductie” omite curentul alternativ generat de invertor; cere context istoric/termeni.
5. **G2-ELEC-193/194:** comparatia deformarii armonicilor necesita bobina/condensator ideal liniar si separarea clara curent vs tensiune; altfel interpretare incompleta.
6. **G2-ELEC-195:** efectul de proximitate cere AC/frecventa/geometrie. Cheia B nu se certifica fara acestea.
7. **G2-ELEC-197:** reciprocitate doar cu retele liniare bilaterale si sensuri de referinta compatibile; simplul cuvant „pasiva” nu e suficient.
8. **G2-ELEC-188:** calcul preliminar repetabil: Z=sqrt(3²+4²)=5 ohm, I=220/5=44 A, corespunde cheii B din tracker.
9. **G2-ELEC-208:** formula corecta W=(1/2)*L*i²; optiunea B din versiunea veche are textul „1/2 Li2” fara exponent explicit, necesita QA de afisare.
10. **G2-ELEC-200/201:** aproape duplicat conceptual; verifica politica de deduplicare inainte de modificare.

## QA si criteriu de inchidere

- [x] 50 ID-uri gasite in tracker GitHub; distributia de chei si provenienta capturate in CSV V10.
- [x] Screening tehnic preliminar al celor 50 pe textul V10.4; 50 note individuale generate si pastrate.
- [ ] Comparatie exacta a 50 de intrebari/ABC/chei cu HTML **V10.29**; nici un verdict de paritate pana atunci.
- [ ] Sursa didactica: document, editie, pagina, fragment exact, legalitatea utilizarii si link offline pentru fiecare intrebare.
- [ ] QA tehnic si lingvistic independent, inclusiv adjudecarea casurilor prioritare; nu au fost lansati executanti independenti.
- [ ] Teste reale pe HTML si APK pentru raspunsuri, randomizare, repetare greseli si afisare referinte.
- [ ] Aprobare explicita de utilizator pentru orice schimbare de barem ori merge/release.

Progres contabil: **67** cazuri V8–V9 examinate preliminar + **50** cazuri V10 examinate **doar pe V10.4 vechi** = **117/822 cu diverse niveluri de screening**, **705 fara screening**, **0 cu QA independent**. Nu confunda cele 50 V10 cu un audit complet canonic V10.29.

Urmatorul lot nominal: 228–277; nu se incepe repararea cheilor pana la inchiderea QA pe surse.
