## Modern Cryptography - prevents eavesdropping.

## XOR Encryption - `M XOR K = C`.

## XOR Decryption - `C XOR K = M`.

## XOR Reason - `(M XOR K) XOR K = M XOR (K XOR K) = M`.

## Ideal Key - random, uncrackable, plaintext-length, one-time use but randomness and secure key sharing are impractical.

## Symmetric Encryption:

## ECB (block cipher)- split message into key-sized blocks; pad last block. Parallel encryption/decryption; very fast but repeated plaintext blocks produce repeated ciphertext blocks. (image pattern example)

## Replay Attack. unique IDs/timestamps plus MAC to stop.
