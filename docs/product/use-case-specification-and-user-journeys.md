# Use Case Specification and User Journeys

| Attribute | Value |
|---|---|
| Project | AI Guardian for Blind People |
| Document ID | UC-001 |
| Version | 0.1 |
| Status | Proposed — stakeholder validation pending |
| Document Type | Use Case Specification |
| Related | PID-001, PMP-001, MVP-001, SRS-001, RTM-001, SYS-ARCH-001, ICD-001, SAF-001, SEC-001, ACC-001, DATA-001, VVP-001 |
| Prepared | 06 November 2026 |

## 1. Purpose and Scope

This document defines the actors, user journeys, use cases, alternative flows, and traceability for the proposed MVP-1 text-reading workflow described in MVP-001.

The use cases are planning artifacts. They do not establish that a workflow has been validated with blind or low-vision users, implemented, or verified. All use cases remain proposed until reviewed with intended users and the project owner.

### 1.1 MVP-1 system boundary

The MVP-1 system is a smartphone application that supports a user-initiated still-image text-reading task. The application manages accessible interaction, camera permission and capture, OCR invocation, speech output, cancellation, session state, and privacy behavior.

The following are outside this use-case boundary: object recognition, open-ended scene description, continuous video/audio capture, custom wearable hardware, remote supporter access, cloud history, autonomous navigation, obstacle avoidance, and road-crossing decisions.

## 2. Actors and External Systems

| Actor ID | Actor | Role | Interaction |
|---|---|---|---|
| ACT-001 | Blind or low-vision user | Primary actor | Starts, controls, cancels, and completes a text-reading task using accessible interaction |
| ACT-002 | Smartphone operating system | Supporting system | Mediates camera permission, camera lifecycle, accessibility services, and speech services |
| ACT-003 | OCR engine/adapter | Supporting system | Receives a user-authorized image and returns recognized text with processing status and available quality metadata |
| ACT-004 | Device text-to-speech service | Supporting system | Speaks recognized text and supports stop/replay behavior |
| ACT-005 | Screen reader/accessibility service | Supporting system | Exposes controls, labels, focus, and status announcements to non-visual interaction |
| ACT-006 | Project evaluator/tester | Evaluation actor | Executes approved tests in a controlled environment; does not represent a normal product user |

No supporter, caregiver, remote operator, or administrator actor is included in MVP-1.

## 3. Preconditions and Global Rules

### 3.1 General preconditions
- The application is installed on a device configuration included in the feasibility test.
- The user can access the application through the device's supported accessibility services.
- Camera hardware and the selected OCR and speech services are available, unless the use case explicitly tests their unavailability.
- The user has been given accessible information about the prototype's capabilities, limitations, permissions, and non-mobility-aid status.

### 3.2 Global rules
- Camera capture is user-initiated for each reading request.
- No continuous capture or background recording is permitted in MVP-1.
- The application must not describe OCR output as guaranteed correct.
- Unreadable, unsupported, incomplete, or low-quality input must result in an explicit status rather than fabricated text.
- User cancellation and speech interruption must be available through accessible controls.
- A result from an old or cancelled session must never be presented as the current session's result.
- Temporary image data must be handled according to SEC-001 and DATA-001; the proposed default is no persistent image retention.
- The application is supplementary information access and must not provide mobility-safety decisions.

## 4. Primary User Journey

| Journey step | User goal/action | System response | Expected state |
|---|---|---|---|
| J-01 | Open the application | Announces application identity and accessible entry point | Ready |
| J-02 | Select “Read text” | Announces task and explains camera need if required | Task selected |
| J-03 | Review/resolve camera permission | Explains purpose and offers the OS permission flow | Permission granted or denied |
| J-04 | Request a capture | Announces capture readiness and waits for explicit user action | Capture ready |
| J-05 | Activate capture | Captures one still image and announces processing | Processing |
| J-06 | Wait for OCR | Announces completion, no-text, uncertainty, or failure status | Result available or recoverable failure |
| J-07 | Listen to recognized text | Speaks returned text through the device speech service | Speaking |
| J-08 | Stop, replay, retry, or finish | Performs the selected action and announces the resulting state | Controlled active session or completed |
| J-09 | End the task | Clears transient state and applies media-retention policy | Closed |

Exact wording, gestures, focus order, voice commands, language, and timing require accessibility and user research. Voice command input is not assumed to be enabled in MVP-1.

## 5. Use Case Catalogue

| Use case ID | Name | Primary actor | Priority | MVP status |
|---|---|---|---|---|
| UC-001 | Understand first-use information and enter text-reading task | User | P0 | In scope |
| UC-002 | Grant or deny camera permission | User | P0 | In scope |
| UC-003 | Capture a still image for text reading | User | P0 | In scope |
| UC-004 | Process image and listen to recognized text | User | P1 | In scope |
| UC-005 | Stop or replay spoken text | User | P0 | In scope |
| UC-006 | Cancel an active reading session | User | P0 | In scope |
| UC-007 | Recover from capture or OCR failure | User | P0 | In scope |
| UC-008 | Review capture/privacy state and finish session | User | P0 | In scope |
| UC-009 | Configure supported speech preferences | User | P1 | In scope where platform supports |
| UC-010 | Use object recognition or scene description | User | Deferred | Out of MVP-1 |

## 6. Detailed Use Cases

### UC-001 — Understand First-use Information and Enter Text-reading Task

**Goal:** The user understands what the prototype can and cannot do and can reach the supported text-reading task without sight.

**Trigger:** User opens the application for the first time or requests the introductory information.

**Preconditions:** Application is installed; accessibility service may be enabled.

**Main flow:**
1. Application presents an accessible welcome and first-use explanation.
2. Explanation covers supported text reading, limitations of OCR, camera permission, capture control, privacy behavior, and safety boundaries.
3. User can replay or navigate the explanation.
4. Application exposes the supported “Read text” task.
5. User selects the task.
6. Application announces the selected task and next required action.

**Alternative/exception flows:**
- A1: User skips optional explanatory detail. The essential safety, privacy, and permission information remains accessible before first capture.
- A2: Accessibility service is unavailable or controls are not exposed accessibly. Application provides a clear status and does not claim the workflow is accessible on that configuration.
- A3: User selects an unsupported feature. Application explains that the feature is not available in this prototype and does not start it.

**Postconditions:** Text-reading task is selected, or the user exits without starting capture.

**Related requirements:** MVP-F-001; SRS FR-001, FR-002, FR-006, FR-020; NFR-001, NFR-002, NFR-003, NFR-011.

### UC-002 — Grant or Deny Camera Permission

**Goal:** The user makes an informed choice about camera access.

**Trigger:** User starts a text-reading task that requires camera access.

**Preconditions:** UC-001 completed; camera permission has not yet been granted or must be requested again.

**Main flow:**
1. Application explains why camera access is needed.
2. User activates the permission action.
3. Operating system presents its permission interface.
4. User grants permission.
5. Application confirms camera readiness accessibly.

**Alternative/exception flows:**
- A1: User denies permission. Application announces that capture cannot proceed and offers a route to retry or open relevant system settings where supported.
- A2: Permission is permanently denied or restricted. Application explains the limitation without repeatedly prompting.
- A3: Camera is unavailable or occupied. Application announces the dependency failure and offers a valid retry or exit action.
- A4: Permission state changes while the application is backgrounded. Application rechecks the state before capture and does not assume prior authorization remains valid.

**Postconditions:** Permission state is accurately represented; no capture occurs merely because permission was granted.

**Related requirements:** MVP-F-002, MVP-F-007; SRS FR-007, FR-008, FR-016, FR-017, FR-027; NFR-008.

### UC-003 — Capture a Still Image for Text Reading

**Goal:** The user explicitly captures one still image for the current reading session.

**Trigger:** User activates the capture action.

**Preconditions:** Text-reading task is active; camera permission is granted; camera is available.

**Main flow:**
1. Application announces that it is ready to capture.
2. User explicitly activates capture.
3. Application starts a single still-image capture operation.
4. Application communicates that capture/processing is underway.
5. Capture adapter returns the image or a capture failure.
6. On success, the application associates the image with the active session and passes it to the OCR adapter.
7. Application does not initiate another capture unless the user requests retry.

**Alternative/exception flows:**
- A1: User cancels before capture begins. No image is captured.
- A2: User cancels while capture is in progress. The application cancels where technically possible, invalidates the session result, and reports cancellation.
- A3: Camera fails or returns no usable image. Application reports the failure and offers retry or exit.
- A4: Image is blank, blurred, rotated, too dark, or otherwise unsuitable. If the system can identify the quality problem, it explains the limitation; otherwise OCR outcome is handled by UC-007.
- A5: Application is interrupted or backgrounded. On resume it revalidates session and permission state; it must not silently resume capture.

**Postconditions:** A single image is either associated with the active session for OCR or discarded after failure/cancellation according to the approved transient-data policy.

**Related requirements:** MVP-F-003, MVP-F-008, MVP-F-009; SRS FR-004, FR-009, FR-016, FR-018, FR-027; NFR-008, NFR-014.

### UC-004 — Process Image and Listen to Recognized Text

**Goal:** The user receives spoken OCR output from the image captured in the current session.

**Trigger:** A valid capture is handed to the OCR adapter.

**Preconditions:** UC-003 succeeded; OCR engine is available; session remains active.

**Main flow:**
1. Application submits the captured image to the OCR adapter.
2. OCR adapter processes the image and returns recognized text, processing status, and available quality/uncertainty metadata.
3. Application verifies that the response belongs to the active session and is structurally valid.
4. Application interprets empty, partial, unsupported, or uncertain results without inventing text.
5. If usable text is returned, application announces that text is available.
6. Application sends the recognized text to the speech output adapter.
7. Speech service reads the text.
8. Application remains responsive to stop, replay, retry, and finish actions.

**Alternative/exception flows:**
- A1: No text detected. Application announces that no readable text was found and offers retry or finish.
- A2: Partial or uncertain text detected. Application announces the limitation before reading available text; it does not imply completeness.
- A3: OCR engine unavailable or processing fails. Application announces the failure and offers a valid recovery path.
- A4: OCR returns malformed or empty data. Application rejects it as a successful result and reports an error.
- A5: A late result arrives after cancellation or a newer session starts. Application rejects it and does not speak it.
- A6: Speech service unavailable or requested voice unsupported. Application announces the limitation and provides any available accessible fallback; it must not silently claim successful speech output.

**Postconditions:** Valid text is spoken, or a clear failure/uncertainty state is presented. Temporary image data is disposed of according to the approved policy.

**Related requirements:** MVP-F-004, MVP-F-005, MVP-F-007, MVP-F-008, MVP-F-009; SRS FR-010, FR-011, FR-016, FR-018, FR-019, FR-020; NFR-004, NFR-008, NFR-010, NFR-014.

### UC-005 — Stop or Replay Spoken Text

**Goal:** The user controls spoken output without needing to recapture the image.

**Trigger:** Speech is playing or has completed.

**Preconditions:** Recognized text is available in the current session.

**Main flow — Stop:**
1. User activates the stop-speech control.
2. Application sends a stop command to the speech service.
3. Application confirms speech has stopped.
4. Recognized text remains available for replay during the current session, subject to the session data policy.

**Main flow — Replay:**
1. User activates replay.
2. Application verifies that the current session still has replayable text.
3. Speech service reads the same recognized text again.
4. User can stop playback at any time.

**Alternative/exception flows:**
- A1: Stop is requested after speech has already ended. Application remains stable and reports or maintains the stopped/completed state.
- A2: Replay is requested when no result is available. Application announces that there is no text to replay.
- A3: A new session has replaced the old one. The previous result is not replayed as if it belonged to the new session.

**Postconditions:** Speech is stopped or replayed as requested; session identity remains correct.

**Related requirements:** MVP-F-006; SRS FR-005, FR-011, FR-015; NFR-001, NFR-003, NFR-011.

### UC-006 — Cancel an Active Reading Session

**Goal:** The user can stop the current task and prevent late results from being presented.

**Trigger:** User activates cancel/end while capture or OCR processing is active.

**Preconditions:** A reading session is active.

**Main flow:**
1. User activates cancel.
2. Application marks the session as cancelled immediately.
3. Application requests cancellation of pending capture/OCR work where supported.
4. Application stops speech if active.
5. Application invalidates pending results associated with the cancelled session.
6. Application disposes of transient image/result data according to the approved policy.
7. Application announces cancellation and returns to a known ready state.

**Alternative/exception flows:**
- A1: Underlying OCR operation cannot be interrupted. Its eventual response is discarded and must not be spoken.
- A2: Application process is interrupted during cancellation. On restart/resume, no previous request may be represented as active without explicit recovery and state validation.
- A3: Speech stop operation fails. Application reports the failure and uses the safest supported platform recovery; it must not claim that speech stopped if it did not.

**Postconditions:** Session is cancelled or explicitly marked as cancellation-incomplete if the platform cannot confirm termination; no late result is presented as current.

**Related requirements:** MVP-F-006, MVP-F-008, MVP-F-009; SRS FR-004, FR-005, FR-018; NFR-008, NFR-014.

### UC-007 — Recover from Capture or OCR Failure

**Goal:** The user understands why text reading failed and can choose a valid recovery action.

**Trigger:** Camera capture, image validation, OCR, or speech dependency returns a failure or unusable result.

**Preconditions:** A text-reading task is active or has just failed.

**Main flow:**
1. Application identifies the failure category from trusted component/system status.
2. Application announces a concise, accessible explanation.
3. Application offers only recovery actions valid for that failure.
4. User chooses retry, resolve permission/dependency, or finish.
5. On retry, application creates a fresh request/session correlation and requires a new explicit capture.
6. Application reports the new request status.

**Alternative/exception flows:**
- A1: User chooses finish. Session closes and transient data is disposed of.
- A2: Required dependency remains unavailable. Application does not enter an endless retry loop; it communicates that the task cannot proceed.
- A3: Failure category is unknown. Application reports a general failure without inventing a cause and provides safe exit/retry where appropriate.
- A4: Network loss occurs. MVP-1 should not require network for the intended local workflow; if a selected OCR implementation does require network, that dependency must be disclosed and its offline failure behavior tested before inclusion.

**Postconditions:** User receives a truthful status and either a fresh retry path or a closed session.

**Related requirements:** MVP-F-007, MVP-F-008; SRS FR-006, FR-016, FR-017, FR-019, FR-025; NFR-008, NFR-012.

### UC-008 — Review Capture/Privacy State and Finish Session

**Goal:** The user can determine the task state, end the session, and rely on the documented media lifecycle.

**Trigger:** User requests status or chooses finish.

**Preconditions:** Application is open; a session may or may not be active.

**Main flow:**
1. User requests current status or activates finish.
2. Application announces whether a reading session is active, processing, speaking, or idle.
3. Application announces relevant capture/privacy state in an understandable way.
4. User confirms finish if required by the accessible interaction design.
5. Application stops speech and invalidates outstanding session work.
6. Application disposes of transient image data and closes the session.
7. Application returns to the accessible task entry state.

**Alternative/exception flows:**
- A1: User requests status while idle. Application announces that no capture/reading session is active.
- A2: User finishes while OCR is pending. Behavior follows UC-006.
- A3: Persistent history is not part of MVP-1. Application must not imply that a prior result has been saved or can be recovered after session closure.

**Postconditions:** Session is closed, capture is inactive, and transient data lifecycle actions have been applied.

**Related requirements:** MVP-F-008, MVP-F-009; SRS FR-004, FR-022, FR-027, FR-028; NFR-006, NFR-007, NFR-008.

### UC-009 — Configure Supported Speech Preferences

**Goal:** The user adjusts speech settings exposed by the selected platform.

**Trigger:** User opens application settings.

**Preconditions:** Application settings are available.

**Main flow:**
1. User opens speech preferences.
2. Application announces available settings, such as speech rate or verbosity, only where supported.
3. User changes a preference.
4. Application applies the setting and announces the result.
5. Preference is stored only as necessary and in accordance with the approved local data policy.

**Alternative/exception flows:**
- A1: Platform does not expose a requested preference. Application does not display a non-functional control.
- A2: Preference cannot be saved. Application reports that it could not persist the setting and uses a documented fallback.

**Postconditions:** Supported preference is applied for the current or subsequent session according to platform capability.

**Related requirements:** MVP-F-010; SRS FR-015; NFR-001, NFR-002.

## 7. Key State Model

| State | Meaning | Permitted next states |
|---|---|---|
| READY | No active reading operation | TASK_SELECTED |
| TASK_SELECTED | Text-reading task selected | PERMISSION_PENDING, CAPTURE_READY, CLOSED |
| PERMISSION_PENDING | OS permission decision pending | CAPTURE_READY, BLOCKED, CLOSED |
| CAPTURE_READY | User may explicitly capture | CAPTURING, CLOSED |
| CAPTURING | Still-image capture in progress | PROCESSING, RECOVERABLE_FAILURE, CANCELLING |
| PROCESSING | OCR operation active | RESULT_READY, RECOVERABLE_FAILURE, CANCELLING |
| RESULT_READY | Valid/partial recognized text is available | SPEAKING, CAPTURE_READY, CLOSED |
| SPEAKING | Speech output active | RESULT_READY, CANCELLING, CLOSED |
| RECOVERABLE_FAILURE | A failure has been identified and explained | CAPTURE_READY, BLOCKED, CLOSED |
| BLOCKED | Required capability unavailable | CAPTURE_READY after resolution, CLOSED |
| CANCELLING | Cancellation and cleanup in progress | READY, CLOSED |
| CLOSED | Session ended; transient state cleared | READY |

State transition rules:
- A cancelled or superseded session cannot transition to RESULT_READY or SPEAKING.
- A new capture requires an explicit user action.
- A retry creates a new request identity; it does not silently reuse a stale result.
- The application must distinguish its own trusted state from OCR-generated content.
- State names are logical design labels; final implementation representation is not prescribed here.

## 8. Failure and Recovery Catalogue

| Failure ID | Scenario | Required user communication | Allowed recovery |
|---|---|---|---|
| FAIL-001 | Camera permission denied | Explain camera access is needed for this task | Retry permission or finish |
| FAIL-002 | Camera unavailable/in use | Explain capture is unavailable | Retry later or finish |
| FAIL-003 | Capture returns no usable image | Explain image capture failed | New explicit capture or finish |
| FAIL-004 | Image unreadable/poor quality | Explain no reliable text could be extracted | Reposition/retry capture or finish |
| FAIL-005 | OCR service unavailable | Explain text recognition is temporarily unavailable | Retry when available or finish |
| FAIL-006 | No text detected | Explain no readable text was found | Retry with another image or finish |
| FAIL-007 | Partial/uncertain OCR result | Explain result may be incomplete/uncertain | Listen to available text, retry, or finish |
| FAIL-008 | Malformed/stale OCR response | Do not read it as a valid current result | Discard and report processing error |
| FAIL-009 | Speech output unavailable | Explain spoken output cannot be started | Use supported accessible fallback or finish |
| FAIL-010 | App interrupted/backgrounded | Explain current state after revalidation | Resume only if safe and session remains valid; otherwise restart |
| FAIL-011 | Cancellation cannot stop underlying work | Explain cancellation status accurately | Discard late result; return to known state |
| FAIL-012 | Local storage/cleanup failure | Explain cleanup could not be confirmed where user action is needed | Apply documented retry/exit policy; record non-sensitive diagnostic |

## 9. Use Case to MVP and SRS Traceability

| Use case | MVP capability | SRS requirement mapping |
|---|---|---|
| UC-001 | MVP-F-001 | FR-001, FR-002, FR-006, FR-020; NFR-001, NFR-002, NFR-003, NFR-011 |
| UC-002 | MVP-F-002, MVP-F-007 | FR-007, FR-008, FR-016, FR-017, FR-027; NFR-008 |
| UC-003 | MVP-F-003, MVP-F-008, MVP-F-009 | FR-004, FR-009, FR-016, FR-018, FR-027; NFR-008, NFR-014 |
| UC-004 | MVP-F-004, MVP-F-005, MVP-F-007 | FR-010, FR-011, FR-016, FR-018, FR-019, FR-020; NFR-004, NFR-008, NFR-010, NFR-014 |
| UC-005 | MVP-F-006 | FR-005, FR-011, FR-015; NFR-001, NFR-003, NFR-011 |
| UC-006 | MVP-F-006, MVP-F-008, MVP-F-009 | FR-004, FR-005, FR-018; NFR-008, NFR-014 |
| UC-007 | MVP-F-007, MVP-F-008 | FR-006, FR-016, FR-017, FR-019, FR-025; NFR-008, NFR-012 |
| UC-008 | MVP-F-008, MVP-F-009 | FR-004, FR-022, FR-027, FR-028; NFR-006, NFR-007, NFR-008 |
| UC-009 | MVP-F-010 | FR-015; NFR-001, NFR-002 |

The mapping is a candidate subset, not a change to SRS-001 or RTM-001. Existing requirements not mapped to MVP-1 remain candidates for later releases or cross-cutting controls and must not be treated as deleted.

## 10. Verification Scenario Planning

The following scenarios should be expanded into detailed test procedures in VVP-001 before execution:

- VS-001: Complete first-use flow with TalkBack or the selected screen reader.
- VS-002: Camera permission granted, denied, revoked, and restricted.
- VS-003: Capture starts only after explicit user action.
- VS-004: Successful OCR and speech playback.
- VS-005: Blank, blurred, rotated, dark, unsupported-language, and no-text inputs.
- VS-006: Partial/uncertain OCR result and malformed response.
- VS-007: Stop and replay speech without recapture.
- VS-008: Cancel during capture, OCR, and speech.
- VS-009: Late response after cancellation or a newer session.
- VS-010: Camera/OCR/TTS dependency unavailable and recovery.
- VS-011: App interruption/background/resume behavior.
- VS-012: Transient image cleanup and diagnostic privacy inspection.
- VS-013: Speech preference availability and persistence.
- VS-014: User can finish and return to a known ready state.

These are proposed scenarios, not executed tests. Test data must be lawfully sourced and documented. Participant-facing evaluation requires the approvals and safeguards in DATA-001 and SAF-001.

## 11. Open Questions and Validation Work

The following must be resolved through discovery, not assumed:
- Which text-reading contexts are most valuable (e.g., printed pages, labels, signs, menus), and which are appropriate for initial evaluation?
- Which languages, scripts, and reading directions are required first?
- What user interaction is preferred for capture and task navigation?
- What level of OCR uncertainty or partial-result disclosure is understandable and useful?
- Which Android versions/devices and assistive technologies can be supported and tested?
- What local data-retention behavior is acceptable and technically verifiable?

No response is requested as a blocker at this stage. These items remain documented research questions for the discovery phase.

## 12. Review and Change Control

Changes to these use cases shall identify affected MVP capabilities, SRS requirements, architecture components, interface contracts, hazards, privacy controls, accessibility behavior, test scenarios, and documentation. Any scope expansion or removal must follow GOV-001 and be reflected in RTM-001.

## 13. Version History

| Version | Date | Change |
|---|---|---|
| 0.1 | 2026-11-06 | Initial proposed actors, MVP user journey, detailed use cases, state model, failure catalogue, and traceability. |
