# ANRE Trainer | UI visual QA contract (future release)
Academy AGENT-014 evidence levels: static source, rendered screenshot, user interaction on real platform, independent review. Never infer UI PASS from build-only CI or programmatic clicks to hidden elements.

## Standalone HTML and Android APK
- Capture actual page/device screenshot with sensitive data redacted. Inspect buttons, tabs, question card, explanation, correct/wrong feedback, documentation fragment and pop-ups for clipping/overlap.
- Execute real tap/click and keyboard navigation where applicable: grade 1/2, answer selection, next/last question, repeat mistakes, randomized flow, document popup and local offline links.
- Compare small/high-DPI displays and check cards appear after answer (not duplicated). Distinguish offline function tests from screenshot appearance.
- Independent reviewer status NOT_RUN unless trace evidence exists. A generated APK or CI PASS alone cannot certify Android runtime.

**Status:** adopted as documentation only, no application code modified or content mapping status changed. The didactic corpus audit remains before release decisions.
Shared Academy policy: https://github.com/AcoBenny/Avengers-Asamble/blob/main/docs/VISUAL_QA_STANDARD.md.
