# Lesson 01 Evidence

This directory contains curated, sanitized proof for Lesson 01. It is intentionally not a dump of every screenshot taken during the lab.

## Evidence index

| File | What it proves |
| --- | --- |
| `01-starting-topology.png` | Lesson 01 begins from the Lesson 00 single-uplink FortiGate state |
| `02-port2-address-cli.png` | FortiOS configuration contains `port2 = 10.10.10.1/24` |
| `03-role-alias.png` | `port2` has alias `LAB-LAN` and role `LAN` |
| `04-dhcp-config.png` | FortiGate DHCP is enabled with pool `10.10.10.100-10.10.10.150` |
| `05-kali-dhcp-route.png` | Kali received `10.10.10.100/24` dynamically and installed `10.10.10.1` as default gateway |
| `06-fortigate-routing-table.png` | Existing upstream default route is preserved and `10.10.10.0/24` is directly connected on `port2` |
| `07-trusted-admin-baseline.png` | `trusted-admin` can successfully reach the FortiGate GUI from Kali before source restriction |
| `08-trusted-host-allowed.png` | Final allowed Trusted Host is `10.10.10.100/32` |
| `09-trusted-host-denied-config.png` | Negative-test Trusted Host is deliberately changed to `10.10.10.99/32` while Kali remains `.100` |
| `10-trusted-host-denied-result.png` | FortiGate rejects authentication when the source does not match Trusted Hosts |
| `11-ping-validation.png` | Kali reaches `10.10.10.1` with 4/4 ICMP replies |
| `12-ssh-validation.png` | `trusted-admin` successfully reaches the FortiGate CLI over SSH |

## Evidence philosophy

Where possible, evidence should combine:

1. configuration proof
2. client/data-plane proof
3. FortiGate/control-plane or security-control proof

The Trusted Hosts test is the strongest example: the account, interface, and Kali client remain constant while only the source-match condition changes.

## Sanitization requirements

Never include:

- FortiGate administrator passwords
- FortiCare/FortiCloud credentials
- VM license data
- private keys
- reusable tokens/cookies
- unrelated personal information

The screenshots in this directory were selected because they contain no reusable password or activation secret.
