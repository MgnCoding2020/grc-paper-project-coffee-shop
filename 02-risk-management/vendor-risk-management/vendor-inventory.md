# Vendor Inventory
Burn and Churn Coffee

---

## Purpose

This vendor inventory is the master list of all third-party vendors used by Burn and Churn Coffee. It records each vendor's service, the data they handle, their inherent risk tier, and the status of their most recent risk assessment.

The inventory is the entry point for the vendor risk management process: each vendor is tiered using the [Inherent Risk Scoring Worksheet](inherent-risk-scoring-worksheet.md), and Moderate/High-risk vendors receive a full assessment using the [Vendor Risk Assessment Template](vendor-risk-assessment-template.md). Findings from those assessments are tracked in the [POA&M](../../07-evidence-pack/poam/poam.md).

---

## Vendor Inventory

| Vendor ID | Vendor Name | Service Provided | Data Accessed / Processed | Inherent Risk Tier | Cardholder Data? | Assessment Status | Last Assessed | Assessment Reference | Owner |
|-----------|-------------|------------------|---------------------------|--------------------|------------------|-------------------|---------------|----------------------|-------|
| V-001 | Toast POS | Point-of-sale & payment processing | Cardholder / payment data | High | Yes | Not Started | - | Planned | Owner |
| V-002 | Northwind Payroll Services | Cloud payroll & HR (SaaS) | Employee PII, payroll, tax, direct-deposit banking | High | No | Complete | 2026-06-23 | Vendor Risk Assessment Lab (repo) | Owner |

---

## How Vendors Are Tiered

Inherent risk tier is assigned **before** reviewing a vendor's security controls, based on:

- **Data sensitivity** — the type and sensitivity of data the vendor handles
- **System access** — how deeply the vendor connects to internal systems
- **Operational dependency** — how critical the vendor is to daily operations
- **Regulatory exposure** — whether the data falls under PCI DSS, privacy, or financial regulations

A higher tier means deeper due diligence is required. See the [Inherent Risk Scoring Worksheet](inherent-risk-scoring-worksheet.md) for the scoring method.

---

## Process Linkage

1. New vendor → complete the **Vendor Intake Questionnaire**
2. Score inherent risk → record the **tier** in this inventory
3. Moderate/High tier → perform **Due Diligence** and a full **Vendor Risk Assessment**
4. Assessment findings → tracked as **POA&M** items and, where needed, new **risk register** entries
5. Update this inventory's **Assessment Status** and **Last Assessed** date

---

## Related Documents

- [Vendor Intake Questionnaire](vendor-intake-questionnaire.md)
- [Inherent Risk Scoring Worksheet](inherent-risk-scoring-worksheet.md)
- [Vendor Due Diligence Checklist](vendor-due-diligence-checklist.md)
- [Vendor Risk Assessment Template](vendor-risk-assessment-template.md)
- [Risk Register](../risk-register.md) · program control **SA-9** (vendor management)
- [POA&M](../../07-evidence-pack/poam/poam.md)

---

*This document is a simulation for educational and portfolio purposes only.*
