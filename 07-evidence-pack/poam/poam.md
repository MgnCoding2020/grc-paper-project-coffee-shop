# Plan of Action & Milestones (POA&M)

## Overview
This POA&M documents identified security weaknesses within the coffee shop system environment and outlines remediation actions, responsible parties, and timelines in alignment with NIST SP 800-53 controls.

---

## POA&M Table

| Weakness ID | Control ID | Description | Risk | Corrective Action | Milestones | Owner | Due Date | Status |
|------------|-----------|------------|------|------------------|-----------|------|----------|--------|
| POAM-001 | AC-2 | No account lifecycle management | High | Implement account disable policy | Define policy → Configure system → Audit accounts | IT Manager | 45 days | Open |
| POAM-002 | IA-2 | No MFA for admin access | High | Enforce MFA | Select tool → Configure → Train users | IT Security | 30 days | Open |
| POAM-003 | SC-7 | No network segmentation | High | Segment guest Wi-Fi | Configure VLAN → Apply firewall rules → Test | Network Admin | 60 days | Open |
| POAM-004 | SI-2 | No patch management process | High | Implement patching schedule | Inventory → Schedule → Automate | IT Manager | 30 days | In Progress |
| POAM-005 | AU-2 | Logging not enabled | Moderate | Enable logging | Configure logs → Centralize → Review | IT Security | 45 days | Open |

---

## POA&M Management Process

The POA&M is reviewed bi-weekly to track remediation progress. All corrective actions require validation and supporting evidence prior to closure. Updates include status changes, revised completion dates, and risk adjustments.
