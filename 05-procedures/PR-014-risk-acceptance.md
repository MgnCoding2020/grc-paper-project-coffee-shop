# Risk Acceptance and Exception Procedure
Burn and Churn Coffee

---

## Document Control
**Owner:** Business Owner | **Approved by:** Business Owner | **Effective:** 2026-11-02 | **Review:** Annually | **Version:** 1.0

---

## 1. Purpose
Sometimes the shop can't meet a policy requirement yet: the licence it has doesn't support a feature, a vendor has no audit report, or a fix is waiting on a project. Many documents in this program say "the Owner approves an exception". This procedure says how: in writing, with compensating controls, with an end date, and in one register so nothing is accepted quietly and forgotten.

It implements NIST SP 800-53 **RA-7 (Risk Response)**.

---

## 2. When an Exception Is Needed
  - A policy requirement can't be met, now or for a known period
  - A vendor can't meet a required contract clause or security requirement ([P-008](../04-policies/P-008-third-party-risk.md) §8)
  - A POA&M item will miss its date and the risk stays in the meantime
  - A residual risk in the risk register is accepted rather than reduced

An exception is **not** needed for an item already being fixed on schedule in the POA&M.

---

## 3. Steps
  1. **Request:** whoever finds the gap (usually the IT Technician) writes it up: which requirement, why it can't be met, what could go wrong, and which compensating controls reduce the risk.
  2. **Rate:** the residual risk, using the [risk register's](../02-risk-management/risk-register.md) method.
  3. **Decide:** **only the Owner** can accept a risk. A High residual risk is accepted only with a fix date, not indefinitely.
  4. **Record:** an `EXC-###` row in the [exception register](../02-risk-management/risk-exceptions.md), with the approval date and an **expiry no more than 12 months away**.
  5. **Review:** at expiry, and at least every six months, the Owner renews, changes or closes the exception. An expired exception is a finding. The monthly program monitor lists exceptions expiring soon.
  6. **Close:** when the requirement is met, the row is marked closed with the date and evidence. It is never deleted.

---

## 4. Current Status
The register starts with six exceptions the program had already accepted in other documents, now recorded in one place and approved by the Owner on 2026-11-02. Tracked under **POAM-034**.

---

## 5. Related Documents
  - [Exception register](../02-risk-management/risk-exceptions.md)
  - [Risk register](../02-risk-management/risk-register.md)
  - [POA&M](../07-evidence-pack/poam/poam.md)
  - [Third-Party Risk Management Policy (P-008)](../04-policies/P-008-third-party-risk.md)

---

*This document is a simulation for educational and portfolio purposes only.*
