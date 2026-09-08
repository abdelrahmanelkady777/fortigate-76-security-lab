# Final lesson update manifest

## Package

`FortiGate_Lesson10_Final_Repo_Update.zip` is a **delta update** for [fortigate-76-security-lab](https://github.com/abdelrahmanelkady777/fortigate-76-security-lab), prepared against main commit `278c9d9144d7760abb6e38355a6a8451a733f8e9`.

It contains only the four revised root Markdown files and the new `lessons/10-sd-wan/` directory. Earlier lessons, their evidence, `.gitignore`, and the lesson template are unchanged. No files need to be deleted or moved.

## Revised root files

| File | Change |
| --- | --- |
| [README.md](README.md) | Concise project overview, final topology, engineering highlights, and complete 00–10 lesson index |
| [REPOSITORY_STRUCTURE.md](REPOSITORY_STRUCTURE.md) | Short reading guide and file/evidence conventions |
| [CHANGELOG.md](CHANGELOG.md) | Condensed dated milestone history, plus the final lesson |
| [UPLOAD_MANIFEST.md](UPLOAD_MANIFEST.md) | This update's scope and application instructions |

## New lesson files

Under `lessons/10-sd-wan/`:

- `README.md` — the final case study, packet lifecycle, member/zone relationships, and engineering observations.
- `configs/README.md` — prerequisites, migration order, policy mappings, and safe use of the references.
- `configs/hq-sdwan-reference.conf`
- `configs/branch-loopback-reference.conf`
- `configs/supporting-routing.txt`
- `configs/verification.txt`
- `evidence/README.md` — artifact-to-claim map and original screenshot provenance.
- Ten original PNGs: `01-sdwan-zones.png`, `02-policy-zone-migration.png`, `03-zone-route-configuration.png`, `04-overlay-selected.png`, `05-overlay-ping.png`, `07-underlay-preference.png`, `08-underlay-ping.png`, `10-sla-target-participants.png`, `11-sla-thresholds-timers.png`, `12-sla-port3-measurement.png`.
- Five sanitized text artifacts: `03-route-lookup-sanitized.txt`, `06-overlay-capture-sanitized.txt`, `09-underlay-capture-sanitized.txt`, `13-member-sources-sanitized.txt`, `14-selector-checkpoints-sanitized.txt`.

**Total: 26 files — 4 revised and 22 new.**

## Apply the update

1. Extract the ZIP into a temporary folder and review its files.
2. Copy its contents into your repository checkout, keeping the paths intact. Replace only the four named root files; add the new lesson directory.
3. Review the diff, preview both READMEs on GitHub, and commit/push through your normal workflow.

If main has changed since the baseline above, merge the root documentation changes with that newer version. The package contains documentation and configuration references; it does not execute commands on the lab appliances.

No GitHub branch, commit, push, or pull request was created by preparing this package.
