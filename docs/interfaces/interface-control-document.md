# Interface Control Document

| Attribute | Value |
|---|---|
| Document ID | ICD-001 |
| Version | 1.0 |
| Status | Logical interface contract; protocol TBD |
| Related | SYS-ARCH-001, SRS-001, HW-001, SEC-001 |

## 1. Purpose
Define logical interfaces among client, orchestration, AI adapters, device gateway, and external services. Wire formats, endpoints, authentication, and transport are not finalized.

## 2. Interface inventory
| ID | Producer | Consumer | Purpose |
|---|---|---|---|
| IF-001 | Accessible Client | Session Orchestrator | Start/cancel task and receive state |
| IF-002 | Capture Manager | Perception Adapter | Submit authorized task input |
| IF-003 | Perception Adapter | Result Interpreter | Structured result and metadata |
| IF-004 | Result Interpreter | Speech Output | User-facing response and limitations |
| IF-005 | Device Gateway | Connected Device | Pairing, status, supported commands |
| IF-006 | Privacy/Data Manager | Application components | Consent, retention, deletion decisions |
| IF-007 | Diagnostics | Maintainer interface | Non-sensitive health and failure status |

## 3. Message principles
Requests/responses should include correlation ID, schema version, task type, and explicit status. Sensitive payloads must not be copied into logs. Validate message size, type, origin, authorization, and schema.

## 4. Logical request fields
Request ID; schema version; task type; authorized input reference/payload; locale where supported; user interaction options; consent/processing policy reference. Exact representation is TBD.

## 5. Logical response fields
Request ID; status (success, partial, rejected, unavailable, failed); result type/content; uncertainty/quality metadata where meaningful; limitation/warning codes; duration; model/service identifier and version. Output must not imply unsupported certainty.

## 6. Device interface requirements
Pairing is user-initiated; identity and authorization are validated; status distinguishes disconnected, connecting, ready, busy, low battery, fault, and unsupported as applicable; firmware/protocol compatibility is checked; malformed/unauthorized commands are rejected; capture activation is observable.

## 7. Error model
Define stable codes for permission denied, invalid input, unsupported task, poor input quality, model unavailable, timeout, network unavailable, device disconnected, low battery, and internal failure. User messages must be accessible and actionable without exposing secrets or stack traces.

## 8. Versioning
Use explicit schema versions. Breaking changes require a version increment, migration/compatibility plan, and regression tests.

## 9. Open decisions
Transport, authentication, encryption, media transfer, payload limits, retry policy, timeout budgets, device discovery, and API hosting remain TBD pending architecture/security review.
