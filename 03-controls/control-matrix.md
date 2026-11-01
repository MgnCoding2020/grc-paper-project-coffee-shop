# Control Matrix
Burn and Churn Coffee

---

## Overview
This control matrix identifies the security controls implemented by Burn and Churn Coffee to mitigate identified cybersecurity risks. 

Controls are aligned primarily with **NIST SP 800-53 control families** and, where relevant, mapped to **PCI DSS requirements** applicable to payment card environments.

Each control references the policy or procedure responsible for implementing the control and identifies evidence that may be used to demonstrate compliance.

-----
## Control Matrix

| Risk ID | Control ID | Control Description | NIST Family | PCI DSS Mapping | Implementation Status | Evidence ID | POA&M ID |
|--------|-----------|---------------------|------------|------------------|----------------------|-------------|----------|
| R-01 | IA-2 | Multi-factor authentication for all user accounts | IA | Req. 8 | Partially Implemented | E-02 | POAM-001 |
| R-01 | AT-2 | Security awareness and phishing training (PR-007) | AT | Req. 12.6 | Not Implemented | E-06 | POAM-002 |
| R-02 | AC-2 | Account management for POS and business systems | AC | Req. 7 | Partially Implemented | E-01 | POAM-014 |
| R-02 | AU-6 | Log review for suspicious POS activity | AU | Req. 10 | Partially Implemented | E-04 | POAM-003 |
| R-02 | CM-6 | Secure configuration baselines for POS and workstations; Microsoft 365 tenant baseline (PR-013) | CM | Req. 2 | Not Implemented | E-12 | POAM-009 |
| R-03 | PE-3 | Physical access control for devices and POS terminals; device inspection (PR-006) | PE | Req. 9 | Partially Implemented | E-07 | POAM-004 |
| R-04 | SC-7 | Network segmentation between POS and internal network (P-005) | SC | Req. 1 | Partially Implemented | E-05 | POAM-015 |
| R-05 | CP-2 | Contingency and outage plan (PR-005) | CP | Req. 12 | Partially Implemented | E-08 | POAM-005 |
| R-19 | CP-9 | System backup: monthly encrypted offline copies in two places; network settings exported after every change; data exported before a vendor account closes (PR-012) | CP | Req. 12.10.1 (data backup processes) | Not Implemented | E-26 | POAM-029 |
| R-19 | CP-10 | System recovery: quarterly restore tests, recovery order and targets, clean-point recovery after an incident (PR-012) | CP | Req. 12.10.1 (business recovery) | Not Implemented | E-26 | POAM-029 |
| R-06 | AC-6 | Least privilege and privileged account review | AC | Req. 7 | Partially Implemented | E-03 | POAM-014 |
| R-21 | AC-19 | Access control for mobile devices: personal phones for Authenticator and viewing only, no company file downloads, same-day reporting of lost phones, security key alternative (P-007) | AC | None (no direct PCI DSS requirement; card data never on phones, P-004) | Not Implemented | E-06 | POAM-031 |
| R-07 | SA-9 | Vendor/service provider management (Toast POS) | SA | Req. 12.8 | Partially Implemented | E-09 | POAM-006 |
| R-08 | SI-3 | Malware protection on business systems | SI | Req. 5 | Partially Implemented | E-10 | POAM-007 |
| R-08 | SI-7 | Monitoring for unauthorized changes | SI | Req. 11 | Not Implemented | E-11 | POAM-008 |
| R-08 | RA-5 | Vulnerability scanning and penetration testing | RA | Req. 11 | Not Implemented | E-14 | POAM-011 |
| R-09 | SC-8 | Encryption of cardholder data in transit (TLS) | SC | Req. 4 | Not Implemented | E-13 | POAM-010 |
| R-09 | SC-28 | Protection of cardholder data at rest | SC | Req. 3 | Not Implemented | E-15 | POAM-012 |
| R-10 | PS-4 | Personnel termination: all access removed when employment ends | PS | Req. 8.2.5 | Partially Implemented | E-17 | POAM-016 |
| R-10 | PS-5 | Personnel transfer: access reviewed and adjusted when a role changes | PS | Req. 7.2 | Not Implemented | E-17 | POAM-016 |
| R-11 | CM-3 | Configuration change control: significant changes documented, approved and reviewed | CM | Req. 6.5.1 | Partially Implemented | E-16 | POAM-017 |
| R-11 | CM-4 | Impact analysis before significant changes | CM | Req. 6.5.1 | Partially Implemented | E-16 | POAM-017 |
| R-13 | IA-5 | Authenticator management: shared admin credentials in a two-member password manager, generated passwords, rotated when anyone who knew them leaves (PR-009) | IA | Req. 8.3, 8.6 (loose) | Not Implemented | E-19 | POAM-021 |
| R-15 | SI-2 | Flaw remediation: critical and high updates within one month, monthly update window, maintenance log (PR-002) | SI | Req. 6.3.3 | Partially Implemented | E-22 | POAM-023 |
| R-15 | CM-8 | System component inventory: equipment register with serials, versions, warranty and support dates (PR-010) | CM | Req. 12.5.1 | Partially Implemented | E-21 | POAM-023 |
| R-16 | MA-2 | Controlled maintenance: planned, recorded and checked repairs and updates (PR-010) | MA | Req. 9.5.1 (loose) | Not Implemented | E-22 | POAM-024 |
| R-16 | MA-5 | Maintenance personnel: technician visits confirmed with the vendor, supervised and logged (PR-010) | MA | Req. 9.5.1.3 | Not Implemented | E-22 | POAM-024 |
| R-15 | SA-22 | Unsupported system components: yearly end-of-support review and replacement plan (PR-010) | SA | Req. 12.3.4 | Not Implemented | E-21 | POAM-025 |
| R-17 | MA-4 | Nonlocal maintenance: vendor remote diagnostics only when requested, named technician, each session logged (PR-011) | MA | Req. 8.2.7 (loose) | Not Implemented | E-23 | POAM-026 |
| R-18 | PE-6 | Monitoring physical access: cameras on entrances and stock room, never on the keypad; owner-approved footage access; 30-day retention (PR-011) | PE | None (no direct PCI DSS requirement) | Not Implemented | E-24 | POAM-027 |
| R-20 | IR-4 | Incident handling: playbooks for each incident type, following the NIST CSF 2.0 functions; incidents logged as INC-### (P-003, IRP-001 to IRP-007) | IR | Req. 12.10.1 | Partially Implemented | E-04 | POAM-030 |
| R-20 | IR-8 | Incident response plan: P-003 and its playbooks, exercised in a yearly tabletop and updated afterwards | IR | Req. 12.10.1, 12.10.2 | Partially Implemented | E-27 | POAM-030 |
| R-12 | CA-5 | Plan of action and milestones: weaknesses tracked, reviewed and driven to closure | CA | None (no direct PCI DSS requirement) | Partially Implemented | E-18 | POAM-019 |
| R-12 | CA-7 | Continuous monitoring: monthly automated program monitor (consistency checker and due-date report) plus the manual activities in the monitoring strategy | CA | None (no direct PCI DSS requirement) | Partially Implemented | E-25 | POAM-028 |

----


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

---

## Revision History

| Date | Change | Reason |
|---|---|---|
| 2026-10-30 | AC-2 and AC-6: Implemented → Partially Implemented (POAM-014); SC-7: Implemented → Partially Implemented (POAM-015) | The Q1 2026 access review left IAM:F-001 to F-004 open, and the network evidence shows POS terminals sharing Wi-Fi with the manager laptop. Found in the program alignment review (AL-16, AL-19) |
| 2026-10-30 | Added PS-4, PS-5, CM-3 and CM-4 (POAM-016, POAM-017) | The Q1 review showed access isn't removed on termination or role change; the change process was created for CR-001 and CR-003 |
| 2026-11-01 | Added AC-19 (POAM-031); CM-6 description adds the tenant baseline (PR-013) | Staff will use personal phones for MFA from the cutover (P-007) |
| 2026-11-01 | Added IR-4 and IR-8 (POAM-030) | Incident playbooks IRP-005 to IRP-007; the plan had never been listed as a control or exercised |
| 2026-11-01 | Added CP-9 and CP-10 (POAM-029) | The shop had no backups of its own; written before the IT Technician role existed (PR-012) |
| 2026-11-01 | Added CA-7 (POAM-028) | Monthly automated program monitor; operational checks are still manual |
| 2026-11-01 | Added MA-4 (POAM-026) and PE-6 (POAM-027) | Connected devices and cameras brought into the program (PR-011) |
| 2026-11-01 | Added SI-2, CM-8, MA-2, MA-5, SA-22 (POAM-023 to POAM-025) | IT Operations Policy (P-006); patching existed only as an undated procedure, with no equipment or maintenance records |
| 2026-10-30 | Added IA-5 (POAM-021) | Shared admin credentials had no managed store, and Vertex knows them (CR-003) |
| 2026-10-30 | Added CA-5 (POAM-019) | The POA&M exists but wasn't reviewed as stated; remediation stalled unnoticed |
| 2026-10-30 | CP-2: Not Implemented → Partially Implemented | Contingency and outage plan documented (PR-005); not yet tested. PE-3 and AT-2 gain procedures (PR-006, PR-007) but keep their ratings until inspections and training actually happen |
