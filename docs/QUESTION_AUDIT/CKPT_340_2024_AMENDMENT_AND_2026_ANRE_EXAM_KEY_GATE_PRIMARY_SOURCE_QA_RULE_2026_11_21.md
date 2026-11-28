# CKPT-340 | 2024 amendment, ANRE 2026 public examples, original-PDF negative QA gate | 2026-11-21

## Real sources and observations
- Prior PR #7 Draft HEAD `cbbb0acc7ea147bb81d37559f9f02eb48d04066a`; no canonical/app mutation.
- **Regulatory amendment:** ANRE Order 65 of 10 September 2024, published 13 September 2024, changes **art. 13(1)** of the regulation approved by Order 66/2023. The operative text does **not** change art.35: https://legislatie.just.ro/Public/DetaliiDocumentAfis/288327 . This specific order does not prove no 2025/2026 art.35 amendment exists; further amendment/edition check required.
- **Official ANRE public page reopened 21 November 2026:** https://anre.ro/participanti-la-piata-de-energie/persoane-fizice/energie-electrica/ lists the 2023 exam bibliography, current 2026 exam-season announcements, Grade I example question XLSX materials (Electrotehnică 09.2024, Legislație 05.2023, Norme 05.2023), and a link titled 'Formular înscriere răspunsuri examen'.
- On this **one examined page**, a local scan found **no item labeled 'barem', 'răspunsuri corecte' or 'cheie oficială'**. This narrow negative finding does NOT establish that a full official keyed answer bank does not exist elsewhere. A blank-form link is not proof of the exam's official correct answer letters. Previous V246 had original question wording but no official scored key.

## Mandatory original-source cross-render gate: reusable QA negative regression
- Original issuing authority PDF: https://anre.ro/wp-content/uploads/2023/05/Ord-66-2023.pdf ; original Monitorul Oficial 417/16 May 2023 **printed page 9, PDF zero-based index 7**, art.35 A(a)(i) reads **'pentru gradul I, vizată la zi'**; clause (ii) requires association with another suitable authorized electrician. Printed page 10 / PDF index 8 continues the next clause b (Grade II/III/IV-specific conditions).
- Portalul Legislativ HTML rendering https://legislatie.just.ro/Public/DetaliiDocumentAfis/270204 and https://legislatie.just.ro/Public/DetaliiDocument/288046 appears to associate text about **Grade II/III/IV** with Grade I art.35 A(a)(i). The underlying cause has NOT been proved; do not label it OCR or legal amendment without further evidence.
- **Negative regression specification `GRADE_I_PFA_II_III_IV_SUBSTITUTION`:** FAIL a proposed source mapping if it assigns a requirement for grade II/III/IV to the Grade I art.35 A(a)(i) solely from conflicting HTML, when the actual original PDF shows 'gradul I'.
- **Positive research specification `GRADE_I_PFA_2023_ORIGINAL_PDF`:** a Grade I source-fidelity PRECHECK may pass based on original PDF plus neighboring articles, but cannot pass the current-2026-edition, examiner official-key or independent signoff gates.
- The above regression cases are **manual evidence-gate specifications**, not an executed automated test suite. The original PDF was actually visually inspected; direct original PDF binary SHA256 acquisition in this runtime was NOT_RUN.
- An external Parallel AI research response suggested this contradiction; that was corroborated on **the official scanned original PDF**, not accepted as a replacement expert signature. CKPT-339 and V253 supersede two erroneous source-assignments in CKPT-338/V252, without erasing earlier records.

## Next gating tasks
1. Certify the exact 2026 applicable edition for every cited norm and any relevant amending instrument, not just 2024 Order 65.
2. Find authenticated official ANRE scored answer keys/errata where available, otherwise label all imported keys as such rather than certified official correctness.
3. Perform independent qualified technical/legal and linguistic review against the ORIGINAL A/B/C and exact source-context page. All 136 explicit semantic holds remain OPEN; all 822 grade routes need final checks; learner approvals **0/822**.

Only this new audit document is written; no question, key, HTML, APK, main, merge or release change.
