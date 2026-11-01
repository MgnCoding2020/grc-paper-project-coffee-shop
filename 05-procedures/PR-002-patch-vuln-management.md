# Patch and Vulnerability Management Procedure
Burn and Churn Coffee

---

## Document Control
**Owner:** Business Owner | **Performed by:** IT Technician | **Approved by:** Business Owner | **Effective:** 2026-11-01 | **Review:** Annually, or when systems change | **Version:** 2.0

---

## 1. Purpose
Keep every system and device updated, so known weaknesses are fixed before someone uses them. This procedure carries out §4 of the [IT Operations Policy (P-006)](../04-policies/P-006-it-operations.md). It implements NIST SP 800-53 **SI-2 (Flaw Remediation)** and supports PCI DSS **6.3.3** (critical and high-security updates installed within one month of release).

---

## 2. Roles

| Role | Responsibility |
|---|---|
| **Owner** | Approves delayed updates (§7) and any update that needs the store closed |
| **IT Administrator** (Vertex IT Support until 2026-11-15, then the IT Technician) | Watches for updates, installs them, checks the result, keeps the maintenance log |
| **Store Manager** | Agrees update times for anything used at the counter; reports devices behaving oddly |

---

## 3. What Gets Updated, and How

| Category | Examples | Who updates | How we check |
|---|---|---|---|
| **Cloud services** | Microsoft 365, Toast cloud, xtraCHEF, Northwind | The vendor | Read the vendor's notices and service health page; act on any customer step they ask for |
| **POS terminal** | Toast terminal POS-01 | Toast pushes updates | Confirm the terminal is on the current version after each update; never update during service |
| **Network equipment** | Router, firewall, access points | IT Technician (router: the internet provider) | Check for firmware monthly; back up the configuration first; install in the update window |
| **Computers and tablets** | Manager laptop, two tablets | Automatic updates; IT Technician checks | Monthly check that updates are installing; after CR-001, Intune update schedules if licensed |
| **Connected devices** | Cameras, espresso machine, temperature sensors, music speaker (as added to the [equipment register](../01-asset-inventory/equipment-register.csv)) | The device vendor or the IT Technician | Automatic updates on where offered; monthly check of the vendor portal; vendor remote updates recorded |

Devices are identified by their tag in the [equipment register](../01-asset-inventory/equipment-register.csv).

---

## 4. Finding Out About Updates
The IT Technician checks, at least monthly and whenever a vendor sends a security notice:
  - vendor security notices and service health pages
  - each device's update or firmware page
  - security alerts from the productivity suite
  - incidents and log reviews ([PR-004](PR-004-log-review.md)) that point to a weakness

---

## 5. How Fast

| Update | Deadline |
|---|---|
| Fixes a weakness that is **actively being exploited** | As soon as possible, as an **emergency change**, recorded within one business day |
| **Critical or high** severity security update | Within **one month** of release (PCI DSS 6.3.3) |
| Other security updates and feature updates | The next monthly update window |

Severity comes from the vendor's own rating. If the vendor gives none, the IT Technician rates it and records why.

---

## 6. The Monthly Update Window

| | |
|---|---|
| **When** | Once a month, in the IT Technician's scheduled block after close, in the week after Microsoft's monthly security release (the second Tuesday) |
| **Before** | Back up network device configurations; check nothing is pending on the POS terminal (never update it with offline payments waiting, [PR-005](PR-005-contingency-plan.md)) |
| **During** | Install, restart, then check the device works: card test transaction on the POS terminal, internet and Wi-Fi on the network, a sign-in on the laptop |
| **After** | Record every update in the [maintenance log](../01-asset-inventory/maintenance-log.csv); update the firmware or version column in the equipment register |
| **If it goes wrong** | Roll back to the previous version or the saved configuration; tell the Store Manager before opening; record it |

Firewall rule changes are **not** updates: they go through a change record ([P-005](../04-policies/P-005-network-security.md) §6).

---

## 7. When an Update Can't Be Installed on Time
Record in the maintenance log: the update, why it's delayed, the temporary protection (for example, turning off the affected feature or isolating the device on its own network segment), and the new date. The Owner approves it. A delay of more than one month is added to the POA&M.

---

## 8. Vulnerability Scanning
There is no vulnerability scanning yet. Scanning and penetration testing are tracked separately under RA-5 (POAM-011).

---

## 9. Records
  - **Maintenance log** ([maintenance-log.csv](../01-asset-inventory/maintenance-log.csv)): one row per update, with date, device, version, who did it and the result. This is the evidence for SI-2 (E-22).
  - **Equipment register** ([equipment-register.csv](../01-asset-inventory/equipment-register.csv)): the current version on each device.

---

## 10. Current Status
  - **No update records exist** from before 2026-11-15: Vertex IT Support kept none. The first recorded update window is the IT Technician's first month (December 2026). Tracked under **POAM-023**.

---

## 11. Related Documents
  - [IT Operations Policy (P-006)](../04-policies/P-006-it-operations.md)
  - [Equipment Maintenance and Lifecycle Procedure (PR-010)](PR-010-equipment-lifecycle.md)
  - [IT Administration and Coverage Procedure (PR-008)](PR-008-it-administration.md)
  - [Asset Inventory](../01-asset-inventory/assets.md)
  - [Control Matrix](../03-controls/control-matrix.md)

---

## Revision History

| Version | Date | Change |
|---|---|---|
| 2.0 | 2026-11-01 | Rewritten under the IT Operations Policy (P-006): update categories including network and connected devices, PCI DSS 6.3.3 one-month deadline for critical and high updates (replaces "preferably within 7 days" and "typically within 30 days"), monthly update window after close, maintenance log as the record, delays approved by the Owner. The earlier version had no document control; it is in the git history |

---

*This document is a simulation for educational and portfolio purposes only.*
