# Interface Control Document

| Attribute | Value |
|---|---|
| Document ID | ICD-001 |
| Version | 1.2 |
| Status | Refined logical interface contract; protocol and schemas TBD |
| Related | SYS-ARCH-001, SRS-001, RTM-001, HW-001, SEC-001, VVP-001, ICD-MVP-001 |

## 1. Purpose and scope

Define logical interface responsibilities and minimum contract semantics among the accessible client, orchestration, capture, AI adapters, device gateway, privacy/data manager, diagnostics, and external services. Wire formats, endpoints, transport, authentication implementation, and payload limits are not finalized. This document is not an API implementation specification.

## 1.1 MVP-specific interface refinement\n\nFor the proposed smartphone text-reading MVP, the detailed capture, OCR, result-validation, speech, cancellation, and error contracts are specified in **ICD-MVP-001**. That document supplements this system-wide interface inventory and does not supersede interfaces IF-001 through IF-008. If an MVP-specific detail appears inconsistent with this system-level contract, the discrepancy must be resolved through GOV-001 before implementation.\n\n## 2. Interface inventory

| ID | Producer | Consumer | Purpose | Related requirements |
|---|---|---|---|---|
| IF-001 | Accessible Client | Session Orchestrator | Start/cancel task and receive lifecycle state | FR-002–FR-006, FR-017 |
| IF-002 | Capture Manager | Perception Adapter | Submit user-authorized task input | FR-007–FR-010, FR-014 |
| IF-003 | Perception Adapter | Result Interpreter | Structured result and metadata | FR-010–FR-013, FR-018–FR-019 |
| IF-004 | Result Interpreter | Speech Output | User-facing response, uncertainty, and limitations | FR-005, FR-011, FR-013, FR-015, FR-019–FR-020 |
| IF-005 | Device Gateway | Connected Device | Pairing, status, and supported commands | FR-016–FR-017, FR-021; HW-REQ-001–004, HW-REQ-008–010 |
| IF-006 | Privacy/Data Manager | Application components | Consent, retention, deletion, and access decisions | FR-007–FR-009, FR-022–FR-027 |
| IF-007 | Diagnostics | Maintainer interface | Non-sensitive health and failure status | FR-006, FR-016–FR-018, FR-028; NFR-007, NFR-012 |
| IF-008 | AI/External Service Adapter | External inference service | Authorized inference request and bounded response | FR-010–FR-013, NFR-005–NFR-010 |

## 3. Contract principles

1. Every request/response exchange shall use a correlation identifier and explicit schema/version identifier.
2. Requests shall identify the task type and only the input authorized for that task.
3. Responses shall identify the corresponding request/session and a defined status.
4. Components shall validate message origin, authorization, size, type, and schema before processing.
5. Unknown or unsupported fields/status values shall be handled safely; malformed messages shall not be treated as successful results.
6. Timeouts, retries, and cancellation shall preserve idempotency or use explicit duplicate protection.
7. Sensitive media and credentials shall not be copied into diagnostic logs.
8. AI-generated content shall remain distinguishable from trusted application, permission, capture, and device status.

## 4. Logical request contract

Candidate logical fields (exact names and representation TBD):

- Request/correlation ID.
- Schema version.
- Session ID.
- Task type and requested operation.
- Authorized input reference or payload.
- Locale/language where supported.
- User interaction options relevant to the task.
- Consent/processing-policy reference.
- Creation time and expiry/validity metadata where required.

The contract shall not transmit unrelated media or user data. Data minimization and processing location shall be documented for each adapter.

## 5. Logical response contract

Candidate logical fields (exact names and representation TBD):

- Matching request/correlation ID and session ID.
- Schema version.
- Status: success, partial, rejected, unavailable, failed, or cancelled.
- Result type and content, when available.
- Uncertainty/quality metadata where meaningful and supported.
- Limitation, warning, and error codes.
- Processing duration and model/service identifier/version where available.
- Freshness/creation metadata needed to reject stale results.

A partial, uncertain, malformed, expired, or mismatched response shall never be silently represented as a fresh, complete, certain result.

## 6. Session and cancellation semantics

The orchestrator owns session lifecycle. A cancellation request shall mark the session as cancelling/cancelled according to the achievable component state. Components shall discard or quarantine late responses for cancelled, expired, or superseded sessions. The UI shall not announce a result as current unless its session and freshness checks pass. Exact timeout and cancellation budgets remain TBD pending platform benchmarks.

## 7. Device interface requirements

Pairing shall be user-initiated. Device identity and authorization shall be validated. Status should distinguish disconnected, connecting, ready, busy, low battery, fault, and unsupported states as applicable. Firmware/protocol compatibility shall be checked. Malformed or unauthorized commands shall be rejected. Capture activation shall be observable. Device commands shall not imply autonomous mobility or obstacle-avoidance capability.

## 8. Error model

Define stable machine-readable categories for permission denied, invalid input, unsupported task, poor input quality, model unavailable, timeout, network unavailable, device disconnected, low battery, malformed response, expired/stale response, cancelled request, and internal failure.

User-facing messages shall be accessible, concise, actionable, and safe. Diagnostic details shall not expose credentials, raw media, personal data, stack traces, or internal secrets.

## 9. Security and privacy

Authenticate and authorize external service and device interactions as applicable. Protect data in transit and at rest using approved platform/service controls. Validate service identity and response integrity. Apply least privilege, consent policy, retention limits, and deletion policy. Third-party processing, data residency, and provider retention must be assessed and disclosed before integration.

## 10. Versioning and compatibility

Use explicit schema versions. Breaking changes require a version increment, migration/compatibility plan, and regression tests. Maintain a compatibility matrix for application, device firmware, protocol, and external service versions. Unsupported combinations shall fail explicitly rather than degrade silently.

## 11. Open decisions

Transport, authentication mechanism, encryption configuration, media transfer strategy, payload limits, retry policy, timeout budgets, device discovery, API hosting, schema serialization, and third-party service selection remain TBD pending architecture, privacy, security, and feasibility review.

## 12. Version history

| Version | Date | Change |
|---|---|---|
| 1.0 | Initial | Initial logical interface inventory and principles. |
| 1.1 | 2026-11-06 | Added requirement trace links, request/response contract semantics, cancellation/stale-response handling, privacy/security controls, and compatibility expectations. |\n| 1.2 | 2026-11-06 | Linked the MVP-specific interface supplement and clarified document authority. |
