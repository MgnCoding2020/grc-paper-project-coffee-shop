# Tenant Provisioning

Scripts that build Burn and Churn Coffee's Microsoft 365 tenant from the program's canonical org data, so the tenant can't drift from the documents.

## provision-users.ps1

Creates every non-terminated person in [people.csv](../../00-company-profile/org/people.csv) as an Entra ID user, creates the `grp-bc-*` security groups, and adds each person to their groups. Safe to re-run: existing users, groups and memberships are skipped.

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
```

### What it writes

Both files go to the git-ignored `_raw/` folder:

| File | Contents | What to do with it |
|---|---|---|
| `initial-passwords-<timestamp>.csv` | Temporary passwords (changed at first sign-in) | Hand out, then delete |
| `provisioning-log-<timestamp>.csv` | Every create, skip and group add, using the fictional domain only | Review, then copy into `07-evidence-pack/` as account-management evidence (AC-2) |

### Deliberately not automated

Admin roles, `adm-` accounts, break-glass accounts, licences and MFA are set up by hand, so each privileged change is a deliberate, reviewed step (least privilege, AC-6).

---

*This document is a simulation for educational and portfolio purposes only.*
