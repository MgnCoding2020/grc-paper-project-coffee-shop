# IT Administration and Coverage Procedure
Burn and Churn Coffee

---

## Document Control
**Owner:** Business Owner | **Performed by:** IT Technician | **Approved by:** Business Owner | **Effective:** 2026-10-30 | **Review:** Annually, or when the IT role changes | **Version:** 1.0

---

## 1. Purpose
Burn and Churn Coffee brings IT in-house under [CR-003](../09-change-management/CR-003-it-support-in-house.md) with one part-time IT Technician, Riley Morgan. One part-time person can't be on call all the time, so this procedure sets out what the IT Technician does and when, who covers when they aren't working, and how knowledge is kept so the business never depends on one person's memory.

It supports NIST SP 800-53 **AC-6** (least privilege), **IA-5** (authenticator management), **CP-2** (contingency planning) and **CM-3** (change control).

---

## 2. The Role

| | |
|---|---|
| **Who** | Riley Morgan, IT Technician (`EMP-022` in [people.csv](../00-company-profile/org/people.csv)) |
| **Hours** | About **10 hours a week**: two scheduled blocks agreed with the Owner, plus maintenance windows after close when a change needs them |
| **Reports to** | Olivia Carter (Owner) |
| **Accounts** | Everyday account `riley.morgan` (no admin roles) and admin account `adm-riley.morgan` (User Administrator and Helpdesk Administrator only, unless a change record grants more) |
| **Responsible for** | Creating, changing and removing accounts; the Microsoft 365 tenant; devices; the store network and firewall; shared credentials ([PR-009](PR-009-credential-vault.md)); log review; patching; evidence exports for access reviews; the technical side of incidents |
| **Never** | Certifies their own access (the Owner and Store Manager sign the quarterly review); approves their own access requests; makes firewall or admin-role changes without a change record |

Before receiving any admin access, the IT Technician completes screening (PS-3) and signs the [Privileged User Agreement](../07-evidence-pack/examples/privileged-user-agreement.md) (PS-6, AC-6).

---

## 3. Duties Calendar

| When | Duty | Procedure |
|---|---|---|
| Every scheduled block | Work through access requests approved by the Owner or Store Manager; check the shared IT inbox for vendor notices and security alerts | PR-001 |
| Weekly | Review sign-in and audit logs, and export them before the 7-day retention ends (Entra ID Free) | PR-004 |
| Monthly | Apply updates in the maintenance window; support the Shift Leader's POS inspection if a device needs attention | PR-002, PR-006 |
| Monthly | Check admin role assignments and break-glass sign-ins; confirm the password manager has only its two members | PR-009 |
| Quarterly | Export account and group data for the access review (export only, never sign-off) | PR-003 |
| Every 6 months | Review firewall rules with the Owner | P-005 |
| Annually | Rotate network admin passwords; run the backup administrator drill with the Owner (§5); update this procedure | PR-009 |
| Any change | Raise a change record before changing firewall rules, admin roles, or a system in scope | CM-3, [change management](../09-change-management/README.md) |

Each block ends with a short entry in the IT work log (a SharePoint list once [CR-001](../09-change-management/CR-001-google-workspace-to-microsoft-365.md) is live): date, hours, what was done, and anything left open.

---

## 4. Coverage When the IT Technician Isn't Working

The **Owner is next in line** for IT, as the backup administrator. There is no outsourced on-call service.

| Order | Who | What they handle |
|---|---|---|
| 1 | **IT Technician** (during scheduled hours, or by phone for a high-severity incident) | Everything in §2 |
| 2 | **Owner** (backup administrator, using `adm-olivia.carter`) | The backup tasks in §5 |
| 3 | **Store Manager** | Keeps the store trading: Toast Offline Mode or cash ([PR-005](PR-005-contingency-plan.md)); coordinates incidents ([P-003](../04-policies/P-003-incident-response.md)) |
| 4 | **Vendor support** | Toast support for POS faults; Microsoft support through the admin centre; the internet service provider for outages |
| Last resort | **Break-glass account** | Only if both the Owner's and the IT Technician's admin accounts are unusable; every use is reviewed afterwards |

Anything that isn't urgent waits for the IT Technician's next block.

---

## 5. Backup Administrator Tasks (Owner)

The Owner can do these without the IT Technician, and practises them once a year in a short drill:

| Task | Why it can't wait |
|---|---|
| Disable an account, reset a password, revoke sessions | Account compromise ([IRP-002](../06-incident-playbooks/IRP-002-account-compromise.md)) or an involuntary termination (24 hours, P-001 §5.4) |
| Reset a user's MFA registration | Staff locked out at opening |
| Retrieve a shared credential from the password manager | Router or internet outage, vendor portal access ([PR-009](PR-009-credential-vault.md)) |
| Restart the router, firewall or access points by following the posted steps | Internet outage |
| Call vendor support with the account details from the password manager | POS or internet fault |

Firewall rule changes and admin-role changes wait for the IT Technician. If one truly can't wait, the Owner makes it as an **emergency change** and records it within one business day.

---

## 6. Keeping Knowledge Out of One Head
  - **Shared credentials** live in the password manager, where both the Owner and the IT Technician can reach them ([PR-009](PR-009-credential-vault.md)).
  - **Network layout, admin interfaces and vendor contacts** are written down in the Security & Compliance site, not in personal notes.
  - **Every change** has a change record, so the history doesn't depend on memory.
  - **If the IT Technician leaves:** the Owner disables both of their accounts, removes them from the password manager, and rotates every credential they could see, the same day.

---

## 7. Handover From Vertex IT Support (CR-003)

On the handover day, Vertex IT Support (V-004) walks the IT Technician through the items below. The IT Technician and the Owner both sign the completed checklist, which is filed with the V-004 offboarding record in the Vendor Risk Assessment Lab.

- [ ] Network diagram, and every network device with its admin interface (router, firewall, access points)
- [ ] Current firewall rules, with the reason for each
- [ ] Every account and credential Vertex holds or knows, listed; each one rotated and stored in the password manager
- [ ] Open tickets and known issues (including the Q1 findings assigned to Vertex: IAM:F-001, F-003, F-004)
- [ ] Vendor and warranty contacts for store equipment
- [ ] Google Workspace admin tasks still pending before CR-001 completes
- [ ] Vertex's generic account and every other Vertex account disabled (CR-003 step 5)

---

## 8. Current Status
  - **Planned.** The IT Technician starts with CR-003 (scheduled 2026-11-15). Until then, Vertex IT Support administers IT.
  - Tracked under **POAM-022** (coverage and backup administrator drill) and **POAM-021** (password manager).

---

## 9. Related Documents
  - [Roles and Responsibilities](../00-company-profile/org/roles.md)
  - [Shared Credential Management Procedure (PR-009)](PR-009-credential-vault.md)
  - [User Access Management Procedure (PR-001)](PR-001-user-access.md)
  - [Contingency and Outage Plan (PR-005)](PR-005-contingency-plan.md)
  - [CR-003: Bring IT Support In-House](../09-change-management/CR-003-it-support-in-house.md)

---

*This document is a simulation for educational and portfolio purposes only.*
