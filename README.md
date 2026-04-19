# ☕ GRC Security Program Simulation – Coffee Shop Environment

## 📌 Overview

This project simulates the design and implementation of a **Governance, Risk, and Compliance (GRC) security program** for a small coffee shop handling **payment card data** and basic IT operations.

The goal of this project is to demonstrate how a real-world organization can:

* Identify and manage cybersecurity risks
* Implement security controls aligned to **NIST SP 800-53**
* Incorporate **PCI DSS concepts** for cardholder data protection
* Establish policies, procedures, and incident response capabilities
* Prepare for audit readiness through documentation and evidence collection

This repository reflects a **full security lifecycle**, from asset identification to continuous monitoring.
This project is structured to demonstrate a complete GRC lifecycle, connecting risk identification, control implementation, evidence validation, and remediation tracking within a cohesive security program.

---

## 🏢 Business Scenario

The organization is a small coffee shop with:

* A **Point-of-Sale (POS) system** processing payment card transactions
* Employee workstations for daily operations
* A basic internal network with internet connectivity
* Third-party vendors (POS provider, payment processor)

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

* NIST SP 800-53

  * Access Control (AC)
  * Identification & Authentication (IA)
  * Incident Response (IR)
  * System & Communications Protection (SC)
  * Risk Assessment (RA)

* PCI DSS (Conceptual Alignment)

  * Cardholder data protection
  * Network segmentation concepts
  * Access control enforcement
  * Logging and monitoring

---

## 🗂️ Project Structure

```
00-company-profile/
01-asset-inventory/
02-risk-management/
03-controls/
04-policies/
05-procedures/
06-incident-playbooks/
07-evidence-pack/
08-architecture/
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

> 📌 *Detailed diagrams and data flows are included in the architecture section.*

---

## ⚠️ Risk Management Approach

A structured risk management process was implemented:

1. Asset Identification
2. Threat & Vulnerability Mapping
3. Risk Scoring (Likelihood × Impact)
4. Control Implementation
5. Residual Risk Evaluation

### Sample Risks:

* Weak authentication controls on POS systems
* Lack of network segmentation
* Insufficient logging and monitoring
* Third-party vendor exposure

---

## 🛡️ Control Implementation

Controls were designed and mapped to **NIST SP 800-53 families**, including:

* **AC-2** – Account Management  
* **AC-6** – Least Privilege  
* **IA-2** – Multi-Factor Authentication  
* **AU-6** – Log Review  
* **SC-7** – Network Segmentation  

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

The project includes formal documentation such as:

* Access Control Policy
* Incident Response Policy
* Data Protection Policy
* Vendor Risk Management Policy

Supporting procedures define:

* User provisioning/deprovisioning
* Log review processes
* Incident escalation workflows

---

## 🚨 Incident Response Capability

An incident response framework was developed including:

* Defined incident categories
* Escalation procedures
* Response playbooks
* Logging and documentation templates

Example scenarios:

* Unauthorized access attempt
* POS compromise
* Suspicious network activity

---

## 📦 Evidence & Audit Readiness

An evidence pack was created to simulate audit validation:

* MFA status tracking (CSV)
* Access review scripts
* Incident logs
* Control validation artifacts

This demonstrates how controls can be validated and assessed in an audit-like scenario using structured evidence and repeatable review processes.

---

## 🤝 Vendor Risk Management

A third-party risk process was implemented including:

* Vendor intake questionnaire
* Risk scoring methodology
* Due diligence checklist
* Ongoing monitoring considerations

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

* Network and data flow diagrams
* Expanded control mapping (full NIST coverage)
* SIEM/logging simulation
* Compliance crosswalk (NIST ↔ PCI DSS)
* Automated compliance tracking

---

## 📌 Disclaimer

This project is a **simulation for educational and portfolio purposes only** and does not represent a production environment.

---

## 👤 Author

Created as part of a cybersecurity portfolio focused on **GRC, Risk, and Security Operations roles**.

---
