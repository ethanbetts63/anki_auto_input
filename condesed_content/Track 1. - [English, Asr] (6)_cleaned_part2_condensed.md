# Asymmetric Cryptography, Digital Signatures, and Certificates

## Public/Private Key Encryption for Online Purchases

In an online shopping scenario such as Amazon, asymmetric cryptography can protect customer credit card information with a single key pair:

- Amazon generates one public/private key pair.
- Amazon shares the public key publicly with all customers.
- Amazon keeps the private key secret.
- Each customer encrypts their own credit card information using Amazon's public key.
- Only Amazon can decrypt the encrypted credit card information, because only Amazon has the matching private key.

This is more efficient than symmetric encryption for this scenario:

- With symmetric encryption, Amazon would need a different shared secret key for each customer.
- Each customer's symmetric key would need to be distributed securely.
- Amazon would need to store and select the correct symmetric key for each customer to decrypt that customer's data.
- With asymmetric encryption, Amazon only needs one public/private key pair for receiving encrypted credit card data from all customers.

The public key does not need secrecy:

- A public key is meant to be public.
- It can be announced openly.
- Anyone can access it and use it for encryption.
- The private key remains protected by the owner.

The major remaining issue is trust: customers must be sure that the public key they are using actually belongs to Amazon, not to an attacker.

## Public Key Authenticity Problem

Asymmetric encryption assumes the receiver's public key is legitimate. In practice, that assumption must be proven.

Example risk:

- A customer wants to encrypt credit card information for Amazon.
- The customer should use Amazon's public key.
- A man-in-the-middle attacker replaces Amazon's public key with the attacker's public key.
- The customer unknowingly encrypts the credit card information using the attacker's public key.
- The attacker can decrypt the credit card information using the attacker's private key.
- Amazon cannot decrypt it because it was not encrypted with Amazon's real public key.

Therefore, there must be a way to prove that a public key belongs to the claimed organization or person. This is where certificates and certificate authorities are used.

## Different Key Use Cases

The number of key pairs required depends on the security goal.

For confidentiality from customers to Amazon:

- Amazon needs one key pair.
- Customers encrypt using Amazon's public key.
- Amazon decrypts using Amazon's private key.

For authentication of multiple people:

- Each person needs their own public/private key pair.
- A user's private key represents that user's identity in the digital space.
- Others verify that user's messages or signatures using the user's public key.

Public keys can be shared openly, but their ownership must be verifiable.

## Document Signing Scenario

Digital signatures are used when Alice wants to send Bob a message and ensure:

- The message was really sent by Alice.
- The message was not modified.
- Alice cannot later deny sending it.
- Bob cannot falsely claim that Alice sent a different message.
- An attacker in the middle cannot alter the message without detection.

Example:

- Alice sends Bob a message such as "Alice owes Bob $10."
- Alice does not want an attacker to change it.
- Alice does not want Bob to claim the message said "$1000."
- Bob needs confidence that the message came from Alice and was unchanged.

A digital signature should be:

- Authentic.
- Unalterable.
- Not reusable for another message.
- Non-repudiable.

## Creating a Digital Signature

Alice signs a message by combining hashing with her private key.

Process:

1. Alice takes the original message.
2. Alice runs a hash function on the message to create a fingerprint/hash.
   - In workshops, commands such as `md5sum` can generate hashes.
   - Different commands or algorithms produce different types of hashes.
3. Alice encrypts the hash using Alice's private key.
4. The encrypted hash becomes the digital signature.
5. Alice sends Bob the plaintext message together with the encrypted hash/signature.

The encrypted fingerprint does not reveal the original message. It is a protected hash value tied to Alice's private key.

## Verifying a Digital Signature

Bob verifies Alice's signed message by comparing two hash values.

Process:

1. Bob receives:
   - The plaintext message.
   - The encrypted fingerprint/signature.
2. Bob hashes the received plaintext message using the same hash function.
3. Bob decrypts the encrypted fingerprint using Alice's public key.
4. Bob compares:
   - The hash he generated from the received message.
   - The decrypted hash from Alice's signature.
5. If the two hashes match:
   - The message was not modified.
   - The signature was produced using Alice's private key.
   - Alice's identity/authenticity is attached to the message.
   - Alice cannot later deny signing the message.
6. If the hashes do not match:
   - The message has been changed, or
   - The signature does not correspond to the message.

The verification works because:

- Only Alice should have Alice's private key.
- Anything decryptable with Alice's public key must have been encrypted with Alice's private key.
- The hash proves integrity.
- The private-key encryption of the hash proves authenticity and supports non-repudiation.

## Security Properties Provided by Digital Signatures

Digital signatures provide:

- **Integrity:** Any change to the message changes the hash, causing verification to fail.
- **Authenticity:** The signature verifies that the message was signed with the sender's private key.
- **Non-repudiation:** The sender cannot later deny signing, because only the sender should have the private key.

In this case, the private key represents Alice's digital identity.

## Modified Message Detection

If Bob receives a message that differs from the one Alice signed:

- Bob's newly generated hash will differ from the decrypted signature hash.
- The comparison fails.
- Bob knows the message is not trustworthy.
- Integrity is not present.

## Code Signing

Code signing uses the same idea as document signing.

Software publishers can sign their code so users or systems can verify:

- The code is authentic.
- The code came from the claimed publisher.
- The code has not been modified since leaving the publisher.
- The publisher cannot deny publishing the code.

The publisher:

- Hashes the code.
- Encrypts the hash using the publisher's private key.
- Attaches the encrypted hash/signature to the code.

Receivers verify the signature using the publisher's public key and compare hashes.

## Digital Certificate Example

A digital certificate can also be generated using hashing and private-key signing.

Example: Cisco or a university issues a certificate to a student.

Certificate creation process:

1. The issuer collects certificate information such as:
   - Student name.
   - Date of birth.
   - Graduation year.
   - ID information.
2. The issuer generates a hash based on that information.
3. The issuer encrypts the hash using the issuer's private key.
4. The resulting encrypted value or unique digital number is attached to the digital certificate.
5. The value is also stored in a database or cloud system.

Certificate verification process:

1. An employer or HR officer wants to verify the certificate.
2. The system asks for the relevant student information, such as:
   - Name.
   - Date of birth.
   - Graduation year.
   - ID information.
3. The system hashes the provided information in the same order.
4. The verifier uses the issuer's public key to decrypt the certificate's attached digital number/signature.
5. The verifier compares the newly generated hash with the decrypted hash.
6. If they match, the certificate is genuine and was issued by the claimed issuer.
7. If they do not match, either:
   - The provided information is wrong, or
   - The certificate/signature is fake or invalid.

Digital certificates can embed:

- Authenticity.
- Integrity.
- Non-repudiation.

## Certificates for Public Key Trust

Certificates solve the problem of proving that a public key belongs to a particular party.

A certificate authority (CA) certifies that a public key belongs to a named organization or person.

Example:

- Amazon has a public key.
- Amazon needs customers' browsers to trust that key.
- A CA such as GlobalSign or a large security company can certify Amazon's public key.
- The browser uses the CA's public key to verify the certificate.
- If verification succeeds, the browser trusts that the public key belongs to Amazon.

Browsers store many trusted CA certificates. Chrome, for example, has a list of trusted certificates in its settings/security area.

## Certificate Signing Request

A small business or website provider may need to pay or apply to a trusted organization to certify its public key. This process is associated with a certificate signing request.

A CA certificate-signing process includes:

1. The business provides its public key and identity information.
2. The certificate authority states that the public key belongs to that business.
3. A hash is generated over the certificate contents.
4. The CA signs the certificate by encrypting the hash or certificate data with the CA's private key.
5. The signed certificate is given to the business.

The CA has its own public/private key pair:

- The CA's private key is used to sign certificates.
- The CA's public key is known and trusted by browsers and systems.
- The CA's public key may itself be certified through higher-level trust arrangements.

## Browser Certificate Verification

When a user visits a website such as Amazon:

1. The browser receives the website certificate.
2. The browser uses the CA's public key to verify/decrypt the CA's signature.
3. The browser extracts the certificate information, including the website public key.
4. The browser generates a hash over the relevant certificate data.
5. The browser compares the generated hash with the decrypted signed hash.
6. If the hashes match, the browser trusts that the public key belongs to the website.
7. If verification fails, the browser does not trust the public key.

If a website's certificate is not recognized, not signed by a trusted CA, invalid, or expired, the browser may show a warning.

Certificates may need to be issued periodically and can have expiry dates.

## Role of Certificate Authorities

Certificate authorities provide market trust by certifying public keys.

They help answer:

- Is this public key really Amazon's public key?
- Is the customer encrypting data for the intended website?
- Has a man-in-the-middle attacker replaced the public key?

Without trusted certificates, users cannot confidently know whether a public key belongs to the claimed party.

## Cryptography Goals and Applications

Cryptographic mechanisms can support several security goals:

- Confidentiality.
- Integrity.
- Authenticity.
- Non-repudiation.

The lecture notes that availability is not directly achieved by these cryptographic methods.

Different cryptographic algorithms have different properties, such as speed and basic operations, but the focus here is on:

- Symmetric cryptography.
- Asymmetric/public-private key cryptography.
- How these support security goals in practical scenarios.

Future topics mentioned:

- Authentication based on public/private key infrastructure.
- SSL/secure layer protocols.
- How symmetric and asymmetric cryptography are combined to guarantee different security goals.
