# MVP-1 Verification Procedure Specification

| Attribute | Value |
|---|---|
| Project | AI Guardian for Blind People |
| Document ID | VTP-MVP-001 |
| Version | 0.1 |
| Status | Draft procedures — platform, OCR engine, test data, and safety review pending |
| Document Type | MVP Verification Procedure Specification |
| Related | MVP-001, UC-001, SRS-001, RTM-001, VVP-001, ICD-001, ICD-MVP-001, SEC-001, SAF-001, ACC-001, DATA-001, ENG-READY-001 |
| Prepared | 06 November 2026 |

## 1. Purpose and status

This document expands the proposed MVP-1 interface scenarios into reviewable verification procedures. It is a test-design artifact only. No application, test harness, OCR engine, device configuration, or test corpus is currently approved by this document. No procedure in this document has been executed.

The procedures are intentionally platform-neutral. Exact control names, operating-system settings, automation methods, test-device models, timeout values, corpus contents, and measurable acceptance thresholds must be completed after platform and OCR selection.

## 2. Verification scope

MVP-1 is limited to a user-initiated smartphone still-image text-reading workflow:
- Accessible task entry and explicit user action.
- Camera permission and one still-image capture.
- OCR request/response handling.
- Result validation and explicit no-text/partial/failure handling.
- Spoken result, stop, replay, retry, and cancellation.
- Session closure and transient media lifecycle.
- Privacy-conscious diagnostics and rejection of stale/malformed responses.

Object recognition, scene description, continuous capture, voice-command initiation, autonomous navigation, external supporter access, custom hardware, and firmware are excluded from this MVP procedure set unless separately approved through change control.

## 3. Preconditions common to all procedures

Before executing any procedure, the test lead must record:
1. Approved MVP and requirement baseline revision.
2. Build identifier and configuration.
3. Device manufacturer/model, OS version, camera configuration, accessibility service and version.
4. OCR engine/provider identifier, version, configuration, and processing location.
5. TTS engine/service and supported voice/language configuration.
6. Network state and remote-service configuration, where applicable.
7. Test account/data state without real personal content.
8. Test corpus identifier, license/consent provenance, expected transcription, language/script, capture condition, and annotation version.
9. Applicable safety protocol and controlled test environment.
10. Tester, reviewer, date, and evidence-storage reference.

Use synthetic or specifically authorized test content. Do not use real identity documents, private correspondence, financial/medical records, or identifiable bystanders unless a separately approved protocol expressly permits it.

## 4. General execution and evidence rules

- Execute only on approved test devices in a controlled environment.
- Do not ask participants to rely on the prototype for navigation, road crossing, obstacle avoidance, or other physical safety decisions.
- Record actual observations separately from expected results.
- Preserve only the minimum test evidence necessary; redact personal data.
- A test is **Blocked** if a required platform, engine, dataset, safety control, or expected threshold is not approved.
- A test is **Not applicable** only with documented scope rationale and reviewer approval.
- A pass requires every mandatory expected result to be met and reviewed.
- A failure creates a defect record with severity, affected requirement, reproduction steps, and evidence.
- Re-test after correction and execute relevant regression cases.
- Do not derive OCR pass/fail from an arbitrary single accuracy score. Use the approved corpus protocol and approved release criteria.

## 5. Test procedure catalogue

### VTP-001 — Permission denied

**Traceability:** IF-MVP-001; UC-002; FR-007, FR-008; TC-FR-007, TC-FR-008.

**Preconditions:** Fresh permission state or a resettable test device; camera permission not granted.

**Steps:**
1. Launch the application and navigate using the supported screen reader.
2. Select the text-reading task.
3. Review the camera-purpose explanation.
4. Deny camera permission using the OS permission interface.
5. Return to the application and attempt to proceed.
6. Inspect application state and diagnostic output.

**Expected results:**
- No capture or OCR request is issued.
- The application announces a clear permission-denied state and available valid actions.
- The user can exit or reach the supported OS permission guidance.
- The application does not repeatedly prompt or bypass the OS decision.
- Diagnostics contain a non-sensitive permission error category only.

**Evidence:** Screen-reader observation, OS permission state, request trace, redacted diagnostic extract.

### VTP-002 — Capture request without explicit user action

**Traceability:** IF-MVP-002; UC-003; FR-009; TC-FR-009.

**Preconditions:** Camera permission granted; capture-ready session; instrumentation capable of observing capture invocation.

**Steps:**
1. Open the text-reading task and reach capture-ready state.
2. Do not activate the capture control.
3. Wait through the approved observation interval.
4. Navigate between controls without activating capture.
5. Inspect camera activity and capture/OCR request records.
6. If supported by the test harness, submit an invalid internal capture command that lacks trusted user-action context.

**Expected results:**
- No still image is captured before explicit user activation.
- No OCR request is created without an authorized media reference.
- Invalid internal commands are rejected.
- No continuous or background camera activity occurs as part of MVP-1.

**Evidence:** Camera activity record, request trace, screen-reader state observations.

### VTP-003 — Valid capture and OCR success

**Traceability:** IF-MVP-003; UC-003/004; FR-009–FR-011; TC-FR-009–011.

**Preconditions:** Approved test image with known ground truth; camera permission granted; selected OCR engine and supported language approved.

**Steps:**
1. Start a new text-reading session.
2. Confirm capture-ready state through accessible feedback.
3. Activate capture once.
4. Observe capture and processing state announcements.
5. Allow OCR to complete.
6. Compare returned text and metadata with the approved ground truth using the approved evaluation protocol.
7. Start speech output and listen to completion.

**Expected results:**
- One capture operation is associated with one request identifier.
- OCR response session/request identifiers match the active request.
- Result status and content are internally consistent.
- The application does not claim perfect or guaranteed recognition.
- Speech output presents the validated recognized text.
- Quality results are judged only against pre-approved corpus criteria; no threshold is invented here.

**Evidence:** Test image ID, ground-truth revision, redacted request/response metadata, transcription comparison, speech observations.

### VTP-004 — Wrong session or request identifier

**Traceability:** IF-MVP-004; UC-007; FR-018; TC-FR-018.

**Preconditions:** Test harness can inject controlled OCR responses; an active request exists.

**Steps:**
1. Start a session and issue a valid OCR request.
2. Prepare a response with a mismatched session identifier.
3. Deliver the response to the result-validation boundary.
4. Repeat with a mismatched request identifier.
5. Observe UI, speech, session state, and diagnostics.

**Expected results:**
- Both mismatched responses are rejected.
- No mismatched text is spoken or presented as the current result.
- The active request remains in a defined state or enters a documented failure state.
- A non-sensitive mismatch diagnostic may be recorded.

**Evidence:** Injected payload fixtures, request correlation trace, state and speech observations.

### VTP-005 — OCR no-text response

**Traceability:** IF-MVP-005; UC-004/007; FR-010, FR-019; TC-FR-010, TC-FR-019.

**Preconditions:** Approved blank/no-readable-text test image; OCR adapter test route.

**Steps:**
1. Start a new session and capture the approved blank/no-text image.
2. Allow OCR processing to complete.
3. Inspect response status and result interpretation.
4. Observe user-facing speech/status.

**Expected results:**
- The response uses an explicit NO_TEXT or approved equivalent status.
- Empty text is not represented as a successful reading.
- No text is invented or inferred.
- The user receives an understandable message and valid recovery option.

**Evidence:** Image fixture ID, response status, screen-reader/TTS observation.

### VTP-006 — Partial OCR response

**Traceability:** IF-MVP-006; UC-004/007; FR-010, FR-019; TC-FR-010, TC-FR-019.

**Preconditions:** Approved test image with deliberately occluded or partially legible text; expected partial-transcription annotation.

**Steps:**
1. Start a new session and capture the partial-text fixture.
2. Receive OCR response.
3. Inspect partial status, recognized blocks, and available quality metadata.
4. Listen to the spoken output.
5. Compare recognized content with the approved partial ground truth.

**Expected results:**
- Partial output is explicitly labelled as partial or uncertain.
- The system does not silently imply that the full source was read.
- Missing words are not fabricated.
- User can stop, replay, recapture, or close according to the approved workflow.

**Evidence:** Fixture and annotation IDs, response, output observation, comparison report.

### VTP-007 — Cancel during capture

**Traceability:** IF-MVP-007; UC-006; FR-004; TC-FR-004.

**Preconditions:** Capture operation can be paused or delayed in a controlled test environment.

**Steps:**
1. Start a session and initiate one capture.
2. While capture is pending, activate cancel.
3. Observe ORCH and CAP state transitions.
4. Allow any delayed capture callback to arrive.
5. Inspect whether OCR was subsequently invoked.

**Expected results:**
- Session enters cancellation before accepting later callbacks.
- Capture stops where supported; otherwise its output is suppressed.
- No OCR request proceeds after cancellation.
- Session reaches CLOSED or another explicitly documented terminal state.
- No late callback reopens the session.

**Evidence:** Timestamped state/request trace and cancellation observations.

### VTP-008 — Cancel during OCR

**Traceability:** IF-MVP-008; UC-006; FR-004, FR-018; TC-FR-004, TC-FR-018.

**Preconditions:** OCR processing can be delayed; response can be released after cancellation.

**Steps:**
1. Start a valid capture and OCR request.
2. Hold the OCR response in the test harness.
3. Cancel the session.
4. Release the held OCR response.
5. Observe result validation, speech, state, and diagnostics.

**Expected results:**
- Cancellation is recorded before the late response is processed.
- Late OCR result is discarded and never spoken.
- Session remains closed.
- Temporary media references are invalidated/released under system control.
- No stale result is shown as current.

**Evidence:** Correlation trace, cancellation timestamp, late-response injection record.

### VTP-009 — Cancel during speech

**Traceability:** IF-MVP-009; UC-005/006; FR-004, FR-005; TC-FR-004, TC-FR-005.

**Preconditions:** Valid result available; TTS can be observed or controlled.

**Steps:**
1. Start speech output for a sufficiently long approved test passage.
2. Activate stop-speech and verify interruption.
3. Replay the result.
4. Activate session cancel while speech is active.
5. Observe speech and session state.

**Expected results:**
- Stop-speech interrupts the current speech operation.
- Replay speaks the same validated result without recapture.
- Session cancellation stops speech and closes the session.
- A delayed TTS completion callback cannot move a closed session back to an active state.

**Evidence:** Speech-operation identifiers, state trace, screen-reader/TTS observations.

### VTP-010 — Timeout followed by late OCR success

**Traceability:** IF-MVP-010; UC-007; FR-016, FR-018; TC-FR-016, TC-FR-018.

**Preconditions:** Approved timeout configuration exists; test harness can delay OCR beyond it.

**Steps:**
1. Start a valid OCR request.
2. Delay response beyond the approved timeout.
3. Observe timeout status and recovery options.
4. Retry using a new request identifier where permitted.
5. Release the original delayed response.
6. Observe whether the old response is accepted.

**Expected results:**
- Timeout creates a typed recoverable failure.
- Retry creates a new request identifier.
- The old response is rejected as stale/expired.
- No late result is spoken or substituted for the newer request.
- Actual timeout value is taken from the approved configuration, not assumed by this procedure.

**Evidence:** Timeout configuration, request identifiers, timestamped response trace.

### VTP-011 — Duplicate retry command

**Traceability:** IF-MVP-011; UC-007; FR-017; TC-FR-017.

**Preconditions:** Capture/OCR request can be held active; duplicate action can be injected.

**Steps:**
1. Start a capture or OCR operation.
2. Trigger retry once while the operation is active.
3. Immediately submit a duplicate retry action.
4. Inspect active operation count and request identifiers.
5. Observe user-facing state.

**Expected results:**
- Duplicate action does not create concurrent unintended captures or duplicate speech.
- The user receives a clear state or valid retry response.
- A new request is created only after the prior operation is cancelled/closed or retry is explicitly permitted by the state model.

**Evidence:** Operation count, identifiers, state trace.

### VTP-012 — Malformed OCR response

**Traceability:** IF-MVP-012; UC-007; FR-016, FR-018; TC-FR-016, TC-FR-018.

**Preconditions:** Controlled OCR response injection.

**Steps:**
1. Start a valid OCR request.
2. Inject a response missing mandatory fields.
3. Repeat with invalid status/content combinations and unsupported schema version.
4. Observe result validation and user output.
5. Inspect diagnostics for sensitive leakage.

**Expected results:**
- Each invalid response is rejected safely.
- No malformed or untrusted text is spoken.
- User receives a generic understandable failure and valid recovery action.
- Logs contain stable non-sensitive error categories only; no stack trace or payload content.

**Evidence:** Payload fixtures, validation result, user-facing message, redacted logs.

### VTP-013 — Media reference after session closure

**Traceability:** IF-MVP-013; UC-008; FR-022, FR-023, FR-028; TC-FR-022, TC-FR-023, TC-FR-028; TC-NFR-006/007.

**Preconditions:** Storage inspection method and approved platform data-lifecycle map available.

**Steps:**
1. Start a session and capture an approved synthetic test image.
2. Complete or cancel the session.
3. Close the session using the supported control.
4. Attempt to reuse the media reference through the authorized test harness.
5. Inspect application-controlled temporary storage, caches, and logs.
6. Record any OS/provider-managed retention behavior separately.

**Expected results:**
- Application-controlled media references are invalidated after their defined lifecycle.
- Reuse is rejected or fails because the reference is no longer valid.
- Application-controlled temporary copies are removed according to the approved design.
- No raw image or recognized text appears in routine diagnostics.
- The test does not claim deletion from OS/provider-managed locations unless verified.

**Evidence:** Data-flow map, storage inspection, reference invalidation result, redacted log review.

### VTP-014 — Diagnostic privacy inspection

**Traceability:** IF-MVP-014; UC-008; FR-028; TC-FR-028, TC-NFR-007.

**Preconditions:** Logging enabled in approved test configuration; synthetic image and text only.

**Steps:**
1. Run success, no-text, malformed-response, permission-denied, and cancellation scenarios.
2. Collect application diagnostics through the approved test channel.
3. Search for raw image bytes, recognized text, raw audio, credentials, access tokens, direct identifiers, and unnecessary personal data.
4. Review event fields and retention configuration.
5. Record any exception with exact source and severity without copying sensitive values into the report.

**Expected results:**
- Logs use documented event/error categories and minimum necessary metadata.
- Raw images, recognized text, raw audio, credentials, and unnecessary personal data are absent by default.
- Any explicitly approved diagnostic exception has a documented purpose, consent basis, access control, retention, and deletion rule.
- Log access is restricted to authorized roles.

**Evidence:** Redacted log sample, inspection checklist, configuration reference.

## 6. Cross-cutting accessibility checks

Apply the following checks to VTP-001 through VTP-014:
- All actions and states are reachable and understandable without sight.
- Focus is not lost when permission dialogs or system camera interfaces return control.
- Capture, processing, success, partial result, failure, cancellation, and closure are distinguishable.
- Stop/cancel remains reachable during long-running operations.
- Announcements do not create repeated or contradictory status messages.
- Error recovery does not depend on a visual-only instruction.
- Screen-reader and TTS speech do not compete in a way that makes critical instructions inaccessible.

These checks require an approved assistive-technology/device matrix and review by intended users before release.

## 7. OCR corpus and evaluation protocol requirements

The OCR test corpus must be separately controlled and include:
- Documented language and script coverage.
- Ground-truth transcription with annotation rules and reviewer records.
- Lawful source, license, consent, and permitted-use statement.
- Held-out evaluation partition not used for engine tuning.
- Representative typography, layout, orientation, capture distance, lighting, blur, occlusion, and background conditions derived from intended use.
- Blank/no-text, partial, unsupported-language, and out-of-distribution cases.
- Versioned fixture identifiers and reproducible capture/processing conditions.

The evaluation report must state engine version, device, configuration, corpus version, metric definitions, per-condition results, error examples, uncertainty behavior, latency, and known limitations. Thresholds require formal approval before execution/release. Do not invent a corpus or claim representative coverage before it exists.

## 8. Test record template

Each executed case shall use this record:

| Field | Record |
|---|---|
| Test ID / revision | TBD |
| Requirement and interface trace | TBD |
| Procedure revision | TBD |
| Build/configuration | TBD |
| Device/OS/accessibility stack | TBD |
| OCR/TTS versions and processing route | TBD |
| Test fixture/corpus and provenance | TBD |
| Preconditions | TBD |
| Steps performed | TBD |
| Expected result | TBD |
| Actual result | TBD |
| Status | Not designed / Designed / Ready / Executed-Pass / Executed-Fail / Blocked / Not applicable |
| Evidence reference | TBD |
| Defect/deviation | TBD |
| Tester/date | TBD |
| Reviewer/date | TBD |
| Retest/regression links | TBD |

## 9. Exit criteria

The MVP verification package is ready for execution only when:
- Target platform, device/OS baseline, OCR engine, TTS route, and processing location are selected and recorded.
- Test corpus and data provenance are approved.
- Test procedures are reviewed and mapped to approved requirements.
- Test environment, instrumentation, and fixtures are reproducible.
- Safety, privacy, and accessibility review conditions are met.
- All release thresholds are approved before test execution.
- Test evidence handling and defect workflow are operational.

MVP release cannot be recommended solely from successful happy-path demonstration. All applicable P0 requirements and safety/privacy/accessibility release gates require objective evidence and approved risk disposition.

## 10. Version history

| Version | Date | Change |
|---|---|---|
| 0.1 | 2026-11-06 | Initial platform-neutral MVP-1 verification procedures for permission, capture, OCR, result validation, speech, cancellation, privacy, and diagnostic behavior. |
