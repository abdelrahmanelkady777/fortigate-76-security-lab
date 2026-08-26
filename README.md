# FortiGate 7.6 Security Lab

Hands-on FortiGate lab built in EVE-NG alongside the FortiOS 7.6 Administrator course. The repository is developed incrementally: each lesson starts from a known-good state, adds one administration or network-security capability, validates it from the client/data plane and FortiGate control plane, and records the engineering decisions and troubleshooting behind the result.

> This is an independent educational lab. It is not official Fortinet course material.

## Current state

**Current milestone: Lesson 06 - Web Filtering (Complete)**

The Lesson 03 dual-routed/ECMP topology and Lesson 04 identity-aware policy now carry both antivirus and URL inspection. After Kali authenticates as `lab-local-user`, Policy ID `3` authorizes HTTP to Alpine's loopback; the inherited AV profile inspects content and `L06-WF-FLOW` evaluates requested URLs. Harmless allowed, monitored, and blocked pages prove local static URL behavior. Flow/proxy profiles, a FortiGate replacement page, exact-URL troubleshooting, and Web Filter logs were validated. FortiGuard category filtering, category actions, rating overrides, and SSL/HTTPS inspection remain theory only under the evaluation environment.

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
| Alpine separate upstream | eth0 most recently observed as `192.168.1.36/24`, default via `192.168.1.1`; DHCP state is volatile |
| FortiGate ECMP routes | `10.60.60.100/32` via R1 `10.30.30.2` and R2 `10.50.50.2`; both distance `10`, metric `0`, priority `1`, weight `0` |
| FortiGate ECMP algorithm | `source-ip-based` |
| Alpine ECMP | Equal-weight route to `10.10.10.0/24` through `10.20.20.1/eth1` and `10.40.40.1/eth2` |
| ECMP proof | `.100` selected port3/R1; temporary `.110` selected port1/R2 |
| Protected application | Python HTTP service on Alpine loopback `10.60.60.100:80` |
| Local firewall identity | `lab-local-user` in `LAB-AUTH-USERS` |
| Identity-aware policy | Policy ID `3`, `auth-lan-to-alpine`; port2 to port1/port3; `KALI-CLIENT` + `LAB-AUTH-USERS` to `ALPINE-LOOPBACK`; `HTTP` and `PING`; NAT disabled |
| Authentication behavior | HTTP form login creates an IP-to-user mapping; PING can reuse the mapping but cannot prompt |
| Authentication lifetime | `5` minutes, `idle-timeout` |
| Monitoring | `diagnose firewall auth list` and GUI Firewall User Monitor correlated |
| HTTPS portal | Theory only in final state; temporary port 1003 test failed TLS cipher negotiation and was rolled back |
| Lesson 05 AV controls | `L05-AV-FLOW` and `L05-AV-PROXY`; HTTP block action validated with benign/EICAR controls |
| AV readiness boundary | AV Engine `7.00054`; base/extended definitions `1.00000` dated 2018; suitable for EICAR only, not current-threat claims |
| Protocol Options experiment | `L05-PROTO-1MB`; oversized logging/blocking at `1 MB`; deliberately restrictive test object |
| Archive inspection | benign ZIP allowed; EICAR ZIP blocked |
| Lesson 06 HTTP controls | `allowed.html` unmatched/allowed; `monitored.html` allowed and logged; `blocked.html` denied by local URL filter |
| Lesson 06 Web Filter profiles | `L06-WF-FLOW` and `L06-WF-PROXY`; identical Simple Block and Monitor intentions validated sequentially |
| Final policy profile state | Policy ID `3`; flow-based; `L05-AV-FLOW`; `L06-WF-FLOW`; `default` Protocol Options; NAT disabled |
| FortiGuard rating status | `diagnose debug rating` and `get webfilter status` reported Web-filter `Disable`; local URL filtering remains functional |
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

## Latest validated physical topology

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
| [04 - Firewall Authentication](lessons/04-firewall-authentication/README.md) | Complete | Local active authentication, identity-aware policy enforcement, HTTP-triggered login, mapping reuse by PING, timeout, and user monitoring; remote authentication and 2FA retained as theory |
| [05 - Antivirus and Inspection Modes](lessons/05-antivirus-inspection/README.md) | Complete | Benign/EICAR controls, flow/proxy AV comparison, block page, log correlation, oversized-file enforcement, and compressed archive inspection |
| [06 - Web Filtering](lessons/06-web-filtering/README.md) | Complete | Unmatched allow plus explicit local Monitor/Block behavior, flow/proxy profiles, replacement page, exact-match troubleshooting, and Web Filter log proof; FortiGuard categories and HTTPS inspection retained as theory |
| 07+ | Planned | Added one level at a time as the FortiOS 7.6 Administrator course progresses |

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
    ├── 03-routing-static-routes-ecmp/
    │   ├── README.md
    │   └── evidence/
    │       ├── README.md
    │       ├── 19-final-dual-path-topology.png
    │       └── curated routing, policy, and ECMP proof artifacts
    ├── 04-firewall-authentication/
    │   ├── README.md
    │   └── evidence/
    │       ├── README.md
    │       └── curated authentication, timeout, and monitoring proof
    ├── 05-antivirus-inspection/
    │   ├── README.md
    │   ├── lab-files/
    │   │   ├── README.md
    │   │   └── benign.txt
    │   └── evidence/
    │       ├── README.md
    │       └── curated AV, inspection-mode, log, size, and archive proof
    └── 06-web-filtering/
        ├── README.md
        ├── lab-files/
        │   ├── README.md
        │   ├── allowed.html
        │   ├── blocked.html
        │   └── monitored.html
        └── evidence/
            ├── README.md
            └── curated Web Filter configuration, behavior, log, and troubleshooting proof
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

Lesson 04 adds identity-specific rules:

- Authentication identifies a user; the firewall policy still performs authorization.
- Source address and user/group are simultaneous match conditions, not alternatives.
- Establish the protected service before adding authentication so application failure is not confused with policy failure.
- A broad unauthenticated policy can bypass a narrower authentication design.
- PING cannot present a login form but can reuse an active mapping created through HTTP.
- Theory-only LDAP, RADIUS, 2FA, passive authentication, and HTTPS hardening are not represented as deployed capabilities.

Lesson 05 adds content-inspection rules:

- Establish benign and known-detectable controls before enabling AV.
- A firewall-policy accept and a later UTM deny are different decisions and should be correlated in separate logs.
- Flow/proxy describes policy processing; stream/legacy describes AV file handling.
- Oversized-file blocking is a resource/inspection-boundary decision, not a malware verdict.
- Archive inspection is proven with paired benign and EICAR archives.
- Old evaluation signatures support deterministic EICAR testing only, not a production-security claim.

Lesson 06 adds URL-control rules:

- A policy accept and a later Web Filter block are separate decisions.
- Local static URL filtering can be validated independently of FortiGuard category ratings.
- An unmatched URL is the negative control; Monitor permits and logs; Block denies.
- Flow/proxy Web Filter profiles must match the policy inspection architecture.
- `Simple` URL entries are deterministic, so exact host/path characters matter.
- Disabled FortiGuard rating status is documented instead of representing category actions as deployed.
- Certificate inspection, deep inspection, and HTTPS path visibility remain theory when no trusted TLS design is implemented.

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

```text
Firewall-authentication proof
before login -> PING denied and HTTP intercepted
after login -> Alpine HTTP and PING allowed
after five idle minutes -> login required again
GUI monitor == diagnose firewall auth list
```

```text
Antivirus/content-inspection proof
before AV -> benign and EICAR both download
flow AV -> benign passes; EICAR stream is reset/denied
proxy AV -> benign passes; EICAR receives FortiGate 403/block page
AV event -> infected EICAR verdict
Forward Traffic -> authenticated user, Policy ID 3, NAT noop, selected ECMP egress
protocol controls -> 2 MiB file passes by default and is blocked at the test 1 MiB threshold
archive controls -> benign ZIP passes; EICAR ZIP is blocked
```

```text
Web Filtering proof
allowed URL -> HTTP 200 with no explicit local match
Monitor URL -> HTTP 200 plus passthrough/UTM-allowed Web Filter event
Block URL -> HTTP 403/FortiGate replacement page
event details -> exact URL, profile, table index, and Local URLfilter Block source
proxy repeat -> same Monitor and Block intention under L06-WF-PROXY
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

These limits directly shaped Lessons 03-06. Port1 was repurposed from its earlier management role to become the R2 transit interface. The two intermediate remote-network routes were later replaced by two routes to the common `/32`. Lesson 03 temporarily used a broad combined policy to cover the ECMP interface combinations. Lesson 04 repurposed Policy ID `3` as the narrower `auth-lan-to-alpine` rule instead of creating a fourth policy. Lesson 05 attached AV profiles to that same policy and recorded the old/unsubscribed signature state. Lesson 06 reused Policy ID `3` again, attached Web Filter profiles sequentially, and used local URL filtering rather than claiming unavailable FortiGuard category enforcement.

## Historical Lesson 02 publication objects

The Lesson 02 VIP demonstrations remain valid evidence for that lesson:

- Static VIP `10.20.20.220 -> 10.10.10.101`
- Port-forward VIP `10.20.20.221:8080 -> 10.10.10.101:80`

They were not revalidated after port3 changed from the directly connected `10.20.20.0/24` outside network to the `10.30.30.0/24` R1 transit network. They must therefore be treated as historical Lesson 02 state, not current integrated-state publication claims.

## Persistence and cleanup notes

- The temporary Kali alias `10.10.10.110/24` was only an ECMP hash probe and should be removed after testing.
- Because `.110` is inside the LAB-LAN DHCP scope, it must be confirmed unused/reserved before any repeat test.
- Alpine `ip addr` and `ip route` commands configure the live system and require separate persistent-network configuration or a preserved node state to survive reboot.
- The Lesson 04 Python HTTP process on Alpine must also be restarted after node reboot unless made persistent.
- Lesson 05's generated EICAR, large-file, and ZIP controls live under `/var/www/lesson04` and may disappear with node replacement; only the harmless control is committed.
- `L05-PROTO-1MB` is a deliberately low test threshold. Restore `default` Protocol Options before ordinary continuation unless one-MiB blocking is explicitly desired.
- Lesson 06's three harmless HTML controls live under `/var/www/lesson04/lesson06`; repository copies are retained under `lab-files/`.
- `L06-WF-PROXY` remains as a validated sequential object; normal continuation returns Policy ID `3` to `L06-WF-FLOW` and `L05-AV-FLOW`.
- Cisco running configurations require `copy running-config startup-config` if restart persistence is desired.
- A production continuation should retain directional, explicit, least-privilege policies and a trusted HTTPS authentication portal.

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
