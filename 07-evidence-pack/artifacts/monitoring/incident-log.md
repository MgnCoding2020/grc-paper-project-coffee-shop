# Incident Log

## INC-001 (formerly Incident 001) – Suspicious Login Attempt

- Date: 2026-03-12
- System: Google Workspace
- User: daniel.lopez@burnandchurncoffee.com
- Description:
  A login attempt was detected from an unrecognized location.

- Action Taken:
  - Password reset enforced
  - User notified
  - MFA verified as active

- Status:
  Resolved

---

## INC-002 (formerly Incident 002) – POS Account Inactivity

- Date: 2026-03-20
- System: Toast POS
- User: aiden.scott@burnandchurncoffee.com

- Description:
  Account inactive for over 60 days but still active in system.

- Action Taken:
  - Flagged during access review
  - Pending account disable

- Status:
  Open

- Related: the Q1 2026 access review found the same account belongs to a terminated employee (IAM:F-001); remediation is tracked under POAM-014.

---

## Corrections

- **2026-10-30:** incident IDs renamed to the program format (`INC-###`); generic accounts replaced with the named employees they belonged to (`manager@` → Daniel Lopez, `barista2@` → Aiden Scott); INC-002 cross-referenced to IAM:F-001. Dates, descriptions and actions are unchanged. See [CORRECTIONS.md](../CORRECTIONS.md) (alignment items AL-01, AL-18).
