# Asset Inventory Register
Burn and Churn Coffee

----
## Purpose
This document maintains an inventory of technology, personnel, and data assets used by Burn and Churn Coffee.

Maintaining an asset inventory supports:
  - Risk management
  - Security control implementation
  - Incident response
  - Business continuity planning

Each asset is categorized and assigned a sensitivity rating based on the **Confidentiality, Integrity, and Availability (CIA) model**.

------

## Asset Register

| Asset ID | Asset Name                   | Asset Type      | Owner         | Location       | Classification | CIA Rating | Status | Notes                                    |
| -------- | ---------------------------- | --------------- | ------------- | -------------- | -------------- | ---------- | ------ | ---------------------------------------- |
| PER-001  | Business Owner               | Personnel       | Owner         | Store / Remote | Confidential   | M-M-H      | Active | Administrative system access             |
| PER-002  | Store Manager                | Personnel       | Owner         | Store          | Confidential   | M-M-H      | Active | Operational management                   |
| PER-003  | Employees (Baristas)         | Personnel       | Owner         | Store          | Internal       | L-M-M      | Active | POS users                                |
| PER-004  | Shift Leaders                | Personnel       | Store Manager | Store          | Internal       | L-M-M      | Active | Shift supervision; POS shift-lead role   |
| PER-005  | IT Vendor Administrators (Vertex IT Support) | Personnel | Owner | Remote | Restricted | H-H-M | Active | Privileged admin access to Google Workspace and network equipment; offboarding planned (CR-003) |
| SYS-001  | Toast POS System             | SaaS Platform   | Owner         | Cloud          | Restricted     | H-H-H      | Active | Processes payment transactions           |
| SYS-002  | Google Workspace             | SaaS Platform   | Owner         | Cloud          | Confidential   | H-H-H      | Active | Email and document management; retirement planned (CR-001) |
| SYS-003  | Google Admin Console         | Admin Interface | Owner         | Cloud          | Restricted     | H-H-H      | Active | Administrative access to company systems; retirement planned (CR-001) |
| SYS-004  | xtraCHEF                     | SaaS Platform   | Store Manager | Cloud          | Internal       | M-M-M      | Active | Inventory and invoices (part of Toast)   |
| SYS-005  | QuickBooks Online            | SaaS Platform   | Owner         | Cloud          | Confidential   | H-H-M      | Active | Accounting; retirement planned (CR-001)  |
| SYS-006  | Northwind Payroll Services   | SaaS Platform   | Owner         | Cloud          | Restricted     | H-H-M      | Active | Payroll and HR (V-002)                   |
| SYS-007  | Store Network                | Network         | Owner         | Store          | Confidential   | M-H-H      | Active | Groups NET-001 to NET-005                |
| SYS-010  | Microsoft Entra ID           | SaaS Platform   | Owner         | Cloud          | Restricted     | H-H-H      | Planned | Identity, from CR-001                   |
| SYS-011  | Exchange Online              | SaaS Platform   | Owner         | Cloud          | Confidential   | H-H-M      | Planned | Email, from CR-001                      |
| SYS-012  | SharePoint Online and Teams  | SaaS Platform   | Owner         | Cloud          | Confidential   | H-H-M      | Planned | Files, intranet and chat, from CR-001   |
| SYS-013  | Microsoft Intune and Defender for Business | SaaS Platform | Owner | Cloud | Internal | M-H-M | Planned | Device management and endpoint protection, from CR-001 (licence-dependent) |
| SYS-014  | Bookkeeping Workbook (Excel for the web) | SaaS Platform | Owner | Cloud | Confidential | H-H-M | Planned | Replaces QuickBooks Online, from CR-001 |
| HW-001   | POS Terminals                | Hardware        | Store Manager | Store          | Restricted     | H-H-H      | Active | Used for customer transactions           |
| HW-002   | Company Tablets              | Hardware        | Store Manager | Store          | Internal       | M-M-M      | Active | Inventory and operational tasks          |
| HW-003   | Manager Laptop               | Hardware        | Store Manager | Store          | Confidential   | M-M-M      | Active | Business network; shares Wi-Fi with POS terminals (POAM-015) |
| NET-001  | Store Router                 | Network Device  | Owner         | Store          | Confidential   | M-H-H      | Active | Network routing                          |
| NET-002  | Firewall / Gateway           | Network Device  | Owner         | Store          | Confidential   | H-H-H      | Active | Network security control                 |
| NET-003  | Wi-Fi Access Points          | Network Device  | Owner         | Store          | Internal       | L-M-H      | Active | Provides staff and guest connectivity    |
| NET-004  | Staff Wi-Fi Network          | Network         | Owner         | Store          | Internal       | L-M-M      | Active | Used by employees                        |
| NET-005  | Guest Wi-Fi Network          | Network         | Owner         | Store          | Public         | L-L-M      | Active | Isolated network for customers           |
| DATA-001 | Payment Transaction Data     | Data            | Owner         | Cloud          | Restricted     | H-H-H      | Active | Stored and processed by POS              |
| DATA-002 | Employee Payroll Data        | Data            | Owner         | Cloud          | Restricted     | H-H-M      | Active | Employee compensation records            |
| DATA-003 | Employee Contact Information | Data            | Owner         | Cloud          | Confidential   | M-M-M      | Active | HR information                           |
| DATA-004 | Business Financial Reports   | Data            | Owner         | Cloud          | Confidential   | M-H-M      | Active | Accounting and sales reports             |



The canonical system list, with each system's vendor and evidence mode, is [systems.csv](../00-company-profile/org/systems.csv).

---

## Revision History

| Date | Change | Reason |
|---|---|---|
| 2026-10-30 | Added PER-004, PER-005, SYS-004 to SYS-007, planned SYS-010 to SYS-014 and HW-003; noted planned retirements; fixed a typo | Assets named in the access review, vendor inventory and network evidence were missing from the register (AL-06) |
