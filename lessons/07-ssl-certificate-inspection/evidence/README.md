# Lesson 07 Evidence Index

These artifacts document the FortiOS 7.6 certificate and SSL/SSH inspection configuration studied in Lesson 07. They are **configuration evidence**, except for the public-CA download artifact. No screenshot is presented as proof that the evaluation VM decrypted HTTPS traffic.

| # | Artifact | What it proves |
| --- | --- | --- |
| 01 | [`01-certificate-store-inventory.png`](01-certificate-store-inventory.png) | Separate Local CA Certificate and Local Certificate inventories, including `Fortinet_CA_SSL`, `Fortinet_CA_Untrusted`, and `Fortinet_GUI_Server` |
| 02 | [`02-fortinet-ca-ssl-details.png`](02-fortinet-ca-ssl-details.png) | `Fortinet_CA_SSL` validity, SHA-256 fingerprint, `CA:TRUE`, and Certificate Sign key usage |
| 03 | [`03-ssl-ssh-profile-inventory.png`](03-ssl-ssh-profile-inventory.png) | Read-only certificate/deep/no-inspection defaults and editable `custom-deep-inspection` inventory |
| 04 | [`04-certificate-inspection-options.png`](04-certificate-inspection-options.png) | Outbound certificate-inspection mode, CA selection, malicious/untrusted decisions, and SNI checking controls |
| 05 | [`05-certificate-inspection-validation-options.png`](05-certificate-inspection-validation-options.png) | HTTPS/ECH, HTTP/3, SSH deep scan, invalid-certificate actions, and anomaly logging controls |
| 06 | [`06-custom-deep-inspection-core.png`](06-custom-deep-inspection-core.png) | `custom-deep-inspection` full-inspection method, `Fortinet_CA_SSL`, malicious/untrusted behavior, and SNI setting |
| 07 | [`07-custom-deep-inspection-protocols.png`](07-custom-deep-inspection-protocols.png) | HTTPS-only mapping and HTTP/3/DNS-over-QUIC blocking |
| 08 | [`08-deep-inspection-exemptions.png`](08-deep-inspection-exemptions.png) | Category and application/FQDN exemption mechanisms |
| 09 | [`09-invalid-certificate-actions.png`](09-invalid-certificate-actions.png) | Custom expired, revoked, validation-timeout, validation-failed, and anomaly-log behavior |
| 10 | [`10-explicit-address-exemption.png`](10-explicit-address-exemption.png) | Selection of the canonical `ALPINE-LOOPBACK` object as a temporary explicit exemption demonstration |
| 11 | [`11-policy-deep-inspection-attachment.png`](11-policy-deep-inspection-attachment.png) | `custom-deep-inspection` selected on the existing policy, decrypted traffic mirroring off, and Security-events logging |
| 12 | [`12-downloaded-inspection-ca.png`](12-downloaded-inspection-ca.png) | `Fortinet_CA_SSL.cer` downloaded and opened on Kali without being imported into its trust store |

## Claim boundary

The evidence supports:

- certificate-role identification
- profile availability and saved settings
- exemption configuration
- firewall-policy attachment
- export of the public inspection CA certificate

The evidence does **not** support:

- successful TLS interception or payload decryption
- endpoint trust in `Fortinet_CA_SSL`
- AV, Web Filter, IPS, or application inspection of HTTPS payloads
- tested QUIC/ECH fallback
- protected-server SSL inspection
- certificate pinning, HSTS, or mutual-TLS compatibility
- production readiness under the evaluation license

The downloaded `.cer` file itself is excluded because it is appliance-specific and should not be imported as a trusted root outside the intended lab appliance.
