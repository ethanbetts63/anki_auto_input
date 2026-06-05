## RSA - public-key cryptography for secure transmission, signatures, key exchange.

## RSA Security - hard to factor large `n = p * q`.

## Key Generation - choose primes `p`, `q`.

## Calculate n - `n = p * q`; example `2 * 7 = 14`.

## Calculate v - `v = (p - 1) * (q - 1)`; example `6`.

## Choose e - odd, prime to `v`, example `6 mod 5 = 1`, so `e = 5`.

## Public Key - `(e, n)`; example `(5, 14)`.

## Choose d - `d * e mod v = 1`; example `11 * 5 mod 6 = 1`, so `d = 11`.

## Private Key - `(d, n)`; example `(11, 14)`.

## Small RSA Weakness - small `n` is easy to factor, exposing `p`, `q`, `v`, and `d`.

## Real RSA Security - large primes make factoring `n` infeasible.

## Size Example - `2^1000 ≈ 10^300`; huge factorization problem.

## Legitimate User - knows `p`, `q`; derives `n` and private `d`.

## Attacker - knows `n` but cannot feasibly recover large `p`, `q`, or `d`.

## Encryption Formula - `ciphertext = message^e mod n`; example `2^5 mod 14 = 4`.

## Decryption Formula - `message = ciphertext^d mod n`; example `4^11 mod 14 = 2`.
