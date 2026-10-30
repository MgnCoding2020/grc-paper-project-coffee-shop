# Security Awareness Training Program
Burn and Churn Coffee

---

## Document Control
**Owner:** Store Manager | **Approved by:** Business Owner | **Effective:** 2026-10-30 | **Review:** Annually | **Version:** 1.0

---

## 1. Purpose
Most incidents at a small shop start with a person: a convincing phishing email, a shared PIN, a skimmer nobody noticed. This program gives every employee short, practical training on the threats they will actually meet. It implements NIST SP 800-53 **AT-2 (Literacy Training and Awareness)** and PCI DSS Requirement **12.6** (security awareness program).

---

## 2. Who and When

| Who | When |
|---|---|
| Every new employee | Before receiving system access, as part of onboarding (PR-001), together with the Acceptable Use Policy acknowledgment (P-002 §11) |
| All staff | Every year |
| All staff | After a relevant incident, or when a major system changes (for example, the Microsoft 365 cutover) |
| Owner, Store Manager, IT Technician | An extra module on admin accounts, MFA for admin roles and approving access |

---

## 3. Topics

| Topic | Why it matters here | Source |
|---|---|---|
| Phishing and suspicious requests | Most likely route to account compromise (R-01) | P-002 §7, IRP-001 |
| Passwords, MFA and never sharing accounts | Every account is individual; MFA on every Microsoft 365 account | P-001 §5.5, P-002 §3 |
| **Toast PINs** | Personal PIN, one person signed in, sign out when leaving the register, never use someone else's PIN | `org/roles.md` |
| Card handling | Never write down or photograph card numbers | P-004 §3 |
| **Spotting POS tampering** | Overlays, extra devices, broken seals, unexpected prompts; checking anyone claiming to service a terminal | PR-006, PCI DSS 9.5.1.3 |
| Outages | Offline payment rules, the $50 limit, never clearing a terminal with pending payments | PR-005 §4 |
| Lost or stolen devices | Report immediately | IRP-004 |
| How to report | Tell the Store Manager or Owner straight away; reporting is always the right call | P-003 §7 |

---

## 4. Delivery
  - A **20-minute in-person session** led by the Store Manager, using this page as the outline, with a short quiz (at least 80% to pass; retake if not).
  - Each employee signs the [training acknowledgement](../07-evidence-pack/examples/security-training-acknowledgement-form.md).
  - Completion is recorded in the [training log](../07-evidence-pack/artifacts/training/security-training-log.csv), and in a SharePoint training list once CR-001 is live.

---

## 5. Measures
  - **Completion:** 100% of active staff trained within 30 days of the first session, and every new hire before system access.
  - **Reporting:** suspicious emails and tamper concerns reported (tracked in the incident log). More reports after training is a good sign, not a bad one.

---

## 6. Current Status
  - **1 of 20 active staff** has a recorded completion (Daniel Lopez, 2026-01-10); there has been no formal program until now.
  - **First all-staff session:** by **2026-11-30**, after the Microsoft 365 cutover, so it can include signing in and enrolling MFA.

Tracked under **POAM-002**. AT-2 stays *Not Implemented* until staff are actually trained.

---

## 7. Related Documents
  - [Acceptable Use Policy (P-002)](../04-policies/P-002-acceptable-use.md)
  - [Contingency and Outage Plan (PR-005)](PR-005-contingency-plan.md)
  - [POS Device Inspection Procedure (PR-006)](PR-006-pos-device-inspection.md)
  - [User Access Management Procedure (PR-001)](PR-001-user-access.md)

---

*This document is a simulation for educational and portfolio purposes only.*
