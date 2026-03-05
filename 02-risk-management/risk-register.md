# Risk Register
Burn and Churn Coffee

---

## Document Overview
This risk register identifies and tracks cybersecurity and operational technology risks that may impact Burn and Churn Coffee systems, payment processing, and business operations.

Risks are periodically reviewed by the Business Owner and Store Manager to determine appropriate mitigation actions.

---

## Risk Rating Method
Risk Levels are determined using the following scale:

| Likelihood | Description         |
| ---------- | ------------------- |
| Low        | Unlikely to occur   |
| Medium     | Possible occurrence |
| High       | Likely to occur     |

| Impact | Description                                                |
| ------ | ---------------------------------------------------------- |
| Low    | Minimal disruption                                         |
| Medium | Noticeable operational impact                              |
| High   | Significant financial, operational, or reputational damage |

The overall risk level is determined based on the combination of likelihood and impact

---

## Active Risk



| Risk ID | Asset | Threat | Vulnerability | Risk Description | Likelihood | Impact | Risk Level | Existing Controls | Risk Owner | Status |
|--------|-------|--------|---------------|------------------|-----------|--------|-----------|------------------|------------|--------|
| R-01 | Google Workspace | Phishing attack | Employee susceptibility to phishing emails | Employee falls victim to phishing email resulting in Google Workspace account compromise | Medium | High | High | MFA enabled, Acceptable Use Policy, Incident Response Plan | Business Owner | Monitoring |
| R-02 | Toast POS | Fraudulent transaction manipulation | Inadequate monitoring of transaction activity | Unauthorized refunds or POS manipulation resulting in financial loss | Medium | Medium | Medium | Access Management Policy, role-based permissions, transaction logs | Store Manager | Monitoring |
| R-03 | Company Tablets | Device theft or loss | Portable devices used outside secure storage | Loss or theft of company tablet exposing business systems | Medium | Medium | Medium | Device passcodes, Access Control Policy, Incident Response Policy | Store Manager | Monitoring |
| R-04 | Toast POS Devices | Physical device tampering | Limited physical security of POS terminals | POS terminal tampering or unauthorized device attachment | Low | High | Medium | Physical supervision of POS devices, Payment Card Data Protection Policy | Business Owner | Monitoring |
| R-05 | Network Infrastructure | Network outage or connectivity disruption | Dependence on external internet connectivity | Network outage preventing payment processing and sales | Medium | Medium | Medium | Vendor support, incident escalation procedures | Business Owner | Monitoring |
| R-06 | Google Workspace | Unauthorized account access | Misuse of administrative privileges or credential compromise | Unauthorized access to payroll or administrative accounts | Low | High | Medium | Access Management Policy, role restrictions, MFA | Business Owner | Monitoring |
| R-07 | Toast POS / Payment Processing | Vendor security breach | Dependency on third-party payment provider security | Vendor security breach impacting Toast POS payment processing | Low | High | Medium | Vendor PCI compliance, Payment Card Data Protection Policy | Business Owner | Monitoring |
| R-08 | Company Tablets | Malware infection | Unsafe browsing or software downloads | Malware infection on company tablet through unsafe browsing or downloads | Medium | Medium | Medium | Acceptable Use Policy, restricted app installation | Store Manager | Monitoring |


--------

## Risk Review Process
Risk listed in this register shall be reviewed:
  - Annually
  - Following significant technology changes
  - After any medium or high-severity security incident

During reviews, risk may be: 
  - Mitigated
  - Accepted
  - Reassessed
  - Escalated

---------------------

## Related Policies
  - Access Management Policy
  - Acceptable Use Policy
  - Incident Response Policy
  - Payment Card Data Protection Policy
