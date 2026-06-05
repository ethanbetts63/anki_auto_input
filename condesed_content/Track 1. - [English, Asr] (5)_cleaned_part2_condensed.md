# Symmetric Cryptography: CBC Decryption, Standards, Applications, and Key Problems

## CBC Decryption - decrypt `Ci`, then XOR IV for first block or `C(i-1)` for later blocks.

## CBC Example - ciphertext `11` reverses to `10`; `10 XOR IV 10 = plaintext 00`.

## Parallel Decryption - each block uses available ciphertext blocks; encryption serial, decryption parallel.

## Symmetric Key / IV - sender and receiver share same secret key; CBC receiver also needs IV.

## Leaked Key - disclosed symmetric key breaks confidentiality.

## IV Changes - different IV changes ciphertext for same message and helps against repeats/replay.

## Other Modes - output feedback and others trade speed and security differently.

## Simple Bitwise Limits - single XOR, short keys, or disclosed key/IV are unsafe.

## DES - 64-bit blocks, 32/32 split, permutation/XOR/swaps, 16 rounds; cracked.

## Triple DES - DES applied three times; 48 rounds; safer than DES, very slow, still risky.

## AES - faster and stronger than Triple DES; variable key sizes; choose AES when available.

## Standards Comparison - DES cracked; 3DES slow; AES fast, strong, widely used; all symmetric.

## Symmetric Applications - secure internet, files, server data, banking, payments, protocols.

## Why Symmetric Is Fast - bitwise calculations remain faster than asymmetric exponential math.

## Symmetric Goals - confidentiality only by itself; integrity/authenticity/non-repudiation need other mechanisms.

## Key Exchange Problem - secret key must be shared securely; CBC IV must match.

## Key Exhaustion - pairwise keys grow as `n x (n - 1) / 2`.

## Key Count Examples - 2 parties need 1 key; 3 need 3; 4 need 6; 5 need 10.

## KDC Problem - trusted center can generate/distribute keys but may read all conversations.

## E-Commerce Scalability - millions of customers would require millions of symmetric keys.

## Motivation for Asymmetric Crypto - scalable key model; different encryption/decryption keys; supports auth/integrity/non-repudiation with hashes.
