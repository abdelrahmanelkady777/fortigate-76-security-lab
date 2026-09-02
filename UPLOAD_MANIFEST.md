# GitHub Update Manifest

Apply this **delta-only Lesson 08 package** to the existing repository root.

The package contains only new or modified paths. It does not include cloned copies of Lessons 00-07, the `.git` directory, or an entire repository export.

## Replacement root files

- `README.md` - advance the integrated project to the data-plane-validated Lesson 08 state.
- `CHANGELOG.md` - record the IPS/Application Control implementation, tests, troubleshooting, cleanup, and evidence boundaries.
- `REPOSITORY_STRUCTURE.md` - add the Lesson 08 directory and its methodology/evidence rules.
- `UPLOAD_MANIFEST.md` - describe this delta-only update.

## New Lesson 08 content

- `lessons/08-ips-application-control/README.md` - implementation, theory tied to the lab, exact controls, troubleshooting, verification, final state, and embedded evidence.
- `lessons/08-ips-application-control/evidence/README.md` - curated evidence index and claim boundary.
- `lessons/08-ips-application-control/evidence/*.png` - 23 sanitized configuration, client, event, troubleshooting, and health artifacts.
- `lessons/08-ips-application-control/lab-files/README.md` - safe deployment and reproduction instructions.
- `lessons/08-ips-application-control/lab-files/baseline.html` - harmless HTTP negative control.
- `lessons/08-ips-application-control/lab-files/bittorrent-responder.py` - safe one-shot BitTorrent-handshake responder.

## Implemented and validated

1. Restored Alpine addressing, loopback, return routes, and the HTTP service.
2. Recorded the old IPS/Application database boundary before making security claims.
3. Created `L08-IPS-MONITOR` with exact EICAR signature `29844` and packet logging.
4. Proved EICAR Monitor delivered 68 bytes and generated an Accept event.
5. Changed only the EICAR action to Block and proved the transfer failed while benign HTTP remained `200`.
6. Correlated IPS events with the authenticated user/group, policy path, URL, method, signature, profile, and result.
7. Diagnosed request-versus-response direction in a narrow IPS exemption, corrected it, proved delivery, removed it, and restored blocking.
8. Retained botnet C&C Monitor as a harmless negative control and left stale malicious-URL enforcement disabled.
9. Created `L08-APP-MONITOR`, normalized all categories to Monitor, and attached it to Policy ID `3` with IPS/AV/Web Filter.
10. Proved Firefox identification and safe BitTorrent identification on TCP/80.
11. Proved service/port (`HTTP`) and payload application (`BitTorrent`) are independent classification layers.
12. Proved exact BitTorrent and Firefox Block overrides, including an HTTP Application Control replacement page.
13. Temporarily proved non-default-port blocking for BitTorrent/TCP-80.
14. Tied Network Protocol Enforcement theory to the same payload/service mismatch without claiming an independent NPE verdict.
15. Removed temporary overrides and non-default-port enforcement; retained all categories Monitor and NPE disabled.
16. Recorded light-load system/process performance and verified global IPS `fail-open disable`.

## Final retained state

| Component | State |
| --- | --- |
| Policy ID `3` | Identity-aware HTTP/PING; flow inspection; all-session logging; NAT disabled |
| Existing UTM | `L05-AV-FLOW`, `L06-WF-FLOW`, default Protocol Options |
| SSL inspection | `no-inspection` for this HTTP lesson |
| IPS | `L08-IPS-MONITOR`; EICAR Block; packet logging; no exemption; botnet C&C Monitor |
| IPS malicious URL | Disabled |
| Application Control | `L08-APP-MONITOR`; all categories Monitor; no exact/filter overrides |
| Non-default-port block / NPE | Disabled |
| DNS logging / HTTP replacement messages | Enabled |
| IPS fail-open | Disabled |

## Explicit claim boundary

The update does not claim:

- current production threat or application-signature coverage;
- contact with or detection of a live botnet C&C endpoint;
- IPS malicious-URL enforcement;
- an independent Network Protocol Enforcement verdict;
- high-load capacity or performance scaling;
- observed traffic behavior during an IPS engine failure;
- HTTPS payload inspection under the low-encryption evaluation.

## Packaging and sanitization

The update excludes the raw EICAR file, generated EICAR downloads, credentials, authentication cookies, license artifacts, private keys, certificate bundles, raw FortiGate backups, FortiGuard account material, unrelated screenshots, all prior lesson directories, and Git metadata.
