# CR-005: Replace Toast POS With Stripe Terminal
Burn and Churn Coffee

| | |
|---|---|
| **Status** | Approved (blocked: needs the CR-002 register to pass acceptance testing) |
| **Requested by** | Olivia Carter (Owner) |
| **Approved by** | Olivia Carter (Owner) |
| **Approved on** | 2026-10-30 |
| **Scheduled** | When the register screen in the online ordering website (CR-002, not yet raised) passes the acceptance tests in §6. No date is set; a date is added here when CR-002 is approved |
| **Implemented by** | IT Technician |
| **Related** | CR-002 (online ordering website, reserved); [CR-001](CR-001-google-workspace-to-microsoft-365.md) (Microsoft 365, where inventory moves); Toast assessment VRA-V001 (POAM-020) |

---

## 1. Business Justification

- **One payment processor.** The website planned under CR-002 takes online orders through Stripe. Running the counter on Stripe Terminal too means one processor, one contract, one vendor assessment and one set of PCI DSS obligations, instead of two.
- **One order board.** Counter orders and online orders land in the same system, so baristas work from one queue.
- **Card data never touches the shop's systems.** The card reader encrypts card data and sends it to Stripe; the register only receives a payment token ([Stripe: Terminal encryption](https://support.stripe.com/questions/stripe-terminal-encryption)).
- **A clearer PCI DSS position.** Stripe states that Terminal payments are validated with **SAQ C** and provides a pre-filled SAQ in the Stripe Dashboard ([Stripe: PCI compliance for Terminal](https://support.stripe.com/questions/pci-compliance-for-stripe-terminal)). The shop's SAQ type under Toast is still unconfirmed (VRA-V001:F-02).
- **It can be tested before go-live.** Stripe's sandbox includes a simulated reader and test cards, so the whole counter flow (sale, decline, refund) can be proven without real cards or money ([Stripe: Test Stripe Terminal](https://docs.stripe.com/terminal/references/testing)).

Facts about Stripe in this record were checked against Stripe's pages on 2026-10-30.

---

## 2. Scope

| | In | Out |
|---|---|---|
| **Systems** | Stripe Terminal card reader at the counter; the register screen in the CR-002 website; a SharePoint inventory list (replaces xtraCHEF) | SYS-001 Toast POS and SYS-004 xtraCHEF (retired at cutover) |
| **Vendors** | Stripe (vendor ID assigned when CR-002 is approved) | V-001 Toast, Inc. (offboarded, covering both Toast POS and xtraCHEF) |
| **Devices** | One Stripe-certified countertop reader (in the lab: Stripe's simulated reader) | Toast terminal POS-01 (returned or wiped as Toast directs) |
| **People** | Every store employee who uses the register (all 20); the IT Technician | — |

---

## 3. RMF Steps

| Step | For this change |
|---|---|
| **Categorize** | Card-present payment data: encrypted at the reader and tokenized by Stripe; the register stores tokens and order details only. High integrity and availability impact (the counter can't take cards when it's down) |
| **Select** | SA-9 (Stripe vendor assessment; Toast offboarding), PE-3 (reader inspection under PR-006, PCI DSS 9.5.1), AC-2 and AC-6 (register sign-in, one person signed in at a time), AU-2 and AU-6 (register and Stripe Dashboard logs), CP-2 (outage plan change, §4 risk 1), SC-8 (encryption in transit), CM-3 and CM-4 (this record) |
| **Implement** | §5 |
| **Assess** | Acceptance tests in §6, run in Stripe's sandbox; evidence committed as `Lab-verified <date>` with test keys kept in `.env` |
| **Authorize** | The Owner's approval above; go-live approval recorded in the log after the acceptance tests pass |
| **Monitor** | Monthly reader inspection (PR-006); weekly register and Dashboard log review (PR-004); Stripe's PCI DSS status checked every 12 months (PCI DSS 12.8.4) |

---

## 4. Risk and Impact Analysis (CM-4)

| # | Risk | Impact | Mitigation |
|---|---|---|---|
| 1 | **No offline card payments.** Stripe's offline mode works only with its iOS, Android and React Native SDKs, not with server-driven integrations ([Stripe: operate offline](https://docs.stripe.com/terminal/features/operate-offline/overview)). A web register can't take cards during an internet outage | Lost card sales during outages | Cash only during outages; PR-005 updated at cutover. This also removes the Toast-era risk of offline payments declining after the customer has left. Cellular failover (PR-005) becomes more valuable |
| 2 | Staff unfamiliar with the new register | Slow service, mistakes at the counter | Training before go-live (PR-007 module), a quick-reference card at the counter, the Store Manager on shift for the first week |
| 3 | Sales history lost when Toast closes | Bookkeeping gaps | Export Toast sales and item history before closing; reconcile in the bookkeeping workbook (SYS-014) |
| 4 | Inventory data lost with xtraCHEF | Ordering mistakes | Export xtraCHEF item and supplier lists; import into the SharePoint inventory list before cutover |
| 5 | Two processors live during the parallel period | Two PCI DSS scopes at once | Parallel period limited to 14 days; Toast's conditions (VRA-V001) still apply until it is closed |
| 6 | Toast terminal left with data or still enrolled | Unauthorized use; continued fees | Terminal returned or wiped as Toast directs; Toast account closed; written confirmation filed as exit evidence |
| 7 | Toast PIN rules lost in the move | Shared logins at the register | The same rules carry over to the register sign-in: one person signed in, accountable for every action, sign out when leaving, never use someone else's login (`org/roles.md`) |
| 8 | Stripe not yet assessed | Unassessed payment provider | Stripe vendor assessment in the Vendor Risk Assessment Lab before go-live; AOC and responsibility information on file (PCI DSS 12.8) |

---

## 5. Implementation Plan

| Step | What |
|---|---|
| 1 | CR-002 approved; Stripe vendor ID and system IDs assigned in `vendors.csv` and `systems.csv` |
| 2 | Stripe vendor assessment completed in the Vendor Risk Assessment Lab |
| 3 | Register screen built in the CR-002 website and connected to the simulated reader |
| 4 | Acceptance tests (§6) pass in the sandbox; evidence committed |
| 5 | Inventory moved from xtraCHEF to the SharePoint list; Toast sales history exported |
| 6 | Staff trained; Owner approves go-live (log entry) |
| 7 | Cutover: the counter uses Stripe Terminal; Toast stays available for 14 days as the rollback |
| 8 | Toast offboarded: account closed, terminal returned or wiped, confirmation filed; V-001 → Offboarded |

**Rollback:** during the 14-day parallel period, the counter can return to Toast in minutes. After step 8, there is no rollback to Toast.

---

## 6. Acceptance Tests (sandbox)

- [ ] A counter sale paid with a test card through the simulated reader appears on the order board
- [ ] A declined test card shows a clear message and no order is completed
- [ ] A refund is issued and recorded
- [ ] An online order and a counter order appear in the same queue
- [ ] Only the employee signed in to the register can take a payment; signing out ends the session
- [ ] No card number appears anywhere in the register's data or logs (tokens only)
- [ ] Test keys are read from `.env`; no key is committed

Mobile wallets (Apple Pay, Google Pay) can't be tested on Stripe Terminal in test mode, so no evidence claims them.

---

## 7. Exit Criteria

- [ ] All acceptance tests passed and evidenced
- [ ] Stripe vendor assessment complete; SAQ C completed and signed by the Owner
- [ ] PR-005 (outage plan), PR-006 (reader inspection), PR-007 (training), P-004 and the crosswalk updated for Stripe Terminal
- [ ] Toast account closed and terminal returned or wiped, with written confirmation
- [ ] V-001 Offboarded; SYS-001 and SYS-004 retired

---

## 8. Post-Implementation Review

The first access review after cutover confirms that register sign-in follows the rules in risk 7 and that no Toast logins remain. The first monthly reader inspection under PR-006 covers the new reader.

---

## 9. Log

| Date | Entry |
|---|---|
| 2026-10-30 | Raised and approved by the Owner, blocked until the CR-002 register passes acceptance testing. Toast remains the store's POS until cutover, and its assessment conditions (VRA-V001:F-01 to F-04, POAM-020) still apply because Toast processes the shop's card payments until then. |

---

*This document is a simulation for educational and portfolio purposes only.*
