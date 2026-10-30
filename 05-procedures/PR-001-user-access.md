# User Access Management Procedure
Burn and Churn Coffee

-----

## 1. Purpose
The purpose of this procedure is to define the process for requesting, approving, granting, modifying, and removing user access to company systems and data used by **Burn and Churn Coffee**.

This procedure ensures that access to company systems is granted according to job responsibilities, follows the principle of least privilege, and is removed promptly when no longer required.

-----

## 2. Scope 
This procedure applies to all Burn and Churn Coffee employees, contractors, and third-party vendors who require access to company information systems.

Systems covered by this procedure include, but are not limited to:
  - Google Workspace (email, Drive, administration)
  - Toast POS system
  - xtraCHEF inventory and supplier management platform
  - QuickBooks Online accounting platform
  - Store Wi-Fi and network resources
  - Company-managed devices and tablets

-----

## 3. Roles and Responsibilities
### Store Owner / Management
  - Approves system access requests
  - Ensures employees only receive access required for their job duties
  - Reviews access during periodic access reviews

### IT Administrator (Vertex IT Support until 2026-11-15, then the IT Technician)
  - Creates, modifies, and removes system accounts
  - Maintains access control configurations
  - Documents account provisioning activities

### Supervisors / Managers
  - Submit access requests for employees
  - Notify administration of role changes
  - Notify administration when employees leave the company

### Employees 
  - Use system access only for authorized business activities
  - Protect login credentials
  - Report suspected unauthorized access or account compromise

-----

## 4. Access Provisioning Process
  1. A supervisor or manager submits a request for system access for a new employee.
  2. The request must include:
     - Employee name
     - Job role
     - Required systems
     - Level of access required
  3. Management reviews and approves the request.
  4. The IT administrator creates the necessary accounts in applicable systems, such as:
     - Google Workspace
     - Toast POS
     - xtraCHEF
     - QuickBooks Online (if applicable)
  5. Default security settings must be applied when accounts are created, including:
     - Strong password requirements
     - Multi-factor authentication, where supported
     - Least-privilege role assignments
  6. The IT administrator documents account creation in the access tracking records.

-----------

## 5. Access Modification
Access must be reviewed and updated when:
  - An employee changes job roles
  - Additional responsibilities require expanded system access
  - Access to certain systems is no longer required

Managers must submit a request to the IT administrator to change access. 
All access modifications must be approved before implementation, and completed **within 3 business days** of the role change being approved or taking effect, whichever is sooner (P-001 §5.3). Access the new role no longer needs is removed as part of the same change.

-------

## 6. Access Removal (Deprovisioning) 
When an employee or contractor leaves the organization, access must be removed promptly.

The following steps must be completed:
  1. The supervisor notifies the IT administrator of employee departure.
  2. The IT administrator disables or removes the user accounts from all systems, including:
     - Google Workspace
     - Toast POS
     - xtraCHEF
     - QuickBooks Online
     - Network access
     - The employee's personal Toast POS PIN
  3. Any company devices assigned to the employee must be returned.
  4. The staff Wi-Fi passphrase is changed if the employee knew it (Network Security Policy, P-005 §4).
  5. Access removal activities must be documented in the access tracking records, with the employee's end date recorded in the staff roster (`people.csv`).

Access must be disabled **no later than 24 hours after separation**, and **immediately** for involuntary or high-risk terminations (P-001 §5.4).

-----

## 6a. Vendor Access

Vendor access follows P-001 §5.7: named individuals only, least privilege, time-bound.

  1. Each vendor contact who needs access is listed in the vendor contacts register (`vendor-contacts.csv`) with a sponsor (the Owner) and an access end date.
  2. Access is granted only through a change record (for example, CR-004) and only to the vendor group (`grp-bc-vendors`).
  3. On or before the end date, the IT administrator removes the access, and the removal is recorded in the register.
  4. Vendor access is checked in every quarterly access review (PR-003).

## 7. Emergency Access
In limited situations, temporary administrative or elevated access may be required to resolve operational issues.

Emergency access must:
  - Be approved by management
  - Be documented
  - Be removed immediately after the issue is resolved

-----

## 8. Logging and Documentation
The following activities must be documented:
  - New account creation
  - Access modifications
  - Accounts removal
  - Administrative access assignments

Documentation may include access request forms, checklists, or system logs.

These records serve as evidence that access control procedures are being followed.

-----

## 9. Procedure Review
This procedure should be reviewed annually or when significant changes occur to company systems or access control practices.

------------------

## 10. Related Documents
- [Access Management Policy](../04-policies/P-001-access-control.md)
- [Asset Inventory](../01-asset-inventory/assets.md)
- [Data Classification Standard](../01-asset-inventory/data-classification.md)
- [Risk Register](../02-risk-management/risk-register.md)
- [Control Matrix](../03-controls/control-matrix.md)
- [Evidence Matrix](../07-evidence-pack/evidence-matrix.md)

---

## Revision History

| Date | Change | Reason |
|---|---|---|
| 2026-10-30 | Removal deadline aligned with P-001 §5.4 (24 hours; immediately for involuntary terminations), replacing "last working day"; 3-business-day deadline for role changes (P-001 §5.3); Toast PIN and staff Wi-Fi passphrase added to removal; vendor access section; role naming | Story-level alignment review found the procedure contradicted the policy (AL-27) |
