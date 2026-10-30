# Evidence Corrections Log
Burn and Churn Coffee

---

## Purpose

Evidence is a dated record and is not silently rewritten. When a correction is unavoidable, it is logged here: what changed, why, and which alignment item (`AL-##`, see the program's `CLAUDE.md`) required it. Dates, outcomes and decisions recorded at the time stay as they were unless the entry says otherwise.

---

## 2026-10-30: Program alignment, phase 2

The internal alignment review found that early evidence used generic placeholder accounts and names that matched no one in the company roster ([people.csv](../../00-company-profile/org/people.csv)). The following corrections map them to the named employees they belonged to.

| File | Change | Reason | Item |
|---|---|---|---|
| [access/user-access-review.csv](access/user-access-review.csv) | `manager@` → `daniel.lopez@`; `barista1@` → `ethan.brooks@`; `barista2@` → `aiden.scott@` | Generic accounts matched no one in the roster. `barista2@` (last login 2026-01-15, "Review Required") is the terminated employee found in the Q1 review (IAM:F-001); `barista1@` is the employee without Google MFA (IAM:F-004) | AL-01, AL-18 |
| [access/user-access-review.csv](access/user-access-review.csv) | Daniel Lopez: Google Workspace `Admin / Privileged` → `User / Standard`; Toast POS `Admin / Privileged` → `Manager / Standard` | Contradicted the detailed Q1 access matrix in the IAM Access Review Lab, which records the Owner as the only Google Workspace Super Admin and the Store Manager with standard and Manager roles. The detailed review is the more reliable source | AL-04 |
| [access/mfa-status.csv](access/mfa-status.csv) | Generic accounts mapped as above; MFA values unchanged | Same as AL-01. Where this file disagrees with the IAM matrix (Ethan Brooks, Aiden Scott), this file is kept as the record and the matrix is corrected in the IAM lab | AL-01, AL-12, AL-18 |
| [training/security-training-log.csv](training/security-training-log.csv) | Rebuilt from the roster: all 20 active store staff. Daniel Lopez completed 2026-01-10; everyone else not completed | The previous names (John Smith, Jane Doe, Alex Carter) exist nowhere in the company. The completion pattern reflects POAM-002 (no formal training program yet): the single 2026-01-10 completion is kept and attributed to the Store Manager, who leads training (see the RACI in [roles.md](../../00-company-profile/org/roles.md)) | AL-02 |
| [monitoring/incident-log.md](monitoring/incident-log.md) | Incidents renamed `INC-001`, `INC-002`; generic accounts mapped; INC-002 linked to IAM:F-001 | Program ID format ([identifiers.md](../../00-company-profile/org/identifiers.md)) and roster alignment | AL-01, AL-18 |

---

*This document is a simulation for educational and portfolio purposes only.*
