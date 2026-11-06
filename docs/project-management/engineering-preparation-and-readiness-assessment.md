# Engineering Preparation and Implementation Readiness Assessment

| Attribute | Value |
|---|---|
| Project | AI Guardian for Blind People |
| Document ID | ENG-READY-001 |
| Version | 0.2 |
| Status | Consolidated planning assessment — implementation authorization not granted |
| Document Type | Engineering Readiness and Gap Assessment |
| Related | PID-001, PMP-001, GOV-001, MVP-001, UC-001, SRS-001, RTM-001, SYS-ARCH-001, ADR-REG-001, ICD-001, ICD-MVP-001, AIML-001, HW-001, SAF-001, SEC-001, ACC-001, DATA-001, VVP-001, OPS-001, USER-001 |
| Prepared | 06 November 2026 |

## 1. Executive assessment

The repository contains a broad engineering-planning baseline and a proposed first MVP workflow. The current proposal is a user-initiated smartphone still-image text-reading workflow with OCR and controllable speech output.

**Current conclusion: NOT READY FOR APPLICATION IMPLEMENTATION.**

This is not a rejection of the project. It means the internal planning artifacts are sufficiently developed to support structured review, but several decisions depend on evidence that cannot be responsibly invented by documentation authors: intended-user validation, platform/device feasibility, OCR evaluation, privacy/security assessment of the chosen processing route, and safety/accessibility review.

This document consolidates the remaining work into one readiness register. It does not claim that any user study, specialist review, benchmark, test, legal assessment, or implementation has occurred.

## 2. Product and MVP baseline

### 2.1 Proposed MVP-1

A user opens an accessible mobile application, selects a text-reading task, grants camera permission if needed, explicitly captures one still image, receives OCR output, listens to recognized text, and can stop, replay, retry, or close the session.

### 2.2 Included MVP capabilities

| MVP capability | Primary requirements | Use cases | Planned verification |
|---|---|---|---|
| Accessible entry and supported task selection | FR-001–FR-003 | UC-001 | TC-FR-001–003 |
| Permission explanation and handling | FR-007–FR-008 | UC-002 | TC-FR-007–008 |
| Explicit single still-image capture | FR-009, FR-016 | UC-003 | TC-FR-009, TC-FR-016 |
| OCR with explicit status and uncertainty | FR-010, FR-018–FR-019 | UC-004, UC-007 | TC-FR-010, TC-FR-018–019 |
| Spoken recognized text | FR-011 | UC-004 | TC-FR-011 |
| Stop and replay speech | FR-005, FR-011 | UC-005 | TC-FR-005, TC-FR-011 |
| Cancel, retry, close, and recover | FR-004, FR-006, FR-017 | UC-006–008 | TC-FR-004, TC-FR-006, TC-FR-017 |
| Privacy/capture state and no-default-retention behavior | FR-022, FR-027–028; applicable NFRs | UC-008 | TC-FR-022, TC-FR-027–028; TC-NFR-006–007 |
| Supported speech preferences | FR-015 | UC-009 | TC-FR-015 |

The detailed logical message and lifecycle contract is ICD-MVP-001. UC-001 remains the use-case authority; MVP-001 remains the MVP scope authority; SRS-001 remains the normative candidate software-requirements authority; RTM-001 remains the traceability authority; VVP-001 remains the verification planning authority.

### 2.3 Explicitly outside MVP-1

Object recognition, scene description, continuous capture/listening, autonomous navigation, obstacle avoidance, route/road-crossing decisions, custom wearable hardware, firmware, remote supporter features, cloud history, accounts, emergency response, and model training on user media remain deferred.

A broader product vision must not be confused with the MVP implementation boundary.

## 3. Consolidated engineering deliverables

| Domain | Controlled artifact | Current state | Remaining action |
|---|---|---|---|
| Project initiation | PID-001 | Existing baseline | Reconfirm scope and ownership during review |
| Project management | PMP-001 | Initial plan | Rebaseline schedule/resources after feasibility and scope review |
| Product/MVP | MVP-001 | Proposed 0.2 | Validate user value and workflow |
| User journeys | UC-001 | Proposed 0.2 | Review interaction and terminology with intended users |
| Software requirements | SRS-001 | Candidate 1.2; requirements proposed | Approve only after source, scope, and acceptance review |
| Traceability | RTM-001 | Planned mapping 1.2 | Reconcile final MVP baseline and evidence links |
| Logical architecture | SYS-ARCH-001 | Refined 1.1 | Validate allocation and processing route |
| Architecture decisions | ADR-REG-001 | Open decisions remain | Record evidence-backed choices as ADRs |
| System interfaces | ICD-001 | Logical 1.2 | Retain system-level contract; align with MVP supplement |
| MVP interfaces | ICD-MVP-001 | Proposed 0.1 | Review schemas and platform feasibility before implementation |
| AI/ML strategy | AIML-001 | Evaluation strategy; no model selected | Define OCR benchmark corpus, metrics, language scope, and candidate evaluation |
| Hardware | HW-001 | Preliminary requirements; no components selected | Keep hardware deferred until phone workflow and user need justify it |
| Security/privacy | SEC-001 | Control baseline; threat model pending | Complete data-flow-specific threat model and processor assessment |
| Safety | SAF-001 | Initial hazard register; specialist review required | Review hazards and controls for the actual MVP workflow |
| Accessibility | ACC-001 | Design baseline; user validation pending | Evaluate non-visual task completion with intended users |
| Research/ethics | DATA-001 | Governance plan; approvals pending | Determine whether evaluation is research, obtain applicable approvals/consent |
| Verification | VVP-001 | 42 planned software tests; not executed; 14 MVP-specific draft procedures linked | Complete platform-specific test data, fixtures, thresholds, review, and execution readiness |
| MVP verification procedures | VTP-MVP-001 | Draft 14-case procedure set; not executed | Complete selected-platform details, corpus, fixtures, and review before execution |\n| Operations | OPS-001 | Future model; deployment not selected | Define only after local/remote processing decision |
| User guidance | USER-001 | Conceptual guide only | Create MVP-specific instructions after workflow validation |
| Governance | GOV-001 | Active process | Maintain version, review, change, and evidence controls |

## 4. Critical readiness gates

All gates below are mandatory before implementation scope is frozen. A gate may be closed only with a recorded evidence item or approved decision, not by assumption.

| Gate | Required evidence / exit condition | Current status |
|---|---|---|
| G-01 Product need | Documented intended-user problem, task priority, and MVP value reviewed with blind/low-vision stakeholders | OPEN — no user validation evidence recorded |
| G-02 Interaction/accessibility | Non-visual journey and capture interaction reviewed; screen-reader compatibility assumptions checked | OPEN — design proposal only |
| G-03 MVP baseline | MVP-1 scope and explicit exclusions reviewed and baselined | OPEN — proposed only |
| G-04 Platform feasibility | Supported OS, framework, camera APIs, accessibility services, speech services, and minimum test devices evaluated | OPEN — no platform selected |
| G-05 OCR feasibility | Candidate OCR engines evaluated on a lawful, representative, documented corpus with language/script and failure analysis | OPEN — no engine or benchmark selected |
| G-06 Privacy/data flow | Local/remote processing route, data inventory, consent, retention, deletion, third-party processing, and logging approved | OPEN — route not selected |
| G-07 Security threat model | Trust boundaries, abuse cases, attack surfaces, mitigations, and residual risks reviewed | OPEN — control plan exists; threat model pending |
| G-08 Safety review | MVP hazards, misuse, foreseeable reliance, unsafe outputs, and residual risks reviewed by appropriate reviewer(s) | OPEN — specialist review pending |
| G-09 Requirements baseline | MVP requirements approved, unambiguous, testable, prioritized, and traced | OPEN — proposed requirements |
| G-10 Interface baseline | Capture/OCR/speech contracts and cancellation/freshness/error behavior reviewed against selected platform and engine | OPEN — logical contracts only |
| G-11 Verification readiness | Detailed test procedures, test data, fixtures, expected results, and evidence templates approved | OPEN — test register is planned only |
| G-12 Resource and schedule | People, equipment, budget, dependencies, and schedule baselined | OPEN — no resourced implementation plan |
| G-13 Legal/licensing | OCR/model/library licenses, dataset rights, privacy notices, and applicable legal obligations reviewed | OPEN — no selected dependencies |
| G-14 Implementation authorization | G-01 through G-13 reviewed; residual risks accepted; explicit project-owner authorization recorded | BLOCKED until preceding gates are addressed |

## 5. Technology and architecture decision register

No technology is selected by this assessment. The following decisions require documented alternatives, criteria, evidence, consequences, and approval through ADR-REG-001.

| Decision ID (proposed) | Decision topic | Evidence required | Current position |
|---|---|---|---|
| ADR-TBD-01 | Mobile platform/framework | Accessibility, camera integration, maintainability, developer capability, device coverage, and future portability | Open |
| ADR-TBD-02 | OCR engine and language scope | Representative corpus benchmark, accuracy/error profile, reading order, latency, offline behavior, license | Open |
| ADR-TBD-03 | Processing location | Privacy, connectivity, latency, cost, reliability, provider retention, device compute | Open |
| ADR-TBD-04 | Speech output | Supported platform service, language/voice coverage, interruption/replay, accessibility | Open |
| ADR-TBD-05 | Data storage and retention | Data inventory, cache behavior, deletion verification, backup/provider behavior | Open |
| ADR-TBD-06 | Diagnostics/telemetry | Operational value, data minimization, consent, retention, access control | Open |
| ADR-TBD-07 | Device/hardware path | Validated user need, ergonomics, safety, battery, thermal, weight, cost, repairability | Deferred |
| ADR-TBD-08 | External service security | Identity, authentication, transport, authorization, secret handling, provider terms | Conditional on remote processing |

The proposed evaluation criteria in MVP-001 are a comparison framework, not a result. A weighted score must not be manufactured before comparable evidence exists.

## 6. MVP data lifecycle and privacy checkpoints

| Stage | Data involved | Required control | Evidence to collect |
|---|---|---|---|
| Task selection | Task identifier and session state | Minimize identifiers; no sensitive permission requested prematurely | Permission/state inspection |
| Permission | OS permission state | Purpose explained; denial respected | Permission test records |
| Capture | One still image and transient metadata | Explicit user action; capture indication; scoped access | Capture lifecycle test |
| OCR processing | Image reference; optional language hint | Approved processing route; minimum necessary fields; protected transfer if remote | Data-flow and security review |
| OCR response | Recognized text and quality/status metadata | Treat as untrusted; validate identity, freshness, schema, and content | Interface contract tests |
| Speech | Recognized text passed to TTS | No unintended external sharing; interruptible output | Speech behavior tests |
| Session closure | Transient image/text references | Release references and verify deletion within system control | Storage/cache inspection |
| Diagnostics | Error codes, state transitions, timing | No raw image/audio, credentials, or unnecessary personal data by default | Log inspection |

A claim that media is never retained or transmitted may be made only after the selected platform, OCR engine, operating-system caches, backups, and third-party processing behavior have been verified. The current product intent is no persistent image retention by default; actual behavior is not yet verified.

## 7. AI/OCR evaluation plan for MVP-1

Before selecting an OCR engine:

1. Define the initial language(s), script(s), document/sign types, and operating conditions from validated user need.
2. Obtain lawful, licensed, representative evaluation data. Separate development/tuning data from held-out evaluation data.
3. Record source, license/consent, collection conditions, annotation method, and known dataset bias.
4. Define ground-truth transcription and text-block/reading-order annotation where required.
5. Compare candidates on character/word error measures appropriate to the language, reading-order errors, no-text behavior, failure rate, uncertainty calibration where available, latency, memory, energy, and offline capability.
6. Report results by condition and content type; do not rely only on one aggregate score.
7. Include blank, blurred, rotated, low-light, partial, cluttered, unsupported-language, and out-of-distribution cases.
8. Document model/engine version, configuration, hardware, test corpus, and reproducibility details.
9. Review license, commercial-use terms, security posture, privacy, and update lifecycle.
10. Approve release thresholds only after user need, risk, and benchmark evidence are reviewed.

No accuracy, latency, or confidence threshold is specified here because no validated dataset, candidate engine, or target platform has been selected.

## 8. Safety and misuse controls

The MVP is an information-access prototype, not a mobility aid. The following constraints apply throughout design, testing, and communication:

- Never advise a user to cross a road, enter traffic, step into an unknown area, or rely on the system to confirm a route is clear.
- Never imply that failure to detect text or an object means that the item is absent.
- Never present OCR output as guaranteed correct or complete.
- Clearly distinguish a successful capture from successful recognition.
- Make uncertainty, partial output, stale output, and dependency failure explicit.
- Preserve user cancellation and speech interruption.
- Do not test by asking participants to navigate, cross roads, or rely on the prototype.
- Conduct evaluation in controlled environments with informed consent and an appropriate safety protocol.
- Keep white cane, guide dog, orientation and mobility training, and human assistance as established independent supports.
- Suspend an affected capability if a serious safety defect or misleading output is identified.

The detailed hazard analysis and risk acceptance process remain governed by SAF-001.

## 9. Accessibility validation plan

Accessibility is a release-blocking property, not a later visual polish task. The MVP evaluation must examine:

- Complete task entry, permission, capture, processing, result, stop/replay, retry, and closure without sight.
- Screen-reader names, roles, states, focus order, announcements, and navigation.
- Clear distinction between capture-ready, capturing, processing, result-ready, speaking, failure, and closed states.
- Interruptibility and predictable speech behavior.
- Non-visual recovery from denied permission, camera failure, unreadable image, OCR failure, and timeout.
- Low-vision presentation where included in the approved scope.
- User comprehension of limitations, uncertainty, and privacy state.
- Comfort and feasibility of holding/aiming the phone without requiring unsafe posture or mobility behavior.

Recruitment, participant characteristics, consent, compensation, accessibility accommodations, and study protocol must be documented and approved before user evaluation. Do not claim user validation from informal assumptions.

## 10. Verification and evidence management

VVP-001 lists 42 planned software test identifiers. VTP-MVP-001 now expands 14 MVP-specific interface scenarios into platform-neutral draft procedures. These procedures are not execution-ready until platform/engine selection, corpus approval, test fixtures, and assurance reviews are complete. No test execution or pass result is claimed.

Before execution, each test record must contain:
- Test ID and requirement revision.
- Purpose and preconditions.
- Device/OS/app/OCR configuration.
- Test data source and rights/consent status.
- Exact steps and expected results.
- Actual results and pass/fail/block status.
- Evidence reference, date, tester, and reviewer.
- Defect or deviation reference.
- Retest and regression linkage where applicable.

Release evidence must include functional, accessibility, OCR quality, performance, reliability, security, privacy, safety, and compatibility results appropriate to the selected MVP. Demonstration alone is not sufficient for verification.

## 11. Implementation authorization checklist

Implementation remains prohibited during the current documentation-only phase. The project may move to implementation planning only after the following checklist is reviewed and explicitly authorized:

- [ ] G-01 to G-13 have evidence or formally accepted dispositions.
- [ ] MVP-1 scope and exclusions are approved.
- [ ] Target platform and development framework are selected through an ADR.
- [ ] OCR engine, language scope, and processing route are selected through evidence and an ADR.
- [ ] Security threat model and privacy/data-flow review are complete.
- [ ] MVP safety review and residual-risk disposition are recorded.
- [ ] Accessibility workflow review has been completed with intended users or a documented staged validation plan approved.
- [ ] SRS-001, RTM-001, ICD-MVP-001, and VVP-001 are baselined consistently.
- [ ] Test procedures and data governance are ready.
- [ ] Schedule, resources, and ownership are recorded.
- [ ] Explicit project-owner authorization to begin implementation is recorded.

A checked item must point to evidence. This checklist is currently not satisfied.

## 12. Current known limitations and unresolved assumptions

- User needs and task priorities have not yet been validated with representative blind/low-vision users.
- The smartphone-only text-reading MVP is a proposal, not a user-approved product decision.
- Mobile platform, framework, device baseline, OCR engine, languages, speech service, and processing location are unselected.
- OCR quality, response time, battery, memory, and thermal performance are unknown.
- Exact data deletion behavior across OS caches, backups, and external providers is unverified.
- Security threat modeling and specialist safety review remain pending.
- VVP-001 contains 42 planned requirement-level test identifiers; VTP-MVP-001 contains 14 draft MVP procedures. None has been executed.
- Hardware remains deferred and no component procurement is authorized by this document.
- Applicable legal, regulatory, and research ethics obligations require jurisdiction- and deployment-specific review.

## 13. Consolidated next work package

The remaining preparation is treated as one coordinated review package rather than a sequence of user-facing micro-steps:

1. Review MVP-001 and UC-001 against intended-user evidence.
2. Resolve platform and OCR feasibility through comparative evaluation.
3. Complete the selected processing route's data-flow, threat, and privacy analysis.
4. Complete MVP-specific hazard and accessibility reviews.
5. Approve the MVP requirement baseline and update RTM traceability.
6. Finalize platform-specific interface details and detailed test procedures.
7. Record architecture decisions, resource estimates, and implementation authorization.

These activities may require external participants, specialist review, test devices, datasets, or legal input. Documentation can prepare and organize them but cannot truthfully substitute for the missing evidence.

## 14. Version history

| Version | Date | Change |
|---|---|---|
| 0.1 | 2026-11-06 | Consolidated product/MVP allocation, engineering deliverables, readiness gates, technology decisions, privacy lifecycle, OCR evaluation, safety/accessibility controls, verification evidence, and implementation authorization criteria. |\n| 0.2 | 2026-11-06 | Updated requirement/interface versions, recorded 14 draft MVP verification procedures, and refined the verification-readiness assessment without claiming test execution. |
