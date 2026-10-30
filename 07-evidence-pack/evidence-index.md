# Evidence Index
Burn and Churn Coffee

---

## Purpose

One table of every evidence artifact in the Burn and Churn Coffee security program, across all of its repositories. It is the starting point for an auditor or reviewer: each row says what the evidence is, which controls it supports, where it lives, when it is from, and how far it can be trusted.

The [evidence matrix](evidence-matrix.md) defines the evidence each control requires; this index points to the artifacts themselves.

---

## Status Values

| Status | Meaning |
|---|---|
| **Simulation** | A documented record for the fictional company. Realistic, internally consistent and checked by the consistency checker, but not produced by a real system |
| **Lab-verified &lt;date&gt;** | Produced by real work on a real machine or tenant on that date, with the raw output preserved (redacted where needed) |
| **Planned** | Evidence a control needs that does not exist yet |

Committed evidence uses the fictional domain `burnandchurncoffee.com`. Where evidence comes from a live tenant, the real domain and tenant identifiers are replaced before committing.

---

## Hub Evidence (this repository)

| Evidence ID | Control(s) | Description | Path | Date | Status | Related POA&M |
|---|---|---|---|---|---|---|
| E-01 | AC-2 | User access review export | [user-access-review.csv](artifacts/access/user-access-review.csv) | 2026-03-25 | Simulation | POAM-014 |
| E-02 | IA-2 | MFA status export | [mfa-status.csv](artifacts/access/mfa-status.csv) | 2026-03-25 | Simulation | POAM-001 |
| E-03 | AC-6 | Privileged access review (script output over E-01) | [privileged_access_review_check.py](artifacts/scripts/privileged_access_review_check.py) | 2026-03-25 | Simulation | POAM-014 |
| E-04 | AU-6 | Incident log (INC-001, INC-002) | [incident-log.md](artifacts/monitoring/incident-log.md) | 2026-03-12 to 2026-03-20 | Simulation | POAM-003 |
| E-05 | SC-7 | Network segmentation summary (documents a gap) | [network-segmentation.md](artifacts/network/network-segmentation.md) | Undated | Simulation | POAM-015 |
| E-06 | AT-2 | Security awareness training log | [security-training-log.csv](artifacts/training/security-training-log.csv) | 2026-01-10 | Simulation | POAM-002 |
| E-07 | PE-3 | POS and device physical inspection checklist | [physical-inspection-checklist.csv](artifacts/physical/physical-inspection-checklist.csv) | From 2026-02-01 | Simulation | POAM-004 |
| E-08 | CP-2 | Backup and outage response documentation | — | — | Planned | POAM-005 |
| E-09 | SA-9 | Vendor assessment summary (Toast POS) | [vendor-assessment-summary.md](artifacts/vendor/vendor-assessment-summary.md) | Undated | Simulation | POAM-006 |
| E-10 | SI-3 | Endpoint protection status | — | — | Planned | POAM-007 |
| E-11 | SI-7 | Change and integrity monitoring logs | — | — | Planned | POAM-008 |
| E-12 | CM-6 | Secure configuration baselines | — | — | Planned | POAM-009 |
| E-13 | SC-8 | Encryption-in-transit evidence | — | — | Planned | POAM-010 |
| E-14 | RA-5 | Vulnerability scan and penetration test reports | — | — | Planned | POAM-011 |
| E-15 | SC-28 | Data-at-rest protection and storage scope | — | — | Planned | POAM-012 |
| E-16 | CM-3, CM-4 | Change process and change records (CR-001, CR-003) | [09-change-management/](../09-change-management/README.md) | 2026-10-30 | Simulation | POAM-017 |
| E-17 | PS-4, PS-5 | Staff roster with employment status | [people.csv](../00-company-profile/org/people.csv) | 2026-10-30 | Simulation | POAM-016 |
| E-18 | CA-5 | POA&M review log | [poam.md](poam/poam.md) | 2026-10-30 | Simulation | POAM-019 |

---

## Companion Lab Evidence

| Source | Control(s) | Description | Path | Date | Status | Related POA&M |
|---|---|---|---|---|---|---|
| IAM lab | AC-2, AC-6 | Q1 2026 user access matrix (all systems, all staff) | [user-access-matrix.csv](https://github.com/MgnCoding2020/IAM-Access-Review-Lab/blob/main/evidence/user-access-matrix.csv) | 2026-03-25 | Simulation | POAM-014 |
| IAM lab | AC-2, AC-6 | Q1 2026 access review findings IAM:F-001 to F-005 | [access-review-findings.md](https://github.com/MgnCoding2020/IAM-Access-Review-Lab/blob/main/findings/access-review-findings.md) | 2026-03-25 | Simulation | POAM-014 |
| IAM lab | AC-2, AC-6 | Remediation tracker | [remediation-tracker.csv](https://github.com/MgnCoding2020/IAM-Access-Review-Lab/blob/main/remediation/remediation-tracker.csv) | Targets 2026-03-31 to 2026-04-05; status check 2026-10-30 (Overdue) | Simulation | POAM-014 |
| IAM lab | AC-2, AC-6, CA-5 | Remediation status checks (overdue findings found and escalated) | [status-checks.md](https://github.com/MgnCoding2020/IAM-Access-Review-Lab/blob/main/remediation/status-checks.md) | 2026-10-30 | Simulation | POAM-014, POAM-019 |
| IAM lab | AC-2, AC-6 | Quarterly access review summary | [quarterly-access-review-summary.md](https://github.com/MgnCoding2020/IAM-Access-Review-Lab/blob/main/review-summary/quarterly-access-review-summary.md) | Q1 2026 | Simulation | POAM-014 |
| IAM lab | AC-2, AC-6 | Local access review of a Windows lab VM (redacted) | [vm-local-access-review-REDACTED.md](https://github.com/MgnCoding2020/IAM-Access-Review-Lab/blob/main/evidence/vm-local-access-review-REDACTED.md) | 2026-03-08 | Lab-verified 2026-03-08 | — (lab demonstration, outside the company boundary) |
| IAM lab | IA-5 (technique) | Password policy before and after hardening (`net accounts` output), IAM:F-005 | [before](https://github.com/MgnCoding2020/IAM-Access-Review-Lab/blob/main/evidence/vm-password-policy-before.txt) · [after](https://github.com/MgnCoding2020/IAM-Access-Review-Lab/blob/main/evidence/vm-password-policy-after.txt) | 2026-03-09 | Lab-verified 2026-03-09 | — (lab demonstration, outside the company boundary) |
| Vendor lab | SA-9 | Toast (V-001) assessment against PCI DSS 12.8: six-factor inherent risk (18/18), due diligence against Toast's public information, findings VRA-V001:F-01 to F-04, final report | [assessments/V-001-toast](https://github.com/MgnCoding2020/Vendor-Risk-Assessment-Lab/tree/main/assessments/V-001-toast) | 2026-10-30 | Simulation (sources checked 2026-10-30) | POAM-020, POAM-006 |
| Vendor lab | SA-9 | Northwind Payroll (V-002) assessment: intake, inherent risk, due diligence, findings VRA-V002:F-01 to F-04, final report | [assessments/V-002-northwind](https://github.com/MgnCoding2020/Vendor-Risk-Assessment-Lab/tree/main/assessments/V-002-northwind) | 2026-06-23 | Simulation | POAM-013 |
| Vendor lab | SA-9 | Microsoft 365 (V-003) assessment before onboarding: six-factor inherent risk (16/18), due diligence against Microsoft's public documentation, findings VRA-V003:F-01 to F-05, final report | [assessments/V-003-microsoft](https://github.com/MgnCoding2020/Vendor-Risk-Assessment-Lab/tree/main/assessments/V-003-microsoft) | 2026-10-30 | Simulation (sources checked 2026-10-30) | POAM-018 |

---

## Program Monitoring Evidence

Runs of the program consistency checker ([`tools/check_program.py`](../tools/check_program.py)) across all three repositories. These are real tool runs over the repositories themselves.

| Description | Path | Date | Status |
|---|---|---|---|
| Baseline before corrections: 28 findings in 5 checks | [2026-10-30-baseline.txt](artifacts/consistency/2026-10-30-baseline.txt) | 2026-10-30 | Lab-verified 2026-10-30 |
| After hub corrections: 8 of 9 checks pass | [2026-10-30-after-hub-corrections.txt](artifacts/consistency/2026-10-30-after-hub-corrections.txt) | 2026-10-30 | Lab-verified 2026-10-30 |
| After all phase 2 corrections: 9 of 9 pass | [2026-10-30-phase2-complete.txt](artifacts/consistency/2026-10-30-phase2-complete.txt) | 2026-10-30 | Lab-verified 2026-10-30 |
| Corrections log for dated evidence | [CORRECTIONS.md](artifacts/CORRECTIONS.md) | 2026-10-30 | Simulation |

---

## Coming From the Live Tenant

Evidence the CR-001 build will produce (see the build-day runbook in `CLAUDE.md` §7.5). Each becomes `Lab-verified <date>` when committed.

| Control(s) | Evidence | Status |
|---|---|---|
| AC-2 | Provisioning log from `provision-users.ps1` | Planned (2026-11-15) |
| AC-2, AC-6 | Entra users, group memberships and admin role assignments | Planned (2026-11-15) |
| IA-2 | Per-user MFA status and sign-in log details | Planned (2026-11-15) |
| AU-2, AU-6 | Audit log export, verified returning records | Planned (2026-11-15) |
| AC-2, AC-6 | Q4 2026 access review run against Entra ID | Planned (Q4 2026) |
| AC-2, SA-9 | Vendor guest invited and added to `grp-bc-vendors` (CR-004 provisioning log) | Planned (after VRA-V002:F-02 closes) |
| AC-6, AU-2 | Guest sign-in and payroll-export access; denied access to other folders | Planned (CR-004) |
| AC-2, PS-4 | Guest removed at access end; failed sign-in afterwards (corrective-action exercise) | Planned (CR-004 + 90 days) |

---

*This document is a simulation for educational and portfolio purposes only.*
