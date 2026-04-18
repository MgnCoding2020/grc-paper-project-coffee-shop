## IRP-003: POS Suspicious Activity / Transaction Anomaly

### Purpose
This playbook outlines the response process for suspected unauthorized or fraudulent activity involving the Point-of-Sale (POS) system.

---

### Scope
Applies to:
- Toast POS system
- Payment transaction anomalies
- Unauthorized refunds or transactions

---

### Detection Sources
- Unusual transaction patterns (high volume, repeated refunds)
- Alerts from POS system or payment processor
- Employee or customer reports
- Log review findings (incident-log.md)

---

### Response Steps

#### 1. Identification
- Review transaction logs for anomalies
- Confirm unusual activity with staff
- Determine affected timeframe and accounts

#### 2. Containment
- Disable or restrict affected user accounts (if applicable)
- Temporarily suspend POS terminal if needed
- Notify management immediately

#### 3. Investigation
- Review transaction history and logs
- Identify:
  - user accounts involved
  - timestamps
  - transaction types
- Cross-check with access review records

#### 4. Eradication
- Remove unauthorized access or accounts
- Reset credentials for affected users
- Apply additional access restrictions if needed

#### 5. Recovery
- Restore normal POS operations
- Monitor transactions for continued anomalies
- Confirm system integrity

---

### Communication
- Notify store owner/manager
- Contact payment processor if fraud is confirmed
- Document findings in incident log

---

### Documentation
- Record all actions in:
  - artifacts/monitoring/incident-log.md
- Retain logs for review

---

### Lessons Learned
- Review access control (AC-2)
- Improve log review process (AU-6)
- Evaluate need for stricter privilege controls

---

### Related Controls
- AC-2 (Account Management)
- AU-6 (Log Review)
- AC-6 (Least Privilege)
