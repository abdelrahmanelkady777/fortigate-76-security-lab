# FortiGate 7.6 Security Lab

Hands-on FortiGate lab built in EVE-NG alongside the FortiOS 7.6 Administrator course. The repository is developed incrementally: each lesson starts from a known-good state, adds one administration or network-security capability, validates it from the data plane and FortiGate control plane, and records troubleshooting and evidence.

> This is an independent educational lab. It is not official Fortinet course material.

## Current state

**Current milestone: Lesson 00 - Environment Setup and Licensing (Complete)**

The base FortiGate VM is operational and ready for the course labs.

| Component | Value |
| --- | --- |
| Platform | EVE-NG / QEMU-KVM |
| Appliance | FortiGate-VM64-KVM |
| FortiOS | `v7.6.7 build 3704 (GA.M)` |
| vCPU | `1` |
| RAM | `2048 MB` |
| Interfaces available to the evaluation VM | `3` |
| Management interface | `port1` via DHCP |
| Evaluation model | Permanent FortiGate-VM evaluation license |
| FortiCare / FortiGuard subscriptions | Not included with the free evaluation |

## What Lesson 00 demonstrates

- Selecting the correct FortiGate KVM deployment image rather than FortiFirewall, ARM64, or upgrade packages
- Importing the FortiGate qcow2 disk into EVE-NG
- Creating a FortiGate node within the permanent evaluation resource limits
- Completing first boot and the enforced FortiOS administrator-password setup
- Verifying FortiOS version, interfaces, routing, Internet access, and DNS
- Diagnosing a GUI license-check stall
- Activating the free permanent evaluation license from the FortiGate CLI
- Completing the post-license setup wizard and reaching the normal FortiOS dashboard
- Recording the limitations that must influence later lab design

## Lessons

| Level | Status | Main outcome |
| --- | --- | --- |
| [00 - Environment Setup and Licensing](lessons/00-environment-setup/README.md) | Complete | Operational FortiGate 7.6.7 VM in EVE-NG with permanent evaluation licensing |
| 01+ | Planned | Added one level at a time as the FortiOS 7.6 Administrator course progresses |

The repository root represents the complete evolving FortiGate project. Each implemented stage lives under `lessons/`, beginning with Lesson 00. Future lessons are added only after they are implemented and validated.

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
    └── 00-environment-setup/
        ├── README.md
        └── evidence/
            └── README.md
```

## Evidence standard

A configuration is not considered complete merely because an object exists in the GUI.

For later FortiGate levels, the expected pattern is:

1. Record the starting state.
2. Configure the feature.
3. Verify the relevant route, policy, session, VPN, security-profile, authentication, or HA state.
4. Generate known-good traffic.
5. Generate a negative/failure/security test when applicable.
6. Check FortiGate logs/diagnostics.
7. Run a regression test against earlier working functionality.
8. Record any limitation caused by the evaluation license.

## Evaluation-license constraint

The permanent evaluation license used in this lab is intentionally restricted. The FortiGate itself reported:

- Maximum `1` CPU and `2 GiB` memory
- Maximum `3` interfaces
- Maximum `3` firewall policies
- Maximum `3` routes
- Low-encryption operation only
- No FortiCare support
- No FortiGuard support

These constraints are part of the lab design. Later lessons must reuse/reset configurations or separate scenarios instead of pretending the appliance has an unrestricted production license.

## Security and sanitization

Never commit:

- FortiCare/FortiCloud account credentials
- FortiGate administrator passwords
- VM license data
- private keys
- reusable tokens or cookies
- screenshots containing account passwords
- unsanitized appliance configuration backups

Use placeholders such as `<FORTICARE_EMAIL>` and `<FORTICARE_PASSWORD>` in documentation.
