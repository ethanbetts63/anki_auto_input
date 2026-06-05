# Asymmetric Cryptography: Confidentiality and Authenticity

## Lecture Context - RSA/Diffie-Hellman applications; public/private key pair; different encryption/decryption keys.

## Goals - asymmetric crypto supports confidentiality, authenticity, non-repudiation, and integrity with hashes.

## Combining Algorithms - symmetric ciphers plus hashes/signatures combine confidentiality with integrity/authenticity.

## Symmetric E-Commerce Problem - one secret key per customer does not scale to millions.

## Symmetric Conferencing Problem - pairwise keys required: `n x (n - 1) / 2`.

## Symmetric Authentication Problem - shared key with the wrong party defeats secrecy; receiver identity must be trusted.

## Security Services - symmetric gives confidentiality; asymmetric gives confidentiality/authenticity/non-repudiation; integrity needs hashes.

## RSA Confidentiality - encrypt with receiver public key; decrypt with receiver private key.

## Amazon Credit Card Example - customers encrypt with Amazon public key; only Amazon private key decrypts.

## Confidentiality Caveat - sender must have the receiver's real public key.

## RSA Authenticity - sign/encrypt with sender private key; verify/decrypt with sender public key.

## Amazon Authenticity Example - Amazon signs with private key; customer verifies with Amazon public key.

## Classroom Public Keys - trusted name-to-public-key list lets students verify lecturer-signed announcements.

## Signature Text - private-key-created text verified by the matching public key.

## Public-Key Trust Assumption - first public-key exchange can be replaced; needs a trust mechanism.

## Why Public Keys Scale - public key can be shared openly; private key stays secret; avoids many symmetric secrets.
