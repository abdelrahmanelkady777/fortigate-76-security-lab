# Lesson 07 - SSL and Certificate Inspection

Lesson 07 extends the authenticated, antivirus-inspected, and URL-filtered path from Lessons 04-06 with FortiGate certificate operations and SSL/SSH inspection profiles. The lesson deliberately focuses on how the FortiOS 7.6 GUI represents trust, certificate inspection, deep inspection, exemptions, certificate errors, modern encrypted transports, and policy attachment.

The evaluation VM permits these objects to be examined and configured, but its low-encryption license and the absence of a managed certificate infrastructure prevent a trustworthy end-to-end deep-inspection test. This is therefore a **configuration-led lesson**: the repository proves the configured control plane and records the intended packet behavior, but it does not claim successful TLS decryption, endpoint trust, inspected HTTPS content, or SSL security-event validation.

> Implementation boundary: certificate stores, inspection profiles, exemptions, validation actions, CA export, and Policy ID `3` attachment were configured or examined. Endpoint CA installation, HTTPS interception testing, server-certificate/private-key deployment, SSL log validation, and certificate/CSR/CRL import workflows were not performed.

## 1. Scope

### Objective

Understand how FortiGate decides whether to leave TLS encrypted, inspect only its certificate exchange, or perform full SSL inspection, and translate those decisions into reusable FortiOS profiles without overstating what the evaluation environment can prove.

### Configured and examined

- FortiGate certificate-store categories and certificate details
- the roles of `Fortinet_CA_SSL`, `Fortinet_CA_Untrusted`, and `Fortinet_GUI_Server`
- built-in SSL/SSH profile inventory and read-only versus editable objects
- editable certificate-inspection profile `L07-CERT-INSPECTION`
- editable full-inspection profile `custom-deep-inspection`
- outbound `Multiple Clients Connecting to Multiple Servers` mode
- inbound `Protecting SSL Server` mode and its server-certificate requirement
- malicious, untrusted, expired, revoked, validation-timeout, and validation-failed certificate handling
- SNI checking, Encrypted Client Hello, protocol/port mapping, HTTP/3, DNS over QUIC, and SSH deep scan controls
- category- and address-based SSL exemptions
- a temporary explicit `ALPINE-LOOPBACK` exemption demonstration
- `custom-deep-inspection` attachment to Policy ID `3`
- export and local examination of `Fortinet_CA_SSL.cer`

### Not performed

- installation of `Fortinet_CA_SSL` into Kali's trusted-root store
- browser, `curl`, HTTPS-server, AV-over-HTTPS, or Web-Filter-over-HTTPS testing
- proof that the evaluation VM decrypted application payloads
- SSL anomaly or deep-inspection log validation
- deployment of a protected HTTPS server certificate and private key
- certificate pinning, mutual-TLS, HSTS-failure, QUIC-fallback, or ECH-fallback traffic tests
- import of local certificates, CA certificates, remote certificates, CSRs, or CRLs
- production PKI, certificate lifecycle, revocation-service, or automated endpoint deployment

## 2. Methodology and design intent

This lesson keeps the repository's existing topology and security stack. Policy ID `3` remains the only policy attachment point under the three-policy evaluation ceiling. The new variable is the SSL/SSH inspection profile.

The working method is:

1. Inspect the appliance certificate store before selecting a signing identity.
2. Separate certificate roles before comparing inspection modes.
3. Examine certificate inspection before deep inspection.
4. Configure an editable profile instead of modifying read-only defaults.
5. Record protocol, validation, and exemption decisions explicitly.
6. Attach the profile to the existing policy without consuming another policy.
7. Treat a saved GUI object as configuration proof only.
8. Refuse to infer payload decryption from a dropdown selection or warning icon.
9. Preserve privacy, compatibility, and trust consequences as part of the control design.
10. State exactly which certificate-deployment and traffic-validation steps were skipped.

The intended outbound decision chain is:

```text
route and authenticated Policy ID 3 match
  -> SSL/SSH inspection profile is selected
  -> certificate inspection reads handshake/certificate metadata only
     OR full SSL inspection terminates and rebuilds TLS
  -> AV and Web Filter can inspect decrypted HTTPS only in the full-inspection case
  -> an exemption leaves the original TLS payload encrypted
```

That chain is architectural intent, not an observed data-plane result in this lesson.

## 3. Inherited state

Lesson 07 reuses the final Lesson 06 architecture:

| Component | Inherited state |
| --- | --- |
| Client | Kali `10.10.10.100/24` represented by `KALI-CLIENT` |
| Protected identity | `lab-local-user` in `LAB-AUTH-USERS` |
| Destination | Alpine loopback `10.60.60.100/32` represented by `ALPINE-LOOPBACK` |
| Transit | FortiGate ECMP through port3/R1 and port1/R2 |
| Policy | ID `3`, `auth-lan-to-alpine` |
| Services | `HTTP` and `PING` in the inherited validated path |
| Inspection architecture | flow-based |
| Antivirus | `L05-AV-FLOW` |
| Web Filter | `L06-WF-FLOW` |
| Protocol Options | `default` |
| NAT | disabled |

The inherited HTTP controls remain the latest **data-plane validated** application state. Lesson 07 adds SSL configuration without claiming that the existing HTTP application became an HTTPS server.

## 4. Certificate foundations

### 4.1 What a certificate proves

A digital certificate binds an identity, such as a DNS name or appliance name, to a public key. A certificate authority signs that binding. A client accepts it only when it can build a valid chain to a trusted CA and all relevant checks succeed.

Typical checks include:

- the issuer is trusted
- the digital signature is valid
- the current time is within the validity period
- the requested hostname matches the certificate identity
- the certificate is not revoked
- the certificate is allowed for its intended key usage

Encryption and identity are related but different: encryption protects confidentiality, while the signed certificate helps the client determine whose public key it is using.

### 4.2 Public key, private key, and digital signature

| Item | May be distributed? | Role |
| --- | --- | --- |
| Public certificate/public key | Yes | Lets others verify identity and signatures or encrypt to the owner |
| Private key | No | Proves possession of the identity and creates signatures/decrypts where applicable |
| CA signature | Included in the certificate | Lets clients verify that the issuing CA approved the identity-to-key binding |

FortiGate can export the public `Fortinet_CA_SSL` certificate to endpoints, but its private signing key must remain on the appliance. Possession of that private key is what lets FortiGate generate replacement certificates during deep inspection.

## 5. Certificate store inspection

`System -> Certificates` showed two important store categories:

| Store/category | Examples observed | Meaning |
| --- | --- | --- |
| Local CA Certificate | `Fortinet_CA_SSL`, `Fortinet_CA_Untrusted` | CA identities capable of signing or representing trust decisions |
| Local Certificate | `Fortinet_Factory`, `Fortinet_GUI_Server`, `Fortinet_SSL` variants | End-entity identities used by FortiGate services or cryptographic variants |

The details for `Fortinet_CA_SSL` showed:

- a FortiGate VM identity/subject
- a ten-year validity window ending in August 2036
- SHA-256 fingerprinting
- X.509 Basic Constraints `CA:TRUE`
- X.509 Key Usage `Certificate Sign`
- a self-signed root relationship, displayed by Kali as verified by itself

`CA:TRUE` and `Certificate Sign` are the decisive properties: this object is a CA, not merely a web-server certificate.

## 6. SSL inspection modes

### 6.1 Comparison

| Mode | FortiGate visibility | Payload decrypted? | Client trust requirement | Security-profile consequence |
| --- | --- | --- | --- | --- |
| No inspection | Network/session metadata | No | None added by FortiGate | Encrypted application content remains unavailable |
| SSL certificate inspection | TLS handshake, certificate, SNI when visible | No | Normally no replacement-site CA trust | Certificate and hostname decisions are possible; payload remains encrypted |
| Full SSL/deep inspection | Handshake plus decrypted application traffic | Yes, through two TLS sessions | Client must trust FortiGate's signing CA | AV, Web Filter, IPS, and similar controls can examine supported HTTPS content |

Certificate inspection is not “partial decryption.” FortiGate reads information available during the TLS setup and validates the server certificate, but it does not terminate and rebuild the application-data TLS tunnel.

Deep inspection acts as a controlled TLS intermediary:

```text
Client <- TLS session 1 -> FortiGate <- TLS session 2 -> Server
```

FortiGate validates the real server, creates a replacement certificate for the requested identity, signs it with its inspection CA, and presents that replacement to the client. This is why managed endpoints must trust the inspection CA.

### 6.2 Outbound versus protected-server direction

| GUI mode | Use case | Certificate requirement |
| --- | --- | --- |
| Multiple Clients Connecting to Multiple Servers | Internal users browsing many external HTTPS services | A signing CA such as `Fortinet_CA_SSL` dynamically signs replacement certificates |
| Protecting SSL Server | External clients access a known internal HTTPS server | FortiGate needs the protected server's certificate and private key |

`L07-PROTECT-SERVER` was created/examined to learn the second context. No suitable internal-server certificate/private key, inbound HTTPS publication policy, or protected HTTPS service was deployed, so it was not treated as a working reverse-inspection implementation.

## 7. SSL/SSH inspection profiles

The profiles were examined and edited under `Security Profiles -> SSL/SSH Inspection`.

### 7.1 Profile inventory

The GUI initially showed:

- read-only `certificate-inspection`
- editable `custom-deep-inspection`
- read-only `deep-inspection`
- read-only `no-inspection`

This distinction matters operationally: Fortinet defaults provide known baselines, while lesson-specific behavior belongs in an editable object.

### 7.2 `L07-CERT-INSPECTION`

An editable certificate-inspection profile was created with the following intent:

| Setting | Lesson state | Reason |
| --- | --- | --- |
| Direction | Multiple clients to multiple servers | Represents outbound user browsing |
| Inspection method | SSL Certificate Inspection | Validate handshake/certificate metadata without payload decryption |
| CA certificate | `Fortinet_CA_SSL` | Available FortiGate inspection CA for relevant generated responses |
| Malicious certificates | Block | Prevent known malicious certificate identities |
| Untrusted SSL certificates | Allow | Preserve availability while separate invalid-certificate actions remain explicit |
| Server certificate SNI check | Enable | Compare the requested SNI with certificate identity when available |
| HTTPS mapping | TCP/443 | Limit the studied mapping to standard HTTPS |
| Encrypted Client Hello | Block | Avoid losing hostname visibility to ECH |
| HTTP/3 | Bypass | Observe the certificate-inspection profile's non-decryption behavior |
| SSH deep scan | Off | Keep this lesson focused on TLS/certificates |
| Invalid certificates | Custom | Make each failure type explicit |
| Log SSL anomalies | On | Retain control-plane visibility when supported |

No HTTPS traffic was generated to validate this profile.

### 7.3 `custom-deep-inspection`

The editable built-in profile was customized as the lesson's full-inspection object.

#### Core SSL decisions

| Setting | Configured value |
| --- | --- |
| Comment | `Lesson07 deep Inspection` |
| Direction | Multiple clients connecting to multiple servers |
| Inspection method | Full SSL Inspection |
| CA certificate | `Fortinet_CA_SSL` |
| Malicious certificates | Block |
| Untrusted SSL certificates | Allow |
| Server certificate SNI check | Enable |
| SSL cipher compliance | Off |
| SSL negotiation compliance | Off |
| RPC over HTTPS | Off |
| MAPI over HTTPS | Off |

#### Protocol mapping

| Protocol | Configured behavior |
| --- | --- |
| Inspect all ports | Off |
| HTTPS | Enabled on TCP/443 |
| SMTPS | Off; default port 465 displayed |
| POP3S | Off; default port 995 displayed |
| IMAPS | Off; default port 993 displayed |
| FTPS | Off; default port 990 displayed |
| DNS over TLS | Off; default port 853 displayed |
| HTTP/3 | Block |
| DNS over QUIC | Block |
| SSH deep scan | Off |

This is a deliberate scope decision. Only standard HTTPS is mapped for inspection; encrypted mail, FTPS, DoT, and SSH are not silently claimed as covered.

Blocking HTTP/3 is intended to make capable clients fall back from QUIC/UDP 443 to inspectable HTTPS/TCP 443. Blocking DNS over QUIC prevents that encrypted transport from becoming a separate visibility bypass. Neither fallback was traffic-tested here.

#### Invalid-certificate actions

| Condition | Configured action | Design meaning |
| --- | --- | --- |
| Expired certificate | Block | Time validity has failed |
| Revoked certificate | Block | The issuing CA has withdrawn trust |
| Validation timed out | Keep Untrusted & Allow | Preserve availability without converting an unknown result into trust |
| Validation failed | Block | A definite validation failure is denied |
| Log SSL anomalies | Enabled | Record certificate/TLS anomalies when the platform can process them |

The distinction between timeout and failure is intentional: timeout means the result could not be obtained in time; validation failure means the check completed with a negative result.

## 8. SSL inspection exemptions

The profile exposed three exemption mechanisms:

| Mechanism | Use |
| --- | --- |
| Reputable websites | Broad reputation-based bypass where supported by rating services |
| Web categories | Privacy/compliance exceptions such as Finance and Banking or Health and Wellness |
| Address/FQDN objects | Precise application or destination exceptions |

The profile displayed category exemptions for `Finance and Banking` and `Health and Wellness`, plus built-in application/update destinations such as Adobe, Apple/App Store, Microsoft authentication/update, Citrix, Dropbox, Firefox update, and similar vendor FQDN objects.

`ALPINE-LOOPBACK` was temporarily added to the address exemptions to demonstrate an explicit destination bypass. It was then removed before the profile's normal policy attachment because leaving the lesson destination exempt would contradict the intent to study deep inspection. An accidental duplicate object named `alpineLoopBack` was treated as cleanup; the established uppercase `ALPINE-LOOPBACK` object remains the canonical Lesson 04 destination object.

`Log SSL exemptions` was enabled during the exemption study so an exempt match would remain observable on a fully capable deployment.

### What an exemption changes

An exemption does not remove the firewall policy or routing decision. It prevents FortiGate from decrypting that TLS payload.

- firewall-policy matching and routing still apply
- connection and some certificate metadata may remain visible
- the original client-to-server TLS session remains intact
- AV cannot scan encrypted file contents
- URL-path Web Filtering and application identification may lose visibility
- the exception creates a deliberate security-visibility gap and should be narrow

Exemptions are therefore compatibility/privacy decisions, not generic fixes for every failed inspection.

## 9. Application and transport compatibility

### 9.1 Certificate pinning

A pinned application expects a specific certificate or public key. A FortiGate-generated certificate can be trusted by the operating system and still fail the application's separate pin comparison.

```text
application expects original certificate/public key
  -> FortiGate presents a replacement certificate
  -> replacement does not match the pin
  -> application rejects the connection
```

Application-specific exemption is a common response when the application cannot be configured to support enterprise inspection.

### 9.2 HSTS

HTTP Strict Transport Security requires HTTPS, prevents downgrade to HTTP, and normally removes the user's ability to click through serious certificate errors. HSTS does **not inherently break deep inspection**: a correctly generated certificate still works when the endpoint trusts `Fortinet_CA_SSL`. If the inspection CA is untrusted or the generated identity is invalid, however, HSTS can turn the warning into a hard failure.

### 9.3 Mutual TLS

Mutual TLS authenticates both the server and the client. Because deep inspection splits one connection into two TLS sessions, direct client-certificate expectations can fail or require product/application-specific support. A narrow exemption may be required when direct end-to-end client authentication must remain intact.

### 9.4 QUIC, HTTP/3, and ECH

- HTTP/3 uses QUIC over UDP rather than ordinary HTTPS over TCP.
- DNS over QUIC creates another encrypted UDP path.
- ECH encrypts Client Hello information, including the true hostname normally exposed through SNI.

The deep-inspection profile blocks HTTP/3 and DNS over QUIC, while the certificate-inspection study blocks Encrypted Client Hello. The intended effect is to prevent modern encrypted transports from silently removing the hostname or payload visibility expected by the profile. Fallback behavior remains theoretical in this lab.

## 10. Three different certificate-warning situations

These warnings look similar in a browser but represent different trust relationships.

| Situation | Certificate involved | Meaning and response |
| --- | --- | --- |
| A valid website is deep-inspected but the endpoint does not trust FortiGate | `Fortinet_CA_SSL` | FortiGate generated the replacement site certificate. Install only the public inspection CA on managed endpoints in a production deployment. |
| The original website has an invalid certificate and the profile permits continued access | `Fortinet_CA_Untrusted` | FortiGate deliberately signs the replacement through an untrusted identity so the original warning is not hidden. Never distribute this CA as trusted. |
| The administrator browses to the FortiGate GUI | `Fortinet_GUI_Server` | This is the management-plane HTTPS identity. A self-signed issuer or IP/hostname mismatch can warn independently of transit inspection. |

The second behavior is especially important. If an expired, revoked, hostname-mismatched, or otherwise invalid server were re-signed by the normal trusted inspection CA without preserving the error, FortiGate would accidentally make a bad origin appear trustworthy. `Fortinet_CA_Untrusted` prevents that outcome when the profile allows the connection. If the configured invalid-certificate action is Block, the session is denied instead.

The GUI certificate is separate from both transit CAs. Replacing `Fortinet_GUI_Server` with a certificate for a real management FQDN can solve an administrative browser warning, but it does not establish endpoint trust for deep-inspected websites.

## 11. Exporting the inspection CA

`Fortinet_CA_SSL` was selected under `System -> Certificates` and downloaded as `Fortinet_CA_SSL.cer`. Kali's certificate viewer displayed:

- the FortiGate VM identity
- a self-signed/verified-by-itself relationship
- expiry in August 2036
- an X.509 certificate file of approximately 940 bytes

The file contains the public CA certificate, not the private key. It was examined but **not imported** into Kali's trusted-root store, so endpoint trust was not deployed or tested.

The appliance-specific `.cer` file is intentionally not committed. A public CA certificate is not secret, but this lab-specific object is not reusable and committing it could encourage accidental trust outside the intended appliance.

## 12. Firewall-policy attachment

Policy ID `3` remained the constrained lab's security-profile attachment point under `Policy & Objects -> Firewall Policy`. The lesson recorded:

| Policy field | Lesson 07 checkpoint |
| --- | --- |
| Inspection architecture | Flow-based continuation |
| Antivirus | `L05-AV-FLOW` |
| Web Filter | `L06-WF-FLOW` |
| SSL inspection | `custom-deep-inspection` |
| Decrypted traffic mirror | Off |
| Allowed-traffic logging | Security events |
| NAT | Disabled |

The warning icon beside SSL inspection represents certificate-trust/readiness consequences; it is not proof that the saved configuration failed. The profile attachment establishes policy intent only. No HTTPS session, decrypted payload, AV-over-HTTPS verdict, Web-Filter-over-HTTPS verdict, or SSL log was generated.

## 13. Certificate import workflows

FortiOS exposes local certificate, CSR, CA certificate, remote certificate, and CRL operations. They were deliberately skipped after the menu review and are not represented as implemented.

Conceptually:

- a local certificate identifies FortiGate or a protected service and normally has a private key
- a CSR asks a CA to sign a public-key identity while the private key remains with its creator
- a CA certificate establishes issuer trust
- a remote certificate represents another peer without giving FortiGate that peer's private key
- a CRL lists certificate serial numbers revoked before their normal expiry

No certificate or revocation object was imported for Lesson 07.

## 14. Troubleshooting and operational decisions

### 14.1 License boundary versus configuration failure

The GUI allowed inspection objects and policy attachment, but the permanent evaluation reports low-encryption operation and no FortiCare/FortiGuard subscription. The lab therefore stopped at configuration proof instead of interpreting an unavailable or unreliable deep-inspection test as a profile defect.

### 14.2 Duplicate address object

During the exemption exercise, `alpineLoopBack` was accidentally created alongside the existing `ALPINE-LOOPBACK`. Case and naming consistency matter because visually similar objects can hide wrong references. The canonical uppercase object was retained; the unused duplicate was designated for deletion after confirming zero references.

### 14.3 Do not exempt the target being studied

Adding `ALPINE-LOOPBACK` proved how an address exemption is selected. Keeping it exempt while claiming deep inspection of that same destination would invalidate the design. The explicit lab-target exemption was therefore temporary.

### 14.4 Do not trust the wrong CA

Only `Fortinet_CA_SSL` is intended for distribution to managed endpoints. Trusting `Fortinet_CA_Untrusted` would remove the warning mechanism designed to preserve an origin certificate failure.

## 15. Verification matrix

| Claim | Evidence type | Result |
| --- | --- | --- |
| FortiGate contains separate local CA and local certificate stores | GUI configuration | Confirmed |
| `Fortinet_CA_SSL` is a signing CA | Certificate details (`CA:TRUE`, Certificate Sign) | Confirmed |
| Certificate-inspection controls are available | GUI profile configuration | Confirmed |
| Deep-inspection controls, mappings, exemptions, and validation actions are available | GUI profile configuration | Confirmed |
| Explicit address exemption can be selected | GUI configuration | Confirmed, then removed from the normal target path |
| Deep-inspection profile is selectable on Policy ID `3` | Policy configuration | Confirmed |
| Public inspection CA can be exported | Downloaded certificate viewed on Kali | Confirmed |
| Kali trusts the inspection CA | Endpoint trust store | Not performed |
| FortiGate decrypts and rebuilds an HTTPS session | Data plane | Not tested |
| AV/Web Filter inspect decrypted HTTPS content | Client plus security logs | Not tested |
| HTTP/3/ECH fallback behaves as intended | Data plane | Not tested |
| Protecting-SSL-server mode works with a real server identity | Inbound HTTPS test | Not implemented |

This matrix is the lesson's central honesty boundary: configuration availability is not equivalent to validated enforcement.

## 16. Final state and continuation boundary

At the end of the lesson:

- `L07-CERT-INSPECTION` is retained as the certificate-inspection study object
- `custom-deep-inspection` contains the documented HTTPS-only full-inspection configuration
- the policy attachment to `custom-deep-inspection` is recorded as a configuration checkpoint
- `L07-PROTECT-SERVER` represents the studied inbound context but has no deployed server certificate/private key path
- `Fortinet_CA_SSL.cer` was downloaded and examined but not installed or committed
- `Fortinet_CA_Untrusted` was never distributed as trusted
- the explicit Alpine exemption was temporary
- data-plane validation remains complete through Lesson 06, not Lesson 07 TLS decryption

For ordinary continuation on this evaluation VM, use `no-inspection` when encrypted traffic must remain functional and reattach the Lesson 07 profile only when studying its GUI/configuration. A production deployment would use a managed enterprise CA, automated endpoint trust, narrow legal/compatibility exemptions, staged rollout, and application-specific validation.

## 17. Persistence and sanitization

The following are intentionally excluded:

- FortiGate private keys
- appliance certificate backups or PKCS#12 bundles
- the downloaded appliance-specific `Fortinet_CA_SSL.cer`
- administrator credentials, cookies, tokens, and license data
- raw FortiGate configuration backups
- screenshots unrelated to the lesson claims

Only sanitized GUI artifacts proving certificate inventory, profile decisions, policy attachment, exemptions, and public-CA export are committed.

## 18. Engineering takeaways

1. Certificate inspection and deep inspection are different controls, not weak and strong versions of the same decryption process.
2. Deep inspection creates two TLS sessions and therefore requires managed client trust.
3. A CA certificate can be distributed; its private signing key must remain protected.
4. `Fortinet_CA_SSL`, `Fortinet_CA_Untrusted`, and `Fortinet_GUI_Server` solve three different trust problems.
5. HSTS does not inherently defeat deep inspection, while certificate pinning can reject even a normally trusted replacement certificate.
6. Mutual TLS, QUIC, HTTP/3, and ECH must be considered explicitly rather than treated as ordinary HTTPS.
7. Exemptions preserve compatibility or privacy at the cost of payload visibility.
8. Blocking QUIC is an intended fallback design, not proof that fallback occurred.
9. A saved SSL profile and policy attachment prove configuration, not actual decryption.
10. License and PKI limitations belong in the result, not hidden in a footnote.

## 19. Evidence

See [`evidence/README.md`](evidence/README.md) for the curated artifact index and claim boundaries.
