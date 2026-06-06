## Rainbow Tables - precomputed password-to-hash maps; crack stolen hashes by lookup; weak/common passwords likely included.

## Salting Password Hashes - random value added before hashing; stored with hash; not secret.

## Linux Shadow Salt Format - fields show hash type, salt, and salted hash; `$6$` indicates SHA-512-style password hashing.

## Why Salting Helps - same password plus different salts creates different hashes; hides password equality.

## Salting vs Rainbow Tables - attacker must precompute every password times every salt; 12-bit salt multiplies table by `2^12`.

## Salting Limits - hardens precomputation/equality attacks; does not stop brute force or replay.

## Brute Force - attacker guesses directly; salt cannot help once the correct password is guessed.

## Brute Force Difficulty - depends on password space, guess rate, length, and complexity.

## Replay / Pass-the-Hash - captured salted hash can be reused if server accepts it as proof.

## Replay Defenses - MFA codes, timestamps, freshness checks, stale-request rejection.

## Password Stretching / Hash Chains - hash many times before storage; bcrypt-style systems slow each guess.

## Stretching Effect - more iterations reduce guesses per second and make cracking harder.

## Password Entropy - more possible combinations means longer cracking time.

## Length vs Complexity - combinations equal character-set size to password length; best is long and complex.

## Usable Strong Passwords - use memorable modified phrases; avoid under 15 characters; over 20 is better.

## Other Factors - authentication can use what you know, have, or are.

## What You Have - OTP devices, bank code devices, certificates; stronger but costly and stealable.

## What You Are - fingerprints, eye scans, face recognition, behavioral analysis; needs sensors/processing.

## Biometric Errors - false negative rejects legitimate users; false positive accepts illegitimate users.

## MFA - combines factors to reduce password-only risks: brute force, rainbow tables, replay, phishing, leakage.

## Password Auth Summary - plaintext bad; encryption has key/ciphertext issues; hashes face rainbow tables; salts harden rainbow attacks; stretching slows brute force; MFA adds proof.

## Passwordless / Public-Key Auth - RSA public/private-key protocols reduce dependence on passwords.
