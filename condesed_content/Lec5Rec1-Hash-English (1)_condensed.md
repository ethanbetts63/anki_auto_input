# Hash Functions

## Definition

A hash function is a mathematical algorithm that transforms an input or message into a fixed-size string of bytes.

The output is usually represented as a hexadecimal number and is called:

- Hash value
- Hash code
- Digital fingerprint of the data

The hash value is associated with the input data. A unique input should produce its own hash value, although collisions are theoretically possible.

Hash functions are designed to be fast and efficient so that data can be processed and retrieved quickly.

## Required Properties of a Hash Function

### Deterministic

A hash function should always produce the same output for the same input.

This ensures consistency in data representation.

### Fixed-Length Output

Regardless of the size of the input data, the output hash value should always have a fixed length.

### One-Way Function

It should be computationally infeasible to reverse engineer the original input from its hash value.

The lecture describes this as:

- It is easy to calculate `y` from `x`.
- It is very hard to find `x` if only `y` is known.

This property is important for maintaining data confidentiality.

### Collision Resistance

A good hash function should minimize the chance that two different inputs produce the same hash output.

Collisions can theoretically occur, but a strong hash function makes them extremely unlikely.

### Avalanche Effect

A small change in the input, even a single bit, should produce a significantly different hash output.

This ensures that similar inputs do not produce similar hash values.

## Uses of Hash Functions

Hash functions can help provide:

- Data integrity
- Protection against unauthorized access
- Protection against tampering

Hash functions can also be combined with RSA or Diffie-Hellman to support data integrity and authentication purposes.

For authentication, hash functions can help protect password confidentiality.

## MD5 Hash Function

MD5 is one example of a hash function.

The lecture shows one operation of MD5. Actual MD5 consists of 64 such operations.

In the shown MD5 operation:

- `B`, `C`, and `D` are each 32-bit values.
- `M_i` denotes a 32-bit block of message input.
- `K_i` denotes a 32-bit constant that is different for each operation.
- A shift operation shifts left by `s` places, where `s` varies for each operation.
- Another operation denotes addition modulo.

The exact internal operation of MD5 does not need to be memorized for the course.

In practice, a command such as:

```text
md5sum
```

can generate an MD5 hash from any message.

MD5 produces a 128-bit hash result.

## Other Hash Functions

Other hash functions include members of the SHA family.

The lecture refers to:

- SHA-1
- SHA-2 family
- SHA-3

### MD5

MD5 is an early hash function.

Its collision resistance has been broken, meaning examples have been found where different inputs generate the same hash.

Although this may not happen often, the existence of such collisions makes MD5 weaker.

### SHA-1

SHA-1 is a later hash function designed in 1995.

Its collision resistance has been weakened. This means the probability of finding a collision is small, but not negligible.

### SHA-2

The SHA-2 family is relatively stronger than MD5 and SHA-1.

### SHA-3

SHA-3 is the latest member of the SHA family of standards mentioned in the lecture.

It was released in 2015.

## MD5 Compared with SHA

MD5:

- Is faster
- Produces a smaller hash result
- Is less secure because its collision resistance has been broken

SHA family:

- Is more secure
- Produces longer hash results

## Key Caveat

No matter which hash function is used, the hash function may be combined with public key algorithms such as RSA or key exchange algorithms such as Diffie-Hellman for security goals such as integrity and authentication.
