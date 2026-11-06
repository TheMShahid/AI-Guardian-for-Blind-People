# Architecture Decision Records

| Attribute | Value |
|---|---|
| Document ID | ADR-REG-001 |
| Version | 1.1 |
| Status | Initial decisions and open questions |
| Related | PID-001, SYS-ARCH-001, ICD-001, AIML-001, HW-001, SEC-001 |

## 1. Purpose

This document is the controlled register containing individual Architecture Decision Records (ADRs). The register identifier (ADR-REG-001) is distinct from the identifiers assigned to individual decisions (ADR-001, ADR-002, and so on).

Each decision records its status, context, decision, and consequences. Material decisions should also record alternatives, evaluation criteria, evidence, decision owner, and review date.

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

## 2. Open decisions

Mobile framework/platforms; local/cloud inference allocation; hardware compute/camera/sensors/power/enclosure; communication protocol; authentication; language/speech stack; storage/hosting jurisdiction; legal and certification obligations.

Each future decision should include alternatives, evaluation criteria, supporting evidence, owner, status, and review date.

## 3. Revision history

| Version | Date | Description |
|---|---|---|
| 1.0 | 2026-11-06 | Initial architecture decision register |
| 1.1 | 2026-11-06 | Distinguished register ID from individual ADR IDs |
