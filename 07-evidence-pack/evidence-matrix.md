# Evidence Matrix 
Burn and Churn Coffee

---

## Overview
This document identifies the evidence artifacts used to demonstrate that security controls within the Burn and Churn Coffee security program are implemented and operating effectively.

The evidence matrix maps controls defined in the **Control Matrix** to the type of documentation or system output that may be used to validate those controls.

Evidence artifacts may include system configuration screenshots, access review documentation, incident reports, device inspection checklists, or vendor documentation.

Example evidence artifacts and templates may be maintained in the **examples** directory within this repository.

---
## Evidence Matrix

| Evidence ID | Control ID | Evidence Description | Source | Validation Method | Status |
|------------|-----------|----------------------|--------|------------------|--------|
| E-01 | AC-2 | User account access review (artifacts/access/user-access-review.csv) | Internal system export | Python script (access_review_check.py) | Valid (shows open findings: POAM-014) |
| E-02 | IA-2 | MFA status report (artifacts/access/mfa-status.csv)) | Google Workspace export | Python script (mfa_review_check.py) | Partial (missing users) |
| E-03 | AC-6 | Privileged account review report | Admin role listing | Python script (privileged_access_review_check.py) | Valid (see IAM:F-002, POAM-014) |
| E-04 | AU-6 | Incident log (artifacts/monitoring/incident-log.md) | Incident tracking log | Python script (incident_log_review_check.py) | Partial (open issues) |
| E-05 | SC-7 | Network segmentation summary (artifacts/network/network-segmentation.md) | Network configuration doc | Manual review | Valid (documents a gap: POAM-015) |
| E-06 | AT-2 | Security awareness training log (artifacts/training/security-training-log.csv) | HR/training records | Manual review | Partial (1 of 20 active staff completed; POAM-002) |
| E-07 | PE-3 | Physical inspection checklist (artifacts/physical/physical-inspection-checklist.csv) | Store inspection log | Manual review | Partial (one inspection recorded, 2026-02-01, with an unresolved issue; procedure PR-006 and device list added 2026-10-30) |
| E-08 | CP-2 | Contingency and outage plan (05-procedures/PR-005-contingency-plan.md) | Plan document | Manual review; tabletop exercise | Partial (documented 2026-10-30; not tested) |
| E-09 | SA-9 | Vendor assessment checklist (artifacts/vendor/vendor-assessment-summary.md) (Toast POS) | Vendor review doc | Manual review | Partial |
| E-10 | SI-3 | Antivirus / endpoint protection status | Device reports | Manual review | Partial |
| E-11 | SI-7 | Change monitoring / integrity logs | System logs | Manual review | Missing |
| E-12 | CM-6 | Secure configuration baseline documentation | Configuration standard | Manual review | Missing |
| E-13 | SC-8 | Encryption-in-transit (TLS) configuration evidence | Vendor/system config | Manual review | Missing |
| E-14 | RA-5 | Vulnerability scan and penetration test reports | Scan tooling output | Manual review | Missing |
| E-15 | SC-28 | Data-at-rest protection / storage scope documentation | Vendor/system config | Manual review | Missing |
| E-16 | CM-3, CM-4 | Change records and change register (09-change-management/) | Change records | Manual review against the change lifecycle | Partial (no change has completed a post-implementation review yet) |
| E-17 | PS-4, PS-5 | Roster with employment status and dates (00-company-profile/org/people.csv) compared with system accounts | HR roster and access review | Consistency checker and quarterly access review | Partial (termination dates not recorded; IAM:F-001) |
| E-18 | CA-5 | POA&M review log (poam/poam.md) | POA&M | Manual review of review dates and outcomes | Partial (first recorded review 2026-10-30) |
| E-19 | IA-5 | Password manager lab test record (artifacts/credentials/vault-test-record.md) | Lab test record with redacted screenshots | Manual review: members, collections, leaver test | Missing (planned with CR-003) |
| E-20 | AC-6 | Signed Privileged User Agreements (template: examples/privileged-user-agreement.md) | Signed form | Manual review: one per admin account holder, renewed yearly | Missing (signed when the IT Technician starts) |

---

## Evidence Review Process 
Evidence supporting security controls should be reviewed periodically to ensure that controls remain effective.

Evidence may be reviewed:
  - During periodic security program reviews
  - Following medium or high-severity incidents
  - During internal or external audits
  - When security controls or systems change
  
The **Business Owner** or designated security administrator is responsible for maintaining and reviewing evidence documentation.

---

## Future Evidence Artifacts
The following example artifacts may be developed to support the controls listed above:
  - Access Review Checklist
  - Incident Report Template
  - POS Device Inspection Checklist
  - Security Training Acknowledgement Form
  - Vendor Security Documentation Summary
  - Privileged User Agreement (created 2026-10-30)

These artifacts may be stored within the **examples** directory under the evidence-pack folder.

----

## Related Documents
  - Risk Register
  - Control Matrix
  - Access Management Policy
  - Acceptable Use Policy
  - Incident Response Policy
  - Payment Card Data Protection Policy

-----

## Plan of Action & Milestones (POA&M)

Gaps identified in evidence and implementation are tracked in the POA&M:

[View POA&M](./poam/poam.md)

The [evidence index](evidence-index.md) lists every evidence artifact across the program's repositories, with dates and verification status.

---

## Revision History

| Date | Change | Reason |
|---|---|---|
| 2026-10-30 | E-01, E-03, E-05 statuses annotated with their POA&M items | Program alignment review (AL-16, AL-19) |
| 2026-10-30 | E-16 and E-17 added | New controls CM-3, CM-4, PS-4, PS-5 |
| 2026-10-30 | E-04 description corrected (the log is markdown, not CSV); E-06 Missing → Partial | The training log exists (rebuilt from the roster in the alignment review); 1 of 20 active staff has completed training |
| 2026-10-30 | E-19 and E-20 added | New control IA-5; admin account agreements (CR-003) |
| 2026-10-30 | E-18 added | New control CA-5 |
| 2026-10-30 | E-08 Missing → Partial; E-07 status detailed | Contingency plan documented; inspection history reviewed |
