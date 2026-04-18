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
