# Plan of Action & Milestones (POA&M)

## Overview
This POA&M documents identified security weaknesses within the coffee shop system environment and outlines remediation actions, responsible parties, and timelines in alignment with NIST SP 800-53 controls.

---

## POA&M Table


| POA&M ID | Control ID | Weakness Description | Planned Remediation | Owner | Priority | Status |
|----------|-----------|----------------------|---------------------|--------|----------|--------|
| POAM-001 | IA-2 | MFA not enabled for all users | Enforce MFA for all employee accounts | Vertex IT Support (IT Technician from CR-003) | High | Open |
| POAM-002 | AT-2 | No formal security awareness training | Implement annual security training program | Manager | High | Open |
| POAM-003 | AU-6 | Log review inconsistent, open incidents remain | Establish weekly log review process | Vertex IT Support (IT Technician from CR-003) | Medium | Open |
| POAM-004 | PE-3 | No formal physical inspection process | Implement monthly device inspection checklist | Store Manager | Medium | Open |
| POAM-005 | CP-2 | No documented outage or backup plan | Create basic contingency and recovery plan | Owner | High | Open |
| POAM-006 | SA-9 | Vendor review not formally documented | Establish vendor assessment checklist and review cadence | Owner | Medium | In Progress (process and templates exist; V-001 Toast assessed 2026-10-30, POAM-020; V-004 offboarding record pending, CR-003) |
| POAM-007 | SI-3 | Malware protection not validated across devices | Deploy and verify endpoint protection on all systems | Vertex IT Support (IT Technician from CR-003) | High | Open |
| POAM-008 | SI-7 | No monitoring for unauthorized changes | Implement basic file/system change monitoring | Vertex IT Support (IT Technician from CR-003) | Medium | Open |
| POAM-009 | CM-6 | No documented secure-configuration baseline; vendor default credentials/settings not formally hardened | Define and apply secure configuration baselines for POS terminals and workstations | Vertex IT Support (IT Technician from CR-003) | High | Open |
| POAM-010 | SC-8 | Encryption of cardholder data in transit not documented or verified | Document and validate TLS/strong cryptography for data transmitted over open networks | Vertex IT Support (IT Technician from CR-003) | High | Open |
| POAM-011 | RA-5 | No vulnerability scanning or penetration testing performed | Establish quarterly vulnerability scanning (RA-5) and annual penetration testing (CA-8) | Owner | Medium | Open |
| POAM-012 | SC-28 | Cardholder data-at-rest protection and storage scope not documented | Document data-at-rest handling and scope; apply protection or confirm scope reduction via Toast POS | Owner | Medium | Open |
| POAM-013 | SA-9 | Northwind Payroll (V-002) vendor assessment identified open findings: MFA not enforced on vendor admin access, breach-notification SLA undefined, SOC 2 Type II not provided, data-retention policy undocumented | Remediate access and contractual findings before go-live; obtain SOC 2 Type II and documented data retention within 90 days; per-finding status tracked in the vendor risk lab (VRA-V002:F-01 to F-04) | Owner | High | Open (onboarding paused; F-01 and F-04 overdue) |
| POAM-014 | AC-2, AC-6 | Q1 2026 access review (IAM Access Review Lab) identified open findings: terminated employee's accounts still active (IAM:F-001), shift leader holds unnecessary Toast admin rights (IAM:F-002), inactive vendor account still enabled (IAM:F-003), one user without MFA (IAM:F-004) | Disable the terminated and inactive vendor accounts, reduce the excess admin role and enrol MFA, per the IAM lab's remediation tracker; confirm in the Q4 2026 review. (IAM:F-005 is a completed lab demonstration outside the company's system boundary) | Owner | High | Open (overdue since 2026-04-05; escalated 2026-10-30) |
| POAM-015 | SC-7 | Network segmentation not validated: POS terminals share the business Wi-Fi with the manager laptop, and no formal firewall rules or VLAN enforcement have been verified | Implement the target segmentation required by the Network Security Policy (P-005 §3: separate POS, staff, guest and management segments; default deny between them; documented allow rules) and validate it | Owner | High | Open |
| POAM-016 | PS-4, PS-5 | No joiner/mover/leaver process ties HR changes to account changes: a terminated employee's accounts stayed active (IAM:F-001) and the termination date wasn't recorded; a shift leader kept excess admin rights (IAM:F-002) | Record start, end and role-change dates in people.csv; disable accounts the same day employment ends (P-001 §5.4); review access on every role change; account changes made by the IT Technician from CR-003 | Owner | High | Open |
| POAM-017 | CM-3, CM-4 | Change-control process newly established (2026-10-30); no change has yet completed the full cycle, including post-implementation review | Take CR-001 and CR-003 through post-implementation review (the Q4 2026 access review); review the process after its first use | Owner | Medium | Open |
| POAM-018 | SA-9 | Microsoft 365 (V-003) assessment, approved with conditions: no Conditional Access on Entra ID Free, Microsoft's SOC 2 Type 2 and ISO 27001 reports not yet reviewed, standing admin roles (no PIM), 7-day sign-in log retention, no subscription to subprocessor notices | Enforce per-user MFA on every account before go-live; record the standing-admin risk acceptance; add the within-7-days log export to PR-004; review the audit reports and subscribe to subprocessor notices within 30 days of onboarding; per-finding status tracked in the vendor risk lab (VRA-V003:F-01 to F-05) | Owner | High | Open |
| POAM-019 | CA-5 | The POA&M is stated to be reviewed every two weeks, but no review was recorded between the items' creation and 2026-10-30; remediation of POAM-013 and POAM-014 stalled unnoticed for months | Record every POA&M review in the review log below (date, reviewer, changes); review at least monthly; the Owner signs each review | Owner | High | Open |
| POAM-020 | SA-9 | Toast (V-001), the payment service provider, assessed 2026-10-30 after eight months in use: no PCI DSS Attestation of Compliance or responsibility matrix on file (12.8.4, 12.8.5), the company's own SAQ never completed, no written 12.8.2 acknowledgment on file, SOC 2 Type II not reviewed | Obtain the AOC, responsibility guide and SOC 2 Type II and build the responsibility matrix by 2026-11-30; locate the service agreement by 2026-11-30; confirm the SAQ type and complete the SAQ by 2026-12-31; re-check Toast's PCI status every 12 months; per-finding status tracked in the vendor risk lab (VRA-V001:F-01 to F-04) | Owner | High | Open |


---

## POA&M Management Process

The POA&M is intended to be reviewed bi-weekly to track remediation progress. Until 2026-10-30 no review was recorded (POAM-019); from now on, every review is logged below. All corrective actions require validation and supporting evidence prior to closure. Updates include status changes, revised completion dates, and risk adjustments.

---

## POA&M Review Log

| Date | Reviewer | Outcome |
|---|---|---|
| 2026-10-30 | Program alignment review, reported to Olivia Carter (Owner) | First recorded review. POAM-013 found stalled (Northwind onboarding paused; F-01 and F-04 overdue) and POAM-014 overdue since April (IAM Q1 findings). Both escalated to the Owner, with closure through CR-001, CR-003 and vendor follow-up. Added POAM-019 for the missing reviews |
