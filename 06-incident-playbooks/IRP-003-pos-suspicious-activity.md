# IRP-003: POS Suspicious Activity / Transaction Anomaly
Burn and Churn Coffee

## Document Control
**Playbook Owner:** Business Owner | 
**Approved By:** Business Owner | 
**Document control added:** 2026-10-30 (original effective date not recorded) | 
**Review Frequency:** Annual or following a POS-related incident | 
**Version:** 1.1


### Purpose
This playbook outlines the response process for suspected unauthorized or fraudulent activity involving the Point-of-Sale (POS) system.

---

### Scope
Applies to:
- Toast POS system
- Payment transaction anomalies
- Unauthorized refunds or transactions
- Suspected tampering with POS terminals (Payment Card Data Protection Policy, P-004 §4)

---

### Detection Sources
- Unusual transaction patterns (high volume, repeated refunds)
- Alerts from POS system or payment processor
- Employee or customer reports
- Log review findings (incident-log.md)
- **Signs of terminal tampering:** unrecognised devices attached, broken or altered seals, unexpected prompts, or a failed monthly device inspection (P-004 §4, PCI DSS 9.5.1)

---

### Response Steps

#### 1. Identification
- Review transaction logs for anomalies
- Confirm unusual activity with staff
- Determine affected timeframe and accounts

#### 2. Containment
- Disable or restrict affected user accounts (if applicable)
- Temporarily suspend POS terminal if needed
- **Suspected tampering:** stop using the terminal, don't unplug or open it, keep it secured, and contact Toast support (V-001) before it returns to service
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
- Contact Toast (payment service provider) if fraud or tampering is suspected or confirmed; external notifications are approved by the Owner (P-003 §9)
- Document findings in incident log

---

### Documentation
- Assign the next incident ID (`INC-###`) and a severity (P-003 §5)
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

---

### Revision History

| Date | Change | Reason |
|---|---|---|
| 2026-10-30 | Document control added; terminal tampering added to scope, detection and containment; Toast named as the contact; incident ID and severity step | P-004 treats suspected tampering as a security incident, but this playbook had no tamper steps (AL-27) |
