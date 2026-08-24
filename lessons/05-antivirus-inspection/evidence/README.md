# Lesson 05 Evidence Index

The evidence follows the repository's three-layer standard: configuration proof, client/data-plane behavior, and FortiGate security/log explanation.

| File | What it proves |
| --- | --- |
| `01-av-engine-and-signature-versions.png` | Signed AV engine exists; base and extended signature sets are old and unsubscribed |
| `02-benign-and-eicar-test-files.png` | Harmless negative control and exact 68-byte EICAR positive control exist on Alpine |
| `03-pre-av-baseline-downloads.png` | Both controls pass before AV enforcement |
| `04-flow-av-profile.png` | `L05-AV-FLOW` blocks detected HTTP content using the flow feature set |
| `05-flow-policy-attachment.png` | Flow inspection and `L05-AV-FLOW` are attached to Policy ID `3` |
| `06-flow-eicar-block.png` | Benign content passes; EICAR causes a reset/denial under flow inspection |
| `07-av-event-details.png` | FortiGate records an infected/malicious event for `eicar.com.txt` |
| `08-forward-log-identity-and-egress.png` | The same traffic is correlated with the authenticated user, port2 ingress, port3/R1 egress, HTTP, and NAT `noop` |
| `09-proxy-av-profile.png` | `L05-AV-PROXY` uses Block, proxy feature set, and HTTP inspection |
| `10-proxy-policy-attachment.png` | Policy ID `3` is temporarily switched to proxy inspection with `L05-AV-PROXY` |
| `11-proxy-eicar-block.png` | Proxy inspection permits the benign file and returns `403 Forbidden` for EICAR |
| `12-antivirus-block-page.png` | FortiGate replacement page identifies `EICAR_TEST_FILE` and the blocked URL |
| `13-large-file-default-baseline.png` | The complete 2 MiB harmless file passes with default Protocol Options |
| `14-protocol-options-name-and-log.png` | Custom profile name, oversized logging, and HTTP/80 mapping |
| `15-protocol-options-oversize-threshold.png` | Oversized blocking enabled with an intentional 1 MiB threshold |
| `16-flow-oversize-reset.png` | Flow inspection releases about 1 MiB and then resets the oversized transfer |
| `17-proxy-oversize-block.png` | Proxy inspection returns `403 Forbidden` for the same oversized file |
| `18-oversize-security-event.png` | Event type `oversize` identifies size—not malware—as the blocking reason |
| `19-compressed-test-archives.png` | Benign and EICAR ZIP controls contain the intended inner files |
| `20-compressed-av-results.png` | Benign ZIP passes while the EICAR ZIP is blocked |

## Deliberate exclusions

- The raw EICAR string and `eicar.zip` are not committed because endpoint security may quarantine them.
- No reusable passwords, cookies, private keys, license files, or raw FortiGate backup are included.
- Repetitive log-list screenshots are omitted when a detailed event already proves the claim.
