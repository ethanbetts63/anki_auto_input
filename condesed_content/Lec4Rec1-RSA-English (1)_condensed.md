# RSA Algorithm

## Overview

RSA is a widely used public key cryptography system for secure data transmission and digital signatures. It is named after its three inventors.

RSA uses a pair of keys:

- **Public key**: shared openly and used for encryption.
- **Private key**: kept secret and used for decryption.

The security of RSA is based on the difficulty of factorizing the product of two large prime numbers.

## RSA Key Generation

RSA key generation produces a public key and a private key.

### 1. Choose Two Prime Numbers

Select two large prime numbers:

- `p`
- `q`

For demonstration, small prime numbers are used:

- `p = 2`
- `q = 7`

In real RSA, these numbers must be very large.

### 2. Calculate `n`

Calculate:

```text
n = p * q
```

Example:

```text
n = 2 * 7 = 14
```

The value `n` becomes part of both the public and private keys.

### 3. Calculate `v`

Calculate:

```text
v = (p - 1) * (q - 1)
```

Example:

```text
v = (2 - 1) * (7 - 1)
v = 1 * 6
v = 6
```

### 4. Choose the Public Exponent `e`

Choose an odd integer `e` that is prime to `v` and satisfies:

```text
v modulo e = 1
```

Modulo means calculating the remainder after division.

Example:

```text
6 modulo 5 = 1
```

So:

```text
e = 5
```

The public key is:

```text
(e, n) = (5, 14)
```

### 5. Calculate the Private Number `d`

Choose `d` so that:

```text
d * e modulo v = 1
```

In the example:

```text
d * 5 modulo 6 = 1
```

The value `d` should not equal `e`, because `d` is private and `e` is public.

By searching for a value:

```text
11 * 5 = 55
55 modulo 6 = 1
```

So:

```text
d = 11
```

The private key is:

```text
(d, n) = (11, 14)
```

The final keys in this demonstration are:

- **Public key**: `(5, 14)`
- **Private key**: `(11, 14)`

## Why Small Numbers Are Insecure

In the demonstration, `n = 14`. Since `14` is small, it is easy to factorize:

```text
14 = 2 * 7
```

Once an attacker knows `p` and `q`, they can calculate:

```text
v = (p - 1) * (q - 1)
```

Then, because `e` is public, the attacker can find `d` by solving:

```text
d * e modulo v = 1
```

For the example:

```text
d * 5 modulo 6 = 1
```

This makes it easy to derive:

```text
d = 11
```

Therefore, RSA using small numbers such as `14` is not secure.

## Why Real RSA Is Secure

Real RSA uses very large prime numbers for `p` and `q`.

RSA security depends on the fact that:

- It is easy to calculate `n = p * q` if `p` and `q` are known.
- It is very hard to factorize a large `n` back into `p` and `q` if only `n` is known.

Example:

```text
319 = 11 * 29
```

This is still a small number, but it takes more effort than factorizing `14`.

In real RSA, the numbers are much larger. The lecture describes prime-number products on the scale of thousands of bits. For example:

```text
2^1000 = (2^10)^100
2^10 = 1024, approximately 10^3
2^1000 is approximately 10^300
```

This means an attacker may need to factorize a number around the size of `10^300`, which cannot be done in a reasonable time.

In the workshop example, `p` and `q` are each 32 hexadecimal digits. In binary, each is 128 bits. This is still much smaller than the numbers used in real RSA security.

For a legitimate RSA user:

- They know `p` and `q`.
- They calculate `n`.
- They derive their private key number `d`.

For an attacker:

- They may know only `n`.
- They cannot feasibly derive `p` and `q` from a sufficiently large `n`.
- Without `p` and `q`, they cannot derive `d`.

## RSA Encryption and Decryption Example

RSA can allow anyone to encrypt data using a public key, while only the private-key owner can decrypt it.

Example scenario:

- A customer wants to send credit card information to eBay.
- Everyone can know eBay's public key.
- Only eBay knows the private key.
- The customer encrypts the credit card information using the public key.
- eBay decrypts it using the private key.

### Encryption

Assume the message is:

```text
message = 2
```

Using the public key `(e, n) = (5, 14)`:

```text
ciphertext = 2^5 modulo 14
ciphertext = 4
```

Instead of sending the original number `2`, the customer sends encrypted number `4`.

### Decryption

Using the private key `(d, n) = (11, 14)`:

```text
message = 4^11 modulo 14
message = 2
```

The decrypted value is the original message.

## Key Use

- Anyone can use the public key to encrypt.
- Only the private key can decrypt.
- The public key cannot be used for decryption in this process.

## Applications of RSA

RSA is used in:

- Secure communication
- Digital signatures
- Key exchange

RSA public and private keys can be combined in different ways to support different security scenarios.
