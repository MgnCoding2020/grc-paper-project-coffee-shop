# Mobile Device and Personal Phone Policy
Burn and Churn Coffee

## Document Control
**Policy Owner:** Business Owner | 
**Approved by:** Business Owner | 
**Effective Date:** 2026-11-15 (with the Microsoft 365 cutover, CR-001) | 
**Review Frequency:** Annual, or when device management (Intune) is licensed | 
**Version:** 1.0

----------

## 1. Purpose
From the Microsoft 365 cutover, every employee signs in with multi-factor authentication (MFA), and most will use the Microsoft Authenticator app on **their own phone**. This policy sets out what a personal phone may and may not be used for, what staff can expect from the company in return, and what happens when a phone is lost or someone leaves.

It implements NIST SP 800-53 **AC-19 (Access Control for Mobile Devices)** and supports IA-2 (MFA).

-----------

## 2. Scope
  - Personal phones used for company sign-in (Authenticator) or to read company email, Teams or files
  - Company tablets (TAB-01, TAB-02) and the manager laptop are company devices, covered by the [IT Operations Policy (P-006)](P-006-it-operations.md)

-----------

## 3. What a Personal Phone May Be Used For

| Use | Allowed? |
|---|---|
| **Microsoft Authenticator** for MFA sign-in | Yes, and recommended. The app holds no company data |
| Teams or Outlook on the phone (Owner, Store Manager, Shift Leaders) | Yes, if the phone has a screen lock (PIN, fingerprint or face) and current updates |
| Viewing the shift schedule and SOPs on the intranet | Yes, in the browser or Teams |
| **Downloading** company files (payroll, bookkeeping workbook, staff records) to the phone | **No.** View them in the browser or app, don't save copies |
| Photographing card details, receipts with card data, or screens showing them | **Never** ([P-004](P-004-payment-card-data-protection.md)) |
| Pairing with store devices (speaker, cameras, POS) | **No** ([PR-011](../05-procedures/PR-011-connected-devices.md)) |
| Connecting to the staff or Devices Wi-Fi | **No.** Personal phones use the guest Wi-Fi ([P-005](P-005-network-security.md)) |

-----------

## 4. Employee Responsibilities
  1. Keep a **screen lock** on the phone and install updates.
  2. Never approve an MFA prompt you didn't start. Number matching shows a code to type; if you didn't sign in, deny it and tell the Store Manager ([IRP-002](../06-incident-playbooks/IRP-002-account-compromise.md)).
  3. **Report a lost, stolen or replaced phone the same day**, so the IT Technician can remove it from your account and you can register the new one.
  4. Don't share your phone's Authenticator with anyone else.

-----------

## 5. What the Company Will and Won't Do
  - The company **doesn't manage, track or wipe personal phones.** It doesn't install device management on them and can't see personal content.
  - It **can** remove the phone as a sign-in method, sign the account out of company apps, and (once licensed) remove company data from the Outlook and Teams apps only.
  - **Nobody is required to use a personal phone.** Anyone who prefers not to gets a **company-provided FIDO2 security key** (a small USB or NFC key) instead, at no cost to them.

-----------

## 6. Leaving the Company
On the last day, the IT Technician disables the account and removes every registered MFA method ([PR-001](../05-procedures/PR-001-user-access.md)). The employee deletes the work account from Authenticator, Outlook and Teams, and returns any security key.

-----------

## 7. Later: Device Management
If Intune is licensed (D-9 trial or later), app protection policies can stop copying company data out of Outlook and Teams on personal phones, still without managing the phone. This policy is reviewed then.

-----------

## 8. Current Status
Takes effect with the Microsoft 365 cutover (2026-11-15). Staff acknowledge it in the first training session ([PR-007](../05-procedures/PR-007-security-awareness-training.md), by 2026-11-30). Tracked under **POAM-031**.

-----------

## 9. Related Documents
  - [Access Management Policy (P-001)](P-001-access-control.md)
  - [Acceptable Use Policy (P-002)](P-002-acceptable-use.md)
  - [Microsoft 365 Tenant Security Baseline (PR-013)](../05-procedures/PR-013-m365-tenant-baseline.md)
  - [Lost or Stolen Device Playbook (IRP-004)](../06-incident-playbooks/IRP-004-lost-stolen-device.md)

-----------

*This document is a simulation for educational and portfolio purposes only.*
