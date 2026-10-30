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
| **`Vendor-Risk-Assessment-Lab`** | Operational: third-party assessments (SA-9). V-002 Northwind Payroll done; next, V-003 Microsoft (assessment) and V-004 Vertex IT Support (offboarding record, CR-003) | "He can assess a vendor end to end." |
| **Microsoft 365 tenant** (not a repo) | **Live evidence source.** Burn and Churn's staff accounts, groups, Conditional Access, MFA, audit log and SharePoint intranet are built in Michael's own tenant (D-4). Redacted exports are committed to the hub as `Lab-verified` evidence | "He can build and run M365 for a real-shaped business, and prove it." |
| **`burn-and-churn`** (future) | The online ordering website: `CR-002`, a separate later project with its own plan. Where the technologies connect: Entra sign-in, least privilege, Stripe test mode | "He can build a system to the controls." |

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
- Email domain in documents: `burnandchurncoffee.com`. **Fictional, not owned:** never hyperlink it or use it as a real `mailto:`. The live tenant (D-4) uses its own `*.onmicrosoft.com` domain. The real domain, tenant ID and Michael's own admin UPN are kept in a local `.env`, never committed; committed evidence shows `burnandchurncoffee.com` UPNs, with the substitution stated once in the evidence index.

### 4.2 People and roles

`people.csv` columns: `person_id, display_name, role, employment_status, start_date, end_date, upn, groups, notes`.

- **The cast comes from the IAM lab's `user-access-matrix.csv`**, the most detailed source:
  - Owner: Olivia Carter
  - Store Manager: Daniel Lopez
  - Shift Leaders: Mia Chen, Marcus Hill, Sofia Patel
  - Baristas: Ethan Brooks, Ava Reed, Noah Bennett, Lily Foster, James Cooper, Chloe Murphy, Logan Price, Grace Kelly, Henry Adams, Ella Turner, Jack Rivera, Nora Bailey, Leo Collins, Zoe Mitchell, Owen Parker
  - Terminated: Aiden Scott
  - **IT Technician (part-time, in-house, from CR-003): Riley Morgan.** Hired to run the M365 migration and own IT from then on. Not counted in the 20 store staff
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
| SYS-001 | Toast POS | Simulation | In-store payments and orders (card-present). No public sandbox, so no live evidence; no real card data anywhere in the program |
| SYS-002 | Google Workspace | Simulation | **Retired** by CR-001 (`retired_on` set); kept for history |
| SYS-003 | Google Admin Console | Simulation | **Retired** with SYS-002 |
| SYS-004 | xtraCHEF | Simulation | Inventory and invoices (by Toast) |
| SYS-005 | QuickBooks Online | Simulation | **Retired** by CR-001: bookkeeping moves to SYS-014. Kept for the Q1 history |
| SYS-006 | Northwind Payroll Services | Simulation | Payroll and HR (V-002). The shop's side (timesheets, payroll export) is Live in SYS-012/014 |
| SYS-007 | Store network | Simulation | Router, firewall, staff and guest Wi-Fi (existing NET-00x assets) |
| SYS-010 | Microsoft Entra ID | Live | Identity, from CR-001 |
| SYS-011 | Exchange Online | Live | Email, from CR-001 (licence-dependent) |
| SYS-012 | SharePoint Online + Teams | Planned → Live | Files, intranet lists and libraries, chat, from CR-001. Live once the SharePoint licence is reactivated (D-8) |
| SYS-013 | Microsoft Intune + Defender for Business | Simulation unless licensed | Device management and endpoint protection, from CR-001 |
| SYS-014 | Bookkeeping workbook (Excel for the web, in SharePoint) | Planned → Live | Sales, expenses and payroll reconciliation in a restricted Finance library, from CR-001. Permissions, versioning and audit-log entries are the live evidence |
| SYS-020 | Online ordering website | Test | **CR-002, later**; with Stripe (test mode) |

Keep the existing `SYS-`, `HW-`, `NET-`, `DATA-` and `PER-` asset IDs where they already exist; renumber only where needed, and record the old ID in `notes`.

### 4.4 Vendors

`vendors.csv` columns: `vendor_id, name, service, data_accessed, cardholder_data, inherent_tier, assessment_status, last_assessed, assessment_ref, owner, status`.

| ID | Vendor | Status |
|---|---|---|
| V-001 | Toast, Inc. (POS, and xtraCHEF) | Active; High; assessment not started |
| V-002 | Northwind Payroll Services | Active; High; **assessed 2026-06-23** (vendor lab) |
| V-003 | Microsoft (Microsoft 365) | Active from CR-001; assessment in P5 |
| V-004 | Vertex IT Support (MSP) | **Offboarded** by CR-003 (IT brought in-house) after a handover; access removal and knowledge-transfer sign-off are the exit evidence (offboarding record in P5) |
| V-005 | NorthPeak Systems | **Offboarded**; access removal is IAM F-003 |
| V-006 | Intuit (QuickBooks Online) | **Offboarded** by CR-001 (replaced by SYS-014); data export and subscription cancellation are CR-001 exit steps |
| V-007 | Google (Workspace) | **Offboarded** by CR-001; data-deletion confirmation is a CR-001 exit step |
| V-008+ | Stripe, Cloudflare, AI provider | Added only by CR-002 |

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

- **Groups** (security groups, `grp-bc-` prefix so they never mix with Michael's lab objects in the shared tenant): `grp-bc-all-staff` (every Burn and Churn account, the scope for Conditional Access), `grp-bc-owners`, `grp-bc-managers`, `grp-bc-shift-leads`, `grp-bc-baristas`, `grp-bc-it`, `grp-bc-break-glass`. Every Burn and Churn user also has department = "Burn and Churn Coffee". Every access decision is granted to a group, never to a person directly (the group-driven role pattern Michael verified live in `workspace`).
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
  - **When SharePoint is reactivated (D-8):** sites, lists, libraries, Excel for the web and the Purview audit log (180 days by default) become available. Confirm which plan includes Purview Audit (Standard) once the licence is chosen.
- **Licensing on paper** (what the fictional company would buy): Microsoft 365 **Business Premium** for the Owner, Manager and Shift Leaders, and Microsoft 365 **F1/F3 frontline** licences for baristas. Business Premium includes Entra ID P1 (Conditional Access), Intune and Defender for Business; PIM needs P2, which Business Premium doesn't include. **Every price or licence claim must be checked against Microsoft's current pages when written, and dated.**
- **Conditional Access baseline:** require MFA for all users; block legacy authentication; require phishing-resistant MFA for admins; exclude break-glass. Report-only first, then enforce, the same pattern as the Cyber Home Lab.
- **Joiner/mover/leaver:** access requests are submitted on the intranet (People site, Access Requests list), approved by the Owner or Manager, and fulfilled by the IT Technician. Termination disables the account the same day (PS-4, AC-2(3)). That's exactly what Q1's F-001 (Aiden Scott) shows went wrong.

### 5.3 Payments

- **No real payments, no real card data, anywhere.** Toast is documented only (`Simulation`); the website uses Stripe test mode with test card numbers.
- **In store: Toast** (card-present). Toast is the PCI service provider; the shop's obligations are SA-9 / PCI DSS 12.8 vendor management plus device inspection (PE-3 / 9.5.1). Unchanged.
- **Online, later: Stripe Checkout in test mode**, via `CR-002`, because Toast's ordering platform has no public sandbox a portfolio project can integrate with. Two processors is a normal small-business pattern; the program must say so explicitly, and give each processor its own vendor entry, crosswalk rows and PCI scope statement.
- Until CR-002 is approved, **no document mentions Stripe** (AL-07).

### 5.4 Store network (target design, AL-19)

Owned by the IT Technician. `Simulation` unless Michael later builds it as a firewall VM with VLANs in his lab, which would make it `Lab-verified`.

| Segment | Who connects | Firewall rule |
|---|---|---|
| POS (wired where possible) | Toast terminals only | Outbound to Toast services only; nothing inbound from other segments |
| Staff | Company-managed devices | Internet and Microsoft 365; no access to POS or management |
| Guest | Customers and personal devices | Internet only; client isolation; bandwidth limit; terms page |
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
- **Until SharePoint is reactivated** (D-8), the sites are `Planned` and documented as design; Entra work (users, groups, Conditional Access, MFA, audit log) can go ahead first.

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
| **P3. CR-001 migration** (3a: change records and new controls, now; 3b: M365 rewrite of current-state documents, merged on the cutover date) | 10 | Hub | Write CR-001; update the current-state documents (§7.3); update the risk register, control matrix and crosswalk; add the PS-4, PS-5, CM-3 and CM-4 rows | No Google mention outside dated records and CR-001; the crosswalk covers every control |
| **P4. Q4 2026 access review** | 6 | IAM | Restructure into `reviews/2026-Q1/` (history, unchanged) and `reviews/2026-Q4/`. Q4 runs against Entra groups and roles: confirm Q1 remediation, raise **AL-13 (generic vendor accounts)** as the "what Q1 missed" finding, check the break-glass and vendor-delegation design | Q4 findings roll up to hub POAM-014 |
| **P5. Vendor assessments** | 6 | Vendor | Restructure into `assessments/V-002-northwind/` (move with redirect notes) plus `assessments/V-003-microsoft/` and `offboarding/V-004-vertex-msp/` (CR-003) | Inventory statuses updated; findings roll up to POAM-0xx |
| **P6. Live tenant build** | 15–25 | Hub (`tools/tenant/`, evidence) + tenant | Create the 20 staff, vendor technician and break-glass accounts and the `grp-` groups from `people.csv`; Conditional Access (report-only, then enforce); MFA registration; verify the unified audit log; then the SharePoint sites (§7.4) once licensed. Commit redacted exports as `Lab-verified` evidence | Real sign-in and MFA evidence in the evidence index; every name matches the hub; no secret or tenant identifier committed |
| **P7. Portfolio** | 3 | Portfolio repo | Update the GRC case study to tell the multi-repo story; link the evidence index | Case study verified against the merged repos |
| **P8. Online ordering** | — | New repo | `CR-002` and the website plan (revised for M365 staff identity). **Out of scope for this file** | — |

**Order of value:** P1 and P2 fix things a reviewer could catch today. P3 and P4 are the strongest new story: a controlled migration plus a post-migration review that finds what the first review missed.

---

## 10. Consistency checker

`tools/check_program.py` in the hub. Python standard library only. It runs **locally** against sibling clones:

```
python tools/check_program.py --hub . --iam ../IAM-Access-Review-Lab --vra ../Vendor-Risk-Assessment-Lab
```

**It checks:**
1. **People:** every person named in any evidence CSV, finding, review or seed file exists in `people.csv`, with a matching role and status.
2. **Systems and vendors:** every system or vendor named matches `systems.csv` or `vendors.csv`. Retired systems may appear only in files dated before their `retired_on`, or in the CR.
3. **IDs:** no duplicate `POAM`, `R`, `E`, `CR` or `INC` IDs. Every POA&M "related finding" resolves to a real file and ID. Every `V-###` reference exists.
4. **Links:** every companion README links the hub; every relative link in the hub resolves.
5. **Controls:** every control in the matrix appears in the crosswalk, and the reverse; control counts in the README match the matrix (the earlier 11-vs-15 bug becomes impossible).
6. **Counts:** the headcount in the company profile matches `people.csv`.
7. **Forbidden terms:** no Stripe before CR-002; no `TODO` in published files; no real-looking personal data (phone numbers, SSNs).
8. **Secrets and tenant identifiers:** no `.env` file tracked; no GUIDs in tenant-ID or client-secret shape, no `*.onmicrosoft.com` domain, no IP addresses and no access tokens in committed files.
9. **Evidence agrees across repos** (added 2026-10-30): for the same person and system, hub `mfa-status.csv` and `user-access-review.csv` match the IAM access matrix (MFA state, access level).

Not yet implemented: the "retired systems only in files dated before `retired_on`" part of check 2; it arrives with CR-001 in P3. The first full run is saved as `07-evidence-pack/artifacts/consistency/2026-10-30-baseline.txt`.

**CI:** the hub's GitHub Action runs the checks that need only the hub. Full cross-repo runs are local, and their output is committed as evidence (`07-evidence-pack/artifacts/consistency/YYYY-MM-DD.txt`). That's continuous monitoring of the program itself, worth one line in the portfolio case study.

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
| D-8 | SharePoint licence reactivation | Michael reactivates it in time for the account build (2026-11-15). Until then SYS-012 and SYS-014 stay `Planned` |
| D-9 | Microsoft 365 Business Premium 30-day trial at build time | **Strong option, decide closer to 2026-11-15.** It adds P1 (Conditional Access, built report-only then enforced), Intune and Defender for Business for the trial window; when it ends, the fall-back to per-user MFA is recorded as a change record plus a POA&M item. Before starting: confirm the trial terms on Microsoft's page and what happens to policies when the trial lapses |

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

---

## 13. References

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
