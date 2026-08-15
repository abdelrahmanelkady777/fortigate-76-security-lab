# GitHub Update Manifest

Apply this Lesson 03 package to the existing repository root.

## Root updates

- `README.md` - advance the integrated project to Lesson 03, document the final dual-path state, and display the latest topology screenshot.
- `CHANGELOG.md` - add the complete 2026-08-15 Lesson 03 implementation and troubleshooting record.
- `REPOSITORY_STRUCTURE.md` - add the realized Lesson 03 directory and routing/ECMP evidence rules.
- `UPLOAD_MANIFEST.md` - describe this update package.

## New Lesson 03 content

- `lessons/03-routing-static-routes-ecmp/README.md` - full routing, static-route, policy, Alpine routing, loopback, and ECMP implementation narrative.
- `lessons/03-routing-static-routes-ecmp/evidence/README.md` - curated evidence index and interpretation notes.
- `lessons/03-routing-static-routes-ecmp/evidence/*.png` - 43 curated proof artifacts.

## Major states represented

1. Inherited Lesson 02 directly connected outside topology.
2. First real routed path through R1.
3. Alpine address-prefix and interface-state troubleshooting.
4. FortiGate static routing versus transit-policy behavior.
5. Second routed path through R2 after port1 repurposing.
6. Alpine dual-interface routing and equal-weight return ECMP.
7. Intermediate proof to Alpine's separate lower and upper addresses.
8. Correction to one shared loopback destination for valid FortiGate ECMP.
9. Equal FortiGate static routes to `10.60.60.100/32` through R1 and R2.
10. Policy-interface mismatch diagnosis and correction.
11. Source-IP-based ECMP proof with `port3 out` and `port1 out` captures.

## Final-state cautions

- FortiGate port1 is no longer the management interface; it is `R2-Port1` at `10.50.50.1/24`.
- The older FortiGate routes to `10.20.20.0/24` and `10.40.40.0/24` are intermediate states, not final installed routes.
- The two final static members both target `10.60.60.100/32` and use equal distance, metric, and priority.
- Alpine and FortiGate each perform their own ECMP selection.
- The temporary Kali address `10.10.10.110/24` exists only as a path-selection probe and should be removed after testing.
- The broad combined policy is a lab workaround for the three-policy evaluation limit, not a production policy recommendation.
- Weight-based ECMP was not configured.
- The earlier Lesson 02 VIPs are historical and were not revalidated after the topology redesign.

## Packaging and sanitization

The update contains documentation and curated screenshots only. It excludes credentials, license artifacts, private keys, reusable tokens, unsanitized backups, and unrelated files.
