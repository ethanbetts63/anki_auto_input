# Classical Cryptography

## Classical Crypto - based on transposition and substitution for secret messages.

## Transposition - rearrange symbol order.

## Substitution - replace symbols with other symbols.

## Shift Substitution - shift letters by fixed key; receiver shifts back.

## Encryption Form - `E_n(m) = c`.

## Decryption Form - `D_n(c) = m`.

## Caesar Cipher - fixed-position letter shift.

## Variable Shift Key - key like `0351` shifts each position differently, then repeats/reverses.

## Breaking Classical Crypto - analyze preserved ciphertext patterns.

## Frequency Analysis - compare ciphertext letter frequencies to normal language frequencies.

## English Frequency Clues - `E`, `T`, `A` common; `Z` rare.

## Monoalphabetic Substitution - each plaintext symbol always maps to same ciphertext symbol.

## Monoalphabetic Weakness - language frequency patterns remain visible.

## Polyalphabetic Substitution - frequency analysis alone insufficient; needs other clues.

## Decryption Process - count frequencies, guess mappings, substitute, inspect partial plaintext.

## Small Text Limitation - short ciphertext may not match normal English frequencies well.

## Digraphs/Trigraphs - common pairs/triples like `THE` reveal mappings.

## Example Clue - if `OIS` likely equals `THE`, then `O=T`, `I=H`, `S=E`.

## Lesson - substitution/transposition ciphers are weak because language patterns leak.

## Modern Transition - modern crypto uses stronger techniques than simple classical patterns.
