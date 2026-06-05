# Authentication, AAA, and Password-Based Authentication

## AAA

- **AAA = Authentication, Authorization, Accountability.**

## Identification

- Subject claims an identity before authentication.

## Authentication

- Verifies claimed identity.
- Can be client-to-server or server-to-client.
- Two-way authentication verifies both sides.

## Authorization / Access Control

- Grants permissions/resources after authentication.

## Accountability

- Records actions after login.
- Examples: last login, duration, transactions.
- Adds storage/resource cost; not required everywhere.

## Basic Authentication Flow

1. Initiation.
2. Challenge.
3. Proof generation.
4. Validation.
5. Decision.

## Authentication Zones

- **Client zone:** secrets may leak locally.
- **Transmission zone:** data may be intercepted.
- **Server zone:** stored credentials may leak.
- Strong authentication protects all three.

## Authentication Factors

- **What you know:** ID/password.
- **What you have:** certificate, OTP/token/code device.
- **What you are:** fingerprint, eye/retina, face.

## Password-Based Authentication

- Proves identity by password knowledge.
- Advantages: cheap, popular, familiar, interoperable, easy to implement.
- Disadvantages: weak alone, hard to manage many passwords, vulnerable in all zones.

## Zone 1 Password Attacks

- Client-side storage/exposure.
- Brute force: try all combinations.
- Phishing: trick user into entering credentials.

## Zone 2 Password Attacks

- Sniffing/interception during transmission.

## Zone 3 Password Attacks

- Insider password-file access.
- Server compromise.
- Dictionary attacks using likely words/patterns.
- Never store/send plaintext passwords.

## Password Managers

- Store/manage many passwords, often encrypted.
- Reduce memorization burden.

## Plain Passwords

- Plain passwords should not be stored or sent.
- Plaintext leaks through insiders, compromise, or sniffing.

## Encrypted Password Problems

- Encryption needs a key.
- Stolen key exposes passwords.
- Same password may produce same ciphertext.
- Ciphertext length may reveal password length.

## Hashing Passwords

- Hash output is fixed-length, deterministic, one-way, no key.
- Store/compare password hashes instead of plaintext.
- Compromised hash database does not directly reveal passwords.

## Hashing Caveat

- Hashes cannot recover original passwords.
- Users reset passwords instead.

## Rainbow Table Attack

- Precomputed password-to-hash lookup table.
- Attacker steals hash and looks up matching plaintext.
- Not mathematical hash reversal.

## Simple Password Risk

- Common/simple passwords are likely in rainbow tables.
- Use long, complex, uncommon passwords.
