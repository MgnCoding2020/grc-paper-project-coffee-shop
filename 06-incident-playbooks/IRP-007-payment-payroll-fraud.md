# IRP-007: Payment and Payroll Fraud Playbook (Business Email Compromise)
Burn and Churn Coffee

## Document Control
**Playbook Owner:** Business Owner | 
**Approved By:** Business Owner | 
**Effective Date:** 2026-11-01 | 
**Review Frequency:** Annual, and after any fraud attempt | 
**Version:** 1.0

---

## 1. Purpose
Guide the response to fraud that tricks someone into sending money to a criminal, usually by email or text pretending to be someone the shop trusts. It's the most common way small businesses lose money to cybercrime, and it often needs no hacking at all: just a convincing message and a rushed decision.

---

## 2. Scope
| Scenario | What it looks like |
|---|---|
| **Payroll diversion** | An "employee" emails asking to change the bank account their pay goes to |
| **Fake supplier invoice** | A "supplier" sends an invoice, or says its bank details have changed |
| **Boss impersonation** | The "Owner" urgently asks the Store Manager to pay something, or buy gift cards, "before end of day" |
| **Hijacked email thread** | A real conversation with a supplier is taken over and the payment details are switched |

Refund and transaction fraud at the POS follows [IRP-003](IRP-003-pos-suspicious-activity.md). A compromised company mailbox also follows [IRP-002](IRP-002-account-compromise.md).

---

## 3. How This Playbook Follows NIST
Steps follow the NIST Cybersecurity Framework 2.0 functions, as [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) recommends. Prevention (§9) matters most here: the controls that stop this fraud are business rules and training, not technology.

| CSF 2.0 function | In this playbook |
|---|---|
| Govern, Protect | §9 Prevention rules |
| Detect | §4 Warning signs, §6 Step 1 |
| Respond | §6 Steps 2 to 4 |
| Recover | §6 Step 5 |
| Identify (improvement) | §6 Step 6 |

---

## 4. Warning Signs
  - **Any request to change bank details**, for staff pay or a supplier
  - Urgency or secrecy: "today", "I'm in a meeting, just do it", "don't tell anyone"
  - Gift cards, unusual payment methods, or a new account in another name or country
  - A sender address that's almost right (a swapped letter, a different domain), or a reply-to address that differs from the sender
  - A known person writing in an unusual way, or a request that skips the normal approval

---

## 5. Severity
| Severity | Example |
|---|---|
| Low | Attempt spotted and stopped; no money moved. **Still recorded:** attempts show where the shop is being targeted |
| Medium | Bank details changed in a system, but no payment made yet |
| **High** | Money sent to the criminal; or a company mailbox was used to send the fraud |

---

## 6. Response Steps

### Step 1: Stop and report (Detect)
Don't reply, don't click, don't pay. Tell the Owner or Store Manager straight away. If a payment has already been sent, **go straight to Step 2: minutes matter.**

### Step 2: If money was sent, call the bank now (Respond)
  - The Owner calls the company's bank **immediately**, on the number on the bank card or the bank's website, and asks it to **recall the payment** and contact the receiving bank. The sooner this happens, the better the chance of getting money back.
  - Report it to the FBI's [Internet Crime Complaint Center (IC3)](https://www.ic3.gov), whatever the amount, with the dates, amounts, bank names and account numbers.

### Step 3: Contain (Respond)
  - **Undo any changed bank details** in payroll or supplier records, and verify the correct details by phone.
  - **Check the company mailbox** that received or sent the messages for signs it was taken over: forwarding rules, unknown sign-ins, sent items nobody wrote. If anything looks wrong, follow [IRP-002](IRP-002-account-compromise.md).
  - **Warn the person or supplier being impersonated**, by phone. Their own email may be compromised.
  - **Tell staff** about the attempt so they recognise the next one.

### Step 4: Keep the evidence (Respond)
Save the emails, with full headers if possible, texts, invoices, bank confirmations and call notes. Record the incident as `INC-###` in the [incident log](../07-evidence-pack/artifacts/monitoring/incident-log.md).

### Step 5: Recover (Recover)
  - **Payroll diversion:** pay the employee their correct wages; their pay doesn't wait for the fraud to be resolved.
  - **Supplier fraud:** confirm with the real supplier what is actually owed, and agree how to settle it.
  - Record any money recovered, and any loss, for the Owner and the bookkeeping workbook.

### Step 6: Lessons learned (Identify)
Why did the request look real, and which rule in §9 would have stopped it, or did stop it? Update training and the rules.

---

## 7. Roles
| Role | Does |
|---|---|
| Any employee | Never acts on a payment or bank-detail request alone; reports it |
| Store Manager | Verifies and escalates; briefs staff |
| Owner | Calls the bank; reports to IC3; approves all payments and bank changes |
| IT Technician | Checks mailboxes and sign-ins; removes forwarding rules |

---

## 8. Records
Incident log entry, including attempts that were stopped: date, scenario, how it arrived, who spotted it, whether money moved, bank and IC3 reference numbers, money recovered, loss.

---

## 9. Prevention Rules (Govern, Protect)
These are company rules, taught in [training (PR-007)](../05-procedures/PR-007-security-awareness-training.md):
  1. **Call back to verify.** Any change to bank details, for an employee or a supplier, is confirmed by phone on a number the shop already has. Never use the number in the request.
  2. **Two people for bank changes.** The person who receives the request doesn't make the change alone; the Owner approves every change to bank details.
  3. **Employees change their own pay details** only through the payroll provider's own portal, or in person with the Owner. Never by email.
  4. **No gift cards and no urgent payments by email or text**, whoever it seems to come from.
  5. **New suppliers** are checked before their first payment; supplier bank details are confirmed when first set up.
  6. **Mailbox protection:** MFA on every account (IA-2), and alerts on new forwarding rules once licensed.

---

## 10. Related Controls
IR-4, IR-8, AT-2 (training, including social engineering), IA-2, AC-2

---

## 11. Related Documents
  - [Incident Response Policy (P-003)](../04-policies/P-003-incident-response.md)
  - [Phishing Playbook (IRP-001)](IRP-001-phishing.md)
  - [Account Compromise Playbook (IRP-002)](IRP-002-account-compromise.md)
  - [Vendor Breach Notification Playbook (IRP-006)](IRP-006-vendor-breach.md)
  - [Security Awareness Training Program (PR-007)](../05-procedures/PR-007-security-awareness-training.md)

---

*This document is a simulation for educational and portfolio purposes only.*
