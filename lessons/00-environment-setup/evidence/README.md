# Lesson 00 Evidence

This directory is for sanitized screenshots or short evidence artifacts that prove the environment was actually built.

## Recommended evidence

| Filename | Evidence purpose |
| --- | --- |
| `01-fortigate-kvm-package-selection.png` | Correct FortiGate `FGT_VM64_KVM` new-deployment package |
| `02-eve-image-import.png` | EVE-NG image import / installed FortiGate image |
| `03-system-status-pre-license.png` | FortiOS 7.6.7 build, CPU/RAM entitlement, initial license state |
| `04-connectivity-and-route-check.png` | Internet reachability, FortiGuard DNS/reachability, default route |
| `05-post-license-setup-wizard.png` | Post-license wizard functioning |
| `06-operational-dashboard.png` | Final working FortiOS dashboard |

## Sanitization requirements

Before committing a screenshot:

- Remove or crop FortiCare/FortiCloud account email if it is not needed.
- Never include a FortiCare/FortiCloud password.
- Never include the FortiGate administrator password.
- Never include private keys, tokens, license files, or activation secrets.
- Avoid unrelated personal paths/usernames when they do not prove anything.
- Keep only the UI/CLI area that supports the technical claim.
- Prefer descriptive filenames over `Screenshot 2026-...png`.

## Explicitly excluded evidence

The CLI screenshot used during activation that displayed the `account-password` command must **not** be committed.
