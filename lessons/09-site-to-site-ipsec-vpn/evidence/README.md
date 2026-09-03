# Lesson 09 Evidence Index

The evidence is intentionally curated. Sanitized CLI checkpoints hold the detailed configuration; screenshots are retained only when they prove a distinct configuration, data-plane, control-plane, or troubleshooting claim.

| File | What it proves |
| --- | --- |
| `01-pre-vpn-negative-control.png` | Kali reaches HQ locally but Branch LAN returns Destination Net Unreachable before VPN routing exists |
| `02-gui-custom-vpn-error.png` | The first custom GUI submission failed twice with `-61: Input not as expected` |
| `03-hq-vpn-interface-route.png` | HQ remote-subnet route correctly selects `HQ-to-Branch` rather than physical `port1` |
| `04-branch-vpn-interface-route.png` | Branch remote-subnet route correctly selects `Branch-to-HQ` |
| `05-on-demand-first-packet.png` | First Kali echo is lost during on-demand negotiation; later echoes reach Alpine |
| `06-reverse-direction-success.png` | Alpine initiates a new session to Kali and receives all replies, validating reverse policies and routing |
| `07-tunnel-summary-sanitized.txt` | HQ control plane reports tunnel `HQ-to-Branch` with `1/1` Phase 2 selector up, without exposing the appliance prompt |

## Deliberate exclusions

- PSK-entry and full CLI screenshots are excluded because they contain secret or encrypted-secret material.
- The VM license/serial screen and status screenshots containing serial-derived default hostnames are excluded. The tunnel summary is retained as a sanitized text excerpt instead.
- Repetitive address-object, policy-editor, peer-ping, and successful-ping screens are omitted when the final configs and selected end-to-end results already prove the same state.
- The misleading physical-interface static-route drafts are discussed as troubleshooting but not retained as final configuration evidence.
- No claim is made that the underlay packet contents were captured as ESP because that optional capture was not performed.

## Claim boundary

The evidence proves one route-based, IKEv1, tunnel-mode site-to-site VPN with mirrored `/24` selectors, traffic-triggered establishment, and bidirectional PING. It does not prove production-strength cryptography, NAT traversal, certificate authentication, IKEv2, transport mode, policy-based VPN, remote-access FortiClient operation, redundant VPN failover, or mesh behavior.
