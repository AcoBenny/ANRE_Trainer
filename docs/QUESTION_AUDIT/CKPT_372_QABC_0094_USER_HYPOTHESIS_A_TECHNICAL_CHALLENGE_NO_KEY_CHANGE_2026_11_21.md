# CKPT-372 | QABC-0094: alegerea utilizatorului A verificată în literatură și păstrată ca IPOTEZĂ | 2026-11-21

## Obiect și proveniență

- `unit_id`: **QABC-0094**; trasee: **G1-ELE-102** și **G2-ELEC-245**.
- Excel original al utilizatorului: `ELECTROTEHNICA-09.2024-2.xlsx`, rândul **109**.
- Enunț original: „În cazul unei scheme cu două bare colectoare şi un întreruptor pe circuit este de preferat ca în regim normal de funcţionare:”
- A: „una dintre barele colectoare să fie sub tensiune, cealaltă bară fiind menţinută în rezervă rece;”
- B: „ambele bare colectoare să fie sub tensiune, cupla transversală fiind menţinută în funcţiune;”
- C: „ambele bare colectoare să fie menţinute sub tensiune, cupla transversală fiind în rezervă caldă.”
- Chei importate, **NU chei oficiale ANRE autentificate**: `G1-ELE-102=A`, `G2-ELEC-245=C`. Diferența de grad nu a fost reconciliată.

## Contribuția utilizatorului, păstrată exact ca ipoteză

> „Pentru QABC-0094 aleg varianta A. Verifică interpretarea mea cu sursele tehnice și păstrează-o ca ipoteză până la validare.”

- `provenance`: USER_INTERPRETATION
- `user_selected_original_excel_option`: **A**
- `user_supplied_explicit_technical_reasoning`: **NU**, utilizatorul a precizat alegerea, nu motivarea; nicio motivație nu se atribuie retrospectiv utilizatorului.
- `hypothesis_status`: **TECHNICALLY_SUPPORTED_CONDITIONALLY__NOT_EXAM_KEY_APPROVED**.
- `do_not_overwrite_hypothesis_on_new_research`: true.

## Verificare favorabilă și limite ale variantei A

1. **S. Rao, R. K. Jain, H. L. Saluja**, *Electrical Safety, Fire Safety Engineering and Safety Management*, Khanna Publishers, ed. a II-a, capitolul **7.13 Double Busbar Scheme (Duplicate Bus)**, pagini tipărite aproximativ **191–192**. Editura publică integral PDF-ul la:
   https://khannapublishers.in/system/storage/download/Electrical_Safety_Fire_Safety_Engineering_S_Rao.pdf.ATUo8lUIxNQ62OYo9FqgVs5vE2kmL2Ss
   - Textul distinge „Main Bus” și „Reserve Bus” și descrie pentru funcționarea normală **o singură bară energizată**, cealaltă în rezervă; avertizează că simultaneitatea complică protecțiile.
   - **Dovezi PRO-A:** regim normal cu o bară sub tensiune, cealaltă nealimentată, explicit descris într-un manual publicat de editură.
   - **Limită PRO-A:** nu apare literal calificarea **„rezervă rece”** și nici obligația ca separatoarele să fie toate deschise. Nealimentată ≠ automat rezervă rece în limbajul operativ NTE.
2. **NTE 009/10/00**, cap. privind stările operative, **art. 12 lit. c2**, text în portaluri de reproduceri legale:
   https://legis.medleg.ro/legislatie/2010-regulament-general-manevre-2
   - Pentru **bara în rezervă rece**, toate separatoarele circuitelor aferente către acea bară trebuie să fie deschise; starea presupune izolare față de sursele de tensiune, cu particularități privind măsura și descărcătoarele.
   - Pentru **cupla dintre bare în rezervă caldă**, separatoarele sunt închise spre ambele bare, întreruptorul este deschis și disponibil pentru conectare.
   - **Norma definește stări**, nu impune din acest pasaj varianta A pentru orice schemă normală dublă.

## Contraexemple și teste negative esențiale

3. **ABB**, *Distribution Automation Handbook*, Section 3, `1MRS757959`, **§3.14.1.4 Double-Busbar Arrangement**, în jurul paginii tipărite **3.8–3.9**, PDF ABB:
   https://library.e.abb.com/public/7dca4ffad2206d36c1257be30048d4be/DAHandbook_Section_3_Power_distribution_systems_757959_ENa.pdf
   - Ca regim tipic, descrie **ambele bare cu plecări repartizate, cupla deschisă**, cu avantajele de limitare a curenților de defect; astfel A **nu este universal preferată**.
   - Este suport didactic/ingineresc pentru posibilitatea topologiei **C**, nu dovada baremului oficial.
4. **Michael J. Bio**, *Electric Power Substations Engineering*, capitolul **3.5 Double Bus–Single Breaker Arrangement**, pagină tipărită **3-4**, extras al editurii Routledge:
   https://www.routledge.com/rsc/downloads/ch_3_9781439856383_text.pdf
   - Descrie chiar **cupla închisă normal** drept regim ce asigură flexibilitate și fiabilitate; cupla deschisă poate degrada configurația la două bare independente, din perspectiva acestui exemplu.
   - Arată că și **B** are justificări inginerești condiționale; nu putem exclude B fără date de stație.
5. **IP71/2015**, *Proiectarea stațiilor de conexiuni și transformare*, copie publică `§5.2.4, §5.2.4.1, §5.2.4.3`, descriptiv pentru două bare și un întreruptor:
   https://stoianconstantin.wordpress.com/wp-content/uploads/2024/11/1.e-ip-71-2015-statii-de-conexiuni-si-de-transformare.pdf
   - Documentul explică flexibilitatea conectării unui circuit la oricare bară; pasajele citite NU constituie o prescriere unică a modului normal A vs B vs C.
   - Limita: exemplar terț, nu validat ca original oficial vizual în acest audit.
6. **Mostră publică de întrebări grad II** găzduită la `electromed.ro`, întrebările **5, 6, 7**:
   https://electromed.ro/wp-content/uploads/2020/04/Test-4-electrotehnica-gradul-II.pdf
   - Q7 este identică cu întrebarea analizată; Q5 discută avantajele ambelor bare sub tensiune, Q6 discută **în mod separat** avantajele unei bare în rezervă rece.
   - Materialul nu are un barem în fragmentul verificat și **nu dovedește** litera corectă; formulările alăturate confirmă că scenariile diferă după criteriu.

## Q/A/B/C comparate și contradicția de examinator

- **A (ales de utilizator):** demonstrat ca **mod de operare realizabil și descris ca normal** de Rao, dar pentru „rezervă rece” trebuie dovedită izolarea completă. Nu este preferință universală demonstrată.
- **B:** cupla închisă, ambele bare alimentate; ilustrată ca „normală” de Routledge pentru altă concepție de operare. Poate fi nepotrivită când cuplarea crește curenții de scurtcircuit sau limitează selectivitatea protecției.
- **C:** ambele bare sub tensiune, cupla disponibilă/deschisă, potrivit definiției NTE a cuplei în rezervă caldă; exemplu ABB de regim tipic. Necesită condiții de alimentare și compatibilitatea instalației.
- **A vs B:** o bară izolată vs două alimentate cu cupla închisă: distincte, ambele descrise în manuale.
- **A vs C:** o bară rece vs două alimentate, cupla deschisă: niciuna nu rezultă universal preferabilă din enunț.
- **B vs C:** închis vs deschis la cuplă, cu efecte diferite în curentul de defect, protecții, manevrabilitate.

**Concluzie tehnică de audit:** alegerea utilizatorului **A este plauzibilă și are sprijin bibliografic pozitiv**, dar insuficientă pentru certificarea literei corecte universal în enunțul original cu „de preferat”. Varianta A importată la gradul I nu atestă oficial gradul I, iar varianta C importată la gradul II nu atestă oficial gradul II. Criteriul lipsă poate fi: alimentarea dintr-o singură sursă, menținerea barei de rezervă complet izolată, protecțiile stației, continuitatea la defect, reducerea scurtcircuitelor, disponibilitatea celei de-a doua surse.

## Gate / acțiune următoare

- O solicitare opțională de motivare de la utilizator poate restrânge ipoteza, **dar nu este condiție pentru a o păstra**.
- Pentru aprobarea definitivă: găsirea sursei/bibliografiei exacte care prescrie una dintre variante pentru acest enunț, verificarea ediției aplicabile examenului, cheie oficială autentificată sau un protocol de adjudecare tehnică și lingvistică calificată.
- `original_excel_changed`: **false**.
- `canonical_QABC_or_imported_keys_changed`: **false**.
- `HTML_or_APK_modified`: **false**.
- `official_exam_key_authenticated`: **false**.
- `qualified_independent_approval`: **false**.
- `learner_approved`: **false**.
- `PR_7_draft`: **true**; no merge, release or main changes.
- Precedent: CKPT-371 / V284 / V285. Acest fișier este anexă append-only, nu rescrie verdictul istoric.
