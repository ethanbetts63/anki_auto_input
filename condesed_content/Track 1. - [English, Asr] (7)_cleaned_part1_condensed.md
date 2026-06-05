# Authentication, AAA, and Password-Based Authentication

## AAA - authentication, authorization, accountability.

## Identification - subject claims identity.

## Authentication - verifies claimed identity; one-way or two-way.

## Authorization / Access Control - grants permissions/resources after authentication.

## Accountability - logs actions such as login time, duration, transactions; costs storage/resources.

## Auth Flow - initiation, challenge, proof, validation, decision.

## Auth Zones - client secrets, transmission interception, server credential storage.

## Auth Factors - know: password; have: certificate/OTP/token; are: biometric.

## Password Auth - cheap/familiar/interoperable but weak alone and vulnerable in all zones.

## Client-Zone Attacks - local exposure, brute force, phishing.

## Transmission-Zone Attacks - sniffing/interception.

## Server-Zone Attacks - insider access, compromise, dictionary attacks.

## Password Managers - encrypted storage for many passwords.

## Plain Passwords - never store/send; leak via insiders, compromise, sniffing.

## Encrypted Password Issues - stolen key exposes data; same passwords/lengths may leak.

## Password Hashing - fixed-length, deterministic, one-way, no key; store/compare hashes.

## Hash Reset Caveat - original password cannot be recovered; reset instead.

## Rainbow Table - precomputed password-hash lookup; cracks weak/common hashes.

## Password Rule - long, complex, uncommon passwords.
