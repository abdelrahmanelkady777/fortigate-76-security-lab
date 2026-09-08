# Lesson 10 evidence map

[Lesson](../README.md) · [Configuration references](../configs/README.md)

The PNGs are original lab screenshots, renamed for navigation and otherwise unchanged. Text files are explicitly labeled transcriptions of selected console excerpts, with serial-derived device prompts removed. Configuration references reconstruct settings; they are not presented as captured command output.

## What each artifact establishes

| Artifact | Evidence and interpretation |
| --- | --- |
| [01 — Zones](01-sdwan-zones.png) | port3 in UNDERLAY with gateway `10.30.30.2`; tunnel in OVERLAY with gateway `0.0.0.0`; both costs `0` |
| [02 — Policy migration](02-policy-zone-migration.png) | The three HQ policies reference SD-WAN zones; a configuration checkpoint during interface migration |
| [03 — Zone-based routes](03-zone-route-configuration.png) | The Branch `/24` references OVERLAY; a single loopback `/32` entry references both zones |
| [03 — Active route lookup](03-route-lookup-sanitized.txt) | The loopback has both port3/R1 and tunnel candidates; Branch LAN has the tunnel candidate |
| [04 — Overlay selection](04-overlay-selected.png) | The manual rule's GUI selected-route marker identifies `HQ-to-Branch` |
| [05 — Overlay ping](05-overlay-ping.png) | Five transmitted, four received; replies start at sequence 2 |
| [06 — Overlay capture](06-overlay-capture-sanitized.txt) | Inner ICMP crosses port2 and `HQ-to-Branch` without source translation |
| [07 — Routed-path preference](07-underlay-preference.png) | Manual preference reordered to port3 first, tunnel second |
| [08 — Routed-path ping](08-underlay-ping.png) | Five transmitted, five received, 0% loss |
| [09 — NAT-aware capture](09-underlay-capture-sanitized.txt) | Narrow filter shows port2 only; broader filter reveals port3 SNAT to `10.30.30.1` and reverse translation |
| [10 — SLA target](10-sla-target-participants.png) | Active Ping to `10.60.60.100`; both members specified as participants |
| [11 — SLA criteria](11-sla-thresholds-timers.png) | Thresholds `30 ms / 10 ms / 10%`, `500 ms` interval, `5/5` state checks, static-route action enabled |
| [12 — SLA sample](12-sla-port3-measurement.png) | port3 measured `1.65 ms` latency, `0%` loss, `0.85 ms` jitter |
| [13 — Member/source excerpts](13-member-sources-sanitized.txt) | Member IDs and explicit health-check sources `10.30.30.1` / `10.10.10.1` |
| [14 — Selector excerpts](14-selector-checkpoints-sanitized.txt) | Mirrored loopback selectors, on-demand settings, and a separately labeled `2/1` selector-count checkpoint |

Settings screenshots establish configuration choices; ping/capture/telemetry artifacts establish the corresponding observations. The SLA measurement belongs to port3. Repeated interface observations of one echo are not additional transmitted pings.

<details>
<summary>Original screenshot provenance</summary>

| Repository artifact | Original screenshot filename |
| --- | --- |
| 01 | `39b4e2a1-5c70-4e38-a972-c38a2a640a19.png` |
| 02 | `184c86b8-f16f-4b08-b34c-c17841c43a57.png` |
| 03 zone routes | `0a69b49a-1176-4473-83d7-2605c3e13922.png` |
| 03 route lookup | `1b93f6d1-f4ed-4cd5-be39-efd76942ff63.png` |
| 04 | `42d2a006-2476-4b4d-89e4-2b9dea7ff17a.png` |
| 05 | `f689f1aa-996c-4cfa-bd0f-7e5038fc13ad.png` |
| 06 | `9bbea759-c8ef-40b5-84a1-fe228f5030a0.png` |
| 07 | `53ab3b1d-a3af-4405-aed9-14ec21bb6398.png` |
| 08 | `a38e3fce-369a-49b1-9903-33dce5fea82d.png` |
| 09 narrow / broad | `3e2a46a2-b4ba-46cc-bc31-2601879b6add.png` / `2d249b5d-6f35-41ca-98dd-8d7071dc6985.png` |
| 10 | `9277423c-bc07-410f-a9f0-088250c83e74.png` |
| 11 | `218598dc-3a2a-4b79-9f0a-986172c6c5c5.png` |
| 12 | `235e0808-faa0-432d-acc3-2ac22faa1d46.png` |
| 13 members / sources | `1a29fdfa-6e65-40d0-ad42-c2c4bf94dd66.png` / `36eb3ef3-d728-4fed-96fb-420afb779909.png` |
| 14 HQ / Branch / count | `c8ec8fe9-a28c-4125-aa75-42baf4c8eb30.png` / `059baa1b-683d-4aa0-af86-a78034c61f46.png` / `c5340033-5b0d-4517-ae3e-506ae06c2473.png` |

</details>
