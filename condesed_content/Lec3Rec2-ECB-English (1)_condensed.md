# Modern Symmetric Encryption and ECB Mode

## Modern Cryptography

Modern cryptography is not based on simple transposition and substitution. It aims to prevent third-party eavesdropping more securely.

The lecture introduces modern symmetric encryption through the XOR operation with a key.

All computer calculations are based on binary calculation, using only:

- `0`
- `1`

## XOR Operation

XOR takes two inputs, `A` and `B`, and produces an output.

Rules:

- If `A` and `B` are the same, the output is `0`.
- If `A` and `B` are different, the output is `1`.

Truth table:

| A | B | A XOR B |
|---|---|---------|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

## XOR in Encryption

In the encryption example, the original message is XORed with the key to generate ciphertext `C`.

For each bit:

- Different digits generate `1`.
- The same digits generate `0`.

The lecture example produces ciphertext:

- `10010010`

## Properties of XOR

XOR has several important properties:

- `A XOR 0 = A`
- `A XOR 1 = NOT A`
- `A XOR A = 0`
- XOR behaves like addition in the sense that grouping does not matter; the order of calculation can be changed.

The property `A XOR A = 0` follows from the rule that two identical digits XORed together produce `0`.

## Encryption and Decryption with XOR

Encryption:

- `M XOR K = C`

Where:

- `M` is the original message.
- `K` is the key.
- `C` is the ciphertext.

Decryption:

- `C XOR K = M`

The same key is used again during decryption.

Reason:

```text
C XOR K
= (M XOR K) XOR K
= M XOR (K XOR K)
= M XOR 0
= M
```

Because `K XOR K = 0` and `M XOR 0 = M`, XORing the ciphertext with the same key recovers the original message.

In the lecture example, decrypting with the same key recovers the original message:

- `01001011`

## Key Requirements for Perfect Safety

To make encryption and decryption theoretically 100% safe from eavesdropping:

- The key should be a random series of numbers.
- The key should not be crackable by a third party.
- The key should be the same length as the plaintext.
- The key should be used only once.

This is not practical in reality.

Practical problems:

- Truly random numbers are difficult to obtain in practice.
- If the sender and receiver can already share the key securely, then they could also exchange the message securely.
- Therefore, a major problem is how to design a practical key and secure the encryption process.

## Symmetric Encryption

Symmetric encryption means the encryption key and decryption key are the same.

The same key is needed because XOR decryption depends on applying the same key a second time to recover the original message.

The lecture frames encryption and decryption operations as based on XOR.

## Block Cipher Operation

In practical block cipher encryption:

1. The key has a fixed length.
2. The original message is chopped into blocks with the same length as the key.
3. For example, message `M` may be chopped into `M1`, `M2`, `M3`, through `M6`.
4. If the last block, such as `M6`, is not long enough, padding is added.
5. Each message block is XORed with the key.
6. Ciphertext blocks are produced.
7. During decryption, each ciphertext block is XORed with the same key again.
8. The plaintext message `M` is recovered.

## Electronic Codebook Mode

The block cipher encryption mode described above is called **Electronic Codebook mode**, or **ECB mode**.

ECB is the simplest symmetric encryption mode.

## Advantages of ECB Mode

ECB allows parallel encryption:

- The original message is chopped into blocks.
- Blocks can perform bitwise XOR operations at the same time.
- This makes encryption very fast.

ECB also allows parallel decryption:

- Ciphertext blocks can be XORed with the key at the same time.
- This makes decryption very fast.

## Weakness: Repeated Blocks Reveal Patterns

If two plaintext blocks contain the same binary data, their ciphertext blocks will also be the same.

As a result, patterns from the original plaintext may still be visible after encryption. An attacker may be able to deduce whether original blocks such as `M1` and `M2` were the same.

The lecture uses the common image example:

- A picture can be represented in binary.
- When the picture is encrypted with ECB mode, identical plaintext blocks produce identical ciphertext blocks.
- The encrypted image still reveals the pattern of the original picture.
- Therefore, the confidentiality of the original message is not perfectly protected.

## Replay Attack

ECB mode is vulnerable to replay attack.

A **replay attack** occurs when an attacker intercepts a valid message and resends that message as many times as desired.

Example:

1. An attacker sniffs packets during a wire transfer transaction.
2. The attacker identifies which ciphertext corresponds to logging into a bank account.
3. The attacker does not need to decrypt the message or learn the password.
4. The attacker resends the intercepted encrypted login ciphertext to the bank system.
5. The system may log the attacker in based on the replayed valid ciphertext.

## Defenses Against Replay Attack

The usual defense is to include a unique value in each message, such as:

- A unique identifier
- A timestamp

This lets the recipient detect repeated messages.

Messages should also be protected against modification using a **message authentication code**. Otherwise, an attacker could simply change the identifier or timestamp.

## Key Takeaways

- Modern symmetric encryption uses the same key for encryption and decryption.
- XOR is central in the lecture's explanation because applying the same key twice recovers the original message.
- A theoretically ideal key would be random, plaintext-length, and used only once, but this is impractical.
- ECB mode is simple and fast because encryption and decryption can be done in parallel.
- ECB leaks patterns when plaintext blocks repeat.
- ECB is vulnerable to replay attack.
- Replay defenses require unique identifiers or timestamps, plus message authentication to prevent modification.
