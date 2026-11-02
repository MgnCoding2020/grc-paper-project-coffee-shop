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

- **Part A** maps all **39 controls in the control matrix** to their primary PCI DSS requirement(s), whatever their implementation status. Of the 39: 0 Implemented, 21 Partially Implemented, 18 Not Implemented (AC-2, AC-6 and SC-7 were downgraded on 2026-10-30; see the revision history).
- **Part B** broadens the view to **all 12 PCI DSS requirements**, marking each as
  ✅ Covered, ⚠️ Partial, or ❌ Gap based on whether an implemented control addresses it.
- **Part C** turns the gaps into **proposed POA&M items**, continuing the
  Risk → Control → Evidence → Validation → **Remediation** chain.

---

## Part A — NIST controls → PCI DSS

| NIST Control | Control Name | Risk ID | PCI DSS v4.0.1 Requirement | Impl. Status |
|--------------|--------------|---------|----------------------------|--------------|
| IA-2 | Identification & Authentication (MFA) | R-01 | **Req. 8** – Identify & authenticate access (8.3.1: MFA for *all* CDE access) | Partially Implemented |
| AT-2 | Awareness & Training | R-01 | **Req. 12.6** – Security awareness program | Not Implemented |
| AC-2 | Account Management | R-02 | **Req. 7 & 8** – Need-to-know access; user identification | Partially Implemented |
| AU-6 | Audit Record Review, Analysis & Reporting | R-02 | **Req. 10** – Log & monitor all access | Partially Implemented |
| CM-6 | Configuration Settings | R-02 | **Req. 2** – Apply secure configurations to all system components | Not Implemented |
| PE-3 | Physical Access Control | R-03 | **Req. 9** – Restrict physical access (9.5.1: POS device inspection) | Partially Implemented |
| SC-7 | Boundary Protection | R-04 | **Req. 1** – Network security controls / segmentation | Partially Implemented |
| CP-2 | Contingency Plan | R-05 | **Req. 12.10** – Incident response / continuity (loose mapping\*) | Partially Implemented |
| CP-9 | System Backup | R-19 | **Req. 12.10.1** – The incident response plan covers data backup processes | Not Implemented |
| CP-10 | System Recovery and Reconstitution | R-19 | **Req. 12.10.1** – The incident response plan covers business recovery and continuity procedures | Not Implemented |
| AC-6 | Least Privilege | R-06 | **Req. 7** – Need-to-know / least privilege | Partially Implemented |
| AC-19 | Access Control for Mobile Devices | R-21 | *No direct PCI DSS requirement* (card data is never on phones: P-004) | Not Implemented |
| SA-9 | External System Services | R-07 | **Req. 12.8.1–12.8.5** – Manage third-party service providers: inventory, written agreements, due diligence, annual compliance checks, responsibility matrix (P-008) | Partially Implemented |
| SI-3 | Malicious Code Protection | R-08 | **Req. 5** – Protect from malicious software | Partially Implemented |
| SI-7 | Software, Firmware & Information Integrity | R-08 | **Req. 11.5** – Change / intrusion detection | Not Implemented |
| RA-5 | Vulnerability Monitoring & Scanning | R-08 | **Req. 11** – Test security of systems & networks regularly | Not Implemented |
| SC-8 | Transmission Confidentiality & Integrity | R-09 | **Req. 4** – Protect cardholder data with strong cryptography in transit | Not Implemented |
| SC-28 | Protection of Information at Rest | R-09 | **Req. 3** – Protect stored account data | Not Implemented |
| PS-4 | Personnel Termination | R-10 | **Req. 8.2.5** – Access for terminated users is immediately revoked | Partially Implemented |
| PS-5 | Personnel Transfer | R-10 | **Req. 7.2** – Access assigned by job function (loose mapping\*) | Not Implemented |
| PS-3 | Personnel Screening | R-22 | **Req. 12.7.1** – Personnel with access to the cardholder data environment are screened before hire, within local law | Not Implemented |
| PS-6 | Access Agreements | R-22 | **Req. 12.2.1** – Acceptable use policies for end-user technologies (loose mapping\*: signed acknowledgments) | Partially Implemented |
| CM-3 | Configuration Change Control | R-11 | **Req. 6.5.1** – Changes follow documented change-control procedures | Partially Implemented |
| CM-4 | Impact Analyses | R-11 | **Req. 6.5.1** – Changes record their security impact | Partially Implemented |
| IA-5 | Authenticator Management | R-13 | **Req. 8.3** – Strong authentication for users and administrators; **8.6** – System and application account credentials strictly managed (loose mapping\*: shared device and portal credentials) | Not Implemented |
| SI-2 | Flaw Remediation | R-15 | **Req. 6.3.3** – Critical and high-security patches installed within one month of release | Partially Implemented |
| CM-8 | System Component Inventory | R-15 | **Req. 12.5.1** – Inventory of in-scope system components maintained; **Req. 9.5.1.1** – list of POI devices | Partially Implemented |
| MA-2 | Controlled Maintenance | R-16 | **Req. 9.5.1** – POI devices protected from tampering and substitution (loose mapping\*: maintenance of card-reading devices) | Not Implemented |
| MA-5 | Maintenance Personnel | R-16 | **Req. 9.5.1.3** – Personnel trained to verify the identity of anyone claiming to be repair or maintenance personnel before granting access | Not Implemented |
| SA-22 | Unsupported System Components | R-15 | **Req. 12.3.4** – Hardware and software technologies reviewed at least once every 12 months, including plans for end-of-life | Not Implemented |
| MA-4 | Nonlocal Maintenance | R-17 | **Req. 8.2.7** – Third-party remote access accounts enabled only when needed, and monitored (loose mapping\*: vendor remote diagnostics on the espresso machine, outside the card environment) | Not Implemented |
| PE-6 | Monitoring Physical Access | R-18 | *No direct PCI DSS requirement* (the camera rule keeps PIN entry off camera) | Not Implemented |
| IR-4 | Incident Handling | R-20 | **Req. 12.10.1** – An incident response plan exists and is ready to be activated, with specific response procedures | Partially Implemented |
| IR-8 | Incident Response Plan | R-20 | **Req. 12.10.1**; **12.10.2** – The plan is reviewed, updated and tested at least once every 12 months | Partially Implemented |
| SI-12 | Information Management and Retention | R-23 | **Req. 3.2.1** – Account data storage kept to a minimum with retention and disposal policies (loose mapping\*: the shop stores no card data) | Partially Implemented |
| MP-6 | Media Sanitization | R-23 | **Req. 9.4.6** – Hard-copy materials with cardholder data destroyed when no longer needed; **9.4.7** – electronic media likewise (secondary sources\*) | Not Implemented |
| RA-7 | Risk Response | R-12 | *No direct PCI DSS requirement* | Partially Implemented |
| CA-5 | Plan of Action and Milestones | R-12 | *No direct PCI DSS requirement* (supports remediation of every requirement's gaps) | Partially Implemented |
| CA-7 | Continuous Monitoring | R-12 | *No direct PCI DSS requirement* (the monitor reports late PCI-related activities, such as device inspections under PCI DSS 9.5.1.2) | Partially Implemented |

\* PCI DSS has limited business-continuity coverage; CP-2's nearest analog is the incident response
plan under Req. 12.10. The mapping is directional, not one-to-one — a normal feature of crosswalks.

---

## Part B — PCI DSS coverage (all 12 requirements)

| # | PCI DSS v4.0.1 Requirement | Mapped NIST Control(s) | Coverage |
|---|----------------------------|------------------------|----------|
| 1 | Install & maintain network security controls | SC-7 | ✅ Covered (partial impl) |
| 2 | Apply secure configurations to all system components | *(none — CM-2 / CM-6 not implemented)* | ❌ Gap |
| 3 | Protect stored account data | P-004 policy, SI-12 (3.2.1) *(SC-28 not implemented)* | ⚠️ Partial / scope-dependent |
| 4 | Protect cardholder data with strong cryptography in transit | *(none — SC-8 not implemented)* | ❌ Gap |
| 5 | Protect all systems & networks from malicious software | SI-3 | ✅ Covered (partial impl) |
| 6 | Develop & maintain secure systems & software | CM-3, CM-4 (6.5.1), SI-2 (6.3.3, PR-002) | ⚠️ Partial |
| 7 | Restrict access by business need-to-know | AC-2, AC-6, PS-5 | ✅ Covered (partial impl) |
| 8 | Identify users & authenticate access | IA-2, IA-5, AC-2, PS-4 (8.2.5), MA-4 (8.2.7, loose) | ✅ Covered — MFA gap (POAM-001); termination gap (POAM-016) |
| 9 | Restrict physical access to cardholder data | PE-3, MA-2, MA-5 (Req. 9.5.1.3), CM-8 (Req. 9.5.1.1), MP-6 (Req. 9.4.6, 9.4.7) | ✅ Covered (partial impl) |
| 10 | Log & monitor all access | AU-6 | ✅ Covered (partial impl) |
| 11 | Test security of systems & networks regularly | SI-7 *(RA-5 / CA-8 not implemented)* | ❌ Gap (no vuln scan / pen test) |
| 12 | Support information security with policies & programs | AT-2, SA-9 (12.8), PS-3 (12.7.1), PS-6 (12.2.1), CM-8 (12.5.1), SA-22 (12.3.4), CP-9 and CP-10 (12.10.1), IR-4 and IR-8 (12.10.1, 12.10.2), P-001–P-010 | ✅ Covered (partial impl) |

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

---

## Revision History

| Date | Change | Reason |
|---|---|---|
| 2026-10-30 | AC-2, AC-6 and SC-7: Implemented → Partially Implemented; PCI DSS Requirements 1 and 7 marked "Covered (partial impl)" | Kept in step with the control matrix (AL-16, AL-19) |
| 2026-10-30 | Added PS-4, PS-5, CM-3, CM-4; Requirements 6, 7 and 8 updated | PCI DSS v4.0.1 numbers 8.2.5 and 6.5.1 checked against secondary sources on 2026-10-30; confirm against the PCI SSC standard text. PS-5 → 7.2 is a loose mapping |
| 2026-11-02 | Added SI-12, MP-6 and RA-7 | Retention and disposal (P-010), risk acceptance (PR-014); 9.4.6 and 9.4.7 from secondary sources, to verify against the PCI SSC text |
| 2026-11-02 | Added PS-3 and PS-6; SA-9 mapped to 12.8.1–12.8.5 | Personnel Security (P-009) and Third-Party Risk Management (P-008) policies |
| 2026-11-01 | Added AC-19 | Personal phones used for MFA (P-007); no direct PCI DSS requirement |
| 2026-11-01 | Added IR-4 and IR-8 | Incident response plan and playbooks (P-003 v1.2, IRP-005 to IRP-007) |
| 2026-11-01 | Added CP-9 and CP-10 | Backups and recovery (PR-012), mapped to the backup and recovery parts of 12.10.1 |
| 2026-11-01 | Added CA-7 | Monthly program monitor; no direct PCI DSS requirement |
| 2026-11-01 | Added MA-4 and PE-6 | Connected devices (PR-011); MA-4 loosely mapped to 8.2.7; PE-6 has no direct PCI DSS requirement |
| 2026-11-01 | Added SI-2, CM-8, MA-2, MA-5, SA-22 | IT Operations Policy (P-006); MA-2 loosely mapped to 9.5.1 |
| 2026-10-30 | Added IA-5 | Shared admin credentials (PR-009); loose mapping to 8.3 and 8.6 |
| 2026-10-30 | Added CA-5 | POA&M management; no direct PCI DSS equivalent |
| 2026-10-30 | CP-2 Not Implemented → Partially Implemented | Contingency and outage plan (PR-005) documented, not yet tested |
