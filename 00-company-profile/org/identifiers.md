# Identifier Conventions
Burn and Churn Coffee

---

## Purpose

Every risk, control, finding, POA&M item, change and piece of evidence in the Burn and Churn Coffee security program has a stable identifier. This page defines each format and where its items live, so that any reference, in this repository or in a companion lab, points to exactly one thing.

---

## Rules

- **IDs are permanent.** Once published, an ID is never reused or renumbered.
- **Retired items stay listed.** They are marked retired, not deleted, so older references still resolve.
- **One home per ID type.** Each kind of item is numbered in exactly one place (see the table below).

---

## Identifier Formats

| Kind | Format | Example | Where it lives |
|---|---|---|---|
| Risk | `R-##` | `R-01` | [Risk register](../../02-risk-management/risk-register.md) |
| Control | NIST SP 800-53 Rev. 5 ID | `AC-2`, `AC-2(7)` | [Control matrix](../../03-controls/control-matrix.md) |
| Evidence | `E-##` | `E-02` | [Evidence matrix](../../07-evidence-pack/evidence-matrix.md) |
| POA&M item | `POAM-###` | `POAM-013` | [POA&M](../../07-evidence-pack/poam/poam.md) (this repository only) |
| Change record | `CR-###` | `CR-001` | `09-change-management/` (planned) |
| Incident | `INC-###` | `INC-001` | [Incident log](../../07-evidence-pack/artifacts/monitoring/incident-log.md) (current entries to be renumbered from "Incident 001/002") |
| Person | `EMP-###` | `EMP-001` | [people.csv](people.csv) (vendor and break-glass accounts are not people) |
| Vendor | `V-###` | `V-002` | [Vendor inventory](../../02-risk-management/vendor-risk-management/vendor-inventory.md) |
| System | `SYS-###` | `SYS-001` | [Asset inventory](../../01-asset-inventory/assets.md) |
| Other assets | `HW-###`, `NET-###`, `DATA-###`, `PER-###` | `NET-002` | [Asset inventory](../../01-asset-inventory/assets.md) |

---

## Lab Findings (cross-repository references)

The companion labs number their own findings locally. Both labs started at `F-0x`, so a bare finding ID is ambiguous outside its own repository. **Inside a lab, use the local ID. Everywhere else, use the prefixed global form.**

| Source | Local ID | Global ID | Example |
|---|---|---|---|
| [IAM Access Review Lab](https://github.com/MgnCoding2020/IAM-Access-Review-Lab), Q1 2026 review | `F-###` | `IAM:F-###` | `IAM:F-001` (terminated employee account still active) |
| IAM Access Review Lab, later reviews | `F-###` | `IAM-<period>:F-###` | `IAM-Q4:F-001` |
| [Vendor Risk Assessment Lab](https://github.com/MgnCoding2020/Vendor-Risk-Assessment-Lab), assessment of vendor V-### | `F-##` | `VRA-V###:F-##` | `VRA-V002:F-02` (vendor admin MFA not enforced) |

Lab findings roll up to this repository's POA&M, which cites them in the global form.

---

*This document is a simulation for educational and portfolio purposes only.*
