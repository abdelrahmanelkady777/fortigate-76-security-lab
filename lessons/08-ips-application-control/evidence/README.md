# Lesson 08 Evidence Index

The evidence follows the repository's three-layer standard: configuration proof, client/data-plane behavior, and FortiGate security/control-plane explanation.

| File | What it proves |
| --- | --- |
| `01-security-database-versions.png` | FortiOS version and the age of the IPS, Application, Proxy Application, and IPS malicious-URL databases |
| `02-alpine-restored-state.png` | Alpine addressing, return routes, HTTP listener, reachability, and benign baseline after volatile recovery |
| `03-ips-monitor-security-event.png` | EICAR signature `29844`, profile, method, URL, and Monitor-stage security event |
| `04-ips-monitor-identity-path.png` | Authenticated user/group plus port2 ingress, Alpine destination, and port3/R1 egress correlation |
| `05-ips-block-client-timeout.png` | EICAR transfer fails after the exact entry action changes to Block |
| `06-benign-baseline-http-200.png` | The harmless HTTP control remains reachable under the same policy and profiles |
| `07-ips-accept-deny-comparison.png` | Sequential Accept and Deny IPS outcomes for the same sensor and signature |
| `08-ips-exemption-request-direction.png` | Initial narrow exemption expressed in client-request direction |
| `09-ips-exemption-corrected-result.png` | Response-direction exemption allows HTTP `200` and the complete 68-byte control |
| `10-final-ips-sensor-gui.png` | Final EICAR Block, packet logging, zero exemptions, and botnet Monitor state |
| `11-final-ips-sensor-cli.png` | Final sensor configuration recorded in FortiOS CLI |
| `12-application-sensor-baseline-options.png` | Empty overrides, NPE/non-default-port controls off, and DNS/replacement options on |
| `13-firefox-monitor-event.png` | `HTTP.BROWSER_Firefox` is accepted and identified under Monitor |
| `14-bittorrent-server-received-68-bytes.png` | Alpine receives the complete deterministic BitTorrent handshake |
| `15-bittorrent-monitor-event-details.png` | BitTorrent ID `6`, P2P category, TCP protocol, HTTP service, and detected action |
| `16-exact-application-overrides.png` | Exact BitTorrent and Firefox Block overrides used for the specificity test |
| `17-bittorrent-deny-event.png` | The exact BitTorrent override changes the result to Deny |
| `18-firefox-application-block-page.png` | A blocked HTTP application receives an Application Control replacement page |
| `19-non-default-port-option.png` | Temporary non-default-port blocking is enabled |
| `20-non-default-port-bittorrent-deny.png` | BitTorrent on the HTTP port is denied during that experiment |
| `21-system-performance-baseline.png` | CPU, memory, traffic, and session baseline under light load |
| `22-ips-process-baseline.png` | `ipsengine` and `ipshelper` process state during the baseline sample |
| `23-ips-fail-open-disabled.png` | IPS global configuration retains `fail-open disable` |

## Deliberate exclusions

- The raw EICAR file is not committed because endpoint security may quarantine it.
- Repetitive log-list screenshots are omitted when a detailed event and client result already prove the decision.
- Temporary GUI steps are omitted when the final state and resulting traffic behavior are preserved.
- No credentials, authentication cookies, private keys, license artifacts, raw FortiGate backup, or FortiGuard account material are included.

## Claim boundary

The evidence proves deterministic EICAR and BitTorrent behavior on this FortiOS evaluation VM. It does not establish current production signature coverage, successful contact with a live botnet C&C service, an independent Network Protocol Enforcement verdict, high-load capacity, or behavior during an actual IPS engine failure.
