# Document Control and Change Management

| Attribute | Value |
|---|---|
| Document ID | GOV-001 |
| Version | 1.0 |
| Status | Active documentation process |
| Related | PMP-001, PID-001 |

## 1. Document status
Draft = under preparation; Under Review = awaiting review; Approved = accepted for stated scope; Superseded = replaced; Retired = no longer applicable. Approved documents may still contain clearly marked assumptions/open decisions.

## 2. Naming and location
Use descriptive lowercase kebab-case filenames under the relevant docs domain. Maintain one authoritative current document per ID; link related documents rather than duplicating conflicting requirements.

## 3. Metadata
Controlled documents include project, document ID, version, status, owner/preparer, date, related documents, and revision history where appropriate.

## 4. Versioning
Major: material scope/architecture/normative change. Minor: additive requirements or clarifications. Patch: editorial correction without meaning change. Refine this convention as the document set grows.

## 5. Review checklist
Check technical correctness, consistency, completeness, testability, traceability, safety, privacy, accessibility, terminology, links, and unsupported claims. Record reviewers and decisions for significant baselines.

## 6. Change requests
Record ID, requester, description, rationale, urgency, affected documents/requirements, safety/privacy/accessibility impact, implementation impact, decision, approver, and verification updates.

## 7. Repository rules
Documentation-only changes in this phase; do not add application code, AI implementation, firmware, secrets, private recordings, or unlicensed datasets. Use focused commit messages. Verify files by fetching them from GitHub; never report unperformed commits or checks.

## 8. Traceability
Requirement changes update RTM-001 and trigger review of architecture, interfaces, risks, and test plans.
