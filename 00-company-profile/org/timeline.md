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
| 2026-10-30 | Network Security Policy (P-005) takes effect, with the current POS segmentation gap recorded as a time-limited exception (POAM-015); P-001 and P-002 v1.2 point to documents that exist | [P-005](../../04-policies/P-005-network-security.md) |
| 2026-10-30 | Change-control process established; CR-001 and CR-003 raised and approved by the Owner | [Change register](../../09-change-management/README.md) |
| 2026-11-15 | **Planned:** CR-001 migration from Google Workspace to Microsoft 365 (QuickBooks retired into an Excel workbook in SharePoint) | [CR-001](../../09-change-management/CR-001-google-workspace-to-microsoft-365.md) |
| 2026-11-15 | **Planned:** CR-003 IT brought in-house: IT Technician hired, Vertex IT Support offboarded | [CR-003](../../09-change-management/CR-003-it-support-in-house.md) |
| 2026 Q4 | **Planned:** Q4 2026 access review, the first run in Microsoft Entra ID | IAM Access Review Lab |

---

*This document is a simulation for educational and portfolio purposes only.*
