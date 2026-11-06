# Document Control and Change Management

| Attribute | Value |
|---|---|
| Document ID | GOV-001 |
| Version | 1.1 |
| Status | Active documentation process |
| Related | PMP-001, PID-001, SRS-001, RTM-001, VVP-001 |

## 1. Purpose

Establish the authoritative process for controlling project documents, requirements, decisions, and evidence. This process applies to planning, design, implementation, verification, and maintenance. Repository history provides change history but does not replace technical review or approval.

## 2. Document status

Document status is distinct from requirement status and test-evidence status.

- **Draft:** under preparation; not approved for reliance.
- **Under Review:** submitted for review; changes may be requested.
- **Approved:** accepted by the designated approver for the stated scope and purpose.
- **Superseded:** replaced by a newer controlled document; retained for history.
- **Retired:** no longer applicable; retained for audit/history where appropriate.

Terms such as "validation pending", "test execution pending", and "components not selected" are descriptive readiness notes, not document lifecycle states. Use them in the status description or a separate readiness field.

## 3. Requirement lifecycle

Use the following controlled lifecycle values in SRS-001 and RTM-001:

Proposed; Under Review; Approved; Implemented; Verified; Failed; Blocked; Deferred; Retired.

- **Proposed:** candidate requirement, not yet approved.
- **Under Review:** being assessed for need, clarity, feasibility, safety, and testability.
- **Approved:** baselined for the defined scope.
- **Implemented:** implementation evidence exists; verification may still be pending.
- **Verified:** required verification passed with a controlled evidence record.
- **Failed:** verification was executed and did not meet acceptance criteria.
- **Blocked:** progress or verification cannot continue due to a recorded dependency or issue.
- **Deferred:** intentionally moved outside the current approved scope.
- **Retired:** formally removed from applicability with rationale and impact review.

Implemented and Verified are separate states. A requirement must not be marked Verified solely because a demonstration appears successful.

## 4. Verification evidence lifecycle

Use evidence states separately from requirement lifecycle: Not designed; Designed; Ready; Executed-Pass; Executed-Fail; Blocked; Not applicable. A pass requires a dated record identifying the procedure, build/configuration, expected and actual results, evidence, tester, and reviewer.

## 5. Naming and location

Use descriptive lowercase kebab-case filenames under the relevant `docs/` domain. Maintain one authoritative current document per document ID. Link related documents rather than duplicating normative requirements. Document IDs remain stable when filenames or titles change.

## 6. Metadata and versioning

Controlled documents include project, document ID, version, status, owner/preparer, date, related documents, and revision history where appropriate.

- **Major version:** material scope, architecture, or normative change requiring re-baselining.
- **Minor version:** additive requirements, substantive clarification, or controlled refinement that does not invalidate the overall document purpose.
- **Patch version:** editorial correction without change to technical meaning.

The project may refine this scheme through an approved change request.

## 7. Review and approval

Review controlled documents for technical correctness, consistency, completeness, testability, traceability, safety, privacy, accessibility, terminology, links, and unsupported claims.

A requirements baseline requires review of stakeholder need/source, acceptance criteria, verification method, architecture allocation, safety/privacy impact, and scope. Approval authority shall be recorded in the project decision/review record. User-needs claims require appropriate stakeholder evidence; they must not be invented by authors.

## 8. Change requests

Record a unique change-request ID, requester, description, rationale, urgency, affected documents/requirements, safety/privacy/accessibility impact, architecture/interface impact, schedule/resource impact, decision, approver, and verification updates.

Before approval, perform impact analysis across SRS, RTM, architecture, ICD, ADRs, AI/ML plan, hardware, safety, privacy/security, accessibility, VVP, and user documentation as applicable.

## 9. Repository rules

Documentation-only changes are authorized during the current planning phase. Do not add application code, AI implementation, firmware, secrets, private recordings, or unlicensed datasets until the project owner explicitly authorizes a later phase.

Use focused commit messages. Fetch the current file and SHA before updates. Fetch updated files after changes to verify publication. Report only actions and checks supported by tool results. GitHub publication does not imply stakeholder approval, implementation, or test execution.

## 10. Traceability and baseline reviews

Requirement changes update RTM-001 and trigger review of architecture, interfaces, risks, test plans, and affected user documentation. Baseline reviews shall check for orphan requirements, orphan tests, unresolved conflicts, and unapproved assumptions.

## 11. Version history

| Version | Date | Change |
|---|---|---|
| 1.0 | Initial | Initial document-control process. |
| 1.1 | 2026-11-06 | Standardized document, requirement, and evidence status vocabularies; clarified approval, versioning, impact analysis, and repository verification rules. |
