# Access Control in Operating Systems

## Access Control Models

- **DAC = Discretionary Access Control:** owners/privileged users control permissions; traditional Unix/Linux.
- **MAC = Mandatory Access Control:** mandatory restrictions; SELinux adds MAC over DAC.
- **RBAC = Role-Based Access Control:** permissions by role.
- **Rule-Based / ABAC:** decisions by rules/attributes.

## Operating System Access Control

- **Subjects:** users, commands, programs.
- **Objects:** files, pipes, sockets, resources.
- Permissions: read, write, execute.
- Linux/Unix permission triplets: owner, group, others.
- `777` = read/write/execute for all.

## Unix DAC vs SELinux

- DAC lets root grant broad permissions, e.g. `chmod 777`.
- Overbroad permissions create security risk.
- SELinux MAC limits dangerous grants and enforces least privilege.

## Malware and User Privilege

- Malware runs with the current user's privilege.
- Normal-user login limits malware impact.
- Admin/root login lets malware inherit high privileges.

## Password File Dilemma

- Shadow password file is protected.
- Normal users need to change their own password.
- Direct write access would let users modify others' passwords.
- File permissions are too coarse for per-field control.

## Two-Tier Protected Resource Approach

- User invokes privileged program.
- Program performs restricted action.
- Example: `passwd` updates only the user's own password field.

## SetUID

- **SetUID = set user ID.**
- Program runs with owner's privilege, not launcher's privilege.
- `passwd` is root-owned; normal user runs it with temporary root EUID.
- User still cannot directly edit shadow file.

## Real User ID vs Effective User ID

- **RUID:** actual launching user.
- **EUID:** identity whose privileges are used.
- SetUID keeps RUID normal but changes EUID to program owner.
- Symbolic `s` in owner execute position shows SetUID.

## Reading SetUID Permission

- Normal: `0755`.
- SetUID: `4755`.
- Leading `4` = SetUID bit (`100` binary).
- `rws` indicates owner execute + SetUID.

## Delegation vs Service Approach

- **SetUID/delegation:** temporary specific privilege through a program.
- **Daemon/service:** privileged background service performs tasks.
- Linux uses SetUID for tasks like `passwd`.
