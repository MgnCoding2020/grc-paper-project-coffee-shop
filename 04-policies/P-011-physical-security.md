# Physical Security Policy
Burn and Churn Coffee

## Document Control
**Policy Owner:** Business Owner | 
**Approved by:** Business Owner | 
**Effective Date:** 2026-11-02 | 
**Review Frequency:** Annual, and whenever a key is lost or the alarm changes | 
**Version:** 1.0

----------

## 1. Purpose
Protect the store, its equipment and its records from theft, tampering and unauthorized access, especially the payment terminal, the network cabinet, the back office and the safe. The customer area is public; everything behind the counter isn't.

It implements NIST SP 800-53 **PE-2 (Physical Access Authorizations)** and **PE-8 (Visitor Access Records)**, alongside the existing PE-3 (device protection, [PR-006](../05-procedures/PR-006-pos-device-inspection.md)) and PE-6 (cameras, [PR-011](../05-procedures/PR-011-connected-devices.md)). It supports PCI DSS Requirement 9.

-----------

## 2. Areas
| Area | Who may enter | What's there |
|---|---|---|
| Customer area | Anyone during opening hours | Seating, the customer side of the counter |
| Behind the counter | Staff on shift; visitors only when escorted | POS terminal, espresso machine, tablets |
| Back office | Owner, Store Manager, Shift Leaders, IT Technician; others escorted | Manager laptop, **network cabinet** (router, firewall), safe, records |
| Stock room | Staff; delivery drivers escorted | Stock, back door, temperature sensors |

-----------

## 3. Keys and Alarm Codes (PE-2)
  1. **Every key and alarm code is personal and recorded** in the [key register](../07-evidence-pack/artifacts/physical/key-register.csv): who holds it, when issued, when returned.
  2. **Store keys:** Owner, Store Manager and Shift Leaders (who open and close). The **back office and network cabinet keys**: Owner, Store Manager and IT Technician only. **Safe:** Owner and Store Manager only.
  3. **Each key holder has their own alarm code**, so the alarm log shows who opened and closed. Codes are never shared or written down.
  4. Keys are returned, and alarm codes deleted, on the last day ([P-009](P-009-personnel-security.md) §7).
  5. **A lost key** is reported the same day; the Owner decides whether to re-key, recorded in the register.
  6. The key register is checked against the keys actually held **every quarter**, at the same time as the access review.

-----------

## 4. Opening and Closing
  - Two people open and close where staffing allows. Whoever opens disarms the alarm with their own code and does the POS opening check ([PR-006](../05-procedures/PR-006-pos-device-inspection.md)).
  - At close: cash in the safe; back office, stock room and back door locked; tablets and laptop locked away or in the back office; alarm set with the closer's own code.

-----------

## 5. Visitors (PE-8)
  - Anyone going behind the counter, into the back office or the stock room who isn't on staff (technicians, inspectors, delivery drivers going past the stock room door, contractors) is **escorted** and **recorded** in the [visitor log](../07-evidence-pack/artifacts/physical/visitor-log.csv): date, name, company, purpose, escorted by, time in and out.
  - Technicians are confirmed with their company **before** they're let in ([PR-010](../05-procedures/PR-010-equipment-lifecycle.md) §4).
  - Nobody touches the POS terminal, network cabinet or laptop without the IT Technician or the Owner present.

-----------

## 6. Equipment
  - The network cabinet stays locked. The POS terminal stays where the counter camera can see the terminal but **not the keypad** (PR-011 §5).
  - Equipment leaving the store for repair or disposal follows [PR-010](../05-procedures/PR-010-equipment-lifecycle.md) and [P-010](P-010-records-retention-disposal.md).
  - Printed records with personal data are kept in the back office and shredded when no longer needed (P-010).

-----------

## 7. Current Status
Keys have never been inventoried, and the alarm uses **one code shared by every key holder**, so the alarm log can't show who opened or closed. There is no visitor log, and nobody knows who holds the back-office key. Tracked under **POAM-035**.

-----------

## 8. Related Documents
  - [POS Device Inspection Procedure (PR-006)](../05-procedures/PR-006-pos-device-inspection.md)
  - [Connected Devices Procedure (PR-011)](../05-procedures/PR-011-connected-devices.md) (cameras)
  - [Equipment Maintenance and Lifecycle Procedure (PR-010)](../05-procedures/PR-010-equipment-lifecycle.md)
  - [Personnel Security Policy (P-009)](P-009-personnel-security.md)

-----------

*This document is a simulation for educational and portfolio purposes only.*
