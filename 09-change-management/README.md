# Change Management
Burn and Churn Coffee

---

## Purpose

Significant changes to Burn and Churn Coffee's systems, vendors or IT responsibilities go through a documented change process, so every change is justified, its security impact is understood before it happens, the Owner approves it, and its result is checked afterwards.

This process implements **CM-3 (Configuration Change Control)** and **CM-4 (Impact Analyses)**, and supports PCI DSS **Requirement 6.5.1** (changes to system components follow documented procedures that record the reason, description and security impact of each change).

---

## When a change record is required

- Adding, replacing or retiring a system in [systems.csv](../00-company-profile/org/systems.csv)
- Onboarding or offboarding a vendor in [vendors.csv](../00-company-profile/org/vendors.csv)
- Changing who administers systems, or what admin rights exist
- Changing firewall rules or network segmentation
- Any change that alters which controls apply, or how

Routine work (password resets, adding a new hire through the normal access-request process) does not need a change record.

---

## Lifecycle

| Stage | What happens | Who |
|---|---|---|
| 1. Request | Business justification, scope, systems and people affected | Requester (usually the IT administrator) |
| 2. Impact analysis (CM-4) | Security and operational risks, each with a mitigation; which controls change | IT administrator, Owner consulted |
| 3. Approval | Written approval and date; the Owner accepts the residual risk | **Owner** |
| 4. Implementation | Carried out to the plan; deviations recorded in the change record | IT administrator |
| 5. Post-implementation review | Evidence that the change worked and the exit criteria were met | Owner and Store Manager (not the implementer) |
| 6. Closed | Record finalised; documents updated with a revision line naming the CR | Owner |

**Status values:** Draft · Approved (scheduled) · In progress · Implemented (awaiting review) · Closed · Rolled back · Cancelled.

A change record is a dated record: once a stage is complete it is not rewritten. Later updates are added as dated entries in the record's log.

---

## Change Register

| CR | Title | Status | Approved | Scheduled | Record |
|---|---|---|---|---|---|
| CR-001 | Migrate from Google Workspace to Microsoft 365 | Approved (scheduled) | 2026-10-30 | 2026-11-15 | [CR-001](CR-001-google-workspace-to-microsoft-365.md) |
| CR-002 | *Reserved for the planned online ordering website* | Not raised | — | — | — |
| CR-003 | Bring IT support in-house; offboard Vertex IT Support | Approved (scheduled) | 2026-10-30 | 2026-11-15 | [CR-003](CR-003-it-support-in-house.md) |
| CR-004 | Time-limited guest access for Northwind's payroll contact | Approved (blocked: needs VRA-V002:F-02 closed and SharePoint live) | 2026-10-30 | After CR-001 | [CR-004](CR-004-vendor-guest-access.md) |

---

*This document is a simulation for educational and portfolio purposes only.*
