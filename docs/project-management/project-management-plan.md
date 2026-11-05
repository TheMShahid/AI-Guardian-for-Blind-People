# Project Management Plan

| Attribute | Value |
|---|---|
| Document ID | PMP-001 |
| Version | 1.0 |
| Status | Initial planning baseline |
| Related | PID-001, SRS-001, SYS-ARCH-001 |

## 1. Purpose
Define governance, planning, reviews, change control, and quality management for the project. This plan governs future engineering work but does not authorize implementation or deployment by itself.

## 2. Delivery principles
- User needs and evidence take priority over feature count.
- Deliver in reviewable phases with explicit exit criteria.
- Treat software, AI, hardware, safety, privacy, and accessibility as one system.
- Every requirement needs a source, priority, verification method, and status.
- Record major technical decisions and changes.
- Publish no safety or performance claim without supporting evidence.

## 3. Responsibilities
| Role | Accountability |
|---|---|
| Project Owner | Product direction, priorities, resources, major scope acceptance |
| Technical Lead | System integrity, architecture, integration strategy |
| Requirements/Documentation Lead | Document control, traceability, consistency |
| AI/ML Lead | Dataset governance, model evaluation, limitations |
| Hardware/Embedded Lead | Component feasibility, power, thermal, enclosure |
| Accessibility/User Research Lead | Inclusive research and accessibility evaluation |
| Safety/Privacy Reviewer | Hazard, security, and privacy review |
| QA/Test Lead | Verification strategy, test evidence, defect management |

One person may perform multiple roles during early stages, but responsibilities remain explicit. Specialist review is required where risk warrants it.

## 4. Lifecycle gates
| Gate | Phase | Required evidence |
|---|---|---|
| G0 | Initiation | PID-001 and repository baseline |
| G1 | Discovery | User research, use cases, prioritized requirements |
| G2 | Architecture | Architecture, interfaces, ADRs, risk review |
| G3 | Feasibility | AI benchmarks, hardware trade study, acceptance criteria |
| G4 | Prototype integration | Integration evidence, accessibility review, hazard controls |
| G5 | Evaluation | User findings, defect disposition, updated risk register |
| G6 | Release decision | Release checklist, operational docs, known limitations, approval |

A gate requires reviewed evidence, not merely document existence.

## 5. Planning and prioritization
Prioritize by user impact, risk reduction, feasibility, dependency, and cost. Begin with a small number of bounded, lower-risk tasks. Safety-critical navigation is excluded from the initial scope.

## 6. Change control
Significant changes record rationale, affected requirements/documents/components, safety/privacy/accessibility impact, cost/schedule impact, decision, approver, and verification updates. Safety- or privacy-impacting changes require review before acceptance.

## 7. Quality management
Review for correctness, consistency, testability, traceability, accessibility, safety, privacy, and unsupported claims. Track defects with severity, reproduction evidence, owner, resolution, and regression coverage. Re-verify impacted requirements after changes.

## 8. Constraints and planning assumptions
Schedule, budget, team capacity, procurement, participant availability, and approvals are not baselined. Estimate them after discovery and feasibility work.

## 9. Review cadence
Review this plan at each lifecycle gate and after material changes to scope, risk, ownership, or delivery strategy.
