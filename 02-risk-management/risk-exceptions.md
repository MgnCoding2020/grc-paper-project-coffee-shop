# Exception Register
Burn and Churn Coffee

Accepted risks and policy exceptions, under the [Risk Acceptance and Exception Procedure (PR-014)](../05-procedures/PR-014-risk-acceptance.md). Only the Owner approves; every exception expires within 12 months; closed rows stay, marked closed. The monthly program monitor reads the **Expires** column.

---

## Register

| ID | Requirement not met | Why | Compensating controls | Residual risk | Approved | Expires | Source | Status |
|---|---|---|---|---|---|---|---|---|
| EXC-001 | Admin roles should be eligible, not standing (just-in-time access) | Needs Entra ID P2 (PIM), which the tenant doesn't have | Separate `adm-` accounts with least-privilege roles; MFA; break-glass accounts; admin roles checked in every quarterly access review | Medium | 2026-11-02, Olivia Carter (Owner) | 2027-11-02 | VRA-V003:F-03; `CLAUDE.md` §5.2 | Open |
| EXC-002 | MFA enforced through Conditional Access, with legacy authentication blocked | Entra ID Free has no Conditional Access | Per-user MFA on every Burn and Churn account (PR-013); Conditional Access built during the Business Premium trial (D-9) | Medium | 2026-11-02, Olivia Carter (Owner) | 2027-05-02 | VRA-V003:F-01 | Open |
| EXC-003 | Network segmented: POS isolated (P-005 §3) | Segments not yet built; POS, laptop and connected devices share one Wi-Fi network | Guest Wi-Fi separate; POS card data encrypted by the provider; segmentation tracked to closure | High (fix date required) | 2026-11-02, Olivia Carter (Owner) | 2027-05-02 | P-005 §7; POAM-015, POAM-026 | Open |
| EXC-004 | MFA on every login (P-001 §5.5) | Toast register logins use PINs by design; cashiers can't do MFA at the counter (D-2) | Personal PINs; one person signed in at a time; sign out when leaving the register; idle auto-logout; no PIN sharing | Low | 2026-11-02, Olivia Carter (Owner) | 2027-11-02 | `org/roles.md`; D-2 | Open |
| EXC-005 | Independent security assurance from every Moderate-tier vendor (P-008 §4) | The espresso service company has no SOC 2 or ISO 27001 | Machine isolated on the Devices segment (once built); remote sessions need approval and are logged; supervised visits | Low (after conditions) | 2026-11-02, Olivia Carter (Owner) | 2027-11-02 | VRA-V011:F-03 | Open |
| EXC-006 | Logging of access to shared credentials (AU-2) | The Bitwarden Free plan has no event log | Two members only; per-item password history; rotation on every staff or vendor change; monthly membership check | Low | 2026-11-02, Olivia Carter (Owner) | 2027-11-02 | PR-009 §5 | Open |

---

## Review Log

| Date | Reviewer | Outcome |
|---|---|---|
| 2026-11-02 | Olivia Carter (Owner) | Register created; EXC-001 to EXC-006 recorded from decisions already made in other program documents |

---

*This document is a simulation for educational and portfolio purposes only.*
