# Lesson 10 configuration references

[Lesson](../README.md) · [Evidence](../evidence/README.md)

These are focused reconstructions of the documented settings, not complete appliance exports or a one-shot deployment script. The baseline is [Lesson 09](../../09-site-to-site-ipsec-vpn/README.md): existing interface addressing, Phase 1 peers, original Branch-LAN selectors, and directional policies remain in place.

| File | Purpose |
| --- | --- |
| [hq-sdwan-reference.conf](hq-sdwan-reference.conf) | Loopback selector, zones, members, policy deltas, route definitions, manual preference, and SLA |
| [branch-loopback-reference.conf](branch-loopback-reference.conf) | Mirrored loopback selector and host route |
| [supporting-routing.txt](supporting-routing.txt) | Alpine runtime addressing/return routes and R1 host route |
| [verification.txt](verification.txt) | The targeted route, ping, tunnel-summary, and capture checks |

## Application order and object identity

1. Establish Alpine's loopback and supporting routes; check the adjacent gateways.
2. Add the mirrored `/32` Phase 2 selectors and the loopback address object. Extend the VPN policies as below.
3. Create HQ's two SD-WAN zones. Migrate direct interface references in existing policies/routes before enrolling port3 and the tunnel as members. The HQ route to `10.20.20.0/24` is not part of this checkpoint.
4. Configure member gateways, the two zone-based route definitions, and the manual rule. Test each preference using a fresh ping and capture.
5. Configure the member probe sources and the active performance SLA.

The files group settings by feature for readability; their section order is not an automatic migration sequence. Match existing objects before applying. HQ policy IDs `2`, `3`, `4` and member IDs `1`, `2` are from this lab. Preserve existing policy permissions and logging rather than creating duplicates.

Static routes use `edit 0` only as an **ID-neutral reference definition**. When updating an existing appliance, edit the matching destination's existing route instead; pasting the definitions repeatedly would create duplicates and consume the limited route budget. The manual rule uses its observed ID `1` without inventing a full name from the truncated GUI label.

## VPN policy address changes

Both firewalls retain the existing PING/HTTP VPN permissions and NAT disabled. Add the loopback without replacing the Branch-LAN address:

| Firewall / direction | Source addresses | Destination addresses |
| --- | --- | --- |
| HQ port2 → OVERLAY | HQ LAN `10.10.10.0/24` | Branch LAN `10.40.40.0/24` and `ALPINE-LOOPBACK` |
| HQ OVERLAY → port2 | Branch LAN and `ALPINE-LOOPBACK` | HQ LAN |
| Branch VPN → port2 | HQ LAN | Branch LAN and `ALPINE-LOOPBACK` |
| Branch port2 → VPN | Branch LAN and `ALPINE-LOOPBACK` | HQ LAN |

Use each firewall's existing address-object names; their capitalization can differ. Branch's policy IDs are intentionally not guessed. No additional reverse policy is needed just for replies to an established session.

The R1 path uses HQ's existing `FG-To-R1` policy with source `HQ-LAN`, destination `ALPINE-LOOPBACK`, and outgoing-interface SNAT. The packet capture confirms translation to `10.30.30.1`.

## Reference notes

- Phase 1 and its PSK are inherited, so no shared secret is included here.
- `DES-SHA1` records the low-encryption evaluation setting; do not deploy this legacy proposal in production.
- Member `source` configures health-check packet sourcing. It is distinct from policy NAT and the general local-out `preferred-source` setting.
- The manual reference records port3-first preference; the same rule was also tested with `priority-members 2 1`.

[Fortinet: zones in routes and rules](https://docs.fortinet.com/document/fortigate/7.6.5/administration-guide/270527/specify-an-sd-wan-zone-in-static-routes-and-sd-wan-rules) · [SD-WAN CLI fields](https://docs.fortinet.com/document/fortigate/7.6.5/cli-reference/838040159/config-system-sdwan)
