# Backup and Recovery Procedure
Burn and Churn Coffee

---

## Document Control
**Owner:** Business Owner | **Performed by:** IT Technician | **Approved by:** Business Owner | **Effective:** 2026-11-01 | **Review:** Annually, and whenever a system is added or retired | **Version:** 1.0

---

## 1. Purpose
Make sure the shop can get its data and settings back after a mistake, a dead device, a vendor failure or ransomware. It carries out §8 of the [IT Operations Policy (P-006)](../04-policies/P-006-it-operations.md) and implements NIST SP 800-53 **CP-9 (System Backup)** and **CP-10 (System Recovery and Reconstitution)**. It supports PCI DSS **12.10.1**, which expects the incident response plan to cover business recovery and data backup.

---

## 2. Why Cloud Services Still Need Backups
Cloud vendors keep their own systems running and recover their own infrastructure. **The shop's data and settings are the shop's responsibility**, and Microsoft's shared-responsibility model says the customer always owns its data, accounts and identities. Built-in safety nets are not backups:
  - **SharePoint and OneDrive recycle bins** keep deleted items for **93 days in total**, then they're gone. Version history goes when the file does.
  - **Ransomware** on a synced laptop can encrypt files, and the encrypted copies sync to the cloud.
  - **A closed account** (for example, a vendor the shop leaves) takes its data with it, unless the data was exported first.

So the shop keeps **its own copy** of everything it couldn't easily recreate.

---

## 3. What Is Backed Up

| What | Lives in | How it's backed up | How often | Kept | Recovery target |
|---|---|---|---|---|---|
| **Firewall and access point settings** (FW-01, AP-01/02) | The devices | Export the configuration file | After every change, and in the monthly update window (PR-002) | Last 12 exports | Rebuild a failed device within 4 hours of having a replacement |
| **Staff accounts, groups and admin roles** | Microsoft Entra ID | **Rebuilt from the program's files:** `people.csv`, `admin-accounts.csv` and `tools/tenant/provision-users.ps1` recreate them | Whenever the roster changes (the files *are* the backup) | Git history | Same day |
| **Conditional Access policies** (once licensed) | Microsoft Entra ID | Export each policy as JSON | After every change | All versions | Same day |
| **Company documents, lists and the training tracker** | SharePoint and OneDrive (after CR-001) | Monthly export of the key libraries to the offline drives (§4); recycle bin and version history for day-to-day mistakes | Monthly | 12 months | Within one business day |
| **Bookkeeping workbook** (SYS-014) | SharePoint Finance library | Copy to the offline drives after month-end close | Monthly | 7 years, as financial records | Within one business day |
| **Toast menu, items, staff and sales reports** | Toast cloud (until CR-005) | Export reports and the menu | Monthly, and before the CR-005 cutover | Until CR-005 closes, then 7 years for sales | Toast restores its own service; exports cover the shop's records |
| **xtraCHEF item and supplier lists** | xtraCHEF (until CR-005) | Export | Monthly, and before the CR-005 cutover | Until moved to the SharePoint list | Within one business day |
| **Food-safety temperature log** | Temperature monitoring service (V-012) | Export the log | Monthly | 2 years | Within one week |
| **Payroll timesheets and exports** | SharePoint (shop side); Northwind keeps payroll records | Included in the monthly SharePoint export | Monthly | 7 years | Within one business day |
| **Password manager** | Bitwarden organization (SYS-015) | Encrypted organization export | Quarterly, and after major changes | Last 4 exports | Same day |
| **Camera footage** | Camera vendor's cloud (V-010) | **Not backed up.** Kept 30 days by the vendor; clips needed for an incident are exported under [PR-011](PR-011-connected-devices.md) §5 | — | 30 days | Not applicable |
| **Manager laptop and tablets** | The devices | **Not backed up as devices:** business files live in OneDrive after CR-001, and a failed device is rebuilt, not restored | — | — | New or rebuilt device within 2 business days |

Retention periods for financial and food-safety records are business decisions by the Owner, recorded here; they are not legal advice.

---

## 4. Offline Copies (the ransomware protection)
  - Two **encrypted USB drives** (BitLocker To Go), used in turn. One is kept in the store safe; the other goes home with the Owner, so a fire or theft can't take both.
  - Each month the IT Technician writes the month's exports (§3) to the drive in the store, checks the files open, then **disconnects it**. A drive that isn't connected can't be encrypted by ransomware.
  - The drives are swapped each month.
  - Drive encryption keys and the password-manager export password are stored in the password manager, and also in the Owner's password manager with the break-glass credentials (SYS-022, PR-009 §3a), so a lost shared vault doesn't lock away its own backup.
  - Before a vendor account is closed (Google under CR-001, Toast and xtraCHEF under CR-005), its data is exported to both drives.

**Option the Owner may choose later:** Microsoft 365 Backup, a paid pay-as-you-go service from Microsoft that keeps frequent restore points for SharePoint, OneDrive and Exchange (it needs an Azure subscription). For now, the monthly offline copy is the accepted approach.

---

## 5. Restore Testing (CP-10)
A backup isn't proven until something has been restored from it.

| Test | When |
|---|---|
| Restore one item from the offline drive, rotating through §3 (a SharePoint file, the bookkeeping workbook, a firewall configuration loaded onto the spare or a lab copy) | Every quarter |
| Full recovery walk-through, as part of the contingency tabletop ([PR-005](PR-005-contingency-plan.md) §8) | Every year |

Each backup and each test is recorded in the [backup log](../07-evidence-pack/artifacts/backup/backup-log.csv): date, what, where, result, who. A failed restore is fixed and re-tested, and noted in the POA&M review log.

---

## 6. Recovering After an Incident
  1. **Find a clean point.** For ransomware or account compromise, decide with the Owner which backup predates the incident ([IRP-005](../06-incident-playbooks/IRP-005-malware-ransomware.md)).
  2. **Fix the cause first**: remove the malware, reset accounts, patch. Then restore, so the restored data isn't re-infected.
  3. **Restore** in priority order: payments (Toast offline or cash keep the counter open meanwhile), staff sign-in, documents and the bookkeeping workbook, everything else.
  4. **Check** that restored data is complete and opens, and record what was lost between the backup and the incident.
  5. **Record** the recovery in the incident log and the backup log.

---

## 7. Current Status (2026-11-01)
  - **No backups exist.** Vertex IT Support never exported the network settings, and the shop has relied on its cloud vendors alone (the earlier wording of PR-005 §7).
  - Backups start with the IT Technician: firewall and access point settings are exported at the Vertex handover ([PR-008](PR-008-it-administration.md) §7); Google Workspace and QuickBooks data are exported before they close (CR-001); the first monthly offline copy is due in **December 2026**; the first restore test by **2027-02-28**.
  - Tracked under **POAM-029**.

---

## 8. Related Documents
  - [IT Operations Policy (P-006)](../04-policies/P-006-it-operations.md)
  - [Contingency and Outage Plan (PR-005)](PR-005-contingency-plan.md)
  - [Malware and Ransomware Playbook (IRP-005)](../06-incident-playbooks/IRP-005-malware-ransomware.md)
  - [Shared Credential Management Procedure (PR-009)](PR-009-credential-vault.md)
  - [Tenant provisioning scripts](../tools/tenant/README.md)

### Sources (checked 2026-11-01)
  - [Microsoft Learn: Restore deleted data in SharePoint Online](https://learn.microsoft.com/training/modules/explore-archiving-records-management/7-restore-deleted-data-sharepoint-online) (93-day retention)
  - [Microsoft 365 Backup](https://www.microsoft.com/microsoft-365/microsoft-365-backup) (pay-as-you-go service)

---

*This document is a simulation for educational and portfolio purposes only.*
