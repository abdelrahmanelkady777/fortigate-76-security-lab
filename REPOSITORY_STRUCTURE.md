# Repository Structure

## Root-versus-lesson mapping

The repository root is **not Lesson 00**. It represents the entire FortiGate project and evolves as new lessons are completed.

```text
fortigate-76-security-lab/          <- whole project
├── README.md                       <- overall project state
├── CHANGELOG.md
├── REPOSITORY_STRUCTURE.md
└── lessons/
    ├── 00-environment-setup/       <- Lesson 00 only
    ├── 01-<first-course-lab>/      <- future Lesson 01
    ├── 02-<second-course-lab>/     <- future Lesson 02
    └── _template/
```

This mirrors the organization used by the FortiWeb project: the root summarizes the integrated project, while each lesson contains its own detailed implementation and evidence.

This repository follows the incremental documentation model used for the FortiGate 7.6 EVE-NG lab.

## Initial structure

```text
.
├── README.md
├── CHANGELOG.md
├── REPOSITORY_STRUCTURE.md
├── .gitignore
└── lessons/
    ├── _template/
    │   └── README.md
    └── 00-environment-setup/
        ├── README.md
        └── evidence/
            └── README.md
```

## Ownership rules

### Root `README.md`

The root README describes:

- the purpose of the full project
- the currently validated FortiGate base environment
- the list/status of completed lessons
- the evidence standard
- the evaluation-license constraints

It should stay concise compared with the individual lesson documents.

### `lessons/NN-<name>/README.md`

Each lesson owns the detailed narrative for one implemented capability:

1. scope
2. starting state
3. architecture delta
4. exact configuration
5. verification plan
6. FortiGate diagnostics/logs
7. troubleshooting
8. final validated result
9. rollback
10. lessons learned
11. evidence

### `lessons/NN-<name>/evidence/`

Contains only sanitized screenshots or small supporting artifacts directly associated with that level.

Do not use this directory as a dump of every screenshot taken while studying.

### `lessons/_template/README.md`

Template for future lessons. Copy it only when a new lesson is actually started.

## Evidence rule

A screenshot of a configured GUI object is not sufficient evidence by itself.

Where applicable, use three layers of proof:

1. **Configuration proof** - the intended FortiGate object exists.
2. **Data-plane proof** - traffic behaves as expected.
3. **Control-plane proof** - FortiGate logs, sessions, routing, VPN state, authentication state, or diagnostics identify why.

## Evaluation-license design rule

The permanent evaluation is restricted to three interfaces, firewall policies, and routes.

Future lessons may therefore:

- reuse existing objects
- reset a completed scenario before building another
- use separate EVE lab files
- temporarily replace a policy or route for a specific experiment

The repository must state when a configuration was reset instead of implying that every level coexisted simultaneously.

## Sanitization rule

Never commit:

- FortiCare/FortiCloud passwords
- FortiGate administrator passwords
- raw VM license artifacts
- private keys
- unredacted secrets/tokens
- unsanitized appliance backup files
