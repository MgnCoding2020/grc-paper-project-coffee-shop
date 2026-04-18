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
| Risk ID | Asset                          | Threat                              | Vulnerability                                 | Risk Description                                                        | Inherent Likelihood | Inherent Impact | Inherent Risk | Controls Implemented                                              | Residual Likelihood | Residual Impact | Residual Risk | Evidence / Scripts                                                                | Risk Owner     | Status     |
| ------- | ------------------------------ | ----------------------------------- | --------------------------------------------- | ----------------------------------------------------------------------- | ------------------- | --------------- | ------------- | ----------------------------------------------------------------- | ------------------- | --------------- | ------------- | --------------------------------------------------------------------------------- | -------------- | ---------- |
| R-01    | Google Workspace               | Phishing attack                     | Employee susceptibility to phishing emails    | Employee falls victim to phishing email resulting in account compromise | Medium              | High            | High          | MFA (IA-2), Security Awareness Training, Acceptable Use Policy    | Low                 | Medium          | Low           | mfa_review_check.py, mfa-status.csv                                               | Business Owner | Monitoring |
| R-02    | Toast POS                      | Fraudulent transaction manipulation | Inadequate monitoring of transaction activity | Unauthorized refunds or manipulation of POS transactions                | Medium              | Medium          | Medium        | Role-Based Access (AC-2), Transaction Logging (AU-6)              | Low                 | Medium          | Low           | (manual logs / POS reports)                                                       | Store Manager  | Monitoring |
| R-03    | Company Tablets                | Device theft or loss                | Portable devices used outside secure storage  | Loss or theft of tablet exposing business systems                       | Medium              | Medium          | Medium        | Device Passcodes, Access Control Policy, Incident Response Policy | Low                 | Low             | Low           | (policy + incident logs)                                                          | Store Manager  | Monitoring |
| R-04    | Toast POS Devices              | Physical device tampering           | Limited physical security of POS terminals    | Unauthorized physical access or tampering with POS hardware             | Low                 | High            | Medium        | Physical Security Controls, Payment Card Data Protection Policy   | Low                 | Medium          | Low           | incident-log.md                                                                   | Business Owner | Monitoring |
| R-05    | Network Infrastructure         | Network outage                      | Dependence on external internet connectivity  | Network disruption impacting payment processing and business operations | Medium              | Medium          | Medium        | Vendor Support SLA, Incident Response Plan                        | Medium              | Low             | Low           | incident_log_review_check.py                                                      | Business Owner | Monitoring |
| R-06    | Google Workspace               | Unauthorized account access         | Privilege misuse or credential compromise     | Unauthorized access to administrative accounts                          | Low                 | High            | Medium        | MFA (IA-2), Least Privilege (AC-6), Access Reviews                | Low                 | Medium          | Low           | access_review_check.py, privileged_access_review_check.py, user-access-review.csv | Business Owner | Monitoring |
| R-07    | Toast POS / Payment Processing | Vendor breach                       | Dependency on third-party provider security   | Vendor compromise impacting payment processing                          | Low                 | High            | Medium        | Vendor Risk Assessment, PCI Compliance Validation                 | Low                 | Medium          | Low           | vendor assessment documentation                                                   | Business Owner | Monitoring |
| R-08    | Company Tablets                | Malware infection                   | Unsafe browsing or downloads                  | Malware infection impacting device security                             | Medium              | Medium          | Medium        | Acceptable Use Policy, Application Restrictions                   | Low                 | Medium          | Low           | (policy enforcement evidence)                                                     | Store Manager  | Monitoring |


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
