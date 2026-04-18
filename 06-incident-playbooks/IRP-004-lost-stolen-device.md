## IRP-004: Lost or Stolen Device (Tablet / POS)

### Purpose
This playbook outlines the response process for lost or stolen business devices, including tablets and POS terminals.

---

### Scope
Applies to:
- Employee tablets
- POS terminals
- Any business-managed device

---

### Detection Sources
- Employee reports device missing
- Physical inspection discrepancies
- Missing asset during inventory check

---

### Response Steps

#### 1. Identification
- Confirm device is missing
- Identify:
  - device type
  - last known location
  - assigned user

#### 2. Containment
- Disable user access associated with the device
- Revoke active sessions if applicable
- If possible, remotely lock or wipe device

#### 3. Investigation
- Determine circumstances of loss/theft
- Check for potential unauthorized access
- Review recent activity logs

#### 4. Eradication
- Remove device access from systems
- Reset credentials tied to the device
- Reissue secure device if needed

#### 5. Recovery
- Replace device if necessary
- Reconfigure device with baseline settings
- Reinstate user access securely

---

### Communication
- Notify store owner/manager
- Report incident internally
- Escalate if sensitive data exposure is suspected

---

### Documentation
- Record in:
  - artifacts/monitoring/incident-log.md
  - artifacts/physical/physical-inspection-checklist.csv (if applicable)

---

### Lessons Learned
- Improve physical security controls (PE-3)
- Enhance device tracking procedures
- Reinforce employee awareness

---

### Related Controls
- PE-3 (Physical Access Control)
- AC-2 (Account Management)
- SI-3 (System Protection)
