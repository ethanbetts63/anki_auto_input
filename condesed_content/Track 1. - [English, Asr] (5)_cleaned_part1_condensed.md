# Cryptography Algorithms: Security Goals and Symmetric Modes

## Learning Focus - crypto as technical countermeasure; confidentiality primary; other goals need combinations.

## Security Goals - confidentiality, integrity, availability, authenticity, non-repudiation.

## Secret Online Message - confidentiality.

## Clean Software - integrity: prove no malicious modification.

## Banking MITM - integrity; often also authenticity and non-repudiation for transactions.

## Certificate Check - authenticity plus integrity.

## E-Signed Document - authenticity plus non-repudiation.

## Classic Cryptography - substitution, transposition, codebooks; obsolete and frequency-analysis vulnerable.

## Modern Cryptography - symmetric and asymmetric; symmetric came first.

## Replay Defenses - timestamps, two-way authentication, one-time codes.

## CBC - each block depends on previous ciphertext; repeated plaintext patterns are hidden.

## Initialization Vector - IV starts first block; different IV changes ciphertext; receiver needs same IV.

## CBC Encryption - `P1 XOR IV -> encrypt = C1`; `Pi XOR C(i-1) -> encrypt = Ci`.

## CBC Speed - encryption is serial and slower than ECB.

## CBC Example - 2-bit blocks with IV `10`; each ciphertext feeds the next plaintext block.

## CBC Decryption Intro - reverse cipher table plus same IV recovers plaintext.
