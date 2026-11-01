# Live Tenant Evidence

Redacted exports from the real Microsoft Entra tenant where Burn and Churn Coffee's accounts are built (decision D-4). Every file here is produced the same way:

1. Export from the portal or a script into the git-ignored `_raw/` folder.
2. Redact with [`tools/tenant/redact_export.py`](../../../tools/tenant/redact_export.py): fictional domain, no GUIDs, IP addresses, tokens or real email addresses.
3. Run the consistency checker, then commit here with the date in the file name, and add a `Lab-verified <date>` row to the [evidence index](../../evidence-index.md).

Nothing is in this folder yet. The table lists each file the builds will produce, so each one has a place before it exists.

---

## Planned Files

| File (date = the day it's captured) | Comes from | Control(s) | Evidence | When |
|---|---|---|---|---|
| `<date>-provisioning-log.csv` | `provision-users.ps1` run log (already uses the fictional domain) | AC-2 | E-01 | Build day (CR-001, CR-003) |
| `<date>-users-and-groups.csv` | Entra admin centre: users export, plus `grp-bc-*` group members | AC-2, AC-6 | E-01, E-03 | Build day |
| `<date>-admin-role-assignments.png` | Entra admin centre: roles and administrators (screenshot, emails blurred) | AC-6 | E-03 | Build day |
| `<date>-mfa-status.csv` | Per-user MFA page (Entra ID Free) | IA-2 | E-02 | Build day |
| `<date>-signins.csv` | Sign-in logs download (7-day retention on Free: same day) | IA-2, AU-2 | E-02 | Build day |
| `<date>-audit-log.csv` | Audit logs download | AU-2, AU-6 | New row when captured | Build day |
| `<date>-conditional-access.json` | Conditional Access policy export (report-only, then on) | IA-2, AC-2 | E-02 | Business Premium trial (D-9) |
| `<date>-guest-lifecycle.md` | Invite, sign-in, file access, denied access, expiry, removal (CR-004) | AC-2, AC-6, PS-4 | — | After CR-004's preconditions |

Password manager evidence goes in [`../credentials/`](../credentials/) (E-19, PR-009 §6).

---

*This document is a simulation for educational and portfolio purposes only.*
