# Software Requirements Specification

| Attribute | Value |
|---|---|
| Document ID | SRS-001 |
| Version | 1.0 |
| Status | Initial requirements baseline — validation pending |
| Related | PID-001, SYS-ARCH-001, SAF-001, ACC-001, VVP-001 |

## 1. Purpose and conventions
This document defines candidate software requirements for discovery and prototype planning. It is not evidence of implementation. Priority: P0 = essential foundation, P1 = high-value initial capability, P2 = later capability, TBD = discovery required. Verification: T=test, I=inspection, A=analysis, D=demonstration.

## 2. Product boundary
Software includes an accessible user interface, session/settings management, capture orchestration, AI service integration, result presentation, optional device connectivity, diagnostics, and privacy controls.

## 3. User classes
Blind users; low-vision users; optional trusted supporters only when explicitly authorized; and maintainers with least-privilege diagnostic access.

## 4. Functional requirements
| ID | Requirement | Priority | Verification |
|---|---|---:|---|
| FR-001 | Provide an accessible introduction explaining capabilities, limitations, permissions, and safety boundaries. | P0 | I,D |
| FR-002 | Allow the user to initiate, cancel, and repeat an assistance request. | P0 | T |
| FR-003 | Provide spoken feedback for supported primary workflows. | P0 | T |
| FR-004 | Allow the user to interrupt or stop spoken feedback. | P0 | T |
| FR-005 | Allow selection of explicitly supported assistance tasks. | P0 | T |
| FR-006 | Communicate when camera, microphone, network, or device permissions/connectivity are unavailable. | P0 | T |
| FR-007 | Request camera/microphone permission only when needed and explain its purpose. | P0 | I,T |
| FR-008 | Present image-description output as an estimate and avoid unsupported certainty. | P1 | T,I |
| FR-009 | Present recognized text through speech and allow replay. | P1 | T |
| FR-010 | Allow speech rate and verbosity adjustment where platform support permits. | P1 | T |
| FR-011 | Expose connected-device status, including disconnected/unavailable states. | P1 | T |
| FR-012 | Provide an accessible failure message and recovery action after inference or connectivity failure. | P0 | T |
| FR-013 | Let the user control whether optional history is saved. | P0 | T,I |
| FR-014 | Provide a documented workflow for deletion of locally retained user content. | P1 | T |
| FR-015 | Do not initiate continuous capture by default. | P0 | T,I |
| FR-016 | Distinguish informational assistance from emergency or safety-critical guidance. | P0 | I,T |
| FR-017 | Identify offline status and reduced capabilities where offline mode exists. | P2 | T |
| FR-018 | Provide an accessible, privacy-conscious way to report incorrect or harmful results. | P2 | D,I |

## 5. Non-functional requirements
| ID | Requirement | Priority | Verification |
|---|---|---:|---|
| NFR-001 | Core workflows shall be operable without sight using supported screen-reader/audio interaction. | P0 | T |
| NFR-002 | Controls shall have semantic labels, predictable focus order, and meaningful names. | P0 | I,T |
| NFR-003 | Processing, waiting, success, and failure states shall be announced accessibly. | P0 | T |
| NFR-004 | End-to-end latency shall be measured per task; thresholds set after baseline studies. | P0 | A,T |
| NFR-005 | Network communication shall use current secure transport mechanisms. | P0 | I,T |
| NFR-006 | Sensitive stored data shall be minimized and protected by platform-appropriate controls. | P0 | I,T |
| NFR-007 | Logs shall exclude raw images, audio, credentials, and unnecessary personal data by default. | P0 | I,T |
| NFR-008 | Recover gracefully from permission denial, process termination, network loss, and disconnection. | P0 | T |
| NFR-009 | Supported devices, OS versions, languages, and accessibility technologies shall be documented. | P1 | I,T |
| NFR-010 | AI shall be evaluated by task and scenario; aggregate accuracy alone is insufficient. | P0 | A |
| NFR-011 | Controls shall be usable with assistive technology and without time-critical visual interaction. | P0 | T |
| NFR-012 | Provide non-sensitive diagnostics sufficient to investigate failures. | P1 | I,T |

## 6. Safety constraints
The software shall not claim to replace a white cane, guide dog, mobility training, or human support. Initial scope excludes autonomous street-crossing decisions and guaranteed obstacle avoidance. It shall disclose unavailable, stale, or low-quality input and never present model output as a safety guarantee.

## 7. Data requirements
For each data category document purpose, source, processing location, retention, access roles, and deletion behavior. Training data requires documented provenance and usage rights. Operational recordings must not be repurposed for training without separate informed authorization.

## 8. Acceptance and open questions
Every approved requirement must trace to a need, architecture component, test case, and result. Open questions include target platforms, first use cases, language/dialect support, latency thresholds, offline needs, account/history expectations, device pairing, and applicable legal requirements.
