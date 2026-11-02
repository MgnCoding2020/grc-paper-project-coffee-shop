# Third-Party Risk Management Policy
Burn and Churn Coffee

## Document Control
**Policy Owner:** Business Owner | 
**Approved by:** Business Owner | 
**Effective Date:** 2026-11-02 | 
**Review Frequency:** Annual | 
**Version:** 1.0

----------

## 1. Purpose
A small coffee shop runs almost entirely on other companies' services: payments, email, payroll, internet, even the espresso machine. This policy sets the rules for choosing, contracting, monitoring and leaving those vendors, so their risks are known and managed rather than discovered.

It implements NIST SP 800-53 **SA-9 (External System Services)** and supports PCI DSS **12.8.1 to 12.8.5** (managing third-party service providers). The vendor templates and inventory already exist; this policy says when they must be used.

-----------

## 2. Scope
Every third party that stores, processes or can access company or customer data, connects to the store network or company systems, or that the business depends on to trade. The current list is the [vendor inventory](../02-risk-management/vendor-risk-management/vendor-inventory.md) (`vendors.csv`).

-----------

## 3. Before Signing (due diligence)
  1. **Inventory first.** Every new vendor gets a `V-###` ID in the inventory before any contract or access (PCI DSS 12.8.1).
  2. **Score the inherent risk** with the [six-factor worksheet](../02-risk-management/vendor-risk-management/inherent-risk-scoring-worksheet.md).
  3. **Assess according to the tier:**

| Tier (score) | Assessment before onboarding | Reassessment |
|---|---|---|
| **High** (14–18) | Full assessment in the Vendor Risk Assessment Lab: intake, due diligence, findings, decision | **Every year** |
| **Moderate** (9–13) | Full assessment | **Every two years**, or at contract renewal if sooner |
| **Low** (6–8) | Intake and a short review of the security overview | When the service or data changes |

  4. **Decide in writing:** approve, approve with conditions, or reject. The Owner signs the decision (PCI DSS 12.8.3).
  5. A vendor already in use but never assessed (like the espresso service company) is assessed as soon as it's found, and the decision becomes **continue, continue with conditions, or exit**.

-----------

## 4. What Every Contract Must Include
| Clause | Why |
|---|---|
| **Breach notification within 72 hours** of the vendor confirming an incident affecting company data | So the shop can act fast ([IRP-006](../06-incident-playbooks/IRP-006-vendor-breach.md)) |
| **Security responsibilities in writing**, and for card data, the provider's written acknowledgment that it is responsible for the cardholder data it handles | PCI DSS 12.8.2 |
| **Data return and deletion** at the end of the contract, with written confirmation | Clean exit |
| **Assurance on request:** a SOC 2 report, ISO/IEC 27001 certificate, PCI DSS Attestation of Compliance, or a security questionnaire for small vendors | Ongoing monitoring |
| **Subcontractors** disclosed, with notice of changes | The shop knows who else touches its data |
| **Vendor access rules:** named individual accounts, MFA, least privilege, only when needed (P-001 §5.7) | No generic or standing vendor access |

Existing contracts that lack a clause are fixed at renewal and tracked as findings until then.

-----------

## 5. While the Vendor Is in Use (monitoring)
  - **Card-data providers:** their PCI DSS compliance status is checked **every 12 months** (PCI DSS 12.8.4), and a responsibility matrix shows which PCI DSS requirements the provider meets and which the shop does (PCI DSS 12.8.5).
  - **Findings** from assessments are tracked to closure in the lab's remediation trackers and roll up to the POA&M.
  - **Vendor access** is reviewed in every quarterly access review.
  - **Vendor incidents** are handled under IRP-006, followed by reassessment.

-----------

## 6. Leaving a Vendor (offboarding)
Every exit has an **offboarding record** in the Vendor Risk Assessment Lab (the [Vertex IT Support record](https://github.com/MgnCoding2020/Vendor-Risk-Assessment-Lab/blob/main/offboarding/V-004-vertex-msp/offboarding-record.md) is the model): knowledge transferred, every account removed, every credential the vendor knew rotated, company data returned or deleted with written confirmation, the contract closed, and the inventory marked *Offboarded*. A change record covers any exit that changes systems (CM-3).

-----------

## 7. Roles
| Role | Responsibility |
|---|---|
| **Owner** | Accountable; approves every vendor decision and contract; owns vendor relationships |
| **IT Technician** | Technical due diligence; vendor accounts and access; offboarding steps |
| **Store Manager** | Raises new vendors before they're engaged; consulted on operational vendors |

-----------

## 8. Exceptions
A vendor that can't meet a requirement may still be used if the Owner accepts the risk in writing, with compensating controls, under the [risk acceptance procedure](../02-risk-management/risk-register.md) and with a review date.

-----------

## 9. Current Status
The process runs in the Vendor Risk Assessment Lab: V-001, V-002, V-003 and V-011 are assessed and V-004's offboarding record is prepared. Not yet assessed: V-009, V-010 and V-012. Breach-notification clauses are missing for Toast (VRA-V001:F-03), Northwind (VRA-V002:F-03) and the espresso service (VRA-V011:F-04). Tracked under **POAM-006** (SA-9).

-----------

## 10. Related Documents
  - [Vendor inventory](../02-risk-management/vendor-risk-management/vendor-inventory.md) and the vendor templates in the same folder
  - [Vendor Risk Assessment Lab](https://github.com/MgnCoding2020/Vendor-Risk-Assessment-Lab)
  - [Access Management Policy (P-001)](P-001-access-control.md) §5.7
  - [Vendor Breach Notification Playbook (IRP-006)](../06-incident-playbooks/IRP-006-vendor-breach.md)

-----------

*This document is a simulation for educational and portfolio purposes only.*
