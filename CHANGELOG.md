# Milestone history

[Project overview](README.md) · Detailed procedures and experiments live in the linked lessons.

## 2026-09-08 — [Lesson 10: SD-WAN](lessons/10-sd-wan/README.md)

- Added the final case study: Alpine's shared loopback, mirrored additional IPsec selectors, `UNDERLAY`/`OVERLAY` zones, member gateways, and zone-based policies/routes.
- Documented manual path selection with client results and interface-level captures, including the SNAT return-path design and the narrow-filter visibility issue.
- Preserved the initial-echo observation as behavior consistent with on-demand SA establishment, rather than a universal packet-loss rule.
- Added active performance SLA settings, explicit probe sources, and the measured port3 sample.
- Added focused configuration references and curated evidence. Reorganized the root overview, reading guide, changelog, and upload manifest without relocating earlier lessons.

## 2026-09-03 — [Lesson 09: Site-to-site IPsec](lessons/09-site-to-site-ipsec-vpn/README.md)

- Introduced Branch FortiGate, mirrored route-based IPsec configuration, protected-subnet routes, and directional firewall policies.
- Validated traffic-triggered SA establishment and bidirectional HQ/Branch communication; published sanitized configuration and packet-cycle references.

## 2026-09-02 — [Lesson 08: IPS and Application Control](lessons/08-ips-application-control/README.md)

- Compared deterministic EICAR Monitor/Block/exemption behavior with packet-log correlation.
- Identified Firefox and BitTorrent, exercised application overrides and non-default-port enforcement, and recorded IPS health and failure-policy settings.

## 2026-08-31 — [Lesson 07: SSL and certificate inspection](lessons/07-ssl-certificate-inspection/README.md)

- Documented certificate roles and stores, certificate/deep-inspection profiles, validation actions, exemptions, public-CA export, and policy attachment.

## 2026-08-26 — [Lesson 06: Web filtering](lessons/06-web-filtering/README.md)

- Validated local HTTP allow, monitor, and block outcomes in flow/proxy profiles, supported by replacement pages and Web Filter logs.

## 2026-08-24 — [Lesson 05: Antivirus](lessons/05-antivirus-inspection/README.md)

- Used benign/EICAR controls to compare inspection modes and validate archive and oversized-file handling.

## 2026-08-17 — [Lesson 04: Firewall authentication](lessons/04-firewall-authentication/README.md)

- Validated local active authentication, identity-aware policy matching, authentication reuse, timeout, and user monitoring.

## 2026-08-15 — [Lesson 03: Routing and ECMP](lessons/03-routing-static-routes-ecmp/README.md)

- Built dual routed paths and shared-loopback tests; examined route attributes, return routing, policy interaction, and source-IP ECMP behavior.

## 2026-08-13 — [Lesson 02: Firewall policies and NAT](lessons/02-firewall-policies-nat/README.md)

- Validated stateful policies, matching order and logs, SNAT/IP pools, VIP destination translation, and port forwarding.

## 2026-08-09 — [Lesson 01: System and administration](lessons/01-system-network-admin-access/README.md)

- Established LAB-LAN, DHCP, client networking, management protocols, and positive/negative Trusted Hosts tests.

## 2026-08-08 — [Lesson 00: Environment](lessons/00-environment-setup/README.md)

- Established the EVE-NG FortiGate 7.6.7 evaluation environment and its resource/licensing baseline.
