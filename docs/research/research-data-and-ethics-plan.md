# Research Data and Ethics Plan

| Attribute | Value |
|---|---|
| Document ID | DATA-001 |
| Version | 1.1 |
| Status | Refined research/data governance plan; approvals pending |
| Related | SRS-001, AIML-001, SEC-001, ACC-001, SAF-001, RTM-001, VVP-001 |

## 1. Purpose and scope

Establish responsible practices for user research, dataset acquisition, annotation, model evaluation, and participant/bystander information. This plan does not constitute ethics approval, legal advice, or authorization to collect participant data.

## 2. Research principles

Respect autonomy, accessibility, dignity, informed consent, confidentiality, fair compensation, and withdrawal rights where applicable. Include blind and low-vision people in decisions affecting them. Avoid extractive practices. Participation shall be voluntary and accessible.

## 3. Participant research and ethics review

Before recruitment, define research questions, eligibility, accessible information sheets, consent process, compensation, foreseeable risks, data collection, retention, withdrawal process, researcher access, and contact details.

Obtain institutional ethics review or other required approvals before research that requires them. Do not assume that a prototype usability session is exempt from institutional or legal review. Participants must be told that the prototype is experimental and must not be relied on for navigation or safety-critical decisions.

## 4. Dataset inventory and provenance

For each dataset/asset record:
- Unique asset/dataset ID, description, source, owner, acquisition date, and provenance.
- License, consent basis, permitted purposes, redistribution restrictions, and attribution requirements.
- Population/environment coverage, collection conditions, annotation protocol, quality checks, and known bias/limitations.
- Sensitive content, bystander content, privacy risk, and any required redaction.
- Storage location, access roles, encryption, retention, deletion, and backup behavior.
- Train/validation/test split, duplicate detection, leakage controls, and version history.

No dataset shall be used until rights and permitted purposes are reviewed and documented.

## 5. Data separation and purpose limitation

Separate participant research data, operational user data, public benchmarks, and model-training data. Access is purpose-limited. Product consent does not imply research or training consent. Operational recordings shall not be repurposed for model training without separate, informed, specific authorization and lawful rights.

## 6. Annotation quality and evaluation integrity

Document label definitions, annotator guidance, quality checks, adjudication, and inter-annotator agreement where appropriate. Preserve uncertainty and ambiguous cases rather than forcing unsupported labels. Keep evaluation data isolated from training/tuning data and prevent leakage. Record dataset and annotation versions with every reported model result.

## 7. Bystander privacy

Images/audio may capture non-consenting people. Minimize capture, avoid unnecessary identification, restrict access, redact where feasible, and define deletion/retention. Do not infer sensitive personal attributes. Research protocols shall explain how incidental bystander information is handled.

## 8. Security, access, and publication

Use access controls, encryption, secure transfer, and approved storage. Never commit private recordings, credentials, participant data, or unlicensed datasets to a public repository. Release data only after rights, privacy, consent, re-identification, and security review. Apply SEC-001 controls.

## 9. Withdrawal, retention, and deletion

Define participant withdrawal conditions and limits before consent. Specify retention periods and deletion procedures for source recordings, annotations, derived data, backups, and third-party processors. Explain when data cannot be withdrawn after anonymization, aggregation, or lawful publication, where applicable. Do not promise deletion beyond actual control.

## 10. Open work and approval gates

Complete data inventory, ethics determination, accessible consent materials, retention schedule, dataset licensing review, annotation protocol, data-access policy, and incident/withdrawal contact process before collecting or using participant data. Complete provider review before sharing data with external AI services.

## 11. Version history

| Version | Date | Change |
|---|---|---|
| 1.0 | Initial | Initial research data and ethics governance plan. |
| 1.1 | 2026-11-06 | Expanded dataset provenance, consent, data separation, annotation integrity, bystander privacy, withdrawal/deletion, and approval gates. |
