# Safety and Risk Management Plan

| Attribute | Value |
|---|---|
| Document ID | SAF-001 |
| Version | 1.1 |
| Status | Initial hazard register refined; specialist and lived-experience review required |
| Related | PID-001, SRS-001, RTM-001, AIML-001, HW-001, ACC-001, SEC-001, VVP-001 |

## 1. Safety policy and intended use

AI Guardian is supplementary informational assistance, not a certified mobility aid or replacement for a white cane, guide dog, orientation and mobility training, or human assistance. Initial scope excludes autonomous street crossing, guaranteed obstacle avoidance, and claims that a route or environment is safe.

The prototype shall be evaluated in controlled conditions. Participants shall not rely on it for navigation or expose themselves to uncontrolled traffic or avoidable hazards.

## 2. Risk-management method

For each hazard record: hazard ID; hazardous situation; initiating event; foreseeable sequence; potential harm; affected users/bystanders; severity; likelihood/exposure; risk rationale; controls; verification evidence; residual risk; owner; and approval.

A competent review group shall select and document a consistent qualitative or quantitative rating method before assigning ratings. This initial register does not invent severity or likelihood scores. A disclaimer alone is not an adequate risk control.

## 3. Initial hazard register

| ID | Hazardous situation | Potential harm | Initial controls | Requirement/test trace |
|---|---|---|---|---|
| H-001 | Incorrect object/scene description trusted as fact | User acts on false information | Bounded task scope, uncertainty/abstention, class/scenario evaluation | FR-012, FR-013, FR-019; TC-FR-012, TC-FR-013, TC-FR-019 |
| H-002 | System fails to detect an obstacle | Collision/injury | No obstacle-avoidance guarantee; no mobility direction from model | FR-020; TC-FR-020 |
| H-003 | Road/traffic context misinterpreted | Unsafe crossing | Explicit exclusion of crossing decisions and unsafe claims | FR-020; TC-FR-020 |
| H-004 | Delayed or stale output interpreted as current | Action based on old information | Session correlation, freshness validation, cancellation of stale responses | FR-004, FR-018; TC-FR-004, TC-FR-018 |
| H-005 | Camera blocked, misaligned, or poor quality | Misleading result | Input-quality checks, failure state, retry guidance | FR-016, FR-019; TC-FR-016, TC-FR-019 |
| H-006 | Audio masks environmental sounds | Reduced situational awareness | User-controlled audio, no default continuous masking, evaluate open-ear options | FR-005, FR-015; TC-FR-005, TC-FR-015 |
| H-007 | Attachment snags, shifts, or obstructs mobility aid | Discomfort/injury | Ergonomic review, safe mounting, no interference with established aids | HW-REQ-005, HW-REQ-007; hardware verification plan |
| H-008 | Battery/device/thermal failure | Assistance unexpectedly stops or causes discomfort | Status/low-battery communication, component-limit testing, safe shutdown | FR-016, FR-017; HW-REQ-003, HW-REQ-004, HW-REQ-006, HW-REQ-008 |
| H-009 | User assumes AI output is guaranteed | Unsafe reliance | Accessible onboarding, contextual limitations, uncertainty and task boundaries | FR-001, FR-019, FR-020; TC-FR-001, TC-FR-019, TC-FR-020 |
| H-010 | Bystander content captured or retained | Privacy harm | User-initiated capture, minimization, consent, retention/deletion controls | FR-007–009, FR-022–024; TC-FR-007–009, TC-FR-022–024 |
| H-011 | Capture continues after cancellation or without clear indication | Privacy intrusion and loss of control | Explicit capture lifecycle, observable indicator, cancellation testing | FR-004, FR-009; HW-REQ-001, HW-REQ-002 |
| H-012 | Device disconnects but app uses stale telemetry/result | Incorrect status or action | Connection-state model, response/session correlation, fail-safe status | FR-016, FR-018, FR-021; HW-REQ-003, HW-REQ-004 |

## 4. Safety requirements and controls

- Communicate unavailable, stale, low-quality, or uncertain results.
- Never claim guaranteed safe passage or absence of obstacles.
- Preserve user control of capture, cancellation, and audio output.
- Separate AI-generated content from trusted device/application state.
- Review high-severity failure modes before any user evaluation.
- Do not expose participants to uncontrolled traffic or avoidable hazards.
- Provide accessible shutdown/recovery and explain system limitations.
- Maintain incident reporting and a process to disable a capability if unsafe behavior is identified.

Related requirements include FR-001, FR-004, FR-005, FR-009, FR-016–020, NFR-008, NFR-010, and NFR-014.

## 5. Safe evaluation

Begin with offline datasets and controlled indoor scenarios. User evaluation requires accessible informed consent, risk review, safe environment, stop procedures, incident contact, and explicit instruction not to rely on the prototype for mobility decisions. Include lived-experience participants and qualified specialists where appropriate. Participant research must also follow DATA-001 and applicable ethics approvals.

## 6. Incident and change response

Record safety incidents, near misses, misleading outputs, and unexpected behavior with relevant build/model/data/device context while minimizing personal data. Triage promptly; suspend the affected capability when credible unacceptable risk is identified; investigate root cause; implement corrective action; retest; and document release decision. Material model, prompt, dataset, hardware, or workflow changes trigger renewed hazard analysis.

## 7. Residual risk and release

Risk acceptance must be explicit, documented, and owned by an accountable reviewer. Unresolved unacceptable risk blocks release. No risk acceptance may override applicable law or permit misleading safety claims. Release requires evidence that safety controls are implemented and verified, limitations are disclosed, and residual risks are acceptable for the defined intended use.

## 8. Required evidence

Task-specific hazard analysis; usability risk analysis; review records; test results; incident/near-miss process; residual-risk acceptance; controlled evaluation protocol; and release limitations.

## 9. Version history

| Version | Date | Change |
|---|---|---|
| 1.0 | Initial | Initial safety policy and hazard register. |
| 1.1 | 2026-11-06 | Added requirement/test traceability, expanded capture/stale-device hazards, clarified risk-rating process, and strengthened incident/change and release controls. |
