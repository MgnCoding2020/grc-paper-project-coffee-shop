# CR-002: Online Ordering Website, Staff Portal and Counter Register
Burn and Churn Coffee

| | |
|---|---|
| **Status** | Approved (in progress) |
| **Requested by** | Olivia Carter (Owner) |
| **Approved by** | Olivia Carter (Owner) |
| **Approved on** | 2026-11-05 |
| **Scheduled** | In phases, per the website plan: staff sign-in next; register and Stripe Terminal; customer ordering with Stripe Checkout; SharePoint content sync during the Microsoft 365 Business Premium trial. Dates are added to the log as each phase goes live |
| **Implemented by** | IT Technician |
| **Related** | [CR-001](CR-001-google-workspace-to-microsoft-365.md) (Microsoft 365: staff identity and SharePoint); [CR-005](CR-005-toast-pos-replacement.md) (Toast replaced by the website's register, which this change builds); register trigger T11 (AI, a separate change) |
| **System** | SYS-020, repository [burn-and-churn-website](https://github.com/MgnCoding2020/burn-and-churn-website) |

---

## 1. Business Justification

- **Order ahead.** Customers can browse the menu and order online, which a counter-only shop can't offer. Toast's ordering platform has no public sandbox, so the program can't test it end to end.
- **One register and one order board.** The website's staff portal becomes the counter register (CR-005), so online and counter orders land in one queue.
- **Staff use their work accounts.** Staff sign in with their Microsoft Entra ID accounts from CR-001; their role in the portal comes from their job, so access follows the joiner/mover/leaver process (PR-001) automatically.
- **Content the managers already own.** Menu, store hours, announcements, shift notes and inventory are edited in SharePoint lists and published to the site, so nobody edits website code to change a price.
- **It can be tested completely.** Stripe test mode, Stripe's simulated card reader and test customer accounts let every flow (sale, decline, refund, sign-in, refusal) be proven with no real money or personal data.

## 2. Scope

| | In | Out |
|---|---|---|
| **Systems** | SYS-020 the website (public site, staff portal, counter register); SYS-021 Stripe Checkout and Terminal (test mode); a dedicated SharePoint site with the website's content lists (part of SYS-012); app registrations in Entra ID (SYS-010); a separate Entra External ID directory for customers | Toast POS (retired by CR-005, not here); the intranet sites (CR-001); any AI feature (separate change, trigger T11) |
| **Vendors** | V-013 Stripe; V-014 Cloudflare (hosting); V-003 Microsoft (existing: Entra ID, External ID, SharePoint, Graph) | — |
| **Data** | Menu and prices (Public); staff identity and role (Internal); customer test accounts and orders (Confidential); payment tokens only, never card numbers | Real cardholder data, real personal data, real money: never, in any environment |
| **People** | All 20 store staff (portal and register), the IT Technician, the Owner (approvals, refunds) | — |

## 3. RMF Steps

| Step | For this change |
|---|---|
| **Categorize** | Public content (menu, hours); staff identities and roles; customer test accounts and orders; payment tokens from Stripe. Integrity and availability matter most (prices, orders, the register). Boundary: one Cloudflare Worker with its own database, plus Stripe, Entra ID and one SharePoint site |
| **Select** | AC-2, AC-3, AC-5 (refund separation of duties), AC-6, AC-11/AC-12 (session timeouts), IA-2, IA-5, IA-8, AU-2, AU-3, AU-6, AU-12, CM-3, CM-4, IR-4 (maintenance switch), SA-9 (Stripe and Cloudflare assessments), SA-11, SC-5, SC-7, SC-8, SC-23, SI-10, SI-12, RA-3 (threat model), RA-5, SR-3 |
| **Implement** | §5, in phases; each phase ends deployed to a preview with checks green |
| **Assess** | Acceptance tests in §6, run in test mode; evidence committed as `Lab-verified <date>` in the website repository (`docs/evidence/`) and indexed here |
| **Authorize** | The Owner's approval above; go-live approval for each phase recorded in the log |
| **Monitor** | CI on every change (tests, CodeQL, dependency review, audit); Dependabot; weekly log review (PR-004) once staff sign-in exists; the program monitor |

## 4. Risk and Impact Analysis (CM-4)

| # | Risk | Impact | Mitigation |
|---|---|---|---|
| 1 | A live Stripe key reaches the site | Real payments taken | The site refuses to serve anything if a non-test key is configured (tested); restricted test key only; keys never in the repository |
| 2 | Staff and customer sessions confused, or a role over-granted | Unauthorized refunds or menu changes | Separate directories for staff and customers; every route declares who may call it; authorization tests for every route; refunds need a manager and can't be issued by the person who took the payment (AC-5) |
| 3 | Shared counter tablet left signed in | Actions taken in another employee's name | 15-minute idle timeout on register screens; quick "switch user" that ends the session; the Toast PIN rules carry over (`org/roles.md`) |
| 4 | Over-broad Microsoft Graph permission | The website could read the whole tenant | App-only `Sites.Selected`, granted read on the one website-content site; certificate credential; grant recorded as evidence |
| 5 | Content from SharePoint or customers injected into pages | Defacement or script injection | Every row validated before publishing; strict Content Security Policy; no raw HTML from data |
| 6 | Secrets or one-time codes in logs | Credential leak | Query strings removed from host logs; no tokens or full emails logged; 3-day log retention |
| 7 | Stripe or Cloudflare not yet assessed | Unassessed vendors in the payment and hosting path | Vendor assessments (VRA-V013, VRA-V014) before customer payments go live (CR-005 step 2) |
| 8 | Business Premium trial ends | SharePoint sync and Conditional Access stop | Content stays in the site's database from the last sync; staff sign-in keeps working on Entra ID Free; recorded under register trigger T5 |

## 5. Implementation Plan

| Step | What | Status |
|---|---|---|
| 1 | Foundations: hosting, CI security checks, security headers, test-mode guard, threat model | Done (website PRs #1–#10, 2026-11-02) |
| 2 | Public site: design system, homepage, menu, information pages, error and maintenance pages; mobile Lighthouse Performance 97 | Done (website PRs #11–#21, 2026-11-02 to 2026-11-05) |
| 3 | Staff sign-in with Entra ID (app registration `bc-website-staff`, app roles, server-side sessions, staff portal, audit log) | Next |
| 4 | Counter register and order board; cash orders; separation of duties on refunds | Planned |
| 5 | Stripe Terminal with the simulated reader; refunds; decline handling (CR-005 §6 tests) | Planned |
| 6 | Customer accounts (Entra External ID), cart and Stripe Checkout; signed webhooks | Planned |
| 7 | During the Business Premium trial: groups to app roles, Conditional Access, the SharePoint site and lists, the content sync | Planned |
| 8 | Vendor assessments V-013 and V-014; program alignment (risks, controls, crosswalk, evidence index) | Planned |

**Rollback:** each phase ships behind its own pull request and can be reverted; the maintenance switch (website runbook `docs/runbooks/maintenance-mode.md`) takes the whole site offline gracefully if needed.

## 6. Acceptance Tests (test mode)

- [ ] A barista signs in with their work account and lands on the staff portal with the Barista role; a non-member is refused by Entra ID
- [ ] A refund by the person who took the payment is refused and the refusal is in the audit log
- [ ] A counter sale through the simulated reader and an online order both appear on the order board (CR-005 §6)
- [ ] A replayed or wrongly signed Stripe webhook is ignored
- [ ] Changing a price in SharePoint and publishing updates the site; pointing the sync at another site is refused (403)
- [ ] No card number appears anywhere in the site's data or logs
- [x] The site refuses to serve with a live Stripe key (Lab-verified 2026-11-02, website ADR-0006)
- [x] Every page carries the fictional-business banner and is excluded from search engines (Lab-verified 2026-11-02, website CI)

## 7. Exit Criteria

- [ ] All acceptance tests passed and evidenced
- [ ] V-013 Stripe and V-014 Cloudflare assessed; SAQ type for the new payment channels confirmed against current PCI SSC and Stripe documents
- [ ] P-004, the control matrix and crosswalk updated for online and counter payments through Stripe
- [ ] Evidence index rows for the website's evidence

## 8. Post-Implementation Review

The first access review after staff sign-in goes live covers the website's app roles; the first weekly log review covers its audit log.

## 9. Log

| Date | Entry |
|---|---|
| 2026-11-05 | Raised and approved by the Owner. Raised **before the first change to company systems** (the Entra ID app registration in step 3). Steps 1 and 2 were already built (2026-11-02 to 2026-11-05) as a public site with fictional content: no company data, no tenant changes and no payments, so no company system had changed yet. Recording them here so the whole website sits under one change record. |

---

*This document is a simulation for educational and portfolio purposes only.*
