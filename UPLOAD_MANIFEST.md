# GitHub Update Manifest

Apply this Lesson 05 package to the existing repository root.

## Root updates

- `README.md` - advance the integrated project to Lesson 05 and summarize the inspected identity-aware HTTP path.
- `CHANGELOG.md` - record AV readiness, baselines, flow/proxy tests, logs, oversized handling, and archive inspection.
- `REPOSITORY_STRUCTURE.md` - add the Lesson 05 directory, lab-file boundary, and AV evidence rules.
- `UPLOAD_MANIFEST.md` - describe this update package.

## New Lesson 05 content

- `lessons/05-antivirus-inspection/README.md` - compact theory/implementation narrative with commands, configurations, results, troubleshooting, and cleanup.
- `lessons/05-antivirus-inspection/lab-files/README.md` - controlled artifact-generation and safety instructions.
- `lessons/05-antivirus-inspection/lab-files/benign.txt` - harmless 33-byte negative control.
- `lessons/05-antivirus-inspection/evidence/README.md` - curated evidence index.
- `lessons/05-antivirus-inspection/evidence/*.png` - 20 sanitized proof artifacts.

## Implemented and validated

1. Restored the cumulative Alpine routing/service state and authenticated Kali path.
2. Recorded AV engine, signature age, and evaluation limitations.
3. Established benign and EICAR pre-AV baselines.
4. Tested flow-based AV with a passing benign control and blocked EICAR control.
5. Tested proxy-based AV with the same controls.
6. Correlated Antivirus and Forward Traffic logs with identity, policy, NAT, and ECMP path context.
7. Validated the FortiGate antivirus replacement page.
8. Proved default versus one-MiB oversized-file behavior.
9. Distinguished flow reset behavior from proxy `403` behavior.
10. Proved benign ZIP acceptance and EICAR ZIP detection.

## Theory-only boundary

- production-current FortiGuard signatures and cloud verdicts
- Virus Outbreak Prevention service behavior
- external malware block lists
- EMS threat feeds
- FortiSandbox submission/analysis
- production HTTPS deep inspection
- deployed legacy full-file AV

## Final-state cautions

- The last captured test state uses proxy inspection, `L05-AV-PROXY`, and the intentionally restrictive `L05-PROTO-1MB` profile.
- For normal continuation, restore `default` Protocol Options and preferably `L05-AV-FLOW` on the `1 vCPU / 2 GiB` evaluation VM.
- Alpine's addresses, routes, HTTP process, and generated controls remain volatile.
- EICAR is harmless but intentionally triggers security products; raw EICAR and ZIP artifacts are excluded.
- The old definition databases support this deterministic lab only and are not evidence of current production protection.

## Packaging and sanitization

The update excludes credentials, authentication cookies, license artifacts, private keys, raw FortiGate backups, live malware, and raw EICAR artifacts. Screenshots are limited to those proving configuration, client behavior, or FortiGate security/log conclusions.
