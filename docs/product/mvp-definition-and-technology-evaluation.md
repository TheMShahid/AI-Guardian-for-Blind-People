# MVP Definition and Technology Evaluation

| Attribute | Value |
|---|---|
| Project | AI Guardian for Blind People |
| Document ID | MVP-001 |
| Version | 0.2 |
| Status | Proposed planning baseline — stakeholder validation and feasibility review pending |
| Document Type | Product Scope and Technology Evaluation |
| Related | PID-001, PMP-001, SRS-001, RTM-001, SYS-ARCH-001, ADR-REG-001, AIML-001, HW-001, ICD-001, SAF-001, SEC-001, ACC-001, VVP-001, DATA-001, ICD-MVP-001, ENG-READY-001 |
| Prepared | 06 November 2026 |

## 1. Purpose

Define a deliberately small first software prototype, identify capabilities that should be deferred, and establish a technology evaluation approach. This document supports discovery and feasibility planning; it does not approve a production architecture, certify a product, or authorize safety-critical use.

The MVP boundary is provisional until reviewed against evidence from blind and low-vision users and technical feasibility work.

## 2. MVP Strategy

The first prototype should validate one complete, bounded, useful workflow before adding multiple AI capabilities or custom hardware.

**Proposed MVP-1: User-initiated printed-text reading through a smartphone.**

A user starts a text-reading task, explicitly captures a still image of a document or sign in a controlled setting, receives OCR output, and listens to the recognized text through accessible speech output. The user can stop speech, replay it, and end the task.

This is a candidate starting point because it is narrower and easier to evaluate than open-ended scene interpretation or navigation assistance. It does not assume that OCR will be accurate for every language, font, surface, lighting condition, or camera position.

## 3. Intended User Outcome

A blind or low-vision user should be able to request reading of selected visible text and receive the recognized content through controllable audio, while being clearly informed when capture or recognition fails or the result may be incomplete.

The prototype is supplementary information access. It must not imply that a sign, label, document, or instruction has been interpreted perfectly.

## 4. MVP-1 Scope

### 4.1 Included capabilities

| ID | Capability | MVP expectation |
|---|---|---|
| MVP-F-001 | Accessible task entry | Launch the text-reading workflow without requiring visual-only interaction |
| MVP-F-002 | Permission handling | Explain and request camera permission at point of use; provide a usable denial path |
| MVP-F-003 | User-controlled capture | Capture a still image only after an explicit user action; communicate capture state |
| MVP-F-004 | OCR processing | Extract text from the captured image using a replaceable OCR adapter |
| MVP-F-005 | Spoken result | Read recognized text using supported device speech output |
| MVP-F-006 | Speech control | Allow the user to stop and replay spoken output |
| MVP-F-007 | Failure communication | Announce camera, permission, image-quality, OCR, and processing failures accessibly |
| MVP-F-008 | Session lifecycle | Start, cancel, complete, and safely reset a reading session |
| MVP-F-009 | Privacy behavior | Avoid retaining captured images by default; explain any data processing and storage |
| MVP-F-010 | Basic settings | Provide accessible speech rate and verbosity controls where supported |

### 4.2 Explicitly deferred from MVP-1

- General object detection and object identification.
- Open-ended scene description and image question answering.
- Continuous video capture or continuous listening.
- Autonomous navigation, obstacle avoidance, route guidance, or road-crossing decisions.
- Custom wearable/portable hardware and embedded firmware.
- Remote supporter monitoring or sharing.
- User accounts, cloud history synchronization, and social features.
- Model training on user recordings or images.
- Emergency response or medical functionality.

Deferred does not mean permanently rejected. Any scope expansion requires user-need evidence, impact analysis, updated requirements, safety/privacy review, and change control.

## 5. Primary User Workflow

1. User opens the accessible application and selects the text-reading task through a validated accessible control. Voice-command initiation is not assumed in MVP-1; it may be added only if separately validated and approved.
2. Application announces that the camera is needed and requests permission if not already granted.
3. Application gives a clear capture-ready status.
4. User explicitly initiates a still-image capture.
5. Application confirms capture and processes the image.
6. OCR adapter returns recognized text, status, and available quality/uncertainty information.
7. Application announces whether text was found and reads the result.
8. User may stop or replay speech, retry capture, or end the session.
9. Session ends and temporary image data is discarded according to the approved data policy.

The exact interaction wording, accessible controls, supported languages, and capture ergonomics require evaluation with intended users.

## 6. MVP Acceptance Evidence

MVP-1 is not considered successful merely because a demo works once. Before a controlled prototype review, collect evidence for:

- Completion of the end-to-end workflow using the intended screen reader and non-visual interaction method.
- Correct permission and capture-state behavior, including permission denial and cancellation.
- OCR quality on a documented, lawfully acquired evaluation set representative of the selected initial text conditions.
- Reading-order and text-recognition error analysis, not only a single aggregate accuracy score.
- Speech stop/replay behavior and recovery from interrupted sessions.
- Clear handling of blank, blurred, rotated, low-light, unsupported-language, and unreadable inputs.
- Confirmation that images are not retained or transmitted contrary to the documented policy.
- Measured response time and resource use on the selected test device.
- Usability feedback from appropriately recruited and consented blind/low-vision participants, after required ethics and safety review.

Numerical thresholds, supported languages, target devices, and sample sizes remain TBD until discovery and feasibility evidence are available. No participant evaluation or test pass is claimed by this document.

## 7. Technology Evaluation

### 7.1 Mobile application candidates

| Candidate | Strengths to evaluate | Risks / trade-offs to evaluate |
|---|---|---|
| Native Android (Kotlin) | Direct Android accessibility, camera, lifecycle, permissions, and speech APIs | Android-only initial implementation; Kotlin learning and maintenance requirements |
| React Native (TypeScript) | Shared JavaScript/TypeScript skills and potential cross-platform reuse | Native camera/OCR integration and accessibility behavior may depend on libraries and native modules |
| Flutter (Dart) | Consistent UI framework and cross-platform application structure | Dart learning; platform-specific camera, OCR, and accessibility behavior still requires validation |

**Provisional evaluation preference:** begin feasibility spikes with native Android (Kotlin) as the reference candidate for an Android-first MVP, because the first workflow depends heavily on Android camera, permission, TalkBack, and text-to-speech integration. This is not a final technology decision. Compare a small React Native proof-of-concept if cross-platform delivery or development maintainability materially changes the decision.

### 7.2 OCR candidates

Evaluate at least:
- On-device OCR integrated with the selected mobile platform.
- A separately replaceable OCR engine suitable for the selected languages and license constraints.

Compare character/word error rates, reading order, language coverage, offline behavior, latency, memory, device compatibility, licensing, privacy, and failure behavior. Do not select an OCR engine based only on a vendor accuracy claim.

### 7.3 Speech output

Prefer platform text-to-speech for the first prototype where language and voice quality meet the validated need. Record supported languages/voices and behavior when a requested voice is unavailable. Speech output must remain interruptible.

### 7.4 Backend and storage

A remote backend is not required by the proposed MVP-1 workflow unless feasibility, security, or a validated user need demonstrates otherwise.

- Prefer on-device capture and OCR evaluation initially.
- Do not introduce account registration or cloud image storage without a justified requirement.
- Store only necessary preferences or non-sensitive session metadata, if required.
- Keep OCR, speech, capture, and session logic behind replaceable interfaces.
- If a backend becomes necessary, assess a Python-based service separately with authentication, authorization, transport security, data minimization, retention, and provider review.

### 7.5 Device and hardware

Do not select a microcontroller, single-board computer, camera module, battery, or wearable form factor for MVP-1. The smartphone is the initial sensing and interaction platform for the proposed software workflow. A connected-device feasibility prototype is a later stage after the software workflow and user needs are better understood.

## 8. Proposed Logical MVP Components

| Component | Responsibility |
|---|---|
| Accessible Application Shell | Screen-reader-compatible navigation, task entry, settings, status |
| Reading Session Controller | Start, cancel, retry, completion, and stale-result prevention |
| Camera Capture Adapter | Permission-aware, user-initiated still-image capture |
| OCR Adapter | Image-to-text processing behind a replaceable interface |
| Speech Output Adapter | Speak, stop, replay, and speech preferences |
| Privacy/Session Data Manager | Temporary media lifecycle and minimal local preferences |
| Diagnostics | Non-sensitive error categories and operational status |

These are logical responsibilities, not an approved source-code folder structure or final deployment design.

## 9. Technology Decision Criteria and Weights

The following criteria should be scored during feasibility work. Weights are provisional planning aids, not measured results.

| Criterion | Proposed weight |
|---|---:|
| Non-visual accessibility and TalkBack behavior | 25% |
| Camera, permission, and lifecycle integration | 20% |
| OCR and speech integration quality | 15% |
| Privacy and on-device processing support | 15% |
| Reliability, testability, and maintainability | 10% |
| Development effort and available skills | 10% |
| Future device integration | 5% |
| **Total** | **100%** |

A candidate must not be selected if it fails a critical accessibility, privacy, or safety constraint, regardless of its weighted score. Record actual spike results, versions, test devices, limitations, and rejected alternatives before creating an approval-ready ADR.

## 10. Delivery Sequence and Exit Gates

| Stage | Work | Exit evidence |
|---|---|---|
| M0 | Validate user need and text-reading workflow | Reviewed user journey and documented assumptions |
| M1 | Compare mobile technology candidates | Reproducible camera, TalkBack, permission, and speech spikes |
| M2 | Compare OCR candidates | Licensed test data, task-specific evaluation, error analysis |
| M3 | Build the bounded software prototype | End-to-end workflow and component-level verification evidence |
| M4 | Conduct controlled accessibility and usability evaluation | Required approvals, accessible consent, participant findings, risk review |
| M5 | Decide next scope | Evidence-based decision to refine MVP, add another task, or begin device feasibility |

Progression between stages requires review of evidence and unresolved risks. Calendar estimates are intentionally omitted until effort and resource assumptions are known.

## 11. Safety, Privacy, and Accessibility Constraints

- The prototype is not a mobility aid and must not provide crossing or obstacle-avoidance instructions.
- The user controls capture and can cancel the task and stop speech.
- Capture state and processing failures must be announced accessibly.
- No continuous capture by default.
- Do not retain or transmit images unless explicitly required, explained, authorized, and covered by the approved data policy.
- Do not use personal or participant data for model training without separate appropriate authorization.
- Unreadable or uncertain text must be reported as such; the system must not invent missing words.
- Evaluate with screen readers and users with relevant lived experience before claiming accessibility.
- Prototype use and evaluation must follow SAF-001, SEC-001, ACC-001, DATA-001, and VVP-001.

## 12. Assumptions, Dependencies, and Open Work

### Assumptions for planning only
- A smartphone-based text-reading workflow is a reasonable first feasibility target.
- A user-initiated still image is preferable to continuous capture for the first prototype.
- Local processing should be evaluated before remote image transfer is introduced.
- A small, bounded workflow will provide clearer evidence than implementing several AI features simultaneously.

### Dependencies
- Access to suitable Android test hardware for feasibility spikes.
- Lawfully usable OCR evaluation data covering the initially selected text conditions.
- Access to TalkBack and relevant accessibility testing.
- Required accessibility, safety, privacy, and ethics review before participant research.
- Approved acceptance thresholds based on evidence rather than assumed targets.

### Open work
- Validate the primary workflow and language priorities with intended users.
- Confirm initial target device/OS coverage through feasibility testing.
- Complete mobile framework and OCR engine comparisons.
- Define the initial evaluation dataset and acceptance thresholds.
- Create an approval-ready architecture decision record after evidence is available.

## 13. Relationship to Controlled Requirements

MVP-001 proposes a subset and sequence for implementation planning; it does not silently approve or retire SRS-001 requirements. Once the MVP is reviewed, update SRS-001, RTM-001, SYS-ARCH-001, ICD-001, AIML-001, SAF-001, ACC-001, SEC-001, and VVP-001 through controlled change impact analysis.

## 14. Version History

| Version | Date | Change |
|---|---|---|
| 0.1 | 2026-11-06 | Initial proposed MVP-1 scope, workflow, technology evaluation criteria, and staged feasibility plan. |
