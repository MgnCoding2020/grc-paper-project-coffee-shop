# Control Matrix
Burn and Churn Coffee

---

## Overiew
This control matrix identifies the security controls implemented by Burn and Churn Coffee to mitigate identified cybersecurity risks. 

Controls are aligned primarily with **NIST SP 800-53 control families** and, where relevant, mapped to **PCI DSS requirements** applicable to payment card environments.

Each control references the policy or procedure responsible for implementing the control and identifies evidence that may be used to demonstrate compliance.

-----

## Control Matrix

| Risk ID | Control ID | Control Description | NIST Family | PCI DSS Mapping | Policy / Control Source | Evidence | Implementation Status | POA&M ID |
| ------- | ---------- | ------------------ | ----------- | --------------- | ----------------------- | -------- | --------------------- | --------- |
| R-01 | AC-2 | User accounts are provisioned and removed according to role-based access control principles | AC – Access Control | Req 7 | Access Management Policy | User account review records | Partial | POAM-001 |
| R-01 | IA-2 | Multi-factor authentication is required for administrative and sensitive accounts | IA – Identification & Authentication | Req 8 | Access Management Policy | Google Workspace MFA configuration | Not Implemented | POAM-002 |
| R-01 | AT-2 | Employees receive guidance on recognizing phishing and suspicious activity | AT – Awareness & Training | Req 12.6 | Acceptable Use Policy | Employee training acknowledgement | Partial | POAM-008 |
| R-02 | AU-2 | Security events such as account changes and login activity are logged where supported | AU – Audit & Accountability | Req 10 | Access Management Policy | System activity logs | Partial | POAM-005 |
| R-02 | IR-4 | Security incidents are managed using a defined incident response lifecycle | IR – Incident Response | Req 12.10 | Incident Response Policy | Incident response documentation | Partial | POAM-007 |
| R-03 | CM-7 | Systems are configured to allow only necessary functionality and approved applications | CM – Configuration Management | Req 2 | Acceptable Use Policy | Device configuration settings | Partial | POAM-009 |
| R-03 | MP-7 | Portable devices containing business access are protected from loss or theft | MP – Media Protection | Req 9 | Access Management Policy | Device management practices | Partial | POAM-009 |
| R-04 | PE-3 | Physical access to POS terminals and network devices is restricted to authorized personnel | PE – Physical & Environmental Protection | Req 9 | Payment Card Data Protection Policy | Store supervision procedures | Partial | POAM-010 |
| R-04 | SI-7 | Systems are monitored for unauthorized modifications or suspicious activity | SI – System & Information Integrity | Req 11 | Incident Response Policy | Security event logs | Partial | POAM-004 |
| R-05 | CP-2 | Incident and operational response planning helps maintain business continuity | CP – Contingency Planning | Req 12 | Incident Response Policy | Incident handling procedures | Partial | POAM-006 |
| R-06 | AC-6 | Privileged access is restricted to authorized personnel only | AC – Access Control | Req 7 | Access Management Policy | Role assignment documentation | Partial | POAM-001 |
| R-07 | SA-9 | Third-party service providers responsible for payment processing maintain their own security controls | SA – System & Services Acquisition | Req 12.8 | Payment Card Data Protection Policy | Vendor security documentation | Implemented | N/A |
| R-08 | SI-3 | Systems are protected against malware and unauthorized software installation | SI – System & Information Integrity | Req 5 | Acceptable Use Policy | Device configuration restrictions | Partial | POAM-004 |
---------------------

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
