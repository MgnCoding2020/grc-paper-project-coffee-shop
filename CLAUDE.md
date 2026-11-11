# Burn and Churn Coffee: one company, one program, every repo telling the same story

> **Where this file goes.** The root of `MgnCoding2020/grc-paper-project-coffee-shop`, as `CLAUDE.md`. That repo is the **program hub**; this file also governs changes Claude Code makes in the companion repos listed in section 2. The repos are public, and this file can be too: it contains nothing private.
>
> **Written 2026-10-29** from a full read of all five repos at these commits: `grc-paper-project-coffee-shop` `e4e0646`, `IAM-Access-Review-Lab` `a965fe0`, `Vendor-Risk-Assessment-Lab` `50b4679`, `workspace` `fe52f01`, `cyber-homelab` `e5f003c`. Every finding in section 3 cites the file it came from. Re-verify anything older than a few weeks before acting on it (§12, rule 8).
>
> **Revised 2026-10-29 (rev 2)** with Michael's decisions: real Entra ID accounts in his own tenant for live evidence; `workspace` and `cyber-homelab` are skill sources, not companion repos; QuickBooks replaced by an Excel workbook in SharePoint; Toast and Northwind stay paper-only; secrets rule added. See the revision history at the end.
>
> **Revised 2026-10-29 (rev 3):** headcount fixed at 20 store staff; IT brought in-house with a part-time IT Technician (Riley Morgan) and Vertex offboarded (CR-003); Toast PIN rules (D-2); cutover 2026-11-15 (D-3); Burn and Churn groups prefixed `grp-bc-` in the shared tenant; network segmentation target design (§5.4, AL-19).

---

## 1. Mission and end state

**Burn and Churn Coffee** is a fictional, single-location coffee shop. Michael has built its security program (this repo) and two operational labs around it (access review, vendor risk). They were written at different times and drifted: different staff, different systems, half-linked repos.

**The end state:** every repo describes **the same company**, with:
- **The same people:** one roster with named staff, roles and accounts, used everywhere.
- **The same systems:** Microsoft 365 for productivity and identity, Toast POS in-store, and later an online ordering site.
- **The same vendors:** one inventory with one ID per vendor, used everywhere.
- **The same identifiers:** risks, controls, findings, POA&M items, change records and evidence, with no collisions.
- **Explicit links:** every repo says what it is part of and links both ways.
- **A documented history:** the move from Google Workspace to Microsoft 365 is a **dated, controlled change** (`CR-001`), not a silent rewrite.

**Why it matters (for Michael's goal):** a hiring manager can follow one finding from the risk register → control → evidence → access review → POA&M → remediation, across repos, and it all lines up. That's what "audit-ready" means, shown rather than claimed. Consistency across artifacts is itself the GRC skill being demonstrated.

**Framework baseline (unchanged):** NIST SP 800-53 Rev. 5 controls, crosswalked to PCI DSS v4.0.1, with NIST RMF steps used to bring new systems into the program (section 6).

---

## 2. The repo ecosystem

| Repo | Role | Audience takeaway |
|---|---|---|
| **`grc-paper-project-coffee-shop`** (this repo) | **Program hub and system of record.** Company profile, canonical org data, policies, procedures, risk register, control matrix, crosswalk, POA&M, change records, evidence index | "He can run a security program." |
| **`IAM-Access-Review-Lab`** | Operational: quarterly access reviews (AC-2, AC-6). Q1 2026 (pre-migration) plus Q4 2026 (post-migration, in Entra ID) | "He can execute and evidence an access certification." |
| **`Vendor-Risk-Assessment-Lab`** | Operational: third-party assessments (SA-9). Eight assessments (V-001, V-002, V-003, V-008 to V-012) and the V-004 Vertex offboarding record (CR-003); every vendor that needs an assessment has one | "He can assess a vendor end to end." |
| **Microsoft 365 tenant** (not a repo) | **Live evidence source.** Burn and Churn's staff accounts, groups, Conditional Access, MFA, audit log and SharePoint intranet are built in Michael's own tenant (D-4). Redacted exports are committed to the hub as `Lab-verified` evidence | "He can build and run M365 for a real-shaped business, and prove it." |
| **[`burn-and-churn-website`](https://github.com/MgnCoding2020/burn-and-churn-website)** (active, CR-002) | The online ordering website, staff portal and counter register: `CR-002` (approved 2026-11-05), with its own plan. Public site live with fictional content; staff sign-in next. Where the technologies connect: Entra sign-in, least privilege, Stripe test mode | "He can build a system to the controls." |

**Skill sources, not part of the program:** `workspace` (SharePoint-shaped intranet engine) and `cyber-homelab` (Entra, Conditional Access, audit log, eDiscovery labs) are where Michael practised the techniques this program now applies. They are not linked as companions, not changed by this plan, and their case studies stay about Michael's own labs. Lessons carried over are credited in prose where useful (e.g. "the break-glass exclusion pattern from the Cyber Home Lab").

### Link rules
- **Hub → each companion repo:** the hub README has a "Program repositories" table linking all companion repos, and the evidence index (§8) links specific artifacts.
- **Each companion → hub:** every companion README opens with: *"Part of the Burn and Churn Coffee security program: [program hub](https://github.com/MgnCoding2020/grc-paper-project-coffee-shop). Company, people, systems and vendors are defined there."*
- **Companion ↔ companion:** only where an artifact actually depends on another, e.g. the Q4 access review cites the Microsoft vendor assessment for the vendor-admin decision.

```
                    ┌──────────────────────────────────────┐
                    │  grc-paper-project-coffee-shop (hub)  │
                    │  org data · policies · risk · controls│
                    │  POA&M · change records · evidence idx│
                    └──┬──────────────┬──────────────┬─────┘
          access       │   vendor     │   live       │   online ordering (later)
          reviews      │   assessments│   evidence   │
     ┌─────────────────▼─┐ ┌──────────▼────────┐ ┌───▼────────────┐ ┌────────────────┐
     │ IAM-Access-Review │ │ Vendor-Risk-      │ │ M365 tenant     │ │ burn-and-churn │
     │ -Lab              │ │ Assessment-Lab    │ │ (Entra, SPO)    │ │ (CR-002)       │
     └───────────────────┘ └───────────────────┘ └────────────────┘ └────────────────┘
          findings ─────────────► roll up to hub POA&M ◄──────────── findings
```

---

## 3. Audit findings (2026-10-29)

These are the alignment problems found in the current repos. IDs are `AL-##` (alignment), tracked here until fixed. **Fixed in phase** refers to section 9.

| ID | Repo / file | What's wrong | Fix | Phase |
|---|---|---|---|---|
| AL-13 | IAM matrix vs hub `P-001` §5.7 | Policy says vendor access is "assigned to named individuals (no generic vendor accounts)", yet the matrix has generic **"Vertex IT Support"** and **"NorthPeak Systems"** accounts, and the review didn't flag it | Leave Q1 as recorded (it's history), but **this is a missed finding**: raise it in the Q4 review as a new finding, a strong "what the first review missed" story. **Rev 3:** the generic Vertex account is removed during the CR-003 handover, so Q4 records the finding *and* its closure evidence | P4 |
| AL-14 | Hub, everywhere | Google Workspace is the productivity suite in 23 files (46 mentions) | `CR-001` migration to Microsoft 365 (section 7). Dated evidence stays; current-state documents change | P3 |
| AL-15 | `workspace` `js/app.js` | `config/sites.json` is fetched from a fixed path, so a second organization pack can't supply its own sites | **Withdrawn (rev 2):** `workspace` is no longer a companion repo; the intranet is built directly in the tenant (§7.4) | — |


### Resolved

| ID | What was wrong | Fixed by | Date |
|---|---|---|---|
| AL-09 | No links between the hub and the IAM lab | Hub PR #5 (Program Repositories table), IAM PR #9 and VRA PR #3 (standard README opener) | 2026-10-30 |
| AL-11 | Both labs numbered findings `F-0x` | Hub PR #5 (`org/identifiers.md`, global IDs `IAM:F-###`, `VRA-V###:F-##`), IAM PR #9 and VRA PR #3 (cross-reference notes) | 2026-10-30 |
| AL-01 | Hub evidence used generic accounts (`manager@`, `barista1@`, `barista2@`) | Hub PR 2c: mapped to Daniel Lopez, Ethan Brooks, Aiden Scott; logged in `CORRECTIONS.md` | 2026-10-30 |
| AL-02 | Training log names existed nowhere | Hub PR 2c: rebuilt from the roster (20 active staff) | 2026-10-30 |
| AL-03 | Profile said about 19 staff | Hub PR 2c: 20 active store staff | 2026-10-30 |
| AL-04 | Hub evidence made the Store Manager a Google Workspace admin | Hub PR 2c: corrected to match the IAM matrix, with a logged correction | 2026-10-30 |
| AL-05 | Vendor inventory listed only V-001 and V-002 | Hub PR 2c: V-001 to V-008, matching `vendors.csv` | 2026-10-30 |
| AL-06 | Assets missing for xtraCHEF, QuickBooks, Northwind, vendor admins | Hub PR 2c: added (plus HW-003 manager laptop, planned M365 systems) | 2026-10-30 |
| AL-07 | Stripe in access-review scope | Hub PR 2c: removed; scope matches the Q1 review | 2026-10-30 |
| AL-08 | Owners "IT Admin" / "System Administrator" didn't exist | Hub PR 2c: Vertex IT Support, then the IT Technician from CR-003 | 2026-10-30 |
| AL-10 | IAM findings never rolled up | Hub PR 2c: POAM-014 (AC-2, AC-6) | 2026-10-30 |
| AL-16 | AC-2 and AC-6 marked Implemented despite open findings | Hub PR 2c: Partially Implemented in matrix, crosswalk and README; R-06 residual raised | 2026-10-30 |
| AL-19 | SC-7 marked Implemented; evidence showed no segmentation | Hub PR 2c: Partially Implemented, POAM-015, architecture text corrected, R-04 residual raised | 2026-10-30 |
| AL-21 | 6 broken links in procedures and data classification | Hub PR 2c: link targets fixed | 2026-10-30 |
| AL-12 | IAM matrix MFA cells contradicted F-004 and the hub export | IAM PR #10: Ethan Brooks's Google MFA corrected; Toast PIN logins documented as outside MFA scope (D-2) | 2026-10-30 |
| AL-17 | F-005 (Windows lab VM) looked like a company system | IAM PR #10: labelled as a lab demonstration outside the system boundary | 2026-10-30 |
| AL-18 | Generic hub accounts hid conflicts with the IAM matrix | Hub PR #8 (mapping) and IAM PR #10 (Aiden Scott's MFA cell) | 2026-10-30 |
| AL-20 | Vendor report kept `YYYY-MM-DD` and `[Name / Role]` placeholders | VRA PR #4: 2026-06-23, Olivia Carter (Owner); checker now flags unfilled placeholders | 2026-10-30 |
| AL-22 | Northwind (V-002) inherent risk used a 4-factor qualitative scale, not the program's 6-factor numeric worksheet | **Accepted:** the dated Northwind score stays as recorded; V-003 onward use the worksheet, and the V-003 score notes the difference (VRA PR #5) | 2026-10-30 |
| AL-23 | IAM Q1 record: summary lacked date and reviewer, said 14 employees; checklist unticked; remediation 7 months overdue with no updates | IAM PR #11: gaps filled from the program record, missing sign-off recorded as a gap, overdue status check with closure plans | 2026-10-30 |
| AL-24 | Northwind listed as Active although its pre-go-live conditions (F-02, F-03) were open | Decision: not live. VRA PR #6 (status check) and this hub PR (status: onboarding pending) | 2026-10-30 |
| AL-25 | POA&M claimed bi-weekly review; none was recorded, so stalls went unnoticed | Hub PR: POA&M review log, new control CA-5 with POAM-019, R-12, E-18 | 2026-10-30 |
| AL-26 | P-001 and P-002 referenced documents that didn't exist (network policy, onboarding procedure, incident plan) | Network Security Policy P-005 written; P-001 and P-002 v1.2 point to P-005, PR-001, P-003 and the playbooks | 2026-10-30 |
| AL-27 | Hub story review: PR-001 removal deadline ("last working day") contradicted P-001 §5.4 (24 hours), and POAM-016 misquoted it as "same day"; PR-003 lacked the sign-off the IAM copy requires; IRP-003 had no tamper steps although P-004 treats tampering as an incident; IRP-003/004 lacked document control; assessment scope omitted xtraCHEF and QuickBooks and contradicted the RACI | All aligned to the policies and RACI, with revision history on each document | 2026-10-30 |
| AL-28 | Vendor lab README said nothing awaited assessment although V-013 and V-014 did | VRA PR #17 (list); VRA PR #18 (Cloudflare assessed; Stripe remains) | 2026-11-08 |
| AL-29 | IAM review scope lacked the website's app roles and an "Assignment required" enforcement check | IAM PR #15 | 2026-11-07 |
| AL-30 | V-014 Cloudflare described as holding staff data "later" and its overdue assessment as merely planned | Hub PR #51 (data, POAM-036); VRA PR #18 (assessment, 2026-11-08) | 2026-11-08 |

**Already fixed** (confirmed in git history, no action): the duplicate evidence scripts (hub PR #1, merged); the control count of 15 across 11 families (hub PRs #2 and #3).

---

## 4. Canonical organization model (single source of truth)

All company facts live in **`00-company-profile/org/`** in the hub, as small machine-readable files. Every other document and repo **uses these values**, and the consistency checker (§10) enforces it.

```
00-company-profile/org/
  people.csv        the staff roster
  roles.md          roles, responsibilities, RACI
  systems.csv       every system in scope, with its boundary
  vendors.csv       every third party, with a stable vendor ID
  identifiers.md    ID conventions and the registry of prefixes
  timeline.md       dated program history (reviews, assessments, changes)
```

### 4.1 Company facts
- **Burn and Churn Coffee**, single retail location (city fictional or unspecified; don't use a real address).
- Email domain in documents: `burnandchurncoffee.com`. **Fictional, not owned:** never hyperlink it or use it as a real `mailto:`. The live tenant (D-4) uses its own `*.onmicrosoft.com` domain. The real domain, tenant ID and Michael's own admin UPN are kept in a local `.env`, never committed; committed evidence shows `burnandchurncoffee.com` UPNs, with the substitution stated once in the evidence index. **No domain is bought** (decided 2026-11-01): the tenant keeps its free default domain, account names match exactly (`olivia.carter@…`) and only the part after the `@` differs, replaced by `tools/tenant/redact_export.py`; the website (CR-002) runs on Cloudflare's free tier with its default subdomain.

### 4.2 People and roles

`people.csv` columns: `person_id, display_name, role, employment_status, start_date, end_date, upn, groups, notes`.

- **The cast comes from the IAM lab's `user-access-matrix.csv`**, the most detailed source:
  - Owner: Olivia Carter
  - Store Manager: Daniel Lopez
  - Shift Leaders: Mia Chen, Marcus Hill, Sofia Patel
  - Baristas: Ethan Brooks, Ava Reed, Noah Bennett, Lily Foster, James Cooper, Chloe Murphy, Logan Price, Grace Kelly, Henry Adams, Ella Turner, Jack Rivera, Nora Bailey, Leo Collins, Zoe Mitchell, Owen Parker
  - Terminated: Aiden Scott
  - **IT Technician (part-time, in-house, from CR-003): Riley Morgan.** Hired to run the M365 migration and own IT from then on. About 10 hours a week; the Owner is the backup administrator (PR-008). Not counted in the 20 store staff
- **Headcount (D-1):** 20 active store staff (1 Owner, 1 Store Manager, 3 Shift Leaders, 15 Baristas) plus the part-time IT Technician. The company profile states it exactly that way.
- **UPN pattern:** `first.last@burnandchurncoffee.com` (e.g. `olivia.carter@…`). Privileged work uses a **separate admin account** (`adm-first.last@…`); only the IT Technician and the Owner have one.
- **Personnel controls for the IT Technician:** screening documented (PS-3), signed access agreement and privileged-user rules (PS-6), admin account separate from the daily account (AC-6(2)).
- **Separation of duties:** the IT Technician creates and changes accounts but **never certifies their own access**. The Owner and Store Manager sign the quarterly review; the IT Technician only exports the data.
- **Vendor access** (any future vendor) is assigned to named individuals, as P-001 requires. Vertex's generic account is removed in the CR-003 handover.
- **Break-glass:** two cloud-only emergency admin accounts (`bg-admin-01`, `bg-admin-02`), excluded from Conditional Access, monitored, credentials sealed with the Owner. This is standard Microsoft guidance, and it gives the Cyber Home Lab's "break-glass exclusion" lesson a home here. Break-glass is tenant-wide: in the shared tenant, document whichever emergency accounts the tenant actually has.
- **Toast PINs (D-2):** every store employee has a personal Toast PIN, because everyone is trained on the register. Only one employee is signed in to a terminal at a time, and that employee is accountable for every action taken while signed in. Employees sign out when they leave the register and never use another employee's PIN. PINs are not MFA: Toast cashier logins are **outside MFA scope by design**, with unique PINs, sign-out rules and an idle auto-logout as compensating controls (exact PCI DSS requirement numbers verified before they're written into P-004).

**RACI** (`roles.md`):

| Activity | Owner | Store Manager | Shift Leaders | IT Technician | Baristas |
|---|---|---|---|---|---|
| Approve access requests | **A** | R (store systems) | C | I | — |
| Create, change and remove accounts | A | C | — | **R** | — |
| Quarterly access review | **A** | R (reviewer, store systems) | C | C (evidence export only) | — |
| Vendor risk management | **A/R** | C | — | C | — |
| Incident response | **A** | R (store) | R (on shift) | R (technical) | I (report) |
| Network and firewall administration | A | I | — | **R** | — |
| Security training | A | **R** | R | C | Participate |
| Policy ownership and approval | **A/R** | C | — | C | I |

"IT Admin" and "System Administrator" in existing documents become **Vertex IT Support (MSP)** for records dated before 2026-11-15 and the **IT Technician** after it, with the Owner accountable throughout.

### 4.3 Systems

`systems.csv` columns: `system_id, name, category, vendor_id, data_classification, boundary, evidence_mode, in_scope_since, retired_on, notes`.

`evidence_mode` says how a system can be evidenced: **Live** (built in Michael's tenant; screenshots and exports possible), **Simulation** (no access exists; documented design only, never claimed as live), **Test** (sandbox or test mode; no real payments or personal data).

| ID | System | Mode | Notes |
|---|---|---|---|
| SYS-001 | Toast POS | Simulation | In-store payments and orders (card-present). No public sandbox, so no live evidence; no real card data anywhere in the program. **Retired by CR-005** when the website's register goes live (D-11) |
| SYS-002 | Google Workspace | Simulation | **Retired** by CR-001 (`retired_on` set); kept for history |
| SYS-003 | Google Admin Console | Simulation | **Retired** with SYS-002 |
| SYS-004 | xtraCHEF | Simulation | Inventory and invoices (by Toast). **Retired by CR-005**; inventory moves to a SharePoint list |
| SYS-005 | QuickBooks Online | Simulation | **Retired** by CR-001: bookkeeping moves to SYS-014. Kept for the Q1 history |
| SYS-006 | Northwind Payroll Services | Simulation | Payroll and HR (V-002). The shop's side (timesheets, payroll export) is Live in SYS-012/014 |
| SYS-007 | Store network | Simulation | Router, firewall, staff and guest Wi-Fi (existing NET-00x assets) |
| SYS-010 | Microsoft Entra ID | Live | Identity, from CR-001 |
| SYS-011 | Exchange Online | Live | Email, from CR-001 (licence-dependent) |
| SYS-012 | SharePoint Online + Teams | Planned → Live | Files, intranet lists and libraries, chat, from CR-001. Live once SharePoint is available with the Business Premium trial (D-8, D-9) |
| SYS-013 | Microsoft Intune + Defender for Business | Simulation unless licensed | Device management and endpoint protection, from CR-001 |
| SYS-014 | Bookkeeping workbook (Excel for the web, in SharePoint) | Planned → Live | Sales, expenses and payroll reconciliation in a restricted Finance library, from CR-001. Permissions, versioning and audit-log entries are the live evidence |
| SYS-015 | Password manager (Bitwarden organization) | Planned → Live | Shared admin credentials only (PR-009). Live once Michael's lab test (test entries only) is recorded |
| SYS-016 | Camera system (cloud recording) | Simulation | Two cameras; footage DATA-005, 30-day retention; never pointed at the keypad (PR-011) |
| SYS-017 | Espresso machine service portal | Simulation | Vendor remote diagnostics (MA-4) |
| SYS-018 | Temperature monitoring service | Simulation | Food-safety temperature log |
| SYS-020 | Online ordering website | Test | **CR-002** (approved 2026-11-05); public site live; staff sign-in next |
| SYS-021 | Stripe (Checkout and Terminal) | Test | CR-002 and CR-005; test mode with the simulated reader; planned |
| SYS-022 | Owner's password manager (Google Password Manager) | Live | Owner-held credentials only: break-glass, admin recovery codes, backup-drive keys (PR-009 §3a). EXC-009; V-015 assessment due 2026-11-25 (POAM-038) |

Keep the existing `SYS-`, `HW-`, `NET-`, `DATA-` and `PER-` asset IDs where they already exist; renumber only where needed, and record the old ID in `notes`.

### 4.4 Vendors

`vendors.csv` columns: `vendor_id, name, service, data_accessed, cardholder_data, inherent_tier, assessment_status, last_assessed, assessment_ref, owner, status`.

| ID | Vendor | Status |
|---|---|---|
| V-001 | Toast, Inc. (POS, and xtraCHEF) | Active; High; assessed 2026-10-30 (continue with conditions); **exit approved under CR-005**, offboarded at cutover |
| V-002 | Northwind Payroll Services | High; **assessed 2026-06-23** (vendor lab); **onboarding pending** until its pre-go-live conditions close (AL-24) |
| V-003 | Microsoft (Microsoft 365) | Assessed 2026-10-30 (High, approve with conditions); Active from CR-001 |
| V-004 | Vertex IT Support (MSP) | **Offboarded** by CR-003 (IT brought in-house) after a handover; access removal and knowledge-transfer sign-off are the exit evidence (offboarding record in P5) |
| V-005 | NorthPeak Systems | **Offboarded**; access removal is IAM F-003 |
| V-006 | Intuit (QuickBooks Online) | **Offboarded** by CR-001 (replaced by SYS-014); data export and subscription cancellation are CR-001 exit steps |
| V-007 | Google (Workspace) | **Offboarded** by CR-001; data-deletion confirmation is a CR-001 exit step |
| V-008 | Internet service provider (unnamed) | Active; provider-managed router; assessed 2026-11-02, Moderate, continue with conditions |
| V-009 | Bitwarden, Inc. (password manager) | Planned with CR-003; Free organization plan, two members (Owner, IT Technician); assessed 2026-11-02, Moderate, approve with conditions |
| V-010 | Cloud camera service (unnamed) | Active; assessed 2026-11-02, Moderate, continue with conditions |
| V-011 | Espresso machine service company (unnamed) | Active; remote access to the machine; assessed 2026-11-01, Moderate, continue with conditions |
| V-012 | Temperature monitoring service (unnamed) | Active; assessed 2026-11-02, Moderate, continue with conditions |
| V-013 | Stripe, Inc. | **Planned** (CR-002, CR-005); assessment not started (before payments go live) |
| V-014 | Cloudflare, Inc. | **Active** (CR-002, hosts the test website); assessment not started |
| V-015 | Google LLC (Google Password Manager) | **Active** since 2026-11-11 (the Owner's password manager, SYS-022); High; assessment due 2026-11-25 (POAM-038) |
| Next free | V-016: the AI provider (T11) | Get the next free `V-###` when added |

Existing IDs V-001 and V-002 **do not change**, because the vendor lab references them.

### 4.5 Identifier conventions

| Kind | Format | Where it lives |
|---|---|---|
| Risk | `R-##` | Hub risk register |
| Control | NIST 800-53 ID (`AC-2`, `AC-2(7)`) | Hub control matrix |
| Evidence | `E-##` | Hub evidence matrix and index |
| POA&M item | `POAM-###` | Hub POA&M only |
| Change record | `CR-###` | Hub `09-change-management/` |
| Incident | `INC-###` | Hub incident log (renumber the current "Incident 001/002") |
| Lab finding | Local `F-###`, referenced globally as `IAM:F-001`, `IAM-Q4:F-001`, `VRA-V002:F-01` | Each lab; the hub POA&M uses the global form |
| Alignment item | `AL-##` | This file only |

**Rule:** IDs are never reused or renumbered once published. Retired items are marked retired, not deleted.

---

## 5. Target architecture (after CR-001)

### 5.1 Systems and boundaries

```
┌─────────────────────────── Microsoft 365 tenant (Burn and Churn) ───────────────────────────┐
│ Entra ID: users, groups, Conditional Access, app roles · Exchange Online · Teams           │
│ SharePoint Online: intranet ─ Operations · People · Finance (Excel bookkeeping, SYS-014) ·  │
│                    Security & Compliance sites                                              │
│ Intune + Defender for Business: manager laptop, store tablets (licence-dependent)          │
└───────────────┬─────────────────────────────────────────────────────────────────────────────┘
                │ SSO (where supported)                       ┌──────────────────────────────┐
   ┌────────────▼───────────┐   ┌─────────────────────────┐   │ Store network (SYS-007)      │
   │ Toast POS + xtraCHEF   │   │ Northwind Payroll       │   │ staff Wi-Fi · guest Wi-Fi ·  │
   │ (card-present; vendor- │   │ (SaaS, own logins;      │   │ POS segment (SC-7)           │
   │ managed PCI scope)     │   │ payroll export from SPO)│   └──────────────────────────────┘
   └────────────────────────┘   └─────────────────────────┘
        Later, CR-002: online ordering site ── Stripe Checkout (test mode) ── customer identity
```

### 5.2 Identity design (Entra ID)

- **Groups** (security groups, `grp-bc-` prefix so they never mix with Michael's lab objects in the shared tenant): `grp-bc-all-staff` (every Burn and Churn account, the scope for Conditional Access), `grp-bc-owners`, `grp-bc-managers`, `grp-bc-shift-leads`, `grp-bc-baristas`, `grp-bc-it`, `grp-bc-vendors` (vendor guests, CR-004), `grp-bc-admins` (the `adm-` accounts only: the scope for admin sign-in rules, never granted site access), `grp-bc-break-glass`. Every Burn and Churn user also has department = "Burn and Churn Coffee". Every access decision is granted to a group, never to a person directly (the group-driven role pattern Michael verified live in `workspace`).
- **Admin roles, least privilege:**
  - Owner: Global Administrator. PIM (eligible, not standing, admin) needs Entra ID P2, which the tenant doesn't have, so standing admin is a **documented gap with compensating controls**: separate admin account, phishing-resistant MFA, break-glass, alerting on role assignments, and admin roles checked in every quarterly review. Recorded as an accepted risk in the risk register.
  - IT Technician: `adm-riley.morgan` holds only the roles the job needs (User Administrator, Helpdesk Administrator, plus others only when a task requires them, recorded in the change). The daily `riley.morgan` account has no admin roles.
  - Baristas: no admin roles.
- **Live tenant vs paper.** What Michael's tenant actually has is recorded separately from what the fictional company would buy. Any control that depends on a missing licence stays `Simulation` and says why.
- **The tenant today (checked against Microsoft Learn, 2026-10-30): Microsoft Entra ID Free.** Tenant ID and domain live in the hub's `.env` only.
  - **Works on Free:** users and groups, scripted creation, built-in admin roles and separate admin accounts, per-user MFA, and sign-in and audit logs (7 days' retention, downloadable as CSV or JSON from the portal).
  - **Needs P1:** Conditional Access, dynamic groups, admin roles scoped to administrative units, the MFA registration-details report, and exporting logs through Graph.
  - **Needs P2:** PIM, risk-based policies, Entra access reviews.
  - **MFA approach on Free:** per-user MFA scoped to the Burn and Churn accounts. Security defaults are tenant-wide and would hit Michael's lab users too. The lack of P1 is recorded as a POA&M item or accepted risk, with per-user MFA as the interim control.
  - **MFA evidence on Free:** the per-user MFA status page plus sign-in log details, exported within the 7-day window.
  - **When SharePoint is available (Business Premium trial, D-8 and D-9):** sites, lists, libraries, Excel for the web and the Purview audit log (180 days by default) become available. Confirm which plan includes Purview Audit (Standard) once the licence is chosen.
- **Licensing on paper** (what the fictional company would buy): Microsoft 365 **Business Premium** for the Owner, Manager and Shift Leaders, and Microsoft 365 **F1/F3 frontline** licences for baristas. Business Premium includes Entra ID P1 (Conditional Access), Intune and Defender for Business; PIM needs P2, which Business Premium doesn't include. **Every price or licence claim must be checked against Microsoft's current pages when written, and dated.**
- **Conditional Access baseline:** require MFA for all users; block legacy authentication; require phishing-resistant MFA for admins; exclude break-glass. Report-only first, then enforce, the same pattern as the Cyber Home Lab.
- **Joiner/mover/leaver:** access requests are submitted on the intranet (People site, Access Requests list), approved by the Owner or Manager, and fulfilled by the IT Technician. Termination disables accounts within 24 hours, immediately for involuntary terminations (P-001 §5.4; PS-4, AC-2(3)). That's exactly what Q1's F-001 (Aiden Scott) shows went wrong.

### 5.3 Payments

- **No real payments, no real card data, anywhere.** Toast is documented only (`Simulation`); the website and the register use Stripe test mode with test card numbers and Stripe's simulated reader.
- **In store today: Toast** (card-present). Toast is the PCI service provider; the shop's obligations are SA-9 / PCI DSS 12.8 vendor management plus device inspection (PE-3 / 9.5.1).
- **In store after CR-005: Stripe Terminal (D-11).** The website's register screen takes counter payments through a Stripe reader (in the lab, Stripe's simulated reader, server-driven). Stripe states Terminal payments are validated with SAQ C. No offline card payments (Stripe's offline mode needs its mobile SDKs), so outages go to cash. Toast stays in use, and its conditions stay due, until cutover. Facts checked 2026-10-30.
- **Online, later: Stripe Checkout in test mode**, via `CR-002`, because Toast's ordering platform has no public sandbox a portfolio project can integrate with. Two processors is a normal small-business pattern; the program must say so explicitly, and give each processor its own vendor entry, crosswalk rows and PCI scope statement.
- Until CR-002 was approved, **no document mentioned Stripe** (AL-07), except CR-005 and this file. CR-002 was approved on 2026-11-05; the checker now allows Stripe once the change register shows CR-002 approved. Current-state documents still describe Stripe as **planned** until the register goes live (T12).

### 5.4 Store network (target design, AL-19)

Owned by the IT Technician. `Simulation` unless Michael later builds it as a firewall VM with VLANs in his lab, which would make it `Lab-verified`.

| Segment | Who connects | Firewall rule |
|---|---|---|
| POS (wired where possible) | Toast terminals only | Outbound to Toast services only; nothing inbound from other segments |
| Staff | Company-managed devices | Internet and Microsoft 365; no access to POS or management |
| Guest | Customers and personal devices | Internet only; client isolation; bandwidth limit; terms page |
| Devices | Cameras, espresso machine, temperature sensors, speaker | Internet to each vendor's cloud only; no access to other segments; nothing inbound; no port forwarding or UPnP |
| Management | Router, firewall, access points | Admin only from the IT Technician's device, with named admin accounts and logging |

Default deny between segments; every allow rule is written down with its reason. Changes to firewall rules go through the CR process (CM-3). The current state (POS and the manager laptop on one Wi-Fi network) stays documented as the starting point, with its POA&M item.

---

## 6. Using the NIST framework consistently

- **Controls:** NIST SP 800-53 Rev. 5, crosswalked to PCI DSS v4.0.1. Add controls only when a change introduces them, and update the crosswalk in the same PR.
- **Bringing a system in or out (RMF-style, kept light):** each change record walks the new system through
  1. **Categorize:** data types, CIA impact, boundary.
  2. **Select:** which controls apply; which existing controls change.
  3. **Implement:** how; who; when.
  4. **Assess:** what evidence proves it.
  5. **Authorize:** the Owner's written approval, as the risk acceptor.
  6. **Monitor:** the cadence in `continuous-monitoring.md`.
- **Controls CR-001 touches** (expected; confirm while writing it):

| Control | Change with M365 |
|---|---|
| IA-2, IA-2(1)/(2) | MFA through Entra (Conditional Access or security defaults). Closes POAM-001 **for M365 accounts** |
| AC-2, AC-2(3), AC-2(7), AC-6 | Group-based access, disable on leave, scoped admin roles, vendor delegation |
| AU-2, AU-6, AU-12 | Unified audit log **on and verified** (the Cyber Home Lab lesson), with a weekly review procedure. Moves POAM-003 forward |
| CM-3, CM-4 | **New:** change control and impact analysis, the CR process itself |
| CM-6, SI-3 | Intune baselines and Defender for Business. Moves POAM-009 and POAM-007 forward, if licensed |
| SA-9 | New vendors V-003 and V-004 assessed; V-007 offboarded |
| SC-8, SC-28 | Microsoft-managed encryption in transit and at rest, documented in the provider's shared-responsibility terms |
| PS-4, PS-5 | **New:** termination and transfer tied to account changes (F-001's root cause) |
| AT-2 | Training tracked in a SharePoint list, using the roster. Moves POAM-002 forward |

- **Status vocabulary, used in every repo:** `Simulation` (documented design for the fictional company), `Lab-verified YYYY-MM-DD` (actually done in a real tenant or VM, with evidence), `Planned`. Never present a simulated control as live.

---

## 7. The Microsoft 365 migration (CR-001)

### 7.1 History is kept, not rewritten

The Q1 2026 access review, the March 2026 incidents and the MFA export **really were** about Google Workspace in the company's timeline. Rewriting them would destroy the audit trail, which is the opposite of what a GRC program does. So:

- **Dated records stay as they are:** access reviews, incident log entries, evidence exports, assessments, training logs dated before the cutover. Only roster corrections from §3 are allowed, and each one gets a dated correction note at the bottom of the file.
- **Current-state documents are updated to M365:** company profile, scope, asset inventory, architecture, policies, procedures, risk register, control matrix, crosswalk, continuous monitoring, glossary, README. Each gets a "Revision history" line naming CR-001.
- **Cutover date (D-3): `2026-11-15`**, so the Q4 2026 access review is the first one run in Entra ID. Because tenant evidence carries real timestamps, the documented dates must match when accounts are actually created: pilot accounts (Owner, Manager, IT Technician) created before the cutover are the CR-001 pilot phase; if the build slips, the CR is revised with the new date rather than backdated.

### 7.2 The change record

Create `09-change-management/CR-001-google-workspace-to-microsoft-365.md` with:
- **Business justification:** one identity platform; Conditional Access; device management; a SharePoint intranet for SOPs, access requests and training; better audit logging.
- **Scope:** systems in (SYS-010 to SYS-014) and out (SYS-002, SYS-003 and SYS-005 QuickBooks); users (all 20 active store staff, the IT Technician and break-glass).
- **Related change, CR-003 (IT brought in-house):** `09-change-management/CR-003-it-support-in-house.md`, same date. Justification, hiring the IT Technician, handover from Vertex, removal of every Vertex account, V-004 offboarding. CR-002 stays reserved for the website.
- **Risk and impact analysis (CM-4):** migration risks (mail cutover, data loss, MFA enrolment gaps, the vendor's admin scope), each with a mitigation.
- **Control impact:** the table in section 6, finalized.
- **Plan:** pilot (Owner and Manager) → all staff → Google read-only for 30 days → Google closed. **Exit criteria:** every account has MFA enrolled; the audit log is verified returning records; Google data is exported and deleted, with the deletion confirmation filed as evidence for V-007 offboarding.
- **Rollback:** what happens if the cutover fails.
- **Approval:** the Owner's sign-off and date (AUTHORIZE).
- **Post-implementation review:** the Q4 access review (P4) is the formal check.

### 7.3 Files that change (hub)

All 23 files mentioning Google, grouped:

| Category | Files | Change |
|---|---|---|
| Current-state descriptions | `company_profile.md`, `assessment_scope.md`, `security-program-overview.md`, `glossary.md`, `system-architecture.md` (and diagram PNGs), `assets.md`, `data-classification.md` | Rewrite to M365, add a revision line |
| Policies | `P-001`, `P-002`, `P-003` | Replace system names; P-001 gains break-glass, group-based access and vendor delegation |
| Procedures | `PR-001` to `PR-004` | Rewrite steps for the Entra admin centre, the intranet access-request list and the unified audit log |
| Playbooks | `IRP-001` phishing, `IRP-002` account compromise | Microsoft 365 steps: revoke sessions, reset, check inbox rules, search the audit log |
| Monitoring | `continuous-monitoring.md` | M365 scope; remove Stripe |
| Evidence (dated) | `mfa-status.csv`, `user-access-review.csv`, `incident-log.md`, `evidence-matrix.md`, `examples/*` | **Keep the Google entries**; apply roster corrections with a note; add a new M365 evidence row when it exists |

### 7.4 The intranet, built in the tenant

**Rev 2:** the intranet is built directly in SharePoint Online in Michael's tenant, applying what he practised in `workspace` and `cyber-homelab`; it is not an org pack in the `workspace` repo.

- **Sites:** Home; **Operations** (opening and closing checklists, food-safety SOPs, equipment issues); **People** (onboarding and offboarding, an **Access Requests** list that drives PR-001, the training tracker for AT-2, timesheets feeding the payroll export); **Finance** (the bookkeeping workbook SYS-014, restricted to `grp-bc-owners` and `grp-bc-managers`); **Security & Compliance** (the published policies, the POA&M tracker, the incident log, the vendor inventory, access review sign-offs).
- **Permissions** are granted to the §5.2 groups only, never to individuals: least privilege is evidenced by the site permission pages themselves.
- **Content:** every person, system and vendor comes from `00-company-profile/org/` in the hub. Provisioning scripts (users, groups, sites, lists) read `people.csv` and the other org files, so the tenant can't drift from the program. Scripts live in the hub under `tools/tenant/`; any tenant-specific value comes from `.env`.
- **Until SharePoint is available** (Business Premium trial, D-8 and D-9), the sites are `Planned` and documented as design; Entra work (users, groups, Conditional Access, MFA, audit log) can go ahead first.

---

### 7.5 Build-day runbook (CR-001 and CR-003)

The order of work for the pilot and the 2026-11-15 cutover. Each step names the evidence it produces. Raw exports go to `_raw/` (git-ignored); only redacted copies are committed, marked `Lab-verified <date>`.

**Before (by 2026-11-14)**
- [ ] Nothing to buy: build day runs on Entra ID Free. The Business Premium trial (D-9) comes later, in the website repo's build phase
- [ ] `Install-Module Microsoft.Graph -Scope CurrentUser`; confirm `.env` values
- [ ] Draft the 3b PR (M365 rewrite of the §7.3 files), opened as a draft and **not merged**
- [ ] Note in the CR-001 log that Google Workspace and QuickBooks data were exported (step 1; fictional systems, so a log entry only)

**Pilot (on or before 2026-11-15)**
- [ ] Hub PR: Riley Morgan `Planned` → `Active` with a start date in `people.csv` (CR-003 step 1)
- [x] ~~Pilot accounts only~~ **Done differently, 2026-11-07:** the Owner chose to create all 20 Active staff at once (`provision-users.ps1 -PersonId EMP-001..EMP-020`) for the website's sign-in tests → E-33 (CR-001 log). Still to run: Riley Morgan once Active (`-PersonId EMP-022`)
- [ ] `provision-users.ps1 -IncludeAdminAccounts`: `adm-olivia.carter` and `adm-riley.morgan` with exactly the roles in `admin-accounts.csv`; turn on their MFA first; document the tenant's existing break-glass accounts → screenshot of role assignments (AC-6)
- [ ] Apply the tenant baseline (PR-013 §2): confirm the tenant-wide settings first (shared tenant), then screenshot each setting page → `artifacts/tenant/<date>-tenant-baseline/` (E-28, CM-6)
- [ ] MFA: per-user MFA for `grp-bc-` users (Entra Free; Conditional Access comes with the trial, D-9) → MFA status export (IA-2)
- [ ] Verify the audit log returns records → audit log export (AU-2)

**Cutover (2026-11-15)**
- [ ] Sign in as test users in InPrivate windows and register Authenticator; leave one barista unregistered on purpose; one wrong password; one denied MFA prompt
- [ ] **Same day** (7-day retention on Free): download sign-in logs, audit logs and the per-user MFA status; export group memberships
- [ ] Redact each export with `tools/tenant/redact_export.py` into `07-evidence-pack/artifacts/tenant/` (the planned file names are listed there); commit as new `Lab-verified` evidence rows; update E-01, E-02, E-03 and the evidence index
- [ ] `systems.csv`: SYS-010 → Live; `vendors.csv`: V-003 Active, V-006 and V-007 offboarding started
- [ ] CR-001 and CR-003 log entries; status → Implemented (awaiting review); **merge the 3b PR**
- [ ] Run the consistency checker; save the run under `07-evidence-pack/artifacts/consistency/`

**After**
- [ ] V-004 Vertex offboarding record (P5); credential rotation recorded
- [ ] Q4 2026 access review in Entra (P4) = post-implementation review for both CRs → CR status Closed; update POAM-001, 002, 003, 014, 016, 017 and re-rate controls on the new evidence

---

## 8. Evidence index

Add `07-evidence-pack/evidence-index.md` to the hub: **one table across all repos.** Columns:

`Evidence ID · Control(s) · Description · Repo · Path (link) · Date · Status (Simulation / Lab-verified) · Related POA&M`

This is the page an auditor (or a hiring manager) starts from. Entries in companion repos link to their exact file.

**Created 2026-10-30.** Update it whenever evidence is added, especially after the build day (§7.5).

---

## 9. Phases

Each phase is a set of PRs. **One repo per PR.** Hub PRs merge before the companion PRs that depend on them.

| Phase | Hours | Repos | What | Done when |
|---|---|---|---|---|
| **P0. Baseline** ✅ PR #4, 2026-10-29 | 1 | All three | Tag the current state `v1-pre-alignment` in each repo; add this file to the hub | Tags pushed; this file merged |
| **P1. Links and IDs** ✅ hub #5, IAM #9, VRA #3, 2026-10-30 | 2 | All three | Fix AL-09 (two-way links) and AL-11 (global finding IDs); add `identifiers.md` | Every companion README links the hub, and the hub links every companion |
| **P2. Canonical data and corrections** ✅ hub #6–#9, IAM #10, VRA #4, 2026-10-30 | 8 | Hub, IAM | Create `00-company-profile/org/*`; fix AL-01 to AL-08, AL-10 and AL-12 (decisions D-1 and D-2 first); add the consistency checker (§10) | The checker passes on all three repos |
| **P3. CR-001 migration** (3a ✅ hub PRs to #11; 3b drafted as PR #35, merged on the cutover date) | 10 | Hub | Write CR-001; update the current-state documents (§7.3); update the risk register, control matrix and crosswalk; add the PS-4, PS-5, CM-3 and CM-4 rows | No Google mention outside dated records and CR-001; the crosswalk covers every control |
| **P4. Q4 2026 access review** (structure done: IAM #13, 2026-11-02; the review runs after the cutover) | 6 | IAM | Restructure into `reviews/2026-Q1/` (history, unchanged) and `reviews/2026-Q4/`. Q4 runs against Entra groups and roles: confirm Q1 remediation, raise **AL-13 (generic vendor accounts)** as the "what Q1 missed" finding, check the break-glass and vendor-delegation design | Q4 findings roll up to hub POAM-014 |
| **P5. Vendor assessments** ✅ structure and every assessment done (VRA PRs #5 to #15, 2026-11-02); the V-004 offboarding record is completed at the CR-003 handover | 6 | Vendor | Restructure into `assessments/V-002-northwind/` (move with redirect notes) plus `assessments/V-003-microsoft/` and `offboarding/V-004-vertex-msp/` (CR-003) | Inventory statuses updated; findings roll up to POAM-0xx |
| **P6. Live tenant build** | 15–25 | Hub (`tools/tenant/`, evidence) + tenant | Create the 20 staff, vendor technician and break-glass accounts and the `grp-` groups from `people.csv`; Conditional Access (report-only, then enforce); MFA registration; verify the unified audit log; then the SharePoint sites (§7.4) once licensed. Commit redacted exports as `Lab-verified` evidence | Real sign-in and MFA evidence in the evidence index; every name matches the hub; no secret or tenant identifier committed |
| **P7. Portfolio** | 3 | Portfolio repo | Update the GRC case study to tell the multi-repo story; link the evidence index | Case study verified against the merged repos |
| **P8. Online ordering** | — | New repo | `CR-002` and the website plan (revised for M365 staff identity), including the counter register on Stripe Terminal that CR-005 depends on. **Out of scope for this file** | — |

**Order of value:** P1 and P2 fix things a reviewer could catch today. P3 and P4 are the strongest new story: a controlled migration plus a post-migration review that finds what the first review missed.

---

## 10. Consistency checker

`tools/check_program.py` in the hub. Python standard library only. It runs **locally** against sibling clones:

```
python tools/check_program.py --hub . --iam ../IAM-Access-Review-Lab --vra ../Vendor-Risk-Assessment-Lab
```

**It checks:**
1. **People:** every person named in any evidence CSV, finding, review or seed file exists in `people.csv`, with a matching role and status.
2. **Systems and vendors:** every system or vendor named matches `systems.csv` or `vendors.csv`. The company profile lists every vendor that isn't offboarded or inactive (added 2026-11-01). Retired systems may appear only in files dated before their `retired_on`, or in the CR.
3. **IDs:** no duplicate `POAM`, `R`, `E`, `CR` or `INC` IDs. Every POA&M "related finding" resolves to a real file and ID. Every `V-###` reference exists.
4. **Links:** every companion README links the hub; every relative link in the hub resolves.
5. **Controls:** every control in the matrix appears in the crosswalk, and the reverse; control counts in the README match the matrix (the earlier 11-vs-15 bug becomes impossible).
6. **Counts:** the headcount in the company profile matches `people.csv`.
7. **Forbidden terms:** no Stripe before CR-002 is approved in the change register (CR-005 excepted; satisfied since 2026-11-05); no `TODO` in published files; no real-looking personal data (phone numbers, SSNs).
8. **Secrets and tenant identifiers:** no `.env` file tracked; no GUIDs in tenant-ID or client-secret shape, no `*.onmicrosoft.com` domain, no IP addresses and no access tokens in committed files.
9. **Evidence agrees across repos** (added 2026-10-30): for the same person and system, hub `mfa-status.csv` and `user-access-review.csv` match the IAM access matrix (MFA state, access level).
10. **CSV files are well formed** (added 2026-11-01): every row has as many fields as its header, so an unquoted comma can't silently shift columns.

The retired-systems part of check 2 was added 2026-11-02: once a system's `retired_on` date has passed, any current-state document that still names it fails, except dated records, registers, change records, revision history and lines that describe it as history. `--as-of YYYY-MM-DD` previews a future date (run against the draft 3b PR #35 as of 2026-11-16: passes; against `main`: the 16 files the rewrite covers). The first full run is saved as `07-evidence-pack/artifacts/consistency/2026-10-30-baseline.txt`.

**CI:** the hub's GitHub Action runs the checks that need only the hub. Full cross-repo runs are local, and their output is committed as evidence (`07-evidence-pack/artifacts/consistency/YYYY-MM-DD.txt`). That's continuous monitoring of the program itself, worth one line in the portfolio case study.

**Monthly program monitor (added 2026-11-01, CA-7):** `.github/workflows/monthly-monitor.yml` runs on the 1st of each month (and on demand). It checks out all three repos, runs the full checker and `tools/due_dates.py`, commits the report as `07-evidence-pack/artifacts/monitoring/program-monitor/<date>.md` (added 2026-11-01, so the record lives in the repo and the monthly commit keeps the repo active), and opens a "Program monitor: YYYY-MM" issue (label `program-monitor`), closing the previous month's. Run by hand on another branch, it commits to that branch and skips the issue (for testing). **It only reads records; it never marks an activity as done** (Michael's question about automated monthly "inspections", answered 2026-11-01: automated detection, not automated completion). GitHub pauses scheduled workflows after 60 days without repo activity; a gap in the issues is recorded as the monitor being paused. When adding a recurring activity or a dated register item, make sure `due_dates.py` can read it: register items start with their deadline ("By 2026-11-30:" or "November 2026:"), and recurring activities are listed in its `recurring()` function.

---

## 11. Decisions for Michael

| ID | Decision | Recommendation |
|---|---|---|
| D-1 | Headcount: 19 or 20 active staff? | **Decided:** 20 active store staff (1/1/3/15), plus the part-time IT Technician (§4.2) |
| D-2 | MFA scope for Toast cashier PIN logins | **Decided:** out of MFA scope by design; personal PINs, one user signed in at a time, accountable, sign out when off register, no PIN sharing (§4.2). F-004 stays a Google MFA gap (AL-12) |
| D-3 | CR-001 cutover date | **Decided: 2026-11-15**, before the Q4 review |
| D-4 | Live tenant: none, the Cyber Home Lab tenant, or a new one | **Decided 2026-10-29:** the same tenant as the Cyber Home Lab, with real accounts for all staff to capture real sign-in and MFA evidence. Burn and Churn objects use the `grp-bc-` prefix and department = "Burn and Churn Coffee"; the homelab case study stays separate. No Entra ID P2 (PIM is a documented gap) |
| D-5 | IT support: outsourced MSP or in-house | **Decided:** hire a part-time in-house IT Technician, **Riley Morgan** (invented name; Michael performs the role in practice, but the fiction uses no real names). Vertex offboarded by CR-003 |
| D-6 | Microsoft licence mix on paper | **Proposed in CR-001 (2026-10-30):** Business Premium for the Owner, Store Manager, Shift Leaders and IT Technician; **F1** for baristas (Microsoft's pages, checked 2026-10-30: F1 and F3 both include Entra ID P1 and Intune Plan 1; only F3 has a mailbox, which baristas don't need) |
| D-7 | Payroll vendor: keep Northwind or replace it | **Recommended: keep V-002 Northwind as a paper vendor.** A vendor assessment never needs access to the vendor's system (it's questionnaires, contracts and SOC reports), the assessment is complete and dated, and it's fictional so no real company is implied. The hands-on part is the shop's own side: timesheets and the payroll export in SharePoint/Excel. **Confirmed by Michael 2026-10-29** |
| D-8 | SharePoint licence | **Superseded 2026-11-01:** no separate SharePoint licence. SharePoint comes with the Business Premium trial (D-9), which includes everything in Business Standard. Until then SYS-012 and SYS-014 stay `Planned` |
| D-9 | Microsoft 365 Business Premium 30-day trial | **Decided 2026-11-01:** started in the **website repo's build phase** (CR-002), when Michael is ready to test everything that needs it in one window: SharePoint sites and lists, Exchange mailboxes, Conditional Access (report-only, then on), guest MFA for CR-004, Intune and Defender. Licences assigned with `provision-users.ps1 -AssignLicenses`. Michael cancels before it converts to paid: before starting, confirm the trial terms, the licence count and how to cancel, and set a reminder. When it ends, a change record and POA&M item record the lost controls (T5); evidence from the trial is marked as covering the trial dates only |
| D-10 | Vendor guest account | **Decided 2026-10-30:** a named Northwind payroll contact as a B2B guest in `grp-bc-vendors`, with time-limited access to the payroll-export folder, under change CR-004, granted only after Northwind confirms MFA (VRA-V002:F-02). Tested end to end in the real tenant (invite, sign-in, file access, expiry, removal) with fictional test data; the guest's real test mailbox lives only in `.env` |
| D-11 | In-store payments: keep Toast or move to Stripe Terminal | **Decided 2026-10-30:** move to Stripe Terminal under CR-005, because Toast offers no sandbox and the program must be testable end to end. Toast is not erased: it stays the POS (Simulation) until the website's register passes acceptance testing, then it is offboarded like Google and Vertex, and its dated assessment stays as history. Trade-offs recorded in CR-005: no offline card payments (cash during outages), xtraCHEF replaced by a SharePoint list, Toast PIN rules carried over to the register sign-in |

---

## 12. Working agreement for Claude Code

1. **Explain first.** Before editing, say what changes, in which repo, and why; afterwards, say how to check it. Michael is learning.
2. **One repo per PR, one concern per PR.** Branch per task. Merge hub changes before the companion PRs that depend on them.
3. **Never rewrite dated records.** Roster corrections only, each with a dated correction note. Superseded documents get a revision line, not silent edits.
4. **IDs are permanent:** never renumber or reuse; mark retired items as retired.
5. **Canonical data wins.** If a document disagrees with `00-company-profile/org/`, fix the document or raise the conflict. Never invent a person, system or vendor outside those files.
6. **Fiction stays labelled.** Every README and generated document keeps "simulation for educational and portfolio purposes". No real company names as Burn and Churn's staff or customers, no real personal data, never link `burnandchurncoffee.com`.
7. **Status words are honest:** `Simulation` vs `Lab-verified YYYY-MM-DD`. Nothing is called live without evidence in the repo.
8. **Verify before claiming.** Facts about Microsoft licensing, pricing, features or PCI requirements are checked against the vendor's or standard's current pages when written, and dated. Facts about Michael's work are checked against the repo, not this plan.
9. **Run the consistency checker before every PR** that touches people, systems, vendors, IDs or controls, and paste its summary in the PR.
10. **Keep this file current:** tick phases as they merge; move fixed `AL-##` rows to a "Resolved" table with the PR number.
11. **Secrets stay local.** Tenant IDs, client IDs and secrets, real domains, Michael's own UPN, API keys (Stripe test keys included) live in a git-ignored `.env` and are read at runtime; commit a `.env.example` with placeholder names only. Raw tenant exports go in git-ignored `_raw/`; only redacted copies (fictional UPNs, no IPs, no GUIDs, no tokens) are committed as evidence. Check `git diff --cached` for secrets before every commit.
12. **Work the deferred-corrections register (§13).** When a trigger event happens, complete its rows, tick and date them, and add any newly discovered future change to the register.
13. **Treat AI as a program-wide change.** When AI is introduced, work register trigger T11 in full; don't add an AI feature to one repo alone.
14. **Program dates are the company's calendar, not Michael's.** Inspection, review and training dates follow best practice to make the fiction believable; Michael won't really run monthly inspections, and the project may sit idle for months. When work resumes after a gap, never backdate an activity that didn't happen: record the missed dates honestly (status check plus a POA&M review-log entry, the way the stalled Q1 remediation was recorded), then set new dates. Dates on `Lab-verified` evidence are always the real dates.

---

### 12a. Repository security (real world)

These repositories are Michael's real public portfolio, so their security is Michael's responsibility, not part of the fiction. In the fiction, the company's security documents live in the SharePoint Security & Compliance site, where the Owner is accountable and the IT Technician administers access through the `grp-bc-` groups.

| Control | State (checked 2026-10-30) |
|---|---|
| Secret scanning and push protection (all three repos) | **Enabled** |
| Collaborators | Michael only |
| Secrets kept out of the repos | `.gitignore` for `.env` and `_raw/`; checker check 8 (GUIDs, tenant domains, IPs, tokens, email addresses); secret scan of every staged diff |
| CI | Hub: consistency checker on every PR and push to `main` |
| Branch protection on `main` | **Not used, by Michael's decision (2026-11-01).** He works alone; CI runs the checker on every PR and push, and changes still go through PRs by habit |
| Two-factor authentication on the GitHub account | **Enabled** (confirmed by Michael 2026-11-01; on for months) |

## 13. Deferred corrections register

Changes we already know will be needed, grouped by the event that triggers them. **When a trigger happens, work through its rows in the same PR set, tick them, and add the date and PR number.** Dated records still follow rule 3: add status entries, don't rewrite history. Re-scan with the consistency checker and a story-level read (every file in the affected repos) after each trigger.

### T1. IT Technician hired (CR-003 step 1)
- [ ] `people.csv`: Riley Morgan `Planned` → `Active`, `start_date` set
- [ ] `roles.md`: headcount table ("planned hire" wording); `company_profile.md` IT paragraph
- [ ] CR-003 log entry: screening (PS-3) and access agreement (PS-6) recorded
- [ ] Privileged User Agreements signed by Riley and Olivia → E-20 present
- [ ] PR-008 §8 and PR-009 §7 status: Planned → in effect; first IT work log entry
- [ ] Within 30 days: first backup administrator drill with the Owner (PR-008 §5) → POAM-022

### T2. Microsoft 365 cutover (CR-001, 2026-11-15; runbook §7.5)
- [ ] Every runbook item in §7.5
- [ ] PR-004: keep log-review records separate from the incident log; add the within-7-days export (Entra ID Free) and the Microsoft 365 audit log; IRP-004: remote lock or wipe through Intune if licensed
- [ ] **3b rewrite** of current-state documents that still describe Google Workspace (AL-14): `assessment_scope.md`, `company_profile.md`, `glossary.md`, `security-program-overview.md`, `assets.md`, `data-classification.md`, `continuous-monitoring.md` (access review scope → Entra ID), `vendor-inventory.md`, `P-001`, `P-002`, `P-003`, `PR-001` to `PR-004`, `IRP-001`, `IRP-002`, `examples/*`, `system-architecture.md`, README business scenario. **Not** dated records (evidence CSVs, incident log, `CORRECTIONS.md`, change records)
- [ ] Architecture diagrams (`08-architecture/*.png`): regenerate if they show Google Workspace
- [ ] `systems.csv`: SYS-010 → Live; SYS-011/012/014 per licence; confirm or revise `retired_on` for SYS-002, SYS-003, SYS-005 (2026-11-15 if on schedule)
- [ ] `vendors.csv` and vendor inventory: V-003 → Active; V-006 and V-007 → offboarding, then Offboarded when the data deletion is confirmed
- [ ] Asset register: SYS-010 to SYS-014 statuses; SYS-002, SYS-003, SYS-005 → Retired
- [ ] IAM lab: procedure scope → Entra ID; README review history
- [x] Checker: "retired systems only in older files" part of check 2 (2026-11-02; run `--as-of` the cutover date before merging #35)
- [ ] Checker: add system aliases for the Microsoft 365 services used in evidence

### T3. Vertex offboarded (CR-003 steps 3–6)
- [ ] V-004 → Offboarded (`vendors.csv`, inventory); offboarding record in the Vendor lab (`offboarding/V-004-vertex-msp/`)
- [ ] Firewall and access point configurations exported at the handover: the first backup (PR-012) → backup log
- [ ] Credential rotation recorded in the CR-003 log; rotated credentials stored in the password manager; handover checklist (PR-008 §7) signed and filed with the V-004 offboarding record
- [ ] NorthPeak account disabled → IAM F-003 closure evidence; V-005 notes
- [ ] Asset PER-005 → Retired
- [ ] Procedures `PR-001` to `PR-004` and the IAM procedure: heading "IT Administrator (Vertex IT Support until 2026-11-15, then the IT Technician)" → "IT Administrator (IT Technician)"; `roles.md` vendor paragraph becomes history

### T3b. Password manager set up and tested (PR-009, POAM-021)
- [ ] Michael's lab test (PR-009 §6) with test entries only; Bitwarden test emails in `.env` only; redacted screenshots → `artifacts/credentials/vault-test-record.md` marked `Lab-verified <date>`
- [ ] E-19 present; SYS-015 → Live; V-009 → Active; IA-5 re-rated on the evidence (matrix, crosswalk, README counts); R-13 residual reviewed
- [x] Vendor lab: V-009 Bitwarden assessment (VRA #12, 2026-11-02: Moderate, approve with conditions)
- [ ] IAM lab: the Q4 review checks password manager membership (exactly the Owner and the IT Technician)

### T3a. Network segmentation implemented (POAM-015)
- [ ] Connected devices moved to the Devices segment (P-005 §3); POAM-026 network part closed
- [ ] P-005 §7 exception closed with a dated note; SC-7 re-rated on the evidence; `network-segmentation.md` gets a new dated record (the old one stays as history); R-04 residual risk reviewed
- [ ] If built as a firewall VM lab: evidence marked `Lab-verified <date>` and the lab labelled as a technique demonstration, like IAM:F-005

### T12. Toast replaced by Stripe Terminal (CR-005 cutover)
Trigger: CR-002 approved and the register passes CR-005 §6. Work these rows in the same PR set as the cutover; Toast mentions in dated records stay.
- [ ] **Before:** ~~Stripe gets its `V-###` and `SYS-###`~~ (done 2026-11-05 with CR-002: V-013, SYS-021); Stripe vendor assessment in the Vendor lab (AOC, responsibility matrix, SAQ C); sandbox evidence for every CR-005 §6 test, marked `Lab-verified <date>`; Stripe test keys in `.env` only
- [ ] **Org data:** `systems.csv` SYS-001 and SYS-004 `retired_on`; new register and reader rows; `vendors.csv` V-001 → Offboarded; `roles.md` Toast PIN section becomes register sign-in rules; `identifiers.md`, `timeline.md`
- [ ] **Current-state documents** (each with a revision line naming CR-005): `company_profile.md`, `assessment_scope.md`, `security-program-overview.md`, `glossary.md`, `assets.md` (HW-001 becomes the Stripe reader; SYS-001/004 retired), `data-classification.md`, `continuous-monitoring.md`, `vendor-inventory.md`, `system-architecture.md` (and diagrams), README
- [ ] **Policies:** P-001, P-002 (register sign-in rules), P-003, P-004 (SAQ C; tokens only), P-005 (POS segment holds the reader)
- [ ] **Procedures and playbooks:** PR-001 (register accounts instead of Toast PINs), PR-002, PR-003, PR-004 (Stripe Dashboard and register logs), **PR-005 (cash only during outages; Toast Offline Mode and the $50 limit removed)**, PR-006 (device list: the Stripe reader), PR-007 (training module), PR-008, IRP-001, IRP-002, IRP-003 (Stripe support contact), IRP-005 and IRP-007 (POS references), IRP-006 (vendor table: Toast row becomes history, Stripe row added)
- [ ] **Controls:** control matrix and crosswalk rows for card-present payments through Stripe; PCI scope note (SAQ C); re-rate PE-3 and SA-9 on the evidence
- [ ] **Evidence:** `pos-device-list.csv` (new reader; Toast terminal row marked retired, not deleted); evidence matrix and index rows; POAM-020 closed when Toast is offboarded (or closed as superseded, with a note)
- [ ] **IAM lab:** Toast stays in the Q1 matrix (history); the next review covers register sign-in and the Stripe Dashboard team members
- [ ] **Vendor lab:** V-001 status entry (offboarded, exit evidence: account closure and terminal return); new Stripe assessment folder
- [ ] **Checker:** ~~remove the CR-005 Stripe exception~~ (made conditional on CR-002's approval, 2026-11-05); add aliases for the register and reader

### T4. SharePoint available (Business Premium trial, D-8 and D-9)
- [ ] SYS-012 and SYS-014 → Live once sites and the Finance library exist
- [ ] Confirm which plan includes Purview Audit (Standard); update the logging approach (VRA-V003:F-04, PR-004)
- [ ] CR-004 precondition 2 met (log entry)

### T5. Business Premium trial starts or ends (D-9)
- [ ] Start: Conditional Access policies (report-only, then on); SYS-013 Live if Intune and Defender are configured; VRA-V003:F-01 can close; CR-004 risk 1 can close for the trial period
- [ ] End: new change record and POA&M item for the lost controls; VRA-V003:F-01 reopens; affected evidence marked as covering the trial dates only

### T6. Northwind conditions close (VRA-V002)
- [ ] F-02 and F-03 closed → V-002 → Active; SYS-006 `in_scope_since` set; asset SYS-006 Pending → Active; `company_profile.md` wording; Vendor-lab tracker and report status entries; POAM-013 status; CR-004 precondition 1 met
- [ ] F-01 and F-04 closed → POAM-013 can close

### T7. Q4 2026 access review completed (P4)
- [x] IAM lab: `reviews/2026-Q1/` (history) and `reviews/2026-Q4/` structure (IAM #13, 2026-11-02)
- [ ] Q4 review: raise AL-13 (generic vendor accounts) as the "what Q1 missed" finding; **record management sign-off** (missing in Q1)
- [ ] Close or update POAM-014 and POAM-016 with evidence; re-rate AC-2, AC-6, IA-2 and PS-4 on the new evidence (matrix, crosswalk, README counts)
- [ ] CR-001 and CR-003 → Closed (post-implementation review); POAM-017
- [ ] POA&M review-log entry (CA-5); evidence index; timeline

### T8. CR-004 implemented, and its access end date
- [ ] VC-001: `Planned` → `Approved` (with dates) → `Active` → `Removed`, each dated
- [ ] Guest evidence rows in the evidence index; what the sign-in log shows for guest MFA recorded (gap and POA&M item if it can't be verified)
- [ ] Corrective-action exercise evidence at the end date

### T9. Microsoft audit reports obtained (VRA-V003:F-02, within 30 days of onboarding)
- [ ] Review recorded (report period, exceptions, customer responsibilities); F-02 and F-05 closed; POAM-018 updated

### T9a. Toast conditions (VRA-V001), deferred by exception EXC-007
Decided 2026-11-02: Toast leaves under CR-005, so its documents (F-01, F-03, F-04) and a Toast-era SAQ (F-02) are not pursued. The Owner accepted the risk until Toast exits (EXC-007).
- [ ] Within 30 days of the CR-005 cutover: the shop's SAQ for the new register (SAQ C, per Stripe) completed and signed by the Owner; it becomes new evidence and may change PCI-mapped control ratings
- [ ] By 2027-01-31: if the CR-005 cutover hasn't happened, EXC-007 lapses and the Toast conditions resume (AOC, responsibility matrix, agreement, SOC 2, Toast-era SAQ), with a POA&M review-log entry

### T9b. Pre-build procedures come due (PR-005, PR-006, PR-007)
- [ ] November 2026: first monthly POS inspection under PR-006, starting with Tablet 2's open 2026-02-01 issue; log results; update E-07 and POAM-004
- [ ] Confirm the $50 offline limit is set in Toast Web and record it (PR-005 §9); Owner decides on cellular failover (if installed: P-005 segmentation applies, assets and vendors updated)
- [ ] By 2026-11-30: first all-staff training session (PR-007), including Microsoft 365 sign-in and MFA; training log updated; AT-2 re-rated only once staff are actually trained
- [ ] December 2026: first tabletop: the contingency plan (PR-005 §8) plus the incident playbooks, at least ransomware (IRP-005) and payroll fraud (IRP-007); record it in `tabletop-log.csv` → E-27, POAM-030, POAM-005; consider adding CP-4 to the control matrix
- [ ] By 2026-11-30: existing staff sign the acceptable use and confidentiality agreements (P-009 §5) in the first training session; personnel files started → POAM-032, E-29
- [ ] By 2026-11-30: staff acknowledge the personal phone policy (P-007) in the first training session; security keys bought for anyone who declines → POAM-031
- [ ] Missed dates → status check and POA&M review-log entry (CA-5)

### T9c. IT operations first cycles (P-006, PR-002, PR-010)
- [ ] By 2026-11-30: first end-of-support review (PR-010 §6); support dates looked up and recorded; replacements proposed to the Owner; exceptions approved → POAM-025
- [ ] December 2026: first recorded monthly update window (PR-002 §6); maintenance log rows; current versions in the equipment register → POAM-023, E-22
- [ ] First technician visit handled under PR-010 §4 (confirmed with the vendor, supervised, logged) → POAM-024; MA-5 re-rated only on real records
- [ ] Connected devices (PR-011): default passwords changed into the password manager; vendor accounts company-owned with MFA; espresso remote sessions logged; checklist re-run → POAM-026, E-23
- [ ] December 2026: first monthly encrypted offline backup copy (PR-012 §4); backup log row → POAM-029, E-26
- [ ] By 2027-02-15: first quarterly device baseline check (PR-015 §9) → baseline-checks.csv, E-12, POAM-009
- [ ] By 2026-11-30: personal alarm codes for each key holder; key register completed; decision on re-keying the back office (P-011) → POAM-035, E-32
- [ ] By 2027-02-28: first restore test from the offline drive (PR-012 §5) → CP-10 re-rated only on a passed test
- [ ] Cameras: each view checked against the keypad rule; entrance sign; 30-day retention; individual accounts → POAM-027, E-24

### T10. Recurring
- [ ] **Every month:** read the program monitor issue; do or reschedule each overdue item; record the outcome in the POA&M review log (CA-5, POAM-028)
- [ ] **Every POA&M review (at least monthly, POAM-019):** a review-log entry
- [ ] **Monthly offline backup copy** and **quarterly restore test (PR-012)**
- [ ] **Monthly update window (PR-002)**, **quarterly equipment register check** and **November end-of-support review (PR-010)**
- [ ] **Monthly POS inspections (PR-006)** and **daily opening checks**; **annual training (PR-007)**; **annual contingency tabletop (PR-005)**
- [ ] **Annual vendor re-checks:** Toast's PCI DSS compliance status every 12 months (PCI DSS 12.8.4); reassess V-001, V-002 and V-003 annually
- [ ] **Every January:** records retention review and disposals logged (P-010 §4). **Every six months:** exception register review (PR-014); expiring exceptions appear in the monitor
- [ ] **Annual policy reviews:** P-001, P-002, P-003 due 2027-02; P-004, IRP-001, IRP-002 due 2027-03
- [ ] **PCI DSS text verified against the official PCI SSC standard:** remove the "secondary sources" notes for 8.2.5, 6.5.1, 7.2, 9.3.1, 9.3.4, 9.4.6 and 9.4.7 in the crosswalk
- [ ] **Before publishing the portfolio case study (P7):** full checker run saved; no `Planned` or `Simulation` item described as live

### T11. AI introduced (likely with the website, CR-002, or the intranet)
AI is planned but not yet part of the company. When it is added, the whole program changes together, in one set of PRs:
- [ ] **Change record** with the RMF steps (§6): purpose, data, users, boundary, approval
- [ ] **Vendor:** a new `V-###` for the AI provider and a full assessment in the Vendor lab (how customer and company data is used, whether it trains models, retention, subprocessors, security reports)
- [ ] **System:** a new `SYS-###` in `systems.csv` and the asset register, with an evidence mode
- [ ] **Data classification:** which classes the AI may process (never cardholder data; Restricted data only with Owner approval)
- [ ] **Acceptable Use Policy (P-002):** approved AI tools only; no pasting Confidential or Restricted data into unapproved tools; staff check AI output before relying on it
- [ ] **Risk register:** AI risks (data leakage, prompt injection, wrong or harmful output, over-reliance, vendor lock-in), each with controls
- [ ] **Controls:** extend the matrix and crosswalk (for example SA-9, AC-6, SI-10 input validation, AU-2 logging of AI use); consider a crosswalk to the NIST AI Risk Management Framework
- [ ] **Training (PR-007):** an AI module; **incident playbook** for AI misuse or data leakage
- [ ] **Secrets:** AI provider API keys in `.env` only; add the provider's key format to checker check 8
- [ ] **Customers:** a privacy notice if the AI is customer-facing
- [ ] **Evidence:** new evidence rows; story-level review of all repos

---

## 14. References

| Topic | Link |
|---|---|
| NIST SP 800-53 Rev. 5 | https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final |
| NIST Risk Management Framework | https://csrc.nist.gov/projects/risk-management |
| PCI DSS v4.0.1 and SAQs | https://www.pcisecuritystandards.org |
| Microsoft Entra documentation | https://learn.microsoft.com/entra/ |
| Microsoft 365 Business Premium (security features) | https://learn.microsoft.com/microsoft-365/business-premium/ |
| Emergency access (break-glass) accounts | https://learn.microsoft.com/entra/identity/role-based-access-control/security-emergency-access |

---

## Revision history

| Rev | Date | Change |
|---|---|---|
| 1 | 2026-10-29 | Plan written from a full read of all five repos |
| 2 | 2026-10-29 | Michael's decisions: live Entra tenant for real evidence (D-4); `workspace`/`cyber-homelab` reclassified as skill sources, AL-15 withdrawn, P6 becomes the live tenant build; QuickBooks retired into an Excel workbook in SharePoint (SYS-014, V-006 offboarded); `evidence_mode` added to systems; no-real-payments rule; PIM gap; secrets rule 11 and checker check 8; new findings AL-16 to AL-18; D-7 and D-8 added |
| 3 | 2026-10-29 | D-1 (20 store staff), D-2 (Toast PIN rules), D-3 (cutover 2026-11-15), D-4 (shared tenant, `grp-bc-` groups), D-5 (in-house IT Technician Riley Morgan; Vertex offboarded by CR-003; GDAP dropped), D-7 confirmed; separation of duties and PS-3/PS-6; network target design §5.4 and finding AL-19 |
| 4 | 2026-10-30 | Tenant confirmed on Entra ID Free: what works on Free and what needs P1 or P2 (§5.2); D-8 timing; D-9 Business Premium trial as a strong option; P0 marked done |
| 5 | 2026-10-30 | P1 marked done; AL-09 and AL-11 moved to Resolved; AL-20 added; canonical `org/` files created (person IDs `EMP-###`; ISP added as V-008; Aiden Scott's termination date left blank as a recorded HR gap) |
| 6 | 2026-10-30 | Checker added (check 9, AL-21); hub corrections from PR 2c: AL-01 to AL-08, AL-10, AL-16, AL-19, AL-21 resolved; AL-12 and AL-18 stay open until the IAM matrix is corrected |
| 7 | 2026-10-30 | AL-12, AL-17, AL-18 and AL-20 resolved (IAM PR #10, VRA PR #4); checker flags unfilled template placeholders; full cross-repo run passes 9 of 9 |
| 8 | 2026-10-30 | `tools/tenant/provision-users.ps1` added: builds users and `grp-bc-` groups from `people.csv` (dry-run verified; run on the CR-001 build day); `.env.example` added; checker also scans `.ps1` files |
| 9 | 2026-10-30 | P2 marked done. P3 split: 3a now (CR-001, CR-003, change process, PS-4/PS-5/CM-3/CM-4, R-10/R-11, E-16/E-17, POAM-016/017); 3b (M365 rewrite of current-state docs) merges on the cutover date, because until then the company still runs Google Workspace. D-6 proposed (F1 for baristas) |
| 10 | 2026-10-30 | Build-day runbook added (§7.5): ordered steps for the pilot and cutover, with the evidence each step produces |
| 11 | 2026-10-30 | P5: vendor lab reorganised per vendor; V-003 Microsoft assessed before onboarding (POAM-018); AL-22 accepted |
| 12 | 2026-10-30 | Story alignment review: AL-23 to AL-25 resolved. Q1 remediation stalled (found by this review; feeds CR-003's justification); Northwind not live; CA-5 added (20 controls, 13 families); D-10 vendor guest account decided |
| 13 | 2026-10-30 | Deferred-corrections register added (§13): every known future update grouped by trigger (hire, cutover, Vertex offboarding, SharePoint, trial, Northwind conditions, Q4 review, CR-004, Microsoft reports, recurring); rule 12; AL-26 (policies reference documents that don't exist) |
| 14 | 2026-10-30 | Hub story-level review (procedures, playbooks, scope): AL-27 resolved; PR-004 and IRP-004 follow-ups added to register T2 |
| 15 | 2026-10-30 | §12a repository security baseline (real world): secret scanning and push protection verified; branch protection and 2FA pending Michael; register T11 for introducing AI program-wide; rule 13 |
| 16 | 2026-10-30 | Rule 14: program dates are the fictional company's calendar; gaps are recorded, never backdated. Cash and card payments both accepted (company profile, PR-005) |
| 17 | 2026-10-30 | In-house IT role completed: PR-008 (10 hours a week, Owner as backup administrator, Vertex handover checklist), PR-009 password manager (Bitwarden Free organization, SYS-015, V-009), Privileged User Agreement, IA-5, R-13/R-14, POAM-021/022, E-19/E-20; register T1, T3, T3b |
| 18 | 2026-10-30 | D-11: in-store payments move from Toast to Stripe Terminal under CR-005 (approved, blocked on the CR-002 register), so every payment flow can be tested; Toast stays until cutover; register trigger T12; checker allows Stripe in CR-005 only |
| 19 | 2026-11-01 | §12a closed: GitHub two-factor authentication confirmed on; branch protection not used, by Michael's decision |
| 20 | 2026-11-01 | Build readiness: no domain bought (tenant default domain; Cloudflare free tier for the website); D-8 superseded and D-9 decided (Business Premium trial in the website repo's build phase, cancelled before it converts); runbook uses `-IncludeAdminAccounts` and `redact_export.py`; `grp-bc-admins` and `grp-bc-vendors` listed; tenant and credentials evidence folders |
| 21 | 2026-11-01 | Batch B, IT operations: P-006 IT Operations Policy, PR-002 v2.0 (one-month PCI deadline, monthly update window), PR-010 equipment lifecycle, equipment register and maintenance log, device tags; SI-2, CM-8, MA-2, MA-5, SA-22 (26 controls, 14 families); R-15/R-16; POAM-023 to 025; E-21/E-22; register T9c |
| 22 | 2026-11-01 | Batch C, connected devices: PR-011 (cameras, espresso machine with vendor remote access, temperature sensors, speaker), P-005 v1.1 Devices segment, devices and vendors V-010 to V-012 and SYS-016 to SYS-018 registered, connected device checklist; MA-4 and PE-6 (28 controls); R-17/R-18; POAM-026/027; E-23/E-24; vendor ID note fixed (no IDs reserved) |
| 23 | 2026-11-01 | Monthly program monitor (GitHub Actions, CA-7): full checker plus `tools/due_dates.py`, opened as a monthly issue; reads records only, never generates evidence; checker check 10 (CSV format); CA-7 (29 controls); POAM-028; E-25 |
| 24 | 2026-11-01 | Batch D, backups: PR-012 (cloud data still needs backups; monthly encrypted offline copies in two places; Entra rebuilt from `people.csv`; quarterly restore tests); P-006 v1.1 §8; PR-005 v1.1; CP-9 and CP-10 (31 controls); R-19; POAM-029; E-26; due-date monitor reads the backup log. First monitor run (issue #30) passed |
| 25 | 2026-11-01 | Batch E, incident playbooks: IRP-005 malware and ransomware, IRP-006 vendor breach (vendor notification commitments from the assessments), IRP-007 payment and payroll fraud (prevention rules: callback, two people, no gift cards); P-003 v1.2 mapped to NIST CSF 2.0 / SP 800-61 Rev. 3 with a playbook index; IR-4 and IR-8 (33 controls, 15 families); R-20; POAM-030; E-27 tabletop log; due-date monitor tracks the yearly tabletop |
| 26 | 2026-11-01 | Program monitor commits each report as a dated file in `artifacts/monitoring/program-monitor/` (workflow needs contents: write); branch runs skip the issue for testing; checker treats saved reports like saved consistency runs |
| 27 | 2026-11-01 | Company profile, assessment scope, program overview and data classification now include the connected devices and vendors V-010 to V-012 (missed in batch C); checker check 2 confirms the profile lists every current vendor |
| 28 | 2026-11-01 | Build-day documents: P-007 Mobile Device and Personal Phone Policy (Authenticator on personal phones, no downloads, security-key alternative) and PR-013 Microsoft 365 Tenant Security Baseline (per-user MFA, user and guest settings, consent, admin roles, logging; tenant-wide items flagged for the shared tenant); AC-19 (34 controls); R-21; POAM-031; POAM-009 In Progress; E-28; runbook applies the baseline |
| 29 | 2026-11-02 | IAM lab reorganised into `reviews/2026-Q1/` and a `reviews/2026-Q4/` plan (IAM #13); checker and monitor read per-review folders (hub #38); hub links updated; V-004 Vertex offboarding record prepared (VRA #11) |
| 30 | 2026-11-02 | Policies batch A: P-008 Third-Party Risk Management (tiers and reassessment cadence, required contract clauses incl. 72-hour breach notice, PCI DSS 12.8.1–12.8.5, offboarding records) and P-009 Personnel Security (position risk, screening within local law, agreements before access, role change, leaving, external personnel, sanctions); personnel file checklist; PS-3 and PS-6 (36 controls); R-22; POAM-032; E-29 |
| 31 | 2026-11-02 | Policies batch B: P-010 Records Retention and Disposal (schedule for every record type, legal hold, NIST SP 800-88 Rev. 2 disposal methods, disposal log, yearly review) and PR-014 Risk Acceptance and Exception Procedure with the exception register (`EXC-###`; six existing exceptions approved, each expiring within 12 months); SI-12, MP-6, RA-7 (39 controls, 16 families); R-23; POAM-033/034; E-30/E-31; monitor reads exception expiries and the yearly records review |
| 32 | 2026-11-02 | Policies batch C: P-011 Physical Security (areas, personal keys and alarm codes, opening and closing, escorted and logged visitors) and PR-015 Device Configuration Baselines (laptop, tablets, POS, firewall, access points, router; quarterly checks; Intune later); key register, visitor log and baseline check log; PE-2, PE-8 (41 controls); CM-6 → Partially Implemented; R-24; POAM-035; E-32; monitor tracks the quarterly baseline check. The gap list's missing-policy items are complete except vulnerability scanning, which waits for the SAQ type |
| 33 | 2026-11-02 | Vendor assessments V-009 Bitwarden (before onboarding), V-010 cameras and V-012 temperature monitoring (VRA #12–#14) rolled up: vendors.csv, inventory, IRP-006 notification table, P-008 status, POAM-021/026/027; only the ISP (V-008) remains unscored |
| 34 | 2026-11-02 | Internet provider (V-008) assessed (VRA #15) and rolled up: every vendor that needs an assessment now has one |
| 35 | 2026-11-02 | Checker check 2: retired-systems rule with `--as-of` preview; flags exactly the 16 current-state files on `main` as of the cutover, and passes on the draft 3b PR |
| 36 | 2026-11-02 | Final alignment audit: hub README brought up to date (repositories table, scenario, 16 families, change management, monitoring, vendors, skills); stale plan lines fixed (vendor lab role, V-002 and V-003 status, SharePoint via the trial, P3 and P5 status); Toast conditions deferred by EXC-007 because Toast exits under CR-005 (T9a rewritten); offboarding vendors marked "Not Required" for assessment; GitHub descriptions and topics refreshed |
| 37 | 2026-11-05 | CR-002 raised and approved (online ordering website, staff portal and counter register; the public site was already live with fictional content and no company data). V-013 Stripe (planned) and V-014 Cloudflare (active) added; SYS-020 and SYS-021; vendor inventory, company profile, asset register, timeline and CR-005 log updated; the checker's Stripe rule is now keyed to CR-002's approval in the register |
| 38 | 2026-11-06 | `provision-users.ps1 -PersonId` added for the CR-001 pilot (only the named people, their groups and their admin accounts; guests skipped; unknown IDs refused; dry-run verified). Build-day pilot step uses it. The website's `setup-staff-app.ps1` (website ADR-0026) assigns app roles from the same roster |
| 39 | 2026-11-07 | First live tenant build: the 20 Active staff, five `grp-bc-` groups and 40 memberships created (CR-001 step 3 run early, by the Owner's decision; E-33, Lab-verified); the website's `bc-website-staff` app registered with 20 role assignments (CR-002 log; website evidence row). CR-001 now "Approved (in progress)"; the Google cutover date is unchanged. Still open: Riley Morgan, admin accounts, MFA, audit log, tenant baseline |
| 40 | 2026-11-07 | CR-002 step 3 live in production: go-live approval logged (it had been missed), acceptance test 1 partly met with the open Entra assignment finding, website repository audit logged (expired rate-limit acceptance reopened; Cloudflare rate limiter chosen), PR-004 weekly review of the website audit log from 2026-11-14; two website evidence rows |
| 41 | 2026-11-07 | Alignment pass after the website go-live and audit: AL-28 (vendor lab README), AL-29 (IAM scope: website app roles, assignment enforcement), AL-30 (V-014 data and overdue assessment); POAM-036 (VRA-V014 before website Phase 3, VRA-V013 before Phase 4) |
| 42 | 2026-11-08 | V-014 Cloudflare assessed (VRA-V014, late): Moderate 13/18, continue with conditions, F-01 to F-05 under POAM-036 (now In Progress); vendors.csv, inventory, evidence index, CR-002 exit criterion and log; AL-28 to AL-30 resolved |
| 43 | 2026-11-11 | The Owner's password manager recorded: Google Password Manager (V-015, SYS-022) holds owner-only credentials (break-glass, Stripe and Cloudflare recovery codes, backup-drive keys); Bitwarden (V-009, SYS-015) stays the planned shared vault for the Owner and IT Technician. PR-009 v1.1 §3a, PR-012 §4, IRP-006, EXC-009 (Microsoft's sealed-storage guidance), POAM-038 (assessment by 2026-11-25), CR-001 log correction |
