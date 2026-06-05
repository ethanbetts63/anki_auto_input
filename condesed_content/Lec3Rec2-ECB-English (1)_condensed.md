# Modern Symmetric Encryption and ECB Mode

## Modern Cryptography - stronger than classical substitution/transposition; prevents eavesdropping.

## Binary Basis - computer calculations use `0` and `1`.

## XOR Rule - same bits -> `0`; different bits -> `1`.

## XOR Table - `0^0=0`, `0^1=1`, `1^0=1`, `1^1=0`.

## XOR Properties - `A XOR 0 = A`; `A XOR 1 = NOT A`; `A XOR A = 0`.

## XOR Encryption - `M XOR K = C`.

## XOR Decryption - `C XOR K = M`.

## XOR Reason - `(M XOR K) XOR K = M XOR (K XOR K) = M`.

## Ideal Key - random, uncrackable, plaintext-length, one-time use.

## Ideal Key Problem - randomness and secure key sharing are impractical.

## Symmetric Encryption - same key encrypts and decrypts.

## Block Cipher - split message into key-sized blocks; pad last block; process each block.

## ECB - simplest block mode; encrypt each block independently with same key.

## ECB Advantage - parallel encryption/decryption; very fast.

## ECB Weakness - repeated plaintext blocks produce repeated ciphertext blocks.

## ECB Pattern Leak - encrypted image still reveals original pattern.

## Replay Attack - attacker resends captured valid ciphertext without decrypting it.

## Replay Example - replay encrypted bank login/transaction packets.

## Replay Defenses - unique IDs/timestamps plus MAC to stop modification.

## Takeaway - ECB is fast but leaks patterns and supports replay unless freshness/authentication are added.
