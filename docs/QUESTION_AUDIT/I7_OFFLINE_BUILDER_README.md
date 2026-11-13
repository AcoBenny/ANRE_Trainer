# I7 offline index | prototip sigur (fără schimbări în aplicație)

## Rulare
Necesită **Node.js 18+**, numai funcții incluse în Node (fără npm).

1. În repository: `node tools/build_offline_i7.mjs --self-test`.
2. Cu acces la Internet: `node tools/build_offline_i7.mjs`. Alternativ, dintr-o pagină HTML oficială salvată local: `node tools/build_offline_i7.mjs --input "i7.html"`.
3. Deschide `offline_legal_build/i7_offline.html` în browser chiar și fără Internet. Vei putea căuta text și numere de articole fără API, cloud, CSS sau JavaScript extern.

Portal: https://legislatie.just.ro/Public/DetaliiDocumentAfis/287132 . Legislația consolidată de pe portal este **consultativă**, nu substituie Monitorul Oficial: https://legislatie.just.ro/Public/Termeni.

## QA și limitele prototipului
- Recunoașterea de articole din HTML este euristică: titluri/fragmente repetate, liste și tabele complexe pot necesita o conversie supervizată; întreg textul brut rămâne disponibil în cititor.
- Sunt necesare **minimum 90.000 caractere, 70 secțiuni și repere I7** pentru a accepta sursa. În caz de eroare HTTP, CAPTCHA, HTML parțial sau lipsă articole, generatorul nu produce fișiere.
- Indexul nu este declarație de conformitate legislativă. `approved_for_app=false`, `independent_qa=NOT_RUN`, amprenta SHA-256 și data capturii sunt înscrise în manifest.
- Cu `--input`, `source_type=USER_SUPPLIED_HTML_UNVERIFIED` (nu este o descărcare oficială verificată); nu promova această versiune automat.
- **Nu s-a obținut încă o descărcare integrală în sesiunea ChatGPT**, conexiunea externă către portal a eșuat în container. Generatorul este livrabilul pregătit pentru executare pe un PC cu Internet.
- Nu înlocui sursele anterioare doar pentru că un fișier a fost creat; cere comparare de articole, istoric de modificări, verificarea anexelor/tabelelor și QA normativ.
- Versiunile vechi se mută logic în `archive` numai după înlocuitor aprobat și pot rămâne disponibile ca istoric; nu șterge PDF-urile din biblioteca personală.
- Nu modifica `app/src/main/assets/anre_trainer.html`, bareme, chei sau APK și nu face merge fără aprobarea utilizatorului.

## Următoarea etapă
Extinde manifestul cu ordinele ANRE și celelalte acte *individual*, validează data aplicabilității și mapează `question_id -> law_id, article_id, source_hash`. Pentru utilizarea în APK încorporează numai HTML-ul offline verificat în assets, cu test fizic fără conectivitate.
