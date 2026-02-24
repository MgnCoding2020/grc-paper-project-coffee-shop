Access Management Policy                              
Burn and Churn Coffee

Document Control
  •  **Policy Owned:** Business Owner
  •  **Approved By:** Business Owner
  •  **Effective Date:** 2026-02-01
  •  **Last Reviewed/Updated:** 2026-02-23
  •  **Review Frequency:** Annual (or upon significant change to systems or roles)
  •  **Version:** 1.1
    

**1. Company Context**
Burn and Churn Coffee uses a small set of cloud and on-site systems to operate daily business functions and store business and customer information. This polic applies to the following system and business and administrative interfaces:
  •  **Toast POS** (point-of-sale devices and administrative portal)
  •  **Google Workspace** (email, share drive content and admin console)
  •  **Company-issued tablets** used for inventory, order, and business operations
  •  **Staff netowrking infrastructure** (router, firewall, Wi-Fi access points, and any network management interfaces)
**Out of Scope:** Guest Wi-Fi user identity controls. Guest Wi-Fi access is not provisioned via individual user accounts; however, guest network access is governed by network segmentation, configuration, and monitoring controls under the **Network/Wireless Security Policy.**

**2. Purpose**

The purpose of this policy is to ensure that access to Burn and Churn Coffee systems and data is authorized, appropriate, and managed throughout the user lifecycle (joiner, mover, leaver). 

Burn and Churn Coffee will limit access to systems and data to authorized individuals based on job responsibilities, using the principles of least privliege and separation of duties to reduce the risk of unauthorized access, fraud, data exposure, or operational disruption. 

This policy establishes requirements for: 
  •  Account provisioning and approval
  •  Role assignment and changes
  •  Authentication and credential management
  •  Privileged (administrative) access
  •  Third-party/vendor access
  •  Periodic access reviews
  •  Access revocation and termination handling
  •  Logging of access and administrative changes
  

**3. Scope**
  
**3.1 People In Scope**
This policy applies to:
  •  All employees (full-time and part-time)
  •  Store Managers
  •  The Business Owner
  •  Authorized third-party IT support vendors who access company systems
**3.2 Systems and Access Types In Scope**
This policy governs logical access (accounts, permissions, and authentication) to:
  •  Toast POS user accounts and roles
  •  Google Workspace accounts and administrative roles
  •  Administrative access to network equipment and Wi-fi management interfaces
  •  Authentication and authorization mechanisms used by company-issues tablets
  •  Company credentials (password, MFA methods, admin accounts)
**3.3 Compliance**
Compliance with this policy is mandatory. Exceptions require documents approval by the Business Owner and must include a defined expiration date and compensating controls where applicable.
**4. Definitions**
  •  **Least Privilege:** Users receive only the access needed to perform their assigned job duties.
  •  **Separation of Duties:** Critical tasks are devided so no single person can complete a high-risk action alone (where feasible).
  •  **Privileged Account:** An account with administrative capabilities (e.g., admin console access, ability to create users, change permissions, or modify-security settings).
  •  **Joiner/Mover/Leaver:** A user who is newly hired (joiner), changes roles (mover), or leaves the company (leaver).


**5. Safeguards**

**5.1 Role Definitions and Access Model**
  **1.** Burn and Churn Coffee shall define and maintain documented user roles for systems within scope (Toast POS, Google Workspace, tablets, and network infrastucture).
  **2.** Roles shall be assigned based on job responsibilities and shall follow least privilege.
  **3.** Separation of duties shall be implemented where feasible, especially for high-risk actions (e.g., refunds, pay/HR access, admin changes).
  **4.** Administrative privileges shall be limited to the Business Owner and explicitly authorized management personnel.
**5.2 Account Provisioning (joiners)**
  **1.** All user accounts shall be uniquely assigned to an individual (no shared accounts), unless a documented exception is approved by the Business Owner.
  **2.** Access shall be provisioned only after documented approval by the user's manager or the Business Owner.
  **3.** New accounts shall be assigned the minimum required role(s) for the individual's job duties.
  **4.** Provisioning actions shall be recorded in a retrievable format (e.g., email approval, ticket, or access request form).
**5.3 Access Changes (Movers)**
  **1.** When a user changes roles or job responsibilities, access rights shall be reviewed and updated to match the new role.
  **2.** Role and permission changes shall be completed within **3 business days** of the role change being approved or effective (whichever is sooner).
  **3.** Access that is no longer required shall be removed as part of the change.
**5.4 Access Revocation (Leavers)**
  **1.** When employment ends, access to Google Workspace, Toast POS, and network administrative interfaces shall be disabled or removed **no later than 24 hours** after separation.
  **2.** For involuntary or high-risk terminations, access shall be disabled **immediately upon notification** of termination or at the time of termination, whichever is earlier.
  **3.** Company-issued devices shall be recovered where feasible. If devices are not recovered promptly, accounts associated with the device shall be disabled and remote wipe shall be performed where supported.
**5.5 Authentication and Credential Requirements**
  **1.** Passwords shall be kept confidential and shall not be shared between individuals.
  **2.** Multi-factor authentication (MFA) shall be enabled for:
      • All Google Workspace administrative accounts (required)
      • All Google Workspace user accounts where supported and feasible (strongly recommended; required if handling sensitive business data)
  **3.** Privileged accounts shall use stronger authentication than standard accounts where possible (e.g., MFA enforced, separate admin accounts).
**5.6 Privileged (Administrative) Access Controls**
  **1.** Privileged access shall be restricted to designated personnel and approval by the Business Owner.
  **2.** Privileged access shall be used only for administrative tasks and not for routine daily operations where feasible.
  **3.** Privileged access shall be reviewed during quaterly access reviews.
  **4.** Administrative changes (user creation, permission changes, group membership changes) shall be logged where supported.
**5.7 Third-Party / Vendor Access**
  **1.** Third-party vendors shall be granted access only when required for business purpose and only with Business Owner approval.
  **2.** Vendor access shall be:
      • Assigned to named individuals (no generic vendor accounts) where supported
      • Limited to least privilege
      • Time-bound whenever feasible (access removed after work is completed)
  **3.** Vendor access shall be reviewed during quarterly access reviews and removed when no longer required.
**5.8 Secure Access and Encryption**
  **1.** Administrative access to Toast POS, Google Workspace, and network equipment shall occur over encrypted connections (HTTPS/TLS) whenever available.
  **2.** Company-issued tablets shall use device-level encryption where supported.
  **3.** For hosted SaaS systems (Toast POS, Google Workspace), Burn and Churn Coffee relies on vendor-managed encryption controls for data in transit and at rest.
**5.9 Access Reviews (Quarterly)**
  **1.** Burn and Churn Coffee shall perform access reviews **quarterly** for:
      • Toast POS user accounts and roles
      • Google Workspace accounts, groups, and administrative roles
      • Network equipment administrative accounts
  **2.** Access reviews shall verify:
      • Former employees do not retain access
      • Privileged access is limited and appropriate
      • Role assignments match current job responsibilities
  **3.** Reviews results shall be documented and retained for at least **one year**.
**5.10 Logging and Monitoring of Access Changes**
  **1.** Administrative actions affecting access (user creation, role changes, group membership shanges) shall be logged where supported.
  **2.** Administrative logging shall remain enabled on network equipment where technically feasible. If logging is not feasible, the Business Owner shall document the limitation and implement compensating controls (e.g., stricter access restrictions, more frequent reviews).
  **3.** Logs shall be reviewed during quarterly access reviews and following suspected security incidents.
To achieve the organization's overall mission, and the purpose of this cybersecurity policy, the organization shall: 
The organization shall define and document user roles for all systems in the scope, including Toast POS, Google Workspace, company tablets, and network infrastructure.
Roles shall be assigned based on job responsibilities. 
The organization shall implement separation of duties where feasible to prevent unauthorized or fraudulent activity.
Administrative privileges shall be restricted to the Owner and authorized management personnel only.

The organization shall maintain documented records of user access and role assignments within:
  •  "Toast POS administrative portal"
  •  "Google Workspace administrative console"
  •  "Network equipment administrative interfaces"
Access permissions shall be based on documented roles and the principle of least privilege.
Access to administrative interfaces shall be limited to authorized personnel.
AM-07: Not applicable. The organization does not maintain internal software development repositories.

Company-issued tablets shall utilize device-level encryption where supported.
All administrative access to Toast POS, Google Workspace, and network equipment shall occur over encrypted connections (HTTPS/TLS).
The organization relies on vendor-managed encryption controls for hosted SaaS systems such as Toast POS and Google Workspace.

The organization shall conduct quarterly access reviews of: 
  •  "Toast POS user accounts and role assignments"
  •  "Google Workspace accounts and administrative roles"
  •  "Network equipment administrative access"
Access reviews shall verify that:
  •  "Former employees no longer retain access"
  •  "Access privileges remain appropriate to job responsibilities"
Documentation of access reviews shall be retained for audit purposes. 

Admnistrative changes to user roles, permissions, and groups memberships within Toast POS and Google Workspace shall be logged where supported.
Administrative logging shall remain enabled on network equipment where technically feasible.
Logs shall be reviewed during scheduled access reviews or following suspected security incidents.

###Policy Sanctions###
Failure to comply with the policy may result in disciplinary action, up to and including termination of employment or contractual relationship. 
Violations may also result in the suspension of system access privileges while investigations are conducted.
Where applicable, violations involving illegal activity may be referred to appropriate authorities.
All enforcement actions shall be applied consisyently and in accordance with company management procedures. 

