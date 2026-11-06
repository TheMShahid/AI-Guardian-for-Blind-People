# Security and Privacy Plan

| Attribute | Value |
|---|---|
| Document ID | SEC-001 |
| Version | 1.1 |
| Status | Refined control baseline; threat model and legal review pending |
| Related | SRS-001, SYS-ARCH-001, ICD-001, RTM-001, DATA-001, SAF-001, VVP-001 |

## 1. Objectives and scope

Protect user autonomy, confidentiality, integrity, availability, and informed control over camera, microphone, optional location, account, device, and diagnostic data. This plan is a control baseline, not a completed threat assessment or legal compliance certification.

## 2. Data minimization and classification

Collect only what the active feature needs. Do not enable continuous capture by default. Prefer transient processing where practical. Exclude raw media and credentials from logs/analytics by default. Separate operational data from optional research/training data.

Before storage or transfer, classify each data category and document purpose, source, collection trigger, processing location, recipient, access roles, retention, deletion, backup behavior, and legal/consent basis. See DATA-001.

## 3. Consent and permissions

Explain each sensitive permission and request it at point of use. Provide an understandable alternative when permission is denied. Product-use consent must not be bundled with research/training consent. Users must be able to stop capture and audio output. Operational recordings shall not be repurposed for model training without separate informed and specific authorization.

## 4. Security controls and requirement mapping

| Area | Minimum control expectation | SRS / verification trace |
|---|---|---|
| Authentication | Secure authentication for accounts and remote services where accounts are in scope | FR-026; TC-FR-026 |
| Authorization | Least privilege; supporter scope explicitly authorized and revocable | FR-026; TC-FR-026 |
| Transport | Current secure transport and authenticated service endpoints | NFR-005; TC-NFR-005 |
| Storage | Platform-appropriate encryption and access restrictions | NFR-006; TC-NFR-006 |
| Secrets | No credentials/API keys in source, logs, or client bundles; use managed secret controls | NFR-007, NFR-012; TC-NFR-007, TC-NFR-012 |
| Device pairing | User-authorized pairing and authenticated commands | FR-021, NFR-005; TC-FR-021, TC-NFR-005 |
| Input validation | Validate media, schema, size, origin, authorization, and response correlation | FR-018, NFR-014; TC-FR-018, TC-NFR-014 |
| Logging | Redact personal data; restrict access and retention | FR-028, NFR-007, NFR-012; TC-FR-028, TC-NFR-007, TC-NFR-012 |
| Dependencies | Track versions, licenses, vulnerabilities, and updates | NFR-009, NFR-012 |
| Updates | Authenticated update and rollback strategy | Operational/security verification before release |

These controls require platform-specific design and verification; this table does not claim implementation.

## 5. Threat scenarios

Threat modeling shall consider unauthorized capture, lost device, stolen phone, malicious paired device, account compromise, insecure network, provider data exposure, prompt/model manipulation, malicious media, dependency compromise, insecure update, privilege escalation, and accidental disclosure through logs/support.

For each threat, record assets, actors, entry points, preconditions, impact, likelihood rationale, controls, residual risk, and verification. Use a recognized threat-modeling method selected during design review; record assumptions and scope.

## 6. Third-party/cloud processing

Before using an external model/API, document provider, processing location, retention, training-use policy, subprocessors, encryption, access controls, contractual terms, incident process, deletion support, and user disclosure. Do not assume provider defaults meet project needs. Obtain privacy/security review before transmitting real user media.

## 7. Privacy lifecycle and deletion

For each data category document purpose, source, storage, access roles, retention, deletion, backup behavior, and whether data leaves the device. Deletion claims must account for local stores, backups, service providers, and legal retention constraints. The user-facing interface shall explain any limits rather than imply complete erasure when that cannot be guaranteed.

## 8. Incident response

Before public release, define severity, containment, investigation, notification obligations, credential rotation, remediation, user communication, evidence preservation, and post-incident review. Maintain a route to suspend an affected service or capability.

## 9. Verification and release gates

Complete threat modeling, permission-flow tests, storage inspection, transport/access-control tests, dependency review, pairing tests, log-redaction checks, deletion tests, and provider assessment. Critical unresolved security/privacy defects block release. Evidence and defects are recorded under VVP-001 and RTM-001.

## 10. Open work

Complete data inventory, threat model, provider assessment, legal review, retention schedule, incident contacts, security acceptance criteria, and backup/deletion analysis before handling real user recordings at scale.

## 11. Version history

| Version | Date | Change |
|---|---|---|
| 1.0 | Initial | Initial security and privacy control baseline. |
| 1.1 | 2026-11-06 | Added SRS/RTM verification traceability, data classification, threat-model scope, third-party processing review, deletion limits, and release gates. |
