# CR-003: Bring IT Support In-House; Offboard Vertex IT Support
Burn and Churn Coffee

| | |
|---|---|
| **Status** | Approved (scheduled) |
| **Requested by** | Olivia Carter (Owner) |
| **Approved by** | Olivia Carter (Owner) |
| **Approved on** | 2026-10-30 |
| **Scheduled** | 2026-11-15 |
| **Related** | [CR-001](CR-001-google-workspace-to-microsoft-365.md) (Microsoft 365 migration, implemented by the new IT Technician) |

---

## 1. Business Justification

- **Accountability:** the Q1 2026 access review found a terminated employee's accounts still active (IAM:F-001) and an inactive vendor account still enabled (IAM:F-003). An in-house owner for account changes closes that gap.
- **Generic vendor access:** Vertex IT Support administers Google Workspace and the network through a generic, shared account, which P-001 §5.7 does not allow.
- **The migration needs an owner:** CR-001 needs someone on site to provision accounts, enrol MFA and verify logging.

---

## 2. Scope

| | |
|---|---|
| **Hire** | Riley Morgan, part-time IT Technician, about 10 hours a week (`EMP-022` in [people.csv](../00-company-profile/org/people.csv)); duties and coverage in [PR-008](../05-procedures/PR-008-it-administration.md) |
| **New system** | Company password manager (SYS-015, Bitwarden Free organization, vendor V-009) for shared admin credentials ([PR-009](../05-procedures/PR-009-credential-vault.md)) |
| **Offboard** | V-004 Vertex IT Support (all accounts and access) |
| **Clean up** | V-005 NorthPeak Systems' network admin account, still enabled at the Q1 review (IAM:F-003) |

---

## 3. Personnel Controls for the IT Technician

| Control | Requirement |
|---|---|
| PS-3 Personnel screening | Background screening completed and recorded before any admin access is granted |
| PS-6 Access agreements | Signed Acceptable Use Policy acknowledgment and [Privileged User Agreement](../07-evidence-pack/examples/privileged-user-agreement.md) (E-20) |
| AC-6 Least privilege | Everyday account `riley.morgan` has no admin roles; admin work only from `adm-riley.morgan`, with only User Administrator and Helpdesk Administrator unless a change record says otherwise |
| Separation of duties | The IT Technician creates and changes accounts but never certifies their own access; the Owner and Store Manager sign the quarterly review |

---

## 4. Risk and Impact Analysis (CM-4)

| # | Risk | Impact | Mitigation |
|---|---|---|---|
| 1 | Knowledge lost when Vertex leaves | Systems can't be maintained | Handover session with written notes (network layout, admin interfaces, open tickets), signed off by the IT Technician and the Owner |
| 2 | Vertex still knows shared passwords | Unauthorized access after offboarding | Rotate every credential Vertex knew (router, firewall, Wi-Fi admin, Google admin) on the handover day, and store the new ones in the password manager (PR-009) |
| 3 | Vertex or NorthPeak accounts left enabled | Repeat of IAM:F-003 | Every vendor account disabled and listed in the offboarding record; checked in the Q4 review |
| 4 | Single person holds all admin rights | No cover; insider risk | Owner keeps a separate admin account and is the second password manager member; break-glass accounts; quarterly review of admin roles |
| 5 | Part-time technician unavailable during an incident | Slower response | Coverage order in PR-008 §4: the Owner is backup administrator and practises the backup tasks yearly (POAM-022); the Store Manager keeps the store trading; vendor support lines for POS and internet |

---

## 5. Implementation Plan

| Step | What |
|---|---|
| 1 | Screening, access agreement and start date recorded; `people.csv` updated from Planned to Active |
| 2 | IT Technician accounts created (everyday and `adm-`), MFA enrolled |
| 3 | Handover from Vertex using the checklist in PR-008 §7, signed by the IT Technician and the Owner; password manager set up with the Owner and the IT Technician as its two members |
| 4 | Rotate every credential Vertex knew, and store the new ones in the password manager |
| 5 | Disable all Vertex accounts and the NorthPeak network admin account |
| 6 | Vendor offboarding record for V-004 completed in the Vendor Risk Assessment Lab |

**Rollback:** if the hire falls through before step 3, Vertex's contract continues and this change is cancelled. After step 4, there is no rollback to the generic account.

---

## 6. Exit Criteria

- [ ] Screening and access agreement on file
- [ ] IT Technician has separate everyday and admin accounts, both with MFA
- [ ] Handover notes signed off
- [ ] Every credential Vertex knew has been rotated and stored in the password manager
- [ ] Privileged User Agreement signed by the IT Technician and the Owner
- [ ] No Vertex or NorthPeak account remains enabled
- [ ] V-004 offboarding record complete; vendor inventory updated

---

## 7. Post-Implementation Review

The Q4 2026 access review confirms that no vendor accounts remain, that the IT Technician's admin roles are limited as above, and that the generic-account finding (AL-13) is closed.

---

## 8. Log

| Date | Entry |
|---|---|
| 2026-10-30 | Raised and approved by the Owner. Scheduled for 2026-11-15. |
| 2026-10-30 | Alignment review: Q1 findings assigned to the outsourced IT administrator (IAM:F-001, F-003, F-004) were found about seven months overdue with no updates. Added to the justification: remediation needs an in-house owner. |
| 2026-10-30 | Scope amended and approved by the Owner: the role is about 10 hours a week, with the Owner as backup administrator (PR-008); a password manager (SYS-015, V-009) holds the shared credentials rotated at handover (PR-009); Privileged User Agreement added to the personnel controls. |

---

*This document is a simulation for educational and portfolio purposes only.*
