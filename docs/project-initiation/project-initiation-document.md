# Project Initiation Document

| Attribute | Value |
|---|---|
| Project | AI Guardian for Blind People |
| Document ID | PID-001 |
| Version | 1.0 |
| Status | Approved for initiation; scope baseline is provisional |
| Document Type | Project Initiation |
| Repository | TheMShahid/AI-Guardian-for-Blind-People |
| Prepared | 06 November 2026 |
| Owner | Project Owner |
| Technical Documentation | Maintained within the project repository |

---

## 1. Executive Summary

AI Guardian for Blind People is an assistive-technology project intended to explore and develop a practical, accessible system that can provide people who are blind or have low vision with useful environmental information through AI-assisted perception and accessible interaction.

The intended product direction combines three cooperating domains:

1. **User-facing software:** an accessible mobile application and voice-first interface.
2. **AI capabilities:** selected perception and language capabilities, potentially including object recognition, scene description, and text recognition.
3. **Physical device:** a wearable or portable sensing unit, with embedded software and connectivity, subject to feasibility and user evaluation.

The project will proceed through evidence-led stages: user and stakeholder discovery, requirements engineering, architecture, proof-of-concept development, hardware prototyping, integration, verification, and controlled field evaluation.

This document authorizes project initiation and establishes an initial direction. It does not claim that any capability has already been implemented, validated, certified, or proven safe.

## 2. Problem Statement

People who are blind or have low vision may encounter barriers when independently accessing visual information in their surroundings, reading printed or digital text that is not accessible, identifying objects, and obtaining timely environmental context.

Existing assistive methods and technologies address important parts of these needs, but no single proposed feature should be assumed to solve every situation. This project will investigate whether a carefully scoped combination of accessible software, AI-assisted perception, and a portable sensing device can provide useful supplementary information while preserving user control and established mobility practices.

The project must be grounded in the lived experience of blind and low-vision users. Technical novelty alone is not sufficient evidence of user value.

## 3. Vision

Develop a dependable, privacy-conscious, accessible assistive technology platform that helps blind and low-vision users obtain relevant information about selected aspects of their environment through understandable and timely audio interaction.

## 4. Goals and Objectives

### 4.1 Product goals

- Provide an accessible, voice-oriented interaction experience.
- Investigate practical AI support for selected visual-information tasks.
- Explore a portable or wearable device that can capture relevant input.
- Integrate the application, AI services, and device through documented interfaces.
- Design for real-world constraints such as latency, lighting, noise, connectivity, battery life, and hardware cost.
- Evaluate usability and usefulness with blind and low-vision participants under an appropriate, safe evaluation protocol.

### 4.2 Initial measurable objectives

Targets below are to be defined after baseline testing and user research; they are not current performance claims.

| ID | Objective | Measurement approach |
|---|---|---|
| OBJ-01 | Establish validated user needs and priority use cases | Reviewed user-research findings and prioritized requirements |
| OBJ-02 | Deliver an accessible software prototype | Accessibility review and task-based usability evaluation |
| OBJ-03 | Evaluate selected AI perception tasks | Task-specific precision, recall, error analysis, and latency |
| OBJ-04 | Demonstrate device-to-software data flow | Repeatable integration tests and interface logs |
| OBJ-05 | Characterize operational constraints | Battery, thermal, connectivity, response-time, and failure tests |
| OBJ-06 | Assess user-perceived usefulness and trust | Structured feedback and observed task outcomes |
| OBJ-07 | Establish safety controls for each supported use case | Hazard analysis, mitigations, and documented test evidence |

Numeric acceptance thresholds will be set in the requirements and verification plans after feasibility studies and stakeholder input.

## 5. Intended Users and Stakeholders

### 5.1 Primary user groups

- People who are blind.
- People with low vision.
- Users with differing levels of technology familiarity and accessibility needs.

### 5.2 Other stakeholders

- Family members or caregivers, where the user chooses to involve them.
- Orientation and mobility professionals.
- Accessibility specialists.
- Rehabilitation organizations and user advocacy groups.
- Software, AI/ML, and embedded-systems developers.
- Research supervisors, evaluators, and potential deployment partners.

Blind and low-vision users must be treated as design partners, not merely as test subjects. Participation, consent, and data handling must be respectful and voluntary.

## 6. Initial Scope

### 6.1 Candidate in-scope capabilities

The following are candidates for investigation. Prioritization will be finalized through requirements discovery and feasibility assessment.

- Accessible onboarding and settings.
- Voice-first commands and spoken feedback.
- Camera-based capture initiated or controlled by the user.
- Object or selected-item recognition.
- Scene or environment description for bounded scenarios.
- OCR and text reading.
- Audio feedback with controls for verbosity, repetition, and interruption.
- Optional connection to a portable or wearable device.
- Device status, connectivity, and battery feedback.
- Local processing or offline operation where technically feasible and beneficial.
- User-controlled data retention and deletion.

### 6.2 Initial out-of-scope items

Unless later approved through change control, the initial project will not claim or attempt to deliver:

- A certified replacement for a white cane, guide dog, or mobility training.
- Guaranteed obstacle avoidance or collision prevention.
- Autonomous street crossing, traffic-signal interpretation for crossing decisions, or safety-critical route guidance.
- Medical diagnosis or emergency-response guarantees.
- Continuous recording or covert monitoring.
- Unsupervised identification of people or sensitive personal attributes.
- A guarantee that AI descriptions are always correct.

Any future proposal involving safety-critical navigation requires a separate risk assessment, specialist input, and substantially stronger validation.

## 7. High-Level Product Concept

The proposed system is modular:

1. **Input layer:** user command and, where enabled, camera or sensor input.
2. **Perception layer:** image processing and selected AI inference tasks.
3. **Interpretation layer:** converts model outputs into bounded, uncertainty-aware information.
4. **Interaction layer:** accessible application and audio/voice feedback.
5. **Device layer:** embedded controller, camera, selected sensors, power management, and connectivity.
6. **Data and privacy layer:** explicit controls governing capture, processing, transmission, retention, and deletion.

The final allocation of processing between a phone, edge device, and remote service is an open architecture decision. It must be selected based on latency, reliability, privacy, power, cost, and model capability.

## 8. Design Principles

- **User autonomy:** the user initiates, controls, interrupts, and dismisses interactions.
- **Accessibility by design:** screen-reader compatibility, semantic controls, keyboard access where relevant, clear audio interaction, and configurable feedback.
- **Safety-first communication:** distinguish detected information from inference; communicate uncertainty and avoid false assurance.
- **Privacy by default:** minimize collection, avoid unnecessary retention, secure data in transit and at rest, and obtain informed consent.
- **Inclusive co-design:** validate workflows with people with different visual abilities and usage contexts.
- **Graceful degradation:** communicate when the camera, model, network, sensor, or battery is unavailable.
- **Modularity:** separate application, AI, device, and integration responsibilities.
- **Evidence-based claims:** publish only performance claims supported by reproducible evaluation.

## 9. Key Constraints

- Project budget and availability of suitable hardware.
- Compute, memory, thermal, and battery limits of portable devices.
- Camera placement, field of view, motion blur, and lighting variability.
- Background noise and speech-recognition limitations.
- Network availability and the cost of cloud inference.
- Model accuracy, bias, uncertainty, and domain shift.
- Device comfort, weight, durability, maintainability, and repairability.
- Privacy, consent, data protection, and applicable legal requirements.
- Access to representative datasets and permission to use them.
- Availability of blind and low-vision participants and qualified evaluation support.

## 10. Initial Risks and Controls

| Risk ID | Risk | Initial control |
|---|---|---|
| RSK-01 | Incorrect AI output may mislead a user | Bound use cases, communicate uncertainty, provide safe fallback behavior, and evaluate errors |
| RSK-02 | User may interpret the prototype as a mobility-safety device | Clear product messaging; no replacement claims; prohibit unsupported safety-critical guidance |
| RSK-03 | Camera or audio data may expose sensitive information | Explicit capture controls, data minimization, encryption, retention limits, and consent |
| RSK-04 | Cloud or network failure interrupts assistance | Detect connectivity loss and provide clear fallback behavior; assess offline options |
| RSK-05 | Hardware is uncomfortable or impractical | Co-design, ergonomic prototypes, and structured wearability evaluation |
| RSK-06 | Model performance degrades in unfamiliar environments | Diverse evaluation data, scenario testing, confidence handling, and documented limitations |
| RSK-07 | Latency makes feedback unusable | Measure end-to-end latency and optimize processing placement |
| RSK-08 | Battery or thermal limits prevent practical use | Instrumented power and thermal testing under representative workloads |
| RSK-09 | Dataset rights or consent are inadequate | Track dataset provenance, licenses, consent, and permitted use before training |
| RSK-10 | Requirements expand beyond available resources | Prioritize a minimum viable use case and manage changes through documented review |

## 11. Dependencies and Assumptions

### 11.1 Dependencies

- Access to blind and low-vision users or representative stakeholder organizations for discovery and evaluation.
- Suitable development hardware and test devices.
- Lawful access to datasets and model licenses.
- Development tools, version control, and reproducible environments.
- Specialist review for accessibility, safety, privacy, and mobility-related use cases where required.

### 11.2 Initial assumptions

- The product should support both software-only evaluation and a later connected-device prototype.
- A smartphone may be useful for early prototyping because it already provides a camera, compute, audio, and connectivity; this is a working assumption, not a final architecture decision.
- A dedicated wearable or portable device may improve ergonomics or sensing, but its value must be demonstrated.
- The first release should focus on a small number of bounded, lower-risk tasks rather than attempting every possible assistive feature.
- Final user needs, preferred form factor, language support, and interaction patterns remain to be confirmed through discovery.

## 12. Delivery Approach and Initial Milestones

| Phase | Name | Main outputs | Exit condition |
|---|---|---|---|
| P0 | Initiation | Project charter, repository baseline, governance | Initiation baseline reviewed |
| P1 | Discovery and requirements | Stakeholder map, user journeys, prioritized requirements, risk register | Priority use cases and acceptance criteria reviewed |
| P2 | Feasibility and architecture | Technology evaluation, system context, architecture decisions | Architecture and prototype scope approved |
| P3 | Software and AI proof of concept | Accessible app prototype and measured AI task prototypes | Demonstrated bounded use cases with evaluation results |
| P4 | Device prototype | Hardware selection, schematics, enclosure concept, embedded prototype | Bench-tested device and documented limitations |
| P5 | Integration and verification | Integrated prototype, test reports, defect log | Verification criteria met for the selected scope |
| P6 | User evaluation and iteration | Usability findings, safety review, revised requirements | Evaluation reviewed and release decision recorded |
| P7 | Release preparation | Deployment, maintenance, support, and user documentation | Release-readiness review completed |

No calendar commitments are set in this initiation document. Scheduling will follow scope, resource, and feasibility estimates.

## 13. Governance and Change Control

- The project owner is accountable for product direction and final project decisions.
- Technical architecture, implementation, and documentation decisions must be recorded in version-controlled project artifacts.
- Requirements changes must identify the reason, affected components, risks, and verification impact.
- Safety- or privacy-impacting changes require explicit review before implementation.
- Major technology choices must be supported by a decision record that includes alternatives and trade-offs.
- Documents must have an ID, version, status, owner, and revision history where appropriate.
- Unverified assumptions must remain visibly marked as assumptions until validated.

## 14. Initial Success Criteria

The project will be considered to have progressed beyond initiation when:

1. Priority user needs have been gathered and reviewed with relevant stakeholders.
2. A bounded minimum viable use case has been selected.
3. Functional and non-functional requirements have measurable acceptance criteria.
4. A system architecture and major technology decisions have documented rationale.
5. A working prototype demonstrates the selected workflow.
6. AI performance, latency, accessibility, and failure behavior have been measured.
7. Risks and limitations are communicated clearly to users and evaluators.
8. No unsupported claim is made that the system guarantees safe navigation.

## 15. Open Decisions

These decisions are intentionally deferred until discovery and feasibility work:

- Primary initial use case and minimum viable product boundary.
- Target users and initial evaluation context.
- Smartphone-only prototype versus early wearable prototype.
- Final hardware platform, camera, sensors, battery, and enclosure.
- On-device, phone-based, edge, or cloud inference allocation.
- AI models and datasets for each selected task.
- Supported languages and speech interaction strategy.
- Data retention and account model.
- Budget, procurement, and target deployment environment.
- Applicable regulatory, certification, and institutional review requirements.

## 16. Approval and Baseline

This document establishes permission to begin structured discovery, requirements engineering, and feasibility assessment. It does not authorize deployment of a safety-critical product or establish that the proposed system is ready for real-world reliance.

The scope and assumptions in this document must be revised when user research and technical evidence become available.

## 17. Revision History

| Version | Date | Author | Description |
|---|---|---|---|
| 1.0 | 2026-11-06 | Project Documentation | Initial project initiation baseline |
