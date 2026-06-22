# Plan of Action & Milestones (POA&M)

## Overview
This POA&M documents identified security weaknesses within the coffee shop system environment and outlines remediation actions, responsible parties, and timelines in alignment with NIST SP 800-53 controls.

---

## POA&M Table


| POA&M ID | Control ID | Weakness Description | Planned Remediation | Owner | Priority | Status |
|----------|-----------|----------------------|---------------------|--------|----------|--------|
| POAM-001 | IA-2 | MFA not enabled for all users | Enforce MFA for all employee accounts | IT Admin | High | Open |
| POAM-002 | AT-2 | No formal security awareness training | Implement annual security training program | Manager | High | Open |
| POAM-003 | AU-6 | Log review inconsistent, open incidents remain | Establish weekly log review process | IT Admin | Medium | Open |
| POAM-004 | PE-3 | No formal physical inspection process | Implement monthly device inspection checklist | Store Manager | Medium | Open |
| POAM-005 | CP-2 | No documented outage or backup plan | Create basic contingency and recovery plan | Owner | High | Open |
| POAM-006 | SA-9 | Vendor review not formally documented | Establish vendor assessment checklist and review cadence | Owner | Medium | Open |
| POAM-007 | SI-3 | Malware protection not validated across devices | Deploy and verify endpoint protection on all systems | IT Admin | High | Open |
| POAM-008 | SI-7 | No monitoring for unauthorized changes | Implement basic file/system change monitoring | IT Admin | Medium | Open |
| POAM-009 | CM-6 | No documented secure-configuration baseline; vendor default credentials/settings not formally hardened | Define and apply secure configuration baselines for POS terminals and workstations | IT Admin | High | Open |
| POAM-010 | SC-8 | Encryption of cardholder data in transit not documented or verified | Document and validate TLS/strong cryptography for data transmitted over open networks | IT Admin | High | Open |
| POAM-011 | RA-5 | No vulnerability scanning or penetration testing performed | Establish quarterly vulnerability scanning (RA-5) and annual penetration testing (CA-8) | Owner | Medium | Open |
| POAM-012 | SC-28 | Cardholder data-at-rest protection and storage scope not documented | Document data-at-rest handling and scope; apply protection or confirm scope reduction via Toast POS | Owner | Medium | Open |


---

## POA&M Management Process

The POA&M is reviewed bi-weekly to track remediation progress. All corrective actions require validation and supporting evidence prior to closure. Updates include status changes, revised completion dates, and risk adjustments.
