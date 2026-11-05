# Hardware Requirements and Prototype Plan

| Attribute | Value |
|---|---|
| Document ID | HW-001 |
| Version | 1.0 |
| Status | Preliminary requirements; components not selected |
| Related | PID-001, SYS-ARCH-001, ICD-001, SAF-001 |

## 1. Purpose
Define device needs and a safe evaluation approach for a future portable/wearable prototype. No final bill of materials is approved.

## 2. Product concept
A portable sensing accessory may capture user-requested visual input and communicate with an accessible phone application. The phone may initially handle interaction, audio, connectivity, and some processing. Dedicated compute remains a feasibility question.

## 3. Candidate subsystems
| Subsystem | Function | Selection criteria |
|---|---|---|
| Camera | Capture still images or selected frames | Field of view, focus, low-light behavior, privacy indicator |
| Compute/controller | Sensor control and possible local inference | Performance, RAM, power, thermal, software support |
| Microphone | Voice commands where needed | Noise handling, placement, privacy |
| Audio output | Feedback through phone/earpiece/device | Intelligibility, user preference, environmental awareness |
| Connectivity | Link device and phone | Reliability, range, security, power |
| Battery/power | Portable operation | Runtime, charging safety, replaceability, thermal |
| Optional sensors | Orientation/proximity context if justified | Accuracy, calibration, safety relevance, power |

No sensor should be added without a defined user need and testable requirement.

## 4. Preliminary requirements
| ID | Requirement | Verification |
|---|---|---|
| HW-REQ-001 | Indicate clearly when capture is active. | Inspection/test |
| HW-REQ-002 | Do not record continuously by default. | Test |
| HW-REQ-003 | Expose battery and connection status where supported. | Test |
| HW-REQ-004 | Communicate connection loss and provide safe recovery. | Test |
| HW-REQ-005 | Enclosure shall avoid sharp edges and foreseeable snagging hazards. | Inspection |
| HW-REQ-006 | Temperature and charging shall remain within component limits. | Measurement |
| HW-REQ-007 | Evaluate camera placement and comfort with users. | User evaluation |
| HW-REQ-008 | Provide accessible power-off/reset method. | Test |
| HW-REQ-009 | Use appropriately secured device pairing and commands. | Security test |
| HW-REQ-010 | Label prototype experimental and not a certified mobility aid. | Inspection |

## 5. Form-factor evaluation
Compare phone-only, clip-on, chest-mounted, glasses-mounted, and handheld concepts by comfort, stability, field of view, weight, battery, repairability, privacy, and cost. Select only after user feedback.

## 6. Prototype stages
Bench-test camera/compute/power/connectivity; demonstrate phone-connected data flow; create safe enclosure mock-up; test runtime/thermal/disconnection/durability; conduct supervised evaluation only after risk review and informed consent.

## 7. Safety constraints
Do not obstruct normal vision, hearing, or established mobility aids. Avoid unsafe attachments. No road-crossing or obstacle-avoidance reliance during prototype tests. Provide and test rapid shutdown.

## 8. Procurement
Final components require a trade study covering availability, total cost, power, performance, maintainability, support lifecycle, compatibility, and safety. No specific board or sensor is selected here.
