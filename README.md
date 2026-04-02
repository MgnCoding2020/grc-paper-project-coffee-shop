# GRC Paper Project – Coffee Shop Security Program

## Overview

This repository contains a mock Governance, Risk, and Compliance (GRC) security program designed for a small, single-location coffee shop called **Burn and Churn Coffee**.

The purpose of this project is to demonstrate how foundational cybersecurity governance artifacts can be developed for a small business environment that processes payment card transactions and relies on common cloud services.

The project simulates a realistic security program, including:

- security policies
- risk management documentation
- control mapping
- incident response planning
- payment card protection practices

The business environment assumes a **family-owned coffee shop operating one retail location** that uses **Toast POS for payment processing and Google Workspace for email and collaboration**.

This project is intended as a **learning and portfolio exercise for entry-level GRC roles**.

---

# Project Objectives

The goals of this project are to:

- Practice developing **security governance documentation**
- Understand how **risk registers connect to controls and policies**
- Demonstrate familiarity with **NIST control families**
- Incorporate **PCI DSS concepts relevant to retail payment environments**
- Build realistic documentation that reflects how **small businesses implement security programs**

---

# Environment Assumptions

The simulated business environment includes:

- Single retail coffee shop location
- Toast POS payment processing system
- Google Workspace for email and administrative services
- Company-issued tablets for operational use
- Staff Wi-Fi network and basic network infrastructure
- Limited IT staff, with most security responsibilities handled by the Business Owner and Store Manager

The organization **does not store payment card data locally** and relies on its payment processor (Toast) for PCI-compliant payment handling.

---

# Framework Alignment

The documentation in this repository aligns primarily with:

**NIST SP 800-53 control families**

Examples include:

- AC – Access Control  
- IA – Identification & Authentication  
- IR – Incident Response  
- AU – Audit & Accountability  
- SI – System & Information Integrity  
- CM – Configuration Management  

Where applicable, certain controls reference **PCI DSS security concepts** relevant to retail merchants processing payment card transactions.

This project does **not implement the full PCI DSS framework**, but demonstrates how PCI considerations may appear in a small merchant security program.

---

# How to Use This Repository

Readers can navigate the project in the following order:

1. **00-company-profile/**
   - Understand the business environment and program scope

2. **02-risk-management/**
   - Review identified risks and continuous monitoring approach

3. **03-controls/**
   - See how risks are mapped to security controls

4. **04-policies/** and **05-procedures/**
   - Review governance documentation and operational processes

5. **06-incident-playbooks/**
   - Understand how incidents are handled

6. **07-evidence-pack/**
   - Review evidence of control implementation and POA&M tracking

This flow reflects how a security program is assessed and reviewed in practice.

---

# Security Program Components

The repository demonstrates several key GRC artifacts commonly used in security governance programs:

### Policies
Define security expectations and governance requirements.

### Risk Register
Identifies and tracks cybersecurity risks affecting the organization.

### Control Matrix
Maps risks to implemented controls and governance policies.

### Incident Response Planning
Defines procedures for identifying, containing, and recovering from security incidents.

### Payment Card Security
Demonstrates merchant-level controls for protecting payment processing systems.

---

# GRC Lifecycle and Traceability

This project is structured to demonstrate how key GRC components connect in practice.

The security program follows a continuous lifecycle:

Risk → Control → Evidence → POA&M → Remediation

- Risks are identified and tracked in the **Risk Register**
- Controls are defined and mapped in the **Control Matrix**
- Evidence supporting control implementation is documented in the **Evidence Matrix**
- Control gaps and deficiencies are tracked in the **POA&M**
- Continuous monitoring activities support ongoing risk management and program improvement

This structure is intended to reflect how real-world GRC programs maintain traceability and accountability across security activities.

# Intended Audience

This project is designed for:

- cybersecurity hiring managers
- GRC teams evaluating entry-level candidates
- individuals learning governance and compliance fundamentals
- students building cybersecurity documentation portfolios
----

# Reusability and Extension

This repository is designed to serve as a foundational GRC framework that can be extended into additional projects and labs.

Future implementations may reuse components from this repository, including:

- Policies and control mappings for vendor risk assessments
- Evidence and POA&M structures for audit simulations
- Risk management approaches for system-specific evaluations

This approach reflects how organizations build and evolve security programs over time rather than starting from scratch for each initiative.

---

# Disclaimer

This project is a **simulated security program created for educational purposes**.

The documentation is not intended to represent a production-ready compliance program or serve as legal or regulatory guidance.

---

# Author

Created as part of a personal learning initiative to develop practical experience with Governance, Risk, and Compliance (GRC) security documentation.

---
