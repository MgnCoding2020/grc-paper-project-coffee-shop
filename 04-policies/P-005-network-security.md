# Network Security Policy
Burn and Churn Coffee

## Document Control
**Policy Owner:** Business Owner | 
**Approved by:** Business Owner | 
**Effective Date:** 2026-10-30 | 
**Review Frequency:** Annual, or upon any change to the store network | 
**Version:** 1.0

----------

## 1. Purpose
This policy sets the security requirements for Burn and Churn Coffee's store network: how it is divided into segments, what traffic is allowed between them, how wireless networks are protected, and how network equipment is administered and changed.

Its main goal is to keep payment terminals isolated from everything else, so a compromised laptop, phone or guest device cannot reach the systems that handle card payments. It implements NIST SP 800-53 **SC-7 (Boundary Protection)** and supports PCI DSS Requirement 1 (network security controls).

-----------

## 2. Scope
This policy applies to:
  - The store network (SYS-007): router, firewall/gateway, Wi-Fi access points and every network segment (assets NET-001 to NET-005)
  - Every device that connects to it, including Toast POS terminals, company tablets, the manager laptop, staff personal devices and customer devices
  - Everyone who administers or uses the network: the IT administrator, staff, vendors and customers

-----------

## 3. Network Segmentation
The store network is divided into four segments:

| Segment | Who connects | Allowed traffic |
|---|---|---|
| **POS** (wired where possible) | Toast POS terminals only | Outbound to Toast services only; nothing inbound from other segments |
| **Staff** | Company-managed devices | Internet and Microsoft 365; no access to the POS or management segments |
| **Guest** | Customers and personal devices | Internet only; devices cannot see each other (client isolation); bandwidth limited; terms page |
| **Management** | Router, firewall, access points | Administration only, from the IT administrator's device |

Rules:
  - Traffic between segments is **denied by default**. Every allowed flow is written down with its business reason.
  - Personal devices never connect to the POS or management segments.
  - Payment terminals connect only to the POS segment.

-----------

## 4. Wireless Networks
  - Staff Wi-Fi uses WPA3 (or WPA2 where a device requires it) with a strong passphrase that is not shared with customers.
  - The staff Wi-Fi passphrase is changed **whenever someone who knows it leaves the company** (see the joiner/mover/leaver process, PR-001) and at least once a year.
  - Guest Wi-Fi is a separate network with client isolation and no route to internal segments.
  - Unauthorized access points and hotspots connected to the company network are prohibited (Acceptable Use Policy, P-002).

-----------

## 5. Network Equipment Administration
  - Each administrator uses a **named account**; shared or default administrator accounts are not allowed.
  - Vendor default passwords and settings are changed before a device goes into service (secure configuration, CM-6).
  - Administration happens only from the management segment or the IT administrator's device, over encrypted connections, with MFA where the device supports it.
  - Administrative logging stays enabled where supported (Access Management Policy, P-001 §5.10).
  - Firmware and security updates follow the patch and vulnerability procedure (PR-002).
  - Vendor remote access follows P-001 §5.7: named individuals, least privilege, time-limited.

-----------

## 6. Changes and Reviews
  - Changes to firewall rules, segments or Wi-Fi settings follow the change management process (CM-3), with a change record for significant changes.
  - Firewall rules and segmentation are reviewed **at least every six months**, and segmentation is tested after any network change (see the continuous monitoring strategy).

-----------

## 7. Current Exceptions
As of the effective date, the store network does **not** yet meet section 3: Toast POS terminals share the business Wi-Fi with the manager laptop, and no firewall rules or segment enforcement have been verified. This is recorded as **POAM-015** (SC-7, Partially Implemented), approved by the Owner as a time-limited exception until the IT administrator implements and validates the segments in section 3.

-----------

## 8. Enforcement
Failure to comply with this policy may result in disciplinary action in accordance with company management procedures, up to and including termination of employment or contractual relationship. Unauthorized devices may be disconnected without notice.

-------------

## 9. Related Documents
  - [Access Management Policy (P-001)](P-001-access-control.md)
  - [Acceptable Use Policy (P-002)](P-002-acceptable-use.md)
  - [Payment Card Data Protection Policy (P-004)](P-004-payment-card-data-protection.md)
  - [Patch and Vulnerability Management Procedure (PR-002)](../05-procedures/PR-002-patch-vuln-management.md)
  - [Network segmentation evidence](../07-evidence-pack/artifacts/network/network-segmentation.md)
  - [POA&M](../07-evidence-pack/poam/poam.md) (POAM-015)

-------------

*This document is a simulation for educational and portfolio purposes only.*
