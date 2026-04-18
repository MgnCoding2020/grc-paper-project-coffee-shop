# IRP-001: Phishing Incident Response Playbook  
Burn and Churn Coffee

---

## Document Control
**Playbook Owner:** Business Owner  
**Approved By:** Business Owner  
**Effective Date:** March 2026  
**Review Frequency:** Annual or following a phishing-related incident  
**Version:** 1.1  

---

## 1. Purpose
This playbook provides operational guidance for responding to suspected or confirmed phishing incidents affecting Burn and Churn Coffee systems and personnel.

Phishing attacks attempt to trick employees into revealing credentials, downloading malware, or performing unauthorized actions. This playbook ensures phishing incidents are handled consistently, contained quickly, and properly documented.

---

## 2. Scope
This playbook applies to phishing incidents affecting:

- Google Workspace email accounts  
- Toast POS administrative access  
- Company-issued tablets  
- Store network accounts  

All employees, managers, and authorized IT support vendors must follow this playbook.

---

## 3. Indicators of a Phishing Incident
Phishing incidents may be suspected when:

- Suspicious emails request credentials or sensitive information  
- Unexpected password reset requests occur  
- Emails contain suspicious links or attachments  
- Employees report clicking a suspicious link  
- Unusual login alerts or unfamiliar locations are detected  
- Fraudulent or unexpected account activity is observed  

Employees must report suspicious messages immediately.

---

## 4. Severity Classification

- **Low:** Suspicious email with no interaction  
- **Medium:** Link clicked or attachment opened, no confirmed compromise  
- **High:** Credentials entered, confirmed unauthorized access, or system impact  

Severity determines escalation and response urgency.

---

## 5. Roles and Responsibilities

### Business Owner
- Oversees incident response and escalation decisions  
- Coordinates with external vendors if required  
- Approves external communication  

### Store Manager
- Serves as incident response coordinator  
- Conducts initial assessment  
- Initiates containment actions  
- Escalates as needed  

### Employees
- Report suspicious messages immediately  
- Avoid interacting with suspicious content  
- Follow response instructions  

### IT Vendor
- Assists with technical investigation and remediation  

---

## 6. Response Procedure

### Step 1: Detection and Reporting
- Employee identifies suspicious message  
- Reports to Store Manager or Business Owner  
- Do not interact further with the message  

### Step 2: Initial Assessment
- Determine if email is malicious  
- Confirm if link was clicked or credentials entered  
- Identify impacted accounts  

### Step 3: Containment
- Reset affected passwords immediately  
- Enforce or enable MFA  
- Revoke active sessions  
- Remove phishing email from inboxes if possible  
- Disable account if compromise is suspected  

### Step 4: Investigation
- Review login activity in Google Workspace  
- Identify suspicious account behavior  
- Review POS or administrative access activity  

### Step 5: Eradication and Remediation
- Remove malicious emails  
- Block malicious senders/domains  
- Reinforce phishing awareness with staff  

### Step 6: Recovery
- Restore secure account access  
- Monitor for continued suspicious activity  
- Confirm systems are functioning normally  

---

## 7. Communication
Internal communication is limited to:
- Business Owner  
- Store Manager  
- Affected employees  
- Authorized IT vendors  

External communication requires Business Owner approval.

---

## 8. Documentation
All phishing incidents must be recorded in:

- artifacts/monitoring/incident-log.md  

Include:
- Date/time of incident  
- Reporting employee  
- Description of phishing attempt  
- Actions taken  
- Systems/accounts affected  
- Resolution  

---

## 9. Lessons Learned
After an incident, review:

- Effectiveness of current controls  
- Need for additional training (AT-2)  
- Potential improvements to detection and response  

---

## 10. Related Controls

- IA-2 (Authentication)  
- AT-2 (Security Awareness Training)  
- AC-2 (Account Management)  
- AU-6 (Log Review)  

---

## 11. Related Documents

- Incident Response Policy  
- Access Control Policy  
- Acceptable Use Policy  
- Risk Register  
- Control Matrix  
