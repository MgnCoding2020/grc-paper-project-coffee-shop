# IRP-006: Vendor Breach Notification Playbook
Burn and Churn Coffee

## Document Control
**Playbook Owner:** Business Owner | 
**Approved By:** Business Owner | 
**Effective Date:** 2026-11-01 | 
**Review Frequency:** Annual, after any vendor breach, and when a vendor is added or removed | 
**Version:** 1.0

---

## 1. Purpose
Guide the response when one of the shop's vendors says it has been breached, or a breach is reported in the news. The shop can't fix the vendor's systems, but it can protect its own accounts, data, staff and customers, and decide whether to keep the vendor.

---

## 2. Scope
Every vendor in [vendors.csv](../00-company-profile/org/vendors.csv), especially those that hold sensitive data or can reach the shop's systems: Toast (payments), Microsoft (email, files, identity), Northwind (payroll, once onboarded), the password manager, and the camera, espresso and temperature services.

---

## 3. How This Playbook Follows NIST
Steps follow the NIST Cybersecurity Framework 2.0 functions, as [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) recommends, and connect incident response to third-party risk management (NIST SP 800-53 SA-9, the supply chain outcomes in CSF 2.0's Govern function).

| CSF 2.0 function | In this playbook |
|---|---|
| Govern, Identify | §4 Vendor notification commitments; vendor assessments (before an incident) |
| Detect | §6 Step 1 |
| Respond | §6 Steps 2 to 5 |
| Recover | §6 Step 6 |
| Identify (improvement) | §6 Step 7, §9 |

---

## 4. Vendor Notification Commitments
How quickly each vendor has promised to tell the shop, from the vendor assessments. Gaps are open findings.

| Vendor | What it holds | Promised notification | Source |
|---|---|---|---|
| V-001 Toast | Card payments, sales, staff PINs | **Unknown:** the service agreement hasn't been located | VRA-V001:F-03 (open) |
| V-002 Northwind | Payroll and staff personal data | **Not defined** in the contract | VRA-V002:F-03 (open) |
| V-003 Microsoft | Email, files, staff accounts | 72 hours, in the Data Protection Addendum | VRA-V003 assessment |
| V-009 Bitwarden | Shared admin credentials (end-to-end encrypted; the vendor can't read them) | Standard terms only; no negotiated timeline | VRA-V009:F-05 (open) |
| V-015 Google (the Owner's password manager) | Break-glass passwords and admin recovery codes | Consumer terms only; no negotiated timeline. **On any notice: rotate both break-glass passwords and regenerate the recovery codes the same day** | VRA-V015 (due 2026-11-25, POAM-038) |
| V-011 Espresso machine service company | Machine telemetry; remote access to the machine | **No timeline:** "without undue delay" | VRA-V011:F-04 (open; 72-hour clause at renewal, 2027-01-15) |
| V-010 Cloud camera service | Video of customers and staff | 72 hours, in the terms of service | VRA-V010 assessment |
| V-012 Temperature monitoring service | Temperature log | **No timeline:** "prompt" | VRA-V012:F-04 (open) |
| V-008 Internet service provider | Traffic in transit (encrypted by the services using it); the router | **None** in the contract | VRA-V008:F-04 (open) |

---

## 5. Severity
| Severity | Example |
|---|---|
| Low | Breach at a vendor with no access to company data or systems |
| Medium | Vendor breach that may include company account details or business data |
| **High** | Card data, staff personal data or admin credentials possibly exposed; or the vendor can reach company systems (remote access, an integration) |

---

## 6. Response Steps

### Step 1: Detect and verify (Detect)
  - A breach notice arrives by email, letter or in the news. **Check it's genuine before acting on it:** fake breach notices are a common phishing lure. Go to the vendor's official website, status page or a known phone number. **Never use links or numbers in the notice itself.**
  - Tell the Owner. Open an incident `INC-###`.

### Step 2: Understand the exposure (Respond)
From [vendors.csv](../00-company-profile/org/vendors.csv), [systems.csv](../00-company-profile/org/systems.csv) and the vendor's notice:
  - which company data the vendor holds, and whose (customers, staff, card data)
  - which company accounts, integrations or remote access the vendor has
  - when the breach happened and what the vendor says was taken

Ask the vendor in writing for anything missing, and record the answers.

### Step 3: Contain on the shop's side (Respond)
  - **Change every credential** the shop uses with that vendor (stored in the password manager, [PR-009](../05-procedures/PR-009-credential-vault.md)), and turn on MFA if it wasn't already.
  - **Pause the vendor's access** to company systems: guest accounts ([CR-004](../09-change-management/CR-004-vendor-guest-access.md)), remote access to devices ([PR-011](../05-procedures/PR-011-connected-devices.md) §4), integrations.
  - **Warn staff** to expect phishing that pretends to be the vendor ([IRP-001](IRP-001-phishing.md)).
  - Vendor-specific checks:
    - **Toast:** watch for unusual refunds and transactions ([IRP-003](IRP-003-pos-suspicious-activity.md)); follow Toast's instructions.
    - **Microsoft:** review the audit and sign-in logs for the affected period ([PR-004](../05-procedures/PR-004-log-review.md)).
    - **Northwind:** freeze bank-detail changes until each one is verified by phone ([IRP-007](IRP-007-payment-payroll-fraud.md)).
    - **Password manager:** rotate every stored credential, starting with network admin logins.

### Step 4: Decide who must be told (Respond)
The Owner decides, with legal advice where personal data is involved ([P-003](../04-policies/P-003-incident-response.md) §9):
  - **Card data:** if card data may be involved, the payment processor leads; the shop follows its instructions.
  - **Staff:** if staff personal data was exposed (for example, payroll), staff are told what happened and what to watch for.
  - **Customers and authorities:** only where the law or a contract requires it.

### Step 5: Record (Respond)
Record everything in the incident log, including the vendor's own timeline. If the vendor told the shop later than it promised (§4), that's a finding for the vendor assessment.

### Step 6: Recover (Recover)
  - Restore any vendor access only after the vendor confirms the breach is contained, and with new credentials.
  - If data was lost, restore it from the shop's own backups ([PR-012](../05-procedures/PR-012-backup-and-recovery.md)).

### Step 7: Reassess the vendor (Identify)
Re-run or update the vendor's assessment in the [Vendor Risk Assessment Lab](https://github.com/MgnCoding2020/Vendor-Risk-Assessment-Lab). The outcome is one of: continue, continue with conditions, or exit (a change record, like the Toast exit under CR-005). Update the risk register.

---

## 7. Roles
| Role | Does |
|---|---|
| Owner | Accountable; vendor contact; decides notifications and whether to keep the vendor |
| IT Technician | Rotates credentials, pauses access, reviews logs |
| Store Manager | Briefs staff; watches for fraud at the counter |

---

## 8. Records
Incident log entry (`INC-###`) with: the notice (copy), how it was verified, data and access involved, credentials rotated, notifications made, vendor timeline, decision on the vendor.

---

## 9. Prevention (Govern, Identify, Protect)
  - Assess every vendor before onboarding and every year (SA-9; Vendor Risk Assessment Lab)
  - Get breach-notification terms into every contract (close VRA-V001:F-03 and VRA-V002:F-03)
  - Least privilege and time limits for vendor access (P-001 §5.7, MA-4)
  - Unique, generated credentials per vendor, in the password manager (IA-5)
  - Own backups of data held by vendors (CP-9)

---

## 10. Related Controls
IR-4, IR-8, SA-9, IA-5, MA-4, CP-9

---

## 11. Related Documents
  - [Incident Response Policy (P-003)](../04-policies/P-003-incident-response.md)
  - [Vendor inventory](../02-risk-management/vendor-risk-management/vendor-inventory.md)
  - [Phishing Playbook (IRP-001)](IRP-001-phishing.md)
  - [Payment and Payroll Fraud Playbook (IRP-007)](IRP-007-payment-payroll-fraud.md)
  - [Shared Credential Management Procedure (PR-009)](../05-procedures/PR-009-credential-vault.md)

---

*This document is a simulation for educational and portfolio purposes only.*
