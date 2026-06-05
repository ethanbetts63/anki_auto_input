# SetUID in Linux

## Overview

SetUID means "set user ID."

It is a mechanism in Linux operating systems that allows a user to execute a program with the permissions of the program's owner rather than the permissions of the user who runs the program.

This allows a program to perform actions that the regular user would not normally have permission to perform.

SetUID is a controlled privilege escalation mechanism.

## Linux Ownership and Permissions

Linux uses two main ownership categories:

- User ownership
- Group ownership

Files and directories have permissions for three categories:

- Owner
- Group
- Other users

The three permission types are:

- Read (`r`)
- Write (`w`)
- Execute (`x`)

## File Permissions

For a regular file:

- `r` means the file can be read.
- `w` means the file can be modified.
- `x` means the file can be executed.

Permissions are usually displayed in triplets.

Example:

```text
rwxr-x---
```

Meaning:

- First triplet, `rwx`: the owner has read, write, and execute permissions.
- Second triplet, `r-x`: the group has read and execute permissions.
- Third triplet, `---`: other users have no permissions.

If permissions are:

```text
rwxrwxrwx
```

then the owner, group, and other users all have full permission.

## Directory Permissions

For a directory, `r`, `w`, and `x` have different meanings:

- `r` means the user can list the contents of the directory.
- `w` means the user can create and remove files in the directory.
- `x` means the user can enter the directory and access files in it.

## Permission Display Format

In a detailed file listing, the first character indicates the file type, such as whether it is a file or directory.

After that, permissions are shown in triplets:

- Owner permissions
- Group permissions
- Other-user permissions

## SetUID Permission Bit

When SetUID is applied, the owner's execute bit appears as `s` instead of `x`.

For example:

```text
rws
```

This means the operating system executes the program using the user ID of the program's owner, not the user ID of the person running it.

## Real User ID and Effective User ID

There are two relevant user IDs:

- Real User ID (RUID)
- Effective User ID (EUID)

### Real User ID (RUID)

The Real User ID identifies the real owner of the process.

It answers the question:

- Who is running the program?

### Effective User ID (EUID)

The Effective User ID is what the operating system uses for access control decisions.

It answers the question:

- What permissions should this process have?

Actual access control is based on the Effective User ID.

## Normal Program Execution

When a normal program is executed:

- RUID equals EUID.
- Both IDs belong to the user who runs the program.

## SetUID Program Execution

When SetUID is applied:

- RUID remains the user ID of the user who runs the program.
- EUID becomes the user ID of the program's owner.

If the program is owned by root, the program runs with root privilege while it is executing.

## Example: `passwd`

The `passwd` program allows a user to change their own password.

It uses SetUID.

The program is owned by root.

When a normal user runs `passwd`:

- The real user is the normal user.
- The effective user is root.
- The program temporarily runs with root privilege.

This is needed because the password information is stored in a protected system file.

## The Shadow File Example

The Linux shadow file stores users' password information.

Its permissions allow root to read and write it.

The transcript describes the shadow file permissions as:

- Root user: read and write
- Shadow group: read
- Other users: no permission

A normal user does not have permission to read or write the shadow file directly.

However, normal users still need to change their own passwords.

SetUID solves this by allowing users to run the root-owned `passwd` program.

When `passwd` runs with root effective privilege, it can write to the shadow file and update the user's password without giving the user full root access.

## Enabling SetUID

The lecture describes two steps to enable SetUID privilege for a program:

1. Change the file owner to root.
2. Turn on the SetUID bit.

### Change Ownership

The `chown` command changes ownership.

Example concept:

- A file created by a normal user can have its ownership changed to root.

### Change Mode

The `chmod` command changes permissions.

The lecture uses:

```text
4755
```

This turns on the SetUID bit while setting normal permissions to `755`.

After this, a detailed permission listing shows `rws`, indicating SetUID is enabled.

If someone else runs that program, and the program is owned by root, the program runs with root privilege during execution.

## Why `4755` Turns on SetUID

Linux permissions can be represented numerically.

The normal permission triplets use binary values:

- `rwx` = `111`
- `r-x` = `101`
- `r-x` = `101`

Each triplet is converted from binary to decimal.

### Binary to Decimal Conversion

For `111`:

```text
1 * 2^2 + 1 * 2^1 + 1 * 2^0 = 7
```

For `101`:

```text
1 * 2^2 + 0 * 2^1 + 1 * 2^0 = 5
```

Therefore:

```text
rwxr-xr-x = 755
```

### Special Permission Digit

The lecture explains that there is an additional special-permission digit in front of the normal three permission digits.

Without SetUID, the leading digit is `0`, producing:

```text
0755
```

When the SetUID bit is turned on, the leading value becomes `4`, producing:

```text
4755
```

The operating system checks this leading bit to decide whether the program should run as a privileged SetUID program or as a normal program.

## Disabling SetUID

SetUID can be turned off by changing the mode back to:

```text
0755
```

This turns the SetUID bit from `1` back to `0`.

After that, running the file uses normal user privilege instead of the program owner's privilege.

## Purpose of SetUID

SetUID is needed when a normal user must perform a specific protected operation but should not receive full root access.

The `passwd` example shows this clearly:

- A normal user cannot directly write to the shadow file.
- The user needs to change their own password.
- The root-owned SetUID `passwd` program temporarily gets root privilege.
- The program modifies the protected file on the user's behalf.
- The user does not receive unrestricted root access.

## Security Implications

SetUID enhances functionality and user experience by enabling controlled privilege escalation.

However, it creates significant security risks if not managed properly, because SetUID programs may execute with elevated privileges such as root.

SetUID should therefore be used carefully and only where necessary.

## Summary

- SetUID means set user ID.
- It lets a program run with the permissions of the program's owner.
- Access control decisions are based on the Effective User ID.
- In normal execution, RUID and EUID are the same.
- In SetUID execution, RUID is the user running the program, while EUID is the program owner's ID.
- A root-owned SetUID program runs with root privilege while executing.
- `passwd` uses SetUID so normal users can change their passwords.
- `chmod 4755` enables the SetUID bit with `755` permissions.
- `chmod 0755` disables the SetUID bit.
- SetUID is useful but risky if poorly managed.
