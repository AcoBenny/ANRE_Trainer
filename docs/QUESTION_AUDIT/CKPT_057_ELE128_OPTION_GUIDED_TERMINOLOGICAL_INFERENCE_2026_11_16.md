# CKPT-057 | ELE-128: inferarea sensului din alternative, cu control anti-circularitate | 2026-11-16

## Proveniență și delta față de CKPT-056
- Continuă CKPT-055/056, fără a repeta sau a credita unități noi. PR #7 OPEN/DRAFT; ramură `audit/anre-v8-priority-17-20261109`; HEAD verificat înainte de scriere `09efae82c83c69bf23109fbef9bc87567f504fc7`.
- Același caz: `ELE-128` / `G1-ELE-128` / `G2-ELEC-268` / `AU-14fb0886051fa595`; barem importat **A**; enunțul și A/B/C nemodificate.
- Explicație suplimentară a utilizatorului, citat integral:
  > „Pentru întrebarea anterioară se folosește pur inductiv pentru că orice altă explicație ar duce la sensul cel cu 45° și dacă nu se găsește în răspuns atunci se ia sensul care ar putea să sugereze unul din răspunsuri”
- **Nuanță față de prima interpretare din CKPT-056:** utilizatorul nu susține că termenul „cu caracter inductiv” are întotdeauna definiția fizică „pur inductiv”. Îl *restrânge contextual* la „pur inductiv” **prin citirea A/B/C ca indiciu despre simplificarea urmărită de autor**. Aceasta este regula de interpretare de grilă descoperită, nu o rescriere a terminologiei din manual.

## Regula operațională: alternativele sunt context interpretativ, nu sursa adevărului
1. Pentru fiecare sens plauzibil, calculați consecința fizică: **RL mixt** cu `R=X>0` produce `φ=45°`, însă **inductiv pur** cu `R=0`, `X>0` produce `φ=90°`.
2. Confruntați cu alternativele originale: **A** `+90°`, **B** `0°`, **C** `-90°`. Nicio alternativă nu exprimă `45°`. Semnele fac B (rezistiv) și C (capacitiv) incompatibile cu un model inductiv net. **A** corespunde singurului caz-limită inductiv listat, model pur inductiv. Astfel, dintre răspunsuri **A este intenția cea mai probabilă a testului**.
3. Păstrați semnificația științifică și contraexemplul **separat**: caracter inductiv generic nu implică exact 90°; cazul RL mixt rămâne valid. **Nu** clasificați A drept teoremă universală sau cheie oficială ANRE doar pentru că eliminarea favorizează A.

### Anti-circularitate: cazuri negative obligatorii
- Dacă opțiunea unică rămasă **contrazice** chiar modelul din enunț sau o sursă de același scop, **nu o forțați**. Marcați `NO_SUPPORTED_EXACT_OPTION` și escaladați.
- Dacă două variante descriu regimuri specializate plauzibile, sau dacă o condiție esențială ar trebui *inventată* în loc de dedusă din context, marcați `NON_UNIQUE_OR_UNSPECIFIED_CONDITION`.
- Dacă una dintre opțiuni ar exprima explicit `45°`, comparația nu mai justifică restrângerea automată la circuit pur inductiv. Reevaluați enunțul și bibliografia.
- Dacă toate cele trei variante sunt greșite pentru interpretarea științifică generală, dar una este corectă într-o **idealizare standard didactică** susținută de surse, înregistrați simultan `EXAM_INTENT_PROBABLE` și `TECHNICAL_QUALIFIER_MISSING` (nu `ANSWER_APPROVED`).

## Învățare cumulativă / aplicare transversală
**Regula indicilor din variante:** `semantic candidates from question → exact A/B/C → infer likely author's intended model → confirm model is physically coherent and bibliographically plausible → keep counterexample and source limits → separate intended exam answer from universal truth → independent QA`.

Transfer la ELE-222: alternativa **C** („reactanței”) poate revela intenția de **model pur reactiv** în opoziție cu „impedanței” (admitanță) și „rezistenței” (conductanță); totuși **nu** schimbă formula complexă corectă pentru circuit mixt și nu oferă singură dovadă de barem oficial.

## Stare și limite
- `ELE128_USER_ANSWER_OPTIONS_CONTEXT_HEURISTIC_RECORDED`.
- `ELE128_EXAM_INTENT_A_PROBABLE_PURE_L`.
- `ELE128_GENERIC_INDUCTIVE_RL_COUNTEREXAMPLE_PRESERVED`.
- `NOT_OFFICIAL_KEY_VERIFIED` / `NOT_INDEPENDENT_QA` / `NOT_APPROVED_FOR_LEARNING`.
- Nu au fost introduse întrebări, A/B/C, bareme, HTML, APK sau merge/release noi; totalurile CKPT-054 rămân 114/568 unități, 139/822 ID-uri documentate contextual și 0/822 aprobate.

## Addendum: eliminare bidirecțională enunț–variante și între variante

**Clarificare textuală a utilizatorului (citat exact):**
> „Corect că deducerea prin eliminare se poate face și întrebarea versus răspunsurile nu doar între răspunsuri”

**Regulă generalizată, complementară CKPT-057, nu o fișă nouă:**
1. **Enunț ↔ A/B/C (vertical):** verifică dacă fiecare variantă poate satisface obiectul, condițiile, calificativele, contextul terminologic și rezultatul matematic al *întrebării*. Elimini sau condiționezi alternativele incompatibile. Variantele pot furniza indicii despre modelul didactic implicat de autor, dar nu îl dovedesc singure.
2. **A ↔ B ↔ C (orizontal):** compară opțiunile între ele pentru contradicții, incluziuni, suprapuneri, excepții, relații general–particular și imposibilitatea ca unele să fie simultan adevărate.
3. **Verificare înapoi (reversibilă):** reconstruiește sensul probabil al enunțului din opțiunea candidat și verifică-l în definițiile aplicabile, sursa bibliografică și cazurile-limită. Nu confunda o opțiune rămasă prin eliminare cu dovada afirmativă că este universal corectă.

**Exemplu ELE-128:** față de enunțul cu „caracter inductiv”, B (0°) indică echivalent rezistiv și C (−90°) capacitiv; A (+90°) este modelul inductiv pur inclus în opțiuni. Interpretarea generică RL cu φ=45° rămâne fizic posibilă, dar nu apare ca opțiune. Rezultat: **A ca răspuns intenționat probabil, nu definiție universală a caracterului inductiv**.

**Teste negative obligatorii:** (i) niciun răspuns exact în domeniul indicat; (ii) mai multe variante simultan adevărate; (iii) unica variantă rămasă contrazice o sursă de exact același domeniu; (iv) deducerea necesită inventarea unei condiții nejustificate. În toate aceste situații păstrează blocajul/ambiguitatea, chiar dacă testul are o cheie istorică.

**Trasabilitate:** această clarificare aparține utilizatorului și îmbunătățește *metoda de raționare* în orice domeniu, nu schimbă baremul ELE-128, nu execută QA independent și nu crește numărul de unități auditate. 114/568, 139/822, 0 aprobate pentru învățare. Fără modificări HTML/APK/merge/release.
