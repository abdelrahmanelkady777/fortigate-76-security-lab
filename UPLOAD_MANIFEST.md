# GitHub Update Manifest

Apply this **delta-only Lesson 07 package** to the existing repository root.

The package contains only new or modified paths. It does not include cloned copies of Lessons 00-06 or an entire repository export.

## Replacement root files

- `README.md` - advance the project to Lesson 07 while preserving Lesson 06 as the latest data-plane validated state.
- `CHANGELOG.md` - record certificate operations, profile configuration, theory, exclusions, cleanup, and evidence boundaries.
- `REPOSITORY_STRUCTURE.md` - add the Lesson 07 directory and configuration-only evidence rules.
- `UPLOAD_MANIFEST.md` - describe this delta-only update.

## New Lesson 07 content

- `lessons/07-ssl-certificate-inspection/README.md` - certificate foundations, exact GUI configuration, comparisons, warnings, compatibility theory, policy attachment, limitations, and engineering conclusions.
- `lessons/07-ssl-certificate-inspection/evidence/README.md` - curated evidence index and claim boundary.
- `lessons/07-ssl-certificate-inspection/evidence/*.png` - 12 sanitized certificate-store, SSL-profile, exemption, policy-attachment, and public-CA export artifacts.

No `lab-files/` directory is added because the lesson did not deploy an HTTPS server, traffic generator, endpoint trust package, or reproducible payload test. The appliance-specific downloaded CA certificate is intentionally excluded.

## Configured and studied

1. Inspected Local CA Certificate and Local Certificate inventories.
2. Verified `Fortinet_CA_SSL` is a signing CA through `CA:TRUE` and Certificate Sign properties.
3. Distinguished the roles of `Fortinet_CA_SSL`, `Fortinet_CA_Untrusted`, and `Fortinet_GUI_Server`.
4. Compared no inspection, certificate inspection, and full SSL/deep inspection.
5. Compared outbound multiple-client inspection with inbound protected-server inspection.
6. Created `L07-CERT-INSPECTION` for HTTPS/443 certificate inspection with explicit certificate, SNI, ECH, HTTP/3, validation, and logging decisions.
7. Customized `custom-deep-inspection` for outbound full SSL inspection using `Fortinet_CA_SSL`.
8. Limited protocol mapping to HTTPS/TCP 443 and blocked HTTP/3 and DNS over QUIC.
9. Configured explicit expired, revoked, validation-timeout, and validation-failed actions.
10. Examined reputation, category, and address/FQDN exemptions.
11. Temporarily demonstrated `ALPINE-LOOPBACK` as an explicit exemption, then removed it from the normal target path.
12. Attached `custom-deep-inspection` to existing Policy ID `3` with decrypted traffic mirroring disabled.
13. Downloaded and examined the public `Fortinet_CA_SSL.cer` certificate without installing it into Kali's trusted roots.
14. Documented certificate pinning, HSTS, mutual TLS, QUIC/HTTP/3, DNS over QUIC, ECH, and the visibility cost of exemptions.
15. Recorded cleanup of the accidental `alpineLoopBack` duplicate while retaining canonical `ALPINE-LOOPBACK`.

## Warning-type comparison retained

- `Fortinet_CA_SSL`: a normally valid deep-inspected site warns when the endpoint does not trust FortiGate's inspection CA.
- `Fortinet_CA_Untrusted`: FortiGate preserves an invalid origin certificate warning when access is permitted; this CA must never be trusted on endpoints.
- `Fortinet_GUI_Server`: a separate management-plane warning can result from self-signing or management IP/FQDN mismatch.

## Explicit validation boundary

The update does not claim:

- endpoint trust deployment
- successful TLS interception or decrypted payload visibility
- HTTPS AV, Web Filter, IPS, or application-control enforcement
- SSL anomaly/security-event validation
- HTTP/3, QUIC, or ECH fallback behavior
- protected-server inspection with a real server certificate/private key
- certificate pinning, HSTS-failure, or mutual-TLS compatibility tests
- imported local/CA/remote certificates, CSRs, or CRLs
- production PKI readiness

Lesson 06 therefore remains the latest traffic-validated milestone. Lesson 07 is complete as a certificate/SSL configuration and design lesson under the evaluation constraint.

## Final-state cautions

- `custom-deep-inspection` is retained as the configured study object.
- `L07-CERT-INSPECTION` is retained as the certificate-inspection comparison object.
- `L07-PROTECT-SERVER` has no deployed server certificate/private-key path.
- Use `no-inspection` for ordinary encrypted traffic on the low-encryption evaluation VM unless a supported trust/test design is introduced.
- The temporary Alpine SSL exemption must not remain when that destination is meant to represent inspected traffic.
- Remove the accidental lowercase duplicate only after confirming it has zero references.
- The exported public CA is appliance-specific and is not included in the package.

## Packaging and sanitization

The update excludes credentials, authentication cookies, license artifacts, private keys, certificate bundles, the exported appliance CA file, raw FortiGate backups, FortiGuard account material, unrelated screenshots, and all prior lesson directories.
