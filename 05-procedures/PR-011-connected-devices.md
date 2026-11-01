# Connected Devices Procedure (Cameras and Other Smart Devices)
Burn and Churn Coffee

---

## Document Control
**Owner:** Business Owner | **Performed by:** IT Technician (cameras: Store Manager for day-to-day use) | **Approved by:** Business Owner | **Effective:** 2026-11-01 | **Review:** Annually, or when a device is added | **Version:** 1.0

---

## 1. Purpose
The shop has several "smart" devices that connect to the internet: security cameras, a connected espresso machine that its service company monitors remotely, fridge temperature sensors for food safety, and a music speaker. Each one is a small computer on the store network, often with a default password and firmware nobody updates, and some let a vendor reach in from outside.

This procedure keeps them on their own network segment, under the company's control, and out of reach of the payment system. It supports NIST SP 800-53 **SC-7** (boundary protection), **CM-8** (inventory), **SI-2** (updates), **IA-5** (credentials), **MA-4** (nonlocal maintenance) and **PE-6** (monitoring physical access).

---

## 2. The Devices

| Device | Tag | Vendor | What it connects to | Data it holds |
|---|---|---|---|---|
| Security cameras (2) | CAM-01, CAM-02 | Cloud camera service (V-010) | The camera vendor's cloud, where video is recorded | Video of customers and staff (Confidential, DATA-005) |
| Connected espresso machine | ESP-01 | Espresso machine service company (V-011) | The service company's cloud, for usage data, fault alerts and remote diagnostics | Machine settings and usage counts |
| Fridge temperature sensors (2) | TMP-01, TMP-02 | Temperature monitoring service (V-012) | The monitoring service's cloud, which keeps the food-safety temperature log and sends alerts | Temperature readings |
| Music speaker | SPK-01 | None beyond the maker's app | The internet, for music streaming | None |

Every device is in the [equipment register](../01-asset-inventory/equipment-register.csv) and has a row in the [connected device checklist](../07-evidence-pack/artifacts/iot/connected-device-checklist.csv).

---

## 3. Rules for Every Connected Device
  1. **In the register before it's switched on** ([PR-010](PR-010-equipment-lifecycle.md) §3).
  2. **On the Devices segment only** ([P-005](../04-policies/P-005-network-security.md) §3): internet to its own vendor's cloud, nothing else. It can't reach the POS, staff or management segments, and nothing can reach it from the internet. No port forwarding, and UPnP is off on the router and firewall.
  3. **Default password changed** to a generated one, stored in the password manager ([PR-009](PR-009-credential-vault.md)). Vendor cloud accounts use MFA where offered.
  4. **Company-owned accounts.** The vendor cloud account belongs to the company (the Owner's or the IT Technician's admin email, never a personal account), so access survives staff changes.
  5. **Automatic updates on** where offered; otherwise checked monthly ([PR-002](PR-002-patch-vuln-management.md)).
  6. **Controlled from company devices only.** The speaker and the sensor app are used from the store tablet; staff don't pair personal phones.
  7. **Retired properly:** factory reset, removed from the vendor account and Wi-Fi, register updated ([PR-010](PR-010-equipment-lifecycle.md) §7).

---

## 4. Vendor Remote Access (MA-4)
The espresso machine's service company can run diagnostics remotely, through its own cloud connection.
  - Remote access is allowed only for diagnostics and repairs the shop has asked for, or a fault alert the vendor tells the shop about first.
  - The vendor names the technician; each session is recorded in the [maintenance log](../01-asset-inventory/maintenance-log.csv).
  - If the vendor offers a setting to require the shop's approval for remote sessions, it's turned on.
  - Remote access never extends beyond the espresso machine: the Devices segment rules in §3 still apply.

The same applies to the camera and temperature services if they offer remote support.

---

## 5. Cameras (PE-6)
  - **Where they point:** CAM-01 covers the front door and customer area; CAM-02 covers the back door and stock room. **No camera can see the card reader's keypad, a customer entering a PIN, or the register screen.** The Store Manager checks this when a camera is installed or moved, and once a year, by viewing each camera's picture.
  - **Notice:** a sign at the entrance tells customers and staff that cameras are recording.
  - **Who can watch:** the Owner and the Store Manager, each with their own camera account and MFA. No shared logins.
  - **How long:** recordings are kept for **30 days**, then deleted automatically, unless saved for an incident.
  - **Exporting footage:** only for an incident, an insurance claim or a police request, approved by the Owner and recorded in the incident log ([P-003](../04-policies/P-003-incident-response.md)).
  - Cameras are never used to monitor how individual staff do their jobs.

---

## 6. Temperature Sensors
The temperature log is a food-safety record, so the sensors matter even though they hold no sensitive data. An offline sensor is treated like a fridge fault: the Shift Leader checks the fridge with a manual thermometer and records the reading until the sensor is back.

---

## 7. Current Status (2026-11-01)
  - **The devices were installed by their vendors** when the shop opened, not by Vertex IT Support, and nobody recorded how they were set up.
  - They are on the **staff Wi-Fi**, the same network as the POS terminal and the manager laptop (P-005 §7 exception, POAM-015).
  - **Default passwords: not verified** on any device. **Vendor cloud accounts:** the camera account is shared by the Owner and the Store Manager; the espresso and sensor accounts were set up by the vendors.
  - **Camera views have not been checked** against the keypad rule, and there is no entrance sign or retention setting on record.
  - The [checklist](../07-evidence-pack/artifacts/iot/connected-device-checklist.csv) records each gap. Tracked under **POAM-026** (devices and vendor access) and **POAM-027** (cameras).

---

## 8. Related Documents
  - [Network Security Policy (P-005)](../04-policies/P-005-network-security.md)
  - [IT Operations Policy (P-006)](../04-policies/P-006-it-operations.md)
  - [Equipment Maintenance and Lifecycle Procedure (PR-010)](PR-010-equipment-lifecycle.md)
  - [Shared Credential Management Procedure (PR-009)](PR-009-credential-vault.md)
  - [Payment Card Data Protection Policy (P-004)](../04-policies/P-004-payment-card-data-protection.md)

---

*This document is a simulation for educational and portfolio purposes only.*
