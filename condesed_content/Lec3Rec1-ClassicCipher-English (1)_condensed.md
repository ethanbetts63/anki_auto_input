# Classical Cryptography

## Overview

Classical cryptography is based on:

- **Transposition:** Rearranging the order of symbols.
- **Substitution:** Replacing one symbol with another symbol.

Classical cryptography was initially created for transmitting secret messages, especially in military contexts. In many examples, the original message is mapped into a mysterious or unreadable form by replacing letters or parts of letters with other letters.

## Shift-Based Substitution

A simple substitution rule can shift letters to the right or left by a fixed number of positions.

Example:

- A boy wants to send a secret message to his sister about buying a gift for their mother.
- He uses a key that shifts each letter right by three positions.
- The receiver shifts each letter back by three positions to recover the original message.

For the sender and receiver to communicate, they must share the key. The key tells the receiver how to reverse the encryption.

### Mathematical Form

Encryption can be written as:

- `E_n(m) = c`

This means encrypt message `m` by shifting it by `n` positions, producing ciphertext `c`.

Decryption can be written as:

- `D_n(c) = m`

This means decrypt ciphertext `c` by reversing the shift and recovering message `m`.

## Caesar Cipher

The simple shift cipher was created by Caesar, so it is called the **Caesar cipher**.

In a Caesar cipher:

- The plaintext letters are shifted by a fixed number of positions.
- The ciphertext is produced by the shifted letters.
- Decryption shifts the letters back by the same number.

## More Complex Classical Ciphers

A more complicated shifting and replacement rule can use a key such as `0351`.

In this example:

- The first letter is shifted by 0 positions.
- The second letter is shifted by 3 positions.
- The third letter is shifted by 5 positions.
- The fourth letter is shifted by 1 position.

Decryption performs the reverse operation using the same key known beforehand.

## Breaking Classical Cryptography

Classical cryptographic methods depend on substitution and transposition. Because of this, they can often be attacked by analyzing patterns in the ciphertext.

## Frequency Analysis

In English, some letters are used more frequently than others. Research has produced frequency analysis results for all 26 English letters.

Important examples from the lecture:

- `E` is the most frequently used English letter.
- `T` is the next most frequently used letter.
- `A` is also highly frequent.
- `Z` is among the least frequently used letters.

If the ciphertext is large enough, the frequency distribution of ciphertext letters may become close to the actual frequency distribution of English letters.

Frequency analysis can help break encrypted messages, especially when a **monoalphabetic substitution cipher** is used.

## Monoalphabetic Substitution Cipher

A **monoalphabetic substitution cipher** is a cipher in which each occurrence of a plaintext symbol is replaced by a corresponding ciphertext symbol to generate the ciphertext.

Because the same plaintext symbol is always replaced by the same ciphertext symbol, the frequency patterns of the original language may still appear in the ciphertext.

## Polyalphabetic Substitution Cipher

For a **polyalphabetic substitution cipher**, frequency analysis alone is not enough. It must be combined with other knowledge to decrypt the ciphertext.

## Example: Using Frequency Analysis to Decrypt Ciphertext

The lecture demonstrates decrypting a paragraph of ciphertext copied from a workshop instruction document.

The process:

1. Copy the ciphertext into a frequency-analysis website.
2. Click the option to find frequencies.
3. Compare the ciphertext letter frequencies with typical English letter frequencies.
4. Use likely mappings as guesses.
5. Apply substitutions.
6. Observe whether the resulting partially decrypted text makes sense.
7. Use English word patterns, digraphs, and trigraphs to improve the substitution guesses.

### Initial Frequency Clues

In the example paragraph:

- `S` is the most frequently used ciphertext letter.
- `Z` and `T` are among the least frequently used ciphertext letters.

Because `E` is usually the most frequent letter in English, it is likely that ciphertext `S` may represent plaintext `E`.

Because `T` is also highly frequent in English, another frequent ciphertext letter, such as `O`, may represent plaintext `T`.

These guesses are applied as substitutions, and the resulting partial plaintext is inspected.

### Interpreting Substitution Output

After applying substitutions:

- Lowercase letters show decrypted letters produced from ciphertext guesses.
- Capital letters show letters that have not yet been decrypted.

The mapping is not always perfectly obvious from frequency analysis because the ciphertext paragraph may be small. A small paragraph may not have frequencies that accurately match full English language frequencies.

Therefore, frequency analysis must be combined with knowledge of English words and meaningful letter patterns.

### Digraphs and Trigraphs

The lecture uses common letter combinations to find more clues.

Examples:

- The trigraph `THE` is very common in English.
- If a ciphertext combination appears frequently and matches the position of `THE`, it may reveal more letter mappings.
- In the example, `OIS` is likely to represent `THE`.
- Since `O` was guessed as `T` and `S` was guessed as `E`, `I` is likely to represent `H`.

The lecture also refers to counting digraphs and trigraphs to identify common combinations.

Other possible clues are tested by seeing whether substitutions produce meaningful English, such as:

- A ciphertext pattern that may represent `TO`
- A ciphertext pattern that may represent `ONE`

The substitution process continues until the original plaintext can be recovered.

## Lesson from Frequency Analysis

Frequency analysis can help crack classical ciphers because classical ciphers preserve meaningful language patterns, especially when they rely on substitution and transposition.

This demonstrates that classical ciphers based on substitution and transposition are not very secure.

## Transition to Modern Cryptography

Modern ciphers, including symmetric encryption, are not based on simple transposition and substitution in the same way. Modern cryptography uses different techniques to provide stronger security.
