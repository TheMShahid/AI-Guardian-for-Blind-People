# Hardware Requirements and Prototype Plan

| Attribute | Value |
|---|---|
| Document ID | HW-001 |
| Version | 1.1 |
| Status | Refined preliminary requirements; components and form factor not selected |
| Related | PID-001, SYS-ARCH-001, ICD-001, RTM-001, SAF-001, SEC-001, VVP-001 |

## 1. Purpose and status

Define candidate device needs and a safe evaluation approach for a future portable/wearable prototype. No final bill of materials, board, sensor, enclosure, or form factor is approved. Requirements below are proposed pending user-needs validation and feasibility review.

## 2. Product concept and boundary

A portable sensing accessory may capture user-requested visual input and communicate with an accessible phone application. The phone may initially handle interaction, speech, connectivity, privacy controls, and some processing. Dedicated compute remains a feasibility question.

The device is supplementary informational assistance, not a mobility aid. It shall not provide or imply guaranteed obstacle avoidance or autonomous street-crossing decisions.

## 3. Candidate subsystems and selection criteria

| Subsystem | Candidate function | Selection criteria |
|---|---|---|
| Camera | Capture still images or selected frames | Field of view, focus, low-light behavior, privacy indicator, mounting stability |
| Compute/controller | Sensor control and possible local inference | Performance, RAM, power, thermal, software support, lifecycle |
| Microphone | Voice commands where needed | Noise handling, placement, user control, privacy |
| Audio output | Feedback through phone/earpiece/device | Intelligibility, user preference, environmental awareness |
| Connectivity | Link device and phone | Reliability, range, security, interoperability, power |
| Battery/power | Portable operation | Runtime, charging safety, replaceability, thermal, protection |
| Optional sensors | Orientation/proximity context only if justified | Defined user need, accuracy, calibration, safety relevance, power |

No sensor shall be added without a defined user need, traceable requirement, and testable acceptance criterion.

## 4. Preliminary hardware requirements

All requirements are **Proposed**. Verification is planned; no hardware test has been executed.

| ID | Requirement | Priority | Source | Verification | Acceptance criterion |
|---|---|---:|---|---|---|
| HW-REQ-001 | The device shall clearly indicate when capture is active. | P0 | PRIV, SAF | Inspection, test | In every capture mode, the active state is perceivable through the approved accessible indication method and is correctly synchronized with capture state. |
| HW-REQ-002 | The device shall not record continuously by default. | P0 | PRIV, SAF | Test | Power-on and idle tests show no capture until the approved user-initiated workflow is activated. |
| HW-REQ-003 | The device shall expose battery and connection status where supported by selected hardware. | P1 | OPS, UN | Test | Status values are reported accurately for normal, low-battery, disconnected, and fault conditions supported by the selected components. |
| HW-REQ-004 | The device shall communicate connection loss and support a defined safe recovery behavior. | P0 | SAF, OPS | Test | Disconnect tests produce a detectable state transition; no stale device state is represented as current; recovery follows the approved pairing policy. |
| HW-REQ-005 | The enclosure shall avoid sharp edges and foreseeable snagging hazards in the intended wearing/handling configuration. | P0 | SAF | Inspection, analysis | Design inspection identifies no exposed sharp edges or foreseeable snag points in the evaluated configuration; residual risks are documented. |
| HW-REQ-006 | Device temperature and charging behavior shall remain within the selected component manufacturers' specified operating limits. | P0 | SAF, OPS | Measurement, inspection | Instrumented tests under defined worst-case conditions remain within documented component limits; charging protections are verified. |
| HW-REQ-007 | Camera placement and device comfort shall be evaluated with intended users before selecting a form factor. | P1 | UN, ACC | User evaluation | Evaluation records placement, field of view, comfort, stability, privacy, and mobility-aid interference feedback; unresolved critical concerns block selection. |
| HW-REQ-008 | The device shall provide an accessible power-off/reset method appropriate to the selected form factor. | P0 | SAF, ACC | Test, demonstration | Intended users can locate and operate shutdown/reset using the approved method; shutdown reaches the documented safe state. |
| HW-REQ-009 | Device pairing and commands shall use an approved security mechanism and reject unauthorized control. | P0 | PRIV, SEC | Security test | Unauthorized pairing/commands are rejected in the defined test cases; authorized pairing and revocation behavior are recorded. |
| HW-REQ-010 | The prototype shall be visibly or accessibly identified as experimental and not a certified mobility aid. | P0 | SAF | Inspection | Prototype labeling and onboarding clearly communicate experimental status and mobility-safety limitations. |

## 5. Form-factor evaluation

Compare phone-only, clip-on, chest-mounted, glasses-mounted, and handheld concepts by comfort, stability, field of view, weight, battery, repairability, privacy, cost, environmental audio awareness, accessibility of controls, and interference with established mobility aids. Select only after evidence-based trade study and user feedback.

## 6. Prototype stages

1. Bench-test candidate camera, compute, power, and connectivity components.
2. Demonstrate phone-connected data flow in a controlled environment.
3. Create a non-production enclosure mock-up and assess ergonomics.
4. Test runtime, thermal behavior, disconnection, charging, shutdown, and durability.
5. Conduct supervised, consented user evaluation only after risk review and approved safety protocol.

No stage shall involve reliance on the prototype for navigation or road-crossing decisions.

## 7. Safety and privacy constraints

Do not obstruct normal vision, hearing, or established mobility aids. Avoid unsafe attachments. Capture shall be user-initiated and indicated. No road-crossing or obstacle-avoidance reliance during prototype tests. Provide and test rapid shutdown. Consider bystander privacy, camera direction, visible capture indication, and secure pairing.

## 8. Procurement and trade study

Final components require a trade study covering availability, total cost, power, performance, maintainability, support lifecycle, compatibility, repairability, licensing, security updates, and safety. Record rejected alternatives and rationale in an ADR where the choice is architecturally significant. No specific board or sensor is selected here.

## 9. Verification and traceability

Hardware requirements are mapped to needs, software dependencies, and planned verification in RTM-001. Detailed hardware test procedures shall be added to VVP-001 after component selection. Use component datasheets and approved test fixtures; do not invent electrical, thermal, charging, or battery limits.

## 10. Version history

| Version | Date | Change |
|---|---|---|
| 1.0 | Initial | Preliminary subsystem concept and hardware requirement list. |
| 1.1 | 2026-11-06 | Added priority, source, objective acceptance criteria, safety/privacy constraints, traceability, and verification planning; retained component/form-factor decisions as open. |
