# GitHub Update Manifest

Apply this **delta-only Lesson 06 package** to the existing repository root.

The package contains only new or modified paths. It does not include cloned copies of Lessons 00-05 or an entire repository export.

## Replacement root files

- `README.md` - advance the integrated project to Lesson 06 and summarize the final stacked identity/AV/Web Filter state.
- `CHANGELOG.md` - record local URL controls, flow/proxy tests, logs, exact-match troubleshooting, theory boundaries, and cleanup.
- `REPOSITORY_STRUCTURE.md` - add the Lesson 06 directory and Web Filter evidence/ownership rules.
- `UPLOAD_MANIFEST.md` - describe this delta-only update.

## New Lesson 06 content

- `lessons/06-web-filtering/README.md` - implementation, theory, commands, results, troubleshooting, final state, and engineering conclusions.
- `lessons/06-web-filtering/lab-files/README.md` - reproduction instructions and control-file roles.
- `lessons/06-web-filtering/lab-files/allowed.html` - harmless unmatched negative control.
- `lessons/06-web-filtering/lab-files/blocked.html` - harmless local Block control.
- `lessons/06-web-filtering/lab-files/monitored.html` - harmless local Monitor control.
- `lessons/06-web-filtering/evidence/README.md` - curated evidence index.
- `lessons/06-web-filtering/evidence/*.png` - 14 sanitized configuration, behavior, log, troubleshooting, and service-boundary artifacts.

## Implemented and validated

1. Restored Alpine's volatile dual-path network, loopback, return ECMP, and HTTP service.
2. Restored `default` Protocol Options and the flow AV baseline before enabling Web Filtering.
3. Created deterministic allowed, monitored, and blocked HTTP controls.
4. Created and attached `L06-WF-FLOW` to authenticated Policy ID `3`.
5. Proved unmatched allow, Monitor passthrough/logging, and Block replacement-page behavior.
6. Correlated exact URLs, profile, URL-filter indexes, and local action source in Web Filter events.
7. Diagnosed `/lesson6/` versus `/lesson06/` as a `Simple` exact-match failure.
8. Created `L06-WF-PROXY`, switched Policy ID `3` sequentially with the matching proxy AV profile, and repeated the same Monitor/Block intention.
9. Recorded Web Filter rating, Antispam, and Virus Outbreak Prevention services as disabled.
10. Returned the continuation design to flow inspection with `L05-AV-FLOW`, `L06-WF-FLOW`, and `default` Protocol Options.

## Theory-only boundary

- FortiGuard category filtering
- FortiGuard category actions: Allow, Block, Monitor, Warning, Authenticate, and Quota
- web rating overrides and custom category enforcement
- SSL certificate inspection configuration
- HTTPS deep inspection and trusted-CA deployment
- HTTPS inspection order and encrypted path visibility beyond conceptual analysis
- production FortiGuard connection remediation

## Final-state cautions

- Alpine addresses, routes, loopback state, and Python HTTP process remain volatile.
- `L05-PROTO-1MB` is retained as a completed Lesson 05 object but remains unattached.
- `L06-WF-PROXY` remains as a validated sequential object; ordinary continuation uses `L06-WF-FLOW`.
- The FortiGuard rating service is disabled, so category enforcement is not claimed.
- The three committed HTML controls are harmless and contain no executable content.

## Packaging and sanitization

The update excludes credentials, authentication cookies, license artifacts, private keys, raw FortiGate backups, FortiGuard account material, unrelated screenshots, and all prior lesson directories.
