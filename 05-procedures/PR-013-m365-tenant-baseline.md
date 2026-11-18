# Microsoft 365 Tenant Security Baseline
Burn and Churn Coffee

---

## Document Control
**Owner:** Business Owner | **Performed by:** IT Technician | **Approved by:** Business Owner | **Effective:** 2026-11-15 (applied on build day, CR-001) | **Review:** Every 6 months, and when the licence changes | **Version:** 1.0

---

## 1. Purpose
The exact security settings for the Microsoft 365 tenant: what each one is set to, and why. It's the secure configuration baseline (NIST SP 800-53 **CM-2** and **CM-6**) for Microsoft 365, so the tenant is set up the same way every time and drift can be spotted. It supports IA-2 (MFA), AC-2, AC-6 and AU-2.

**Shared tenant note:** Burn and Churn's accounts live in the same tenant as Michael's lab (D-4). Settings marked **tenant-wide** also apply to the lab's users. Each one is standard good practice, but Michael confirms them before applying.

Facts checked against Microsoft Learn on 2026-11-01 (sources at the end).

---

## 2. Baseline Settings (Entra ID Free)

### 2.1 Sign-in and MFA
| Setting | Value | Why | Scope |
|---|---|---|---|
| **Per-user MFA** | **Enforced** for every Burn and Churn account (`grp-bc-*` members and `adm-` accounts) | MFA on every account (P-001 §5.5, IA-2) | Burn and Churn only |
| Security defaults | **Off** | They're tenant-wide and would change the lab's users; per-user MFA is used instead (recorded decision) | Tenant-wide |
| MFA methods | **Microsoft Authenticator** (number matching); **FIDO2 security keys** for staff who don't use a personal phone (P-007 §5); SMS only as a temporary fallback while a new phone is set up | Phishing-resistant where possible | Tenant-wide |
| Password expiry | **Never expire** | With MFA, forced periodic changes make passwords weaker; NIST SP 800-63B advises against them. Passwords change on suspected compromise | Tenant-wide |

### 2.2 What ordinary users can do
| Setting (Entra admin centre → Users → User settings) | Value | Why | Scope |
|---|---|---|---|
| Users can register applications | **No** | Stops staff creating app registrations that could reach company data | Tenant-wide |
| Restrict non-admin users from creating tenants | **Yes** | New tenants are created outside the company's control | Tenant-wide |
| Users can create security groups | **No** | Groups are the access model (P-001); only admins create them | Tenant-wide |
| Users can create Microsoft 365 groups | **No** | Same reason; avoids unmanaged Teams and SharePoint sites | Tenant-wide |
| LinkedIn account connections | **No** | No company directory data shared with LinkedIn | Tenant-wide |
| Restrict access to the Microsoft Entra admin centre | **Yes** | Adds friction for casual browsing. **Microsoft is explicit that this isn't a security control**; Conditional Access is the real one, once licensed | Tenant-wide |

### 2.3 Apps and consent
| Setting (Enterprise apps → Consent and permissions) | Value | Why | Scope |
|---|---|---|---|
| User consent for applications | **Do not allow user consent** | Consent phishing (a fake app asking for mailbox access) is a common attack | Tenant-wide |
| Admin consent requests | **On**; reviewers: the Owner's and IT Technician's admin accounts | Staff can still ask for an app; an admin decides | Tenant-wide |

### 2.4 Guests (external collaboration)
| Setting | Value | Why | Scope |
|---|---|---|---|
| Guest user access | **Restricted to properties and memberships of their own directory objects** | A vendor guest can't browse the staff directory | Tenant-wide |
| Guest invite restrictions | **Only users assigned to specific admin roles can invite** | Guests are added only through CR-004's process | Tenant-wide |
| Guests can invite | **No** | — | Tenant-wide |

### 2.5 Admin accounts
| Setting | Value | Why |
|---|---|---|
| Admin roles | Exactly as in [admin-accounts.csv](../00-company-profile/org/admin-accounts.csv): Owner Global Administrator; IT Technician User Administrator and Helpdesk Administrator | Least privilege (AC-6); assigned by `provision-users.ps1 -IncludeAdminAccounts` |
| Global Administrators | No more than the Owner's admin account plus the tenant's break-glass accounts | Fewer accounts that can do everything |
| Admin accounts | Separate from everyday accounts, no licence, no site access, MFA on | P-001 §5.6 |

### 2.6 Logging
| Setting | Value | Why |
|---|---|---|
| Entra sign-in and audit logs | On by default; **exported within 7 days** (Free keeps 7 days) | PR-004, AU-2 |
| Microsoft 365 unified audit log | **Verified on** once a Microsoft 365 licence exists (D-9) | The Cyber Home Lab lesson: confirm it returns records, don't assume |

---

## 3. When Licensed (Business Premium trial, D-9)
| Setting | Value |
|---|---|
| Conditional Access: require MFA for all users | Report-only first, then on; break-glass excluded |
| Conditional Access: block legacy authentication | Report-only first, then on |
| Conditional Access: phishing-resistant MFA for admins | Applies to `grp-bc-admins` |
| Conditional Access: block admin centre access for non-admins | Replaces the "friction" setting in §2.2 as the real control |
| Intune app protection for personal phones | Company data can't be copied out of Outlook and Teams (P-007 §7) |

Exported as JSON after every change ([PR-012](PR-012-backup-and-recovery.md)).

---

## 4. Applying and Checking
  1. **Build day:** the IT Technician applies §2 and takes a **screenshot of each setting page** (account names blurred) → `07-evidence-pack/artifacts/tenant/<date>-tenant-baseline/` (evidence E-28), redacted like every tenant export.
  2. **Every 6 months**, and after any licence change: compare the tenant with this page, fix drift, record the check in the maintenance log.
  3. Any change to a setting here goes through a change record (CM-3).

---

## 5. Current Status
Documented; applied on build day (2026-11-15). Tracked under **POAM-009** (CM-6).

---

## 6. Related Documents
  - [Access Management Policy (P-001)](../04-policies/P-001-access-control.md)
  - [Mobile Device and Personal Phone Policy (P-007)](../04-policies/P-007-mobile-devices.md)
  - [CR-001](../09-change-management/CR-001-google-workspace-to-microsoft-365.md) and [CR-004](../09-change-management/CR-004-vendor-guest-access.md)
  - [Tenant provisioning scripts](../tools/tenant/README.md)

### Sources (checked 2026-11-01)
  - [Microsoft Learn: Default user permissions](https://learn.microsoft.com/en-us/entra/fundamentals/users-default-permissions)
  - [Microsoft Learn: Configure how users consent to applications](https://learn.microsoft.com/en-gb/entra/identity/enterprise-apps/configure-user-consent)

---

*This document is a simulation for educational and portfolio purposes only.*
