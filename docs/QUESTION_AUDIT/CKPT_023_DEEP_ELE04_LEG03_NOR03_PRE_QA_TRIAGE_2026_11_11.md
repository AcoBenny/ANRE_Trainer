# CKPT-023 | 3 loturi noi ANRE: ELE-04 / LEG-03 / NOR-03 | 2026-11-11

**Repo:** `AcoBenny/ANRE_Trainer`, PR #7 **Draft**, branch `audit/anre-v8-priority-17-20261109`. Continuă CKPT-022, fără Perplexity și fără repetarea loturilor deja cercetate.

## Rezultat efectiv
| Lot | Unități exacte QABC cercetate preliminar | ID-uri originale asociate | Tip |
|---|---:|---:|---|
| DEEP-ELE-04 | 20 | 39 | Electrotehnică (1 P1, rest P2) |
| DEEP-LEG-03 | 20 | 20 | Legislație (20 P1) |
| DEEP-NOR-03 | 20 | 20 | Norme (20 P1) |
| **Total nou** | **60** | **79** | **CERCETARE PRE-QA, NU APROBARE** |

Acumulat: **10/30 loturi cercetate preliminar, 200/568 unități QABC, 265/822 ID-uri originale**. **0/30 loturi închise definitiv, 0/822 întrebări aprobate pentru învățare.** 20 loturi/368 unități/557 ID-uri încă fără fișă aprofundată pre-QA; în plus cele 10 loturi cercetate necesită audit independent.

## Dovezi salvate
- [DEEP-ELE-04 / 20 unități](DEEP_EXECUTION_2026_11_11/DEEP_ELE_04_ALL_20_PRE_REVIEW_SOURCE_ABC_TRIAGE.csv)
- [DEEP-LEG-03 / 20 unități](DEEP_EXECUTION_2026_11_11/DEEP_LEG_03_ALL_20_PRE_REVIEW_SOURCE_ABC_TRIAGE.csv)
- [DEEP-NOR-03 / 20 unități](DEEP_EXECUTION_2026_11_11/DEEP_NOR_03_ALL_20_PRE_REVIEW_SOURCE_ABC_TRIAGE.csv)

Fiecare rând conține ID de unitate și hash, surse/locator, **raționamente A/B/C individuale**, observarea sau lipsa accesului, candidat marcat *NOT_APPROVED*, blocaj și `independent_review=NOT_RUN`. Pentru ELE-04 fiecare unitate păstrează separat cheile tuturor celor 39 ID-uri Grade I/II. Căutările web și sursele anterioare sunt diferențiate de accesarea exactă nouă; referințele didactice generale nu primesc statut de dovadă decisivă.

## Constatări importante pentru viitorul QA
1. **G1-LEG-043:** Regulamentul de furnizare aprobat prin Ordinul ANRE 5/2023 **art.26(4)(b)** precizează `5 zile lucrătoare` pentru neplata facturii la clienții noncasnici; întrebarea din bancă menționează `5 zile` fără tipul de zile și extinde formularea generic la nerespectarea obligațiilor contractuale. Nu valida fără precizare de cauză/termen.
2. **G1-LEG-040:** Reg66/2023 art.9(a)/art.35(A)(a) susține 10kW/<1kV fără atestat de operator economic în condiții, dar art35(A)(a)(i), în forma consolidată citită, cere autorizație grad II/III/IV chiar în alineatul intitulat grad I. Este **neconcordanță textuală a sursei** de clarificat cu istoricul modificărilor, nu aprobarea automată a C.
3. **G1-NOR-054:** I7 5.4.22 recomandă **0,6–1,5m** pentru întrerupătoare/comutatoare/butoane, iar cheia originală A spune numai 1m. B reproduce intervalul, dar diferă descrierea punctului măsurat (ax versus aparat); candidat **B**, QA lingvistic și normativ necesar.
4. **G1-NOR-041:** I7 §5.2.4.6.1 menționează monofazat **două conductoare** și polifazat ≤16mm² Cu /25mm² Al; banca spune monofazat **trei conductoare**. Susține numeric B, dar nu neapărat obiectul complet.
5. **G1-NOR-050/051:** minima 2,5mm² Cu este candidat în circuitele vizate, dar variantele 4mm² Al pot fi valide în alt material; se cere analiza **anexei 5.32**, nu eliminare automată C.
6. **G1-LEG-047:** definiția ATR/ofertă versus accept, în forma actualizată Reg59/2013, necesită deschidere art3 și comparație semantică; pagina directă a returnat timeout.
7. **G1-ELE-007:** alunecarea 0–1 este domeniul normal *motoring*; modurile generatoare/frânare au alte valori. **G1-ELE-009/026/033:** «nu se folosește», «se preferă», și afirmațiile de incendiu/economie depind de configurație și condiții.
8. **G1-LEG-041/045/046/050:** Ordin5/2023 confirmă orientativ 42 zile, clasificarea căminelor studențești și IMM, eșalonarea clientului vulnerabil; **nu** certifică exhaustiv toate amendamentele la 11.11.2026.

## QA executat / lecție de regresie
- Primul validator structural a așteptat numai `next_gate`, deși ELE folosește `remaining_gate`. Rezultat inițial: **false structural FAIL pe20 ELE**. Datele efective erau prezente; am schimbat checker-ul local să citească ambele variante și am reluat verificarea integrală.
- **Recheck PASS:** 60/60 unități și 79/79 ID-uri trase la `UNITS_568`, `ID_ROUTING_822`, V73; hash QABC, textul întrebării și variantele A/B/C, cheia originală, gradul, riscul și batch identice; fiecare rând are sursă/locator, ABC, blocaj și status **NOT_RUN / NO**. **0 diferențe canonice**.
- Testul verifică structura, nu ediția, acoperirea sursei exacte sau adevărul variantelor. **Review independent și calificat: NOT_RUN**, nicio aprobare pentru învățare, nicio versiune de manual declarată vizual certificată. Pagini printabile I7 au întors 502, text indexat disponibil; nu afirma inspectarea vizuală a PDF-urilor.
- **Nicio schimbare la întrebările/baremurile originale, HTML, APK, `main`, merge sau release.** Nu este pornit niciun worker asincron.

## Handoff
Prioritizează verificarea independentă a conflictelor G1-NOR-054 și G1-LEG-040/043 și sursele I7/anexa 5.32; apoi următoarele loturi care nu sunt cercetate: `DEEP-ELE-05`, `DEEP-LEG-04`, `DEEP-NOR-04`. Menține sursele generice ca indicii, nu le promova prin simplă clasificare.
