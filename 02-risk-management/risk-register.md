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

## Risk Register

| Risk ID | Risk Description | Impact | Likelihood | Inherent Risk | Controls | Residual Risk |
|--------|------------------|--------|------------|----------------|----------|----------------|
| R-01 | Phishing attack leading to account compromise | High | Medium | High | IA-2, AT-2 | Medium |
| R-02 | Unauthorized POS transactions or misuse | High | Medium | High | AC-2, AU-6 | Medium |
| R-03 | Theft or loss of POS/tablet devices | Medium | Medium | Medium | PE-3 | Medium |
| R-04 | Network-based attack due to poor segmentation | High | Low | Medium | SC-7 | Medium |
| R-05 | Internet or network outage impacting operations | Medium | Medium | Medium | CP-2 | Medium |
| R-06 | Excessive privileges leading to misuse | High | Low | Medium | AC-6 | Medium |
| R-07 | Vendor compromise or service disruption (Toast POS) | High | Low | Medium | SA-9 | Medium |
| R-08 | Malware infection on business systems | Medium | Medium | Medium | SI-3, SI-7 | Medium |
| R-09 | Cardholder data exposure due to insufficient encryption in transit or at rest | High | Medium | High | SC-8, SC-28 | High |
| R-10 | Former employees or vendors keep access after leaving, or staff keep access after changing roles | High | High | High | PS-4, PS-5, AC-2 | High |
| R-11 | Unplanned or poorly controlled changes (such as the Microsoft 365 migration or the IT handover) disrupt operations or weaken security | Medium | Medium | Medium | CM-3, CM-4 | Medium |

----

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

---

## Revision History

| Date | Change | Reason |
|---|---|---|
| 2026-10-30 | R-04 residual risk Low → Medium; R-06 residual risk Low → Medium | Program alignment review: SC-7 segmentation is not validated (POAM-015) and the Q1 access review left excess-privilege findings open (IAM:F-002, POAM-014), so the controls don't yet reduce these risks as far as recorded (AL-16, AL-19) |
| 2026-10-30 | Added R-10 (access kept after leaving or changing roles) and R-11 (uncontrolled change) | R-10 already happened (IAM:F-001, IAM:F-003); R-11 arises from CR-001 and CR-003 |
