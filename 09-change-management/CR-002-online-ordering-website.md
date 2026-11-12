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
| 3 | Staff sign-in with Entra ID (app registration `bc-website-staff`, app roles, server-side sessions, staff portal, audit log) | Live in production 2026-11-07 (website PRs #23–#28). Sign-ins for the other three roles Lab-verified 2026-11-08 (website evidence `2026-11-08-role-tests`); the role-change test (step 7) and one open finding remain |
| 4 | Counter register and order board; cash orders; separation of duties on refunds | Live in production 2026-11-08 to 2026-11-09 (website PRs #33–#37): register with cash sales, order board, sold-out items and the restock chain, staff activity by role, refunds, end-of-shift cash count. Role and restock checks Lab-verified (website evidence `2026-11-08-role-tests`). The Owner ran the refund and cash-count checks in production on 2026-11-09 and reported them working, but chose not to save evidence; they stay CI-verified. **Phase 3 closed 2026-11-09** |
| 5 | Stripe Terminal with the simulated reader; refunds; decline handling (CR-005 §6 tests) | **Live in production 2026-11-09 to 2026-11-10** (website PRs #39, #41, #43; ADR-0035 to ADR-0037): set-up, card payments with declines, card refunds with separation of duties. Lab-verified (website evidence `2026-11-09-stripe-setup`, `2026-11-09-card-payments`, `2026-11-10-card-refunds`). V-013 Stripe to be assessed before the step is closed (Owner, 2026-11-09) |
| 6 | Customer accounts (Entra External ID), cart and Stripe Checkout; signed webhooks | **In progress.** Customer directory created 2026-11-12 (SYS-023, website ADR-0041); customer sign-in, cart and Checkout next |
| 7 | During the Business Premium trial: groups to app roles, Conditional Access, the SharePoint site and lists, the content sync | Planned |
| 8 | Vendor assessments V-013 and V-014; program alignment (risks, controls, crosswalk, evidence index) | Planned |

**Rollback:** each phase ships behind its own pull request and can be reverted; the maintenance switch (website runbook `docs/runbooks/maintenance-mode.md`) takes the whole site offline gracefully if needed.

## 6. Acceptance Tests (test mode)

- [ ] A barista signs in with their work account and lands on the staff portal with the Barista role; a non-member is refused by Entra ID. **Partly met:** the barista half is Lab-verified 2026-11-07 in production. The non-member half is an **open finding**: Entra issued a token to an account with no app role despite Assignment required, and the site's own role check refused it (website `docs/evidence/2026-11-07-staff-sign-in/`)
- [x] A refund by the person who took the payment is refused and the refusal is in the audit log. **Lab-verified 2026-11-10** in production for a card sale: the Manager who took it was refused, the refusal appears in the Owner's activity view, and the Owner refunded it to the card (website evidence `2026-11-10-card-refunds`; ADR-0034, ADR-0037). Cash refunds follow the same rule (CI-verified; checked by the Owner 2026-11-09 without saved evidence)
- [ ] A counter sale through the simulated reader and an online order both appear on the order board (CR-005 §6). **Counter half Lab-verified 2026-11-09** (website evidence `2026-11-09-card-payments`: a card sale through the simulated reader appears on the board as "COUNTER · CARD"); the online half arrives with step 6
- [ ] A replayed or wrongly signed Stripe webhook is ignored
- [ ] Changing a price in SharePoint and publishing updates the site; pointing the sync at another site is refused (403)
- [ ] No card number appears anywhere in the site's data or logs
- [x] The site refuses to serve with a live Stripe key (Lab-verified 2026-11-02, website ADR-0006)
- [x] Every page carries the fictional-business banner and is excluded from search engines (Lab-verified 2026-11-02, website CI)

## 7. Exit Criteria

- [ ] All acceptance tests passed and evidenced
- [ ] V-013 Stripe and V-014 Cloudflare assessed; SAQ type for the new payment channels confirmed against current PCI SSC and Stripe documents. **Assessments done:** V-014 2026-11-08 (VRA-V014), V-013 2026-11-10 (VRA-V013, a day after use, POAM-037), both continue with conditions. **Still open:** the SAQ type (VRA-V013:F-02)
- [ ] P-004, the control matrix and crosswalk updated for online and counter payments through Stripe
- [ ] Evidence index rows for the website's evidence

## 8. Post-Implementation Review

The first access review after staff sign-in goes live covers the website's app roles; the first weekly log review covers its audit log.

## 9. Log

| Date | Entry |
|---|---|
| 2026-11-05 | Raised and approved by the Owner. Raised **before the first change to company systems** (the Entra ID app registration in step 3). Steps 1 and 2 were already built (2026-11-02 to 2026-11-05) as a public site with fictional content: no company data, no tenant changes and no payments, so no company system had changed yet. Recording them here so the whole website sits under one change record. |
| 2026-11-07 | **First change to company systems.** Entra ID app `bc-website-staff` registered by the website's `scripts/tenant/setup-staff-app.ps1` (website ADR-0026): single tenant; certificate credential only (expires 2027-11-07), no client secret; delegated `openid` and `profile` only, admin consent granted; four app roles; Assignment required = Yes; 20 per-user role assignments from `people.csv` (1 Owner, 1 Manager, 3 Shift Leads, 15 Baristas; group assignment needs Entra ID P1, step 7). Accounts came from CR-001 the same day. Evidence: website `docs/evidence/2026-11-07-entra-staff-app/` (Lab-verified 2026-11-07). Sign-in itself is tested when the routes are built. |
| 2026-11-07 | **Go-live of step 3 (staff sign-in) in production.** The Owner approved the merge of website PR #26 ("please merge"), which deployed it; this entry records that approval, made the same day. Before it, the Owner created the production and preview D1 databases and set the production Worker secrets (website secrets inventory). First live sign-in: a barista, role shown correctly, sign-out working (website evidence `2026-11-07-staff-sign-in`). Follow-ups the same day: website PR #27 (evidence), PR #28 (sign-out warning for WCAG 2.2.1, hourly clean-up of expired sessions, privacy and security pages corrected for live sign-in). |
| 2026-11-07 | **Website repository audit** (website evidence `2026-11-07-repo-audit`, PR #29). Found: this go-live had not been logged here (entry above); the website's accepted risk "no rate limiting" expired with this step and was not revisited, so the public sign-in start can be used to exhaust the free daily D1 writes. Reopened in the website threat model (v1.4); the Owner chose a Cloudflare rate limiter, to follow in its own change. PR-004 weekly log review of the website's audit log begins **2026-11-14**, by direct D1 query until the Manager audit-log view exists (step 4). |
| 2026-11-08 | **V-014 Cloudflare assessed** (VRA-V014), late: in use since 2026-11-02, staff data since 2026-11-07. Moderate (13/18), **continue with conditions**; five findings under POAM-036, none blocking. Compensating control already in place: no anonymous request writes to the database (website ADR-0030), because Cloudflare's rate limiter doesn't enforce on this account (website ADR-0029). Re-scored High when the register replaces Toast (CR-005). |
| 2026-11-09 | **Go-live of step 4 (register, order board, refunds, cash count) in production, logged late.** The Owner approved each merge as it happened: website PR #33 (register, cash sales, order board) and #34 (sold-out items, restock requests, staff activity) on 2026-11-08; #35 (restock fix) and #36 (the restock chain, at the Owner's request after his role test) on 2026-11-08; #37 (refunds with separation of duties, the end-of-shift cash count, fixed reason lists) on 2026-11-09. Before each merge the Owner applied its database migration (0003 to 0006) to production and preview. This entry should have been written with the first of those merges (website working agreement item 13); found at the Phase 3 close-out check. Lab-verified so far: per-role sign-ins and the restock chain (website evidence `2026-11-08-role-tests`). Pending: the Owner's production check of refunds and the cash count. The Manager and Owner audit view now exists (website Activity screen: own entries and roles below; the Owner sees all), so the PR-004 weekly log review from 2026-11-14 can use it. The register is cash-only; Toast stays the store's POS until CR-005 §6 (Stripe Terminal) passes. |
| 2026-11-09 | **Stripe key exposure, contained the same day.** While setting up step 5, the Owner pasted the Stripe **test-mode** secret key into an AI assistant chat. The assistant didn't store or use it and advised rolling it; the Owner expired it in the Dashboard the same day. Test mode only: no real money or card data could be reached. The site now uses a **restricted** key with custom permissions (website ADR-0035), which the Owner placed in the git-ignored local settings himself; no full secret key is used by anything. Lesson: keys go straight from the Dashboard into the local file or `wrangler secret put`, never through a chat. |
| 2026-11-09 | **Stripe test-mode set-up (change to a vendor system).** The Owner ran the website's `scripts/stripe/setup-test.mjs` (21:29 UTC) with a one-time restricted key, deleted afterwards: a Terminal location (fictional address, Stripe-only), one **simulated** reader (`simulated_wisepos_e`), and the production webhook endpoint (8 events, API version pinned). The webhook signing secret went straight into the production Worker without being shown; the Worker's restricted key and the two IDs were set as Worker secrets by the Owner. Checked from outside: unsigned and forged webhook calls are refused (400). Evidence: website `docs/evidence/2026-11-09-stripe-setup` (Lab-verified 2026-11-09). Website PR 4.2 adds card payments at the counter (ADR-0036), checked once against Stripe's real test API. No live keys exist. |
| 2026-11-10 | **Go-live of step 5 (Stripe Terminal, card refunds) in production, logged with its evidence.** The Owner approved each merge: website PR #39 (Stripe foundations, 2026-11-09), #41 (card payments, 2026-11-09, migration 0008 applied first), #43 (card refunds, 2026-11-09). Lab-verified by the Owner in production: card payments with a decline and a retry (2026-11-09), and card refunds with separation of duties (2026-11-10), which **meets acceptance test 2**. A small defect found in the refund evidence (the form stayed visible after a refund, harmless) was fixed with it (website PR #44). Still open for this step: **V-013 Stripe** before it is closed. Toast remains the store's POS until CR-005 §6 is run in full. |
| 2026-11-12 | **Customer directory created (step 6; change to a vendor system).** The Owner ran the website's `scripts/tenant/setup-customer-directory.ps1` (website PR #55, ADR-0041) from his own terminal: resource provider registered, resource group `rg-bc-customers`, the external tenant **Burn and Churn Customers** (data in the United States) linked to the pay-as-you-go Azure subscription, not a trial, and a $5 monthly budget alerting the Owner at 80% and 100%. A first attempt with a common domain name failed within seconds, most likely because the name was already taken worldwide (Azure gave no reason); the failed entry was deleted and the second attempt succeeded. The directory is separate from the staff tenant, so staff Conditional Access never applies to customers and a customer account can never become a staff account. Customers: fictional demo accounts only (`example.com`, 555-01xx numbers, unusable passwords); real sign-up is tested later with the Owner's own addresses, which stay out of every repository. No IDs or domain names are recorded here. New system SYS-023 under V-003 Microsoft; VRA-V003 did not cover External ID, so a scope addendum is tracked as POAM-039. |

---

*This document is a simulation for educational and portfolio purposes only.*
