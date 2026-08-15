# FortiGate 7.6 Security Lab

Hands-on FortiGate lab built in EVE-NG alongside the FortiOS 7.6 Administrator course. The repository is developed incrementally: each lesson starts from a known-good state, adds one administration or network-security capability, validates it from the client/data plane and FortiGate control plane, and records the engineering decisions and troubleshooting behind the result.

> This is an independent educational lab. It is not official Fortinet course material.

## Current state

**Current milestone: Lesson 03 - Routing, Static Routes, and ECMP (Complete)**

The lab now implements a dual-routed underlay between `LAB-LAN` and Alpine Linux. FortiGate reaches one shared Alpine loopback through two equivalent static routes: port3/R1 and the repurposed port1/R2. Alpine also has its own equal-cost return route toward `LAB-LAN`. FortiGate source-IP-based ECMP was proven on both members with packet captures, including an explicit `port1 out` capture for the upper path.

| Component | Current validated state |
| --- | --- |
| Platform | EVE-NG / QEMU-KVM |
| Appliance | FortiGate-VM64-KVM |
| FortiOS | `v7.6.7 build 3704` |
| vCPU / RAM | `1 vCPU / 2048 MB` |
| Evaluation limits used by this design | Maximum `3` interfaces, `3` firewall policies, and `3` routes |
| FortiGate `port2` | Alias `LAB-LAN`, `10.10.10.1/24`; current GUI/client access |
| LAB-LAN DHCP | `10.10.10.100-10.10.10.150` |
| Kali | `10.10.10.100/24`; temporary `10.10.10.110/24` used only to prove the second ECMP hash member |
| Metasploitable | `10.10.10.101/24` |
| FortiGate `port3` | Alias `TRANSIT-R1`, `10.30.30.1/24` |
| R1 | Gi0/1 `10.30.30.2/24`; Gi0/0 `10.20.20.1/24` |
| Alpine lower path | eth1 `10.20.20.100/24` |
| FortiGate `port1` | Alias `R2-Port1`, `10.50.50.1/24`; repurposed from the earlier management uplink |
| R2 | Gi0/0 `10.50.50.2/24`; Gi0/1 `10.40.40.1/24` |
| Alpine upper path | eth2 `10.40.40.100/24` |
| Shared ECMP destination | Alpine loopback `10.60.60.100/32` |
| Alpine separate upstream | eth0 observed as `192.168.1.161/24`, default via `192.168.1.1` |
| FortiGate ECMP routes | `10.60.60.100/32` via R1 `10.30.30.2` and R2 `10.50.50.2`; both distance `10`, metric `0`, priority `1`, weight `0` |
| FortiGate ECMP algorithm | `source-ip-based` |
| Alpine ECMP | Equal-weight route to `10.10.10.0/24` through `10.20.20.1/eth1` and `10.40.40.1/eth2` |
| ECMP proof | `.100` selected port3/R1; temporary `.110` selected port1/R2 |
| Current management decision | port1 is no longer management; administration continues through port2/LAB-LAN |
| FortiCare / FortiGuard subscriptions | Not included with the free evaluation |

The final FortiGate installed route state is intentionally small:

```text
C 10.10.10.0/24 directly connected, port2
C 10.30.30.0/24 directly connected, port3
C 10.50.50.0/24 directly connected, port1
S 10.60.60.100/32 [10/0] via 10.30.30.2, port3
                     [10/0] via 10.50.50.2, port1
```

The earlier `10.20.20.0/24` and `10.40.40.0/24` FortiGate routes were validated intermediate states. They were repurposed to the common `/32` routes because equal-cost routes to different destination prefixes are not ECMP.

## Latest validated topology

![Latest Lesson 03 dual-path routing topology](lessons/03-routing-static-routes-ecmp/evidence/19-final-dual-path-topology.png)

The design deliberately uses two independent routed paths:

- **Lower member:** FortiGate port3 -> R1 -> Alpine eth1
- **Upper member:** FortiGate port1 -> R2 -> Alpine eth2
- **Common target:** Alpine `lo` -> `10.60.60.100/32`

The loopback is essential to the ECMP test. Alpine's `10.20.20.100` and `10.40.40.100` are different destinations, so routes to them cannot demonstrate FortiGate ECMP. The loopback gives both routers one identical destination prefix while remaining independent of either physical link address.

## Lessons

| Level | Status | Main outcome |
| --- | --- | --- |
| [00 - Environment Setup and Licensing](lessons/00-environment-setup/README.md) | Complete | Operational FortiGate 7.6.7 VM in EVE-NG with permanent evaluation licensing |
| [01 - System, Network, and Administrative Access Foundations](lessons/01-system-network-admin-access/README.md) | Complete | Internal LAB-LAN, DHCP, persistent Kali client, management protocols, and Trusted Hosts positive/negative validation |
| [02 - Firewall Policies and NAT](lessons/02-firewall-policies-nat/README.md) | Complete | Stateful policy behavior, matching/order/logging, SNAT/IP pools, VIP DNAT, and port forwarding |
| [03 - Routing, Static Routes, and ECMP](lessons/03-routing-static-routes-ecmp/README.md) | Complete | Route lookup and attributes, Cisco/Alpine return routing, route-versus-policy behavior, dual routed paths, Alpine ECMP, shared loopback, and FortiGate source-IP ECMP proof |
| 04+ | Planned | Added one level at a time as the FortiOS 7.6 Administrator course progresses |

The repository root describes the currently integrated project. Each lesson preserves the detailed implementation and its validated historical stages.

## Repository layout

```text
.
├── README.md
├── CHANGELOG.md
├── REPOSITORY_STRUCTURE.md
├── UPLOAD_MANIFEST.md
├── .gitignore
└── lessons/
    ├── _template/
    │   └── README.md
    ├── 00-environment-setup/
    │   ├── README.md
    │   └── evidence/
    ├── 01-system-network-admin-access/
    │   ├── README.md
    │   └── evidence/
    ├── 02-firewall-policies-nat/
    │   ├── README.md
    │   └── evidence/
    └── 03-routing-static-routes-ecmp/
        ├── README.md
        └── evidence/
            ├── README.md
            ├── 19-final-dual-path-topology.png
            └── curated routing, policy, and ECMP proof artifacts
```

## Project methodology

The Fortinet course is the curriculum, not a list of GUI screens to reproduce.

The working sequence is:

1. Understand the lesson objective and translate it into observable behavior.
2. Extend the existing topology instead of building an unrelated mini-lab.
3. Preserve established endpoint identities when a transit-network redesign is sufficient.
4. Validate interfaces and same-subnet adjacency before adding remote routes.
5. Configure both forward and return routing.
6. Prove FortiGate-originated routing separately from client transit policy.
7. Change one control at a time and keep useful negative results.
8. Correlate GUI configuration with CLI tables, endpoint behavior, and packet capture.
9. State evaluation-license object reuse and sequential states honestly.
10. Commit only curated, sanitized evidence.

Lesson 03 adds several important methodology rules:

- A route answers **where traffic goes**; a policy answers **whether transit is allowed**.
- A successful FortiGate-local ping does not prove a client forwarding policy.
- ECMP requires equivalent routes to the same destination prefix, not merely two reachable paths.
- Packet direction matters: `port1 in` is not evidence of `port1 out`.
- Different devices can make independent ECMP decisions, producing an asymmetric return path.
- A saved configuration is the test state; an unsaved GUI editor is not.

## Evidence standard

Where applicable, use three layers of proof:

1. **Configuration proof** - the intended interface, route, policy, or algorithm exists.
2. **Data-plane/client proof** - the endpoint succeeds or fails as expected.
3. **Control-plane/diagnostic proof** - routing tables, route lookup, logs, or packet captures explain why.

Lesson 03 examples:

```text
Route-versus-policy test
FortiGate -> Alpine succeeds
Kali -> Alpine fails without a matching policy
Kali -> Alpine succeeds after policy restoration
```

```text
Correct ECMP test
same destination: 10.60.60.100/32
member 1: via 10.30.30.2 on port3
member 2: via 10.50.50.2 on port1
```

```text
Packet-level member proof
source 10.10.10.100 -> port3 out
source 10.10.10.110 -> port1 out
```

## Evaluation-license constraint

The permanent evaluation license used in this lab is intentionally restricted. The FortiGate reported:

- Maximum `1` CPU and `2 GiB` memory
- Maximum `3` interfaces
- Maximum `3` firewall policies
- Maximum `3` routes
- Low-encryption operation only
- No FortiCare support
- No FortiGuard support

These limits directly shaped Lesson 03. Port1 was repurposed from its earlier management role to become the R2 transit interface. The two intermediate remote-network routes were later replaced by two routes to the common `/32`. A broad bidirectional lab policy was used to cover the possible ECMP interface combinations within the three-policy ceiling. That policy is documented as a lab compromise, not as a production least-privilege design.

## Historical Lesson 02 publication objects

The Lesson 02 VIP demonstrations remain valid evidence for that lesson:

- Static VIP `10.20.20.220 -> 10.10.10.101`
- Port-forward VIP `10.20.20.221:8080 -> 10.10.10.101:80`

They were not revalidated after port3 changed from the directly connected `10.20.20.0/24` outside network to the `10.30.30.0/24` R1 transit network. They must therefore be treated as historical Lesson 02 state, not current Lesson 03 publication claims.

## Persistence and cleanup notes

- The temporary Kali alias `10.10.10.110/24` was only an ECMP hash probe and should be removed after testing.
- Because `.110` is inside the LAB-LAN DHCP scope, it must be confirmed unused/reserved before any repeat test.
- Alpine `ip addr` and `ip route` commands configure the live system and require separate persistent-network configuration or a preserved node state to survive reboot.
- Cisco running configurations require `copy running-config startup-config` if restart persistence is desired.
- A production continuation should replace the broad lab policy with directional, explicit, least-privilege policies when license capacity permits.

## Security and sanitization

Never commit:

- FortiCare/FortiCloud account credentials
- FortiGate administrator passwords
- VM license data
- private keys
- reusable tokens or cookies
- screenshots containing reusable passwords
- unsanitized appliance configuration backups

Use placeholders for credentials and keep evidence limited to what proves the technical claim.
