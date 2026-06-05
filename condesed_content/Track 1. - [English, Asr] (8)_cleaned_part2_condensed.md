# SetUID, SetGID, Sticky Bit, and Access-Control Vulnerabilities

## SetUID - `4755`; leading `4`; owner execute shows `s`; runs with owner/root EUID.

## SetGID - `2755`; leading `2`; group execute shows `s`; runs with file group or inherits directory group.

## Sticky Bit - `1755`; leading `1`; other execute shows `t`; shared dirs like `/tmp`.

## Sticky Bit Purpose - users can create files but not delete/modify others' files.

## Special Bits - SetUID owner privilege; SetGID group privilege/inheritance; sticky restricts deletion.

## SetUID Principle - privilege goes to program, not user; user can only do program-coded actions.

## SetUID Safety - safer than broad root only when program is tightly constrained.

## Bad SetUID Design - flawed logic/environment assumptions expose protected files/actions.

## Root SetUID Editors - `vi`, `nano`, `pico` should not be SetUID root; can edit protected files.

## Race Condition - timing bug where check/update order changes outcome.

## Race Example - two withdrawals accepted before balance update.

## Privileged Race Risk - exploit before privilege is dropped.

## Dirty COW - 2016 copy-on-write race exploit modifying protected read-only files.

## Accountability - logs show what happened and where.

## Access-Control Risk - misconfigured permissions, flawed privileged programs, race conditions.
