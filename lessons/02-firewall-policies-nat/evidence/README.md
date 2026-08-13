# Lesson 02 Evidence

This directory contains curated, sanitized proof for Lesson 02 - Firewall Policies and NAT. It intentionally records only artifacts that prove a configuration state, packet behavior, policy decision, or address translation.

## Evidence index

| File | What it proves |
| --- | --- |
| `01-port3-outside-interface.png` | `port3` is the controlled outside interface at `10.20.20.1/24`, alias `externalToAlpine`, role WAN |
| `02-alpine-dual-homed-routing.png` | Alpine preserves its normal default route on `eth0` while routing `10.10.10.0/24` through `eth1` to FortiGate |
| `03-implicit-deny-baseline.png` | Kali has the correct default gateway but transit to `10.20.20.100` fails before a matching firewall policy |
| `04-first-firewall-policy.png` | Initial `Lab-To-Outside` policy defines the intended `port2 -> port3` forwarding direction |
| `05-service-matching-negative.png` | Correct source/destination plus `Service=SSH` does not match an ICMP ping |
| `06-policy-sequence-deny-first.png` | Moving `DENY-LAB-OUTSIDE (2)` above `Lab-To-Outside (1)` changes the traffic result without changing the IDs |
| `07-forward-traffic-policy-logs.png` | FortiGate logs attribute accept traffic to Policy 1 and denied traffic to Policy 2 |
| `08-outgoing-interface-snat.png` | Alpine sees source `10.20.20.1` after outgoing-interface SNAT |
| `09-overload-ip-pool-snat.png` | `SNAT-OVERLOAD` translates the source to `10.20.20.200` |
| `10-one-to-one-multi-host-snat.png` | Two simultaneous internal clients are represented by distinct one-to-one pool addresses `10.20.20.210` and `.211` |
| `11-static-vip-dnat.png` | Static VIP `10.20.20.220 -> 10.10.10.101` publishes the Metasploitable HTTP service to Alpine |
| `12-port-forward-config-policy.png` | Port-forward VIP translates external TCP/8080 to backend TCP/80 and is referenced by the inbound policy |
| `13-port-forward-success.png` | Alpine successfully retrieves the backend page through `10.20.20.221:8080` |

## Evidence philosophy

Lesson 02 deliberately uses multiple forms of proof:

1. **Configuration proof** - interfaces, policies, IP pools, and VIPs exist with the intended values.
2. **Data-plane proof** - ping, curl, and packet capture demonstrate what the endpoints actually experience.
3. **FortiGate decision proof** - Forward Traffic logs identify which policy accepted or denied the session.

The strongest experiments change one variable at a time. Examples include the wrong-source, wrong-destination, wrong-service, policy-order, and VIP-policy-destination negative tests.

## Sanitization requirements

Never include:

- FortiGate administrator passwords
- FortiCare/FortiCloud credentials
- VM license data
- private keys
- reusable tokens/cookies
- unrelated personal information

Screenshots that exposed reusable login credentials were sanitized before being added to this directory.
