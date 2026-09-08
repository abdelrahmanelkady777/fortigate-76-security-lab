# Repository guide

[Back to the project](README.md)

## Where to start

| Reader goal | Start here |
| --- | --- |
| Understand the project quickly | [Root overview and lesson index](README.md) |
| Follow the final integrated network | [Lesson 10 — SD-WAN](lessons/10-sd-wan/README.md) |
| Understand the VPN beneath SD-WAN | [Lesson 09 — IPsec](lessons/09-site-to-site-ipsec-vpn/README.md) |
| Reproduce the foundations in order | [Lesson 00 — Environment](lessons/00-environment-setup/README.md), then the numbered lessons |
| Inspect proof without reading every step | Each lesson's `evidence/README.md` |
| Review the latest upload | [Update manifest](UPLOAD_MANIFEST.md) |

## File responsibilities

| Path | Responsibility |
| --- | --- |
| `README.md` | Project purpose, final topology, lesson navigation, and safety context |
| `CHANGELOG.md` | Short dated milestone history |
| `REPOSITORY_STRUCTURE.md` | This reading and maintenance guide |
| `UPLOAD_MANIFEST.md` | Exact scope of the latest repository update |
| `lessons/00-…` through `lessons/10-sd-wan/` | Numbered, self-contained learning checkpoints |
| `lessons/_template/README.md` | Reusable lesson-writing structure |
| A lesson's `README.md` | Why the change was made, what was configured, how it works, and what the evidence shows |
| A lesson's `evidence/` | Curated original screenshots or explicitly labeled sanitized transcripts, with an index |
| A lesson's `configs/` | Focused configuration references and application notes, where applicable |
| A lesson's `lab-files/` | Small supporting test assets, where applicable |

## Reading historical configurations

The lessons preserve their own checkpoints. For example, Lesson 03 documents ECMP, Lesson 09 documents the two-FortiGate VPN, and Lesson 10 reuses that VPN alongside R1 under SD-WAN. Read a configuration with its lesson's topology and prerequisites; do not combine unrelated checkpoints into one appliance configuration.

The root stays short. Detailed address plans, commands, tests, and explanations belong in the relevant lesson rather than being repeated in several root files.

## Evidence conventions

- Number evidence in the order it supports the explanation; use descriptive filenames.
- Connect each artifact to a specific configuration or observation.
- Distinguish a settings screenshot from a measured traffic result.
- Label transcribed excerpts and remove identifiers without changing packet addresses, interfaces, or outcomes.
- Keep secrets, private keys, license material, full backups, and copyrighted course slides out of the repository.

Lesson 10 follows the same pattern with [a configuration guide](lessons/10-sd-wan/configs/README.md) and [an evidence map](lessons/10-sd-wan/evidence/README.md).
