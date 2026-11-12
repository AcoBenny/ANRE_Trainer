# Avengers Academy | Întrebări cu incertitudine: dialog ghidat | v1 | 2026-11-12

## Principiu
**Când o întrebare ANRE rămâne realmente incertă după recuperarea dovezilor accesibile, o prezintăm utilizatorului pentru a cerceta împreună sensul corect al cerinței și alegerea opțiunii.** Participarea utilizatorului este aport de raționament/interpretare, **nu atestare a baremului, legii sau sursei**. Aplicabil și altor proiecte Avengers, dacă raționamentul uman clarifică o ambiguitate reală.

## Când escaladăm către utilizator
- După analiza anterioară/surselor, două interpretări sau răspunsuri rămân plauzibile; sau există conflict între enunț și normă, excepție de obiect/scope, termen/limbaj special, figură incompletă cu consecințe pentru răspuns.
- Preferabil când înțelegerea semantică **ar putea produce o regulă reutilizabilă** (de ex. prag normativ vs valori admise, 3 conductoare fizice vs 2 conductoare active).
- **Nu** escaladăm pentru calcule triviale, pentru fiecare întrebare în așteptarea accesului la o sursă, pentru fiecare sursă inaccesibilă sau pentru conflicte închise demonstrabil. Nu întrerupem utilizatorul cu același ID deja discutat fără dovezi/întrebări noi.

## Formatul minim al unei discuții
1. **ID + formularea originală + toate A/B/C + cheia istorică (dacă există)**, fără simplificare/alterare, plus sursa cu versiune și locator, gradul.
2. **Ce știm** prin dovezi versus **ce nu știm**; arată exact cele două interpretări rivale și care cuvinte produc divergența. Nu spune dinainte că un răspuns este verificat dacă a rămas doar candidat.
3. **O singură întrebare orientată** către utilizator: „Cum ai interpreta [termenul critic] și de ce?”; nu chestionare lungi. Afișează cel mult un caz per răspuns, dacă nu sunt cerute mai multe.
4. După contribuția utilizatorului: formulează regula candidat `IF context/object/qualifier THEN interpretation`, caută contraexemple, verifică o sursă primară cu versiune/grad și A/B/C, apoi consemnează `USER_HYPOTHESIS` separat de `SOURCE_EVIDENCE`, de `INDEPENDENT_REVIEW` și de `APPROVED_FOR_LEARNING`.
5. Transformă o descoperire confirmată într-o **regulă de QA + test de regresie pozitiv/negativ**. Nu modifica original QABC, cheia sau aplicația automat. Păstrează toate pistele anterioare, chiar infirmate, ca lecții.

## Modalitate de lucru care economisește timp
- Continuă autonom loturile clare; cere ajutorul utilizatorului **numai la blocajele semantice cu impact real**.
- Dacă utilizatorul nu răspunde imediat, rămâne `PENDING_USER_INTERPRETATION`, fără blocarea muncii la alte unități; nu pretinde lucru în fundal.
- Un ID devine `RESOLVED_QA_PENDING` numai după dovada și controlul necesare, nu prin simplul acord al utilizatorului. Închiderea finală pentru învățare respectă regulile Avengers QA existente.

## Primul caz propus pentru dialog (nu decis)
- `G1-NOR-041`, Grad I, `DEEP-NOR-03`. Barem original **B**.
- A: circuite monofazate cu trei conductoare, polifazate indiferent de secțiune.
- B: circuite monofazate cu trei conductoare și polifazate cu faze <=16mm² Cu/25mm² Al.
- C: circuite monofazate cu trei conductoare și polifazate cu faze <=25mm² Cu/35mm² Al.
- Sursa: **I7 §5.2.4.6.1 lit. a și b** spune `monofazate cu două conductoare` și praguri `16mm² Cu/25mm² Al`. Poate `trei conductoare` din enunț reprezenta `L+N+PE` fizic, în timp ce norma contabilizează numai `L+N` active? Sau este schimbare de obiect / redactare care cere control?
- Întrebarea pentru utilizator: **„Când citești «monofazat cu trei conductoare» aici, înțelegi L+N+PE sau trei conductoare active, și ce indiciu din formulare te determină?”**
- Până la verificare: `USER_HYPOTHESIS=PENDING`; `CANDIDATE=B_CONDITIONAL`; `INDEPENDENT_QA=NOT_RUN`; `APPROVED_FOR_LEARNING=NO`.

## Referințe
- Bază: `QA_RULES/FAST_QA_TRIAGE_NO_RESTART_V1_2026_11_12.md`, `CKPT_024_NOR029_BOUND_EXCEPTION_QA_REGRESSION_2026_11_12.md`, `DEEP_EXECUTION_2026_11_11/DEEP_NOR_03_ALL_20_PRE_REVIEW_SOURCE_ABC_TRIAGE.csv`.
- Text I7 §5.2.4.6.1 în reproducerea Monitorului Oficial: https://curentulelectric.ro/wp-content/uploads/2019/01/NORMATIV_I7_2011_actualizat.pdf ; sursa 2011 nu garantează de una singură toate modificările și ediția ANRE 2026; `web.screen` anexă PDF a eșuat cache miss în sesiune.

Nu se modifică `main`, bareme, întrebări, HTML, APK; nu se face merge/release fără acord.
