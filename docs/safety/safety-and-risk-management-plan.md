# Safety and Risk Management Plan

| Attribute | Value |
|---|---|
| Document ID | SAF-001 |
| Version | 1.0 |
| Status | Initial hazard register; specialist review required |
| Related | PID-001, SRS-001, AIML-001, HW-001, VVP-001 |

## 1. Safety policy
This is supplementary assistive technology, not a certified mobility aid or replacement for a white cane, guide dog, mobility training, or human assistance. Initial scope excludes autonomous street crossing and guaranteed obstacle avoidance.

## 2. Hazard analysis
For each hazard record hazardous situation, initiating event, potential harm, severity, likelihood, controls, verification evidence, and residual risk. Ratings require an agreed method and competent review; this initial register does not invent numeric ratings.

## 3. Initial hazard register
| ID | Hazardous situation | Potential harm | Initial control |
|---|---|---|---|
| H-001 | Incorrect object/scene description trusted | User acts on false information | Uncertainty-aware wording, task limits, false-output evaluation |
| H-002 | System fails to detect obstacle | Collision/injury | No obstacle-avoidance guarantee; no mobility direction from model |
| H-003 | Road/traffic context misinterpreted | Unsafe crossing | Explicitly exclude crossing decisions |
| H-004 | Delayed output interpreted as current | Action based on stale information | State/timestamp handling; cancel stale responses |
| H-005 | Camera blocked or poorly positioned | Misleading result | Input-quality checks and retry guidance |
| H-006 | Audio masks environmental sounds | Reduced situational awareness | User-controlled audio; evaluate open-ear options |
| H-007 | Attachment snags or shifts | Discomfort/injury | Ergonomic review and safe mounting |
| H-008 | Battery/device failure | Assistance unexpectedly stops | Low-battery warnings and graceful shutdown |
| H-009 | User assumes AI output is guaranteed | Unsafe reliance | Onboarding, in-context limitations, evaluation |
| H-010 | Bystander content captured | Privacy harm | User-initiated capture, minimization, retention controls |

## 4. Safety requirements
Safety claims need evidence. Communicate unavailable, stale, low-quality, or uncertain results. Never claim guaranteed safe passage. Preserve user control of capture/audio. Review high-severity failure modes before evaluation. Do not expose participants to uncontrolled traffic or avoidable hazards.

## 5. Safe evaluation
Start with offline datasets and controlled indoor scenarios. User evaluation requires informed consent, risk review, safe environment, stop procedures, and no reliance on prototype for mobility decisions. Include lived-experience participants and qualified specialists where appropriate.

## 6. Residual risk and release
Risk acceptance must be explicit and owned. Unresolved unacceptable risk blocks release. A disclaimer alone is not an adequate control.

## 7. Required evidence
Task-specific hazard analysis, usability risk analysis, review minutes, test results, incident process, residual-risk acceptance, and release limitations.
