# Symmetric Cryptography: CBC Decryption, Standards, Applications, and Key Problems

## CBC Decryption

In Cipher Block Chaining mode, the receiver decrypts the transmitted ciphertext using:

- The same key or reverse cipher table.
- The same initialization vector, or IV.
- The previous ciphertext block for each block after the first.

Process:

1. Take the first ciphertext block.
2. Use the key or decipher table to reverse the encryption.
3. XOR the result with the IV to recover the first plaintext block.
4. For the second ciphertext block, reverse it using the key or decipher table.
5. XOR that result with the previous ciphertext block, not the IV.
6. Continue block by block.

Example details from the lecture:

- A ciphertext block `11` is checked against the decipher table.
- If `11` originally came from `10`, then decryption first recovers `10`.
- That value is XORed with the IV `10`.
- `10 XOR 10 = 00`, recovering the first plaintext block.
- For the next block, the previous ciphertext block is used as the XOR input.

## CBC Decryption Can Be Parallel

CBC decryption can be done in parallel.

Reason:

- A block does not need to wait for the previous block's decrypted output.
- Each block only needs the current ciphertext block and the previous ciphertext block, which are already available in the transmitted ciphertext.

Contrast with encryption:

- CBC encryption must be serial because each block needs the previous block's newly generated ciphertext.
- CBC decryption can be faster because blocks can be processed at the same time.

Speed comparison:

- CBC encryption is slower than ECB encryption.
- CBC decryption can be quick.

## Key and IV Requirements in Symmetric Encryption

Symmetric encryption uses the same key for encryption and decryption.

Requirements:

- The sender and receiver must share the same key securely.
- In CBC mode, the receiver must also know the IV.
- If the receiver has the key but not the correct IV, decryption will not work properly.

Security note:

- The key must be shared secretly and safely.
- If the key is disclosed, secrecy is lost.

For CBC:

- Changing the IV changes the ciphertext even for the same message.
- This adds a layer of security.
- The lecture says changing the IV helps prevent replay attacks because repeated messages will not produce the same encrypted output.

## Other Symmetric Modes

The lecture mentions that other modes also exist, such as output feedback mode.

General idea:

- Different modes arrange encryption and decryption steps differently.
- They have different advantages and disadvantages.
- Some modes may be faster, while others may be slower.
- Most rely on bitwise operations combined with a key or cipher table.

## Why Simple Bitwise Encryption Is Not Enough

If encryption only performs a single bitwise operation, it is not safe enough.

Risks:

- A disclosed key breaks secrecy.
- A disclosed IV can weaken the mode.
- Short keys or simple operations may be cracked.

This motivated the design of encryption standards that make bitwise-based operations more complicated.

## DES: Data Encryption Standard

DES stands for Data Encryption Standard.

Background:

- Designed more than 50 years ago.
- Created because simple one-time bitwise operations were not safe enough.

High-level process:

- The original input is chopped into 64-bit blocks.
- Each block is split into left 32 bits and right 32 bits.
- One side is processed using a function and a key.
- Operations include shifting/permutation and XOR.
- Left and right sides are swapped.
- The process repeats for multiple rounds.

DES uses:

- 16 rounds.
- A different key for each round.

Important point:

- DES is much more complicated than a single XOR operation.
- DES is no longer considered safe because it has been cracked.

## Triple DES

Triple DES applies DES three times.

Characteristics:

- Each DES operation includes 16 rounds.
- Triple DES effectively involves 48 rounds.
- It is safer than DES.
- It is much slower because it repeats DES three times.

Security status from the lecture:

- Triple DES is still regarded as relatively safe compared with DES.
- It still has risk of being cracked.
- Its speed is a major disadvantage.

## AES: Advanced Encryption Standard

AES stands for Advanced Encryption Standard.

Purpose:

- Designed because people were not satisfied with the speed of Triple DES.
- Intended to be faster and stronger than Triple DES.

Characteristics:

- Uses different key-size options.
- Longer keys generally make encryption stronger, though they may affect speed.
- AES is faster than DES and Triple DES in the lecture's comparison.
- AES provides better security than Triple DES.

Practical recommendation from the lecture:

- If a router or system offers AES or Triple DES, choose AES.
- AES gives faster speed and better protection.

## DES, Triple DES, and AES Comparison

The lecture compares these standards by:

- Invention time.
- Key size.
- Block size.
- Number of rounds.
- Speed.
- Security.

General comparison:

- DES: symmetric cipher, 16 rounds, slow, cracked.
- Triple DES: symmetric cipher, 48 rounds, very slow, stronger than DES but still with cracking risk.
- AES: symmetric cipher, fast, stronger than Triple DES, widely used.

All are symmetric ciphers:

- The same key is used for encryption and decryption.
- If an IV is used, the IV must also be shared with the receiver.

## Applications of Symmetric Cryptography

Symmetric cryptography is widely used because it is fast.

Applications mentioned:

- Secure internet communication.
- File encryption and decryption.
- Server data encryption.
- Banking sector systems.
- Payment applications.
- Secure online protocols.

Reason for continued use:

- Symmetric cryptography is based on bitwise calculations.
- Even with many rounds, it is still much faster than asymmetric cryptography.

Contrast:

- Asymmetric cryptography is based on exponential calculations and repeated multiplication.
- Asymmetric cryptography is much slower.

## Security Goals Achieved by Symmetric Cryptography

By itself, symmetric encryption mainly guarantees:

- Confidentiality

It does not by itself solve:

- Authenticity
- Integrity
- Non-repudiation

To achieve other goals, symmetric encryption must be combined with other algorithms, such as hash-based mechanisms.

## Key Exchange Problem

Symmetric encryption requires the same secret key to be shared between sender and receiver.

Main problem:

- The key must be exchanged securely.
- If the key is disclosed, confidentiality is lost.

For CBC mode:

- The IV must also be shared correctly.
- The receiver cannot decrypt properly without the IV.

## Key Exhaustion and Scalability

Symmetric encryption has a scalability problem called key exhaustion.

If every pair of parties needs a separate secret key:

- 2 parties need 1 key.
- 3 parties need 3 keys.
- 4 parties need 6 keys.
- 5 parties need 10 keys.

Formula:

```text
number of keys = n x (n - 1) / 2
```

Where:

- `n` is the number of parties.
- Each pair needs a separate key for private communication.

Problem:

- The number of required keys grows quickly.
- This makes symmetric encryption hard to scale for large networks.

## Key Distribution Center Problem

One possible architecture is to use a key distribution center.

Role:

- Generate keys.
- Distribute keys securely.
- Oversee key exchange between parties.

Problems:

- Someone must be trusted to act as the key distribution center.
- The center may have access to all keys.
- Since the same symmetric key can decrypt messages, whoever controls all keys could read all conversations.
- It is unclear who should be trusted for this role, such as a government, company, or other external party.

## E-Commerce Scalability Problem

Example:

- Amazon or eBay may have millions of customers.
- If only symmetric encryption were used, Amazon would need to generate and maintain a different symmetric key for each customer.

Problem:

- Millions of customers require millions of separate keys.
- Managing and securely distributing those keys is not realistic.

Conclusion:

- Symmetric encryption alone is not scalable for large online services.
- The growth of large e-commerce platforms depends on asymmetric cryptography, where encryption and decryption keys are different.

## Motivation for Asymmetric Cryptography

Asymmetric cryptography solves problems that symmetric cryptography cannot solve well.

Benefits mentioned:

- No key distribution center is needed in the same way.
- It is scalable to any size of network.
- Encryption and decryption keys are different.
- It can help with authenticity, integrity, and non-repudiation when combined with other algorithms.

Next topic:

- RSA and Diffie-Hellman algorithms.
- Applications of asymmetric cryptography.
