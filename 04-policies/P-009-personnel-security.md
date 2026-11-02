# Personnel Security Policy
Burn and Churn Coffee

## Document Control
**Policy Owner:** Business Owner | 
**Approved by:** Business Owner | 
**Effective Date:** 2026-11-02 | 
**Review Frequency:** Annual | 
**Version:** 1.0

----------

## 1. Purpose
Most of the shop's security depends on its people: a barista at the register, a manager with access to payroll, an IT Technician with admin rights. This policy ties together what happens to security at each stage of employment, from hiring to leaving, so nobody gets access before they're ready for it or keeps it after they've gone.

It implements NIST SP 800-53 **PS-2, PS-3, PS-4, PS-5, PS-6, PS-7 and PS-8** and supports PCI DSS **12.7.1** (screening personnel who will have access to the cardholder data environment).

-----------

## 2. Scope
Every employee, the part-time IT Technician, and external personnel (vendors' staff, temporary workers) who use company systems or work in the store.

-----------

## 3. Position Risk (PS-2)
| Level | Roles | Why |
|---|---|---|
| **High** | Owner, IT Technician | Admin accounts; access to every system and shared credential |
| **Moderate** | Store Manager, Shift Leaders | Approve access; handle cash, refunds and staff records; supervise the register |
| **Standard** | Baristas | Register sign-in, the intranet, their own records |

-----------

## 4. Screening (PS-3)
  - **High** roles: background screening before any admin access is granted, recorded in the personnel file (CR-003 requires it for the IT Technician).
  - **Moderate** roles: reference check and identity verification before starting.
  - **Standard** roles: identity verification and right-to-work check.
  - Screening is done **within the limits of local law**, with the person's written consent, and only to the extent the role needs. Results are confidential and kept by the Owner only.
  - Everyone who uses the register has access to payment devices, so everyone is screened at least to the Standard level before their first shift (PCI DSS 12.7.1).

-----------

## 5. Agreements Before Access (PS-6)
Before receiving any account or register PIN, each person signs:

| Agreement | Who |
|---|---|
| Acceptable Use Policy acknowledgment ([P-002](P-002-acceptable-use.md)) | Everyone |
| Confidentiality agreement (company, staff and customer information) | Everyone |
| Personal phone policy acknowledgment ([P-007](P-007-mobile-devices.md)), if using a personal phone for MFA | Everyone who does |
| [Privileged User Agreement](../07-evidence-pack/examples/privileged-user-agreement.md) | Owner and IT Technician |

Agreements are renewed every year with security training ([PR-007](../05-procedures/PR-007-security-awareness-training.md)), and after any significant change to the policies.

-----------

## 6. Changing Roles (PS-5)
When someone's role changes, access for the new role is granted and access the new role doesn't need is removed within three business days ([PR-001](../05-procedures/PR-001-user-access.md)). A promotion to a higher position-risk level triggers that level's screening first.

-----------

## 7. Leaving (PS-4)
  - Accounts are disabled **within 24 hours** of leaving, and **immediately** for an involuntary termination (P-001 §5.4). The register PIN is removed, MFA methods are removed, and the staff Wi-Fi passphrase is changed ([P-005](P-005-network-security.md)).
  - Keys, security keys and any company equipment are returned and recorded.
  - Shared credentials the person knew are rotated ([PR-009](../05-procedures/PR-009-credential-vault.md)).
  - Confidentiality obligations continue after leaving.

The Q1 2026 access review found a terminated employee's accounts still active (IAM:F-001). That gap is why this section has firm deadlines.

-----------

## 8. External Personnel (PS-7)
Vendors' staff and temporary workers follow the same rules as employees for the access they get: named accounts, signed agreements where they use company systems, supervision on site ([PR-010](../05-procedures/PR-010-equipment-lifecycle.md) §4), and removal when the work ends ([P-008](P-008-third-party-risk.md) §6).

-----------

## 9. Sanctions (PS-8)
Breaking security policies leads to disciplinary action in line with company procedures, proportionate to the harm and intent, up to dismissal. Reporting a mistake promptly is always treated more favourably than hiding it.

-----------

## 10. Personnel File
Each person has a file, kept by the Owner, recording screening, signed agreements and dates, using the [personnel file checklist](../07-evidence-pack/examples/personnel-file-checklist.md) (evidence E-29).

-----------

## 11. Current Status
No screening or confidentiality agreements are recorded for current staff, who were hired before this policy. Existing staff sign the agreements in the first training session (by 2026-11-30). The IT Technician is screened and signs before receiving admin access (CR-003). Tracked under **POAM-032**.

-----------

## 12. Related Documents
  - [Access Management Policy (P-001)](P-001-access-control.md)
  - [User Access Management Procedure (PR-001)](../05-procedures/PR-001-user-access.md)
  - [Roles and Responsibilities](../00-company-profile/org/roles.md)
  - [CR-003: Bring IT Support In-House](../09-change-management/CR-003-it-support-in-house.md)

-----------

*This document is a simulation for educational and portfolio purposes only.*
