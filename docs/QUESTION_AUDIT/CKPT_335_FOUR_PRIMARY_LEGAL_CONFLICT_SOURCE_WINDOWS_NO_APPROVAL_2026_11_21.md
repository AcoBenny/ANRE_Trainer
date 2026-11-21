# CKPT-335 | 4 conflicte de barem documentate cu surse legale primare, fără aprobare | 2026-11-21

## Verificare efectiv executată
- Baza verificată: PR #7 Draft, branch `audit/anre-v8-priority-17-20261109`, HEAD anterior `b4806abaf0d08856ed4ba493c990b4e1fd993999`.
- Deschise direct **două surse oficiale**: Legea 123/2012 pe Portalul Legislativ (`https://legislatie.just.ro/Public/FormaPrintabila/00000G0CDOUQ5TXYOEU0X4Y9QAXWNAF7`) și Regulamentul electricianilor aprobat prin Ordinul ANRE 66/2023 (`https://legislatie.just.ro/Public/DetaliiDocument/288046`). Ambele au returnat pagini HTML accesibile prin Firecrawl. Pentru Legea 123, pagina conține referința la OUG 9/27.02.2026, dar **nu demonstrează singură că toate modificările până la 21.11.2026 sunt incluse**.
- Confruntate **4 QABC / 4 ID-uri G1** cu enunțurile A/B/C și cheia importată conservate în V207/V209/V211, care sunt la rândul lor mapate prin V246 la originalele XLSX ale utilizatorului (fără o nouă citire a fișierelor binare în această rundă).
- Pentru fiecare: text legal original vizibil, vecinătăți/articol, obiect și condiții, A/B/C explicate; extrageri literale verificate prin potrivire directă cu sursa online accesată.

| QABC / întrebare | Cheia importată, NEMODIFICATĂ | Candidat susținut de sursa citită | Articol / problema exactă |
|---|---|---|---|
| QABC-0283 / G1-LEG-019 | C («Abatere») | **B** («Contravenție») | Legea 123 art. 93 alin. (1) pct. 3 califică nerespectarea normelor tehnice ANRE drept contravenție |
| QABC-0290 / G1-LEG-026 | C («contravenție sau infracțiune») | **B** («infracțiune») | Legea 123 art. 92 alin. (2) califică exact instalarea/folosirea clandestină pentru racordare directă ca infracțiune |
| QABC-0298 / G1-LEG-034 | B (participare chiar nesolicitată) | **A** (respectarea proiectului) | Regulament art. 37 lit. e) impune respectarea proiectului, lit. h) condiționează participarea la solicitare |
| QABC-0312 / G1-LEG-048 | A (impunerea oricărei metode de plată) | **B** (alegerea uneia oferite) | Legea 123 art. 57 alin. (2) permite alegerea dintre modalitățile oferite de furnizor |

## Dovezi detaliate
Fișierul [`V250_FOUR_PRIMARY_PORTAL_LEG019_026_034_048_SOURCE_WINDOWS_NO_KEYS_CHANGED_2026_11_21.json`](./V250_FOUR_PRIMARY_PORTAL_LEG019_026_034_048_SOURCE_WINDOWS_NO_KEYS_CHANGED_2026_11_21.json) conține pentru fiecare caz originalul întrebării și al variantelor, cheia inițială, pasajul relevant din sursa publică, contextul înainte și după, motivele A/B/C și toate porțile de validare rămase deschise. Contextul este cel din reprezentarea paginii web guvernamentale, care poate include normalizare de spații și separatori vizuali; nu se pretinde transcriere certificată a unui PDF.

## QA, limitări și next
- **PASS structural 4/4**: enunțurile, opțiunile și cheile au fost recitite din fișele editoriale existente; fiecare fragment de sursă extras există în pagina guvernamentală consultată. Nu este test independent de adevăr juridic.
- **PENDING**: ediția/consolidarea exactă aplicabilă în noiembrie 2026; confruntarea completă cu orice modificări și excepții aplicabile; baremul oficial ANRE pe grade; revizie juridică și lingvistică real independentă.
- **Cele 136 de blocaje rămân toate DESCHISE**, iar 0/822 sunt aprobate independent pentru învățare. Acest lot restrânge incertitudinea pentru patru cazuri, nu certifică bareme.
- Nicio întrebare, variantă, barem, HTML, APK sau `main` modificat; PR rămâne Draft, fără merge sau release.

Următoarea intervenție GFR: verificarea ediției aplicabile și a baremelor/eratelor oficiale pentru aceste patru, apoi escaladare către reviewer independent, respectând cele 10 pachete I7 din V249 și fără recercetarea trierei încheiate.
