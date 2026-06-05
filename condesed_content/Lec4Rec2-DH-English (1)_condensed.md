## Diffie-Hellman - shared secret over public channel without prior shared secret/third party.

## Process - agree public parameters, choose private keys, compute/exchange public keys, compute shared secret.

## Example Public Parameters - `g = 7`, `p = 23`.

## Example Private Keys - Alice `3`, Bob `6`.

## Alice Public Key - `7^3 mod 23 = 21`.

## Bob Public Key - `7^6 mod 23 = 4`.

## Alice Shared Secret - Bob public key with Alice private: `4^3 mod 23 = 18`.

## Bob Shared Secret - Alice public key with Bob private: `21^6 mod 23 = 18`.

## Shared Secret - both compute `18`.

## Attacker Sees public keys, but lacks private exponents. Hard to derive private exponent from `A = g^x mod p`.

## Applications - SSL, TLS, VPNs, secure messaging.

