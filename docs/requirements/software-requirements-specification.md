# Software Requirements Specification

| Attribute | Value |
|---|---|
| Document ID | SRS-001 |
| Version | 1.2 |
| Status | Refined candidate baseline — stakeholder validation pending |
| Related | PID-001, SYS-ARCH-001, ADR-REG-001, SAF-001, ACC-001, SEC-001, HW-001, VVP-001, RTM-001, MVP-001, UC-001, ICD-MVP-001, VTP-MVP-001 |

## 1. Purpose and status

This specification defines candidate software requirements for the AI Guardian for Blind People. It supports scope control, architecture, implementation planning, and verification. It does not claim that any feature has been implemented, tested, or validated with users.

Requirements in this version are **Proposed** until reviewed and approved by the project owner and, where appropriate, representative users and safety/privacy reviewers.

### 1.1 Requirement conventions

- **Priority:** P0 = essential safety/accessibility foundation; P1 = candidate initial capability; P2 = later/optional capability; TBD = priority requires discovery.
- **Source:** UN = user need to be validated; SAF = safety constraint; PRIV = privacy/security constraint; ACC = accessibility constraint; ARCH = architecture/platform constraint; OPS = operations/maintenance need.
- **Verification:** T = test; I = inspection; A = analysis; D = demonstration. Multiple methods may apply.
- **Requirement status:** Proposed, Under Review, Approved, Implemented, Verified, Failed, Blocked, Deferred, Retired. Implemented is not equivalent to Verified.
- **Acceptance criteria:** Each criterion defines observable evidence. Where a numeric threshold depends on research or benchmarking, the criterion requires an approved threshold to be established before release; no unsupported numeric target is assumed.

A requirement shall use one unique ID, one testable obligation, and one controlled status. Changes shall be recorded through GOV-001.

## 2. Product boundary

The software system includes the accessible client, session/task orchestration, user-authorized capture, AI capability integration, result interpretation and speech presentation, settings, privacy/data controls, diagnostics, and optional connected-device integration.

The product is supplementary informational assistance. It is not a replacement for a white cane, guide dog, orientation and mobility training, or human assistance. The initial concept excludes autonomous street-crossing decisions, guaranteed obstacle avoidance, and claims of certified mobility assistance.

## 3. User classes and operating assumptions

- Blind users who primarily interact through speech, audio, and compatible assistive technology.
- Low-vision users who may additionally use visual presentation, magnification, and contrast settings.
- A trusted supporter only where the user explicitly authorizes a defined action or access.
- Maintainers/evaluators with least-privilege access to non-sensitive diagnostics.

Target operating systems, minimum device specifications, supported languages/dialects, and supported assistive technologies remain **TBD** and require a documented platform feasibility and user-needs decision before implementation scope is frozen.

## 4. Functional requirements

All requirements below have status **Proposed**. Test IDs are planned identifiers, not evidence of executed tests.

| ID | Requirement (shall statement) | Priority | Source | Verification | Acceptance criterion | Planned test |
|---|---|---:|---|---|---|---|
| FR-001 | The software shall provide an accessible first-use explanation of supported capabilities, limitations, permissions, and safety boundaries. | P0 | ACC, SAF, UN | I,D | A first-time user can reach and replay the explanation without sight; review confirms all four topics are covered. | TC-FR-001 |
| FR-002 | The software shall allow the user to select only assistance tasks identified as supported in the current release. | P0 | UN, SAF | T | Every displayed task maps to an approved capability; unsupported tasks cannot be started. | TC-FR-002 |
| FR-003 | The software shall allow the user to initiate an assistance session through an accessible control. Additional initiation modes, including voice interaction, shall be included only when separately scoped, validated, and approved for a release. | P0 | UN, ACC | T,D | MVP-1 initiation through an accessible control starts one identifiable session and announces its state; no voice-command initiation is assumed in MVP-1. Any later initiation mode has its own approved scope and verification. | TC-FR-003 |
| FR-004 | The software shall allow the user to cancel an active capture or assistance request. | P0 | SAF, UN | T | Cancellation stops further capture/processing where technically possible, announces cancellation, and does not present a late result as current. | TC-FR-004 |
| FR-005 | The software shall allow the user to interrupt and stop spoken output. | P0 | ACC, UN | T | A user action stops current speech within the approved interaction threshold; the control remains available during playback. | TC-FR-005 |
| FR-006 | The software shall provide accessible progress, completion, and failure status for each assistance session. | P0 | ACC, UN | T | Screen-reader/audio checks confirm each state is announced once in a distinguishable and understandable form. | TC-FR-006 |
| FR-007 | The software shall request camera, microphone, and other sensitive permissions only when a selected workflow requires them. | P0 | PRIV, SAF | I,T | Permission prompts occur only for the relevant workflow; denial does not trigger repeated unauthorized capture attempts. | TC-FR-007 |
| FR-008 | The software shall explain the purpose of each sensitive permission request before or at the point of request. | P0 | PRIV, ACC | I,T | Each permission prompt has an accessible purpose statement and a clear deny/cancel path. | TC-FR-008 |
| FR-009 | The software shall capture input only after an explicit user action for the active request, except for a separately approved and clearly indicated feature. | P0 | PRIV, SAF | T,I | Tests show no default continuous capture; capture begins only after the required user action and visible/audible indication. | TC-FR-009 |
| FR-010 | The software shall provide text recognition only when OCR is an approved capability in the selected release. | P1 | UN | T | For an approved test corpus, the system returns recognized text or an explicit failure/uncertainty state; it does not silently invent missing text. | TC-FR-010 |
| FR-011 | The software shall present recognized text through supported accessible output and allow replay. | P1 | UN, ACC | T | A user can hear the recognized text, interrupt it, and replay it without recapturing the source. | TC-FR-011 |
| FR-012 | The software shall provide object-recognition output only for object classes and conditions documented as supported. | P1 | UN, SAF | T,A | Evaluation reports per-class results and known limitations; unsupported or uncertain cases are communicated as uncertain rather than asserted as fact. | TC-FR-012 |
| FR-013 | The software shall provide scene-description output only within a documented task scope and shall avoid unsupported safety conclusions. | P1 | UN, SAF | T,I | Scenario review confirms descriptions are bounded, uncertainty is communicated, and no output claims a route is safe or an obstacle is absent with certainty. | TC-FR-013 |
| FR-014 | The software shall accept speech input only through an explicitly enabled and documented interaction mode. | P1 | UN, PRIV | T,I | Microphone activation follows the permission and activation model; the user can stop listening. | TC-FR-014 |
| FR-015 | The software shall allow supported speech-output preferences, including speech rate or verbosity, where the selected platform provides them. | P1 | ACC, UN | T | Each exposed preference changes output as described and remains operable using supported assistive technology. | TC-FR-015 |
| FR-016 | The software shall identify unavailable camera, microphone, model service, network, or connected-device dependencies when they prevent a requested task. | P0 | SAF, OPS | T | Fault injection for each dependency produces a specific accessible status and does not fabricate a successful result. | TC-FR-016 |
| FR-017 | The software shall provide a recovery action appropriate to a recoverable failure, such as retry, change permission, reconnect, or cancel. | P0 | UN, SAF | T,D | Each defined recoverable failure offers only valid recovery actions; retry does not duplicate an active request. | TC-FR-017 |
| FR-018 | The software shall identify results that are stale, incomplete, malformed, or associated with a different session before presenting them as current. | P0 | SAF, ARCH | T | Injected stale/malformed responses are rejected or explicitly labelled; no stale result is presented as a fresh observation. | TC-FR-018 |
| FR-019 | The software shall communicate uncertainty or input-quality limitations when the AI service cannot provide a sufficiently reliable result. | P0 | SAF | T,I | Approved challenge cases produce an uncertainty/failure response rather than an unqualified assertion. | TC-FR-019 |
| FR-020 | The software shall distinguish informational assistance from emergency, medical, or safety-critical guidance. | P0 | SAF | I,T | Content review and scenario tests find no claim that the system provides emergency response or certified mobility guidance. | TC-FR-020 |
| FR-021 | The software shall expose connected-device connection state when optional hardware integration is enabled. | P1 | ARCH, UN | T | Connected, disconnected, pairing, and unavailable states are distinguishable through accessible feedback. | TC-FR-021 |
| FR-022 | The software shall provide a user-controlled option for saving or not saving optional session history. | P0 | PRIV, UN | T,I | With history disabled, the application does not retain optional session content beyond transient processing required for the request. | TC-FR-022 |
| FR-023 | The software shall provide a documented and accessible process to delete locally retained user content under its control. | P1 | PRIV, ACC | T,D | A deletion test confirms the selected content is removed from the defined local stores, with any unavoidable limits explained. | TC-FR-023 |
| FR-024 | The software shall provide a privacy-conscious mechanism to report an incorrect or harmful result where feedback collection is enabled. | P2 | UN, PRIV | T,I | Reporting is optional, accessible, explains what will be submitted, and does not attach raw media without separate informed consent. | TC-FR-024 |
| FR-025 | The software shall identify offline or degraded-connectivity state and disclose which functions are unavailable or reduced. | P2 | OPS, UN | T | Network-loss tests produce an accurate status and prevent unavailable remote tasks from appearing successful. | TC-FR-025 |
| FR-026 | The software shall not expose supporter access unless the user has explicitly authorized the relevant scope. | P1 | PRIV | T,I | Unauthorized supporter attempts are denied; authorized scope is limited to the permission granted and can be revoked. | TC-FR-026 |
| FR-027 | The software shall provide a user-accessible way to review the current privacy and capture state. | P1 | PRIV, ACC | T,D | A user can determine whether a capture workflow is active and whether optional history is enabled without sight. | TC-FR-027 |
| FR-028 | The software shall record non-sensitive diagnostic events sufficient to identify session failures without recording raw media or credentials by default. | P0 | OPS, PRIV | I,T | Log inspection confirms defined event codes and excludes raw images, raw audio, credentials, and unnecessary personal data. | TC-FR-028 |

## 5. Non-functional requirements

All requirements below have status **Proposed**. Quantitative thresholds marked TBD must be established through user research, platform benchmarking, risk analysis, and formal approval before release; they shall not be guessed.

| ID | Requirement (shall statement) | Priority | Source | Verification | Acceptance criterion | Planned test |
|---|---|---:|---|---|---|---|
| NFR-001 | Core in-scope workflows shall be operable without sight using the supported screen reader and/or audio interaction. | P0 | ACC | T,D | Every approved critical workflow passes the agreed blind-user accessibility test protocol on each supported platform. | TC-NFR-001 |
| NFR-002 | Interactive controls shall expose meaningful accessible names, roles, states, and predictable focus order. | P0 | ACC | I,T | Automated and manual accessibility inspection finds no unresolved critical control-label or focus-order defect in release workflows. | TC-NFR-002 |
| NFR-003 | Progress, success, warning, and failure states shall be announced without requiring visual attention. | P0 | ACC, SAF | T | Each state is announced and distinguishable in the supported assistive-technology test matrix. | TC-NFR-003 |
| NFR-004 | End-to-end response latency shall be measured separately for each supported task and operating condition. | P0 | UN, ARCH | A,T | A benchmark report records median and tail latency by task/device/network; release thresholds are approved before release. | TC-NFR-004 |
| NFR-005 | Network communications shall use currently supported secure transport and authenticated service endpoints where applicable. | P0 | PRIV | I,T | Security review confirms approved transport configuration and rejects invalid/untrusted endpoint configurations. | TC-NFR-005 |
| NFR-006 | Stored sensitive data shall be minimized and protected using platform-appropriate access controls and encryption capabilities. | P0 | PRIV | I,T | Data-flow and storage inspection verifies approved data inventory, access restrictions, and protection controls. | TC-NFR-006 |
| NFR-007 | Diagnostic logs shall exclude raw images, raw audio, credentials, and unnecessary personal data by default. | P0 | PRIV | I,T | Representative logs contain no prohibited data under normal and failure scenarios. | TC-NFR-007 |
| NFR-008 | The software shall recover safely from permission denial, process interruption, network loss, and device disconnection. | P0 | SAF, OPS | T | Each failure scenario returns to a known state, communicates the condition, and does not present an invalid result. | TC-NFR-008 |
| NFR-009 | Supported devices, OS versions, languages, dialects, and assistive technologies shall be explicitly documented for each release. | P1 | ARCH, ACC | I | Release documentation contains a tested compatibility matrix; untested combinations are not represented as supported. | TC-NFR-009 |
| NFR-010 | AI capabilities shall be evaluated per task, class, and relevant operating scenario; aggregate accuracy alone shall not establish release suitability. | P0 | SAF, ARCH | A | Evaluation report includes task-specific metrics, failure analysis, uncertainty behavior, and documented release criteria. | TC-NFR-010 |
| NFR-011 | User workflows shall not require time-critical visual interaction for core operation. | P0 | ACC, SAF | T,D | Usability evaluation completes all approved core tasks using non-visual interaction; any visual-only dependency blocks approval. | TC-NFR-011 |
| NFR-012 | Diagnostics shall use stable, documented error categories and avoid disclosure of sensitive content. | P1 | OPS, PRIV | I,T | Defined failure scenarios map to documented error categories and the diagnostic output passes privacy inspection. | TC-NFR-012 |
| NFR-013 | Battery, memory, thermal behavior, and compute use shall be measured on each proposed supported device configuration. | P1 | ARCH, OPS | A,T | A reproducible benchmark report records operating conditions and measured values; acceptance limits are approved before release. | TC-NFR-013 |
| NFR-014 | The system shall maintain clear separation between user-facing AI output and verified system/device status. | P0 | SAF, ARCH | T,I | Tests confirm model-generated text cannot overwrite trusted permission, connection, capture, or error state indicators. | TC-NFR-014 |

## 6. Hardware boundary and allocation

Physical device requirements are controlled in **HW-001**, not duplicated as software requirements. Software-to-device interfaces and responsibilities are controlled in **ICD-001**. The RTM shall link software requirements to relevant hardware requirements where applicable. A software feature that depends on unselected hardware remains conditional and shall not be represented as available.

## 7. Safety constraints

1. The product shall not claim to replace a white cane, guide dog, mobility training, or human assistance.
2. Initial scope excludes autonomous street-crossing decisions and guaranteed obstacle avoidance.
3. AI output shall not be presented as a safety guarantee or as proof that a path is clear.
4. The system shall communicate unavailable, stale, incomplete, or uncertain input/results.
5. Users shall retain control over capture, cancellation, and spoken output.
6. Prototype evaluation shall be controlled and consented; participants shall not rely on the prototype for navigation.
7. Safety controls and residual risks are governed by SAF-001 and verified through VVP-001.

## 8. Data and privacy requirements

For every data category, the design shall document purpose, source, collection trigger, processing location, recipients, retention, access roles, deletion behavior, and legal/consent basis. Training datasets shall have documented provenance and usage rights. Operational recordings shall not be repurposed for model training without separate, informed, specific authorization. Third-party AI processing shall be disclosed and assessed before use.

## 9. Requirement approval and change control

A requirement may move to **Approved** only when its source/need, scope, acceptance criterion, verification method, safety/privacy implications, and architecture allocation have been reviewed. A requirement may move to **Implemented** only with implementation evidence, and to **Verified** only after its planned verification passes against a recorded build/configuration. Failed, blocked, deferred, and retired requirements remain visible in RTM-001.

## 10. Open decisions and release gates

The following are unresolved and shall be decided using evidence rather than assumption:

- First-release use cases and explicit exclusions.
- Target mobile platform(s), supported OS versions, and minimum device capability.
- Supported languages, dialects, speech engines, and accessibility technologies.
- OCR, object-recognition, and scene-description model/service selection and task-specific quality thresholds.
- Latency, battery, thermal, memory, and offline acceptance thresholds.
- Account, history, cloud processing, retention, and deletion policy.
- Device form factor, sensors, connectivity, pairing protocol, and hardware allocation.
- Applicable legal, regulatory, and data-protection obligations.

No release scope is approved by this document alone. The project owner and relevant reviewers must approve the baseline after user-needs validation, risk review, and feasibility evidence.

## 11. Version history

| Version | Date | Change |
|---|---|---|
| 1.0 | Initial | Initial candidate functional and non-functional requirements. |
| 1.1 | 2026-11-06 | Added requirement sources, status lifecycle, objective acceptance criteria, planned test IDs, explicit hardware allocation, and release gates; clarified candidate scope and unresolved thresholds. |
| 1.2 | 2026-11-06 | Clarified MVP-1 session initiation as accessible-control based; future voice-command initiation requires separate scope approval and verification. |
