# Device Configuration Baselines
Burn and Churn Coffee

---

## Document Control
**Owner:** Business Owner | **Performed by:** IT Technician | **Approved by:** Business Owner | **Effective:** 2026-11-02 | **Review:** Annually, and when a device type is added | **Version:** 1.0

---

## 1. Purpose
The secure settings for each kind of company device, so every device starts secure, stays that way, and can be checked. With the [Microsoft 365 Tenant Security Baseline (PR-013)](PR-013-m365-tenant-baseline.md), this completes the program's configuration baselines (NIST SP 800-53 **CM-6**, with CM-2). It supports PCI DSS Requirement 2 (secure configurations).

Devices are identified by their tag in the [equipment register](../01-asset-inventory/equipment-register.csv).

---

## 2. Manager Laptop (LAP-01, Windows)
| Setting | Value |
|---|---|
| Disk encryption | **BitLocker on**; recovery key stored in the password manager (PR-009) |
| Daily account | Standard user (no local admin rights); signs in with the Microsoft 365 account after CR-001 |
| Local administrator | Only through a separate admin account used for installs; the built-in Administrator and Guest accounts disabled |
| Sign-in | Strong password or Windows Hello PIN; **screen locks after 5 minutes** |
| Updates | Windows Update automatic; checked in the monthly update window (PR-002) |
| Protection | Microsoft Defender antivirus and Windows Firewall on; tamper protection on |
| Software | Business software only; no personal accounts or games; browsers update automatically |
| Network | Staff Wi-Fi only (P-005) |

## 3. Company Tablets (TAB-01, TAB-02)
| Setting | Value |
|---|---|
| Passcode | **Required**; auto-lock after 2 minutes |
| Encryption | On (the platform default once a passcode is set) |
| Updates | Automatic OS and app updates |
| Apps | Only the apps the shop needs (inventory, Teams, the intranet); installed from the official store; no personal accounts |
| Lost device | "Find my device" on, linked to the company account, so it can be locked or erased (IRP-004) |
| Network | Staff Wi-Fi only |

## 4. POS Terminal (POS-01)
| Setting | Value |
|---|---|
| Software and updates | Managed by the POS vendor; never update during service (PR-002) |
| Sign-in | Personal PINs; one person signed in at a time; idle auto-logout on (`org/roles.md`) |
| Offline payments | Limited as set in the outage plan (PR-005) |
| Other use | Nothing else installed or browsed on it |
| Physical | Inspected daily and monthly (PR-006); on the POS network segment only (P-005) |

## 5. Firewall and Gateway (FW-01)
| Setting | Value |
|---|---|
| Admin account | Default account renamed or disabled; **named admin accounts**; passwords in the password manager |
| Admin access | Only from the management segment, over HTTPS; **remote administration from the internet off** |
| Rules | Default deny between segments; every allow rule written down with its reason (P-005) |
| UPnP and port forwarding | **Off** (P-005 §5) |
| Logging | On; reviewed in the log review (PR-004) |
| Firmware | Current; updated in the monthly update window |
| Configuration backup | After every change (PR-012) |

## 6. Wi-Fi Access Points (AP-01, AP-02)
| Setting | Value |
|---|---|
| Networks | Separate networks for Staff, Guest and Devices (P-005 §3); POS wired where possible |
| Encryption | WPA3, or WPA2 where a device requires it; **WPS off** |
| Guest network | Client isolation on; bandwidth limit; no route to internal segments |
| Admin | Unique admin password in the password manager; managed only from the management segment |
| Firmware | Current; monthly check |

## 7. Internet Router (RTR-01, provider-managed)
| Setting | Value |
|---|---|
| Admin password | Changed from the default if the provider allows customer access; stored in the password manager |
| Remote management | Off for the customer side; the provider's own management is recorded as a vendor dependency (V-008) |
| Wi-Fi on the router | Off, so all Wi-Fi comes from the shop's own access points |

## 8. Connected Devices
Covered by the [Connected Devices Procedure (PR-011)](PR-011-connected-devices.md) §3.

---

## 9. Checking Devices Against the Baseline
  - **New devices** are set to the baseline before they're used (PR-010 §3).
  - **Every quarter**, with the equipment register walk-through, the IT Technician checks each device and records the result in the [baseline check log](../07-evidence-pack/artifacts/assets/baseline-checks.csv) (evidence E-12). Anything that doesn't match is fixed or raised as an exception (PR-014).
  - **When Intune is licensed** (D-9), the laptop and tablet settings are enforced with compliance policies, and the check uses Intune's compliance report.

---

## 10. Current Status
The baselines are new. No device has been checked against them, and the firewall and access points still have settings nobody recorded (Vertex kept no configuration records). The first check is due in the IT Technician's first quarter (by 2027-02-15). Tracked under **POAM-009**.

---

## 11. Related Documents
  - [Microsoft 365 Tenant Security Baseline (PR-013)](PR-013-m365-tenant-baseline.md)
  - [Network Security Policy (P-005)](../04-policies/P-005-network-security.md)
  - [IT Operations Policy (P-006)](../04-policies/P-006-it-operations.md)
  - [Equipment Maintenance and Lifecycle Procedure (PR-010)](PR-010-equipment-lifecycle.md)

---

*This document is a simulation for educational and portfolio purposes only.*
