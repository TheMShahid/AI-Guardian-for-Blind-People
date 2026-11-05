# Requirements Traceability Matrix

| Attribute | Value |
|---|---|
| Document ID | RTM-001 |
| Version | 1.0 |
| Status | Initial mapping; test IDs pending |
| Related | PID-001, SRS-001, SYS-ARCH-001, VVP-001 |

## 1. Purpose
Maintain bidirectional traceability from stakeholder needs to requirements, architecture, verification, and evidence. This is planned coverage, not evidence that tests have run.

## 2. Traceability
| Need ID | Stakeholder need | Requirement IDs | Architecture area | Verification |
|---|---|---|---|---|
| NEED-01 | Operate core tasks without sight | FR-001–FR-005, NFR-001–NFR-003, NFR-011 | Accessible interaction | Accessibility and task usability tests |
| NEED-02 | Understand selected visual information | FR-008, FR-009, NFR-010 | AI perception/result presentation | Dataset evaluation and scenario tests |
| NEED-03 | Control capture and personal data | FR-007, FR-013–FR-015, NFR-005–NFR-007 | Privacy/data controls | Permission, retention, deletion, security tests |
| NEED-04 | Know when assistance is unavailable | FR-006, FR-012, FR-017, NFR-008 | Orchestration/diagnostics | Fault-injection and recovery tests |
| NEED-05 | Use connected device when available | FR-011 | Device integration | Pairing, disconnection, compatibility tests |
| NEED-06 | Avoid unsafe reliance on AI | FR-016 and safety constraints | Safety controls | Hazard-control verification and content review |
| NEED-07 | Receive useful, timely feedback | FR-003, FR-004, FR-010, NFR-004 | Audio interaction | Latency and interaction tests |
| NEED-08 | Report incorrect outputs | FR-018 | Feedback/quality loop | Workflow and privacy review |

## 3. Coverage rules
1. Every approved requirement traces to a user need or justified system constraint.
2. Every P0/P1 requirement has a verification method and planned test ID.
3. Failed or blocked verification remains visible and is never marked passed.
4. Requirement changes trigger review of architecture, interfaces, risks, and tests.
5. Release evidence records requirement, test, build/configuration, result, date, and reviewer.

## 4. Status vocabulary
Proposed, under review, approved, implemented, verified, failed, blocked, deferred, retired. Implemented and verified are distinct states.
