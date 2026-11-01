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
| SYS-002  | Google Workspace             | SaaS Platform   | Owner         | Cloud          | Confidential   | H-H-H      | Retired | Email and document management; retired 2026-11-15 (CR-001); data exported, deletion confirmation pending |
| SYS-003  | Google Admin Console         | Admin Interface | Owner         | Cloud          | Restricted     | H-H-H      | Retired | Administrative access to company systems; retired 2026-11-15 (CR-001) |
| SYS-004  | xtraCHEF                     | SaaS Platform   | Store Manager | Cloud          | Internal       | M-M-M      | Active | Inventory and invoices (part of Toast)   |
| SYS-005  | QuickBooks Online            | SaaS Platform   | Owner         | Cloud          | Confidential   | H-H-M      | Retired | Accounting; retired 2026-11-15 (CR-001); data exported to the bookkeeping workbook |
| SYS-006  | Northwind Payroll Services   | SaaS Platform   | Owner         | Cloud          | Restricted     | H-H-M      | Pending | Payroll and HR (V-002); onboarding pending until vendor conditions close                   |
| SYS-007  | Store Network                | Network         | Owner         | Store          | Confidential   | M-H-H      | Active | Groups NET-001 to NET-005                |
| SYS-010  | Microsoft Entra ID           | SaaS Platform   | Owner         | Cloud          | Restricted     | H-H-H      | Active | Identity, from CR-001                   |
| SYS-011  | Exchange Online              | SaaS Platform   | Owner         | Cloud          | Confidential   | H-H-M      | Active | Email, from CR-001                      |
| SYS-012  | SharePoint Online and Teams  | SaaS Platform   | Owner         | Cloud          | Confidential   | H-H-M      | Active | Files, intranet and chat, from CR-001   |
| SYS-013  | Microsoft Intune and Defender for Business | SaaS Platform | Owner | Cloud | Internal | M-H-M | Active | Device management and endpoint protection, from CR-001 (licence-dependent) |
| SYS-014  | Bookkeeping Workbook (Excel for the web) | SaaS Platform | Owner | Cloud | Confidential | H-H-M | Active | Replaces QuickBooks Online, from CR-001 |
| SYS-015  | Password Manager (Bitwarden organization) | SaaS Platform | Owner | Cloud | Restricted | H-H-M | Planned | Shared admin credentials only; two members (Owner, IT Technician); PR-009, CR-003 |
| SYS-016  | Camera System (cloud recording) | SaaS Platform | Owner | Cloud and store | Confidential | M-M-M | Active | Two cameras; footage kept 30 days (PR-011) |
| SYS-017  | Espresso Machine Service Portal | SaaS Platform | Store Manager | Cloud | Internal | L-M-M | Active | Vendor remote diagnostics (PR-011 §4) |
| SYS-018  | Temperature Monitoring Service | SaaS Platform | Store Manager | Cloud | Internal | L-H-M | Active | Food-safety temperature log |
| HW-001   | POS Terminals                | Hardware        | Store Manager | Store          | Restricted     | H-H-H      | Active | Used for customer transactions           |
| HW-002   | Company Tablets              | Hardware        | Store Manager | Store          | Internal       | M-M-M      | Active | Inventory and operational tasks          |
| HW-003   | Manager Laptop               | Hardware        | Store Manager | Store          | Confidential   | M-M-M      | Active | Business network; shares Wi-Fi with POS terminals (POAM-015) |
| HW-004   | Security Cameras             | Hardware        | Owner         | Store          | Confidential   | M-M-M      | Active | CAM-01, CAM-02 (equipment register) |
| HW-005   | Connected Espresso Machine   | Hardware        | Store Manager | Store          | Internal       | L-M-H      | Active | ESP-01; vendor remote access |
| HW-006   | Fridge Temperature Sensors   | Hardware        | Store Manager | Store          | Internal       | L-H-M      | Active | TMP-01, TMP-02 |
| HW-007   | Music Speaker                | Hardware        | Store Manager | Store          | Public         | L-L-L      | Active | SPK-01 |
| NET-001  | Store Router                 | Network Device  | Owner         | Store          | Confidential   | M-H-H      | Active | Network routing                          |
| NET-002  | Firewall / Gateway           | Network Device  | Owner         | Store          | Confidential   | H-H-H      | Active | Network security control                 |
| NET-003  | Wi-Fi Access Points          | Network Device  | Owner         | Store          | Internal       | L-M-H      | Active | Provides staff and guest connectivity    |
| NET-004  | Staff Wi-Fi Network          | Network         | Owner         | Store          | Internal       | L-M-M      | Active | Used by employees                        |
| NET-005  | Guest Wi-Fi Network          | Network         | Owner         | Store          | Public         | L-L-M      | Active | Isolated network for customers           |
| NET-006  | Devices Network Segment      | Network         | Owner         | Store          | Internal       | M-M-M      | Planned | Cameras, espresso machine, sensors, speaker (P-005 §3) |
| DATA-001 | Payment Transaction Data     | Data            | Owner         | Cloud          | Restricted     | H-H-H      | Active | Stored and processed by POS              |
| DATA-002 | Employee Payroll Data        | Data            | Owner         | Cloud          | Restricted     | H-H-M      | Active | Employee compensation records            |
| DATA-003 | Employee Contact Information | Data            | Owner         | Cloud          | Confidential   | M-M-M      | Active | HR information                           |
| DATA-004 | Business Financial Reports   | Data            | Owner         | Cloud          | Confidential   | M-H-M      | Active | Accounting and sales reports             |
| DATA-005 | Camera Footage               | Data            | Owner         | Cloud          | Confidential   | H-M-M      | Active | Customers and staff on video; kept 30 days; export only with Owner approval |



The canonical system list, with each system's vendor and evidence mode, is [systems.csv](../00-company-profile/org/systems.csv). Individual devices, with serial numbers, warranty and support dates, are in the [equipment register](equipment-register.csv), and their updates, repairs and technician visits in the [maintenance log](maintenance-log.csv) (PR-010).

---

## Revision History

| Date | Change | Reason |
|---|---|---|
| 2026-11-15 | SYS-002, SYS-003 and SYS-005 → Retired; SYS-010 to SYS-014 → Active | Microsoft 365 cutover (CR-001). Evidence modes (Live, Planned, Simulation) stay in systems.csv |
| 2026-10-30 | Added PER-004, PER-005, SYS-004 to SYS-007, planned SYS-010 to SYS-014 and HW-003; noted planned retirements; fixed a typo | Assets named in the access review, vendor inventory and network evidence were missing from the register (AL-06) |
| 2026-11-01 | Added SYS-016 to SYS-018, HW-004 to HW-007, NET-006 (planned) and DATA-005 | Connected devices were in the store but not in the register (PR-011) |
| 2026-10-30 | SYS-006 Active → Pending | Northwind's pre-go-live conditions are open; onboarding has not proceeded (AL-24) |
