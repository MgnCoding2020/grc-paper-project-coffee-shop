# Control Matrix
Burn and Churn Coffee

---

## Overiew
This control matrix identifies the security controls implemented by Burn and Churn Coffee to mitigate identified cybersecurity risks. 

Controls are aligned primarily with **NIST SP 800-53 control families** and, where relevant, mapped to **PCI DSS requirements** applicable to payment card environments.

Each control references the policy or procedure responsible for implementing the control and identifies evidence that may be used to demonstrate compliance.

-----
## Control Matrix

| Risk ID | Control ID | Control Description | NIST Family | PCI DSS Mapping | Implementation Status | Evidence ID | POA&M ID |
|--------|-----------|---------------------|------------|------------------|----------------------|-------------|----------|
| R-01 | IA-2 | Multi-factor authentication for all user accounts | IA | Req. 8 | Partially Implemented | E-02 | POAM-001 |
| R-01 | AT-2 | Security awareness and phishing training | AT | Req. 12.6 | Not Implemented | E-06 | POAM-002 |
| R-02 | AC-2 | Account management for POS and business systems | AC | Req. 7 | Implemented | E-01 | - |
| R-02 | AU-6 | Log review for suspicious POS activity | AU | Req. 10 | Partially Implemented | E-04 | POAM-003 |
| R-03 | PE-3 | Physical access control for devices and POS terminals | PE | Req. 9 | Partially Implemented | E-07 | POAM-004 |
| R-04 | SC-7 | Network segmentation between POS and internal network | SC | Req. 1 | Implemented | E-05 | - |
| R-05 | CP-2 | Basic contingency planning for network outages | CP | Req. 12 | Not Implemented | E-08 | POAM-005 |
| R-06 | AC-6 | Least privilege and privileged account review | AC | Req. 7 | Implemented | E-03 | - |
| R-07 | SA-9 | Vendor/service provider management (Toast POS) | SA | Req. 12.8 | Partially Implemented | E-09 | POAM-006 |
| R-08 | SI-3 | Malware protection on business systems | SI | Req. 5 | Partially Implemented | E-10 | POAM-007 |
| R-08 | SI-7 | Monitoring for unauthorized changes | SI | Req. 11 | Not Implemented | E-11 | POAM-008 |


## Control Review Process
The control matrix shall be reviewed:
  - Annually
  - Following major system changes
  - After significant security incidents
  - When new risks are identified

Updates to the control matrix must be approved by the **Business Owner**.

----

## Related Documents
  - Risk Register
  - Access Management Policy
  - Acceptable Use Policy
  - Incident Response Policy
  - Payment Card Data Protection Policy

---

## Plan of Action & Milestones (POA&M)

Control deficiencies and partial implementations are tracked in the POA&M:

[View POA&M](../07-evidence-pack/poam/poam.md)
