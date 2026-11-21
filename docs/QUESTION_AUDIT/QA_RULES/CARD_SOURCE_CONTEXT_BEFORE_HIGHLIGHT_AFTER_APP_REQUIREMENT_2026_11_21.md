# Cerință ANRE Trainer: carduri cu context documentar ÎNAINTE + PASAJ EVIDENȚIAT + DUPĂ
**Decizie acceptată de utilizator:** 2026-11-21. **Tip:** cerință de produs / criteriu obligatoriu de QA pentru integrarea viitoare în aplicația HTML și APK. **Status:** APROBATĂ CA CERINȚĂ, NEIMPLEMENTATĂ, SURSELE NU SUNT AUTOMAT VALIDATE.

## Obiectiv
Când utilizatorul deschide cardul documentar după răspuns, nu afișăm doar o frază sau un grup de cuvinte decupate ca dovadă. Afișăm un **context mai amplu, păstrat fidel sursei**, cu pasajul care susține răspunsul evidențiat clar în **bold**.

## Format obligatoriu al cardului
1. **Context anterior:** propoziția/paragraful din sursa originală imediat dinaintea pasajului relevant, pentru identificarea situației, definițiilor și condițiilor.
2. **Pasaj central:** propoziția/paragraful exact, relevant pentru răspuns, **îngroșat (bold)** și integrat în același fir logic. Nu este obligatoriu să evidențiem tot paragraful; marcăm doar formularea care dovedește concluzia.
3. **Context ulterior:** propoziția/paragraful din aceeași sursă imediat după pasajul relevant, pentru continuare, limite, excepții și condiții conexe.
4. **Metadate și navigare:** titlul sursei, ediția/data, articolul/paragraful/pagina, un link către textul documentar integral și, când este disponibil, ancora locală offline. Contextul trebuie să poată fi extins în text integral.
5. **Explicațiile A/B/C și exercițiul reformulat sunt o secțiune distinctă**, sub extrasul documentar. Explicațiile editoriale nu se prezintă ca text citat din normativ.

## Proveniență și reguli de fidelitate
- Înainte / central / după = **text adiacent real** din aceeași sursă și ediție, în ordinea originală, nu paragraf inventat, comprimat sau extras din alt document.
- Se păstrează formularea, numerotarea, negațiile, condițiile și trimiterile normative. Nu se înlocuiește originalul cu versiunea Trainer ori invers; la diferențe materiale se afișează și marchează proveniența ambelor variante.
- Dacă pasajul este primul/ultimul dintr-o secțiune, e prea lung, include tabel/figură ori partea adiacentă lipsește din corpus, nu se fabrică un text de umplutură. Se arată contextul disponibil cu marcaj **CONTEXT INCOMPLET** și link spre documentul integral; QA rămâne blocat până la verificarea sursei.
- Dacă sensul depinde de titlu, definiții anterioare, excepții ori cross-reference, se extinde numai cât este necesar pentru a evita scoaterea din context, chiar dacă depășește un singur paragraf.
- Se evidențiază vizual pasajul relevant prin HTML semantic `<strong>` (sau echivalent accesibil), fără să se modifice textul sursei. Nu se îngroașă tot contextul.
- Un document fără sursă exactă verificabilă poate primi o explicație didactică separată, etichetată ca atare, dar nu un «citat original» fabricat.
- Când un text legislativ a fost schimbat, se păstrează ID-ul versiunii și se marchează aplicabilitatea temporală; o copie offline nu devine automat sursă legală în vigoare.

## Model de date recomandat pentru implementare
```json
{
  "card_id": "QABC-XXXX",
  "grade_ids": ["G1-..."],
  "source_version": {
    "title": "Titlu sursă",
    "edition": "Ediție / data sursei",
    "locator": "§ articol / paragraf / pagină",
    "offline_anchor": "ancoră verificată sau null",
    "source_url": "URL oficial/verificabil sau null"
  },
  "document_excerpt": {
    "before": "Text real anterior sau null",
    "focus": "Text central exact, relevant",
    "after": "Text real ulterior sau null",
    "source_exact": false,
    "context_complete": false,
    "bold_focus_only": true
  },
  "editorial_explanations": {
    "A": "De ce A este sau nu susținută, separat de citatul sursei",
    "B": "De ce B este sau nu susținută",
    "C": "De ce C este sau nu susținută"
  },
  "status": "DRAFT_NOT_INDEPENDENTLY_APPROVED"
}
```
Modelul de mai sus este schema-țintă orientativă, **nu o afirmație că datele au fost populate sau funcționalitatea a fost implementată**.

## Criterii de acceptare QA înainte de integrare
- [ ] Pentru fiecare card cu sursă disponibilă, se regăsesc în corpus **before / focus / after**, cu locatori și hash/ediție identificați; absențele sunt marcate, nu inventate.
- [ ] Pasajul central este evidențiat cu **bold**, iar textele înainte/după rămân lizibile și bine delimitate.
- [ ] Teste pozitive: citat la mijlocul secțiunii; citat care depinde de definiție anterioară; excepție în paragraful următor; ancoră offline funcțională.
- [ ] Teste negative: paragraf limită fără vecin; sursă lipsă; ediție depășită; surse cu condiții în conflict; întrebări cu variante originale ANRE diferite material de Trainer; text în tabel/figură.
- [ ] Verificarea este pe **exact același obiect, condiție, acțiune, grad și ediție** ca întrebarea. Nicio evidențiere nu transformă o sursă nepotrivită în dovadă.
- [ ] Evaluare separată a exactității sursei, argumentelor A/B/C și autentificării cheii de examen; doar un reviewer independent calificat poate bifa poarta de validare destinată învățării.
- [ ] Pe mobil și în HTML offline, nu se pierde contextul la deschiderea popup-ului, navigare, fonturi adaptabile ori evidențiere; legăturile locale nu necesită internet pentru documente deja incluse legal.
- [ ] Nu se confundă conținutul editorial/didactic cu citatele oficiale sau cu dovada unei chei oficiale.

## Limite de implementare și păstrarea statusului
Cerința este **salvată pentru integrarea viitoare**, după validarea surselor/cardurilor. Această înregistrare **nu modifică** baremele, întrebările, explicațiile deja existente, aplicația HTML, APK, fișierele sursă I7 sau gradele de validare. **PR #7 rămâne Draft; fără merge/release.** Până la aprobare finală: 0/822 ID-uri certificate pentru învățare conform CKPT-318.

## Următorul punct de reluare
Când începe faza de integrare a cardurilor: citiți **această cerință** împreună cu `CKPT_318_40_LAYER_TRANSVERSAL_STRUCTURAL_QA_SIX_STRICT_CASES_NO_APPROVAL_2026_11_21.md` și manifestul V241. Implementați explicit contextul sursei înainte / pasaj bold / după pentru toate cardurile aplicabile; păstrați excepțiile în stare blocată și rulați testele pozitive, negative și pe mobil.
