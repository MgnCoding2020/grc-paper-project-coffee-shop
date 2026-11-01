# Continuous Monitoring Strategy

## Purpose
This document defines how the coffee shop maintains ongoing awareness of security control effectiveness and system risk.

## Monitoring Activities

### Access Reviews
- Frequency: Quarterly
- Scope: Microsoft Entra ID (users, groups, admin roles, guests), Toast POS, xtraCHEF, network administration interfaces, the password manager and connected-device portals (from the Q4 2026 review; the Q1 2026 review covered Google Workspace and QuickBooks Online)
- Objective: Identify inactive or unauthorized accounts

### MFA Enforcement
- Frequency: Monthly
- Scope: Administrative and payment systems
- Objective: Ensure MFA remains enabled where required

### System Updates / Patching
- Frequency: Monthly update window (PR-002)
- Scope: POS terminal, computers and tablets, network equipment, connected devices
- Objective: Ensure systems are up to date; every update recorded in the maintenance log

### Incident Monitoring
- Frequency: Ongoing (as events occur)
- Source: User reports, login alerts
- Objective: Detect and respond to suspicious activity

### Network Monitoring
- Frequency: Periodic review
- Scope: Guest vs Internal Wi-Fi
- Objective: Validate segmentation remains in place

### Program Monitor (automated)
- Frequency: Monthly, on the 1st (GitHub Actions: [monthly-monitor.yml](../.github/workflows/monthly-monitor.yml)); also on demand
- Scope: all three repositories
- What it does: runs the [consistency checker](../tools/check_program.py) and the [due-date monitor](../tools/due_dates.py), then opens a "Program monitor" issue listing overdue remediation targets, register items due soon, and recurring activities that are behind (POA&M review, POS inspections, update windows, access reviews, training, firewall review)
- What it doesn't do: it never records an activity as done. It reads the records people keep; a missed date stays listed until the work is done and recorded
- Evidence: a dated report file committed each run to [artifacts/monitoring/program-monitor/](../07-evidence-pack/artifacts/monitoring/program-monitor/README.md), and the monthly issues (label `program-monitor`), E-25
- Limit: GitHub pauses scheduled workflows in a public repository after 60 days without activity, so a gap in the monthly issues means the monitor itself was paused. That gap is recorded honestly too

## POA&M Integration
Findings identified through monitoring activities are documented and tracked in the POA&M:

[View POA&M](../07-evidence-pack/poam/poam.md)

## Revision History

| Date | Change | Reason |
|---|---|---|
| 2026-11-15 | Access review scope moves to Microsoft Entra ID and the systems added since Q1 | Microsoft 365 cutover (CR-001) |
| 2026-11-01 | Added the automated program monitor; patching scope widened | Monthly checks of the program's own records (CA-7); IT Operations Policy (P-006) |
| 2026-10-30 | Access review scope: Stripe removed; xtraCHEF, QuickBooks Online and network administration interfaces added | Stripe is not used by the company; scope now matches the systems actually reviewed (AL-07) |
