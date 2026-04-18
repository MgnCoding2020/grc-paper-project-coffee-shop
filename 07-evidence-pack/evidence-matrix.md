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
| E-01 | AC-2 | User account access review CSV | Internal system export | Python script (access_review_check.py) | Valid |
| E-02 | IA-2 | MFA status report | Google Workspace export | Python script (mfa_review_check.py) | Partial (missing users) |
| E-03 | AC-6 | Privileged account review report | Admin role listing | Python script (privileged_access_review_check.py) | Valid |
| E-04 | AU-6 | Incident log review CSV | Incident tracking log | Python script (incident_log_review_check.py) | Partial (open issues) |
| E-05 | SC-7 | Network segmentation summary | Network configuration doc | Manual review | Valid |
| E-06 | AT-2 | Security awareness training records | HR/training records | Manual review | Missing |
| E-07 | PE-3 | Physical inspection checklist | Store inspection log | Manual review | Partial |
| E-08 | CP-2 | Backup / outage response documentation | Internal documentation | Manual review | Missing |
| E-09 | SA-9 | Vendor assessment checklist (Toast POS) | Vendor review doc | Manual review | Partial |
| E-10 | SI-3 | Antivirus / endpoint protection status | Device reports | Manual review | Partial |
| E-11 | SI-7 | Change monitoring / integrity logs | System logs | Manual review | Missing |

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
