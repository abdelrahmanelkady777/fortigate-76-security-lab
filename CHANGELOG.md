# Changelog

All notable lab milestones are documented here.

## 2026-08-15

### Lesson 03 - Routing, Static Routes, and ECMP

- Converted the directly attached Lesson 02 outside segment into a routed topology while preserving Alpine's established `10.20.20.100/24` address.
- Added `10.30.30.0/24` as the FortiGate-R1 transit network instead of reusing Alpine's endpoint subnet as a transit link.
- Corrected an Alpine address that had been created as `/32`, documented that Linux `ip addr` expects CIDR prefix notation, and brought eth1 administratively up.
- Configured R1 Gi0/0 as `10.20.20.1/24` and Gi0/1 as `10.30.30.2/24`.
- Added R1's return route to `10.10.10.0/24` through FortiGate at `10.30.30.1`.
- Added Alpine routes to LAB-LAN and the R1-FortiGate transit through `10.20.20.1`.
- Readdressed FortiGate port3 as `TRANSIT-R1` at `10.30.30.1/24`.
- Validated the lower path in layers: same-subnet adjacency, R1 forwarding, FortiGate static route, FortiGate-originated ping, then client transit.
- Configured the intermediate FortiGate route to `10.20.20.0/24` through `10.30.30.2` with distance `10`.
- Proved that a working route does not authorize transit: FortiGate could ping Alpine while Kali failed without a matching policy.
- Restored the `Lab-to-Alpine` port2-to-port3 PING policy with NAT disabled and then verified Kali-to-Alpine reachability at TTL `62`.
- Correlated the FortiGate CLI routing table with the GUI Routing Monitor and documented `[distance/metric]` output.
- Recorded route lookup, longest-prefix match, RIB/FIB, administrative distance, metric, FortiGate priority, and reverse-path context against the live topology.
- Documented static routes with named addresses, Internet Service routing, and the GUI Route Lookup tool as studied concepts, while clearly stating why no separate lab implementation was claimed.
- Preserved the Lesson 02 VIP evidence only as historical state; the publication design was not claimed as revalidated after the port3 topology change.
- Added R2 as the second routed path and repurposed FortiGate port1 from its former management/upstream role because the evaluation permits only three interfaces.
- Configured FortiGate port1 as `R2-Port1` at `10.50.50.1/24`.
- Configured R2 Gi0/0 as `10.50.50.2/24`, Gi0/1 as `10.40.40.1/24`, and added its return route to `10.10.10.0/24` through `10.50.50.1`.
- Added Alpine eth2 at `10.40.40.100/24` and verified both Alpine routed identities.
- Installed full iproute2 on Alpine with `apk add iproute2` to support multipath `nexthop` syntax.
- Configured Alpine's equal-weight route to `10.10.10.0/24` through both R1/eth1 and R2/eth2, plus explicit routes to the two remote FortiGate transit networks.
- Used `ip route get` with bound source addresses to confirm Alpine's lower- and upper-path selection.
- Documented that Alpine ECMP and FortiGate ECMP are independent routing decisions.
- Exposed and corrected an operational error where a GUI policy draft had not been saved with **OK**.
- Reused the available three-policy budget transparently; the combined bidirectional interface policy is documented as a lab-only compromise rather than production least privilege.
- Corrected the ECMP test design after recognizing that `10.20.20.100` and `10.40.40.100` are different destinations and therefore cannot form FortiGate ECMP.
- Added Alpine loopback `10.60.60.100/32` as one shared destination reachable through either routed member.
- Added R1's `/32` route through Alpine `10.20.20.100` and R2's `/32` route through Alpine `10.40.40.100`.
- Replaced the two intermediate FortiGate remote-network routes with two equal static routes to `10.60.60.100/32`: via R1 `10.30.30.2` on port3 and via R2 `10.50.50.2` on port1.
- Confirmed both FortiGate routes were installed with distance `10`, metric `0`, and equal priority, allowing FortiGate ECMP to form automatically.
- Verified the FortiGate itself could reach the shared loopback at TTL `63`.
- Diagnosed a Kali failure with `diagnose sniffer packet`: requests appeared only as `port2 in`, identifying a firewall-policy interface mismatch before any ECMP egress occurred.
- Added port3 to the combined policy's incoming and outgoing interface lists so either ECMP member could be authorized.
- Confirmed `set v4-ecmp-mode source-ip-based` in the FortiGate system settings.
- Proved source `10.10.10.100` used port3/R1 with `port3 out` packet-capture evidence.
- Correctly interpreted source `.101` as an asymmetric-return example: the request left port3 while Alpine's own ECMP decision returned through port1.
- Added temporary Kali alias `10.10.10.110/24` and proved the second FortiGate member with an explicit `port1 out` request capture.
- Recorded that equal source-IP-based ECMP does not alternate packets and that adjacent source addresses are not guaranteed to hash to different members.
- Discussed weight-based ECMP without claiming it was implemented; the completed lab retains equal weights and source-IP-based selection.
- Documented cleanup and persistence requirements for the temporary Kali address, live Alpine `ip` configuration, and Cisco running configurations.
- Embedded the latest dual-path topology in the root README and added 43 curated evidence artifacts covering configuration, success, failure, diagnosis, and correction.

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
