# FortiGate 7.6 Security Lab

Hands-on FortiGate lab built in EVE-NG alongside the FortiOS 7.6 Administrator course. The repository is developed incrementally: each lesson starts from a known-good state, adds one administration or network-security capability, validates it from the client/data plane and FortiGate control plane where applicable, and records the engineering decisions behind the implementation.

> This is an independent educational lab. It is not official Fortinet course material.

## Current state

**Current milestone: Lesson 02 - Firewall Policies and NAT (Complete)**

The project now contains an operational FortiGate 7.6.7 VM, a stable internal `LAB-LAN`, a protected management/recovery path on `port1`, a controlled outside network on `port3`, two internal test hosts, a lightweight Alpine outside host, validated stateful firewall behavior, policy matching/order/logging, SNAT, IP pools, static VIP DNAT, and VIP port forwarding.

| Component | Current validated state |
| --- | --- |
| Platform | EVE-NG / QEMU-KVM |
| Appliance | FortiGate-VM64-KVM |
| FortiOS | `v7.6.7 build 3704` |
| vCPU / RAM | `1 vCPU / 2048 MB` |
| Evaluation interfaces | Maximum `3` |
| `port1` | Upstream DHCP / protected management and recovery path |
| `port2` | Alias `LAB-LAN`, role `LAN`, `10.10.10.1/24` |
| LAB-LAN DHCP | `10.10.10.100-10.10.10.150` |
| Kali | `10.10.10.100/24` |
| Metasploitable | `10.10.10.101/24` |
| `port3` | Alias `externalToAlpine`, role `WAN`, `10.20.20.1/24` |
| Alpine lab NIC | `10.20.20.100/24`; route to `10.10.10.0/24` through FortiGate |
| Policy processing | Implicit deny, stateful return handling, source/destination/service matching, first-match sequence |
| Logging | Forward Traffic logs validated for both allow and deny decisions |
| SNAT | Outgoing-interface, overload pool, and one-to-one pool validated by packet capture |
| Static VIP | `10.20.20.220 -> 10.10.10.101` |
| Port-forward VIP | `10.20.20.221:8080 -> 10.10.10.101:80` |
| FortiCare / FortiGuard subscriptions | Not included with the free evaluation |

The exact `port1` address and upstream gateway remain environment-dependent. `port1` is treated as infrastructure and is intentionally excluded from forwarding/NAT experiments so that a known-good management path survives every lesson.

## Validated architecture

```text
Management / upstream network
          |
        port1
 management + recovery
      UNCHANGED
          |
   +-------------+
   | FortiGate   |
   | 7.6.7       |
   +-------------+
      /       \
   port2      port3
  LAB-LAN     externalToAlpine
10.10.10.1    10.20.20.1
     |             |
  switch          Alpine
  /   \         10.20.20.100
Kali  Metasploitable
.100      .101
          HTTP :80
```

Lesson 02 uses this topology to prove both directions of firewall behavior:

```text
LAB-LAN -> outside
policy matching + stateful sessions + SNAT

outside -> LAB-LAN
VIP/DNAT + inbound firewall policy
```

## Lessons

| Level | Status | Main outcome |
| --- | --- | --- |
| [00 - Environment Setup and Licensing](lessons/00-environment-setup/README.md) | Complete | Operational FortiGate 7.6.7 VM in EVE-NG with permanent evaluation licensing |
| [01 - System, Network, and Administrative Access Foundations](lessons/01-system-network-admin-access/README.md) | Complete | Internal LAB-LAN, DHCP, persistent Kali client, management protocols, and Trusted Hosts positive/negative validation |
| [02 - Firewall Policies and NAT](lessons/02-firewall-policies-nat/README.md) | Complete | Stateful transit policy behavior, source/destination/service matching, Policy ID vs sequence, logging, SNAT/IP pools, VIP DNAT, and port forwarding |
| 03+ | Planned | Added one level at a time as the FortiOS 7.6 Administrator course progresses |

The repository root represents the complete evolving FortiGate project. Detailed implementation belongs inside each lesson.

## Repository layout

```text
.
├── README.md
├── CHANGELOG.md
├── REPOSITORY_STRUCTURE.md
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
    └── 02-firewall-policies-nat/
        ├── README.md
        └── evidence/
            ├── README.md
            └── curated policy/NAT/VIP proof artifacts
```

## Project methodology

The course is the curriculum, not a list of GUI screens to reproduce.

The working sequence is:

1. Understand the lesson objective.
2. Decide whether the topic needs implementation or only conceptual understanding.
3. Extend the existing topology instead of creating an unrelated mini-lab.
4. Change one control at a time.
5. Preserve a known-good recovery path.
6. Validate behavior from the appropriate client, FortiGate CLI, routing/authentication state, packet capture, or logs.
7. Include a negative/failure/security test when it adds real proof.
8. Record engineering decisions and evaluation-license constraints honestly.
9. Commit only curated, sanitized evidence.

A configuration is not considered proven just because a GUI object exists.

Lesson 02 extends that methodology by using packet captures at the receiving host to prove address translation and Forward Traffic logs to attribute allow/deny decisions to specific Policy IDs.

## Evidence standard

Where applicable, use three layers of proof:

1. **Configuration proof** - the intended FortiGate object exists.
2. **Data-plane/client proof** - the endpoint behaves as expected.
3. **Control-plane/security proof** - FortiGate routing, sessions, authentication state, logs, or diagnostics explain the mechanism.

Lesson 02 examples:

```text
Policy order test
same source/destination/service
DENY policy above ALLOW -> denied by Policy ID 2
ALLOW above DENY -> accepted by Policy ID 1
```

```text
One-to-one SNAT test
Kali + Metasploitable initiate simultaneously
Alpine observes 10.20.20.210 and 10.20.20.211
```

```text
VIP port forwarding
Alpine requests 10.20.20.221:8080
FortiGate publishes backend 10.10.10.101:80
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

These constraints are part of the architecture. Lesson 02 demonstrates the intended response: reuse policies, change test conditions sequentially, and combine objects only when the security intent is genuinely identical. The repository does not pretend that every temporary test state coexisted as a production rulebase.

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
