# CKPT-059 | Lot K | ELE-231, ELE-245, ELE-257 prin inferență bidirecțională v0.4.6 | 2026-11-16

## Domeniu, bază, anti-duplicare
- Repo `AcoBenny/ANRE_Trainer`, ramură `audit/anre-v8-priority-17-20261109`, PR #7 Open/Draft, HEAD pre-write `f869399afa47bc3c588830e266a5c066480573cf`.
- Nu repetă cercetarea inițială din CKPT-050/051. Cele **3 unități** / **6 ID-uri** sunt deja în 114/568 și 139/822; **delta de coverage = 0**. Valabil `approved_for_learning=0/822`.
- Nicio modificare a textului canonic, opțiunilor, cheilor, mapării, HTML/APK sau main; fără merge/release.
- Surse suplimentare identificate/inspectate pentru comparație contextuală în această sesiune: OpenStax §15.5 (HTML deschis), IEC 80000-6:2022 §0.4.3–4 (extragere de index, pagina HTML a returnat cache miss), Stephen Ellingson, *Electromagnetics I*, §5.5 (extras de index, acces pagină cache miss), *Electromagnetic Fields and Waves* §3.2.1 (extras index, pagina cache miss). Aceste surse sunt **context tehnic**, nu dovadă că ANRE folosește exact ediția lor în 2026. Nu s-au reanalizat vizual PDF-uri. Nu inventați QA independent.

## ELE-231 | G1-ELE-231 / G2-ELEC-367 | AU-62bf06e215a53d51 | barem B neschimbat
**Enunț:** „Singurele mărimi fizice reale în curent alternativ sunt:”
- **A:** „mărimile efective de curent sau de tensiune”
- **B:** „mărimile instantanee de curent sau de tensiune”
- **C:** „valorile medii de curent sau de tensiune”

**Vertical enunț↔variante:**
- A: **CONDITIONAL, NU FALS UNIVERSAL**. RMS `I=sqrt((1/T)∫i(t)²dt)` este număr real, măsurabil și echivalent termic; nu reprezintă *semnalul instantaneu*.
- B: **POTRIVIT modelului timp-real versus fazor complex**. `i(t),u(t)` sunt mărimi instantanee reale, fazorul este reprezentare matematică complexă.
- C: **CONDITIONAL, NU FALS UNIVERSAL**. Media pe o perioadă pentru sinus fără componentă DC este 0 A, un număr real, nu un obiect matematic imaginar; ca mărime derivată, nici media nu este semnalul instantaneu.

**Orizontal A↔B↔C:** A vs B = valoare efectivă agregată versus valoare la moment; B vs C = instantaneu versus media intervalului; A vs C = două funcționale diferite (RMS pozitiv în general, media sinusului poate fi nulă). **Nu se exclud prin cuvântul „real” în sens matematic/fizic uzual.**

**Model invers dedus din B:** autorul probabil contrastează *mărimi instantanee din domeniul timp* și *fazorii complecși*, nu afirma că RMS/media sunt nereale. Cuvântul **„singurele”**, rămas necalificat, face enunțul contestabil. Exemple: `i(t)=sqrt(2)sin(ωt) A` are `I_RMS=1 A`, `I_med=0 A`, ambele valori reale, iar `i(t)` instantaneu este real. **Nu** se poate elimina A/C ca false științific doar din „singurele”.

**Sursă și vecinătate:** *IEC 80000-6:2022*, §0.4.3 reprezintă expresia sinusoidală în timp și fazorul complex; §0.4.4 definește distinct RMS real, `I,U`: https://www.standards.iteh.ai/catalog/standards/iec/7c9bc1fb-b469-4ffb-8b51-1a40cb0af306/iec-80000-6-2022 . Această sursă a fost văzută în extrasul indexat; deschiderea HTML a eșuat, deci **nu** se pretinde text integral verificat. Regula contextului: vecinătatea §§0.4.3–4 arată că valori instantanee, RMS și fazori coexistă, nu că RMS este imaginar.

**Status:** `INTENDED_B_PROBABLE_TIME_DOMAIN` și `BLOCKED_LINGUISTIC_ABSOLUTE_SINGURELE`; dovadă pozitivă parțială, nu calificare oficială confirmată. User-gate necesar doar dacă rămâne imposibil de adjudecat după sursa exactă a autorului.

## ELE-245 | G1-ELE-245 / G2-ELEC-381 | AU-bd60af52c290f7af | barem A neschimbat
**Enunț:** „Un circuit de curent alternativ, pentru care factorul de putere este egal cu 1, este un circuit:”
- **A:** „pur rezistiv”
- **B:** „pur inductiv”
- **C:** „pur capacitiv”

**Vertical:** A = potrivit la `cos φ=1`, `φ=0`; B/C = incompatibile, fiecare prezintă `|φ|=90°`, PF=0 în modelul pur ideal. **Orizontal:** B și C sunt regimuri reactive de sens contrar, dar ambele PF=0; A nu este suprapunere fizică la borne cu B/C pure.

**Reversie/context:** A înseamnă *impedanță echivalent pur rezistivă la borne*; nu poate impune inventarul fizic „numai rezistoare”. Contraexemplu: `R=10Ω`, `X_L=X_C=20Ω`; `Z=10+j0Ω` și PF=1, deși circuitul conține L și C. Nu este contraexemplu la **A ca tip de comportament**, doar la interpretarea literală „fără L și C”. Sursa **OpenStax University Physics v2, §15.5**, ecuațiile (15.15–15.17) și explicația imediat următoare spun că la rezonanță `X_L=X_C`, `φ=0`, `Z=R`, comportament pur rezistiv: https://openstax.org/books/university-physics-volume-2/pages/15-5-resonance-in-an-ac-circuit . HTML deschis direct în această sesiune.

**Status:** `INTENDED_A_POSITIVE_EQUIVALENT_BEHAVIOR_SUPPORT` / `PHYSICAL_COMPONENTS_CAUTION`; nu există probă oficială ANRE 2026/QA independent.

## ELE-257 | G1-ELE-257 / G2-ELEC-392 | AU-23d536ba936f2f33 | barem B neschimbat
**Enunț:** „Unitatea de măsură a fluxului electric este:”
- **A:** „V/m”
- **B:** „Coulombul”
- **C:** „Faradul”

**Vertical:** A = unitatea intensității câmpului electric `E`, nu a fluxului; B = unitatea fluxului *inducției electrice* `Ψ_D=∫D·dS` dacă D în C/m²; C = unitatea capacității, nu a fluxului.
**Orizontal:** A și C au dimensiuni distincte; B nu poate fi dedus din simpla excludere a unităților greșite fără definiția pozitivă a fluxului din D.
**Reversie/context:** din B se deduce modelul de electrotehnică în care fluxul electric se definește prin D; se coroborează explicit cu definiția acelei discipline. **Nu** confunda cu fluxul câmpului E, `Φ_E=∫E·dS`, având unitatea V·m (în SI); nicio variantă nu oferă acea unitate.

**Surse:** extras tehnic de la Stephen Ellingson, *Electromagnetics I* LibreTexts §5.5: `∮D·dS=Q_encl`, `[D]=C/m²`, deci `[Ψ_D]=C`: https://phys.libretexts.org/Bookshelves/Electricity_and_Magnetism/Electromagnetics_I_%28Ellingson%29/05%3A_Electrostatics/5.05%3A_Gauss_Law_-_Integral_Form ; și tutorialul *Electric Flux Density and Electric Flux* §3.2.1: https://www.emfieldsandwaves.com/electrostatics/gauss-law/321-electric-flux-density-and-electric-flux/ ; ambele extrase indexate, deschidere HTML cache miss. **Cercetarea anterioară CKPT-051** a citat 2 manuale românești cu secțiuni și dimensiuni; nu se atribuie acea cercetare ca redeschidere nouă. Ambele definiții fizice E/D rămân în card ca diferență, nu drept evoluție terminologică dovedită.

**Status:** `INTENDED_B_POSITIVE_D_FLUX_UNIT` / `E_VS_D_DEFINITION_SCOPE_PRESERVED` / `NOT_INDEPENDENT_QA`.

## Preflight numeric/dimensional efectiv executat, distinct de QA de sursă
Script Python local în această sesiune, 5/5:
1. RMS de amplitudine `sqrt(2) A` = 1 A, valoare reală (ELE231) PASS.
2. Media unui sinus pe perioadă = 0 A, tot reală (ELE231) PASS.
3. `R=10, X_L=X_C=20 Ω` => PF=1, circuit RLC fizic (ELE245) PASS.
4. `D=2 C/m²`, `S=0,5 m²` => `Ψ_D=1 C` (ELE257) PASS.
5. `E=5 V/m`, `S=0,5 m²` => `Φ_E=2,5 V·m` (ELE257) PASS.

**Aceste teste verifică numai calcule/modelul, nu sursa, cheia oficială sau un reviewer independent.** În special nu s-a executat acum un preflight al scriptului pluginului v0.4.6, ci s-a aplicat metoda manual, cu calculele de mai sus.

## Handoff și contabilitate
- Trei unități **reanalizate fără duplicare**; coverage cumulativ neschimbat **114/568, 139/822**, 0/822 aprobate.
- Rezultat interpretativ: `ELE231=B_PROBABIL/TERMINOLOGIC_UNRESOLVED`, `ELE245=A_ECHIVALENT_SUSTINUT`, `ELE257=B_D_FLUX_SUSTINUT`, fără promovare în matrice de aprobare.
- Nu solicitați utilizatorului decizie pentru ELE245/257: domeniul didactic pozitiv este clar. ELE231 necesită verificare de context al autorului înainte de o eventuală întrebare utilizator.
- Următorul lot să introducă **unități P0 noi**, după verificarea against master/CKPT043–050, în locul unei noi reanalize inutile a acestor cazuri.
- **Nicio modificare a cheii, întrebării, surselor canonice, HTML, APK; fără merge/release.**
