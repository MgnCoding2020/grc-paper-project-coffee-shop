# Asset Inventory Register
Burn and Churn Coffee

----
## Purpose
This document maintains an inventory of technology, personnel, and data assets used by Burn and Churn Coffee.

Maintaining an asset inventory supports:
  - Rick management
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
| SYS-001  | Toast POS System             | SaaS Platform   | Owner         | Cloud          | Restricted     | H-H-H      | Active | Processes payment transactions           |
| SYS-002  | Google Workspace             | SaaS Platform   | Owner         | Cloud          | Confidential   | H-H-H      | Active | Email and document management            |
| SYS-003  | Google Admin Console         | Admin Interface | Owner         | Cloud          | Restricted     | H-H-H      | Active | Administrative access to company systems |
| HW-001   | POS Terminals                | Hardware        | Store Manager | Store          | Restricted     | H-H-H      | Active | Used for customer transactions           |
| HW-002   | Company Tablets              | Hardware        | Store Manager | Store          | Internal       | M-M-M      | Active | Inventory and operational tasks          |
| NET-001  | Store Router                 | Network Device  | Owner         | Store          | Confidential   | M-H-H      | Active | Network routing                          |
| NET-002  | Firewall / Gateway           | Network Device  | Owner         | Store          | Confidential   | H-H-H      | Active | Network security control                 |
| NET-003  | Wi-Fi Access Points          | Network Device  | Owner         | Store          | Internal       | L-M-H      | Active | Provides staff and guest connectivity    |
| NET-004  | Staff Wi-Fi Network          | Network         | Owner         | Store          | Internal       | L-M-M      | Active | Used by employees                        |
| NET-005  | Guest Wi-Fi Network          | Network         | Owner         | Store          | Public         | L-L-M      | Active | Isolated network for customers           |
| DATA-001 | Payment Transaction Data     | Data            | Owner         | Cloud          | Restricted     | H-H-H      | Active | Stored and processed by POS              |
| DATA-002 | Employee Payroll Data        | Data            | Owner         | Cloud          | Restricted     | H-H-M      | Active | Employee compensation records            |
| DATA-003 | Employee Contact Information | Data            | Owner         | Cloud          | Confidential   | M-M-M      | Active | HR information                           |
| DATA-004 | Business Financial Reports   | Data            | Owner         | Cloud          | Confidential   | M-H-M      | Active | Accounting and sales reports             |


