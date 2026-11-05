# Architecture Decision Records

| Attribute | Value |
|---|---|
| Document ID | ADR-001 |
| Version | 1.0 |
| Status | Initial decisions and open questions |

## ADR-001 — Separate interaction, AI, and device responsibilities
**Status:** Accepted as a logical design principle  
**Context:** The system spans accessible software, AI perception, and optional hardware.  
**Decision:** Maintain explicit boundaries between client, orchestration, AI adapters, device gateway, and privacy controls.  
**Consequences:** More interface documentation, but components remain independently testable and replaceable.

## ADR-002 — Evaluate phone-first prototyping
**Status:** Provisional; validate after user discovery  
**Context:** A smartphone provides camera, compute, audio, and connectivity; custom hardware adds power, thermal, enclosure, and maintenance complexity.  
**Decision:** Evaluate priority use cases on a phone before committing to custom wearable hardware, unless user research justifies earlier hardware work.  
**Consequences:** Faster early learning; wearability and camera placement remain unvalidated.

## ADR-003 — Exclude safety-critical navigation from initial scope
**Status:** Accepted scope constraint  
**Context:** Perception errors can cause physical harm.  
**Decision:** Initial capabilities are bounded and informational. No autonomous crossing, guaranteed obstacle avoidance, or replacement claims.  
**Consequences:** Reduced initial scope; any future navigation proposal requires specialist review and a separate safety case.

## ADR-004 — Select AI models through task-specific evaluation
**Status:** Accepted  
**Decision:** Define datasets, scenarios, metrics, and acceptance criteria before selecting production models.  
**Consequences:** Model selection is evidence-led and requires benchmarking.

## ADR-005 — Apply privacy by minimization
**Status:** Accepted  
**Decision:** Capture only for user-initiated tasks by default; minimize retention/transmission; separate product consent from optional research/training consent.  
**Consequences:** Some cloud/history features may be constrained; privacy controls are core requirements.

## Open decisions
Mobile framework/platforms; local/cloud inference allocation; hardware compute/camera/sensors/power/enclosure; communication protocol; authentication; language/speech stack; storage/hosting jurisdiction; legal and certification obligations. Each decision needs alternatives, criteria, evidence, owner, and review date.
