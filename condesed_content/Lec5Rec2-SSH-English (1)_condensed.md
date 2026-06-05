# SSH Public Key Authentication

## SSH Overview

SSH (Secure Shell) is a protocol used to securely connect to remote machines over an unsecured network.

SSH protects communication by encrypting data exchanged between the client and server, helping prevent:

- Eavesdropping
- Data loss or leakage
- Tampering

Common SSH uses include:

- Remote login
- Remote server management
- File transfers
- Secure communications
- Execution of commands on remote systems

## SSH Authentication Types

SSH supports two main authentication methods:

- Password-based authentication
- Public key authentication

### Password-Based Authentication

Password-based authentication requires the client to provide the correct password or credential combination before the server grants access.

### Public Key Authentication

Public key authentication uses a public/private key pair and the RSA algorithm.

It improves security by:

- Avoiding password vulnerabilities
- Verifying user identity using cryptographic keys
- Preventing unauthorized access to the remote server
- Encrypting SSH data transmission

It also improves convenience because users do not need to remember many passwords.

## Setting Up SSH Key Authentication

Before public key authentication can be used, the client and server must be prepared.

### 1. Generate a Key Pair

The client generates a key pair:

- Public key
- Private key

The private key remains with the client.

### 2. Copy the Public Key to the Server

The client copies the public key to the server.

The server stores the public key in the appropriate SSH authorization file. In the workshop activity, this setup step is required before testing passwordless SSH login.

### 3. Test the SSH Connection

After the public key is stored on the server, the client can connect using SSH.

If key authentication is configured correctly, the user can log in without entering a password.

## Public Key Authentication Process

The authentication process verifies that the client possesses the private key corresponding to the public key stored on the server.

### Preparation

Before the connection request:

- The client has generated a public/private key pair.
- The client's public key has been copied to the remote server.
- The server already has the public key associated with that client.

### Step 1: Client Requests an SSH Connection

The client initiates an SSH connection request to the server.

### Step 2: Server Sends an Encrypted Challenge

The server:

- Generates a random number.
- Combines it with a session ID.
- Encrypts the message using the client's public key.
- Sends the encrypted message back to the client.
- Keeps a hash value generated from the random number and session ID.

### Step 3: Client Decrypts the Challenge

The client receives the encrypted message and uses its private key to decrypt it.

After decryption, the client obtains:

- The random number
- The session ID

The client then generates the same hash value from the random number and session ID.

### Step 4: Client Signs or Encrypts the Hash

The client encrypts the hash value using its own private key.

In the lecture transcript, the hash is described as an MD5 hash.

The client sends this encrypted hash value back to the server.

### Step 5: Server Verifies the Client

The server:

- Receives the encrypted hash value from the client.
- Decrypts it using the client's stored public key.
- Retrieves the clear hash value.
- Compares it with the hash value the server kept earlier.

If the two hash values match, the server concludes that the client possesses the matching private key.

The server then authenticates the client and grants access.

## Security Reasoning

The authentication depends on possession of the private key.

Only the legitimate client should be able to:

- Decrypt the server's challenge using the private key.
- Produce the correct hash from the random number and session ID.
- Encrypt or sign that hash using the private key.

The server can verify the result using the corresponding public key.

## Man-in-the-Middle Consideration

A man-in-the-middle attacker may observe:

- The initial connection request
- The encrypted challenge sent from the server to the client
- The message sent from the client back to the server

However:

- The attacker does not have the client's private key.
- The attacker cannot decrypt the server's encrypted challenge to obtain the random number.
- Even if the attacker has the client's public key and can read some later message, the random number itself is not the secret that matters.
- The attacker cannot impersonate the client because they cannot encrypt or sign the required value using the client's private key.

Therefore, the attacker cannot prove possession of the private key and cannot be authenticated as the client.

## Key Concept

SSH public key authentication uses private-key operations and public-key verification to prove the client's identity.

The server stores the client's public key and challenges the client to prove possession of the matching private key. If the proof succeeds, the server verifies the client's identity and grants access.

## Summary

- SSH securely connects clients to remote machines over unsecured networks.
- SSH encrypts data exchanged between client and server.
- SSH supports password-based and public key authentication.
- Public key authentication uses a public/private key pair.
- The public key is stored on the server before authentication.
- The private key remains with the client.
- During login, the server challenges the client.
- The client proves possession of the private key.
- The server verifies the proof using the stored public key.
- Public key authentication helps prevent impersonation and unauthorized access.
