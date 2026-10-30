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
| POAM-006 | SA-9 | Vendor review not formally documented | Establish vendor assessment checklist and review cadence | Owner | Medium | Open |
| POAM-007 | SI-3 | Malware protection not validated across devices | Deploy and verify endpoint protection on all systems | Vertex IT Support (IT Technician from CR-003) | High | Open |
| POAM-008 | SI-7 | No monitoring for unauthorized changes | Implement basic file/system change monitoring | Vertex IT Support (IT Technician from CR-003) | Medium | Open |
| POAM-009 | CM-6 | No documented secure-configuration baseline; vendor default credentials/settings not formally hardened | Define and apply secure configuration baselines for POS terminals and workstations | Vertex IT Support (IT Technician from CR-003) | High | Open |
| POAM-010 | SC-8 | Encryption of cardholder data in transit not documented or verified | Document and validate TLS/strong cryptography for data transmitted over open networks | Vertex IT Support (IT Technician from CR-003) | High | Open |
| POAM-011 | RA-5 | No vulnerability scanning or penetration testing performed | Establish quarterly vulnerability scanning (RA-5) and annual penetration testing (CA-8) | Owner | Medium | Open |
| POAM-012 | SC-28 | Cardholder data-at-rest protection and storage scope not documented | Document data-at-rest handling and scope; apply protection or confirm scope reduction via Toast POS | Owner | Medium | Open |
| POAM-013 | SA-9 | Northwind Payroll (V-002) vendor assessment identified open findings: MFA not enforced on vendor admin access, breach-notification SLA undefined, SOC 2 Type II not provided, data-retention policy undocumented | Remediate access and contractual findings before go-live; obtain SOC 2 Type II and documented data retention within 90 days; per-finding status tracked in the vendor risk lab (VRA-V002:F-01 to F-04) | Owner | High | Open |
| POAM-014 | AC-2, AC-6 | Q1 2026 access review (IAM Access Review Lab) identified open findings: terminated employee's accounts still active (IAM:F-001), shift leader holds unnecessary Toast admin rights (IAM:F-002), inactive vendor account still enabled (IAM:F-003), one user without MFA (IAM:F-004) | Disable the terminated and inactive vendor accounts, reduce the excess admin role and enrol MFA, per the IAM lab's remediation tracker; confirm in the Q4 2026 review. (IAM:F-005 is a completed lab demonstration outside the company's system boundary) | Owner | High | Open |
| POAM-015 | SC-7 | Network segmentation not validated: POS terminals share the business Wi-Fi with the manager laptop, and no formal firewall rules or VLAN enforcement have been verified | Implement the target segmentation (separate POS, staff, guest and management segments; default deny between them; documented allow rules) and validate it | Owner | High | Open |


---

## POA&M Management Process

The POA&M is reviewed bi-weekly to track remediation progress. All corrective actions require validation and supporting evidence prior to closure. Updates include status changes, revised completion dates, and risk adjustments.
