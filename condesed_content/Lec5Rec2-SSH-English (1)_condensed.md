# SSH Public Key Authentication

## SSH - secure remote connection over unsecured networks.

## SSH Protects - encryption against eavesdropping, leakage, tampering.

## SSH Uses - remote login, server management, file transfer, commands.

## SSH Auth Types - password-based and public-key authentication.

## Password Auth - client supplies correct password/credentials.

## Public-Key Auth - RSA key pair proves identity without password weaknesses.

## Public-Key Benefits - stronger identity proof, less password reliance, encrypted transmission.

## Setup Step 1 - client generates public/private key pair.

## Setup Step 2 - private key stays client-side.

## Setup Step 3 - public key copied to server authorization file.

## Setup Step 4 - test passwordless SSH login.

## Auth Goal - prove client has private key matching server-stored public key.

## Connection Request - client initiates SSH connection.

## Server Challenge - random number + session ID encrypted with client public key; server keeps hash.

## Client Decryption - client uses private key to recover random number/session ID.

## Client Response - hashes random/session ID and signs/encrypts hash with private key.

## Server Verification - decrypts response with stored public key and compares hash.

## Success Condition - matching hashes prove client private-key possession.

## Security Reasoning - only private-key holder can decrypt challenge and sign correct response.

## MITM View - attacker sees traffic but lacks private key and cannot prove possession.

## Key Concept - server challenges; client proves private key; server verifies with public key.
