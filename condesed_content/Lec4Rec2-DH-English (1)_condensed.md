# Diffie-Hellman Algorithm

## Diffie-Hellman - creates shared secret over public channel without prior shared secret/third party.

## Purpose - generate symmetric key for later encryption.

## Core Idea - both parties compute same secret without sending it.

## Process - agree public parameters, choose private keys, compute/exchange public keys, compute shared secret.

## Example Public Parameters - `g = 7`, `p = 23`.

## Example Private Keys - Alice `3`, Bob `6`.

## Alice Public Key - `7^3 mod 23 = 21`.

## Bob Public Key - `7^6 mod 23 = 4`.

## Alice Shared Secret - Bob public key with Alice private: `4^3 mod 23 = 18`.

## Bob Shared Secret - Alice public key with Bob private: `21^6 mod 23 = 18`.

## Shared Secret - both compute `18`; never transmitted.

## Eve Sees - `g`, `p`, Alice public key, Bob public key.

## Eve Lacks - Alice/Bob private exponents.

## Hard Problem - deriving private exponent from `A = g^x mod p`.

## Security - without private exponents, Eve cannot compute shared secret.

## Applications - SSL, TLS, VPNs, secure messaging.

## Summary - secure public-channel key exchange based on hard modular exponent reversal.
