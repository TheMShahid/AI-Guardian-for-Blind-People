# Requirements Traceability Matrix

| Attribute | Value |
|---|---|
| Document ID | RTM-001 |
| Version | 1.2 |
| Status | Expanded planned traceability — stakeholder validation and test execution pending |
| Related | PID-001, SRS-001, SYS-ARCH-001, HW-001, ICD-001, SAF-001, ACC-001, SEC-001, VVP-001, MVP-001, UC-001, ICD-MVP-001, VTP-MVP-001 |

## 1. Purpose and interpretation

This matrix provides bidirectional traceability from candidate stakeholder/system needs to software requirements, logical architecture, hardware requirements, and planned verification. It is a planning baseline only. A planned test ID is not evidence that a test has been designed in executable detail or run.

All SRS-001 requirements currently have status **Proposed**. Evidence status is **Not executed** unless updated with a controlled test record.

## 2. Need catalogue

| Need ID | Need statement | Source / validation state |
|---|---|---|
| NEED-01 | A blind or low-vision user can understand the product, its limits, and how to operate it accessibly. | User need; stakeholder validation pending |
| NEED-02 | The user can deliberately select, start, control, and end an assistance task. | User need; stakeholder validation pending |
| NEED-03 | The user can obtain bounded visual information such as recognized text, supported object information, or scene description. | Candidate use case; priority and task scope pending |
| NEED-04 | The user retains control over camera/microphone activation and personal data. | Privacy and safety constraint |
| NEED-05 | The user receives understandable status, uncertainty, and recovery information when the system cannot help. | Safety and usability need |
| NEED-06 | AI results do not create false confidence or imply guaranteed mobility safety. | Safety constraint |
| NEED-07 | The user can receive and control spoken feedback and use supported speech interaction. | Accessibility/user need; validation pending |
| NEED-08 | Optional connected hardware can be paired, monitored, and safely disconnected. | Conditional system need; hardware selection pending |
| NEED-09 | The user can control optional history, deletion, and authorized supporter access. | Privacy/user need; policy validation pending |
| NEED-10 | Maintainers can diagnose faults without unnecessary access to sensitive user content. | Operations/privacy need |
| NEED-11 | The product has measured accessibility, AI quality, performance, reliability, and resource behavior before release. | Verification/release constraint |
| NEED-12 | The product's data, platform, and external-service dependencies are documented and controlled. | Architecture/security/operations constraint |

## 3. Software requirement traceability

Architecture component abbreviations:
- **UI** = Accessible Client
- **ORCH** = Session Orchestrator
- **CAP** = Capture Manager
- **AI** = Perception Adapter
- **RES** = Result Interpreter
- **TTS** = Speech Output
- **DEV** = Device Gateway
- **DATA** = Privacy/Data Manager
- **DIAG** = Diagnostics

| Requirement ID | Need ID(s) | Architecture allocation | Planned verification | Hardware trace | Evidence status |
|---|---|---|---|---|---|
| FR-001 | NEED-01, NEED-06 | UI, RES | TC-FR-001 (I,D) | — | Not executed |
| FR-002 | NEED-02 | UI, ORCH | TC-FR-002 (T) | — | Not executed |
| FR-003 | NEED-02, NEED-07 | UI, ORCH | TC-FR-003 (T,D) | Conditional: HW-REQ-008 | Not executed |
| FR-004 | NEED-02, NEED-06 | ORCH, CAP, AI | TC-FR-004 (T) | Conditional: HW-REQ-002 | Not executed |
| FR-005 | NEED-02, NEED-07 | UI, TTS | TC-FR-005 (T) | — | Not executed |
| FR-006 | NEED-01, NEED-05 | UI, ORCH, DIAG | TC-FR-006 (T) | Conditional: HW-REQ-003, HW-REQ-004 | Not executed |
| FR-007 | NEED-04 | UI, CAP, DATA | TC-FR-007 (I,T) | — | Not executed |
| FR-008 | NEED-01, NEED-04 | UI, DATA | TC-FR-008 (I,T) | — | Not executed |
| FR-009 | NEED-02, NEED-04, NEED-06 | CAP, ORCH | TC-FR-009 (T,I) | HW-REQ-001, HW-REQ-002 | Not executed |
| FR-010 | NEED-03, NEED-05 | AI, RES | TC-FR-010 (T) | Conditional: HW-REQ-001 | Not executed |
| FR-011 | NEED-03, NEED-07 | RES, TTS, UI | TC-FR-011 (T) | — | Not executed |
| FR-012 | NEED-03, NEED-05, NEED-06 | AI, RES | TC-FR-012 (T,A) | Conditional: HW-REQ-001 | Not executed |
| FR-013 | NEED-03, NEED-05, NEED-06 | AI, RES | TC-FR-013 (T,I) | Conditional: HW-REQ-001 | Not executed |
| FR-014 | NEED-04, NEED-07 | UI, CAP, ORCH | TC-FR-014 (T,I) | — | Not executed |
| FR-015 | NEED-01, NEED-07 | UI, TTS | TC-FR-015 (T) | — | Not executed |
| FR-016 | NEED-05, NEED-08, NEED-10 | ORCH, CAP, AI, DEV, DIAG | TC-FR-016 (T) | HW-REQ-003, HW-REQ-004 | Not executed |
| FR-017 | NEED-02, NEED-05, NEED-08 | UI, ORCH, DEV, DIAG | TC-FR-017 (T,D) | HW-REQ-004, HW-REQ-008 | Not executed |
| FR-018 | NEED-05, NEED-06 | ORCH, AI, RES | TC-FR-018 (T) | — | Not executed |
| FR-019 | NEED-05, NEED-06 | AI, RES, TTS | TC-FR-019 (T,I) | — | Not executed |
| FR-020 | NEED-01, NEED-06 | UI, RES | TC-FR-020 (I,T) | — | Not executed |
| FR-021 | NEED-08 | DEV, UI, DIAG | TC-FR-021 (T) | HW-REQ-003, HW-REQ-004, HW-REQ-009 | Not executed |
| FR-022 | NEED-04, NEED-09 | DATA, UI | TC-FR-022 (T,I) | — | Not executed |
| FR-023 | NEED-04, NEED-09 | DATA, UI | TC-FR-023 (T,D) | — | Not executed |
| FR-024 | NEED-04, NEED-10 | UI, DATA, DIAG | TC-FR-024 (T,I) | — | Not executed |
| FR-025 | NEED-05, NEED-12 | ORCH, DIAG, UI | TC-FR-025 (T) | — | Not executed |
| FR-026 | NEED-04, NEED-09 | UI, DATA | TC-FR-026 (T,I) | — | Not executed |
| FR-027 | NEED-01, NEED-04 | UI, CAP, DATA | TC-FR-027 (T,D) | Conditional: HW-REQ-001 | Not executed |
| FR-028 | NEED-10, NEED-12 | DIAG, DATA | TC-FR-028 (I,T) | — | Not executed |
| NFR-001 | NEED-01, NEED-02, NEED-07 | UI, TTS | TC-NFR-001 (T,D) | — | Not executed |
| NFR-002 | NEED-01, NEED-02 | UI | TC-NFR-002 (I,T) | — | Not executed |
| NFR-003 | NEED-01, NEED-05 | UI, ORCH, TTS | TC-NFR-003 (T) | — | Not executed |
| NFR-004 | NEED-03, NEED-11 | ORCH, AI, RES | TC-NFR-004 (A,T) | Conditional: HW-REQ-006 | Not executed |
| NFR-005 | NEED-04, NEED-12 | AI, DEV, DATA | TC-NFR-005 (I,T) | HW-REQ-009 | Not executed |
| NFR-006 | NEED-04, NEED-09, NEED-12 | DATA | TC-NFR-006 (I,T) | — | Not executed |
| NFR-007 | NEED-04, NEED-10 | DIAG, DATA | TC-NFR-007 (I,T) | — | Not executed |
| NFR-008 | NEED-05, NEED-08 | ORCH, CAP, DEV, DIAG | TC-NFR-008 (T) | HW-REQ-004, HW-REQ-008 | Not executed |
| NFR-009 | NEED-01, NEED-11, NEED-12 | UI, platform integration | TC-NFR-009 (I) | Conditional compatibility evidence for selected hardware | Not executed |
| NFR-010 | NEED-03, NEED-06, NEED-11 | AI, RES | TC-NFR-010 (A) | — | Not executed |
| NFR-011 | NEED-01, NEED-02, NEED-07 | UI, TTS | TC-NFR-011 (T,D) | — | Not executed |
| NFR-012 | NEED-05, NEED-10, NEED-12 | DIAG, DATA | TC-NFR-012 (I,T) | — | Not executed |
| NFR-013 | NEED-08, NEED-11 | ORCH, AI, DEV | TC-NFR-013 (A,T) | HW-REQ-006; HW-REQ-003 | Not executed |
| NFR-014 | NEED-05, NEED-06, NEED-08 | RES, ORCH, DEV, UI | TC-NFR-014 (T,I) | HW-REQ-003, HW-REQ-004 | Not executed |

A dash means no direct physical hardware requirement is allocated. “Conditional” means the software behavior depends on a future hardware choice and is not a commitment that the hardware will be included.

## 4. Hardware requirement traceability

| Hardware requirement | Need ID(s) | Related software requirement(s) | Architecture/interface area | Planned verification | Evidence status |
|---|---|---|---|---|---|
| HW-REQ-001 | NEED-04, NEED-06, NEED-08 | FR-009, FR-027 | CAP, DEV; ICD-001 capture/status interface | Hardware inspection and capture-indicator integration test | Not executed |
| HW-REQ-002 | NEED-04, NEED-06 | FR-004, FR-009 | CAP, ORCH; capture control | Bench test of capture activation and shutdown | Not executed |
| HW-REQ-003 | NEED-05, NEED-08, NEED-11 | FR-006, FR-016, FR-021; NFR-013, NFR-014 | DEV, DIAG; telemetry/status interface | Battery/status telemetry and fault tests | Not executed |
| HW-REQ-004 | NEED-05, NEED-08 | FR-016, FR-017, FR-021; NFR-008, NFR-014 | DEV, ORCH; connection lifecycle | Disconnect/reconnect and stale-state tests | Not executed |
| HW-REQ-005 | NEED-08 | None direct; system safety constraint | Enclosure/mechanical design | Inspection and supervised fit/handling review | Not executed |
| HW-REQ-006 | NEED-08, NEED-11 | NFR-004, NFR-013 | Device power/thermal; system performance | Instrumented thermal and charging tests against selected component limits | Not executed |
| HW-REQ-007 | NEED-01, NEED-08 | NFR-001, NFR-009 | Form factor, CAP | Consent-based user evaluation and fit/field-of-view assessment | Not executed |
| HW-REQ-008 | NEED-02, NEED-05, NEED-08 | FR-003, FR-017; NFR-008 | Device controls, DEV, ORCH | Power-off/reset usability and shutdown tests | Not executed |
| HW-REQ-009 | NEED-04, NEED-08, NEED-12 | FR-021; NFR-005 | DEV, ICD-001 pairing/command boundary | Pairing authorization and command-security tests | Not executed |
| HW-REQ-010 | NEED-01, NEED-06 | FR-001, FR-020 | UI, product labeling/documentation | Inspection of device label and user-facing warnings | Not executed |

## 5. Verification planning and evidence rules

1. Planned test identifiers are reserved in VVP-001. Detailed procedures, test data, fixtures, and expected results must be completed before execution.
2. Every test record shall identify requirement IDs, build/software version, model and preprocessing version where relevant, device/OS/firmware, test data provenance, network and environmental conditions, tester, date, expected result, actual result, evidence location, and defect reference.
3. Evidence status values: **Not designed**, **Designed**, **Ready**, **Executed-Pass**, **Executed-Fail**, **Blocked**, **Not applicable**. Do not use “Pass” without a dated test record and reviewer.
4. A requirement is **Implemented** only when implementation evidence exists. It is **Verified** only when its defined verification passes. Demonstration alone does not replace required testing or analysis.
5. P0 requirements and safety/privacy controls are release gates. Failed or blocked P0 requirements prevent release unless a formally authorized risk disposition explicitly permits otherwise; no waiver may override applicable law or create a false safety claim.
6. User-needs validation, accessibility testing with representative users, and controlled consented evaluation are separate evidence streams; developer self-testing does not substitute for them.

## 6. Coverage rules

- Every SRS requirement shall trace to at least one need or justified system constraint, architecture allocation, and planned verification.
- Every hardware requirement shall trace to a need, a verification activity, and software/interface requirements where relevant.
- Every approved requirement shall have at least one verification record or an explicitly justified analysis/inspection record.
- Orphan requirements, orphan tests, and unallocated hardware requirements shall be reviewed at each baseline change.
- Requirement changes trigger impact analysis across architecture, ICD, safety, privacy, AI evaluation, hardware, and test plans.
- Traceability shall be reviewed before design baseline approval and each release candidate.

## 7. Status vocabulary

Requirement lifecycle: Proposed, Under Review, Approved, Implemented, Verified, Failed, Blocked, Deferred, Retired.

Evidence lifecycle: Not designed, Designed, Ready, Executed-Pass, Executed-Fail, Blocked, Not applicable.

These are separate from document status. Document status is governed by GOV-001.

## 8. Current baseline summary

- SRS-001 software requirements traced: 42 (28 functional, 14 non-functional).
- HW-001 hardware requirements traced: 10.
- Planned software test identifiers: 42.
- Executed test evidence: 0 recorded in this matrix.
- Stakeholder/user validation: pending.
- Architecture and hardware allocation: preliminary; conditional allocations remain subject to design decisions.

## 9. Version history

| Version | Date | Change |
|---|---|---|
| 1.0 | Initial | Initial high-level need-to-requirement mapping. |
| 1.1 | 2026-11-06 | Added individual software requirement traceability, architecture allocation, hardware cross-links, planned test IDs, evidence rules, and baseline coverage summary. |\n| 1.2 | 2026-11-06 | Added traceability references to the MVP-specific interface and draft verification procedure supplements; clarified that detailed procedures are not executed evidence. |
