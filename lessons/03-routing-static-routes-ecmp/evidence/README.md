# Lesson 03 Evidence Index

This directory contains the curated, sanitized proof set for Lesson 03. The files are ordered by the actual lab progression: inherited Lesson 02 state, the first routed path through R1, the second routed path through R2, Alpine multipath routing, creation of a common loopback destination, FortiGate ECMP, policy troubleshooting, and packet-level proof of both FortiGate ECMP members.

The evidence intentionally represents sequential states. The permanent evaluation is limited to three FortiGate interfaces, three policies, and three routes, so intermediate routes and policies were repurposed after their behavior had been proven. The screenshots must not be read as if every temporary object existed simultaneously.

## Evidence standard

The lesson uses three complementary proof layers:

1. **Configuration proof** - interfaces, routes, policies, and ECMP settings exist as intended.
2. **Data-plane proof** - FortiGate, Kali, Alpine, or the Cisco routers can or cannot reach the test destination as expected.
3. **Diagnostic proof** - routing tables, route selection, and FortiGate packet sniffing explain the observed result.

## Architecture progression

| File | What it proves |
| --- | --- |
| [01-lesson02-starting-topology.png](01-lesson02-starting-topology.png) | The directly connected Lesson 02 starting point before routing was introduced. |
| [02-single-r1-topology.png](02-single-r1-topology.png) | The first routed design: FortiGate port3 to R1, then R1 to Alpine. |
| [19-final-dual-path-topology.png](19-final-dual-path-topology.png) | The latest topology: port2 LAB-LAN, port3/R1 lower path, and repurposed port1/R2 upper path. |

## First routed path through R1

| File | What it proves |
| --- | --- |
| [03-alpine-prefix-troubleshooting.png](03-alpine-prefix-troubleshooting.png) | Alpine initially received an unintended `/32`; Linux `ip` required CIDR notation rather than a dotted-decimal mask. |
| [04-alpine-eth1-down.png](04-alpine-eth1-down.png) | Correct addressing alone was insufficient because Alpine eth1 remained administratively down. |
| [05-r1-interface-configuration.png](05-r1-interface-configuration.png) | R1 Gi0/0 and Gi0/1 addressing for the Alpine and FortiGate transit networks. |
| [06-r1-status-initial-ping-failure.png](06-r1-status-initial-ping-failure.png) | R1 interfaces were operational while the initial same-subnet ping still failed, directing troubleshooting toward Alpine's link state. |
| [07-alpine-routes-r1-reachability.png](07-alpine-routes-r1-reachability.png) | Corrected Alpine routes and successful reachability to R1's far-side transit address. |
| [08-fortigate-port3-transit.png](08-fortigate-port3-transit.png) | FortiGate port3 was repurposed as the `10.30.30.1/24` R1 transit interface. |
| [09-fortigate-r1-adjacency.png](09-fortigate-r1-adjacency.png) | FortiGate-to-R1 same-subnet adjacency succeeded before testing a remote network. |
| [10-fortigate-lower-static-route.png](10-fortigate-lower-static-route.png) | Static route to `10.20.20.0/24` through R1 at `10.30.30.2`. |
| [11-fortigate-to-alpine-lower.png](11-fortigate-to-alpine-lower.png) | FortiGate reached Alpine through R1, validating the lower route independently of transit policy. |
| [12-policy-negative-baseline.png](12-policy-negative-baseline.png) | The firewall itself could route while Kali transit failed without a matching policy. |
| [13-lab-to-alpine-policy.png](13-lab-to-alpine-policy.png) | The restored narrow port2-to-port3 ICMP policy with NAT disabled. |
| [14-kali-to-alpine-lower.png](14-kali-to-alpine-lower.png) | Kali reached Alpine after both routing and policy requirements were satisfied. |
| [15-fortigate-single-path-routing-table.png](15-fortigate-single-path-routing-table.png) | CLI route-table state during the completed single-R1 phase. |
| [16-routing-monitor-single-path.png](16-routing-monitor-single-path.png) | GUI Routing Monitor correlation with the CLI route table. |
| [17-legacy-vip-objects.png](17-legacy-vip-objects.png) | Lesson 02 VIP objects still existed as historical configuration after the routing redesign; they were not revalidated in the final topology. |
| [18-alpine-to-kali-observed.png](18-alpine-to-kali-observed.png) | Observed Alpine-initiated reachability toward Kali in the routed topology. |

## Second path through R2 and Alpine multipath routing

| File | What it proves |
| --- | --- |
| [20-r2-interface-status.png](20-r2-interface-status.png) | R2 Gi0/0 `10.50.50.2/24` and Gi0/1 `10.40.40.1/24` were up/up. |
| [21-r2-return-route.png](21-r2-return-route.png) | R2 had a return route to `10.10.10.0/24` through FortiGate port1. |
| [22-fortigate-upper-static-route.png](22-fortigate-upper-static-route.png) | Intermediate FortiGate route to Alpine's upper `10.40.40.0/24` network through R2. |
| [23-fortigate-to-r2-far-interface.png](23-fortigate-to-r2-far-interface.png) | FortiGate reached R2's far-side interface, proving R2 forwarding before the Alpine upper address was tested. |
| [24-alpine-dual-interface-addressing.png](24-alpine-dual-interface-addressing.png) | Alpine eth1 and eth2 had the lower and upper routed-path addresses and were up. |
| [25-alpine-iproute2-multipath-command.png](25-alpine-iproute2-multipath-command.png) | Full iproute2 was installed and Alpine's equal-cost multipath route to LAB-LAN was entered. |
| [26-alpine-dual-path-routing-table.png](26-alpine-dual-path-routing-table.png) | Alpine's live table contained both equal-weight next hops plus explicit transit routes. |
| [27-alpine-route-selection.png](27-alpine-route-selection.png) | `ip route get` selected the appropriate next hop when the source was bound to eth1 or eth2. |
| [28-fortigate-to-alpine-upper.png](28-fortigate-to-alpine-upper.png) | FortiGate reached Alpine's upper address through R2. |
| [29-unsaved-upper-policy-draft.png](29-unsaved-upper-policy-draft.png) | The combined policy was present only in the editor; it had not yet been committed with **OK**. |
| [30-kali-to-alpine-upper.png](30-kali-to-alpine-upper.png) | Kali reached Alpine's upper address after the policy was actually saved. |
| [31-alpine-to-kali-upper.png](31-alpine-to-kali-upper.png) | Alpine initiated traffic from its upper address toward Kali successfully. |

## Shared loopback and FortiGate ECMP

| File | What it proves |
| --- | --- |
| [32-alpine-loopback-target.png](32-alpine-loopback-target.png) | Alpine loopback `10.60.60.100/32` existed and answered locally. |
| [33-r1-loopback-route-proof.png](33-r1-loopback-route-proof.png) | R1 routed to the shared loopback through Alpine eth1 and successfully pinged it. |
| [34-fortigate-ecmp-routing-table.png](34-fortigate-ecmp-routing-table.png) | FortiGate installed two equal static next hops to the exact same `10.60.60.100/32` destination. |
| [35-fortigate-ecmp-target-ping.png](35-fortigate-ecmp-target-ping.png) | FortiGate itself reached the common ECMP destination. |
| [36-ecmp-policy-mismatch-sniffer.png](36-ecmp-policy-mismatch-sniffer.png) | Failed Kali traffic appeared only as `port2 in`, proving the packet reached FortiGate but no ECMP egress was authorized. |
| [37-ecmp-policy-port3-gap.png](37-ecmp-policy-port3-gap.png) | The combined lab policy omitted port3, explaining the failure when ECMP selected the R1 member. |
| [38-ecmp-policy-fixed.png](38-ecmp-policy-fixed.png) | Port3 was added to the combined policy's incoming and outgoing interface lists under the three-policy constraint. |
| [39-kali-to-ecmp-target.png](39-kali-to-ecmp-target.png) | Kali reached `10.60.60.100` after the policy-interface mismatch was corrected. |
| [40-ecmp-port3-source100.png](40-ecmp-port3-source100.png) | Source `10.10.10.100` left FortiGate on port3/R1 and returned on the same member. |
| [41-asymmetric-return-source101.png](41-asymmetric-return-source101.png) | Source `.101` left on port3 while Alpine's separate ECMP choice returned through port1; this is return-path evidence, not proof of FortiGate port1 egress. |
| [42-fortigate-ecmp-mode-source-ip.png](42-fortigate-ecmp-mode-source-ip.png) | FortiGate's active IPv4 ECMP mode was `source-ip-based`. |
| [43-ecmp-port1-source110.png](43-ecmp-port1-source110.png) | Temporary source `10.10.10.110` produced the required `port1 out` request and proved FortiGate used the R2 ECMP member. |

## Evidence interpretation notes

- `10.20.20.100` and `10.40.40.100` are different connected identities on Alpine. Equal-distance routes to those different prefixes do **not** constitute FortiGate ECMP.
- `10.60.60.100/32` is the common destination that made the two FortiGate routes equivalent and therefore eligible for ECMP.
- Alpine and FortiGate made independent ECMP decisions. An asymmetric reply can therefore enter FortiGate on a member different from the member used for the request.
- A packet shown as `port1 in` proves only its ingress direction. FortiGate's use of the upper ECMP member is proven by `port1 out` in file 43.
- The broad combined policy is a transparent lab workaround for the three-policy evaluation limit. It is not a production least-privilege recommendation.
- Weight-based ECMP was discussed but not configured. The final proof uses equal route cost/priority and FortiGate's source-IP-based algorithm.
- The R2 route to the loopback and its reachability were confirmed during the live implementation, but no separate screenshot was captured. The lesson states that limitation instead of inventing evidence.

## Sanitization

The evidence set excludes administrator passwords, FortiCare/FortiCloud credentials, license artifacts, private keys, reusable tokens, raw configuration backups, and unrelated desktop content.
