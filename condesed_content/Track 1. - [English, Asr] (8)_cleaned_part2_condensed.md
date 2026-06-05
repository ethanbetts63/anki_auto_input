# SetUID, SetGID, Sticky Bit, and Access-Control Vulnerabilities

## SetUID Numeric Representation

- Normal: `0755`.
- SetUID: `4755`.
- Leading `4` = SetUID bit (`100` binary).
- Symbolic `s` in owner execute position, e.g. `rws`.
- Root-owned SetUID program runs with root EUID.

## SetGID

- **SetGID = set group ID.**
- Example: `2755`.
- Leading `2` = SetGID bit (`010` binary).
- Symbolic `s` in group execute position.
- File: runs with file group privilege.
- Directory: new files/folders inherit parent directory group.

## Sticky Bit

- Example: `1755`.
- Leading `1` = sticky bit (`001` binary).
- Symbolic `t` often in other execute position, e.g. `rwt`.
- Used in shared directories like `/tmp`.
- Users can create files but cannot delete/modify others' files.

## Special Permission Bits

- **SetUID:** run with file owner privilege.
- **SetGID:** run with file group privilege or inherit directory group.
- **Sticky bit:** restrict shared-directory deletion/modification to owner.

## SetUID Security Principle

- Privilege is granted to the program, not directly to the user.
- User can only perform actions implemented by the SetUID program.
- RUID stays normal; EUID becomes program owner.
- Safer than broad superuser delegation only if program is constrained.

## Bad SetUID Program Design

- Flawed SetUID logic can expose protected files/actions.
- Attackers exploit the program or environment assumptions.
- SetUID programs must tightly constrain behavior.

## Editor with Incorrect SetUID Permission

- Editors like `vi`, `nano`, `pico` should not be SetUID root.
- Root-EUID editor can modify many protected files.
- Remove/restrict broad SetUID permissions.

## Race Condition Vulnerability

- **Race condition:** timing of operations changes outcome.
- Example: two withdrawals accepted before balance update.
- Cause: unsynchronized check/update.
- Privileged programs can be exploited before privilege is dropped.

## Dirty COW

- **Dirty COW = dirty copy on write.**
- Famous 2016 race-condition-style exploit.
- Allowed protected files to be modified despite read-only access.

## Access Control and Accountability

- **AAA:** Authentication, Access control/Authorization, Accountability.
- Accountability uses logs to show what happened and where.
- Misconfigured permissions, flawed privileged programs, and race conditions create security problems.
