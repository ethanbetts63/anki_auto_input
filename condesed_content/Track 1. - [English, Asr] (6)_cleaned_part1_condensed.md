# Asymmetric Cryptography: Confidentiality and Authenticity

## Lecture Context

This lecture continues the cryptography topic and focuses on asymmetric cryptography applications.

Assumed background:

- RSA algorithm.
- Diffie-Hellman algorithm.

The lecture focuses less on algorithm internals and more on application scenarios.

Basic assumption:

- Algorithms such as RSA can generate a public key and private key pair.
- The encryption key and decryption key are different.

## Goals of Asymmetric Cryptography

The lecture focuses on how asymmetric cryptography can help achieve:

- Authenticity
- Non-repudiation
- Integrity in combination with other algorithms
- Confidentiality

The goal is to understand how different algorithms can be combined to achieve different security goals.

## Combining Algorithms

Different cryptographic algorithms can be combined to provide multiple security properties.

Examples discussed:

- DES, Triple DES, or AES can be combined with hash algorithms.
- This can provide confidentiality and integrity together.
- In workshop activities, MD5 hash was used to create a signature-like check to determine whether original code had been modified.

Clarification from the lecture:

- Symmetric encryption by itself guarantees confidentiality.
- Integrity requires a hash algorithm or another mechanism.
- Asymmetric cryptography can also support integrity when combined with hash algorithms.

## Why Symmetric Cryptography Is Not Enough

The lecture revisits problems with symmetric cryptography.

### E-Commerce Case

Scenario:

- Millions of customers need to communicate with a server.

Problem with symmetric encryption:

- The server would need to generate a different symmetric key for each customer.
- This means maintaining millions of keys.
- This is not scalable.

### Online Conferencing Case

Scenario:

- Every pair of participants in an online conference wants to exchange secret messages.

Problem:

- Each pair needs a separate symmetric key.
- The number of keys required is:

```text
n x (n - 1) / 2
```

Where:

- `n` is the number of parties.

Additional issues:

- Someone must generate and distribute the keys.
- Someone must oversee key exchange, expiration, and related management.

### Authenticating the Right Party

Symmetric encryption does not by itself authenticate the other party.

Problem:

- If a key is shared with the wrong person, that person can access the secret data.
- The sender must know the key is being shared with the correct receiver.

Asymmetric cryptography helps solve these issues.

## Security Services: Symmetric vs Asymmetric

The lecture compares security services supported by symmetric and asymmetric cryptography.

Important caveat:

- Both symmetric and asymmetric approaches may need to be combined with hash algorithms to provide integrity.

Symmetric cryptography:

- Provides confidentiality by itself.
- Can support integrity only when combined with hash algorithms.

Asymmetric cryptography:

- Can be used to support confidentiality.
- Can be used to support authenticity.
- Can be used to support non-repudiation.
- Can support integrity when combined with hash algorithms.

Availability is not treated as a cryptographic goal in this discussion.

## RSA for Confidentiality

Scenario:

- Alice wants to send confidential information to Bob.
- Bob may represent Amazon.
- Alice may represent a customer.

Each party has:

- A public key.
- A private key.

To preserve confidentiality:

1. Alice obtains Bob's public key.
2. Alice encrypts her confidential message using Bob's public key.
3. Alice sends the encrypted message to Bob.
4. Bob decrypts it using Bob's private key.

Example:

- A customer wants to send credit card information to Amazon.
- The customer encrypts the credit card information using Amazon's public key.
- Amazon decrypts it using Amazon's private key.

Why confidentiality is preserved:

- Many people may know Amazon's public key.
- Many people may see the encrypted message.
- But only Amazon has Amazon's private key.
- Only Amazon can decrypt the credit card information.

Key relationship for confidentiality:

```text
public key for encryption + private key for decryption = confidentiality
```

Important assumption:

- The customer must have the true public key belonging to Amazon.
- If the first public key exchange is compromised, the model has a problem that must be solved separately.

## RSA for Authenticity

To prove a message is truly from a sender, the key order is reversed.

For authenticity:

1. The sender encrypts or signs the message using the sender's private key.
2. The receiver decrypts or verifies it using the sender's public key.

Key relationship for authenticity:

```text
private key for encryption/signing + public key for decryption/verification = authenticity
```

## Amazon Authenticity Example

Scenario:

- A customer wants to ensure a message is truly from Amazon.

Process:

1. Amazon encrypts or signs the message using Amazon's private key.
2. Amazon sends the resulting signed/encrypted text to the customer.
3. The customer uses Amazon's public key to decrypt or verify it.
4. If the message can be verified using Amazon's public key, the customer has confidence that it came from Amazon.

Reason:

- The message must have been created using Amazon's private key.
- Amazon's private key is supposed to be known only by Amazon.

## Classroom Public Key Example

The lecture uses a virtual classroom to explain authenticity.

Scenario:

- There are 28 people in the room.
- Each person generates one public/private key pair.
- Each person shares their public key with the other 27 people.
- Each person keeps their private key secret.

Everyone builds a list of other people's public keys.

Assumption:

- The public key list is clean.
- Each listed public key truly belongs to the named person.

Example message:

- The lecturer wants to send an important exam announcement containing a link and submission date.

Problem:

- Plain text can be forged.
- Simply writing a name at the end of a message is not trustworthy.

Authenticity process:

1. The lecturer encrypts or signs the exam announcement with the lecturer's private key.
2. Students receive the encrypted or signed message.
3. Students look up the lecturer's public key from their trusted public key list.
4. Students use that public key to decrypt or verify the message.
5. If verification succeeds, students trust that the message was created by the lecturer.

Why this works:

- Only the lecturer has the lecturer's private key.
- The corresponding public key verifies the message.
- Other people's public keys would not verify the lecturer's signed message.

The lecture calls this a signature text:

- The text has been signed or encrypted using the sender's private key.
- The associated public key verifies who signed it.

## Public Key Trust Assumption

Both confidentiality and authenticity examples depend on a trusted public key.

For confidentiality:

- The customer must be sure they are using Amazon's true public key before encrypting credit card information.

For authenticity:

- The receiver must be sure the public key used for verification really belongs to the claimed sender.

Risk:

- A public key may be replaced or forged by an attacker during the first exchange.

The lecture notes that a later mechanism is needed to guarantee that the initial public key exchange is trustworthy.

## Why Public Keys Are Easier Than Symmetric Keys

Question addressed:

- If Amazon and customers exchange encrypted messages, why is asymmetric key use easier than sharing symmetric keys?

Answer from the lecture:

- Private keys are not shared.
- Public keys are meant to be public.
- Amazon can announce one public key openly.
- Millions of customers can all use the same Amazon public key to encrypt their credit card information.
- Amazon keeps only its private key secret.
- Attackers may obtain the public key and encrypted messages, but they cannot decrypt the messages without Amazon's private key.

Difference from symmetric encryption:

- Symmetric encryption would require Amazon to generate and manage a different secret key for each customer.
- Asymmetric encryption allows many customers to use Amazon's single public key while only Amazon can decrypt with its private key.
