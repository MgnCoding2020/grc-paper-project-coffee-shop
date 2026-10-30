# Burn and Churn Coffee: one company, one program, every repo telling the same story

> **Where this file goes.** The root of `MgnCoding2020/grc-paper-project-coffee-shop`, as `CLAUDE.md`. That repo is the **program hub**; this file also governs changes Claude Code makes in the companion repos listed in section 2. The repos are public, and this file can be too: it contains nothing private.
>
> **Written 2026-10-29** from a full read of all five repos at these commits: `grc-paper-project-coffee-shop` `e4e0646`, `IAM-Access-Review-Lab` `a965fe0`, `Vendor-Risk-Assessment-Lab` `50b4679`, `workspace` `fe52f01`, `cyber-homelab` `e5f003c`. Every finding in section 3 cites the file it came from. Re-verify anything older than a few weeks before acting on it (§12, rule 8).

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
| **`Vendor-Risk-Assessment-Lab`** | Operational: third-party assessments (SA-9). V-002 Northwind Payroll done; Microsoft and the IT managed-service provider next | "He can assess a vendor end to end." |
| **`workspace`** | **Burn and Churn's intranet**, as a second organization pack inside the existing engine (section 7.4). The Contoso Defense demo stays intact | "He can build and run M365/SharePoint for a real-shaped business." |
| **`burn-and-churn`** (future) | The online ordering website: `CR-002`, a separate later project with its own plan | "He can build a system to the controls." |
| `cyber-homelab` | **Not part of the fiction.** Michael's own Microsoft 365 tenant lab. It may host Burn and Churn's live tenant objects (decision D-4); its case study stays about Michael's lab | — |

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
          access       │   vendor     │   intranet   │   online ordering (later)
          reviews      │   assessments│   (M365)     │
     ┌─────────────────▼─┐ ┌──────────▼────────┐ ┌───▼────────────┐ ┌────────────────┐
     │ IAM-Access-Review │ │ Vendor-Risk-      │ │ workspace       │ │ burn-and-churn │
     │ -Lab              │ │ Assessment-Lab    │ │ (B&C org pack)  │ │ (CR-002)       │
     └───────────────────┘ └───────────────────┘ └────────────────┘ └────────────────┘
          findings ─────────────► roll up to hub POA&M ◄──────────── findings
```

---

## 3. Audit findings (2026-10-29)

These are the alignment problems found in the current repos. IDs are `AL-##` (alignment), tracked here until fixed. **Fixed in phase** refers to section 9.

| ID | Repo / file | What's wrong | Fix | Phase |
|---|---|---|---|---|
| AL-01 | Hub `07-evidence-pack/artifacts/access/*.csv`, `monitoring/incident-log.md` | Evidence uses generic accounts (`manager@`, `barista1@`, `barista2@`) that don't match the named roster in the IAM lab | Map to named people in the roster (§4.2), keep the dates | P2 |
| AL-02 | Hub `artifacts/training/security-training-log.csv` | Names (John Smith, Jane Doe, Alex Carter) exist nowhere else | Rebuild from the roster: all 20 active staff, with plausible completion states that match POAM-002 ("no formal training") | P2 |
| AL-03 | Hub `company_profile.md` vs IAM `user-access-matrix.csv` | Profile says ~19 staff (1 + 1 + 3 + **14**); the matrix has **15** active employees plus one terminated | Decide the count (D-1); recommended: the profile says 20 active, matching the evidence | P2 |
| AL-04 | Hub `user-access-review.csv` vs IAM matrix | Hub says the **Store Manager** is Google Workspace *Admin*; the IAM matrix says the Manager is a Standard User and the **Owner** is Super Admin | The IAM matrix wins (it's the detailed review); fix the hub evidence | P2 |
| AL-05 | Hub `vendor-inventory.md` | Lists only V-001 Toast and V-002 Northwind. The IAM lab and profile also use **Vertex IT Support** and **NorthPeak Systems** (IT vendors), **xtraCHEF**, **QuickBooks Online** and Google Workspace, none of which are inventoried | Full vendor inventory with stable IDs (§4.4) | P2 |
| AL-06 | Hub `01-asset-inventory/assets.md` | No assets for xtraCHEF, QuickBooks Online, Northwind Payroll, or vendor admin accounts; systems are named inconsistently with the IAM lab | Rebuild from the canonical system list (§4.3) | P2 |
| AL-07 | Hub `02-risk-management/continuous-monitoring.md` | Puts **Stripe** in access-review scope, but nothing else in the program has Stripe (payments are Toast) | Remove now; Stripe enters only through `CR-002` (online ordering) | P2 |
| AL-08 | Hub POA&M and procedures | Owners are "IT Admin" / "System Administrator", roles that don't exist in the company profile | Define the role: Vertex IT Support (managed service provider) performs administration, and the Owner is accountable (§4.2 RACI) | P2 |
| AL-09 | **Hub ↔ IAM lab** | **No links in either direction.** The hub README links only the vendor lab; the IAM lab README names the company but never links the program | Add the link rules in §2 | P1 |
| AL-10 | Hub POA&M | IAM lab findings (F-001 to F-005) never roll up to the hub POA&M, unlike the vendor lab, which rolls up as POAM-013 | Add a rolled-up item (POAM-014, AC-2) referencing the IAM lab's remediation tracker | P2 |
| AL-11 | IAM lab vs vendor lab | **Finding-ID collision:** both use `F-0x` | Keep local IDs; reference them globally as `IAM:F-001` and `VRA-V002:F-01` (§4.5) | P1 |
| AL-12 | IAM `user-access-matrix.csv`, `F-004` | All 15 cashiers have Toast MFA "No"; only Ethan Brooks is flagged ("MFA not enabled") while the rest say "Access appropriate". Ethan's Google Workspace row shows MFA "Yes" | Decide the MFA scope (D-2). Recommended: Toast cashier PIN logins are out of MFA scope by design; F-004 becomes Ethan's **admin-capable** or Workspace account, with the data made to agree | P2 |
| AL-13 | IAM matrix vs hub `P-001` §5.7 | Policy says vendor access is "assigned to named individuals (no generic vendor accounts)", yet the matrix has generic **"Vertex IT Support"** and **"NorthPeak Systems"** accounts, and the review didn't flag it | Leave Q1 as recorded (it's history), but **this is a missed finding**: raise it in the Q4 review as a new finding, a strong "what the first review missed" story | P4 |
| AL-14 | Hub, everywhere | Google Workspace is the productivity suite in 23 files (46 mentions) | `CR-001` migration to Microsoft 365 (section 7). Dated evidence stays; current-state documents change | P3 |
| AL-15 | `workspace` `js/app.js` | `config/sites.json` is fetched from a fixed path, so a second organization pack can't supply its own sites | Small engine change: a `sitesPath` setting alongside the existing `seedPath` (§7.4) | P6 |

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
- Email domain in documents: `burnandchurncoffee.com`. **Fictional, not owned:** never hyperlink it or use it as a real `mailto:`. If a live tenant is used (D-4), its real domain is the tenant's `*.onmicrosoft.com`, documented as the lab mapping.

### 4.2 People and roles

`people.csv` columns: `person_id, display_name, role, employment_status, start_date, end_date, upn, groups, notes`.

- **The cast comes from the IAM lab's `user-access-matrix.csv`**, the most detailed source:
  - Owner: Olivia Carter
  - Store Manager: Daniel Lopez
  - Shift Leaders: Mia Chen, Marcus Hill, Sofia Patel
  - Baristas: Ethan Brooks, Ava Reed, Noah Bennett, Lily Foster, James Cooper, Chloe Murphy, Logan Price, Grace Kelly, Henry Adams, Ella Turner, Jack Rivera, Nora Bailey, Leo Collins, Zoe Mitchell, Owen Parker
  - Terminated: Aiden Scott
- **UPN pattern:** `first.last@burnandchurncoffee.com` (e.g. `olivia.carter@…`).
- **Vendor people are named individuals**, as P-001 requires: Vertex IT Support's technician is a named person with a `vendor` role (create one, e.g. "Sam Ortiz (Vertex IT Support)"), not a shared account.
- **Break-glass:** two cloud-only emergency admin accounts (`bg-admin-01`, `bg-admin-02`), excluded from Conditional Access, monitored, credentials sealed with the Owner. This is standard Microsoft guidance, and it gives the Cyber Home Lab's "break-glass exclusion" lesson a home here.

**RACI** (`roles.md`):

| Activity | Owner | Store Manager | Shift Leaders | Vertex IT Support (MSP) | Baristas |
|---|---|---|---|---|---|
| Approve access requests | **A** | R (store systems) | C | I | — |
| Create, change and remove accounts | A | C | — | **R** | — |
| Quarterly access review | **A** | R (reviewer, store systems) | C | R (evidence export) | — |
| Vendor risk management | **A/R** | C | — | C | — |
| Incident response | **A** | R (store) | R (on shift) | R (technical) | I (report) |
| Security training | A | **R** | R | — | Participate |
| Policy ownership and approval | **A/R** | C | — | C | I |

"IT Admin" and "System Administrator" in existing documents become **Vertex IT Support (MSP)**, with the Owner accountable.

### 4.3 Systems

`systems.csv` columns: `system_id, name, category, vendor_id, data_classification, boundary, in_scope_since, retired_on, notes`.

| ID | System | Notes |
|---|---|---|
| SYS-001 | Toast POS | In-store payments and orders (card-present). Unchanged |
| SYS-002 | Google Workspace | **Retired** by CR-001 (`retired_on` set); kept for history |
| SYS-003 | Google Admin Console | **Retired** with SYS-002 |
| SYS-004 | xtraCHEF | Inventory and invoices (by Toast) |
| SYS-005 | QuickBooks Online | Accounting |
| SYS-006 | Northwind Payroll Services | Payroll and HR (V-002) |
| SYS-007 | Store network | Router, firewall, staff and guest Wi-Fi (existing NET-00x assets) |
| SYS-010 | Microsoft Entra ID | Identity, from CR-001 |
| SYS-011 | Exchange Online | Email, from CR-001 |
| SYS-012 | SharePoint Online + Teams | Files, intranet (Workspace), chat, from CR-001 |
| SYS-013 | Microsoft Intune + Defender for Business | Device management and endpoint protection, from CR-001 (licence-dependent; see §7.2) |
| SYS-020 | Online ordering website | **CR-002, later**; with Stripe (test mode) |

Keep the existing `SYS-`, `HW-`, `NET-`, `DATA-` and `PER-` asset IDs where they already exist; renumber only where needed, and record the old ID in `notes`.

### 4.4 Vendors

`vendors.csv` columns: `vendor_id, name, service, data_accessed, cardholder_data, inherent_tier, assessment_status, last_assessed, assessment_ref, owner, status`.

| ID | Vendor | Status |
|---|---|---|
| V-001 | Toast, Inc. (POS, and xtraCHEF) | Active; High; assessment not started |
| V-002 | Northwind Payroll Services | Active; High; **assessed 2026-06-23** (vendor lab) |
| V-003 | Microsoft (Microsoft 365) | Active from CR-001; assessment in P5 |
| V-004 | Vertex IT Support (MSP) | Active; privileged access; assessment in P5 |
| V-005 | NorthPeak Systems | **Offboarded**; access removal is IAM F-003 |
| V-006 | Intuit (QuickBooks Online) | Active; tier to score |
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
│ SharePoint Online: intranet hub (Workspace org pack) ─ Operations · People · Finance ·      │
│                    Security & Compliance sites                                              │
│ Intune + Defender for Business: manager laptop, store tablets (licence-dependent)          │
└───────────────┬─────────────────────────────────────────────────────────────────────────────┘
                │ SSO (where supported)                       ┌──────────────────────────────┐
   ┌────────────▼───────────┐   ┌─────────────────────────┐   │ Store network (SYS-007)      │
   │ Toast POS + xtraCHEF   │   │ QuickBooks Online       │   │ staff Wi-Fi · guest Wi-Fi ·  │
   │ (card-present; vendor- │   │ Northwind Payroll       │   │ POS segment (SC-7)           │
   │ managed PCI scope)     │   │ (SaaS, own logins)      │   └──────────────────────────────┘
   └────────────────────────┘   └─────────────────────────┘
        Later, CR-002: online ordering site ── Stripe Checkout (test mode) ── customer identity
```

### 5.2 Identity design (Entra ID)

- **Groups** (security groups, `grp-` prefix): `grp-owners`, `grp-managers`, `grp-shift-leads`, `grp-baristas`, `grp-vendor-msp`, `grp-break-glass`. Every access decision is granted to a group, never to a person directly. Workspace's persona derivation from group membership already works this way (verified live, per Workspace `docs/STATUS.md`).
- **Admin roles, least privilege:**
  - Owner: Global Administrator, kept **eligible**, not standing, where PIM is licensed; otherwise documented as a gap.
  - Vertex: delegated admin with only the roles it needs (User Administrator, Helpdesk Administrator), time-bound. In the documents this is **GDAP**, Microsoft's granular delegated admin model for service providers. In a lab tenant without a partner relationship, show it as a named vendor account with scoped roles and record the difference.
  - Baristas: no admin roles.
- **Licensing on paper** (what the fictional company would buy): Microsoft 365 **Business Premium** for the Owner, Manager and Shift Leaders, and Microsoft 365 **F1/F3 frontline** licences for baristas. Business Premium includes Entra ID P1 (Conditional Access), Intune and Defender for Business; PIM needs P2, which Business Premium doesn't include. **Every price or licence claim must be checked against Microsoft's current pages when written, and dated.**
- **Conditional Access baseline:** require MFA for all users; block legacy authentication; require phishing-resistant MFA for admins; exclude break-glass. Report-only first, then enforce, the same pattern as the Cyber Home Lab.
- **Joiner/mover/leaver:** access requests are submitted on the intranet (Workspace Access Requests list), approved by the Owner or Manager, and fulfilled by Vertex. Termination disables the account the same day (PS-4, AC-2(3)). That's exactly what Q1's F-001 (Aiden Scott) shows went wrong.

### 5.3 Payments

- **In store: Toast** (card-present). Toast is the PCI service provider; the shop's obligations are SA-9 / PCI DSS 12.8 vendor management plus device inspection (PE-3 / 9.5.1). Unchanged.
- **Online, later: Stripe Checkout in test mode**, via `CR-002`, because Toast's ordering platform has no public sandbox a portfolio project can integrate with. Two processors is a normal small-business pattern; the program must say so explicitly, and give each processor its own vendor entry, crosswalk rows and PCI scope statement.
- Until CR-002 is approved, **no document mentions Stripe** (AL-07).

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
- **The cutover date is a decision (D-3).** Recommended: `2026-11-15`, so the Q4 2026 access review is the first one run in Entra ID.

### 7.2 The change record

Create `09-change-management/CR-001-google-workspace-to-microsoft-365.md` with:
- **Business justification:** one identity platform; Conditional Access; device management; a SharePoint intranet for SOPs, access requests and training; better audit logging.
- **Scope:** systems in (SYS-010 to SYS-013) and out (SYS-002 and SYS-003); users (all 20 active staff plus the vendor technician plus break-glass).
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

### 7.4 Workspace as Burn and Churn's intranet

**Recommendation: an organization pack inside the `workspace` repo, not a fork.** The engine already separates code from content: `js/` never names the company, `check-workspace.py` enforces that, and the README's "Bringing your own organisation" section says a new business is "a real authoring task" while the engine is reusable. A fork would drift; a pack reuses every engine fix.

- **Engine change (AL-15):** add `data.sitesPath` beside the existing `data.seedPath` in `config/app.json`, and have `app.js` read it instead of the fixed `config/sites.json`. Burn and Churn is selected in `config/app.local.json` (git-ignored) or by a build flag; the Contoso Defense default doesn't change.
- **Pack location:** `orgs/burn-and-churn/` with `app.json` (org and brand overrides), `sites.json` and `seed/`.
- **Sites:** Home; **Operations** (opening and closing checklists, food-safety SOPs, equipment issues); **People** (onboarding and offboarding, an **Access Requests** list that drives PR-001, the training tracker for AT-2); **Finance** (the Timesheets module, feeding the Northwind payroll export, and QuickBooks reconciliations); **Security & Compliance** (the published policies, the POA&M tracker, the incident log, the vendor inventory, access review sign-offs).
- **Roles** map to the §5.2 groups (`grp-owners` and so on). Persona derivation from Entra groups is already verified live.
- **Content:** every person, system and vendor comes from `00-company-profile/org/` in the hub. Write a small export script in the hub that produces the pack's seed data from the org files, so the intranet can't drift from the program.
- **Live tenant: optional and later** (D-4, licensing). The pack is fully demonstrable on the `memory` provider; any live claim follows the Workspace `docs/STATUS.md` standard.
- **Effort:** this is the largest piece: about 15–25 hours of seed authoring. Do it after the hub and labs are aligned.

---

## 8. Evidence index

Add `07-evidence-pack/evidence-index.md` to the hub: **one table across all repos.** Columns:

`Evidence ID · Control(s) · Description · Repo · Path (link) · Date · Status (Simulation / Lab-verified) · Related POA&M`

This is the page an auditor (or a hiring manager) starts from. Entries in companion repos link to their exact file.

---

## 9. Phases

Each phase is a set of PRs. **One repo per PR.** Hub PRs merge before the companion PRs that depend on them.

| Phase | Hours | Repos | What | Done when |
|---|---|---|---|---|
| **P0. Baseline** | 1 | All three | Tag the current state `v1-pre-alignment` in each repo; add this file to the hub | Tags pushed; this file merged |
| **P1. Links and IDs** | 2 | All three | Fix AL-09 (two-way links) and AL-11 (global finding IDs); add `identifiers.md` | Every companion README links the hub, and the hub links every companion |
| **P2. Canonical data and corrections** | 8 | Hub, IAM | Create `00-company-profile/org/*`; fix AL-01 to AL-08, AL-10 and AL-12 (decisions D-1 and D-2 first); add the consistency checker (§10) | The checker passes on all three repos |
| **P3. CR-001 migration** | 10 | Hub | Write CR-001; update the current-state documents (§7.3); update the risk register, control matrix and crosswalk; add the PS-4, PS-5, CM-3 and CM-4 rows | No Google mention outside dated records and CR-001; the crosswalk covers every control |
| **P4. Q4 2026 access review** | 6 | IAM | Restructure into `reviews/2026-Q1/` (history, unchanged) and `reviews/2026-Q4/`. Q4 runs against Entra groups and roles: confirm Q1 remediation, raise **AL-13 (generic vendor accounts)** as the "what Q1 missed" finding, check the break-glass and vendor-delegation design | Q4 findings roll up to hub POAM-014 |
| **P5. Vendor assessments** | 6 | Vendor | Restructure into `assessments/V-002-northwind/` (move with redirect notes) plus `assessments/V-003-microsoft/` and `assessments/V-004-vertex-msp/` | Inventory statuses updated; findings roll up to POAM-0xx |
| **P6. Intranet org pack** | 15–25 | Workspace (+ hub export script) | AL-15 engine change; the Burn and Churn pack; seed generated from hub org data | Works on `memory`; every name and system matches the hub |
| **P7. Portfolio** | 3 | Portfolio repo | Update the GRC case study to tell the multi-repo story; link the evidence index | Case study verified against the merged repos |
| **P8. Online ordering** | — | New repo | `CR-002` and the website plan (revised for M365 staff identity). **Out of scope for this file** | — |

**Order of value:** P1 and P2 fix things a reviewer could catch today. P3 and P4 are the strongest new story: a controlled migration plus a post-migration review that finds what the first review missed.

---

## 10. Consistency checker

`tools/check_program.py` in the hub. Python standard library only. It runs **locally** against sibling clones:

```
python tools/check_program.py --hub . --iam ../IAM-Access-Review-Lab --vra ../Vendor-Risk-Assessment-Lab [--workspace ../workspace]
```

**It checks:**
1. **People:** every person named in any evidence CSV, finding, review or seed file exists in `people.csv`, with a matching role and status.
2. **Systems and vendors:** every system or vendor named matches `systems.csv` or `vendors.csv`. Retired systems may appear only in files dated before their `retired_on`, or in the CR.
3. **IDs:** no duplicate `POAM`, `R`, `E`, `CR` or `INC` IDs. Every POA&M "related finding" resolves to a real file and ID. Every `V-###` reference exists.
4. **Links:** every companion README links the hub; every relative link in the hub resolves.
5. **Controls:** every control in the matrix appears in the crosswalk, and the reverse; control counts in the README match the matrix (the earlier 11-vs-15 bug becomes impossible).
6. **Counts:** the headcount in the company profile matches `people.csv`.
7. **Forbidden terms:** no Stripe before CR-002; no `TODO` in published files; no real-looking personal data (phone numbers, SSNs).

**CI:** the hub's GitHub Action runs the checks that need only the hub. Full cross-repo runs are local, and their output is committed as evidence (`07-evidence-pack/artifacts/consistency/YYYY-MM-DD.txt`). That's continuous monitoring of the program itself, worth one line in the portfolio case study.

---

## 11. Decisions for Michael

| ID | Decision | Recommendation |
|---|---|---|
| D-1 | Headcount: 19 or 20 active staff? | **20** (the evidence has 15 baristas); update the profile |
| D-2 | MFA scope for Toast cashier PIN logins | Out of scope by design (documented); re-point F-004 at a real MFA gap |
| D-3 | CR-001 cutover date | **2026-11-15**, before the Q4 review |
| D-4 | Live tenant: none, the Cyber Home Lab tenant, or a new one | Decide after checking current licences. Until then, everything is `Simulation`. If you reuse the lab tenant, prefix every Burn and Churn object (`bc-`) and keep its case study separate |
| D-5 | Vertex technician's name | Pick one invented name and use it everywhere |
| D-6 | Microsoft licence mix on paper | Business Premium for leaders, F1/F3 for baristas, verified against Microsoft's current pages when written |

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
| Granular delegated admin privileges (GDAP) | https://learn.microsoft.com/partner-center/customers/gdap-introduction |
