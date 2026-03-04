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

# Repository Structure

```
00-company-profile
    Business environment description

01-asset-inventory
    Asset inventory and data classification

02-risk-management
    Risk register identifying key security risks

03-controls
    Control matrix mapping risks to security controls

04-policies
    Core governance policies
        P-001 Access Management Policy
        P-002 Acceptable Use Policy
        P-003 Incident Response Policy
        P-004 Payment Card Data Protection Policy

05-procedures
    Operational procedures supporting policies

06-incident-playbooks
    Incident response playbooks for specific scenarios

07-evidence-pack
    Example evidence artifacts demonstrating control implementation
```

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

# Intended Audience

This project is designed for:

- cybersecurity hiring managers
- GRC teams evaluating entry-level candidates
- individuals learning governance and compliance fundamentals
- students building cybersecurity documentation portfolios

---

# Disclaimer

This project is a **simulated security program created for educational purposes**.

The documentation is not intended to represent a production-ready compliance program or serve as legal or regulatory guidance.

---

# Author

Created as part of a personal learning initiative to develop practical experience with Governance, Risk, and Compliance (GRC) security documentation.

---
