# Repository Structure

## Root-versus-lesson mapping

The repository root is **not a lesson**. It represents the entire FortiGate project and evolves as new lessons are completed.

```text
fortigate-76-security-lab/                 <- whole project
├── README.md                              <- overall project state
├── CHANGELOG.md
├── REPOSITORY_STRUCTURE.md
└── lessons/
    ├── 00-environment-setup/              <- Lesson 00
    ├── 01-system-network-admin-access/    <- Lesson 01
    ├── 02-firewall-policies-nat/          <- Lesson 02
    ├── 03-routing-static-routes-ecmp/      <- Lesson 03
    ├── 04-firewall-authentication/        <- Lesson 04
    ├── 05-antivirus-inspection/            <- Lesson 05
    ├── 06-web-filtering/                    <- Lesson 06
    ├── 07-<next-course-lab>/               <- future
    └── _template/
```

This mirrors the organization used by the FortiWeb project: the root summarizes the integrated project, while each lesson contains its own detailed implementation and evidence.

## Current realized structure

```text
.
├── README.md
├── CHANGELOG.md
├── REPOSITORY_STRUCTURE.md
├── .gitignore
└── lessons/
    ├── _template/
    │   └── README.md
    ├── 00-environment-setup/
    │   ├── README.md
    │   └── evidence/
    │       └── README.md
    ├── 01-system-network-admin-access/
    │   ├── README.md
    │   └── evidence/
    │       ├── README.md
    │       └── curated proof artifacts
    ├── 02-firewall-policies-nat/
    │   ├── README.md
    │   └── evidence/
    │       ├── README.md
    │       └── curated policy/NAT/VIP proof artifacts
    ├── 03-routing-static-routes-ecmp/
    │   ├── README.md
    │   └── evidence/
    │       ├── README.md
    │       ├── 19-final-dual-path-topology.png
    │       └── curated routing/policy/ECMP proof artifacts
    ├── 04-firewall-authentication/
    │   ├── README.md
    │   └── evidence/
    │       ├── README.md
    │       └── 15 curated authentication proof artifacts
    ├── 05-antivirus-inspection/
    │   ├── README.md
    │   ├── lab-files/
    │   │   ├── README.md
    │   │   └── benign.txt
    │   └── evidence/
    │       ├── README.md
    │       └── 20 curated AV/inspection proof artifacts
    └── 06-web-filtering/
        ├── README.md
        ├── lab-files/
        │   ├── README.md
        │   ├── allowed.html
        │   ├── blocked.html
        │   └── monitored.html
        └── evidence/
            ├── README.md
            └── 14 curated Web Filter proof artifacts
```

## Ownership rules

### Root `README.md`

The root README describes:

- the purpose of the full project
- the currently validated integrated architecture
- the list/status of completed lessons
- the project methodology
- the evidence standard
- the evaluation-license constraints

It stays concise compared with individual lesson documents.

### `lessons/NN-<name>/README.md`

Each lesson owns the detailed narrative for one implemented stage:

1. scope
2. starting state
3. architecture delta
4. exact configuration
5. verification plan and observed results
6. FortiGate diagnostics/control-plane state
7. troubleshooting and operational decisions
8. final validated result
9. cleanup/rollback
10. lessons learned
11. evidence

Lesson 02 expands this model with packet-capture evidence because NAT claims are strongest when the receiving endpoint proves the translated address it actually observed.

Lesson 03 expands it again by preserving sequential architecture states. The lesson distinguishes:

- the first routed path through R1
- the second routed path through R2
- Alpine's equal-cost return routing
- the correction from two different remote prefixes to one shared loopback destination
- FortiGate ECMP installation and per-source member selection
- negative results caused by interface state, missing policy, unsaved GUI state, and policy-interface mismatch

The detailed lesson must make clear which routes and policies were intermediate and which remained in the final state.

Lesson 04 returns to a deliberately compact narrative. It distinguishes:

- local active authentication that was implemented and validated
- LDAP, RADIUS, passive authentication, 2FA/FortiToken, and production HTTPS portal design that remain theory only
- the inherited broad policy that initially bypassed authentication
- the final identity-aware Policy ID `3`
- pre-authentication denial, post-authentication access, idle timeout, and user monitoring
- the temporary HTTPS attempt that failed TLS cipher negotiation and was fully rolled back

The lesson should explain the identity and policy reasoning without duplicating the full Lesson 03 routing build.

Lesson 05 continues the compact form. It distinguishes:

- policy inspection architecture (`flow-based` or `proxy-based`) from AV file handling (`stream` or proxy-only `legacy`)
- firewall-policy acceptance from a later antivirus/UTM denial
- harmless negative controls from the known-detectable EICAR positive control
- default file handling from the deliberately restrictive `L05-PROTO-1MB` experiment
- an oversized-file event from a malware verdict
- benign ZIP handling from detection inside an EICAR ZIP
- implemented local AV behavior from unavailable/current cloud-assisted FortiGuard and FortiSandbox services

The lesson reuses the authenticated Policy ID `3` and existing Alpine HTTP service instead of rebuilding routing or identity controls.

Lesson 06 continues the compact form. It distinguishes:

- policy authorization from a later Web Filter/UTM decision
- an unmatched allowed URL from explicit Monitor and Block entries
- flow and proxy feature-set profiles with identical local URL-filter intentions
- local static URL filtering from unavailable FortiGuard category rating
- static URL actions implemented in the lab from FortiGuard category actions retained as theory
- a `Simple` exact-match typo from a policy/profile attachment failure
- certificate inspection from deep inspection and the resulting HTTPS visibility boundary
- the observed disabled rating-service status from successful local URL filtering

The lesson reuses Policy ID `3`, `L05-AV-FLOW`/`L05-AV-PROXY`, the Alpine loopback HTTP service, and the existing identity mapping. It adds Web Filter profiles and three harmless reproducible HTML controls without consuming another policy.

### `lessons/NN-<name>/evidence/`

Contains only sanitized screenshots or small supporting artifacts directly associated with that level.

Do not use this directory as a dump of every screenshot taken while studying.

### `lessons/_template/README.md`

Template for future lessons. Copy it only when a new lesson is actually started.

## Project methodology

The Fortinet course is used as the curriculum, not as a sequence of GUI screenshots to reproduce.

A topic is implemented only when it adds meaningful lab behavior. Theory can remain theory.

The topology is cumulative wherever practical, and every experiment should preserve a known-good recovery path.

Lessons 02-06 reinforce several methodology rules:

- established management infrastructure is preserved until a later design intentionally repurposes it and records the new access path
- negative tests should change one match condition at a time
- logs and packet captures are preferred over GUI-only claims
- equivalent objects can share one policy when the security intent is genuinely identical
- a course example does not require a duplicate lab if the same mechanism has already been proven more meaningfully
- interface state and same-subnet adjacency are validated before remote routing
- forward routing and return routing are configured explicitly
- a FortiGate-originated ping is not treated as proof of client transit authorization
- ECMP requires equal eligible routes to the same destination prefix
- packet direction is interpreted literally: an ingress line is not outbound-member proof
- sequential reuse under an evaluation limit is documented rather than hidden
- authentication and authorization are kept distinct
- the protected application is validated before enforcing an identity condition
- source address and user/group are documented as simultaneous policy matches
- theory-only identity systems are labeled explicitly instead of being simulated without meaningful validation
- AV is tested with both a negative control and a deterministic positive control
- flow/proxy behavior is compared without incorrectly equating proxy inspection with legacy full-file AV
- Protocol Options limits are documented as inspection/resource boundaries
- signature age and subscription limitations remain visible in the conclusion
- Web Filtering is tested with unmatched allow, explicit Monitor, and explicit Block controls
- local static URL behavior is kept separate from FortiGuard category behavior
- feature-set compatibility is preserved when switching flow/proxy profiles sequentially
- exact URL-table state is checked before blaming policy, routing, or licensing
- disabled rating services and theory-only HTTPS inspection remain visible in the conclusion

## Evidence rule

A screenshot of a configured GUI object is not sufficient evidence by itself.

Where applicable, use three layers of proof:

1. **Configuration proof** - the intended FortiGate object exists.
2. **Data-plane/client proof** - traffic or endpoint behavior matches the intended state.
3. **Control-plane/security proof** - FortiGate routing, sessions, authentication, logs, or diagnostics identify why.

Negative/failure/security testing should be included when it materially strengthens the claim.

For NAT, packet capture at the receiving host is preferred because it proves which translated address reached the destination.

For ECMP, a FortiGate sniffer trace must identify the request's actual egress interface. Lesson 03 therefore distinguishes `port1 in` return traffic from the `port1 out` request that proves FortiGate selected the R2 member.

For firewall authentication, evidence should show the negative pre-authentication state, successful portal login, protected-resource access, the CLI/GUI user mapping, and timeout behavior. A login-page screenshot alone is not sufficient.

For antivirus, evidence should show the profile/policy state, the benign and EICAR client outcomes, and a FortiGate security event that explains the verdict. Forward Traffic evidence should retain the authenticated identity and selected ECMP path. Large-file and archive claims require paired baselines so a size or file-extension assumption cannot replace content-aware proof.

For Web Filtering, evidence should show the profile/policy attachment, the allowed/monitored/blocked client outcomes, and Web Filter events that identify the exact URL, profile, table index, and action source. A replacement page alone does not prove the intended profile matched. Exact-match troubleshooting should preserve both the incorrect URL-table state and the corrected result.

## Evaluation-license design rule

The permanent evaluation is restricted to three interfaces, firewall policies, and routes.

Future lessons may therefore:

- reuse existing objects
- reset a completed scenario before building another
- use separate EVE lab files
- temporarily replace a policy or route for a specific experiment
- combine address objects in one policy when the traffic has genuinely identical security intent

The repository must state when a configuration was reset or reused instead of implying that every temporary state coexisted simultaneously.

Lesson 03 applies this rule directly:

- port1 was repurposed from management/upstream connectivity to the R2 transit link
- management continued through port2/LAB-LAN
- intermediate routes to `10.20.20.0/24` and `10.40.40.0/24` were replaced by two routes to `10.60.60.100/32`
- one broad combined policy covered possible ECMP directions within the three-policy ceiling
- that broad policy is explicitly a constrained lab design, not a production recommendation

Lesson 04 reuses Policy ID `3` as `auth-lan-to-alpine`. Both ECMP egress interfaces remain in the rule, but source, authenticated group, destination, and service are narrowed to the lesson's security intent.

Lesson 05 continues to reuse Policy ID `3` and changes only its inspection/security-profile state between tests. `L05-PROTO-1MB` is an intentionally restrictive experiment and should not remain attached for ordinary continuation unless one-MiB blocking is explicitly required.

Lesson 06 also reuses Policy ID `3`. `L06-WF-FLOW` and `L06-WF-PROXY` are attached sequentially with the matching AV feature set. The final continuation design returns to flow inspection with `default` Protocol Options, `L05-AV-FLOW`, and `L06-WF-FLOW`. FortiGuard category features are not represented as deployed under the unlicensed evaluation.

## Sanitization rule

Never commit:

- FortiCare/FortiCloud passwords
- FortiGate administrator passwords
- raw VM license artifacts
- private keys
- unredacted secrets/tokens
- unsanitized appliance backup files
- screenshots containing reusable passwords
