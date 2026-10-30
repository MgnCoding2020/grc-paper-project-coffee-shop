# Contingency and Outage Plan
Burn and Churn Coffee

---

## Document Control
**Owner:** Business Owner | **Approved by:** Business Owner | **Effective:** 2026-10-30 | **Review:** Annually, after any outage longer than one business day, and after any change to payment or network systems | **Version:** 1.0

---

## 1. Purpose
This plan keeps the store trading, and keeps card payments safe, when a system the store depends on is unavailable. It implements NIST SP 800-53 **CP-2 (Contingency Plan)** and is the "Business Continuity procedure" referred to in the Incident Response Policy (P-003 §2).

**Responsibility:** Toast keeps its own platform running, but **the shop owns its response to an outage**. Toast's Offline Mode lets terminals keep taking card payments, and the shop carries the risk of any payment that is declined afterwards.

---

## 2. Roles

| Role | During an outage |
|---|---|
| Shift Leader on shift | Declares the outage, switches the store to the outage procedure, informs the Store Manager |
| Store Manager | Coordinates; decides on cash-only; contacts the IT administrator and vendors |
| IT administrator | Diagnoses network and device problems; contacts the internet provider; restores service |
| Owner | Approves any decision with financial or customer impact; approves external communication |

Contact details for Toast support, the internet service provider (V-008) and the IT administrator are kept in the store's printed outage card (not in this repository).

---

## 3. Scenarios and Responses

| # | Scenario | Response |
|---|---|---|
| 1 | **Internet outage** (provider down, router failure) | Toast terminals switch to **Offline Mode** automatically; follow the offline payment rules (§4). IT administrator contacts the internet provider. If cellular failover is installed (§5), it takes over |
| 2 | **Toast cloud outage** | Same as 1: Offline Mode. Check Toast's status page; don't troubleshoot the terminals |
| 3 | **Power or local network outage** | Terminals on battery keep working offline if possible; otherwise **cash only** with handwritten order slips (no card data on them) |
| 4 | **One terminal fails** | Use the remaining device; contact Toast support for a replacement; follow PR-006 before any replacement terminal goes into service |
| 5 | **Email and documents unavailable** (Google Workspace now; Microsoft 365 after CR-001) | Store keeps trading (sales don't depend on it). Use the printed outage card for contacts |
| 6 | **Key person unavailable** (Owner or IT administrator) | Store Manager acts; break-glass accounts exist for emergency admin access after CR-001 |

---

## 4. Offline Payment Rules (Toast Offline Mode)
From Toast's own guidance (checked 2026-10-30):

  - Offline card payments are stored on the terminal and sent for authorization **when it reconnects**. They can be **declined after the customer has left**; the shop absorbs those losses.
  - **Offline limit:** a per-transaction limit for offline card payments is set in Toast Web. **Owner decision (2026-10-30): $50**, which covers normal orders while limiting decline losses.
  - Staff check the cardholder's name and the card's expiry date, and keep the merchant copy of each receipt.
  - **Never clear a terminal's memory, uninstall the app or factory-reset a terminal while payments are pending.** Pending offline payments that are lost can't be recovered.
  - Gift cards and loyalty redemptions don't work offline.
  - Reconnect as soon as possible: card authorizations can expire, and the longer a terminal stays offline, the larger the decline risk.

**Never** write down card numbers or take manual card imprints as a fallback (Payment Card Data Protection Policy, P-004 §3). Cash, which the shop accepts every day, is the fallback.

---

## 5. Options Considered

| Option | Decision | Why |
|---|---|---|
| Toast Offline Mode with a $50 limit | **Adopted** | Built in; no extra vendor; risk capped |
| Cellular failover internet (backup router or Toast's cellular router service) | **Recommended; Owner to decide on cost** | Toast recommends cellular backup to avoid declined payments; keeps terminals online. Must connect through the store firewall so segmentation (P-005) still applies |
| Cash only | **Adopted as the last fallback** | Cash is accepted every day, so staff already know the till; always available; no card data risk |
| A second card reader on a different payment processor | **Rejected for now** | Adds a second PCI service provider, contract and PCI DSS 12.8 obligations, and staff training, for a rare event |
| Writing down card numbers or manual imprints | **Prohibited** | Stores cardholder data on paper (P-004 §3) |

Mobile wallets (for example Apple Pay) are payment methods, not a backup: they run through the same Toast terminal and processor.

---

## 6. Recovery
  1. Confirm terminals are back online and **pending offline payments have uploaded**.
  2. Reconcile: any check reopened by a declined offline payment is resolved by the Store Manager; losses are recorded.
  3. Record the outage in the incident log (`INC-###`; an extended outage affecting sales is High severity under P-003 §5).
  4. If the outage lasted more than one business day, review this plan.

---

## 7. Data Recovery
Business data lives in vendor-managed cloud services (Toast, Google Workspace now, Microsoft 365 after CR-001) that run their own backups. After CR-001, SharePoint version history and the recycle bin cover accidental deletion of company documents. The shop does not run its own backup system.

---

## 8. Testing and Training
  - **Tabletop exercise** at least annually: walk the store team through scenario 1. The first is planned for December 2026, after the Microsoft 365 cutover. (Formal contingency plan testing is NIST CP-4, not yet in the control matrix.)
  - Outage procedure and offline payment rules are part of security awareness training (PR-007).

---

## 9. Current Status
  - Plan documented; **not yet tested**.
  - Offline limit decided; setting it in Toast Web is to be confirmed and recorded.
  - Cellular failover: not installed (decision pending).

These are tracked under **POAM-005**.

---

## 10. Related Documents
  - [Incident Response Policy (P-003)](../04-policies/P-003-incident-response.md)
  - [Payment Card Data Protection Policy (P-004)](../04-policies/P-004-payment-card-data-protection.md)
  - [Network Security Policy (P-005)](../04-policies/P-005-network-security.md)
  - [POS Device Inspection Procedure (PR-006)](PR-006-pos-device-inspection.md)
  - [Security Awareness Training Program (PR-007)](PR-007-security-awareness-training.md)

### Sources (checked 2026-10-30)
  - [Toast: Prepare to Operate in Offline Mode](https://support.toasttab.com/en/article/Prepare-to-Operate-in-Offline-Mode-During-Service-Disruptions-or-Outages)
  - [Toast: Use Toast in Offline Mode](https://support.toasttab.com/en/article/Using-Toast-in-Offline-Mode?lang=en_US)
  - [Toast blog: POS outages](https://pos.toasttab.com/blog/on-the-line/pos-outage) (cellular backup recommendation)

---

*This document is a simulation for educational and portfolio purposes only.*
