# Equipment Maintenance and Lifecycle Procedure
Burn and Churn Coffee

---

## Document Control
**Owner:** Business Owner | **Performed by:** IT Technician | **Approved by:** Business Owner | **Effective:** 2026-11-01 | **Review:** Annually | **Version:** 1.0

---

## 1. Purpose
Track every piece of equipment from purchase to disposal: what it is, where it is, who looks after it, when it was last serviced, and when its maker stops supporting it. This procedure carries out §3, §5, §6 and §7 of the [IT Operations Policy (P-006)](../04-policies/P-006-it-operations.md). It implements NIST SP 800-53 **CM-8**, **MA-2**, **MA-5** and **SA-22**.

---

## 2. The Two Records

| Record | What it holds | Updated |
|---|---|---|
| [Equipment register](../01-asset-inventory/equipment-register.csv) | One row per device: tag, asset ID, make and model, serial number, location, purchase date, warranty end, support end, current version, who maintains it, status | When a device is added, moved, repaired, replaced or retired |
| [Maintenance log](../01-asset-inventory/maintenance-log.csv) | One row per event: date, device, activity (update, repair, part replaced, technician visit, configuration backup, inspection), who did it, who supervised, change record, result | Every time something is done to a device |

Device tags are listed in the [identifier registry](../00-company-profile/org/identifiers.md). The register covers more than the [POS device list](../07-evidence-pack/artifacts/physical/pos-device-list.csv), which stays as the PCI DSS 9.5.1.1 list for card-reading devices.

---

## 3. New Equipment
  1. The Owner approves the purchase. If the device connects to a company network, the IT Technician confirms which network segment it goes on ([P-005](../04-policies/P-005-network-security.md)).
  2. Before it goes into use, the IT Technician adds it to the register, changes any default password (stored in the password manager, [PR-009](PR-009-credential-vault.md)), turns on automatic updates where offered, and checks the maker's support end date.
  3. Card-reading devices are also added to the POS device list and inspected under [PR-006](PR-006-pos-device-inspection.md).

---

## 4. Technician Visits (MA-5)
When someone arrives to service equipment, including the POS terminal, network gear, the espresso machine and other connected devices:
  1. **Confirm before access.** Call the vendor on the number in the password manager or contract, not a number the visitor gives, and confirm the visit and the technician's name. No confirmation, no access (PCI DSS 9.5.1.3).
  2. **Supervise.** The Store Manager or a Shift Leader stays with the technician.
  3. **Record.** Add a maintenance log row: date, device, company, technician name, supervisor, what was done.
  4. **Check afterwards.** For a card-reading device, inspect it under PR-006 before it's used again.

Remote work by a vendor follows the same idea: named vendor accounts only, only when needed, recorded in the log.

---

## 5. Repairs and Parts
  - Repairs and replaced parts are logged against the device's tag.
  - **Spares** (for example a spare access point or network cable) are listed in the register with status *Spare*, so they're counted and ready.
  - A device sent away for repair has company data removed first where possible, and is inspected when it returns.

---

## 6. End of Support (SA-22)
  - **Every November**, the IT Technician lists every device whose support ends in the next 12 months, or whose support end is *Unknown*, and proposes replacements and costs to the Owner (PCI DSS 12.3.4).
  - Unknown support dates are looked up on the maker's website and recorded.
  - Equipment past its support end is replaced. Until then it's an exception approved by the Owner, kept on an isolated network segment, and tracked in the POA&M.

---

## 7. Disposal
  1. Erase company data (factory reset with storage encryption on, or destroy the storage).
  2. Remove the device from accounts, management tools and Wi-Fi; rotate any credential stored on it.
  3. Card-reading devices go back to the vendor as they direct, with written confirmation.
  4. Mark the device *Retired* in the register with the date and method. Never delete the row.

---

## 8. Quarterly Check
At the quarterly access review, the IT Technician walks the store with the register: every device found is listed, every listed device is found. Differences are recorded and fixed.

---

## 9. Current Status
  - **Register created 2026-11-01** from the asset inventory and the POS device list. Serial numbers are simulated. Warranty and support dates are missing for most devices because Vertex IT Support kept no equipment records. The warranty on the firewall and the manager laptop has already ended.
  - **Maintenance log** starts with the only recorded event (the 2026-02-01 inspection). The handover from Vertex (PR-008 §7) should supply any history Vertex has.
  - Tracked under **POAM-023** (register and update records), **POAM-024** (maintenance and visit records) and **POAM-025** (support end dates).

---

## 10. Related Documents
  - [IT Operations Policy (P-006)](../04-policies/P-006-it-operations.md)
  - [Patch and Vulnerability Management Procedure (PR-002)](PR-002-patch-vuln-management.md)
  - [POS Device Inspection Procedure (PR-006)](PR-006-pos-device-inspection.md)
  - [Asset Inventory](../01-asset-inventory/assets.md) and [Asset Lifecycle](../01-asset-inventory/asset-management/asset-lifecycle.md)

---

*This document is a simulation for educational and portfolio purposes only.*
