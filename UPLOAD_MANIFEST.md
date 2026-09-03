# GitHub Update Manifest

Apply this **delta-only Lesson 09 package** to the existing repository root.

The package contains only new or modified paths. It does not include cloned copies of Lessons 00-08, the `.git` directory, or a full repository export.

## Replacement root files

- `README.md` - advance the integrated project to the validated two-FortiGate IPsec state.
- `CHANGELOG.md` - record the topology, routing, VPN, policy, troubleshooting, and proof completed in Lesson 09.
- `REPOSITORY_STRUCTURE.md` - add the Lesson 09 directory and its methodology/evidence rules.
- `UPLOAD_MANIFEST.md` - describe this delta-only update.

## New Lesson 09 content

- `lessons/09-site-to-site-ipsec-vpn/README.md` - compact theory, complete implementation, packet cycle, troubleshooting, and results.
- `lessons/09-site-to-site-ipsec-vpn/configs/README.md` - safe use and sanitization notes.
- `lessons/09-site-to-site-ipsec-vpn/configs/hq-fortigate.conf` - sanitized HQ interfaces, objects, IKE/IPsec, routes, and policies.
- `lessons/09-site-to-site-ipsec-vpn/configs/branch-fortigate.conf` - sanitized Branch interfaces, objects, IKE/IPsec, routes, and policies.
- `lessons/09-site-to-site-ipsec-vpn/configs/supporting-routing.txt` - R1 and Alpine changes required by the new topology.
- `lessons/09-site-to-site-ipsec-vpn/evidence/README.md` - curated evidence index and claim boundary.
- `lessons/09-site-to-site-ipsec-vpn/evidence/*.png` - six selected routing, negotiation, traffic, and troubleshooting artifacts.
- `lessons/09-site-to-site-ipsec-vpn/evidence/07-tunnel-summary-sanitized.txt` - control-plane selector proof without the appliance prompt.

## Implemented and validated

1. Replaced the Lesson 03 upper-path R2 with a separately licensed Branch FortiGate.
2. Reused HQ `port1` as `10.50.50.1/24` and assigned Branch `port1` as `10.50.50.2/24` for the direct VPN underlay.
3. Assigned Branch `port2` as `10.40.40.1/24` and retained Alpine `eth2` as `10.40.40.100/24`.
4. Removed the active `10.60.60.100/32` shared-loopback ECMP continuation and obsolete R1 route while preserving Lesson 03 as history.
5. Replaced Alpine's ECMP return path with `10.10.10.0/24 via 10.40.40.1 dev eth2`.
6. Proved peer underlay reachability and captured Branch-LAN failure before a protected route existed.
7. Diagnosed two GUI custom-tunnel `-61` failures and created the intended objects through CLI.
8. Created mirrored IKEv1 Main Mode Phase 1 objects with PSK, `DES-SHA1`, DH14, DPD on-idle, and NAT-T disabled.
9. Created mirrored ESP tunnel-mode Phase 2 objects with `/24` selectors, `DES-SHA1`, PFS/DH14, replay protection, and 43200-second lifetimes.
10. Disabled Auto-negotiate and Autokey Keep Alive so interesting traffic would establish the SAs.
11. Pointed each protected-subnet route to its IPsec virtual interface rather than physical `port1` or an underlay next hop.
12. Added two PING/HTTP policies per FortiGate so either site can initiate; NAT and UTM remain disabled for the transport test.
13. Observed the first Kali echo time out during negotiation and later packets succeed.
14. Confirmed `1/1` selector up, Branch GUI status `Up`, and a separate Alpine-to-Kali test with 3/3 replies.

## Final retained state

| Component | HQ | Branch |
| --- | --- | --- |
| Protected LAN | `10.10.10.0/24` | `10.40.40.0/24` |
| Underlay | `port1` / `10.50.50.1` | `port1` / `10.50.50.2` |
| Phase 1 | `HQ-to-Branch` | `Branch-to-HQ` |
| Phase 2 | `HQ-BR-P2` | `BR-HQ-P2` |
| Protected route | `10.40.40.0/24` via `HQ-to-Branch` | `10.10.10.0/24` via `Branch-to-HQ` |
| Policies | LAN-to-VPN and VPN-to-LAN | LAN-to-VPN and VPN-to-LAN |
| Services / NAT | PING, HTTP / disabled | PING, HTTP / disabled |

## Explicit claim boundary

The update proves one route-based, point-to-point site-to-site tunnel with bidirectional PING and traffic-triggered establishment. It does not claim production-strength cryptography, IKEv2, certificate authentication, NAT traversal, transport mode, policy-based VPN, remote-access operation, redundant-tunnel failover, or mesh behavior.

## Packaging and sanitization

The update excludes the real PSK and encrypted PSK output, VM serial/license material, raw FortiGate backups, private keys, certificates, unrelated screenshots, all prior lesson directories, and Git metadata. Reusable configs contain `REPLACE_WITH_SHARED_SECRET` only.
