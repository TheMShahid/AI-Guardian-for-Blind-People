# System Architecture

| Attribute | Value |
|---|---|
| Document ID | SYS-ARCH-001 |
| Version | 1.0 |
| Status | Conceptual architecture; validation pending |
| Related | PID-001, SRS-001, ICD-001, ADR-001 |

## 1. Architectural intent
Define a modular assistive system with explicit boundaries between user interaction, perception, orchestration, device integration, and data governance. This is a logical architecture, not a deployment commitment.

## 2. System context
External actors/systems include the blind or low-vision user; optional trusted supporter with user authorization; smartphone OS and accessibility services; optional wearable/portable device; optional remote inference/update service; and maintainers/evaluators under controlled access.

## 3. Logical components
| Component | Responsibility |
|---|---|
| Accessible Client | Voice-first and assistive-technology-compatible interaction |
| Session Orchestrator | Task lifecycle, cancellation, retries, and state |
| Capture Manager | User-authorized image/audio/sensor input and permissions |
| Perception Adapter | Task-specific local or remote AI request/response boundary |
| Result Interpreter | Structured, uncertainty-aware feedback; no unsupported safety conclusions |
| Speech Output | Spoken feedback and playback controls |
| Device Gateway | Pairing, telemetry, and device command boundary |
| Privacy/Data Manager | Consent, retention, deletion, and access policy |
| Diagnostics | Non-sensitive status and failure codes |

## 4. Primary data flow
1. User selects or speaks a task.
2. Client announces state and requests required permission.
3. Capture Manager obtains only input needed for that request.
4. Orchestrator selects an available processing route under policy.
5. Perception Adapter invokes the selected capability.
6. Result Interpreter validates response structure, uncertainty, and task scope.
7. Speech Output presents concise result and limitations.
8. Session closes; retention follows user settings and policy.

## 5. Processing options
| Option | Benefits | Trade-offs |
|---|---|---|
| Phone-local | Lower network dependence; local control | Compute, memory, thermal, battery, model size |
| Remote inference | Larger models; centralized updates | Connectivity, latency, cost, data transfer/privacy |
| Dedicated edge | Dedicated sensing/compute | Weight, heat, battery, cost, maintenance |
| Hybrid | Flexible allocation | Complex orchestration and testing |

Selection requires benchmarks and privacy threat assessment. No option is selected here.

## 6. Trust boundaries
User device/network; mobile app/connected hardware; app/OS permissions; inference adapter/third-party service; user content/diagnostics. Authenticate interactions, validate inputs/outputs, minimize transferred data, and document third-party processing.

## 7. Resilience
Handle denied permissions, camera failure, poor input quality, unavailable model, malformed response, network loss, device disconnection, low battery, overheating, and interrupted speech. Failures must be communicated accessibly; never fabricate results.

## 8. Quality attributes
Accessibility, safety, privacy, reliability, latency, portability, maintainability, observability, and cost are architectural drivers. Quantitative targets await user research and feasibility measurements.

## 9. Validation
Validate with use-case walkthroughs, threat modeling, hazard analysis, interface prototyping, latency/power benchmarks, and user evaluation. Update this document when decisions are evidence-based.
