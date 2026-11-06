# AI/ML Strategy and Evaluation Plan

| Attribute | Value |
|---|---|
| Document ID | AIML-001 |
| Version | 1.1 |
| Status | Refined strategy and evaluation baseline; no model selected |
| Related | SRS-001, SYS-ARCH-001, RTM-001, SAF-001, SEC-001, DATA-001, VVP-001 |

## 1. Purpose and scope

Define candidate AI task families, model-selection criteria, dataset governance, evaluation methods, output-safety controls, and model lifecycle. No model, dataset, provider, deployment route, or performance result is approved by this document.

## 2. Candidate task families and SRS mapping

| Task | Candidate SRS requirements | Potential value | Key limitations |
|---|---|---|---|
| OCR/text reading | FR-010, FR-011 | Read selected printed/digital text | Blur, glare, layout, language, small fonts, handwriting |
| Object recognition | FR-012 | Identify supported object classes | Occlusion, unfamiliar items, domain shift, false detections |
| Scene description | FR-013 | Summarize bounded visual context | Hallucination, omission, ambiguity, verbosity |
| Image question answering | Candidate only; not independently approved | Answer bounded questions about captured content | Unsupported inference and overconfidence |
| Speech interaction | FR-014, FR-015 | Voice commands and spoken responses | Noise, accents, language coverage, privacy |

Image question answering is not a committed release feature. Every capability must be separately scoped, prioritized, and approved.

## 3. Model and service selection criteria

Evaluate task-specific performance; subgroup/condition performance where appropriate; calibration/uncertainty; robustness; false-positive/negative severity; latency; memory; compute; energy; network dependence; licensing; data handling; cost; maintainability; provider retention; and failure modes.

Compare local, remote, and hybrid execution against SYS-ARCH-001. No model should be selected on benchmark accuracy alone.

## 4. Dataset governance

For every dataset record source, owner, provenance, acquisition date, license, consent, permitted use, population/environment coverage, annotation protocol, quality checks, sensitive content, split strategy, leakage controls, storage/access/retention, and limitations.

Do not use personal recordings for training without lawful rights and separate informed authorization. Keep training, validation, test, participant-research, and operational user data appropriately separated. Dataset decisions are governed by DATA-001 and SEC-001.

## 5. Evaluation metrics by task

- **OCR:** character error rate, word error rate, exact-match rate, layout/reading-order errors, and task usability.
- **Object detection/recognition:** precision, recall, class-wise performance, false-positive/negative analysis, and confidence/uncertainty behavior.
- **Scene descriptions:** factuality, omission severity, hallucination rate, unsupported safety statements, usefulness, and structured human review.
- **Speech recognition:** word error rate by supported language/accent/noise condition, command completion, false activation, and recovery.
- **End-to-end:** task completion, response latency, cancellation/interrupt success, failure recovery, comprehension, and user-rated usefulness.

Report sample sizes, test conditions, model/version, confidence intervals where appropriate, failure examples, and evaluation-data provenance. Metrics must match the actual capability and intended use.

## 6. Robustness, fairness, and uncertainty

Test relevant variation in lighting, distance, motion blur, occlusion, camera angle, clutter, indoor/outdoor settings, noise, language variation, and supported device constraints. Examine performance differences across relevant conditions without unnecessarily inferring sensitive attributes. Define abstention/uncertainty behavior for ambiguous, unsupported, or low-quality inputs.

## 7. Output safety

Distinguish recognized content from inferred context. Never convert uncertain perception into safety instructions. State when the system cannot determine an answer. Do not fabricate details. Keep outputs within the selected task scope. Do not claim a path is clear, an obstacle is absent, or a crossing is safe. Apply SRS FR-018–020 and SAF-001 controls.

## 8. Model lifecycle and change control

Maintain model card, source/version, license, preprocessing, prompts/configuration where applicable, dataset references, evaluation results, known limitations, dependencies, deployment location, monitoring, rollback, and retirement criteria. Re-evaluate after model, dataset, prompt, provider, hardware, or preprocessing changes. Material changes require impact analysis and an ADR where appropriate.

## 9. Release criteria

A capability requires:
- Approved task scope and user need.
- Lawful dataset/model rights and documented provenance.
- Task-specific acceptance thresholds approved before release.
- Representative evaluation and failure analysis.
- Tested uncertainty/abstention and stale-response behavior.
- Verified privacy, security, safety, and accessibility controls.
- Documented limitations and rollback/disable strategy.

A single aggregate accuracy score or successful demonstration is insufficient.

## 10. Open work

Select the first bounded use case; validate it with intended users; identify lawful datasets; define scenario coverage and thresholds; benchmark candidate models on target devices; assess external providers; complete model/data cards and controlled evaluation records.

## 11. Version history

| Version | Date | Change |
|---|---|---|
| 1.0 | Initial | Initial task-family and evaluation strategy. |
| 1.1 | 2026-11-06 | Added SRS mapping, explicit non-commitment for image QA, dataset separation, uncertainty/abstention, provider evaluation, and release/change-control criteria. |
