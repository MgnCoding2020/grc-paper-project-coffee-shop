# Company Profile
Burn and Churn Coffee

---

## Business Overview

Burn and Churn Coffee is a small retail coffee shop that provides in-store beverage and food service to local customers.

The business accepts both cash and card payments; most sales are card payments, processed in store through Toast. It relies on cloud-based business services to support daily operations.

Because the business processes payment card transactions and stores limited operational data, cybersecurity risks primarily involve:

- Payment card fraud
- Account compromise
- Disruption of store operations
- Unauthorized access to business systems

---

## Business Size

Burn and Churn Coffee operates a single retail location with 20 active store staff.

Organizational roles include:

- 1 Business Owner
- 1 Store Manager
- 3 Shift Leaders
- 15 Baristas

Named staff, roles and responsibilities are maintained in the [org directory](org/): [people.csv](org/people.csv) and [roles.md](org/roles.md).

IT administration is currently performed by an external managed service provider, **Vertex IT Support**. A previous IT vendor, **NorthPeak Systems**, no longer has an active engagement. A part-time in-house IT Technician is planned to replace Vertex from 2026-11-15 (CR-003).

---

## Technology Environment

The organization relies on several technology systems to operate daily business functions.

Key systems include:

- **Toast POS System**  
  Used for payment processing and order management.

- **Microsoft 365**  
  Staff accounts and sign-in (Microsoft Entra ID), email (Exchange Online), files, the intranet and chat (SharePoint and Teams). Replaced Google Workspace on 2026-11-15 (CR-001).

- **xtraCHEF**  
  Inventory and invoice management (part of Toast).

- **Bookkeeping workbook**  
  Excel for the web in a restricted SharePoint Finance library (Owner and Store Manager only). Replaced QuickBooks Online on 2026-11-15 (CR-001).

- **Northwind Payroll Services**  
  Payroll and HR (approved with conditions after a vendor risk assessment on 2026-06-23; onboarding pending until the vendor meets its pre-go-live conditions).

- **Store Network Infrastructure**  
  Router, firewall, and Wi-Fi network supporting POS devices and employee systems.

- **Company Tablets**  
  Used by store managers and employees for operational tasks.

- **Connected Devices**  
  Two security cameras with cloud recording, a connected espresso machine that its service company monitors remotely, fridge temperature sensors that keep the food-safety log, and a music speaker ([PR-011](../05-procedures/PR-011-connected-devices.md)).

---

## External Service Providers

Burn and Churn Coffee relies on several third-party vendors, each with a stable ID in the [vendor inventory](../02-risk-management/vendor-risk-management/vendor-inventory.md):

- Toast, Inc. (point of sale, payment processing and xtraCHEF), V-001
- Northwind Payroll Services (payroll and HR), V-002
- Vertex IT Support (IT managed services), V-004
- Microsoft (Microsoft 365), V-003
- Intuit (QuickBooks Online), V-006: being offboarded under CR-001 (data exported; subscription cancelled)
- Google (Workspace email and collaboration), V-007: being offboarded under CR-001 (data exported; deletion confirmation pending)
- Internet service provider, V-008
- Cloud camera service, V-010
- Espresso machine service company (including remote diagnostics), V-011
- Temperature monitoring service, V-012

Planned: Bitwarden (password manager), V-009, with CR-003.

Card payments are processed through Toast, which connects to the card networks. These vendors introduce **third-party risk considerations** that must be evaluated as part of the security program.

---

## Security Risk Considerations

Due to the nature of the business, key cybersecurity risks include:

- Payment card data exposure
- Compromise of employee credentials
- Malware affecting POS systems
- Unauthorized access to cloud services
- Network misuse through guest Wi-Fi

These risks are addressed through the organization's security governance program.

---

## Revision History

| Date | Change | Reason |
|---|---|---|
| 2026-11-15 | Google Workspace replaced by Microsoft 365 and QuickBooks Online by the bookkeeping workbook; V-003 active; V-006 and V-007 being offboarded | Microsoft 365 cutover (CR-001) |
| 2026-11-01 | Connected devices and their vendors (V-010 to V-012) added; planned vendors V-003 and V-009 noted | The devices were registered in the asset and vendor inventories (PR-011) but missing here |
| 2026-10-30 | Headcount corrected from about 19 to 20 active store staff (15 Baristas); IT vendors named; xtraCHEF, QuickBooks Online and Northwind Payroll added; vendors listed with their inventory IDs | Aligned with the canonical org data and the Q1 2026 access review (AL-03, AL-05) |
| 2026-10-30 | Stated that cash and card payments are both accepted | Clarification; the contingency plan (PR-005) relies on cash as a fallback |
