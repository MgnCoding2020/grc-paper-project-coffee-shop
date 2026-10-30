# CR-001: Migrate from Google Workspace to Microsoft 365
Burn and Churn Coffee

| | |
|---|---|
| **Status** | Approved (scheduled) |
| **Requested by** | IT administrator (Vertex IT Support; implemented by the IT Technician under CR-003) |
| **Approved by** | Olivia Carter (Owner) |
| **Approved on** | 2026-10-30 |
| **Scheduled cutover** | 2026-11-15 |
| **Related** | [CR-003](CR-003-it-support-in-house.md) (IT brought in-house, same date) |

---

## 1. Business Justification

- **One identity platform** for email, files, chat and the intranet, with group-based access instead of per-person grants.
- **Stronger sign-in security:** MFA for every staff account, and Conditional Access where licensed.
- **A SharePoint intranet** for SOPs, access requests, the training tracker and timesheets, replacing scattered documents.
- **Better audit logging:** the Microsoft 365 audit log covers sign-ins, admin actions and file activity.
- **Bookkeeping consolidated:** QuickBooks Online is replaced by a restricted Excel workbook in SharePoint, removing a separate vendor login.

---

## 2. Scope

| | Systems |
|---|---|
| **In** | SYS-010 Microsoft Entra ID · SYS-011 Exchange Online · SYS-012 SharePoint Online and Teams · SYS-013 Intune and Defender for Business (if licensed) · SYS-014 Bookkeeping workbook (Excel for the web) |
| **Out (retired)** | SYS-002 Google Workspace · SYS-003 Google Admin Console · SYS-005 QuickBooks Online |
| **Unchanged** | SYS-001 Toast POS · SYS-004 xtraCHEF · SYS-006 Northwind Payroll · SYS-007 Store network |

**Vendors:** V-003 Microsoft onboarded; V-006 Intuit and V-007 Google offboarded.

**People:** all 20 active store staff and the IT Technician, from [people.csv](../00-company-profile/org/people.csv). Aiden Scott (terminated) gets no account. Two break-glass accounts are documented.

---

## 3. Categorization

| Data | Classification | Where it lives after the change |
|---|---|---|
| Staff accounts and sign-in data | Restricted | Entra ID |
| Business email | Confidential | Exchange Online |
| SOPs, policies, training records | Internal | SharePoint |
| Financial records | Confidential | Finance library (SYS-014), restricted to owners and managers |
| Payroll export | Restricted | People site, restricted; sent to Northwind |

No cardholder data enters Microsoft 365. Card payments stay in Toast.

---

## 4. Identity Design

- **Groups:** `grp-bc-all-staff`, `grp-bc-owners`, `grp-bc-managers`, `grp-bc-shift-leads`, `grp-bc-baristas`, `grp-bc-it`, `grp-bc-break-glass`. Access is granted to groups only.
- **Accounts:** created from `people.csv` by [`tools/tenant/provision-users.ps1`](../tools/tenant/provision-users.ps1), so the tenant matches the roster.
- **Admin roles:** the Owner and the IT Technician each have a separate `adm-` account with only the roles they need. Admin roles are standing (PIM requires Entra ID P2, which the company doesn't have); this is an accepted risk with compensating controls (separate admin accounts, MFA, break-glass, quarterly review).
- **MFA:** required for every account. Method depends on licensing: Conditional Access (P1) where available, otherwise per-user MFA scoped to Burn and Churn accounts.

### Licensing (company plan, checked against Microsoft's pages 2026-10-30)

| Who | Licence | Why |
|---|---|---|
| Owner, Store Manager, Shift Leaders, IT Technician | Microsoft 365 Business Premium | Mailbox, Office apps, Entra ID P1 (Conditional Access), Intune, Defender for Business |
| Baristas | Microsoft 365 F1 | Teams and SharePoint for SOPs and training; includes Entra ID P1 and Intune Plan 1; no mailbox, which baristas don't need |

Prices are not recorded here; check Microsoft's current pricing at purchase. The live lab tenant runs on Entra ID Free; any control that needs a licence the lab doesn't have stays `Simulation` in the evidence and says so.

---

## 5. Risk and Impact Analysis (CM-4)

| # | Risk | Impact | Mitigation |
|---|---|---|---|
| 1 | Mail or files lost during migration | Business records missing | Full export of Google data before cutover; Google kept read-only for 30 days |
| 2 | Staff can't sign in on day one | Store operations disrupted (email, SOPs) | Pilot first (Owner, Manager, IT Technician); temporary passwords handed out in person; Toast POS is unaffected, so sales continue |
| 3 | MFA enrolment gaps leave accounts unprotected | Account compromise (R-01) | MFA registration tracked per user; exit criterion requires every active account enrolled |
| 4 | Audit logging not actually working | Incidents can't be investigated (AU-2, AU-6) | Audit log verified returning records before Google is closed |
| 5 | Former IT vendor keeps admin access to old or new systems | Unauthorized changes (R-06) | Vertex gets no Microsoft 365 access; Google closed; handled in CR-003 |
| 6 | Over-broad permissions on the Finance library | Financial data exposed | Library restricted to `grp-bc-owners` and `grp-bc-managers`; checked in the post-implementation review |
| 7 | Licence lapse (for example, a trial ending) removes Conditional Access | MFA enforcement weakens | Fall back to per-user MFA; the lapse is recorded as its own change and POA&M item |

---

## 6. Control Impact

| Control | Change |
|---|---|
| IA-2 | MFA through Entra ID for every Microsoft 365 account; moves POAM-001 forward |
| AC-2, AC-6 | Group-based access, separate admin accounts, accounts created from the roster |
| AU-2, AU-6 | Microsoft 365 audit log verified and reviewed weekly; moves POAM-003 forward |
| CM-3, CM-4 | This change record is the first use of the change process |
| SA-9 | V-003 Microsoft assessed; V-006 and V-007 offboarded with data export and deletion confirmed |
| AT-2 | Training tracked in a SharePoint list from the roster; moves POAM-002 forward |
| SI-3, CM-6 | Defender for Business and Intune baselines, if licensed; moves POAM-007 and POAM-009 forward |
| SC-8, SC-28 | Microsoft-managed encryption in transit and at rest, per Microsoft's shared-responsibility terms |

---

## 7. Implementation Plan

| Step | When | What |
|---|---|---|
| 1 | Before cutover | Export all Google Workspace and QuickBooks data; confirm the exports open |
| 2 | Pilot (on or before 2026-11-15) | Provision Owner, Store Manager and IT Technician; enable MFA; verify the audit log |
| 3 | 2026-11-15 | Provision all staff from `people.csv`; groups and memberships; MFA enrolment begins |
| 4 | Cutover week | SharePoint sites and the Finance library (once the SharePoint licence is active); Google set to read-only |
| 5 | Cutover + 30 days | Close Google Workspace and QuickBooks; file the deletion confirmations |

**Rollback:** until Google is closed in step 5, Google stays available read-only and can be returned to service. Rolling back is recorded in this record's log, with the reason.

---

## 8. Exit Criteria

- [ ] Every active staff account exists and matches `people.csv`
- [ ] Every active account has MFA registered
- [ ] Audit log verified returning sign-in and admin records
- [ ] Finance library restricted to owners and managers, verified
- [ ] Google Workspace and QuickBooks data exported, then deleted, with confirmations filed as evidence (V-006, V-007 offboarding)

---

## 9. Post-Implementation Review

The **Q4 2026 access review** in the IAM Access Review Lab is the formal check: the first review run against Entra ID users, groups and admin roles. It is performed by the Owner and Store Manager, not by the IT Technician who implemented the change.

---

## 10. Log

| Date | Entry |
|---|---|
| 2026-10-30 | Raised and approved by the Owner. Scheduled for 2026-11-15. |

---

*This document is a simulation for educational and portfolio purposes only.*
