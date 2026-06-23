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

## 🏢 Business Scenario

**Burn and Churn Coffee** is a small coffee shop with:

* A **Point-of-Sale (POS) system** processing payment card transactions
* Employee workstations for daily operations
* A basic internal network with internet connectivity
* Third-party vendors (**Toast POS** as the point-of-sale provider, plus the payment processor)

### Key Risks:

* Unauthorized access to POS systems
* Exposure of cardholder data
* Lack of centralized monitoring and logging
* Weak vendor security oversight

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

* **NIST SP 800-53** — control families implemented in the [control matrix](03-controls/control-matrix.md):

  * Access Control (AC)
  * Awareness & Training (AT)
  * Audit & Accountability (AU)
  * Configuration Management (CM)
  * Contingency Planning (CP)
  * Identification & Authentication (IA)
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
├── 01-asset-inventory/      # Asset register, data classification, asset lifecycle & review
├── 02-risk-management/      # Risk register, continuous monitoring, vendor risk management
├── 03-controls/             # Control matrix (NIST 800-53 ↔ PCI DSS) and evidence plan
├── 04-policies/             # P-001–P-004 governance policies
├── 05-procedures/           # PR-001–PR-004 operational procedures
├── 06-incident-playbooks/   # IRP-001–IRP-004 incident response playbooks
├── 07-evidence-pack/        # Evidence matrix, POA&M, artifacts, and validation scripts
└── 08-architecture/         # System architecture and data-flow diagrams
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
* **R-07** – Vendor compromise or service disruption (Toast POS)

---

## 🛡️ Control Implementation

Controls were designed and mapped to **NIST SP 800-53 families** and, where relevant, **PCI DSS requirements**. A representative sample:

* **IA-2** – Multi-Factor Authentication (PCI Req. 8)
* **AC-2** – Account Management (PCI Req. 7)
* **AC-6** – Least Privilege (PCI Req. 7)
* **AU-6** – Log Review (PCI Req. 10)
* **SC-7** – Network Segmentation (PCI Req. 1)

The full set of 11 controls, with implementation status and PCI mappings, is maintained in the [control matrix](03-controls/control-matrix.md).

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

## 📑 Policies & Procedures

The project includes formal governance **policies**:

* Access Control Policy (P-001)
* Acceptable Use Policy (P-002)
* Incident Response Policy (P-003)
* Payment Card Data Protection Policy (P-004)

And supporting operational **procedures**:

* User access provisioning/deprovisioning (PR-001)
* Patch & vulnerability management (PR-002)
* Quarterly access review (PR-003)
* Log review (PR-004)

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

---

## 📦 Evidence & Audit Readiness

An evidence pack was created to simulate audit validation:

* MFA status tracking (CSV)
* Access review and privileged-access review scripts (Python)
* Incident log review script (Python)
* Control validation artifacts

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
* Vendors are tracked in the [vendor inventory](02-risk-management/vendor-risk-management/vendor-inventory.md). A full worked example — the assessment of Northwind Payroll Services — is executed in the companion [Vendor Risk Assessment Lab](https://github.com/MgnCoding2020/Vendor-Risk-Assessment-Lab), with findings rolled up here under POAM-013 (SA-9).

---

## 📊 Continuous Monitoring & Metrics

Continuous monitoring concepts were implemented using periodic reviews, log analysis, and control validation activities:

* Periodic access reviews
* Log review processes
* Control validation tracking

Future enhancements may include:

* KPI dashboards
* Automated monitoring scripts
* Risk trend analysis

---

## 🚀 Key Skills Demonstrated

* GRC program development
* Risk assessment and analysis
* Control implementation and mapping
* Policy and procedure development
* Incident response planning
* Audit evidence preparation
* Vendor risk management
* Basic technical security validation

---

## 📈 Future Enhancements

* Expanded control mapping (broader NIST 800-53 coverage)
* SIEM / logging simulation
* Automated compliance tracking and KPI dashboards

---

## 📌 Disclaimer

This project is a **simulation for educational and portfolio purposes only** and does not represent a production environment.

---

## 👤 Author

Created as part of a cybersecurity portfolio focused on **GRC, Risk, and Security Operations roles**.

---
