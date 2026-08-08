# Lesson 00 - Environment Setup and Licensing

> Lab status: `Complete`  
> Documentation status: `Reviewed`  
> Date completed: `2026-08-08`  
> Depends on: `Clean EVE-NG installation with Internet access`

## 1. Scope

### Objective

Deploy an official FortiGate-VM64-KVM image running FortiOS 7.6.7 in EVE-NG, activate the free permanent evaluation license, verify basic network reachability, and reach an operational FortiOS GUI that can be used as the base state for later FortiOS 7.6 Administrator labs.

### In scope

- Official FortiGate KVM image selection
- EVE-NG image import
- FortiGate node creation
- First login and administrator-password policy
- FortiOS/version/resource/interface verification
- Management access through `port1`
- Routing and DNS validation
- Troubleshooting the stalled GUI license-check screen
- Permanent evaluation-license activation
- Post-license setup wizard
- Final operational-state validation

### Out of scope

- Firewall policy design
- NAT
- Security profiles
- VPN configuration
- User authentication
- HA
- Production licensing
- FortiGuard subscription services

### Completion criteria

- [x] FortiGate-VM64-KVM v7.6.7 boots in EVE-NG.
- [x] FortiOS reports build `3704`.
- [x] The VM operates with `1 vCPU` and `2048 MB RAM`.
- [x] `port1` obtains network connectivity.
- [x] FortiGate reaches the Internet and resolves/reaches FortiGuard infrastructure.
- [x] The permanent evaluation-license flow completes.
- [x] The FortiOS setup wizard becomes usable after licensing.
- [x] The normal FortiOS dashboard is reachable.
- [x] Evaluation-license restrictions are recorded.
- [x] No real credentials are included in the repository.

---

## 2. Final environment

| Item | Observed value |
| --- | --- |
| FortiGate package | `FGT_VM64_KVM-v7.6.7.M-build3704-FORTINET.out.kvm.zip` |
| FortiOS | `FortiGate-VM64-KVM v7.6.7, build3704, 260601 (GA.M)` |
| Architecture | x86-64 |
| Hypervisor | EVE-NG / QEMU-KVM |
| EVE image directory | `/opt/unetlab/addons/qemu/fortinet-FGT-v7.6.7/` |
| EVE disk name | `virtioa.qcow2` |
| vCPU | `1` |
| RAM | `2048 MB` |
| Management interface | `port1` |
| Addressing | DHCP in this build |
| Observed lab IP | `192.168.1.63/24` |
| Observed gateway | `192.168.1.1` |
| License | Permanent evaluation license |
| Final outcome | Operational FortiOS dashboard |

> The management IP and gateway are environment-specific. A different EVE bridge or DHCP server can assign different values.

---

## 3. Download the correct FortiGate image

The Fortinet download page contains several similarly named packages. The important distinction is to use the **FortiGate** x86-64 **new deployment** KVM package.

### Selection

1. Open the Fortinet Customer Service & Support portal.
2. Go to **Downloads -> VM Images**.
3. Select **Product: FortiGate**.
4. Select **Platform: KVM**.
5. Open FortiOS `7.6.7`.
6. Select **New deployment of FortiGate for KVM**.

The selected package was:

```text
FGT_VM64_KVM-v7.6.7.M-build3704-FORTINET.out.kvm.zip
```

In the portal list used during this build, it appeared as item **#6**.

### Packages deliberately not used

| Prefix/type | Why it was rejected |
| --- | --- |
| `FFW_VM64_KVM...` | FortiFirewall, not the FortiGate VM used for this lab |
| `FGT_ARM64_KVM...` | ARM64 build, not the x86-64 VM64 image required by this EVE host |
| `Upgrade from previous version` | Firmware upgrade package, not the fresh KVM deployment package |

---

## 4. Import the image into EVE-NG

WinSCP was used to transfer the KVM deployment ZIP directly to:

```text
/opt/unetlab/addons/qemu/
```

### EVE shell commands

```bash
cd /opt/unetlab/addons/qemu/

mkdir -p fortinet-FGT-v7.6.7

unzip FGT_VM64_KVM-v7.6.7.M-build3704-FORTINET.out.kvm.zip \
  -d fortinet-FGT-v7.6.7

ls -lah fortinet-FGT-v7.6.7
```

The extracted deployment package contained:

```text
fortios.qcow2
```

EVE-NG expects the first virtio disk to use the `virtioa.qcow2` name:

```bash
mv fortinet-FGT-v7.6.7/fortios.qcow2 \
   fortinet-FGT-v7.6.7/virtioa.qcow2
```

Then repair EVE-NG permissions:

```bash
/opt/unetlab/wrappers/unl_wrapper -a fixpermissions
```

### Final image path

```text
/opt/unetlab/addons/qemu/fortinet-FGT-v7.6.7/virtioa.qcow2
```

### Optional cleanup

After confirming the VM boots correctly, the original ZIP can be removed from the EVE QEMU directory to reclaim disk space.

A safer workflow is to keep any previously working FortiGate image until the new version successfully boots.

---

## 5. Create the FortiGate node

The node was created with resources that fit the free permanent evaluation entitlement.

| Setting | Value |
| --- | --- |
| Image | FortiGate 7.6.7 KVM |
| vCPU | `1` |
| RAM | `2048 MB` |
| Interfaces | `3` |
| `port1` connection | EVE network/bridge with DHCP, DNS, and Internet access |

### Why these resources?

The evaluation license itself reports a maximum of:

```text
1 CPU
2 GiB memory
3 interfaces
3 firewall policies
3 routes
```

The lab therefore uses `1 vCPU` and `2048 MB RAM` intentionally rather than allocating unnecessary resources that exceed the evaluation entitlement.

---

## 6. First boot and administrator password

At first boot, the FortiGate console presented:

```text
FortiGate-VM64-KVM login:
```

The initial login used:

```text
Username: admin
Password: <blank on first login>
```

FortiOS then forced an administrator-password change.

The password policy observed on this FortiOS build required:

- Minimum length: `12`
- At least `1` uppercase letter
- At least `1` lowercase letter
- At least `1` number
- At least `1` non-alphanumeric character

### Repository rule

The actual administrator password is deliberately not documented.

Never place the real password in:

- README files
- screenshots
- terminal transcripts
- issue descriptions
- commit messages
- Git history

---

## 7. Verify the base FortiGate state

Before relying on the GUI, verify the appliance from the CLI.

### FortiOS and license/resource state

```bash
get system status
```

The important observations before activation were:

```text
Version: FortiGate-VM64-KVM v7.6.7,build3704,260601 (GA.M)
FortiOS x86-64: Yes
License Status: Invalid
VM Resources: 1 CPU/1 allowed, ~2 GB RAM/2048 MB allowed
Current HA mode: standalone
```

`License Status: Invalid` was expected before the evaluation-license activation step.

### Interfaces

```bash
get system interface
```

Observed base state:

```text
port1: DHCP, 192.168.1.63/24, up
port2: no configured IP
port3: no configured IP
```

Again, the specific `port1` DHCP address is lab-specific.

---

## 8. Access the FortiOS GUI

From the management workstation:

```text
https://<PORT1_IP>
```

In this build:

```text
https://192.168.1.63
```

The browser displayed the expected certificate warning because the FortiGate management GUI used a self-signed certificate. The warning was accepted for the isolated lab.

### Problem observed

The setup page loaded mostly blank. When refreshed, it briefly showed that the license was being checked by FortiGuard, but the page did not progress.

At this point, the issue was treated as a possible connectivity or activation problem.

---

## 9. Validate Internet, DNS, and the default route

Three checks were used to determine whether the FortiGate could reach the Internet and Fortinet infrastructure.

### Internet reachability

```bash
execute ping 8.8.8.8
```

Result: replies were received.

### DNS and FortiGuard reachability

```bash
execute ping guard.fortinet.net
```

Result:

- hostname resolved successfully
- ICMP replies were received

### Routing table

```bash
get router info routing-table all
```

Observed default route:

```text
S* 0.0.0.0/0 [5/0] via 192.168.1.1, port1
```

### Interpretation

Because all three were present:

- Internet access worked
- DNS worked
- `guard.fortinet.net` was reachable
- a default route existed through `port1`

The blank setup page was not caused by a basic routing or DNS failure.

---

## 10. Additional FortiGuard/update diagnostics

The update daemon was also observed and an update was forced:

```bash
diagnose debug application update -1
diagnose debug enable
execute update-now
```

After collecting output:

```bash
diagnose debug disable
```

Additional checks:

```bash
get system status
diagnose autoupdate versions
```

These diagnostics did not complete the license activation. They were useful because they reinforced that the next troubleshooting step should focus on the activation flow rather than the basic network path.

---

## 11. Activate the permanent evaluation license

The successful activation was performed directly from the FortiGate CLI.

### Set the FortiCare/FortiCloud account

```bash
execute vm-license-options account-id <FORTICARE_EMAIL>
execute vm-license-options account-password <FORTICARE_PASSWORD>
```

Then request the evaluation license:

```bash
execute vm-license
```

FortiOS displayed the evaluation terms and prompted:

```text
Do you want to continue? (y/n)
```

Answer:

```text
y
```

The FortiGate then rebooted.

### Important credential warning

The `account-password` command can appear in terminal output or history.

Never commit a screenshot or transcript that contains the credential.

If the credential is exposed, rotate it immediately.

---

## 12. Evaluation-license restrictions

The FortiGate CLI itself displayed the following restrictions during activation.

| Evaluation condition | Limit |
| --- | --- |
| Expiration | Does not expire |
| CPU | Maximum `1` |
| Memory | Maximum `2 GiB` |
| Interfaces | Maximum `3` |
| Firewall policies | Maximum `3` |
| Routes | Maximum `3` |
| Encryption | Low-encryption operation only, except supported management communications |
| FortiCare support | Not included |
| FortiGuard support | Not included |

The free evaluation is therefore suitable for controlled training, but later project levels must be designed around the three-policy and three-route limits.

---

## 13. Complete the post-license setup wizard

After the reboot, the setup wizard became usable.

The choices used for this clean lab were:

| Wizard item | Choice |
| --- | --- |
| Migrate Config with FortiConverter | `Later` |
| Automatic Patch Upgrades | Manual/disabled for controlled lab work |
| Dashboard Setup | Defaults |
| Change Your Password | Already completed during first login |

The lab is a fresh deployment, so there is no configuration to migrate with FortiConverter.

---

## 14. Final validation

After the setup wizard, the normal FortiOS dashboard loaded successfully.

The dashboard showed:

```text
Firmware: v7.6.7 build3704 (Mature)
Allocated vCPUs: 1 / 1
Allocated RAM: 2 GiB / 2 GiB
```

The orange licensing/FortiGuard indicators are consistent with the restricted evaluation model and do not mean the VM has expired.

### Final state

```text
Official FortiGate KVM image
        ->
Imported into EVE-NG
        ->
1 vCPU / 2 GiB / 3 interfaces
        ->
First boot + admin password
        ->
port1 DHCP management access
        ->
Internet + DNS + route verified
        ->
Permanent evaluation activated via CLI
        ->
FortiGate reboot
        ->
Post-license setup wizard
        ->
Operational FortiOS 7.6.7 dashboard
```

---

## 15. Troubleshooting record

| Symptom | Initial hypothesis | Diagnostic evidence | Root cause / conclusion | Fix |
| --- | --- | --- | --- | --- |
| GUI remained mostly blank during setup | Internet/DNS/license validation problem | `8.8.8.8` replied; `guard.fortinet.net` resolved/replied; default route existed | Basic network path was healthy; activation flow had not completed | Activate permanent evaluation directly with `execute vm-license` |
| `License Status: Invalid` before activation | VM image/resource issue | `get system status` showed correct 7.6.7 build and resources within entitlement | VM was simply not activated yet | Complete CLI evaluation activation |
| Update forcing did not resolve setup page | FortiGuard update daemon might be stuck | `execute update-now` and autoupdate diagnostics did not complete licensing | Licensing required the explicit VM-license flow | Use `vm-license-options` + `execute vm-license` |

---

## 16. Command recap

### EVE-NG image import

```bash
cd /opt/unetlab/addons/qemu/
mkdir -p fortinet-FGT-v7.6.7

unzip FGT_VM64_KVM-v7.6.7.M-build3704-FORTINET.out.kvm.zip \
  -d fortinet-FGT-v7.6.7

ls -lah fortinet-FGT-v7.6.7

mv fortinet-FGT-v7.6.7/fortios.qcow2 \
   fortinet-FGT-v7.6.7/virtioa.qcow2

/opt/unetlab/wrappers/unl_wrapper -a fixpermissions
```

### FortiGate verification

```bash
get system status
get system interface

execute ping 8.8.8.8
execute ping guard.fortinet.net
get router info routing-table all
```

### Optional update diagnostics

```bash
diagnose debug application update -1
diagnose debug enable
execute update-now
diagnose debug disable
diagnose autoupdate versions
```

### Permanent evaluation activation

```bash
execute vm-license-options account-id <FORTICARE_EMAIL>
execute vm-license-options account-password <FORTICARE_PASSWORD>
execute vm-license
```

Then answer:

```text
y
```

---

## 17. Lessons learned

- Fortinet's VM download list contains similarly named products and architectures; the image prefix matters.
- For this lab, `FGT_VM64_KVM` is the relevant x86-64 FortiGate package.
- In EVE-NG, the FortiGate qcow2 disk must be placed in the Fortinet QEMU image folder and named `virtioa.qcow2`.
- A DHCP lease alone is not sufficient proof of end-to-end connectivity; Internet reachability, DNS resolution, and the routing table were all verified separately.
- A valid network path does not guarantee that the FortiGate VM license has been activated.
- The CLI license workflow was more reliable than waiting for the stalled GUI activation page.
- The evaluation limitations are architectural constraints, not details to hide. Future lab levels must be designed around them.
- Credentials must never become evidence. Use placeholders and sanitized screenshots.

---

## 18. Evidence

Evidence should be added only after sanitization.

See [`evidence/README.md`](evidence/README.md) for the expected files and sanitization rules.

Recommended evidence set:

| File | What it should prove |
| --- | --- |
| `01-fortigate-kvm-package-selection.png` | Correct `FGT_VM64_KVM` new-deployment image selected |
| `02-eve-image-import.png` | FortiGate 7.6.7 image present in EVE QEMU directory |
| `03-system-status-pre-license.png` | Correct FortiOS build and evaluation resource entitlement |
| `04-connectivity-and-route-check.png` | Internet, FortiGuard DNS/reachability, and default route |
| `05-post-license-setup-wizard.png` | Setup wizard usable after activation |
| `06-operational-dashboard.png` | Final operational FortiOS dashboard |

Do **not** add any screenshot that contains a real FortiCare password or other credential.

---

## 19. References

- Fortinet - Downloading the FortiGate-VM deployment package (KVM):  
  https://docs.fortinet.com/document/fortigate-private-cloud/7.4.0/kvm-administration-guide/961760/downloading-the-fortigate-vm-deployment-package
- EVE-NG - Fortinet images:  
  https://www.eve-ng.net/index.php/documentation/howtos/howto-add-fortinet-images/
- Fortinet - Permanent trial mode for FortiGate-VM:  
  https://docs.fortinet.com/document/fortigate/7.6.3/administration-guide/441460
- Fortinet - Connecting to the FortiGate-VM GUI (KVM):  
  https://docs.fortinet.com/document/fortigate-private-cloud/7.6.0/kvm-administration-guide/142213/connecting-to-the-fortigate-vm-gui
- Fortinet - Default administrator password / first-login policy:  
  https://docs.fortinet.com/document/fortigate/7.6.6/administration-guide/99980/default-administrator-password
