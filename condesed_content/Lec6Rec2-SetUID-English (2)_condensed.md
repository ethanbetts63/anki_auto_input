# SetUID in Linux

## SetUID - lets program run with owner permissions instead of runner permissions.

## Purpose - controlled privilege escalation for specific protected operations.

## Linux Ownership - user owner and group owner.

## Permission Categories - owner, group, other.

## Permission Types - read `r`, write `w`, execute `x`.

## File Permissions - `r` read; `w` modify; `x` execute.

## Permission Triplets - example `rwxr-x---`: owner full, group read/execute, others none.

## Full Permissions - `rwxrwxrwx`.

## Directory Permissions - `r` list; `w` create/remove; `x` enter/access.

## Listing Format - first character file type; then owner/group/other triplets.

## SetUID Bit Display - owner execute becomes `s`, e.g. `rws`.

## RUID - real user running the program.

## EUID - effective user used for access-control decisions.

## Normal Execution - RUID = EUID = runner.

## SetUID Execution - RUID = runner; EUID = program owner.

## Root-Owned SetUID - program temporarily runs with root privilege.

## passwd - root-owned SetUID program letting users change their own passwords.

## Shadow File - protected password file writable by root, not normal users.

## SetUID passwd Flow - normal user runs `passwd`; EUID root writes shadow file.

## Enable SetUID Step 1 - change owner to root with `chown`.

## Enable SetUID Step 2 - turn on SetUID bit with `chmod 4755`.

## Numeric Permissions - `rwx = 111 = 7`; `r-x = 101 = 5`; `rwxr-xr-x = 755`.

## Special Leading Digit - `0` normal; `4` SetUID.

## `4755` - SetUID enabled plus `755` normal permissions.

## Disable SetUID - `chmod 0755`.

## Security Risk - elevated privileges make SetUID dangerous if poorly managed.

## Takeaway - useful for narrow privilege delegation, but use carefully and only when necessary.
