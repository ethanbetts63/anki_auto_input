# Cryptography Algorithms: Security Goals and Symmetric Modes

## Learning Focus

This lecture introduces cryptography algorithms as technical countermeasures.

Primary objective:

- Understand how confidentiality can be guaranteed through cryptographic algorithms.
- Understand that other security goals often require combining multiple algorithms.

The five security goals discussed are:

- Confidentiality
- Integrity
- Availability
- Authenticity
- Non-repudiation

The algorithms discussed in this lecture primarily support confidentiality. Integrity, authenticity, and non-repudiation usually require combining algorithms, especially with methods covered later.

## Security Goals in Different Scenarios

Different systems need different security goals, or combinations of goals.

### Secret Online Message

Scenario:

- Someone wants to send a secret message to a partner online.

Main goal:

- Confidentiality

Meaning:

- The message should remain secret during transmission.

### App Developer Proving Software Is Clean

Scenario:

- An app developer wants to prove that software is clean and no malicious code has been attached.

Main goal:

- Integrity

Meaning:

- The software should not have been modified.

### Bank System and Man-in-the-Middle Risk

Scenario:

- A bank wants to ensure messages are not modified by a man-in-the-middle attacker.

Main goal when focusing on modification:

- Integrity

Additional goals often needed in banking:

- Authenticity: verify the true sender.
- Non-repudiation: the sender cannot later deny authorizing a transaction, such as after clicking a confirmation button.

### Checking a Digital Certificate

Scenario:

- An HR officer checks whether a certificate provided by a new employee is true or fake.
- Example certificates include a university certificate or a Cisco/CISSP-style security certificate.

Main goal:

- Authenticity

Additional goal:

- Integrity, because the certificate information should be unchanged and should have been issued or signed by the correct body.

### Checking an E-Signed Document

Scenario:

- A person checks whether an electronically signed document came from the true sender.

Main goals:

- Authenticity: verify the sender.
- Non-repudiation: the true sender cannot later deny signing.

## Evolution of Cryptography

Cryptography developed from classic methods to modern symmetric and asymmetric methods.

### Classic Cryptography

Classic cryptography was based on:

- Substitution
- Transposition

Characteristics:

- Historically used, including in military contexts more than 100 years ago.
- Often relied on shifting, substitution, and code books.
- No longer considered safe enough.
- Vulnerable to techniques such as frequency analysis.

### Modern Cryptography

Modern cryptography includes:

- Symmetric cryptography
- Asymmetric cryptography

Symmetric cryptography developed before asymmetric cryptography.

This lecture focuses on symmetric cryptography. Asymmetric cryptography, including RSA and Diffie-Hellman, is covered later with more focus on applications.

## XOR Operation

Symmetric encryption is fundamentally based on bitwise XOR operations.

XOR means exclusive OR.

Rules:

- If the two input bits are different, the output is `1`.
- If the two input bits are the same, the output is `0`.

Examples:

- `0 XOR 1 = 1`
- `1 XOR 0 = 1`
- `1 XOR 1 = 0`
- `0 XOR 0 = 0`

Encryption:

- `message XOR key = ciphertext`

Decryption:

- `ciphertext XOR key = original message`

Reason:

- XORing with the same key twice cancels the key and recovers the original message.
- The same key is used for encryption and decryption in symmetric encryption.

## Electronic Codebook Mode

Electronic Codebook mode, or ECB mode, is a simple block encryption mode.

Process:

- The original message is chopped into identical-size blocks.
- Each block is encrypted separately using the same key.
- The same plaintext block with the same key produces the same ciphertext block.

Key weakness:

- ECB does not hide data patterns.
- If two plaintext blocks are identical, their ciphertext blocks are also identical.
- Looking at ciphertext may reveal repeated structure in the original data.

Example:

- The lecture uses the well-known penguin image example.
- After ECB encryption, the visual pattern of the penguin can still be recognized because repeated image blocks produce repeated encrypted blocks.

Advantages:

- Very fast encryption.
- Very fast decryption.
- Blocks can be processed in parallel because each block is independent.

Disadvantages:

- Unsuitable for long messages because patterns may remain visible.
- Susceptible to replay attacks.

## Replay Attacks Against ECB

A replay attack can happen when an attacker steals an entire encrypted message, such as encrypted identity or password information, and sends the same ciphertext to the system again.

Problem:

- If the system accepts the repeated ciphertext as valid, the attacker may gain access.

Defenses mentioned:

- Add a timestamp to the message.
- Use two-way authentication or a separate one-time code, such as a six-digit code sent to a phone or email.

Timestamp defense:

- The system checks whether the embedded timestamp is valid.
- A previously captured encrypted message with an old timestamp should be rejected.

One-time code defense:

- Even if the attacker steals the encrypted identity information, they still need the current authentication code.

## Cipher Block Chaining Mode

Cipher Block Chaining mode, or CBC mode, is presented as safer than ECB.

Main idea:

- Each block depends on the previous ciphertext block.
- Repeated plaintext does not lead to repeated ciphertext.
- Patterns are hidden better than in ECB.

The lecture also connects this chaining idea to blockchain:

- CBC uses a simple chaining concept where output from one block feeds into the next block.

## Initialization Vector

CBC mode starts with an initialization vector, or IV.

Purpose:

- The IV is used for the first plaintext block.
- It helps ensure the same plaintext can produce different ciphertext when a different IV is used.

Important requirement:

- The receiver must know the same IV.
- If the receiver does not have the correct IV, they cannot decrypt properly.

## CBC Encryption Process

CBC encryption is serial, not parallel.

Process:

1. XOR the first plaintext block with the IV.
2. Encrypt the result with the key to produce the first ciphertext block.
3. XOR the second plaintext block with the first ciphertext block.
4. Encrypt the result with the key to produce the second ciphertext block.
5. Continue this process block by block.

Why encryption is serial:

- Each block must wait for the previous ciphertext block.
- The previous block's output becomes input for the next round.

Speed implication:

- CBC encryption is slower than ECB encryption.
- ECB can process blocks in parallel; CBC encryption cannot.

Security benefit:

- Identical plaintext blocks do not necessarily produce identical ciphertext blocks because each block is combined with a different previous ciphertext value.

## CBC Example

The lecture uses a simplified binary example.

Given:

- Original message divided into two-bit blocks.
- IV: `10`
- A cipher table is used as the key.

Encryption flow:

1. First plaintext block `00` is XORed with IV `10`.
   - `00 XOR 10 = 10`
2. The cipher table maps input `10` to ciphertext `11`.
3. The first ciphertext output `11` is fed into the next block.
4. The next plaintext block is XORed with `11`.
5. The resulting value is looked up in the cipher table.
6. Each ciphertext block becomes input for the next block.

Important point:

- CBC encryption chains each ciphertext block into the encryption of the next plaintext block.

## CBC Decryption Introduction

For decryption, the receiver needs:

- The ciphertext.
- The same key or reverse cipher table.
- The same IV used by the sender.

The lecture begins explaining that decryption uses the reverse version of the cipher table:

- If a ciphertext output was originally produced from a certain input, the receiver reverses that mapping.
- For example, if `01` was originally produced from `00`, then during decryption `01` maps back to `00`.

The same IV must be shared with the receiver:

- Without the correct IV, the receiver cannot properly recover the original message.
