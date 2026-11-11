# Vendor Inventory
Burn and Churn Coffee

---

## Purpose

This vendor inventory is the master list of all third-party vendors used by Burn and Churn Coffee. It records each vendor's service, the data they handle, their inherent risk tier, and the status of their most recent risk assessment.

The inventory is the entry point for the vendor risk management process: each vendor is tiered using the [Inherent Risk Scoring Worksheet](inherent-risk-scoring-worksheet.md), and Moderate/High-risk vendors receive a full assessment using the [Vendor Risk Assessment Template](vendor-risk-assessment-template.md). Findings from those assessments are tracked in the [POA&M](../../07-evidence-pack/poam/poam.md).

---

## Vendor Inventory

| Vendor ID | Vendor Name | Service Provided | Data Accessed / Processed | Inherent Risk Tier | Cardholder Data? | Assessment Status | Last Assessed | Assessment Reference | Owner | Status |
|-----------|-------------|------------------|---------------------------|--------------------|------------------|-------------------|---------------|----------------------|-------|--------|
| V-001 | Toast, Inc. (Toast POS, xtraCHEF) | Point-of-sale & payment processing; inventory | Cardholder / payment data; sales; inventory | High | Yes | Complete | 2026-10-30 | [Vendor Risk Assessment Lab](https://github.com/MgnCoding2020/Vendor-Risk-Assessment-Lab/tree/main/assessments/V-001-toast) (VRA-V001) | Owner | Active (continue with conditions); exit approved under [CR-005](../../09-change-management/CR-005-toast-pos-replacement.md) |
| V-002 | Northwind Payroll Services | Cloud payroll & HR (SaaS) | Employee PII, payroll, tax, direct-deposit banking | High | No | Complete | 2026-06-23 | [Vendor Risk Assessment Lab](https://github.com/MgnCoding2020/Vendor-Risk-Assessment-Lab) (VRA-V002) | Owner | Approved with conditions; onboarding pending (F-02, F-03 open) |
| V-003 | Microsoft (Microsoft 365) | Identity, email, files, intranet | Employee accounts; business documents; email | High | No | Complete | 2026-10-30 | [Vendor Risk Assessment Lab](https://github.com/MgnCoding2020/Vendor-Risk-Assessment-Lab/tree/main/assessments/V-003-microsoft) (VRA-V003) | Owner | Planned (CR-001) |
| V-004 | Vertex IT Support | IT managed services (privileged admin) | Admin access to Google Workspace and network equipment | High | No | Not Started | - | Offboarding record planned (CR-003) | Owner | Active; offboarding planned (CR-003) |
| V-005 | NorthPeak Systems | Former IT support vendor | Network admin account (still enabled at Q1 review) | Not scored | No | Not Required | - | IAM:F-003 | Owner | Inactive |
| V-006 | Intuit (QuickBooks Online) | Accounting software | Financial records | Not scored | No | Not Required (offboarding, CR-001) | - | - | Owner | Active; offboarding planned (CR-001) |
| V-007 | Google (Workspace) | Email and collaboration | Employee accounts; business documents; email | Not scored | No | Not Required (offboarding, CR-001) | - | - | Owner | Active; offboarding planned (CR-001) |
| V-008 | Internet service provider | Store internet connectivity; provider-managed router | Network traffic in transit | Moderate | No | Complete | 2026-11-02 | [Vendor Risk Assessment Lab](https://github.com/MgnCoding2020/Vendor-Risk-Assessment-Lab/tree/main/assessments/V-008-internet-provider) (VRA-V008) | Owner | Active (continue with conditions) |
| V-009 | Bitwarden, Inc. | Password manager (shared admin credentials) | Encrypted shared credentials | Moderate | No | Complete | 2026-11-02 | [Vendor Risk Assessment Lab](https://github.com/MgnCoding2020/Vendor-Risk-Assessment-Lab/tree/main/assessments/V-009-bitwarden) (VRA-V009) | Owner | Planned (CR-003); approved with conditions |
| V-010 | Cloud camera service (unnamed) | Security cameras and cloud video recording | Video of customers and staff | Moderate | No | Complete | 2026-11-02 | [Vendor Risk Assessment Lab](https://github.com/MgnCoding2020/Vendor-Risk-Assessment-Lab/tree/main/assessments/V-010-camera-service) (VRA-V010) | Owner | Active (continue with conditions) |
| V-011 | Espresso machine service company (unnamed) | Espresso machine servicing and remote diagnostics | Machine data; remote access to the machine | Moderate | No | Complete | 2026-11-01 | [Vendor Risk Assessment Lab](https://github.com/MgnCoding2020/Vendor-Risk-Assessment-Lab/tree/main/assessments/V-011-espresso-service) (VRA-V011) | Owner | Active (continue with conditions) |
| V-012 | Temperature monitoring service (unnamed) | Fridge temperature sensors and food-safety log | Temperature readings | Moderate | No | Complete | 2026-11-02 | [Vendor Risk Assessment Lab](https://github.com/MgnCoding2020/Vendor-Risk-Assessment-Lab/tree/main/assessments/V-012-temperature-monitoring) (VRA-V012) | Owner | Active (continue with conditions) |
| V-013 | Stripe, Inc. | Online payments (Checkout) and card-present payments (Terminal) | Payment tokens and order amounts; card data stays with Stripe | High | Yes | Complete | 2026-11-10 | [Vendor Risk Assessment Lab](https://github.com/MgnCoding2020/Vendor-Risk-Assessment-Lab/tree/main/assessments/V-013-stripe) (VRA-V013) | Owner | Active ([CR-002](../../09-change-management/CR-002-online-ordering-website.md); continue with conditions; also CR-005) |
| V-014 | Cloudflare, Inc. | Website hosting (Workers), D1 database, static assets, request logs, build and deploy | Website code and content; request logs (3-day retention); since 2026-11-07 staff names and directory IDs, roles, hashed sessions and the staff audit log (D1) | Moderate | No | Complete | 2026-11-08 | [Vendor Risk Assessment Lab](https://github.com/MgnCoding2020/Vendor-Risk-Assessment-Lab/tree/main/assessments/V-014-cloudflare) (VRA-V014) | Owner | Active ([CR-002](../../09-change-management/CR-002-online-ordering-website.md)); continue with conditions |
| V-015 | Google LLC (Google Password Manager) | The Owner's password manager for owner-held emergency and recovery credentials ([PR-009 §3](../../05-procedures/PR-009-credential-vault.md)) | Break-glass account passwords; two-factor recovery codes for the Stripe and Cloudflare accounts; backup-drive and vault-export passwords | High | No | Not Started (due 2026-11-25, POAM-038) | — | — | Owner | Active (in use since 2026-11-11; EXC-009) |

The machine-readable copy of this inventory is [vendors.csv](../../00-company-profile/org/vendors.csv); the two must match (the program's consistency checker verifies this).

**Revision history:** 2026-11-11, V-015 Google (Google Password Manager) added: the Owner's own password manager for owner-held emergency and recovery credentials, in use since 2026-11-11; assessment due 2026-11-25 (POAM-038). Bitwarden (V-009) stays planned as the shared Owner and IT Technician vault. 2026-11-10, V-013 Stripe assessed (a day late, in use since 2026-11-09): High 16/18, continue with conditions, VRA-V013:F-01 to F-06 under POAM-037; re-scored 17 at the CR-005 cutover. 2026-11-08, V-014 Cloudflare assessed (late, in use since 2026-11-02): Moderate 13/18, continue with conditions, VRA-V014:F-01 to F-05 under POAM-036; re-scored High when the register replaces Toast (CR-005). 2026-11-07, V-014 data updated (staff data in D1 since 2026-11-07) and its assessment marked overdue under P-008 step 5 (POAM-036, AL-30). 2026-11-05, V-013 Stripe and V-014 Cloudflare added with CR-002; assessments not started. 2026-10-30, V-003 to V-008 added and a Status column introduced, so every vendor named elsewhere in the program is inventoried (AL-05). 2026-10-30, V-003 Microsoft assessed before onboarding: High inherent risk, approved with conditions (POAM-018). 2026-10-30, V-002 status Active → onboarding pending: the pre-go-live conditions are still open (alignment review). 2026-10-30, V-001 Toast assessed for the first time, eight months after go-live: 18/18 High; continue with conditions (POAM-020).

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
