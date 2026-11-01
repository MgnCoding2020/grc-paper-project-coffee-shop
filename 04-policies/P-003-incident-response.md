# Incident Response Policy (IRP)

Burn and Churn Coffee

-----------------------------------------------------

## Document Control
**Policy Owner:** Business Owner
**Approved By:** Business Owner
**Effective Date:** February 2026
**Review Frequency:** Annual or following a major incident
**Version:** 1.2

------------------------------------------------------

## 1. Purpose
The purpose of this Incident Response Policy is to establish a structured and consistent approach for identifying, responding to, and recovering from cybersecurity incidents affecting Burn and Churn Coffee systems, devices, and business operations.

Effective incident response helps the organization:
  - Minimize operational disruption
  - Protect customer and business information
  - Reduce financial and reputational impact
  - Restore system safely and efficiently
  - Improve security controls through lessons learned

--------------------------------------------------------

## 2. Scope
This policy applies to all individuals who interact with Burn and Churn Coffee technology systems, including:
  - Business Owner
  - Store Managers
  - Shift Leaders
  - Employees
  - Authorized third-party IT vendors

Systems and services covered by this policy include:
  - Toast POS systems and administrative portal
  - Google Workspace email and administrative console
  - Company-issued tablets and operational devices
  - Network infrastructure (router, firewall, Wi-Fi access points)
  - Staff Wi-Fi network

This policy addresses **cybersecurity and technology-related incidents**. Broader operational disruptions such as natural disasters or extended power outages are managed under **Business Continuity procedures** where applicable (see the [Contingency and Outage Plan, PR-005](../05-procedures/PR-005-contingency-plan.md)). 

------------------------------------------------------

## 3. Definition of a Security Incident
A **Security incident** is any event that compromises, or has the potential to compromise, the **confidentiality, integrity, or availability** of Burn and Churn Coffee systems, data, or operations.

Examples include:
  - Phishing email resulting in account compromise
  - Unauthorized refunds or suspicious POS activity
  - Malware infection on a company device
  - Loss or theft of company-issued device
  - Unauthorized access to payroll or administrative accounts
  - Network intrusion or unauthorized configuration changes
  - Vendor-reported security incidents affecting company systems
  - Suspicious login activity or account misuse
Events that may appear minor should still be reported so they can be evaluated appropriately.

-----------------------------------------------------------

## 4. Roles and Responsibilities

### **Business Owner**
The Business Owner provides executive oversight during security incidents and is responsible for:
  - Approving major containment or recovery actions
  - Authorizing external communications and notifications
  - Coordinating with vendors or external parties if necessary
  - Approving policy or control changes following incidents
### Store Manager
The Store Manager serves as the primary incident response coordinator and is responsible for:
  - Receives incident reports from employees
  - Performing initial incident assessment
  - Initiating containment actions where appropriate
  - Escalates significant incidents to the Business Owner
  - Coordinating response activities with vendors
### Shift Leader
Shift Leaders assist with immediate response actions and operational continuity, including:
  - Supporting containment activities
  - Helping maintain store operations when systems are disrupted
  - Ensuring employees follow response instructions
### Employees
All employees play an important role in incident detection and are responsible for:
  - Promptly reporting suspected security incidents
  - Following instructions from management during response activities
  - Avoiding unauthorized attempts to investigate or fix incidents
### IT Vendor (if applicable)
Authorized IT vendors may assist with:
  - Technical containment actions
  - Malware removal and system remediation
  - Investigation and system restoration
  - Security recommendations following incidents

--------------------------------------------------------------

## 5. Incident Severity Classification
Incidents shall be categorized based on business impact and risk level.
### Low Severity
Incidents with minimal impact to operations and no confirmed data exposure.
Examples may include:
  - Suspicious email reported by an employee
  - Minor device malfunction with no security impact
### Medium Severity
Incidents that disrupt systems or involve suspicious activity requiring investigation.
Examples may include:
  - Temporary system disruption
  - Suspicious login attempts
  - Possible unauthorized access
### High Severity
Incidents that significantly impact operations, financial security, or sensitive data.
Examples include:
  - Confirmed data breach
  - Compromised administrative account
  - Financial fraud or unauthorized refunds, including money sent to a fraudster (IRP-007)
  - Any ransomware (IRP-005)
  - A vendor breach exposing card data, staff personal data or admin credentials (IRP-006)
  - Extended system outage affecting sales operations

High-severity incidents must be escalated immediately to the Business Owner.

---------------------------------------------------------------

## 6. Incident Response Lifecycle
Burn and Churn Coffee follows the lifecycle below. It lines up with the NIST Cybersecurity Framework 2.0 functions, which [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) (April 2025) uses to organise incident response. The playbooks (§6.7) use the CSF function names for their steps.

| Lifecycle step (this policy) | CSF 2.0 function |
|---|---|
| 6.1 Preparation | Govern, Identify, Protect |
| 6.2 Identification | Detect |
| 6.3 Containment, 6.4 Eradication | Respond |
| 6.5 Recovery | Recover |
| 6.6 Lessons Learned | Identify (improvement) |

### 6.1 Preparation
Preparation activities help ensure the organization can respond effectively to incidents.
These activities include:
  - Maintain updated contact information for personnel and vendors
  - Ensure system logging and monitoring are enabled where feasible
  - Maintaining current security policies and procedures
  - Conduct periodic incident response discussions or tabletop exercises
### 6.2 Identification
Identification involves detecting and evaluating potential incidents.
During this stage:
  - Employees report suspicious activity
  - Managers assess whether an event qualifies as a security incident
  - The severity level is assigned
  - Relevant systems and accounts are identified
### 6.3 Containment
Containment actions aim to prevent the incident from spreading or causing further harm.
Examples include:
  - Disable compromised accounts
  - Disconnect affected devices from the network
  - Temporarily restricting system access
  - Preserving logs or other evidence for investigation
### 6.4 Eradication
Eradication focuses on removing the root cause of the incident.
Actions may include:
  - Removing malware or malicious software
  - Resetting passwords and authentication credentials
  - Correcting security misconfigurations
  - Applying patches or updates
### 6.5 Recovery
Recovery restores systems and operations to a safe and stable state.
This may include:
  - Reconnecting restored systems to the network
  - Validating that security controls are functioning properly
  - Monitoring for recurring suspicious activity
  - Returning systems to normal business operations
### 6.6 Lessons Learned
Following medium or high-severity incidents, a review shall be conducted to identify improvements.
The review should include:
  - Root cause analysis
  - Impact assessment
  - Effectiveness of the response actions
  - Recommended improvements to controls or procedures

### 6.7 Playbooks
Each playbook applies this lifecycle to one kind of incident:

| Playbook | Incident |
|---|---|
| [IRP-001](../06-incident-playbooks/IRP-001-phishing.md) | Phishing |
| [IRP-002](../06-incident-playbooks/IRP-002-account-compromise.md) | Account compromise |
| [IRP-003](../06-incident-playbooks/IRP-003-pos-suspicious-activity.md) | POS suspicious activity or tampering |
| [IRP-004](../06-incident-playbooks/IRP-004-lost-stolen-device.md) | Lost or stolen device |
| [IRP-005](../06-incident-playbooks/IRP-005-malware-ransomware.md) | Malware and ransomware |
| [IRP-006](../06-incident-playbooks/IRP-006-vendor-breach.md) | A vendor reports a breach |
| [IRP-007](../06-incident-playbooks/IRP-007-payment-payroll-fraud.md) | Payment and payroll fraud (business email compromise) |

The plan and the playbooks are exercised in a tabletop at least once a year, with the contingency plan ([PR-005](../05-procedures/PR-005-contingency-plan.md)), and updated afterwards.

--------------------------------------------------------------

## 7. Reporting and Escalation
All suspected security incidents must be reported **immediately** to the Store Manager or Business Owner.
Reports may include:
  - Suspicious emails
  - Unexpected system behavior
  - Lost or stolen devices
  - Unauthorized system access
  - Unusual POS activity

High-severity incidents must be escalated immediately to the Business Owner.

Failure to report known incidents may result in disciplinary action.

-----------------------------------------------------------------

## 8. Documentation Requirements
For each confirmed incident, the following information shall be documented:
  - Date and time the incident was detected
  - The individual who reported the incident
  - Description of the event
  - Systems or accounts affected
  - Incident severity classification
  - Containment and remediation action taken
  - Final resolution
  - Estimated operational or financial impact

Incident documentation shall be retained for **at least one year** for operational and review purposes.

--------------------------------------------------------------------------

## 9. External Notification
External notifications shall be made when required by applicable law, contractual obligations, or payment processor 
requirements.
Possible notification recipients include:
  - Payment processors
  - Vendors
  - Customers
  - Regulatory authorities
  - The company's bank, **immediately**, when money has been sent to a fraudster (IRP-007)
  - Law enforcement: the FBI's [Internet Crime Complaint Center (IC3)](https://www.ic3.gov) for fraud and ransomware
  - The cyber insurer, if the company has a policy

External communications must be approved by the Business Owner before being issued.

---------------------------------------------------------------------------

## 10. Post-Incident Improvement
Following medium or high-severity incidents:
  - Security controls shall be reviewed for effectiveness
  - Policies or procedures may be updated if necessary
  - Additional employee training may be conducted
  - Preventive security measures may be implemented
---------------------------------------------------------------------------

## 11. **Enforcement**
Failure to comply with this policy may result in disciplinary action in accordance with company management procedures, up 
to and including termination of employment or contractual relationship.

---------------------------------------------------------------------------

## Revision History

| Version | Date | Change |
|---|---|---|
| 1.2 | 2026-11-01 | §6 lifecycle mapped to the NIST CSF 2.0 functions used by NIST SP 800-61 Rev. 3; §6.7 playbook index with IRP-005 to IRP-007 and a yearly tabletop; High-severity examples for ransomware, vendor breach and payment fraud; §9 adds the bank, IC3 and the insurer |
| 1.1 | Before 2026-10-30 | Earlier version (not dated) |

*This document is a simulation for educational and portfolio purposes only.*
