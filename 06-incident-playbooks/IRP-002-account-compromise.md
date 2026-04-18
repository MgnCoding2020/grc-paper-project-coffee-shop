# IRP-002: Account Compromise Response Playbook  
Burn and Churn Coffee

---

## Document Control
**Playbook Owner:** Business Owner  
**Approved By:** Business Owner  
**Effective Date:** March 2026  
**Review Frequency:** Annual or following an account compromise incident  
**Version:** 1.1  

---

## 1. Purpose
This playbook provides operational guidance for responding to suspected or confirmed account compromise incidents.

Account compromise occurs when unauthorized individuals gain access to company accounts through phishing, credential theft, password reuse, or malware.

---

## 2. Scope
This playbook applies to compromised accounts affecting:

- Google Workspace user accounts  
- Google Workspace administrative accounts  
- Toast POS administrative accounts  
- Company-issued tablets  
- Network administration accounts  

---

## 3. Indicators of Account Compromise

- Unusual login alerts or unfamiliar locations  
- Unexpected password reset notifications  
- Emails sent without user knowledge  
- Unauthorized account changes  
- Suspicious forwarding rules  
- Unauthorized administrative activity  
- Reports of fraudulent transactions  

---

## 4. Severity Classification

- **Low:** Suspicious activity, no confirmed unauthorized access  
- **Medium:** Likely compromise affecting a single account  
- **High:** Confirmed compromise, multiple accounts, or business impact  

---

## 5. Roles and Responsibilities

### Business Owner
- Oversees incident response  
- Approves major containment actions  
- Coordinates external communication  

### Store Manager
- Coordinates response  
- Conducts initial assessment  
- Initiates containment actions  

### Employees
- Report suspicious activity immediately  
- Follow response instructions  

### IT Vendor
- Assists with investigation, remediation, and recovery  

---

## 6. Response Procedure

### Step 1: Detection and Reporting
- Suspicious activity identified through alerts or user reports  
- Report to Store Manager or Business Owner  

### Step 2: Initial Assessment
- Confirm signs of unauthorized access  
- Identify affected accounts  
- Determine potential impact  

### Step 3: Containment
- Reset passwords immediately  
- Revoke active sessions  
- Enforce MFA  
- Disable account if needed  
- Remove malicious forwarding rules  

### Step 4: Investigation
- Review login activity and locations  
- Identify unauthorized actions  
- Determine if additional accounts are affected  

### Step 5: Eradication and Remediation
- Remove unauthorized changes  
- Secure all affected accounts  
- Strengthen authentication controls  

### Step 6: Recovery
- Restore account access  
- Monitor activity post-incident  
- Confirm system integrity  

---

## 7. Communication
Internal communication limited to:
- Business Owner  
- Store Manager  
- Affected employees  
- IT vendor  

External communication requires approval.

---

## 8. Documentation
All incidents must be recorded in:

- artifacts/monitoring/incident-log.md  

Include:
- Date/time detected  
- Accounts affected  
- Actions taken  
- Investigation findings  
- Final resolution  

---

## 9. Lessons Learned
Review:
- Cause of compromise  
- Effectiveness of controls  
- Need for improved authentication or monitoring  

---

## 10. Related Controls

- IA-2 (Authentication)  
- AC-2 (Account Management)  
- AC-6 (Least Privilege)  
- AU-6 (Log Review)  

---

## 11. Related Documents

- Incident Response Policy  
- Phishing Playbook (IRP-001)  
- Access Control Policy  
- Acceptable Use Policy  
- Risk Register  
- Control Matrix  
