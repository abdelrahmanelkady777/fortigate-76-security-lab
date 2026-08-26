# Lesson 06 Evidence Index

The evidence follows the repository's three-layer standard: configuration proof, client/data-plane behavior, and FortiGate security/log explanation. It also preserves one useful negative troubleshooting path.

| File | What it proves |
| --- | --- |
| `01-alpine-volatile-start.png` | Alpine rebooted with eth1/eth2 down, no lab addresses/routes, and no TCP/80 listener |
| `02-alpine-restored-ecmp-routes.png` | Connected lab networks, transit return routes, default route, and equal-weight route to `10.10.10.0/24` were restored |
| `03-http-control-files.png` | Harmless allowed, blocked, and monitored HTTP controls exist at the intended document-root path |
| `04-flow-policy-profile-cli.png` | Policy ID `3` retains identity-aware matching and attaches `L05-AV-FLOW` plus `L06-WF-FLOW` |
| `05-simple-url-typo-cli.png` | CLI exposes the incorrect `/lesson6/blocked.html` Simple entry |
| `06-typo-block-request-passed.png` | The actual `/lesson06/blocked.html` request passes while the configured pattern differs |
| `07-corrected-local-url-block-page.png` | Corrected exact match returns a FortiGate page identifying `Local URLfilter Block` |
| `08-flow-block-event-details.png` | Flow event records `L06-WF-FLOW`, the exact blocked URL, filter index `1`, and local block source |
| `09-flow-monitor-event-details.png` | Monitor event records `L06-WF-FLOW`, the exact monitored URL, filter index `2`, and informational/allowed behavior |
| `10-proxy-profile-feature-set.png` | `L06-WF-PROXY` uses the proxy feature set |
| `11-proxy-url-filter-entries.png` | Proxy profile contains enabled Simple Block and Monitor entries for the corrected URLs |
| `12-proxy-policy-attachment.png` | Policy ID `3` is sequentially switched to proxy mode with matching AV and Web Filter profiles |
| `13-proxy-client-results.png` | Proxy Monitor returns HTTP `200`; Proxy Block returns HTTP `403` |
| `14-fortiguard-rating-services-disabled.png` | `diagnose debug rating` and `get webfilter status` show the Web Filter rating service disabled |

## Deliberate exclusions

- Repetitive baseline screenshots are omitted after the inherited route, policy, authentication, and HTTP state was revalidated.
- An HTTPS/CA build is not included because it was not performed and was retained as theory only.
- No credentials, authentication cookies, VM license data, private keys, raw backups, or FortiGuard account material are included.
