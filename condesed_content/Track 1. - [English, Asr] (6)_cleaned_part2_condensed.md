# Asymmetric Cryptography, Digital Signatures, and Certificates

## Online Purchase Confidentiality - Amazon publishes public key; customers encrypt; only Amazon private key decrypts.

## Asymmetric vs Symmetric Purchase Keys - one Amazon key pair replaces per-customer symmetric key distribution/storage.

## Public-Key Authenticity Problem - MITM can swap Amazon public key; customer encrypts to attacker.

## Key Use Cases - confidentiality can use receiver key pair; authentication needs each signer identity key pair.

## Document Signing Goals - prove sender, prevent modification, prevent denial, prevent reuse on another message.

## Signature Creation - hash message; encrypt hash with sender private key; send message plus signature.

## Signature Verification - hash received message; decrypt signature with sender public key; compare hashes.

## Signature Properties - integrity, authenticity, and non-repudiation.

## Modified Message Detection - changed message causes hash mismatch.

## Code Signing - publisher signs code hash; users verify origin and unchanged code.

## Digital Certificate Creation - issuer hashes certificate info and signs hash with issuer private key.

## Digital Certificate Verification - verifier rehashes info, decrypts signature with issuer public key, compares hashes.

## Certificates for Public-Key Trust - CA certifies that a public key belongs to a named party.

## CSR - business submits public key/identity; CA signs certificate with CA private key.

## Browser Verification - browser verifies CA signature/hash/public key; warns if invalid, expired, or untrusted.

## CA Role - provide market trust and prevent public-key substitution/MITM.

## Crypto Goals - confidentiality, integrity, authenticity, non-repudiation; not availability.

## Future Topics - PKI authentication, SSL/TLS, and symmetric/asymmetric combinations.
