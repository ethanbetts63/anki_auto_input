# Diffie-Hellman Algorithm

## Overview

The Diffie-Hellman algorithm was proposed by Whitfield Diffie and Martin Hellman.

It allows two parties to generate a shared secret key without:

- Meeting in person beforehand
- Sharing a secret beforehand
- Using a third party to distribute the key

This is useful for symmetric encryption, where two parties need to share the same symmetric key before encryption can happen.

The main idea is that two parties can independently calculate the same shared secret number, even though that secret number is never directly sent over the communication channel.

## General Process

Diffie-Hellman key exchange follows these steps:

1. Both parties agree on public parameters.
2. Each party generates a private key known only to themselves.
3. Each party computes a public key.
4. They exchange public keys.
5. Each party uses their own private key and the other party's public key to compute the same shared secret.

The shared secret can then be used as a symmetric key, for example with DES or Triple DES.

## Example Goal

Alice and Bob want to share a common secret.

- The common secret should be known only to Alice and Bob.
- No third party should know it.
- In the lecture example, the shared secret is `18`.

## Step-by-Step Example

### 1. Agree on Public Parameters

Alice and Bob agree on two public values:

```text
g = 7
p = 23
```

These values can be shared openly.

The lecture uses small numbers for demonstration, but real systems use much larger values.

### 2. Choose Private Keys

Alice and Bob each choose a private key:

```text
Alice private key = 3
Bob private key = 6
```

They do not share these numbers with each other or with any third party.

### 3. Compute Public Keys

Alice computes her public key using the public parameters and her private key:

```text
Alice public key = 7^3 modulo 23
Alice public key = 21
```

Alice sends `21` to Bob.

Bob computes his public key using the public parameters and his private key:

```text
Bob public key = 7^6 modulo 23
Bob public key = 4
```

Bob sends `4` to Alice.

The public keys exchanged over the public channel are:

- Alice sends `21`
- Bob sends `4`

### 4. Compute the Shared Secret

Alice receives Bob's public key `4`. She uses Bob's public key and her own private key:

```text
Alice shared secret = 4^3 modulo 23
Alice shared secret = 18
```

Bob receives Alice's public key `21`. He uses Alice's public key and his own private key:

```text
Bob shared secret = 21^6 modulo 23
Bob shared secret = 18
```

Both sides calculate the same shared secret:

```text
shared secret = 18
```

Alice and Bob have created the same secret key without sending the secret itself.

## Security Reasoning

Suppose Eve is listening to all communication between Alice and Bob.

Eve can hear:

- Public parameter `g = 7`
- Public parameter `p = 23`
- Alice's public key `21`
- Bob's public key `4`

Eve does not know:

- Alice's private key `3`
- Bob's private key `6`

Eve also knows the theory of the Diffie-Hellman calculation and knows that modulo arithmetic is being used.

For Alice, calculating her public key is easy because she knows her private key:

```text
A = g^x modulo p
```

In the example:

```text
21 = 7^x modulo 23
```

Eve knows `21`, `7`, and `23`, but does not know the exponent `x`, which is Alice's private number.

The hard problem for Eve is to derive the private exponent from the public result. In other words, going from the public value back to the private exponent is difficult.

Without knowing Alice's or Bob's private exponent, Eve cannot calculate the shared secret `18`.

## Applications

Diffie-Hellman key exchange is widely used in cryptographic protocols, including:

- SSL
- TLS
- VPN protocols, where VPN means Virtual Private Network
- Secure messaging applications

## Summary

Diffie-Hellman is a cornerstone of modern cryptography because it enables secure key exchange over a public communication channel. Its security relies on mathematical principles that make it hard for an eavesdropper to derive the private values or the final shared secret from the public information alone.
