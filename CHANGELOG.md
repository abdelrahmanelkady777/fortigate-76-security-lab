# Changelog

All notable lab milestones are documented here.

## 2026-09-02

### Lesson 08 - Intrusion Prevention and Application Control

- Preserved the Lesson 03 ECMP topology, Lesson 04 authenticated Policy ID `3`, and the Lesson 05-06 flow AV/Web Filter continuation; no new interface, route, or firewall policy was consumed.
- Restored Alpine's volatile addresses, loopback, remote-transit routes, equal-weight return route, and Python HTTP service before introducing inspection changes.
- Recorded IPS/Application/Proxy Application database `6.00741` and the 2015 malicious-URL database; bounded the lesson to deterministic EICAR and BitTorrent mechanics rather than current-threat claims.
- Created `L08-IPS-MONITOR` with exact `Eicar.Virus.Test.File` signature ID `29844`, enabled status, and packet logging.
- Proved Monitor delivered the complete 68-byte control while recording an IPS Accept event with profile, signature, URL, method, user/group, ingress, destination, and ECMP egress.
- Changed only the exact signature action to Block; proved the EICAR transfer failed while harmless `baseline.html` still returned HTTP `200` and the IPS result changed to Deny.
- Retained the sensor name across sequential states and documented that FortiGate enforces the configured entry action, not the descriptive object name.
- Tested a narrow IPS exemption, diagnosed that the signature matched in the server-response direction, reversed the pair to Alpine source/Kali destination, proved HTTP `200` and 68-byte delivery, then removed the exemption and restored blocking.
- Set botnet C&C checking to Monitor and used harmless traffic as a negative control; did not contact a live C&C destination.
- Left IPS malicious-URL blocking disabled because the installed database is stale and local URL filtering is already validated in Lesson 06.
- Created `L08-APP-MONITOR`, normalized every category to Monitor, enabled DNS logging and HTTP replacement messages, and left overrides, Network Protocol Enforcement, and non-default-port blocking empty/disabled for the baseline.
- Attached IPS and Application Control to Policy ID `3` alongside `L05-AV-FLOW` and `L06-WF-FLOW`, using flow inspection, `no-inspection`, all-session logging, and NAT disabled.
- Proved normal Firefox traffic was accepted and identified as `HTTP.BROWSER_Firefox`.
- Replaced the HTTP listener temporarily with a safe one-shot responder and sent a deterministic 68-byte BitTorrent handshake to TCP/80.
- Proved the firewall service remained HTTP while Application Control identified BitTorrent ID `6`, P2P category, and detected/Accept behavior from payload inspection.
- Added an exact BitTorrent Block override while leaving P2P Monitor and proved the same handshake was denied, demonstrating exact-application precedence over the category action.
- Added an exact Firefox Block override and validated the FortiGate Application Control replacement page; documented why non-HTTP BitTorrent traffic does not receive a friendly page merely because it uses TCP/80.
- Temporarily enabled non-default-port blocking and proved BitTorrent on TCP/80 was denied; correlated the same service/payload mismatch to Network Protocol Enforcement theory without claiming an independent NPE verdict.
- Removed temporary application overrides and non-default-port enforcement; retained all categories Monitor and NPE disabled in the final profile.
- Recorded a light-load performance baseline: 100% idle CPU, approximately 53.2% memory use, and sleeping `ipsengine`/`ipshelper` processes.
- Verified IPS global `fail-open disable` and documented the availability-versus-inspection-integrity tradeoff without inducing an engine failure.
- Added harmless baseline and BitTorrent responder files plus 23 curated configuration, client, event, troubleshooting, and health artifacts; excluded raw EICAR, credentials, cookies, private keys, backups, and license material.

## 2026-08-31

### Lesson 07 - SSL and Certificate Inspection

- Preserved the Lesson 03 ECMP topology, Lesson 04 identity-aware Policy ID `3`, Lesson 05 AV profiles, and Lesson 06 Web Filter profiles; no interface, route, or additional firewall-policy object was consumed.
- Defined Lesson 07 as configuration-led because the permanent evaluation operates with low encryption and the lab has no managed certificate infrastructure.
- Inspected the FortiGate certificate store and distinguished Local CA Certificate objects from Local Certificate objects.
- Examined `Fortinet_CA_SSL` and confirmed `CA:TRUE`, Certificate Sign key usage, SHA-256 fingerprinting, and a validity window ending in August 2036.
- Distinguished `Fortinet_CA_SSL` for normal inspection signing, `Fortinet_CA_Untrusted` for preserving an invalid-origin warning, and `Fortinet_GUI_Server` for management-plane HTTPS.
- Compared no inspection, SSL certificate inspection, and full SSL/deep inspection without representing certificate inspection as partial payload decryption.
- Compared outbound `Multiple Clients Connecting to Multiple Servers` with inbound `Protecting SSL Server`; recorded that the latter requires the protected server's certificate and private key.
- Created `L07-CERT-INSPECTION` with HTTPS/443 certificate inspection, malicious-certificate blocking, SNI checking, ECH blocking, custom invalid-certificate handling, and SSL anomaly logging.
- Customized `custom-deep-inspection` for outbound full SSL inspection using `Fortinet_CA_SSL` and an explicit `Lesson07 deep Inspection` comment.
- Restricted deep-inspection protocol mapping to HTTPS/TCP 443; left SMTPS, POP3S, IMAPS, FTPS, DNS over TLS, and SSH deep scan disabled.
- Configured HTTP/3 and DNS over QUIC to Block, documenting the intended TCP/TLS fallback without claiming it was traffic-tested.
- Configured expired, revoked, and validation-failed certificates to Block; retained `Keep Untrusted & Allow` for validation timeout; enabled SSL anomaly logging.
- Examined reputation, category, and FQDN/address exemption mechanisms, including Finance and Banking, Health and Wellness, and built-in application/update destinations.
- Temporarily selected `ALPINE-LOOPBACK` as an explicit exemption, then removed it from the normal target path so the lesson destination was not silently excluded from the deep-inspection design.
- Recorded cleanup of the accidental `alpineLoopBack` duplicate while retaining the established uppercase `ALPINE-LOOPBACK` object.
- Attached `custom-deep-inspection` to Policy ID `3` alongside the flow AV/Web Filter continuation; left decrypted traffic mirroring disabled and Security-events logging enabled.
- Downloaded `Fortinet_CA_SSL.cer`, examined the self-signed public CA certificate on Kali, and deliberately did not import it into the endpoint trust store.
- Documented certificate pinning, HSTS, mutual TLS, QUIC/HTTP/3, DNS over QUIC, ECH, privacy exemptions, and the inspection visibility lost when traffic is exempted.
- Explicitly skipped certificate/CSR/CA/remote-certificate/CRL import workflows, protected-server certificate deployment, endpoint trust, HTTPS traffic tests, and SSL log validation.
- Preserved Lesson 06 as the latest data-plane validated state; Lesson 07 claims configuration and design intent only.
- Added 12 curated certificate-store, SSL-profile, exemption, policy-attachment, and public-CA export artifacts while excluding private keys, raw backups, appliance-specific certificate files, credentials, cookies, and license material.

## 2026-08-26

### Lesson 06 - Web Filtering

- Preserved the dual-routed/ECMP topology, authenticated user, Alpine loopback application, and Policy ID `3`; no new interface, route, or firewall policy was consumed.
- Restored Alpine's volatile eth1/eth2/loopback addresses, equal-weight route to `10.10.10.0/24`, transit return routes, and Python HTTP listener.
- Removed the deliberately restrictive Lesson 05 continuation state by restoring flow inspection, `L05-AV-FLOW`, and `default` Protocol Options before introducing Web Filtering.
- Created harmless allowed, monitored, and blocked HTML controls under `/var/www/lesson04/lesson06`.
- Created flow profile `L06-WF-FLOW` with a Simple Block entry for `blocked.html` and a Simple Monitor entry for `monitored.html`; left `allowed.html` unmatched as the negative control.
- Attached `L06-WF-FLOW` to the existing identity-aware Policy ID `3` alongside `L05-AV-FLOW`.
- Proved the allowed control passed, Monitor returned HTTP `200` and produced an informational/passthrough event, and Block returned a FortiGate replacement page/HTTP `403`.
- Correlated flow events with the exact URLs, profile `L06-WF-FLOW`, URL-filter indexes, and `Local URLfilter Block` source.
- Diagnosed an initial failure caused by `/lesson6/blocked.html` in the Simple rule versus the actual `/lesson06/blocked.html` request.
- Verified that policy UTM/profile attachment was correct before inspecting the URL-filter table, then corrected one character and recovered the intended block.
- Created `L06-WF-PROXY` with the same corrected rules, sequentially switched Policy ID `3` to proxy inspection with `L05-AV-PROXY`, and repeated the Monitor/Block outcomes.
- Recorded that flow and proxy produced the same visible URL-filter decision; no unsupported performance or behavior difference is claimed.
- Ran `diagnose debug rating` and `get webfilter status`; Web-filter, Antispam, and Virus Outbreak Prevention reported disabled while local URL filtering remained functional.
- Kept FortiGuard category filtering, category Allow/Block/Monitor/Warning/Authenticate/Quota actions, web rating overrides, SSL certificate inspection, HTTPS deep inspection, and HTTPS inspection order as theory only.
- Returned the continuation design to flow mode with `L05-AV-FLOW`, `L06-WF-FLOW`, `default` Protocol Options, and NAT disabled.
- Added three harmless reproducible HTML controls and 14 curated evidence artifacts; excluded credentials, cookies, private keys, raw backups, and license material.

## 2026-08-24

### Lesson 05 - Antivirus and Inspection Modes

- Preserved the Lesson 03 dual-routed/ECMP topology and Lesson 04 identity-aware Policy ID `3`; no new interface, route, or firewall policy was consumed.
- Restored Alpine's volatile eth1/eth2/loopback addresses, ECMP return route, remote-transit routes, and Python HTTP service before introducing AV.
- Verified AV Engine `7.00054` and signed base/extended definitions `1.00000`; documented their 2018 age and the absence of current subscribed FortiGuard coverage.
- Created a 33-byte harmless text file as the negative control and the canonical 68-byte EICAR string as the deterministic positive control.
- Recorded exact byte counts and SHA-256 hashes so shell quoting or file corruption could not invalidate the test.
- Established the pre-AV baseline: both benign and EICAR files downloaded completely after active authentication.
- Diagnosed earlier 131-byte HTML downloads as expired-authentication responses rather than the requested artifacts.
- Created `L05-AV-FLOW` with Block action and HTTP inspection, attached it to the flow-based authenticated policy, and proved benign content passed while EICAR was reset/denied.
- Correlated the EICAR result with an Antivirus event showing infected/malicious content and with Forward Traffic details showing `lab-local-user`, `LAB-AUTH-USERS`, port2 ingress, port3/R1 egress, HTTP, and NAT `noop`.
- Validated the FortiGate replacement page identifying `EICAR_TEST_FILE` and the blocked URL.
- Created `L05-AV-PROXY`, temporarily switched Policy ID `3` to proxy inspection, and proved the same benign/blocked verdict with an immediate FortiGate `403 Forbidden` for EICAR.
- Confirmed the proxy AV profile used `set scan-mode default`; documented that proxy inspection architecture is not automatically legacy full-file AV.
- Documented flow/proxy as policy-processing modes and stream/legacy as AV file-handling modes.
- Created a harmless 2 MiB file and proved it downloaded completely with default Protocol Options.
- Created `L05-PROTO-1MB` with oversized logging, HTTP/80 mapping, one-MiB threshold, and oversized blocking.
- Proved the oversized flow transfer was reset near the threshold and the proxy transfer received `403 Forbidden`.
- Confirmed `Event Type: oversize` and profile `L05-PROTO-1MB`, distinguishing a size/resource decision from a malware verdict.
- Created paired benign and EICAR ZIP archives; the benign archive passed while the EICAR archive was blocked, proving content-aware archive inspection.
- Kept FortiSandbox, current cloud-assisted verdicts, external malware lists, EMS feeds, production HTTPS deep inspection, and deployed legacy AV as theory only.
- Added one harmless reproducible lab file, safe artifact-generation instructions, and 20 curated screenshots; raw EICAR/ZIP artifacts were intentionally excluded.
- Recorded the last evidenced checkpoint as proxy AV plus `L05-PROTO-1MB`, while recommending `default` Protocol Options and flow AV for normal continuation on the constrained evaluation VM.

## 2026-08-17

### Lesson 04 - Firewall Authentication

- Preserved the Lesson 03 dual-routed topology and used Alpine's `10.60.60.100/32` loopback as the protected destination; Alpine remained outside `LAB-LAN`.
- Restored volatile Alpine/router state and validated Kali/FortiGate reachability before adding authentication.
- Hosted a small protected page on `10.60.60.100:80` with Python because this Alpine BusyBox build did not include the `httpd` applet.
- Diagnosed why the first HTTP test bypassed authentication: the inherited policy matched all interfaces, sources, destinations, and services.
- Reused Policy ID `3` under the three-policy evaluation limit instead of creating an unavailable fourth rule.
- Created local user `lab-local-user` and firewall group `LAB-AUTH-USERS`; the password is excluded from the repository.
- Reused `KALI-CLIENT` and created `ALPINE-LOOPBACK` to retain explicit `/32` endpoint conditions.
- Narrowed Policy ID `3` to `auth-lan-to-alpine`: port2 ingress, port1/port3 ECMP egress, Kali source, authenticated group, Alpine loopback destination, HTTP/PING services, and NAT disabled.
- Proved the unauthenticated state: PING failed and HTTP was intercepted by the FortiGate authentication portal.
- Authenticated through the HTTP form portal and verified redirection to the Alpine protected resource.
- Confirmed `diagnose firewall auth list` mapped `lab-local-user` and `LAB-AUTH-USERS` to `10.10.10.100` with timers and traffic counters.
- Proved PING succeeded after HTTP created the authentication mapping, while documenting that ICMP itself cannot present an active login prompt.
- Verified five-minute `idle-timeout` behavior by observing the authentication portal return after inactivity.
- Correlated the GUI Firewall User Monitor with the CLI mapping and documented GUI deauthentication capability.
- Recorded the active authentication types, on-demand mode, timeout values, portal behavior, and certificate selection.
- Tested optional HTTP-to-HTTPS portal redirection to port `1003`; both available VM certificates produced `SSL_ERROR_NO_CYPHER_OVERLAP`.
- Refused to weaken browser cryptography, restored `Fortinet_Factory`, disabled `auth-secure-http`, and retained HTTPS portal hardening as theory only.
- Documented LDAP directory structure, LDAP versus RADIUS, RADIUS AAA/message flow, 2FA/FortiToken, passive authentication/FSSO, protocol behavior, and mixed-policy ordering as theory only.
- Marked LDAP and RADIUS explicitly as unimplemented; no identity server is claimed on Kali, Alpine, or Metasploitable.
- Added 15 curated evidence artifacts covering configuration, negative behavior, login, successful access, timeout, monitoring, settings, and the HTTPS rollback decision.

## 2026-08-15

### Lesson 03 - Routing, Static Routes, and ECMP

- Converted the directly attached Lesson 02 outside segment into a routed topology while preserving Alpine's established `10.20.20.100/24` address.
- Added `10.30.30.0/24` as the FortiGate-R1 transit network instead of reusing Alpine's endpoint subnet as a transit link.
- Corrected an Alpine address that had been created as `/32`, documented that Linux `ip addr` expects CIDR prefix notation, and brought eth1 administratively up.
- Configured R1 Gi0/0 as `10.20.20.1/24` and Gi0/1 as `10.30.30.2/24`.
- Added R1's return route to `10.10.10.0/24` through FortiGate at `10.30.30.1`.
- Added Alpine routes to LAB-LAN and the R1-FortiGate transit through `10.20.20.1`.
- Readdressed FortiGate port3 as `TRANSIT-R1` at `10.30.30.1/24`.
- Validated the lower path in layers: same-subnet adjacency, R1 forwarding, FortiGate static route, FortiGate-originated ping, then client transit.
- Configured the intermediate FortiGate route to `10.20.20.0/24` through `10.30.30.2` with distance `10`.
- Proved that a working route does not authorize transit: FortiGate could ping Alpine while Kali failed without a matching policy.
- Restored the `Lab-to-Alpine` port2-to-port3 PING policy with NAT disabled and then verified Kali-to-Alpine reachability at TTL `62`.
- Correlated the FortiGate CLI routing table with the GUI Routing Monitor and documented `[distance/metric]` output.
- Recorded route lookup, longest-prefix match, RIB/FIB, administrative distance, metric, FortiGate priority, and reverse-path context against the live topology.
- Documented static routes with named addresses, Internet Service routing, and the GUI Route Lookup tool as studied concepts, while clearly stating why no separate lab implementation was claimed.
- Preserved the Lesson 02 VIP evidence only as historical state; the publication design was not claimed as revalidated after the port3 topology change.
- Added R2 as the second routed path and repurposed FortiGate port1 from its former management/upstream role because the evaluation permits only three interfaces.
- Configured FortiGate port1 as `R2-Port1` at `10.50.50.1/24`.
- Configured R2 Gi0/0 as `10.50.50.2/24`, Gi0/1 as `10.40.40.1/24`, and added its return route to `10.10.10.0/24` through `10.50.50.1`.
- Added Alpine eth2 at `10.40.40.100/24` and verified both Alpine routed identities.
- Installed full iproute2 on Alpine with `apk add iproute2` to support multipath `nexthop` syntax.
- Configured Alpine's equal-weight route to `10.10.10.0/24` through both R1/eth1 and R2/eth2, plus explicit routes to the two remote FortiGate transit networks.
- Used `ip route get` with bound source addresses to confirm Alpine's lower- and upper-path selection.
- Documented that Alpine ECMP and FortiGate ECMP are independent routing decisions.
- Exposed and corrected an operational error where a GUI policy draft had not been saved with **OK**.
- Reused the available three-policy budget transparently; the combined bidirectional interface policy is documented as a lab-only compromise rather than production least privilege.
- Corrected the ECMP test design after recognizing that `10.20.20.100` and `10.40.40.100` are different destinations and therefore cannot form FortiGate ECMP.
- Added Alpine loopback `10.60.60.100/32` as one shared destination reachable through either routed member.
- Added R1's `/32` route through Alpine `10.20.20.100` and R2's `/32` route through Alpine `10.40.40.100`.
- Replaced the two intermediate FortiGate remote-network routes with two equal static routes to `10.60.60.100/32`: via R1 `10.30.30.2` on port3 and via R2 `10.50.50.2` on port1.
- Confirmed both FortiGate routes were installed with distance `10`, metric `0`, and equal priority, allowing FortiGate ECMP to form automatically.
- Verified the FortiGate itself could reach the shared loopback at TTL `63`.
- Diagnosed a Kali failure with `diagnose sniffer packet`: requests appeared only as `port2 in`, identifying a firewall-policy interface mismatch before any ECMP egress occurred.
- Added port3 to the combined policy's incoming and outgoing interface lists so either ECMP member could be authorized.
- Confirmed `set v4-ecmp-mode source-ip-based` in the FortiGate system settings.
- Proved source `10.10.10.100` used port3/R1 with `port3 out` packet-capture evidence.
- Correctly interpreted source `.101` as an asymmetric-return example: the request left port3 while Alpine's own ECMP decision returned through port1.
- Added temporary Kali alias `10.10.10.110/24` and proved the second FortiGate member with an explicit `port1 out` request capture.
- Recorded that equal source-IP-based ECMP does not alternate packets and that adjacent source addresses are not guaranteed to hash to different members.
- Discussed weight-based ECMP without claiming it was implemented; the completed lab retains equal weights and source-IP-based selection.
- Documented cleanup and persistence requirements for the temporary Kali address, live Alpine `ip` configuration, and Cisco running configurations.
- Embedded the latest dual-path topology in the root README and added 43 curated evidence artifacts covering configuration, success, failure, diagnosis, and correction.

## 2026-08-13

### Lesson 02 - Firewall Policies and NAT

- Preserved `port1` strictly as the protected management/recovery path and moved all transit experiments to `port2`/`port3`.
- Configured `port3` as `10.20.20.1/24`, alias `externalToAlpine`, role `WAN`, with no administrative access and no FortiGate DHCP service.
- Added lightweight Alpine Linux as the controlled outside host at `10.20.20.100/24` on a dedicated lab NIC.
- Kept Alpine's normal Internet/default route on its separate DHCP NIC and added only `10.10.10.0/24 via 10.20.20.1` for the FortiGate lab.
- Proved the implicit deny by showing Kali could route toward Alpine through its existing default gateway but could not transit FortiGate before a matching policy existed.
- Created `Lab-To-Outside` as the first `port2 -> port3` transit policy.
- Verified FortiGate stateful behavior: replies to a Kali-initiated session returned without a reverse policy, while a new Alpine-initiated session toward Kali remained blocked.
- Created and tested `KALI-CLIENT` and `ALPINE-OUTSIDE` address objects.
- Proved source matching with a correct `/32` and a deliberately wrong source object.
- Proved destination matching with a correct `/32` and a deliberately wrong destination object.
- Proved service matching by allowing `PING` and then showing the same ICMP flow fail when the policy service was changed to `SSH`.
- Created temporary `DENY-LAB-OUTSIDE` Policy ID `2` and proved first-match processing against `Lab-To-Outside` Policy ID `1`.
- Verified that moving policies changes sequence/precedence without changing their Policy IDs.
- Captured Forward Traffic logs showing accept by Policy ID `1` and deny by Policy ID `2` for the same source/destination flow.
- Studied flow-based versus proxy-based inspection and retained flow-based mode instead of creating an artificial proxy-inspection test.
- Validated outgoing-interface SNAT: Alpine observed source `10.20.20.1` instead of the internal Kali address.
- Created overload pool `SNAT-OVERLOAD` at `10.20.20.200` and proved translation with `tcpdump` on Alpine.
- Added Metasploitable to `LAB-LAN`; it obtained `10.10.10.101/24` and was represented by address object `MSF-CLIENT`.
- Expanded the existing outbound policy to include both Kali and Metasploitable instead of creating a redundant equivalent policy.
- Created one-to-one pool `SNAT-OneToOne`, extended it to `10.20.20.210-10.20.20.211`, and proved simultaneous multi-host translations with packet capture.
- Validated the Metasploitable HTTP backend locally before introducing DNAT.
- Created static VIP `MSF-WEB-VIP`: `10.20.20.220 -> 10.10.10.101`.
- Created inbound `OUTSIDE-to-MSF-WEB` policy from `port3 -> port2`, using the VIP object as destination and leaving policy SNAT disabled.
- Verified Alpine could retrieve the internal Metasploitable HTTP page through `10.20.20.220`.
- Created port-forward VIP `MSF-Web_PORTFWD`: `10.20.20.221:8080 -> 10.10.10.101:80`.
- Expanded the inbound policy to include both VIP objects instead of creating another equivalent inbound rule.
- Verified Alpine could retrieve the backend page through external TCP/8080.
- Proved VIP policy matching by replacing the VIP destination with the real backend object, observing failure, then restoring the VIP and recovering access.
- Recorded the design insight that one external IP can publish multiple internal services when distinct external ports uniquely identify the mappings.
- Deliberately skipped a separate outgoing static-NAT example because outbound source translation had already been demonstrated more meaningfully through outgoing-interface and IP-pool scenarios.
- Added curated, sanitized evidence for policy matching, Policy ID/sequence, logging, SNAT, IP pools, static VIP DNAT, and port forwarding.

## 2026-08-09

### Lesson 01 - System, Network, and Administrative Access Foundations

- Extended the Lesson 00 FortiGate with a persistent internal `LAB-LAN` on `port2`.
- Configured `port2` as `10.10.10.1/24`, alias `LAB-LAN`, role `LAN`.
- Added a FortiGate DHCP pool of `10.10.10.100-10.10.10.150`.
- Used Kali as the persistent internal administration/test workstation.
- Verified Kali received `10.10.10.100/24` dynamically and installed `10.10.10.1` as its default gateway.
- Observed and preserved the existing upstream default route on `port1` instead of creating a redundant route.
- Kept `port1` untouched because the upstream DHCP address/subnet can change with the host Wi-Fi/network.
- Enabled HTTPS, SSH, and PING on `port2` for controlled management testing.
- Created a separate `trusted-admin` account so Trusted Hosts testing could not lock out the original administrator.
- Verified successful login when the Trusted Host matched Kali at `10.10.10.100/32`.
- Verified authentication failure when the Trusted Host was changed to `10.10.10.99/32` while Kali remained `10.10.10.100`.
- Restored the final Trusted Host to `10.10.10.100/32`.
- Verified PING and SSH from Kali to the FortiGate.
- Added curated, sanitized evidence for the configuration, client behavior, routing state, and positive/negative security tests.

## 2026-08-08

### Lesson 00 - Environment Setup and Licensing

- Selected the official FortiGate x86-64 KVM new-deployment package for FortiOS 7.6.7.
- Imported `fortios.qcow2` into EVE-NG as `virtioa.qcow2`.
- Created the FortiGate node with 1 vCPU, 2048 MB RAM, and three interfaces.
- Completed first-login password setup.
- Verified FortiOS 7.6.7 build 3704 and interface state.
- Verified Internet reachability, DNS/FortiGuard reachability, and the default route.
- Recorded troubleshooting for the stalled GUI license-check page.
- Activated the permanent evaluation license through the CLI.
- Completed the post-license setup wizard.
- Reached the operational FortiOS dashboard.
- Recorded the permanent-evaluation resource, interface, policy, route, encryption, support, and FortiGuard limitations.
