# Hash Functions

## Hash Function - maps input/message to fixed-size byte string.

## Hash Output - hash value/code/digital fingerprint, often hexadecimal.

## Deterministic - same input always gives same hash.

## Fixed Length - output size constant regardless of input size.

## One-Way - easy `x -> y`, hard to recover `x` from `y`.

## Collision Resistance - hard to find two inputs with same hash.

## Avalanche Effect - tiny input change causes very different hash.

## Hash Uses - integrity, tamper detection, unauthorized-access protection.

## Hash Combinations - combine with RSA/DH for integrity/authentication.

## Password Use - helps protect password confidentiality.

## MD5 - early 128-bit hash; command example `md5sum`.

## MD5 Internals - 64 operations using 32-bit values, message blocks, constants, shifts, modular addition.

## MD5 Caveat - collision resistance broken.

## SHA Family - SHA-1, SHA-2, SHA-3.

## SHA-1 - 1995; collision resistance weakened.

## SHA-2 - stronger than MD5/SHA-1.

## SHA-3 - newer SHA standard; released 2015.

## MD5 vs SHA - MD5 faster/smaller/weaker; SHA longer/more secure.

## Key Caveat - hashes support goals when combined with public-key or key-exchange algorithms.
