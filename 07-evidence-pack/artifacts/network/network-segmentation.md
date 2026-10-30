# Network Segmentation Summary

## Overview
The coffee shop maintains two separate wireless networks to support business operations and customer access.

## Network Configuration

### Business Network
- SSID: CoffeeShop-Internal
- Access: Staff only
- Connected Systems:
  - Toast POS terminals
  - Manager laptop
- Security:
  - WPA2/WPA3 password protected
  - Router admin access restricted

### Guest Network
- SSID: CoffeeShop-Guest
- Access: Public customers
- Restrictions:
  - Internet-only access
  - No access to internal systems

## Observed Gap
Network segmentation is configured at the router level, but no formal firewall rules or VLAN enforcement has been validated.

## Risk
Potential lateral movement from guest network to internal systems if misconfigured.

## Related Control
SC-7 – Boundary Protection

## Status (added 2026-10-30)
This document is the record of the current state and is unchanged above. It shows that POS terminals share the business network with the manager laptop, so the POS environment is **not** isolated from other staff devices. SC-7 is therefore **Partially Implemented**, and the remediation is tracked as **POAM-015**: separate POS, staff, guest and management segments, default deny between them, and documented allow rules, owned by the IT administrator (Vertex IT Support, then the IT Technician from CR-003).
