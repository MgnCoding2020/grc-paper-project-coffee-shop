# NIST SP 800-53 ↔ PCI DSS Crosswalk
Burn and Churn Coffee

---

## Purpose

This crosswalk maps the **NIST SP 800-53 (Rev. 5)** controls implemented in this program to the
**PCI DSS v4.0.1** requirements they help satisfy, and — going the other direction — shows how well
each of the 12 PCI DSS requirements is currently covered.

It is a **reference/translation document** and is intentionally kept separate from the
[control matrix](control-matrix.md), which tracks operational status, evidence, and remediation.
The matrix answers *"what controls do we run and are they working?"*; this crosswalk answers
*"how do our controls line up against PCI DSS, and where are the gaps?"*

> **Standard versions:** NIST SP 800-53 Rev. 5 · PCI DSS **v4.0.1** (the only active version in 2026;
> v4.0 retired and all formerly future-dated requirements are now mandatory).

---

## How to read this document

- **Part A** maps the program's **11 implemented controls** to their primary PCI DSS requirement(s).
- **Part B** broadens the view to **all 12 PCI DSS requirements**, marking each as
  ✅ Covered, ⚠️ Partial, or ❌ Gap based on whether an implemented control addresses it.
- **Part C** turns the gaps into **proposed POA&M items**, continuing the
  Risk → Control → Evidence → Validation → **Remediation** chain.

---

## Part A — Implemented NIST controls → PCI DSS

| NIST Control | Control Name | Risk ID | PCI DSS v4.0.1 Requirement | Impl. Status |
|--------------|--------------|---------|----------------------------|--------------|
| IA-2 | Identification & Authentication (MFA) | R-01 | **Req. 8** – Identify & authenticate access (8.3.1: MFA for *all* CDE access) | Partially Implemented |
| AT-2 | Awareness & Training | R-01 | **Req. 12.6** – Security awareness program | Not Implemented |
| AC-2 | Account Management | R-02 | **Req. 7 & 8** – Need-to-know access; user identification | Implemented |
| AU-6 | Audit Record Review, Analysis & Reporting | R-02 | **Req. 10** – Log & monitor all access | Partially Implemented |
| PE-3 | Physical Access Control | R-03 | **Req. 9** – Restrict physical access (9.5.1: POS device inspection) | Partially Implemented |
| SC-7 | Boundary Protection | R-04 | **Req. 1** – Network security controls / segmentation | Implemented |
| CP-2 | Contingency Plan | R-05 | **Req. 12.10** – Incident response / continuity (loose mapping\*) | Not Implemented |
| AC-6 | Least Privilege | R-06 | **Req. 7** – Need-to-know / least privilege | Implemented |
| SA-9 | External System Services | R-07 | **Req. 12.8** – Manage service providers (Toast POS) | Partially Implemented |
| SI-3 | Malicious Code Protection | R-08 | **Req. 5** – Protect from malicious software | Partially Implemented |
| SI-7 | Software, Firmware & Information Integrity | R-08 | **Req. 11.5** – Change / intrusion detection | Not Implemented |

\* PCI DSS has limited business-continuity coverage; CP-2's nearest analog is the incident response
plan under Req. 12.10. The mapping is directional, not one-to-one — a normal feature of crosswalks.

---

## Part B — PCI DSS coverage (all 12 requirements)

| # | PCI DSS v4.0.1 Requirement | Mapped NIST Control(s) | Coverage |
|---|----------------------------|------------------------|----------|
| 1 | Install & maintain network security controls | SC-7 | ✅ Covered |
| 2 | Apply secure configurations to all system components | *(none — CM-2 / CM-6 not implemented)* | ❌ Gap |
| 3 | Protect stored account data | P-004 policy *(SC-28 not implemented)* | ⚠️ Partial / scope-dependent |
| 4 | Protect cardholder data with strong cryptography in transit | *(none — SC-8 not implemented)* | ❌ Gap |
| 5 | Protect all systems & networks from malicious software | SI-3 | ✅ Covered (partial impl) |
| 6 | Develop & maintain secure systems & software | PR-002 procedure *(SI-2 not formalized)* | ⚠️ Partial |
| 7 | Restrict access by business need-to-know | AC-2, AC-6 | ✅ Covered |
| 8 | Identify users & authenticate access | IA-2, AC-2 | ✅ Covered — MFA gap (POAM-001) |
| 9 | Restrict physical access to cardholder data | PE-3 | ✅ Covered (partial impl) |
| 10 | Log & monitor all access | AU-6 | ✅ Covered (partial impl) |
| 11 | Test security of systems & networks regularly | SI-7 *(RA-5 / CA-8 not implemented)* | ❌ Gap (no vuln scan / pen test) |
| 12 | Support information security with policies & programs | AT-2, SA-9, P-001–P-004 | ✅ Covered (partial impl) |

**Summary:** 7 of 12 requirements have at least one implemented control; 2 are partial; 3 are gaps.

---

## Part C — Gaps → proposed POA&M items

The crosswalk surfaces PCI requirements with no implemented control. These extend the existing
POA&M (which currently runs POAM-001 through POAM-008):

| PCI Req | Gap | Suggested NIST Control | Proposed POA&M |
|---------|-----|------------------------|----------------|
| 2 | No documented secure-configuration baseline (default credentials, hardening) | CM-2, CM-6 | POAM-009 |
| 4 | Encryption of cardholder data in transit not documented | SC-8 | POAM-010 |
| 11.3 | No vulnerability scanning or penetration testing | RA-5, CA-8 | POAM-011 |
| 3 | Data-at-rest protection / storage scope not documented | SC-28 *(or document scope reduction)* | POAM-012 |

---

## Scope note — service provider & SAQ

Because **Toast POS** is a third-party point-of-sale and payment provider, a meaningful share of the
cardholder data environment is handled by the provider under a **shared-responsibility** model
(PCI DSS Req. 12.8). For a small card-present merchant, using a validated provider can **reduce PCI
scope** and determine which **Self-Assessment Questionnaire (SAQ)** applies. The precise SAQ type and
the requirements that remain the merchant's direct responsibility depend on exactly how card data is
captured and transmitted, which should be confirmed with the acquiring bank and documented using the
[vendor security documentation summary](../07-evidence-pack/examples/vendor-security-documentation-summary.md).

Note also that the e-commerce-focused requirements added in v4.0 (e.g., 6.4.3 and 11.6.1 for payment-page
scripts) are generally **not applicable** to a card-present-only environment — recording that
applicability decision is itself part of good scoping.

---

## Related documents

- [Control Matrix](control-matrix.md) — operational control status & evidence
- [Risk Register](../02-risk-management/risk-register.md)
- [Evidence Matrix](../07-evidence-pack/evidence-matrix.md)
- [POA&M](../07-evidence-pack/poam/poam.md)

---

## Disclaimer

This crosswalk is a **simulation for educational and portfolio purposes only**. Mappings are
directional and simplified; an official PCI DSS assessment must be performed against the full
standard by a Qualified Security Assessor (QSA) or via the appropriate SAQ.
