# IT Operations Policy
Burn and Churn Coffee

## Document Control
**Policy Owner:** Business Owner | 
**Approved by:** Business Owner | 
**Effective Date:** 2026-11-01 | 
**Review Frequency:** Annual, or when systems or the IT role change | 
**Version:** 1.0

----------

## 1. Purpose
This policy sets the rules for looking after Burn and Churn Coffee's technology once it's in place: knowing what equipment the business has, keeping it updated, maintaining and repairing it safely, and replacing it before its maker stops supporting it.

It implements NIST SP 800-53 **CM-8 (System Component Inventory)**, **SI-2 (Flaw Remediation)**, **MA-2 (Controlled Maintenance)**, **MA-5 (Maintenance Personnel)** and **SA-22 (Unsupported System Components)**, and supports PCI DSS Requirements 6.3.3, 9.5.1, 12.3.4 and 12.5.1.

-----------

## 2. Scope
  - Every system in [systems.csv](../00-company-profile/org/systems.csv) and every device in the [equipment register](../01-asset-inventory/equipment-register.csv): the POS terminal, tablets, the manager laptop, network equipment and connected devices
  - Everyone who updates, maintains or repairs them: the IT Technician, staff, and vendors' technicians

-----------

## 3. Equipment Register (CM-8)
  1. Every device that connects to a company network, or handles company or card data, is listed in the equipment register **before** it goes into use, with its serial number, location, warranty end, the date its maker stops supporting it, and who maintains it.
  2. The IT Technician updates the register whenever a device is added, moved, repaired, replaced or retired. Retired devices stay in the register, marked retired, never deleted.
  3. The register is checked against what's actually in the store every quarter, at the same time as the access review.

-----------

## 4. Updates and Patching (SI-2)
  1. Automatic updates stay on wherever a device or service supports them.
  2. **Critical and high-severity security updates** are installed within **one month** of release (PCI DSS 6.3.3). An update for a weakness that is **actively being exploited** is installed as soon as possible, as an emergency change.
  3. Other updates are installed in the **monthly update window**, after close, so trading is never interrupted.
  4. Every update to network equipment, the POS terminal or a connected device is recorded in the maintenance log.
  5. If an update can't be installed on time, the reason, the temporary protection and the new date are recorded and approved by the Owner.

The [Patch and Vulnerability Management Procedure (PR-002)](../05-procedures/PR-002-patch-vuln-management.md) describes how.

-----------

## 5. Maintenance and Repairs (MA-2, MA-5)
  1. Maintenance on company equipment is planned, recorded in the maintenance log, and checked afterwards.
  2. **Anyone who comes to service equipment** (POS, network, espresso machine or other connected devices) has their identity and visit confirmed with the vendor **before** they touch anything, is supervised by the Store Manager or a Shift Leader, and is recorded in the maintenance log (PCI DSS 9.5.1.3).
  3. **Remote maintenance** by a vendor is allowed only through the vendor's own named accounts, only when needed, and is recorded.
  4. A device that leaves the store for repair has company data removed first, where possible, and is inspected when it comes back.

The [Equipment Maintenance and Lifecycle Procedure (PR-010)](../05-procedures/PR-010-equipment-lifecycle.md) describes how.

-----------

## 6. Supported Equipment Only (SA-22)
  1. Every device and system must be supported by its maker, meaning it still receives security updates.
  2. Once a year, the IT Technician reviews the register for equipment reaching its end-of-support date in the next 12 months (PCI DSS 12.3.4) and proposes a replacement plan to the Owner.
  3. Equipment past its end of support is replaced. Until then it's an exception, approved by the Owner and tracked in the POA&M, with extra protection (for example, isolated on its own network segment).

-----------

## 7. Disposal
Before a device is sold, recycled or returned to a vendor, company data is erased (or the storage is destroyed), its accounts and credentials are removed, and the register is updated with the date and method.

-----------

## 8. Current Exceptions
  - **Equipment records are incomplete.** Before 2026-11-15, Vertex IT Support kept no maintenance records, and the support end dates for the firewall, access points and tablets are not on file. The register marks them *Unknown*. Tracked under POAM-023 and POAM-025.

-----------

## 9. Enforcement
Equipment that isn't in the register, isn't updated on time, or is past its end of support without an approved exception is a finding in the next review. Unrecorded maintenance by a visitor is treated as a security incident under the [Incident Response Policy (P-003)](P-003-incident-response.md).

-----------

## 10. Related Documents
  - [Patch and Vulnerability Management Procedure (PR-002)](../05-procedures/PR-002-patch-vuln-management.md)
  - [Equipment Maintenance and Lifecycle Procedure (PR-010)](../05-procedures/PR-010-equipment-lifecycle.md)
  - [POS Device Inspection Procedure (PR-006)](../05-procedures/PR-006-pos-device-inspection.md)
  - [IT Administration and Coverage Procedure (PR-008)](../05-procedures/PR-008-it-administration.md)
  - [Network Security Policy (P-005)](P-005-network-security.md)
  - [Asset Inventory](../01-asset-inventory/assets.md)

-----------

*This document is a simulation for educational and portfolio purposes only.*
