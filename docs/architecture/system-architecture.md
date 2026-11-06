# System Architecture

| Attribute | Value |
|---|---|
| Document ID | SYS-ARCH-001 |
| Version | 1.1 |
| Status | Refined logical architecture; design validation pending |
| Related | PID-001, SRS-001, RTM-001, ADR-REG-001, ICD-001, SAF-001, SEC-001, ACC-001, HW-001, VVP-001 |

## 1. Architectural intent and status

Define a modular assistive system with explicit boundaries between user interaction, task orchestration, capture, AI perception, result interpretation, device integration, and data governance. This is a logical architecture, not a deployment or technology selection. Component boundaries are proposed and require validation against approved use cases and feasibility evidence.

## 2. System context

External actors/systems include:
- Blind or low-vision user.
- Optional trusted supporter, only within user-authorized scope.
- Smartphone OS, camera/microphone permissions, and accessibility services.
- Optional portable/wearable sensing device.
- Optional remote inference or update service.
- Maintainers/evaluators with controlled access to non-sensitive diagnostics.

The product is supplementary informational assistance and shall not be treated as a certified mobility aid or guarantee of safe navigation.

## 3. Logical components and requirement allocation

| Component | Responsibility | Primary requirement allocation |
|---|---|---|
| Accessible Client (UI) | Voice-first and assistive-technology-compatible interaction, task selection, state and settings | FR-001–003, FR-005–008, FR-015, FR-020, FR-022–027; NFR-001–003, NFR-009, NFR-011 |
| Session Orchestrator (ORCH) | Session lifecycle, cancellation, retry, correlation, freshness, routing and state | FR-002–006, FR-016–018, FR-025; NFR-004, NFR-008 |
| Capture Manager (CAP) | User-authorized image/audio/sensor input, permission checks, capture lifecycle | FR-007–009, FR-014, FR-016, FR-027 |
| Perception Adapter (AI) | Task-specific local/remote AI request-response boundary | FR-010, FR-012–013, FR-016, FR-018–019; NFR-004, NFR-010, NFR-013 |
| Result Interpreter (RES) | Response validation, uncertainty, task scope, limitations and freshness checks | FR-010–013, FR-018–020; NFR-010, NFR-014 |
| Speech Output (TTS) | Spoken feedback, interruption, replay, supported speech preferences | FR-005–006, FR-011, FR-015; NFR-001, NFR-003, NFR-011 |
| Device Gateway (DEV) | Pairing, telemetry, supported device commands and compatibility | FR-016–017, FR-021; NFR-005, NFR-008, NFR-013–014 |
| Privacy/Data Manager (DATA) | Consent, retention, deletion, access policy and data minimization | FR-007–009, FR-022–027; NFR-005–007 |
| Diagnostics (DIAG) | Non-sensitive health, failure codes and operational status | FR-006, FR-016–017, FR-028; NFR-007, NFR-012 |

Requirement allocation is logical; it does not imply implementation or approval. RTM-001 is the detailed traceability authority.

## 4. Primary session/data flow

1. User selects or speaks a supported task.
2. UI announces task and session state.
3. CAP checks the permission and consent policy; capture starts only after the required user action.
4. ORCH creates a correlated session and selects an available processing route under policy.
5. AI adapter sends only task-authorized input to the selected capability.
6. RES validates response schema, request/session identity, freshness, uncertainty, and task scope.
7. TTS presents a concise accessible result, limitation, or actionable failure.
8. ORCH closes/cancels the session; DATA applies the selected retention policy; DIAG records only non-sensitive diagnostics.

Late, stale, malformed, mismatched, or cancelled-session results must not be announced as current results.

## 5. Processing allocation options

| Option | Benefits | Trade-offs / evidence needed |
|---|---|---|
| Phone-local | Reduced network dependency; local control | Compute, memory, thermal, battery, model size and platform support |
| Remote inference | Potentially larger models and centralized updates | Connectivity, latency, cost, data transfer, provider retention and privacy |
| Dedicated edge | Dedicated sensing/compute | Weight, heat, battery, cost, maintenance and safety |
| Hybrid | Flexible task allocation | Complex orchestration, consistency, failure handling and testing |

No option is selected. Selection requires task benchmarks, privacy threat assessment, cost analysis, and hardware feasibility evidence. The default architecture shall not assume cloud processing or continuous capture.

## 6. Trust boundaries and security

Trust boundaries include user device/network; mobile app/OS permissions; app/connected hardware; app/inference adapter/third-party service; user content/diagnostics; and maintainer access. Authenticate and authorize interactions, validate inputs/outputs, minimize transferred data, protect secrets, and document third-party processing. See SEC-001 and ICD-001.

## 7. Resilience and safe failure

Handle denied permissions, camera/microphone failure, poor input quality, unavailable model, malformed or stale response, network loss, device disconnection, low battery, overheating, process interruption, and interrupted speech. Failures must be communicated accessibly; no component may fabricate a result or convert uncertainty into a safety instruction. See FR-016–019 and NFR-008.

## 8. Quality attributes

Accessibility, safety, privacy, reliability, latency, portability, maintainability, observability, energy use, and cost are architectural drivers. Quantitative targets await user research and feasibility measurements. Each release shall document supported platforms, device configurations, and known limitations.

## 9. Interface and decision control

Logical interfaces IF-001 through IF-008 are defined in ICD-001. Protocols, schemas, endpoints, deployment topology, model selection, and hardware remain open decisions. Material choices require an ADR in ADR-REG-001 with alternatives, evidence, consequences, and status.

## 10. Validation plan

Validate through use-case walkthroughs, requirements/architecture reviews, threat modeling, hazard analysis, interface contract tests, accessibility prototyping, latency/power benchmarks, fault injection, and consented user evaluation. Update architecture only when decisions are evidence-based.

## 11. Version history

| Version | Date | Change |
|---|---|---|
| 1.0 | Initial | Initial conceptual component architecture and data flow. |
| 1.1 | 2026-11-06 | Added SRS allocation, interface references, session freshness/cancellation semantics, trust-boundary controls, and explicit architecture decision gates. |
