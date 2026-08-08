# Lesson NN - <Title>

> Lab status: `<Planned | In progress | Complete>`  
> Documentation status: `<Outline | Draft | Reviewed>`  
> Date completed: `YYYY-MM-DD`  
> Depends on: `<Lesson NN or clean base>`

## 1. Scope

### Objective

State the FortiGate administration or security capability added in this level.

### In scope

- `<Capability>`
- `<Configuration object / topology change>`
- `<Validation or negative-test family>`

### Out of scope

- `<Deferred capability>`
- `<Objects deliberately reused without modification>`

### Completion criteria

- [ ] Starting state is known and reproducible.
- [ ] Configuration is present on the intended FortiGate object/interface/policy.
- [ ] Known-good traffic behaves as expected.
- [ ] Negative/failure/security test behaves as expected, when applicable.
- [ ] FortiGate CLI/log/session evidence confirms the mechanism.
- [ ] Earlier working functionality passes regression testing.
- [ ] Evaluation-license limitations are recorded honestly.

## 2. Starting state

| Existing component | Value | Reused or changed? |
| --- | --- | --- |
| FortiOS | `7.6.7 build 3704` | Reused |
| Interface | `<port/IP>` | `<Reused/changed>` |
| Route | `<route>` | `<Reused/changed>` |
| Firewall policy | `<name/ID>` | `<Reused/changed>` |

## 3. Architecture delta

Explain only what this level adds or changes.

```mermaid
flowchart LR
    C["Client / network"] --> F["FortiGate"]
    F --> N["New control or path"]
    N --> D["Destination / service"]
```

## 4. Configuration

Record exact GUI/CLI object names and critical settings.

| Order | Object type | Object name / ID | Critical settings | Relationship |
| ---: | --- | --- | --- | --- |
| 1 | `<Interface/address/route/etc.>` | `<name>` | `<settings>` | `<parent/path>` |

### Exact CLI used

```bash
<commands>
```

## 5. Verification plan

| Test ID | Type | Action | Expected result | Observed result | Evidence |
| --- | --- | --- | --- | --- | --- |
| `NN-01` | Baseline | `<known-good traffic>` | `<result>` | `<result>` | `<file>` |
| `NN-02` | Negative/failure/security | `<test>` | `<result>` | `<result>` | `<file>` |
| `NN-03` | Regression | `<earlier path>` | `<result>` | `<result>` | `<file>` |

## 6. FortiGate diagnostics and logs

```bash
<get/diagnose commands>
```

Record the output needed to prove the FortiGate mechanism rather than relying only on endpoint behavior.

## 7. Troubleshooting

| Symptom | Root cause | Diagnostic evidence | Fix | Retest |
| --- | --- | --- | --- | --- |
| `<symptom>` | `<cause>` | `<command/log>` | `<change>` | `<result>` |

## 8. Final validated results

Summarize what is now working, what remained unchanged, and any limitation.

## 9. Cleanup / rollback

```bash
<rollback commands if appropriate>
```

## 10. Lessons learned

- `<FortiGate/networking insight>`
- `<Troubleshooting insight>`
- `<Validation insight>`

## 11. Evidence and sanitization

| Artifact | Description |
| --- | --- |
| `evidence/<file>` | `<what it proves>` |

Before commit:

- [ ] No real passwords
- [ ] No FortiCare/FortiCloud credentials
- [ ] No VM license files/data
- [ ] No private keys
- [ ] No reusable authentication tokens
- [ ] No unrelated personal information in screenshots
- [ ] Every technical claim has matching CLI/log/data-plane evidence where possible
