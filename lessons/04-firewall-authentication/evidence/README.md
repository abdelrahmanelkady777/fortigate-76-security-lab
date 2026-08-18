# Lesson 04 Evidence Index

Only screenshots that prove a configuration, behavior, monitoring result, or useful troubleshooting conclusion are retained.

| File | What it proves |
| --- | --- |
| `01-alpine-http-listener.png` | Python HTTP service listening on `10.60.60.100:80` |
| `02-broad-policy-interfaces.png` | Inherited policy covered all FortiGate lab interfaces |
| `03-broad-policy-all-match.png` | Inherited policy used source/destination `all` and service `ALL` |
| `04-local-firewall-group.png` | `lab-local-user` is a member of `LAB-AUTH-USERS` |
| `05-auth-policy-interfaces.png` | Final policy uses port2 ingress and both ECMP egress members |
| `06-auth-policy-matches.png` | Source, group, destination, HTTP/PING, and NAT-disabled policy state |
| `07-unauthenticated-negative-test.png` | PING denied and HTTP intercepted before authentication |
| `08-authentication-portal.png` | FortiGate form-based active-authentication prompt |
| `09-protected-resource-after-auth.png` | Alpine resource loads after successful login |
| `10-cli-authenticated-user.png` | CLI IP-to-user mapping, group, timers, and counters |
| `11-post-auth-ping.png` | PING succeeds after HTTP authentication |
| `12-idle-timeout-reauthentication.png` | Portal returns after five idle minutes |
| `13-firewall-user-monitor.png` | GUI displays the same user/IP/group mapping |
| `14-active-auth-settings.png` | Recorded global authentication types and timers |
| `15-https-cipher-incompatibility.png` | Optional HTTPS redirect reached port 1003 but TLS negotiation failed |

## Sanitization

No reusable password, private key, license file, session token, or raw configuration backup is included. The HTTPS failure is retained only because it supports the decision to roll back and treat portal hardening as theory only.
