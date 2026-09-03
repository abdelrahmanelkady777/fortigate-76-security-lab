# Lesson 09 Configuration Checkpoints

These files reconstruct the relevant final state without exporting complete appliance backups:

- `hq-fortigate.conf` - HQ interfaces, objects, route-based IPsec, route, and directional policies.
- `branch-fortigate.conf` - Branch interfaces, objects, route-based IPsec, route, and directional policies.
- `supporting-routing.txt` - R1 and Alpine cleanup/return-routing commands used to replace the old ECMP continuation.

The FortiGate policy/static-route `edit` values used for new objects are intentionally `0` where FortiOS can allocate an ID. Review existing IDs before applying. Replace `REPLACE_WITH_SHARED_SECRET` on both peers with the same strong secret.

The lab used `DES-SHA1` only because the permanent evaluation was operating in low-encryption mode. Replace it with a mutually supported modern proposal in production.
