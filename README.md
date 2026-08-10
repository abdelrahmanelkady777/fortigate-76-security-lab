# FortiGate 7.6 Security Lab

Hands-on FortiGate lab built in EVE-NG alongside the FortiOS 7.6 Administrator course. The repository is developed incrementally: each lesson starts from a known-good state, adds one administration or network-security capability, validates it from the client/data plane and FortiGate control plane where applicable, and records the engineering decisions behind the implementation.

> This is an independent educational lab. It is not official Fortinet course material.

## Current state

**Current milestone: Lesson 01 - System, Network, and Administrative Access Foundations (Complete)**

The project now contains an operational FortiGate 7.6.7 VM plus a stable internal lab subnet on `port2`, FortiGate-provided DHCP, a persistent Kali workstation, and a controlled administrative-access path with Trusted Hosts validation.

| Component | Current validated state |
| --- | --- |
| Platform | EVE-NG / QEMU-KVM |
| Appliance | FortiGate-VM64-KVM |
| FortiOS | `v7.6.7 build 3704` |
| vCPU / RAM | `1 vCPU / 2048 MB` |
| Evaluation interfaces | Maximum `3` |
| `port1` | Upstream DHCP / existing management and recovery path |
| `port2` | Alias `LAB-LAN`, role `LAN`, `10.10.10.1/24` |
| LAB-LAN DHCP | `10.10.10.100-10.10.10.150` |
| Persistent client | Kali Linux, observed at `10.10.10.100/24` |
| Administrative protocols on `port2` | HTTPS, SSH, PING |
| Test administrator | `trusted-admin` |
| Final Trusted Host | `10.10.10.100/32` |
| FortiCare / FortiGuard subscriptions | Not included with the free evaluation |

The exact `port1` address and upstream gateway are environment-dependent because the EVE uplink can change with the host Wi-Fi/network. `port1` is therefore treated as infrastructure and is intentionally protected from unnecessary experiments.

## Validated architecture

```text
Upstream EVE DHCP / Wi-Fi-dependent network
                 |
               port1
        existing management/uplink
                 |
          +-------------+
          | FortiGate   |
          | 7.6.7       |
          +-------------+
                 |
               port2
        LAB-LAN 10.10.10.1/24
        DHCP 10.10.10.100-150
        HTTPS / SSH / PING
                 |
               Kali
        10.10.10.100/24 via DHCP
                 |
        trusted-admin allowed
        from 10.10.10.100/32
```

## Lessons

| Level | Status | Main outcome |
| --- | --- | --- |
| [00 - Environment Setup and Licensing](lessons/00-environment-setup/README.md) | Complete | Operational FortiGate 7.6.7 VM in EVE-NG with permanent evaluation licensing |
| [01 - System, Network, and Administrative Access Foundations](lessons/01-system-network-admin-access/README.md) | Complete | Internal LAB-LAN, DHCP, persistent Kali client, management protocols, and Trusted Hosts positive/negative validation |
| 02+ | Planned | Added one level at a time as the FortiOS 7.6 Administrator course progresses |

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
    │       └── README.md
    └── 01-system-network-admin-access/
        ├── README.md
        └── evidence/
            ├── README.md
            ├── 01-starting-topology.png
            ├── 02-port2-address-cli.png
            ├── 03-role-alias.png
            ├── 04-dhcp-config.png
            ├── 05-kali-dhcp-route.png
            ├── 06-fortigate-routing-table.png
            ├── 07-trusted-admin-baseline.png
            ├── 08-trusted-host-allowed.png
            ├── 09-trusted-host-denied-config.png
            ├── 10-trusted-host-denied-result.png
            ├── 11-ping-validation.png
            └── 12-ssh-validation.png
```

## Project methodology

The course is the curriculum, not a list of GUI screens to reproduce.

The working sequence is:

1. Understand the lesson objective.
2. Decide whether the topic needs implementation or only conceptual understanding.
3. Extend the existing topology instead of creating an unrelated mini-lab.
4. Change one control at a time.
5. Preserve a known-good recovery path.
6. Validate behavior from the appropriate client, FortiGate CLI, routing/authentication state, or logs.
7. Include a negative/failure/security test when it adds real proof.
8. Record engineering decisions and evaluation-license constraints honestly.
9. Commit only curated, sanitized evidence.

A configuration is not considered proven just because a GUI object exists.

## Evidence standard

Where applicable, use three layers of proof:

1. **Configuration proof** - the intended FortiGate object exists.
2. **Data-plane/client proof** - the endpoint behaves as expected.
3. **Control-plane/security proof** - FortiGate routing, sessions, authentication state, logs, or diagnostics explain the mechanism.

Lesson 01 demonstrates this most clearly with Trusted Hosts:

```text
Kali source 10.10.10.100
Trusted Host 10.10.10.100/32
=> login succeeds

Kali source 10.10.10.100
Trusted Host 10.10.10.99/32
=> authentication fails
```

Only the trusted-source match changed in the negative test.

## Evaluation-license constraint

The permanent evaluation license used in this lab is intentionally restricted. The FortiGate reported:

- Maximum `1` CPU and `2 GiB` memory
- Maximum `3` interfaces
- Maximum `3` firewall policies
- Maximum `3` routes
- Low-encryption operation only
- No FortiCare support
- No FortiGuard support

These constraints are part of the architecture. Later lessons must reuse/reset configurations or separate scenarios instead of pretending the appliance has an unrestricted production license.

## Security and sanitization

Never commit:

- FortiCare/FortiCloud account credentials
- FortiGate administrator passwords
- VM license data
- private keys
- reusable tokens or cookies
- screenshots containing passwords
- unsanitized appliance configuration backups

Use placeholders for credentials and keep evidence limited to what proves the technical claim.
