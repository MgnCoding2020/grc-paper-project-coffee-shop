# CR-004: Time-Limited Guest Access for Northwind's Payroll Contact
Burn and Churn Coffee

| | |
|---|---|
| **Status** | Approved (blocked until its preconditions are met) |
| **Requested by** | Olivia Carter (Owner) |
| **Approved by** | Olivia Carter (Owner) |
| **Approved on** | 2026-10-30 |
| **Scheduled** | When the preconditions in section 2 are met (after CR-001) |
| **Related** | [CR-001](CR-001-google-workspace-to-microsoft-365.md) (SharePoint), Northwind assessment VRA-V002, [vendor-contacts.csv](../00-company-profile/org/vendor-contacts.csv) |

---

## 1. Business Justification

Once Northwind Payroll Services (V-002) goes live, its payroll contact needs to collect the bi-weekly payroll export (staff hours from the timesheets). Sharing it from a controlled SharePoint folder replaces emailing spreadsheets, and gives the company a sign-in record and an audit trail for every access.

This change also demonstrates the vendor-access rules in the Access Management Policy (P-001 §5.7): **named individuals only, least privilege, time-bound access, reviewed and removed** — the rules the old generic Vertex IT Support account broke.

---

## 2. Preconditions (all must be met before implementation)

1. **Northwind's vendor MFA is confirmed** (finding VRA-V002:F-02 closed). No vendor access before then.
2. **SharePoint is live** (CR-001; licence reactivated, D-8).
3. The contact's **own account has MFA turned on**, confirmed with the vendor before the invitation is sent.

---

## 3. Scope

| | |
|---|---|
| **Who** | VC-001 Jordan Ellis, Northwind Payroll Services (fictional; played by a dedicated test mailbox whose address lives only in the git-ignored `.env`) |
| **Account type** | Microsoft Entra B2B guest (`userType = Guest`), created by invitation |
| **Group** | `grp-bc-vendors` (new; vendor guests only) |
| **Access** | **Read-only** to one folder: People site → Payroll Export. Nothing else |
| **Duration** | 90 days from the access start date, then removed unless renewed by a new approval |
| **Sponsor** | Olivia Carter (Owner): accountable for the access and for its removal |

---

## 4. Risk and Impact Analysis (CM-4)

| # | Risk | Mitigation |
|---|---|---|
| 1 | **MFA can't be enforced for guests on Entra ID Free** (no Conditional Access; guests use their own account's MFA or an email one-time code) | Precondition 3 (vendor confirms MFA on the contact's account); verify what the sign-in log records for each guest sign-in. If MFA can't be verified, record a gap with compensating controls: read-only, one folder, 90-day limit, group-based removal. If the Business Premium trial (D-9) is active, a Conditional Access policy requiring MFA for guests closes this |
| 2 | Guest access outlives the business need | 90-day end date in `vendor-contacts.csv`; SharePoint guest-expiration setting on the site; access checked in every quarterly access review |
| 3 | Guest sees more than the payroll export | Permission granted to `grp-bc-vendors` on one folder only; verified by signing in as the guest |
| 4 | Real personal data used in testing | The payroll export test file uses the fictional roster and made-up hours; no pay rates or bank details |
| 5 | Cost | Guest users are billed per monthly active user, with the first 50,000 free (Microsoft's licensing page, checked 2026-10-30); confirm on build day whether a linked Azure subscription is needed |

---

## 5. Implementation Plan

| Step | What | Evidence |
|---|---|---|
| 1 | Confirm preconditions 1–3; record them in the log below | Log entry |
| 2 | Set `VC-001` to `Approved` with `access_start` and `access_end` in `vendor-contacts.csv`; put the test mailbox address in `.env` | Commit |
| 3 | Run `tools/tenant/provision-users.ps1`: invites the guest and adds them to `grp-bc-vendors` | Provisioning log |
| 4 | Share the Payroll Export folder read-only with `grp-bc-vendors`; set site guest expiration to 90 days | Screenshot of permissions and setting |
| 5 | Upload the test payroll export; the guest accepts the invitation, signs in and opens it | Sign-in log and audit log entries (redacted) |
| 6 | Negative test: the guest tries another folder and is denied | Screenshot or audit entry |

---

## 6. Corrective-Action Exercise (planned)

To evidence that time-bound access actually ends, the access end date is tested as a **planned exercise**, labelled as such:

1. When `access_end` passes, the quarterly access review checks `grp-bc-vendors` against `vendor-contacts.csv`.
2. Any guest still present after their end date is recorded as a review finding.
3. Corrective action: the guest is removed from the group and deleted; removal is verified by a failed sign-in attempt.
4. Evidence: the review finding, the removal entry in the audit log, the failed sign-in, and `VC-001` set to `Removed`.

---

## 7. Exit Criteria

- [ ] Preconditions 1–3 recorded
- [ ] Guest exists, is in `grp-bc-vendors` only, and can read only the Payroll Export folder
- [ ] Guest sign-in and file access appear in the logs (and what the log shows for MFA is recorded)
- [ ] 90-day end date set in `vendor-contacts.csv` and in SharePoint

## 8. Post-Implementation Review

The first quarterly access review after implementation confirms the guest's group, permissions and end date, and later the removal.

---

## 9. Log

| Date | Entry |
|---|---|
| 2026-10-30 | Raised and approved by the Owner. Blocked until VRA-V002:F-02 is closed and SharePoint is live. |

---

*This document is a simulation for educational and portfolio purposes only.*
