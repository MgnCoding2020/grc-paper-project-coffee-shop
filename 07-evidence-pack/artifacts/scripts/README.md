# 🛠️ Evidence Validation Scripts

## 📌 Overview

This directory contains scripts used to support **control validation and evidence generation** within the GRC security program.

These scripts are designed to simulate how organizations validate security controls through automated or semi-automated checks.

---

## 🧭 Purpose

The scripts in this folder support:

* Periodic access reviews
* Multi-factor authentication (MFA) validation
* Privileged account monitoring
* Incident tracking and review

They provide **supporting evidence** for control effectiveness and audit readiness.

---

## 🔐 Control Alignment

These scripts align with controls from:

* NIST SP 800-53:

  * AC-2 (Account Management)
  * AC-6 (Least Privilege)
  * IA-2 (Identification and Authentication)
  * AU-6 (Audit Review)
  * IR-4 (Incident Handling)

* PCI DSS Concepts:

  * Access control enforcement
  * Authentication validation
  * Logging and monitoring

---

## 📂 Script Inventory

### 🔍 `access_review_check.py`

Identifies inactive or unreviewed user accounts based on login activity and review status.

Supports:

* AC-2 (Account Management)
* AC-6 (Least Privilege)

---

### 🔑 `mfa_review_check.py`

Validates MFA enforcement and flags accounts without MFA or with outdated verification.

Supports:

* IA-2 (Multi-Factor Authentication)

---

### 🧱 `privileged_access_review_check.py`

Reviews privileged or administrative accounts and flags those lacking proper approval.

Supports:

* AC-2 (Account Management)
* AC-6 (Least Privilege)

---

### 🚨 `incident_log_review_check.py`

Parses the incident log and identifies unresolved or open incidents.

Supports:

* IR-4 (Incident Handling)
* AU-6 (Audit Review)

---

## 📊 Data Sources

Scripts reference files located in:

```plaintext
../
```

Including:

* `user-access-review.csv`
* `mfa-status.csv`
* `incident-log.md`

---

## ▶️ Usage

Scripts can be executed individually from the `scripts/` directory:

```bash
python <script_name>.py
```

---

## 📈 GRC Context

These scripts demonstrate how organizations:

* Validate control implementation
* Identify gaps in security posture
* Support audit and compliance activities

They are part of a broader **evidence collection and validation process**.

---

## ⚠️ Note

These scripts are designed for **demonstration and portfolio purposes only**.

They do not perform automated remediation and should be used alongside formal review and approval processes.

---
