# Changelog

All notable lab milestones are documented here.

## 2026-08-13

### Lesson 02 - Firewall Policies and NAT

- Preserved `port1` strictly as the protected management/recovery path and moved all transit experiments to `port2`/`port3`.
- Configured `port3` as `10.20.20.1/24`, alias `externalToAlpine`, role `WAN`, with no administrative access and no FortiGate DHCP service.
- Added lightweight Alpine Linux as the controlled outside host at `10.20.20.100/24` on a dedicated lab NIC.
- Kept Alpine's normal Internet/default route on its separate DHCP NIC and added only `10.10.10.0/24 via 10.20.20.1` for the FortiGate lab.
- Proved the implicit deny by showing Kali could route toward Alpine through its existing default gateway but could not transit FortiGate before a matching policy existed.
- Created `Lab-To-Outside` as the first `port2 -> port3` transit policy.
- Verified FortiGate stateful behavior: replies to a Kali-initiated session returned without a reverse policy, while a new Alpine-initiated session toward Kali remained blocked.
- Created and tested `KALI-CLIENT` and `ALPINE-OUTSIDE` address objects.
- Proved source matching with a correct `/32` and a deliberately wrong source object.
- Proved destination matching with a correct `/32` and a deliberately wrong destination object.
- Proved service matching by allowing `PING` and then showing the same ICMP flow fail when the policy service was changed to `SSH`.
- Created temporary `DENY-LAB-OUTSIDE` Policy ID `2` and proved first-match processing against `Lab-To-Outside` Policy ID `1`.
- Verified that moving policies changes sequence/precedence without changing their Policy IDs.
- Captured Forward Traffic logs showing accept by Policy ID `1` and deny by Policy ID `2` for the same source/destination flow.
- Studied flow-based versus proxy-based inspection and retained flow-based mode instead of creating an artificial proxy-inspection test.
- Validated outgoing-interface SNAT: Alpine observed source `10.20.20.1` instead of the internal Kali address.
- Created overload pool `SNAT-OVERLOAD` at `10.20.20.200` and proved translation with `tcpdump` on Alpine.
- Added Metasploitable to `LAB-LAN`; it obtained `10.10.10.101/24` and was represented by address object `MSF-CLIENT`.
- Expanded the existing outbound policy to include both Kali and Metasploitable instead of creating a redundant equivalent policy.
- Created one-to-one pool `SNAT-OneToOne`, extended it to `10.20.20.210-10.20.20.211`, and proved simultaneous multi-host translations with packet capture.
- Validated the Metasploitable HTTP backend locally before introducing DNAT.
- Created static VIP `MSF-WEB-VIP`: `10.20.20.220 -> 10.10.10.101`.
- Created inbound `OUTSIDE-to-MSF-WEB` policy from `port3 -> port2`, using the VIP object as destination and leaving policy SNAT disabled.
- Verified Alpine could retrieve the internal Metasploitable HTTP page through `10.20.20.220`.
- Created port-forward VIP `MSF-Web_PORTFWD`: `10.20.20.221:8080 -> 10.10.10.101:80`.
- Expanded the inbound policy to include both VIP objects instead of creating another equivalent inbound rule.
- Verified Alpine could retrieve the backend page through external TCP/8080.
- Proved VIP policy matching by replacing the VIP destination with the real backend object, observing failure, then restoring the VIP and recovering access.
- Recorded the design insight that one external IP can publish multiple internal services when distinct external ports uniquely identify the mappings.
- Deliberately skipped a separate outgoing static-NAT example because outbound source translation had already been demonstrated more meaningfully through outgoing-interface and IP-pool scenarios.
- Added curated, sanitized evidence for policy matching, Policy ID/sequence, logging, SNAT, IP pools, static VIP DNAT, and port forwarding.

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
