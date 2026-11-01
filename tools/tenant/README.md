# Tenant Provisioning

Scripts that build Burn and Churn Coffee's Microsoft 365 tenant from the program's canonical org data, so the tenant can't drift from the documents.

## provision-users.ps1

Creates every non-terminated person in [people.csv](../../00-company-profile/org/people.csv) as an Entra ID user, creates the `grp-bc-*` security groups, and adds each person to their groups. Safe to re-run: existing users, groups, memberships, roles and licences are skipped.

Each user gets their job title, department ("Burn and Churn Coffee") and **employee ID** (`EMP-###` from `person_id`). People sign in with their user principal name (`first.last@...`), not the employee ID; the ID ties the directory to HR records. Each person gets a random 16-character temporary password and must change it at first sign-in. Passwords built from personal details (name, employee ID) are deliberately not used, because anyone who knows the pattern could guess them.

### One-time setup

1. Copy [.env.example](../../.env.example) to `.env` at the hub root and fill in the tenant ID and domain. `.env` is git-ignored.
2. Install the Microsoft Graph PowerShell module:
   ```powershell
   Install-Module Microsoft.Graph -Scope CurrentUser
   ```
3. Sign in as an account that can create users and groups (User Administrator plus Groups Administrator, or Global Administrator).

### Run

```powershell
# Preview: no connection, nothing changes
.\tools\tenant\provision-users.ps1 -DryRun

# Build (on the CR-001 build day)
.\tools\tenant\provision-users.ps1

# Also the admin accounts and their roles
.\tools\tenant\provision-users.ps1 -IncludeAdminAccounts

# Also licences, once a subscription or trial is active (set BC_LICENSE_SKU in .env first)
.\tools\tenant\provision-users.ps1 -IncludeAdminAccounts -AssignLicenses
```

| Switch | What it adds | Extra permission |
|---|---|---|
| `-IncludeAdminAccounts` | The accounts in [admin-accounts.csv](../../00-company-profile/org/admin-accounts.csv) (`adm-olivia.carter`, `adm-riley.morgan`), added to `grp-bc-admins`, with exactly the directory roles listed there. No licence, no site access. **Turn on MFA for them straight away** | `RoleManagement.ReadWrite.Directory` |
| `-AssignLicenses` | The licence named by `BC_LICENSE_SKU` in `.env` for every provisioned person (not admin accounts or guests). The script shows how many licences are free before assigning. List your tenant's licence names with `Get-MgSubscribedSku \| Select-Object SkuPartNumber` | `Organization.Read.All` |

### What it writes

Both files go to the git-ignored `_raw/` folder:

| File | Contents | What to do with it |
|---|---|---|
| `initial-passwords-<timestamp>.csv` | Temporary passwords (changed at first sign-in) | Hand out, then delete |
| `provisioning-log-<timestamp>.csv` | Every create, skip and group add, using the fictional domain only | Review, then copy into `07-evidence-pack/` as account-management evidence (AC-2) |

### Vendor guests (CR-004)

Vendor contacts in [vendor-contacts.csv](../../00-company-profile/org/vendor-contacts.csv) are invited as B2B guests only when their status is `Approved` or `Active`; `Planned` and `Removed` contacts are skipped. Each contact's real email address is read from `.env` (the key in its `env_email_key` column), and the run log names guests by contact ID only. Inviting guests needs the `User.Invite.All` permission.

### Deliberately not automated

- **Break-glass accounts:** tenant-wide, so they're documented for whatever emergency accounts the shared tenant actually has, not created per company.
- **MFA:** each person registers at first sign-in; per-user MFA (Entra ID Free) or Conditional Access (with Entra ID P1) is switched on in the portal.
- **Admin roles beyond `admin-accounts.csv`:** only through a change record (PR-008).

## redact_export.py

Turns a raw export (sign-in log, audit log, MFA status, group members) into a copy that's safe to commit. Run it from the hub root:

```powershell
python tools/tenant/redact_export.py _raw/signins.csv 07-evidence-pack/artifacts/tenant/2026-11-15-signins.csv
```

| Replaced | With |
|---|---|
| The real tenant domain (any `*.onmicrosoft.com`) | `burnandchurncoffee.com` |
| Real email addresses kept in `.env` (any key containing `EMAIL`) | A readable stand-in, e.g. `vendor.guest.vc001@example.com` |
| Tenant ID and every other GUID | `<guid>` |
| IPv4 and IPv6 addresses | `<ip>` |
| Access tokens | `<token>` |
| Any other email outside the fictional domain | `<email>` |

It rescans its own output and refuses to write the file if anything tenant-shaped is left. Then run the consistency checker before committing (check 8 scans for the same things).

**Why the domains differ:** the tenant's only domain is its free default `*.onmicrosoft.com` domain, and Burn and Churn never buys a domain. Account names match exactly (`olivia.carter@...`); only the part after the `@` changes, in one substitution.

---

*This document is a simulation for educational and portfolio purposes only.*
