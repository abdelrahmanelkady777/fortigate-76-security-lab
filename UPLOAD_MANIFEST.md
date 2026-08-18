# GitHub Update Manifest

Apply this Lesson 04 package to the existing repository root.

## Root updates

- `README.md` - advance the integrated project to Lesson 04 and summarize the current identity-aware policy state.
- `CHANGELOG.md` - record the local active-authentication implementation, validation, theory boundaries, and HTTPS rollback.
- `REPOSITORY_STRUCTURE.md` - add the Lesson 04 directory and authentication evidence rules.
- `UPLOAD_MANIFEST.md` - describe this update package.

## New Lesson 04 content

- `lessons/04-firewall-authentication/README.md` - compact theory/implementation narrative.
- `lessons/04-firewall-authentication/evidence/README.md` - curated evidence index.
- `lessons/04-firewall-authentication/evidence/*.png` - 15 sanitized proof artifacts.

## Implemented and validated

1. Protected Python HTTP service on Alpine loopback `10.60.60.100:80`.
2. Diagnosis of the inherited broad policy that initially bypassed authentication.
3. Local user and firewall group.
4. Narrow identity-aware Policy ID `3` with both possible ECMP egress interfaces.
5. Unauthenticated PING denial and HTTP interception.
6. Browser form login and successful protected-resource access.
7. Post-authentication PING through the existing IP-to-user mapping.
8. Five-minute idle timeout and reauthentication.
9. CLI and GUI firewall-user monitoring.
10. Recording of effective global authentication settings.

## Theory-only boundary

- LDAP directory structure and FortiGate integration model
- RADIUS AAA, ports, shared secret, and response types
- server-based user/group authentication
- passive authentication/FSSO
- 2FA and FortiToken
- production HTTPS portal design

The temporary HTTPS redirect test is documented only as troubleshooting evidence. It failed TLS cipher negotiation and was rolled back. The final lab keeps `auth-secure-http disable`; no working HTTPS portal is claimed.

## Final-state cautions

- Alpine is external to `LAB-LAN`; Kali and Metasploitable remain the LAN-side hosts.
- Policy ID `3` is now `auth-lan-to-alpine`, not the inherited broad Lesson 03 policy.
- Alpine's network state and Python HTTP process may require restoration after reboot.
- LDAP and RADIUS were not installed on any lab host.
- The HTTP authentication portal is acceptable only in this isolated educational lab.

## Packaging and sanitization

The update contains documentation and curated screenshots only. It excludes credentials, license artifacts, private keys, reusable tokens, authentication cookies, raw backups, and unrelated screenshots.
