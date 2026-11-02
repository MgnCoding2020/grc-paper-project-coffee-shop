# Program Timeline
Burn and Churn Coffee

---

## Purpose

A dated history of the Burn and Churn Coffee security program: policies, reviews, assessments, incidents and changes. Every dated record in the program should fit this timeline. Planned items are marked **Planned** and are dated only when they happen.

---

## Timeline

| Date | Event | Reference |
|---|---|---|
| 2026-02-01 | Security program starts; Access Management and Acceptable Use policies take effect | [P-001](../../04-policies/P-001-access-control.md), [P-002](../../04-policies/P-002-acceptable-use.md) |
| 2026-02 | Incident Response Policy takes effect | [P-003](../../04-policies/P-003-incident-response.md) |
| 2026-02-23 | Access Management Policy reviewed (v1.1) | P-001 |
| 2026-02-25 | Acceptable Use Policy reviewed (v1.1) | P-002 |
| 2026-03 | Payment Card Data Protection Policy and the phishing and account-compromise playbooks take effect | [P-004](../../04-policies/P-004-payment-card-data-protection.md), IRP-001, IRP-002 |
| 2026-03-12 | Incident 001: suspicious login attempt on the Store Manager's Google Workspace account | [Incident log](../../07-evidence-pack/artifacts/monitoring/incident-log.md) |
| 2026-03-20 | Incident 002: inactive Toast POS account still enabled | Incident log |
| 2026-03-25 | Q1 2026 quarterly access review completed; findings IAM:F-001 to IAM:F-005 | [IAM Access Review Lab](https://github.com/MgnCoding2020/IAM-Access-Review-Lab) |
| 2026-03-31 to 2026-04-05 | Target dates for Q1 remediation | IAM remediation tracker |
| 2026-06-23 | Northwind Payroll Services (V-002) assessed: approved with conditions; findings VRA-V002:F-01 to F-04, rolled up as POAM-013 | [Vendor Risk Assessment Lab](https://github.com/MgnCoding2020/Vendor-Risk-Assessment-Lab) |
| 2026-10-29 | Internal program alignment review begins: cross-repository findings AL-01 onward; baseline tagged `v1-pre-alignment` | `CLAUDE.md` |
| 2026-10-30 | Alignment review status checks: Q1 access findings overdue since April (POAM-014); Northwind onboarding paused with pre-go-live conditions open (POAM-013); no POA&M review recorded since creation (POAM-019, new control CA-5). All escalated to the Owner | [POA&M review log](../../07-evidence-pack/poam/poam.md) |
| 2026-10-30 | Toast (V-001) assessed for the first time, eight months after go-live: 18/18 High; continue with conditions; findings VRA-V001:F-01 to F-04, rolled up as POAM-020 | [Vendor Risk Assessment Lab](https://github.com/MgnCoding2020/Vendor-Risk-Assessment-Lab/tree/main/assessments/V-001-toast) |
| 2026-10-30 | Microsoft (V-003) assessed before onboarding: High inherent risk, approved with conditions; findings VRA-V003:F-01 to F-05, rolled up as POAM-018 | [Vendor Risk Assessment Lab](https://github.com/MgnCoding2020/Vendor-Risk-Assessment-Lab/tree/main/assessments/V-003-microsoft) |
| 2026-10-30 | CR-004 approved: time-limited guest access for Northwind's payroll contact (VC-001), blocked until Northwind confirms MFA (VRA-V002:F-02) and SharePoint is live | [CR-004](../../09-change-management/CR-004-vendor-guest-access.md) |
| 2026-11-02 | Physical Security Policy (P-011) and Device Configuration Baselines (PR-015) take effect; PE-2 and PE-8 added; CM-6 moves to Partially Implemented | [P-011](../../04-policies/P-011-physical-security.md) |
| 2026-11-02 | Records Retention and Disposal Policy (P-010) and Risk Acceptance and Exception Procedure (PR-014) take effect; six exceptions approved into the new register; SI-12, MP-6 and RA-7 added | [risk-exceptions.md](../../02-risk-management/risk-exceptions.md) |
| 2026-11-02 | Third-Party Risk Management Policy (P-008) and Personnel Security Policy (P-009) take effect; PS-3 and PS-6 added | [04-policies/](../../04-policies/) |
| 2026-11-01 | Mobile Device and Personal Phone Policy (P-007) and Microsoft 365 tenant baseline (PR-013) written for the cutover; AC-19 added | [P-007](../../04-policies/P-007-mobile-devices.md) |
| 2026-11-01 | Espresso machine service company (V-011) assessed: Moderate, continue with conditions | [Vendor Risk Assessment Lab](https://github.com/MgnCoding2020/Vendor-Risk-Assessment-Lab/tree/main/assessments/V-011-espresso-service) |
| 2026-11-01 | Incident Response Policy v1.2 mapped to NIST CSF 2.0 (SP 800-61 Rev. 3); playbooks IRP-005 (malware and ransomware), IRP-006 (vendor breach) and IRP-007 (payment and payroll fraud); IR-4 and IR-8 added | [06-incident-playbooks/](../../06-incident-playbooks/) |
| 2026-11-01 | Backup and Recovery Procedure (PR-012): monthly encrypted offline copies, quarterly restore tests; CP-9 and CP-10 added. First program monitor run (issue #30) | [PR-012](../../05-procedures/PR-012-backup-and-recovery.md) |
| 2026-11-01 | Monthly program monitor added (GitHub Actions): consistency checker plus due-date report across all three repos, opened as a monthly issue; CA-7 added | [monthly-monitor.yml](../../.github/workflows/monthly-monitor.yml) |
| 2026-11-01 | Connected devices brought into the program: cameras, espresso machine, temperature sensors and speaker registered (PR-011); Devices segment added to P-005 (v1.1); MA-4 and PE-6 added | [PR-011](../../05-procedures/PR-011-connected-devices.md) |
| 2026-11-01 | IT Operations Policy (P-006), patch procedure v2.0 (PR-002) and equipment lifecycle procedure (PR-010) take effect; equipment register and maintenance log created; SI-2, CM-8, MA-2, MA-5, SA-22 added | [P-006](../../04-policies/P-006-it-operations.md) |
| 2026-10-30 | CR-005 approved: replace Toast POS once the website's register passes acceptance testing (blocked on CR-002); Toast stays in use until cutover | [CR-005](../../09-change-management/CR-005-toast-pos-replacement.md) |
| 2026-10-30 | IT administration and coverage (PR-008) and shared credential management (PR-009) take effect; CR-003 scope amended (10 hours a week, Owner as backup administrator, password manager); IA-5 added | [05-procedures/](../../05-procedures/) |
| 2026-10-30 | Contingency and outage plan (PR-005), POS device inspection procedure (PR-006) and security awareness training program (PR-007) take effect; CP-2 moves to Partially Implemented | [05-procedures/](../../05-procedures/) |
| 2026-10-30 | Network Security Policy (P-005) takes effect, with the current POS segmentation gap recorded as a time-limited exception (POAM-015); P-001 and P-002 v1.2 point to documents that exist | [P-005](../../04-policies/P-005-network-security.md) |
| 2026-10-30 | Change-control process established; CR-001 and CR-003 raised and approved by the Owner | [Change register](../../09-change-management/README.md) |
| 2026-11-15 | **Planned:** CR-001 migration from Google Workspace to Microsoft 365 (QuickBooks retired into an Excel workbook in SharePoint) | [CR-001](../../09-change-management/CR-001-google-workspace-to-microsoft-365.md) |
| 2026-11-15 | **Planned:** CR-003 IT brought in-house: IT Technician hired, Vertex IT Support offboarded | [CR-003](../../09-change-management/CR-003-it-support-in-house.md) |
| 2026 Q4 | **Planned:** Q4 2026 access review, the first run in Microsoft Entra ID | IAM Access Review Lab |

---

*This document is a simulation for educational and portfolio purposes only.*
