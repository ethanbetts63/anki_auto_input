# Access Control in Operating Systems

## OS Access Models - DAC, MAC, RBAC, rule/attribute-based access.

## DAC - owners/privileged users set permissions; traditional Unix/Linux.

## MAC / SELinux - mandatory restrictions over DAC; enforces least privilege.

## Subjects / Objects - subjects: users/commands/programs; objects: files/pipes/sockets/resources.

## Permissions - read, write, execute for owner/group/others; `777` = full access for all.

## DAC Risk - root can grant dangerous broad permissions like `chmod 777`.

## Malware Privilege - malware inherits current user privilege; admin/root login increases damage.

## Shadow File Dilemma - users need password changes but cannot directly edit protected password file.

## Two-Tier Approach - user calls privileged program that performs only restricted action.

## SetUID - program runs with owner privilege, not launcher privilege.

## passwd - root-owned SetUID program updates only user's password field.

## RUID / EUID - RUID = launcher; EUID = identity used for permissions.

## SetUID RUID/EUID - RUID stays normal user; EUID becomes program owner.

## SetUID Display - `s` in owner execute position.

## SetUID Numeric - normal `0755`; SetUID `4755`; leading `4` = SetUID bit.

## Delegation vs Service - SetUID grants temporary program privilege; daemon service performs privileged tasks.
