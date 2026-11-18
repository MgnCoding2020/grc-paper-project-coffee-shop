# ☕ GRC Security Program Simulation – Burn and Churn Coffee

## 📌 Overview

This project simulates the design and implementation of a **Governance, Risk, and Compliance (GRC) security program** for **Burn and Churn Coffee**, a small coffee shop handling **payment card data** and basic IT operations.

The goal of this project is to demonstrate how a real-world organization can:

* Identify and manage cybersecurity risks
* Implement security controls aligned to **NIST SP 800-53**
* Incorporate **PCI DSS concepts** for cardholder data protection
* Establish policies, procedures, and incident response capabilities
* Prepare for audit readiness through documentation and evidence collection

This repository reflects a **full security lifecycle** — connecting risk identification, control implementation, evidence validation, and remediation tracking within a cohesive GRC program, from asset identification through continuous monitoring.

---

## 🔗 Program Repositories

This repository is the **program hub and system of record**: the company, its people, systems and vendors are defined here, and findings from the companion labs roll up into this repository's POA&M.

| Repository | Role in the program | Rolls up to |
|---|---|---|
| **grc-paper-project-coffee-shop** (this repo) | Program hub: policies, procedures, risk register, control matrix, crosswalk, POA&M, evidence | — |
| [IAM Access Review Lab](https://github.com/MgnCoding2020/IAM-Access-Review-Lab) | Quarterly access reviews (AC-2, AC-6): the Q1 2026 review (Google Workspace era), and the Q4 2026 review planned as the first in Microsoft Entra ID | POAM-014 (AC-2, AC-6) |
| [Vendor Risk Assessment Lab](https://github.com/MgnCoding2020/Vendor-Risk-Assessment-Lab) | Third-party risk (SA-9): eight vendor assessments (Toast, Northwind, Microsoft, the internet provider, Bitwarden, and the camera, espresso and temperature services) and the Vertex IT Support offboarding record | POAM-006, -013, -018, -020, -021, -026, -027 |
| Microsoft 365 tenant (not a repository) | **Live evidence source** from the CR-001 build: real Entra ID accounts, groups, MFA and logs, committed here as redacted `Lab-verified` evidence | [Evidence index](07-evidence-pack/evidence-index.md) |
| Online ordering website (planned repository) | Change CR-002: where staff identity, payments in test mode and the new counter register connect | Planned |

Findings from the labs are referenced here by repository-prefixed IDs (for example `IAM:F-001`, `VRA-V002:F-01`) so the two labs' local finding numbers never collide. See [identifiers](00-company-profile/org/identifiers.md) for every ID format used across the program.

---

## 🏢 Business Scenario

**Burn and Churn Coffee** is a small coffee shop with:

* **20 store staff** (Owner, Store Manager, 3 Shift Leaders, 15 Baristas) and a part-time in-house **IT Technician**, hired under change CR-003 to replace an outsourced IT provider
* A **Toast POS** register taking cash and card payments, to be replaced by an integrated register under change CR-005
* **Microsoft 365** for identity, email and files, replacing Google Workspace on 2026-11-15 (change CR-001)
* A small store network, a manager laptop, tablets and **connected devices** (cameras, a remotely serviced espresso machine, fridge sensors)
* Twelve third-party vendors, each with an ID, a risk tier and an assessment or exit record

### Key Risks:

* Unauthorized access to POS systems
* Exposure of cardholder data
* Lack of centralized monitoring and logging
* Weak vendor security oversight
* Gaps inherited from an outsourced IT provider: shared accounts, no records, no backups

---

## 🎯 Objectives

This project was designed to:

* Simulate a **risk-based security program**
* Apply structured controls from **NIST SP 800-53**
* Introduce **PCI DSS-aligned safeguards** for payment environments
* Demonstrate **audit-ready documentation practices**
* Showcase both **technical and governance capabilities**

---

## 🧱 Security Framework Alignment

This project aligns with:

* **NIST SP 800-53** — control families covered by the [control matrix](03-controls/control-matrix.md):

  * Access Control (AC)
  * Awareness & Training (AT)
  * Assessment, Authorization & Monitoring (CA)
  * Audit & Accountability (AU)
  * Configuration Management (CM)
  * Contingency Planning (CP)
  * Identification & Authentication (IA)
  * Incident Response (IR)
  * Maintenance (MA)
  * Media Protection (MP)
  * Personnel Security (PS)
  * Physical & Environmental Protection (PE)
  * Risk Assessment (RA)
  * System & Services Acquisition (SA)
  * System & Communications Protection (SC)
  * System & Information Integrity (SI)

* **PCI DSS** (Conceptual Alignment)

  * Cardholder data protection
  * Network segmentation concepts
  * Access control enforcement
  * Logging and monitoring

A detailed [NIST 800-53 ↔ PCI DSS crosswalk](03-controls/nist-pci-crosswalk.md) maps each implemented control to its PCI DSS v4.0.1 requirement and identifies coverage gaps that feed the POA&M.

---

## 🗂️ Project Structure

```
.
├── 00-company-profile/      # Business profile, assessment scope, glossary, program overview
├── 01-asset-inventory/      # Asset register, equipment register, maintenance log, data classification, lifecycle
├── 02-risk-management/      # Risk register, exception register, continuous monitoring, vendor risk management
├── 03-controls/             # Control matrix (NIST 800-53 ↔ PCI DSS) and evidence plan
├── 04-policies/             # P-001–P-011 governance policies
├── 05-procedures/           # PR-001–PR-015 operational procedures
├── 06-incident-playbooks/   # IRP-001–IRP-007 incident response playbooks
├── 07-evidence-pack/        # Evidence matrix, POA&M, artifacts, and validation scripts
├── 08-architecture/         # System architecture and data-flow diagrams
├── 09-change-management/    # Change process and change records (CR-001, CR-003, CR-004, CR-005)
└── tools/                   # Consistency checker, due-date monitor, tenant scripts
```

---

## 🔍 System Boundary & Architecture

The environment includes:

* POS system connected to payment processor
* Internal business network
* Employee endpoints
* External vendor integrations

### Security Boundary Includes:

* Systems storing or transmitting cardholder data
* Authentication systems controlling access
* Logging and monitoring mechanisms

> 📌 *Detailed diagrams and data flows are included in the [architecture section](08-architecture/).*

---

## ⚠️ Risk Management Approach

A structured risk management process was implemented:

1. Asset Identification
2. Threat & Vulnerability Mapping
3. Risk Scoring (Likelihood × Impact)
4. Control Implementation
5. Residual Risk Evaluation

### Sample Risks (from the [risk register](02-risk-management/risk-register.md)):

* **R-01** – Phishing leading to account compromise
* **R-02** – Unauthorized POS transactions or misuse
* **R-04** – Network-based attack due to poor segmentation
* **R-07** – Vendor compromise, disruption or a poorly managed exit

---

## 🛡️ Control Implementation

Controls were designed and mapped to **NIST SP 800-53 families** and, where relevant, **PCI DSS requirements**. A representative sample:

* **IA-2** – Multi-Factor Authentication (PCI Req. 8)
* **AC-2** – Account Management (PCI Req. 7)
* **AC-6** – Least Privilege (PCI Req. 7)
* **AU-6** – Log Review (PCI Req. 10)
* **SC-7** – Network Segmentation (PCI Req. 1)

The full set of **41 controls across 16 families** — 0 Implemented, 22 Partially Implemented, 19 Not Implemented, with every open gap tracked to a POA&M item — is maintained in the [control matrix](03-controls/control-matrix.md).

Each control includes:

* Control description
* Implementation details
* Associated risks
* Evidence requirements

---

## Control Traceability

This project demonstrates end-to-end traceability across the GRC lifecycle:

Risk → Control → Evidence → Validation → Remediation

- Risks are defined in the Risk Register
- Controls are mapped using NIST SP 800-53 families
- Evidence artifacts support each control
- Python scripts simulate control validation
- Gaps are tracked through the POA&M

This structure reflects a simplified but realistic GRC program model used in small business environments.

---

## 🔄 Change Management and the Microsoft 365 Migration

Significant changes go through [change records](09-change-management/README.md) that walk each system through the NIST RMF steps (categorize, select, implement, assess, authorize, monitor):

* **CR-001** – Google Workspace to Microsoft 365 (cutover 2026-11-15). History is kept, not rewritten: dated records stay as written, and current-state documents change on the day
* **CR-003** – IT brought in-house; the outsourced provider offboarded with a recorded handover
* **CR-004** – Time-limited guest access for a vendor's payroll contact
* **CR-005** – The Toast POS replaced by an integrated register (approved, waiting on the website, CR-002)

Accepted risks are recorded in the [exception register](02-risk-management/risk-exceptions.md), each approved by the Owner with compensating controls and an expiry date.

---

## 📑 Policies & Procedures

The project includes formal governance **policies**:

* Access Management Policy (P-001)
* Acceptable Use Policy (P-002)
* Incident Response Policy (P-003)
* Payment Card Data Protection Policy (P-004)
* Network Security Policy (P-005)
* IT Operations Policy (P-006)
* Mobile Device and Personal Phone Policy (P-007)
* Third-Party Risk Management Policy (P-008)
* Personnel Security Policy (P-009)
* Records Retention and Disposal Policy (P-010)
* Physical Security Policy (P-011)

And supporting operational **procedures**:

* User access provisioning/deprovisioning (PR-001)
* Patch & vulnerability management (PR-002)
* Quarterly access review (PR-003)
* Log review (PR-004)
* Contingency and outage plan (PR-005)
* POS device inspection (PR-006)
* Security awareness training program (PR-007)
* IT administration and coverage (PR-008)
* Shared credential management with a password manager (PR-009)
* Equipment maintenance and lifecycle (PR-010)
* Connected devices: cameras and smart devices (PR-011)
* Backup and recovery (PR-012)
* Microsoft 365 tenant security baseline (PR-013)
* Risk acceptance and exceptions, with the exception register (PR-014)
* Device configuration baselines (PR-015)

---

## 🚨 Incident Response Capability

An incident response framework was developed including:

* Defined incident categories
* Escalation procedures
* Response playbooks
* Logging and documentation templates

Playbooks included:

* Phishing (IRP-001)
* Account compromise (IRP-002)
* POS suspicious activity (IRP-003)
* Lost or stolen device (IRP-004)
* Malware and ransomware (IRP-005)
* Vendor breach notification (IRP-006)
* Payment and payroll fraud (IRP-007)

---

## 📦 Evidence & Audit Readiness

An evidence pack was created to simulate audit validation. **Start with the [evidence index](07-evidence-pack/evidence-index.md)**: every artifact across the program's repositories, with dates and whether it is simulated or lab-verified.

* MFA status tracking (CSV)
* Access review and privileged-access review scripts (Python)
* Incident log review script (Python)
* Registers kept as evidence: equipment, maintenance, backups, disposals, keys and visitors, connected devices
* **Live tenant evidence** from the Microsoft 365 build, redacted with [`tools/tenant/redact_export.py`](tools/tenant/README.md) before it's committed

This demonstrates how controls can be validated and assessed in an audit-like scenario using structured evidence and repeatable review processes.

**Running the validation scripts** (Python 3, no external dependencies):

```bash
cd 07-evidence-pack/artifacts/scripts
python3 mfa_review_check.py
python3 access_review_check.py
python3 privileged_access_review_check.py
python3 incident_log_review_check.py
```

Each script reads the relevant evidence artifact and prints a review report that flags exceptions — for example, accounts missing MFA, stale access reviews, or unresolved incidents. Example templates that support these artifacts are kept in [`07-evidence-pack/examples/`](07-evidence-pack/examples/).

---

## 🤝 Vendor Risk Management

A third-party risk process was implemented including:

* Vendor intake questionnaire
* Risk scoring methodology
* Due diligence checklist
* Ongoing monitoring considerations
* Vendors are tracked in the [vendor inventory](02-risk-management/vendor-risk-management/vendor-inventory.md) and governed by the [Third-Party Risk Management Policy (P-008)](04-policies/P-008-third-party-risk.md): risk tiers set how deep and how often each vendor is assessed, and every contract needs a breach-notification clause.
* **Every vendor that needs an assessment has one**, executed in the companion [Vendor Risk Assessment Lab](https://github.com/MgnCoding2020/Vendor-Risk-Assessment-Lab): real vendors from their public compliance documents, fictional ones from simulated questionnaires. Exits get an offboarding record (Vertex IT Support, V-004).

---

## 📊 Continuous Monitoring & Metrics

The program monitors itself as well as the shop:

* **Consistency checker** ([`tools/check_program.py`](tools/check_program.py)): ten checks across all three repositories (people, systems and vendors match the canonical data, IDs, links, control counts, secrets, CSV format, and retired systems after a cutover). Runs in CI on every change
* **Monthly program monitor** (GitHub Actions): on the 1st of each month it runs the checker and a [due-date report](tools/due_dates.py) of overdue findings, upcoming deadlines, expiring exceptions and late recurring activities, and saves the result as a dated [report](07-evidence-pack/artifacts/monitoring/program-monitor/README.md) and a GitHub issue. It reads the records; it never marks anything done
* Periodic access reviews, log reviews, inspections, update windows and restore tests, each with its own record

Future enhancements may include KPI dashboards and risk trend analysis.

---

## 🚀 Key Skills Demonstrated

* GRC program development
* Risk assessment and analysis
* Control implementation and mapping
* Policy and procedure development
* Incident response planning
* Audit evidence preparation
* Vendor risk management, including exits
* Change management with NIST RMF steps
* Microsoft 365 and Entra ID identity design (groups, admin roles, MFA, tenant baseline)
* Automation: Python validation, PowerShell with Microsoft Graph, GitHub Actions
* Basic technical security validation

---

## 📈 Future Enhancements

* The Microsoft 365 build (CR-001): real accounts, MFA and sign-in evidence
* The online ordering website and new register (CR-002, CR-005)
* SIEM / logging simulation and KPI dashboards

---

## 📌 Disclaimer

This project is a **simulation for educational and portfolio purposes only** and does not represent a production environment.

---

## 👤 Author

Created as part of a cybersecurity portfolio focused on **GRC, Risk, and Security Operations roles**.

---
