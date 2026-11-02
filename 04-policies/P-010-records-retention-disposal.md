# Records Retention and Disposal Policy
Burn and Churn Coffee

## Document Control
**Policy Owner:** Business Owner | 
**Approved by:** Business Owner | 
**Effective Date:** 2026-11-02 | 
**Review Frequency:** Annual | 
**Version:** 1.0

----------

## 1. Purpose
Keep each kind of record long enough to run the business, meet obligations and investigate problems, and no longer, then destroy it so it can't be recovered. Records kept "just in case" are records that can leak; records destroyed too early can't prove anything.

It implements NIST SP 800-53 **SI-12 (Information Management and Retention)** and **MP-6 (Media Sanitization)**, following **NIST SP 800-88 Rev. 2** (September 2025) for disposal. It supports PCI DSS 3.2.1, 9.4.6 and 9.4.7.

The periods below are the Owner's business decisions, recorded here. **They aren't legal advice:** the Owner confirms financial and employment record periods with the company's accountant, and local law always takes precedence.

-----------

## 2. Retention Schedule

| Record | Where it lives | Keep for | Then |
|---|---|---|---|
| **Card numbers and card data** | **Nowhere.** Never stored ([P-004](P-004-payment-card-data-protection.md)) | — | Any card number written down by mistake is cross-cut shredded at once and reported |
| Sales and financial records (bookkeeping workbook, POS reports, invoices) | SharePoint Finance library; POS vendor | **7 years** | Delete; confirm with the accountant first |
| Payroll records and timesheets | SharePoint; payroll provider | **7 years** | Delete |
| Personnel files (agreements, training, role changes) | Owner only | **Employment plus 7 years** | Delete or shred |
| Screening results | Owner only | **Until the hiring decision** | Shred; the personnel file keeps only "done, passed" ([P-009](P-009-personnel-security.md)) |
| Sign-in and audit log exports | `07-evidence-pack/artifacts/tenant/` (redacted) | **12 months** (the same as PCI DSS 10.5.1 asks of card environments) | Older raw exports in `_raw/` deleted; redacted evidence kept with its records |
| Incident records | Incident log | **3 years** (P-003 requires at least one) | Kept in git history |
| Access reviews and their evidence | IAM Access Review Lab | **3 years** | Kept in git history |
| Vendor assessments and contracts | Vendor Risk Assessment Lab; Owner | **Contract term plus 3 years** | Contracts shredded; assessments kept in git |
| Policies, procedures, change records, risk register, POA&M | This repository | **Permanently** (git history) | — |
| Training records | Training log | **Employment plus 3 years** | Delete |
| Camera footage | Camera vendor's cloud | **30 days**, unless saved for an incident ([PR-011](../05-procedures/PR-011-connected-devices.md)) | Deleted automatically |
| Food-safety temperature log | Temperature monitoring service | **2 years** | Delete |
| Backups | Encrypted offline drives | **12 months** ([PR-012](../05-procedures/PR-012-backup-and-recovery.md)) | Overwritten in rotation |
| Equipment register and maintenance log | This repository | **Life of the device plus 1 year** | Kept in git history |
| Technician and visitor records | Maintenance log | **1 year** | Kept in git history |

**Legal hold:** if a record may be needed for a dispute, claim or investigation, the Owner suspends its deletion in writing until the hold is lifted.

-----------

## 3. Disposal Methods (MP-6)

| What | Method (NIST SP 800-88 Rev. 2 level) |
|---|---|
| Paper (receipts, handwritten notes, printed reports, contracts) | **Cross-cut shredding** on site (destroy) |
| Laptops, tablets, phones being retired or sold | Encryption on, then factory reset, which erases the encryption key (**purge**); or physical destruction if it won't reset |
| USB drives and old backup drives | **Physical destruction** (destroy) |
| Card-reading devices (POS terminal, card reader) | Returned to the vendor as it directs, with written confirmation ([PR-010](../05-procedures/PR-010-equipment-lifecycle.md) §7) |
| Cloud data | Deleted in the service; for a vendor being left, written deletion confirmation ([P-008](P-008-third-party-risk.md) §6) |
| Connected devices | Factory reset and removed from the vendor account ([PR-011](../05-procedures/PR-011-connected-devices.md)) |

Every disposal of a device, drive or box of records is recorded in the [disposal log](../07-evidence-pack/artifacts/assets/disposal-log.csv): date, what, method, who did it, who witnessed it. The equipment register is updated too.

-----------

## 4. Yearly Review
Every **January**, the IT Technician and the Owner go through the schedule: anything past its period (and not on legal hold) is disposed of and logged, and the schedule is checked for new kinds of records.

-----------

## 5. Current Status
The schedule is new. No disposal has ever been recorded, and the first yearly review is due January 2027. Tracked under **POAM-033**.

-----------

## 6. Related Documents
  - [Payment Card Data Protection Policy (P-004)](P-004-payment-card-data-protection.md)
  - [IT Operations Policy (P-006)](P-006-it-operations.md) §7
  - [Backup and Recovery Procedure (PR-012)](../05-procedures/PR-012-backup-and-recovery.md)
  - [NIST SP 800-88 Rev. 2, Guidelines for Media Sanitization](https://csrc.nist.gov/pubs/sp/800/88/r2/final)

-----------

*This document is a simulation for educational and portfolio purposes only.*
