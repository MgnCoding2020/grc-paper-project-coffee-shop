# 🧠 System Architecture Diagram

## 📌 Overview

This diagram represents the simulated network architecture for the coffee shop environment. It highlights system components, trust boundaries, and security controls aligned with NIST SP 800-53 and PCI DSS concepts.

---

## 🏗️ Architecture Description

The environment consists of:

* A **Point-of-Sale (POS) system** handling cardholder transactions
* **Employee workstations** for business operations
* A **segmented network** protected by a firewall
* External connections to:

  * Payment processor
  * Third-party vendors

---

## 🔐 Key Security Components

### 🔥 Firewall / Boundary Protection

* Acts as the primary network security boundary
* Filters inbound and outbound traffic
* Supports segmentation between internal and external systems

---

### 💳 POS System (Cardholder Data Environment)

* Processes payment card transactions
* Transmits sensitive data securely to payment processor
* Highest security priority system

---

### 💻 Internal Systems

* Office workstations used by employees
* Restricted access to sensitive systems
* Subject to access control and monitoring

---

### 📶 WiFi Network

* Separate from POS environment (segmentation concept)
* Used by employee devices
* Limited access to internal resources

---

### 🌐 External Systems

* Payment processor (handles card transactions)
* Vendors providing POS or IT services

---

### 📊 Logging & Monitoring

* Centralized logging concept
* Supports audit and incident response

---

### 🔑 Access Control / MFA

* Controls user authentication
* Enforces least privilege access

---

## 🧱 Security Boundaries

The architecture enforces:

* Network segmentation between POS and internal systems
* Controlled communication with external entities
* Logical separation of sensitive data environments

---

## 🧭 Alignment with Security Frameworks

This architecture supports:

* NIST SP 800-53:

  * SC-7 (Boundary Protection)
  * AC-2 (Account Management)
  * IA-2 (Authentication)
  * AU-6 (Audit Review)

* PCI DSS Concepts:

  * Cardholder data environment isolation
  * Secure transmission of payment data
  * Network segmentation

---

## 📌 Notes

This is a simplified architecture intended for educational and portfolio demonstration purposes.

---
