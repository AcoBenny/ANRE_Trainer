# CKPT-344 | ANRE single-correct scoring format and graphic authenticity gates | 2026-11-21

## Source directly reopened
- Regulation approved by Ordinul ANRE 66/2023: https://legislatie.just.ro/Public/DetaliiDocumentAfis/270204 .
- In **Anexa nr. 1, procedure for exam questionnaires**, points **10–13**, the regulation says the commission prepares the exam questions; point **11** states a questionnaire contains **25 questions with three answer variants**; point **12** says each question has **exactly one correct alternative**. Point 13 assigns an identification code to the questionnaire. Original website text was directly reopened and the entire nearby run 10–14 checked, 21 Nov 2026.
- The 2023 rule should not be confused with an older ANRE web archive document (2020) that was surfaced in search results and described at least one correct variant. The official 2023 source governs the currently studied model unless a later applicable change is demonstrated; do not claim an exhaustive no-amendment result without checking.

## Implications for the 822 trainer
1. `FORMAT_EXPECTED_ONE_CORRECT_ANSWER`: input grading model one choice per question is consistent with the 2023 procedure. This source DOES NOT authenticate any imported letter or validate a practice/question-bank item's text.
2. `TWO_PLAUSIBLE_ALTERNATIVES_NEGATIVE`: if exact source and stem permit two alternatives, the review must remain `HOLD_OPTION_NON_UNIQUENESS` rather than forcing a favorite based on elimination. This remains true even when the actual live exam is required to have one correct option.
3. `REWRITTEN_STEM_NEGATIVE`: a didactic rephrasing that repairs an exam example's ambiguity is separate from the published exam item. Preserve both texts and mark a reformulation as practice-only.
4. `FIGURE_LINK_NOT_ORIGINAL_SOURCE`: CKPT-343/V256 located 9 public alternative figure images but all 9 remain `IMAGE_ORIGINAL_NOT_AUTHENTICATED` until official XLSX embedded DrawingML or another authoritative official-image representation can be visually matched. Third-party answer letters cannot satisfy the official scoring-key gate.

## Regression fixture specifications (not automated execution)
| Fixture | Input | Expected status |
|---|---|---|
| ANRE66_2023_ONE_ABC | 25x3 answer format and point 12 | `EXAM_FORMAT_SUPPORTED_ONLY`, **not** key certification |
| EXAMPLE_WITH_TWO_SUPPORTED_OPTIONS | Original ambiguously supports A and B | `HOLD_OPTION_NON_UNIQUENESS`, no forced answer |
| THIRD_PARTY_IMAGE_JPEG_200 | Public response 200 but original XLSX graphic unavailable | `IMAGE_CANDIDATE_ONLY`, no visual original approval |
| OFFICIAL_XLSX_TEXT_ONLY | Original text matches, but three graphical A/B/C absent from extraction | `IMAGE_CHOICES_NOT_YET_RECOVERED`, not a complete exam question |

## Checkpoint
- Prior HEAD 6e70209ef1fc256f3ec403bb5f651686a188337d; PR #7 Draft. This is an **evidence-rule checkpoint**, not an executable test run.
- **136 prior explicit semantic holds remain open; 6 historic strict conflicts remain open; 9 original-source graphically missing rows are not source-authenticated; 0/822 independently approved.**
- No edits to canonical questions, A/B/C, imported keys, HTML, APK, `main`, merge or release.

