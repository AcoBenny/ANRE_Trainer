# ANRE Trainer | Reguli de predare către etapa întrebărilor

**Acest fișier este protocol, nu demararea auditului întrebărilor.** Datele celor 822 de întrebări sunt înghețate până la autorizarea explicită de trecere de la etapa documentară.

## Unitatea de lucru la întrebări

Un rând de întrebare trebuie să păstreze: ID stabil (grad/tip/disciplină), textul original, opțiunile A/B/C în ordinea sursei, cheia originală și proveniența ei, versiunea sursei normative, pagina PDF și paragraful/figura. Auditul trebuie să separe în mod clar: afirmația întrebării, ipotezele necesare, validarea tehnică, validarea juridică și justificarea pedagogică.

## Clasificări acceptate

- `SUPPORTED_CLAUSE_VERIFIED`: propoziția exactă este susținută de un text deschis și aplicabil, iar nu doar de keyword-uri.
- `SUPPORTED_WITH_CONDITIONS`: corect în ipoteze explicit documentate.
- `CONFLICT`: surse/ediții sau răspunsuri incompatibile, **fără schimbarea baremului**.
- `NO_AUTHORITATIVE_SOURCE`: doar manual istoric/curs scanat/catalog/rezumat comercial.
- `NEEDS_INDEPENDENT_REVIEW`: calcul, siguranță, interpretare normativă ori controversă insuficient rezolvată.
- `SOURCE_MISMATCH`: sursa trimite la alt ID sau altă întrebare, conform crosswalk-ului de 76 din pilotul anterior.

## Blocaj de implementare

Nu actualiza HTML/APK, bareme, distribuire de cărți, figuri sau texte SR/IEC cu plată. Documentează propunerile separat și aplică doar după aprobare. Un review de către același model nu este «auditor independent».

## Ordine recomandată

1. Grad I și II, electrotehnică fundament și I7 din sursele deja inspectate.
2. Legislație: folosește textul oficial consolidat la articol și data din întrebare; nu manualul din 1995.
3. Subiecte cu risc: formule, diagrame, wording-capcană, ediții, A/B/C, surse care corespund altor ID-uri.
4. Control QA extern separat pentru schimbările de barem cu impact și acceptanță HTML/APK abia ulterior.
