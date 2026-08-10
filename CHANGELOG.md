# Changelog

All notable lab milestones are documented here.

## 2026-08-09

### Lesson 01 - System, Network, and Administrative Access Foundations

- Extended the Lesson 00 FortiGate with a persistent internal `LAB-LAN` on `port2`.
- Configured `port2` as `10.10.10.1/24`, alias `LAB-LAN`, role `LAN`.
- Added a FortiGate DHCP pool of `10.10.10.100-10.10.10.150`.
- Used Kali as the persistent internal administration/test workstation.
- Verified Kali received `10.10.10.100/24` dynamically and installed `10.10.10.1` as its default gateway.
- Observed and preserved the existing upstream default route on `port1` instead of creating a redundant route.
- Kept `port1` untouched because the upstream DHCP address/subnet can change with the host Wi-Fi/network.
- Enabled HTTPS, SSH, and PING on `port2` for controlled management testing.
- Created a separate `trusted-admin` account so Trusted Hosts testing could not lock out the original administrator.
- Verified successful login when the Trusted Host matched Kali at `10.10.10.100/32`.
- Verified authentication failure when the Trusted Host was changed to `10.10.10.99/32` while Kali remained `10.10.10.100`.
- Restored the final Trusted Host to `10.10.10.100/32`.
- Verified PING and SSH from Kali to the FortiGate.
- Added curated, sanitized evidence for the configuration, client behavior, routing state, and positive/negative security tests.

## 2026-08-08

### Lesson 00 - Environment Setup and Licensing

- Selected the official FortiGate x86-64 KVM new-deployment package for FortiOS 7.6.7.
- Imported `fortios.qcow2` into EVE-NG as `virtioa.qcow2`.
- Created the FortiGate node with 1 vCPU, 2048 MB RAM, and three interfaces.
- Completed first-login password setup.
- Verified FortiOS 7.6.7 build 3704 and interface state.
- Verified Internet reachability, DNS/FortiGuard reachability, and the default route.
- Recorded troubleshooting for the stalled GUI license-check page.
- Activated the permanent evaluation license through the CLI.
- Completed the post-license setup wizard.
- Reached the operational FortiOS dashboard.
- Recorded the permanent-evaluation resource, interface, policy, route, encryption, support, and FortiGuard limitations.
