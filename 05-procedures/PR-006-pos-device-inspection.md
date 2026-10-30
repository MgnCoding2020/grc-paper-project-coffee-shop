# POS Device Inspection Procedure
Burn and Churn Coffee

---

## Document Control
**Owner:** Store Manager | **Approved by:** Business Owner | **Effective:** 2026-10-30 | **Review:** Annually, or when devices change | **Version:** 1.0

---

## 1. Purpose
Card skimmers and swapped terminals are a real risk at a busy counter. This procedure makes sure the store knows exactly which payment devices it has, checks them for tampering on a set schedule, and reacts correctly if something looks wrong. It implements NIST SP 800-53 **PE-3** for payment devices and PCI DSS Requirement **9.5.1**.

---

## 2. Device List (PCI DSS 9.5.1.1)
Every payment and business device is listed in the [POS device list](../07-evidence-pack/artifacts/physical/pos-device-list.csv) with its make, model, serial number and location. The Store Manager updates the list whenever a device is added, replaced or removed, and a device not on the list is never used.

---

## 3. Inspection Frequency: Targeted Risk Analysis (PCI DSS 9.5.1.2.1)
PCI DSS leaves the frequency to the merchant's own risk analysis:

| Factor | Assessment |
|---|---|
| Location | Countertop terminal at the staffed counter; tablets behind the counter |
| Supervision | Staff present whenever the store is open; devices are not left unattended in public areas |
| Exposure | High foot traffic during opening hours; customers handle the card reader |
| Past issues | One issue found (loose casing on Tablet 2, 2026-02-01) with no follow-up recorded |

**Result:**
  - **Daily opening check** (about one minute) of the card reader by the opening Shift Leader: nothing attached, no overlay, no damage. Not logged unless something is wrong.
  - **Monthly recorded inspection** of every device on the list by a Shift Leader, reviewed by the Store Manager.
  - **Extra inspection** after any repair, replacement, suspicious visit or outage.

---

## 4. Monthly Inspection Steps (PCI DSS 9.5.1.2)
For each device on the list:
  1. **Identity:** the serial number matches the device list (detects a swapped device).
  2. **Surfaces:** no overlays, extra parts or unusual adhesive on the card slot, PIN pad or contactless area.
  3. **Seals and casing:** seals intact; casing closed; no loose parts, scratches or pry marks around seams.
  4. **Cables and connections:** only expected cables; nothing added between the terminal and its connections.
  5. **Behaviour:** no unexpected prompts or screens.

Record each device's result in the [inspection log](../07-evidence-pack/artifacts/physical/physical-inspection-checklist.csv): date, device, inspector, OK or Issue, notes.

---

## 5. If Something Is Wrong
  1. **Stop using the device.** Don't unplug it, open it or try to fix it.
  2. Tell the Store Manager immediately; follow the **POS suspicious activity playbook (IRP-003)**, which treats suspected tampering as a security incident.
  3. Contact Toast support before the device returns to service.
  4. An Issue in the log is **not closed** until the follow-up is recorded (fixed, replaced or confirmed harmless) with a date and name.

---

## 6. Training (PCI DSS 9.5.1.3)
Everyone who uses the register is trained to recognise tampering and swapped devices, to check the identity of anyone claiming to service a terminal, and to report concerns. This is part of the security awareness program (PR-007).

---

## 7. Current Status
  - Only **one inspection** is recorded (2026-02-01).
  - Its Issue (Tablet 2, loose casing) has **no recorded follow-up**.
  - No inspections are recorded since.

The first monthly inspection under this procedure is due in **November 2026**, starting with Tablet 2. Tracked under **POAM-004**.

---

## 8. Related Documents
  - [Payment Card Data Protection Policy (P-004)](../04-policies/P-004-payment-card-data-protection.md)
  - [IRP-003 POS Suspicious Activity](../06-incident-playbooks/IRP-003-pos-suspicious-activity.md)
  - [Asset Inventory](../01-asset-inventory/assets.md)

PCI DSS v4.0.1 9.5.1 sub-requirement numbers checked against secondary sources on 2026-10-30; confirm against the PCI SSC standard text.

---

*This document is a simulation for educational and portfolio purposes only.*
