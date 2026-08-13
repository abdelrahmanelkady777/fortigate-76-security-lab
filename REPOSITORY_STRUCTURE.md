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
    ├── 03-<next-course-lab>/              <- future
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
    └── 02-firewall-policies-nat/
        ├── README.md
        └── evidence/
            ├── README.md
            └── curated policy/NAT/VIP proof artifacts
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

### `lessons/NN-<name>/evidence/`

Contains only sanitized screenshots or small supporting artifacts directly associated with that level.

Do not use this directory as a dump of every screenshot taken while studying.

### `lessons/_template/README.md`

Template for future lessons. Copy it only when a new lesson is actually started.

## Project methodology

The Fortinet course is used as the curriculum, not as a sequence of GUI screenshots to reproduce.

A topic is implemented only when it adds meaningful lab behavior. Theory can remain theory.

The topology is cumulative wherever practical, and every experiment should preserve a known-good recovery path.

Lesson 02 reinforces several methodology rules:

- management infrastructure is not repurposed merely because it already has connectivity
- negative tests should change one match condition at a time
- logs and packet captures are preferred over GUI-only claims
- equivalent objects can share one policy when the security intent is genuinely identical
- a course example does not require a duplicate lab if the same mechanism has already been proven more meaningfully

## Evidence rule

A screenshot of a configured GUI object is not sufficient evidence by itself.

Where applicable, use three layers of proof:

1. **Configuration proof** - the intended FortiGate object exists.
2. **Data-plane/client proof** - traffic or endpoint behavior matches the intended state.
3. **Control-plane/security proof** - FortiGate routing, sessions, authentication, logs, or diagnostics identify why.

Negative/failure/security testing should be included when it materially strengthens the claim.

For NAT, packet capture at the receiving host is preferred because it proves which translated address reached the destination.

## Evaluation-license design rule

The permanent evaluation is restricted to three interfaces, firewall policies, and routes.

Future lessons may therefore:

- reuse existing objects
- reset a completed scenario before building another
- use separate EVE lab files
- temporarily replace a policy or route for a specific experiment
- combine address objects in one policy when the traffic has genuinely identical security intent

The repository must state when a configuration was reset or reused instead of implying that every temporary state coexisted simultaneously.

## Sanitization rule

Never commit:

- FortiCare/FortiCloud passwords
- FortiGate administrator passwords
- raw VM license artifacts
- private keys
- unredacted secrets/tokens
- unsanitized appliance backup files
- screenshots containing reusable passwords
