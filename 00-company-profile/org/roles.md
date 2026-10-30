# Roles and Responsibilities
Burn and Churn Coffee

---

## Purpose

This page defines every role in the Burn and Churn Coffee security program, who holds it, and who is responsible for each security activity. Named people are listed in [people.csv](people.csv); this page describes what their roles mean.

---

## Headcount

20 active store staff, plus a part-time IT Technician:

| Role | Count | People |
|---|---|---|
| Owner | 1 | Olivia Carter |
| Store Manager | 1 | Daniel Lopez |
| Shift Leader | 3 | Mia Chen, Marcus Hill, Sofia Patel |
| Barista | 15 | See [people.csv](people.csv) |
| IT Technician (part-time) | 1 | Riley Morgan (planned hire, CR-003) |

---

## Roles

### Owner
Accountable for the security program. Approves policies, access requests and exceptions; accepts risk; signs the quarterly access review; approves external communications during incidents; owns vendor risk management.

### Store Manager
Runs day-to-day store operations and is the primary incident coordinator. Approves access requests for store systems, reviews store-system access in the quarterly review, and leads security training.

### Shift Leader
Supervises the store during a shift. Supports incident containment on shift, keeps the store running when systems are disrupted, and makes sure staff follow security rules.

### Barista
Uses the Toast POS register and follows the Acceptable Use Policy. Reports suspicious activity, lost devices and suspected incidents immediately.

### IT Technician (part-time, from CR-003)
Creates, changes and removes accounts; administers the Microsoft 365 tenant, devices and store network; exports evidence for access reviews; handles the technical side of incidents. Holds a separate admin account for privileged work.

### Vendors (before CR-003)
Until 2026-11-15, IT administration was performed by **Vertex IT Support** (V-004), a managed service provider. Older documents that name an "IT Admin" or "System Administrator" mean Vertex for records dated before 2026-11-15 and the IT Technician after it, with the Owner accountable throughout.

---

## RACI

R = Responsible, A = Accountable, C = Consulted, I = Informed.

| Activity | Owner | Store Manager | Shift Leaders | IT Technician | Baristas |
|---|---|---|---|---|---|
| Approve access requests | **A** | R (store systems) | C | I | — |
| Create, change and remove accounts | A | C | — | **R** | — |
| Quarterly access review | **A** | R (reviewer, store systems) | C | C (evidence export only) | — |
| Vendor risk management | **A/R** | C | — | C | — |
| Incident response | **A** | R (store) | R (on shift) | R (technical) | I (report) |
| Network and firewall administration | A | I | — | **R** | — |
| Security training | A | **R** | R | C | Participate |
| Vendor guest access (sponsor, grant, remove) | **A** (sponsor) | C | — | **R** | — |
| Policy ownership and approval | **A/R** | C | — | C | I |

---

## Separation of Duties

- The IT Technician creates and changes accounts but **never certifies their own access**. The Owner and Store Manager sign the quarterly review; the IT Technician only exports the data.
- Only the Owner and the IT Technician hold admin accounts, and those accounts are separate from their everyday accounts.

---

## Accounts

| Account type | Pattern | Who | Notes |
|---|---|---|---|
| Everyday account | `first.last@burnandchurncoffee.com` | Every employee | No admin roles |
| Admin account | `adm-first.last@burnandchurncoffee.com` | Owner, IT Technician | Least-privilege admin roles only; MFA required |
| Break-glass account | `bg-admin-01`, `bg-admin-02` | Emergency use only | Excluded from MFA enforcement policies; credentials sealed with the Owner; every sign-in reviewed |
| Vendor guest account | B2B guest, invited by email | Named vendor contacts in [vendor-contacts.csv](vendor-contacts.csv) | Member of `grp-bc-vendors` only; least privilege; time-bound (access_end); sponsored by the Owner; no generic vendor accounts (P-001 §5.7) |

`burnandchurncoffee.com` is fictional. The live tenant uses its own domain, which is kept out of this repository.

---

## Toast POS PINs

- Every store employee has a **personal Toast PIN**, because everyone is trained on the register.
- Only **one employee is signed in** to a terminal at a time, and that employee is **accountable for every action** taken while signed in.
- Employees **sign out when they leave the register**, and an idle auto-logout backs this up.
- Employees **never use another employee's PIN**.
- PINs are not multi-factor authentication. Toast cashier logins are outside MFA scope by design; the rules above are the compensating controls.

---

## Role Names in Older Records

Records written before 2026-10-30 use some different role names. They mean the same roles:

| Older name | Role on this page |
|---|---|
| Business Owner | Owner |
| Employee, Clerk | Barista |
| IT Admin, System Administrator, IT Vendor | Vertex IT Support before 2026-11-15; IT Technician after |

---

*This document is a simulation for educational and portfolio purposes only.*
