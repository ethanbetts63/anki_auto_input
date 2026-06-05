# Salting, Password Stretching, and Multi-Factor Authentication

## Rainbow Tables and Simple Passwords

Rainbow tables contain precomputed mappings between plaintext password combinations and their hash outputs.

They can be used to crack passwords when an attacker obtains a password hash:

- The attacker compares the stolen hash with hashes in the table.
- If a match exists, the attacker looks up the corresponding plaintext password.

Simple passwords are more likely to appear in free or purchased rainbow tables. Users should choose passwords that are long, complex, and unlikely to be included in such tables.

The workshop activity mentioned in the transcript includes trying rainbow-table-based password cracking through available online mapping tables.

## Salting Password Hashes

Salting is a system technique used to make rainbow table attacks harder.

A salt is:

- A randomly generated value.
- Added to the password before hashing.
- Stored with or alongside the password hash.
- Not necessarily kept secret.

The transcript refers to salts as random bits or digits. The salt length depends on system design.

Example:

- A system might use 12 random bits.
- It could also use 6 digits, 20 digits, or another length depending on the design.

## Salt Representation in Linux Shadow Files

The transcript notes that salt information can be visible in a Linux shadow file.

Example structure discussed:

- A leading number such as `6` can indicate the hash function type.
- The transcript states that `6` corresponds to a 512 password hash.
- Dollar signs separate fields.
- One field contains the salt.
- Another field contains the salted password hash.

The key point is that salts are often stored openly with the hash. Their purpose is not secrecy but making precomputation much harder.

## Why Salting Helps

Without a salt:

- The same password always produces the same hash.
- If Alice and Bob use the same password, their hashes will be the same.
- An attacker can infer that both users have the same password.
- A rainbow table can map each candidate password to one hash result.

With a salt:

- The same password can produce different hashes for different users.
- Alice and Bob can use the same password but still have different stored hash values.
- Observing two different hashes does not reveal whether the original passwords are the same.

Salting fixes the equality problem of simple unsalted password hashes.

## Salting and Rainbow Table Size

Salting makes precomputed rainbow tables much larger.

Without salting:

- Each candidate password maps to one hash.
- A rainbow table stores one result per password candidate.

With salting:

- Each candidate password must be combined with every possible salt value.
- Each password may have many possible salted hash outputs.

Example from the transcript:

- If a 12-bit salt is used, there are `2^12` possible salt values.
- For a single password such as `111`, the attacker would need `2^12` hash results, one for each possible salt.
- For another password such as `112`, the attacker again needs `2^12` hash results.
- The rainbow table becomes `2^12` times larger than the original unsalted table.

The larger table makes:

- Precomputation harder.
- Storage requirements much larger.
- Matching and reverse lookup slower.

The transcript mentions the `rockyou.txt` list as a common freely available password list/rainbow-table-related resource, with a size around 133 MB. If salts are included, the precomputed data would need to multiply by the number of possible salts, making it much larger.

## Limits of Salting

Salting does not solve every password attack.

Salting makes precomputation attacks harder, but:

- It does not increase the computational difficulty of cracking one specific password if the attacker can test guesses.
- It does not stop brute force guessing.
- It does not prevent replay attacks.

## Salting Does Not Stop Brute Force Attacks

In a brute force attack, the attacker tries password combinations directly.

If the attacker guesses the correct password:

- The correct password can still pass authentication.
- The presence of a salt does not matter once the correct password is guessed.

The difficulty of brute forcing one password depends mainly on:

- How many possible password combinations exist.
- How quickly the attacker can test guesses.
- How long and complex the password is.

Salting mainly affects precomputed table attacks, not direct guessing of one password.

## Salting Does Not Stop Replay Attacks

A replay attack occurs when an attacker captures valid authentication data and reuses it.

Pass-the-hash example:

- An attacker in the transmission zone steals the whole password hash or salted hash.
- The attacker sends that same hash to the system later.
- If the system accepts the hash as reusable proof, the attacker can get through.

Salting does not fix this by itself because the captured hash can still be replayed.

Defenses against replay attacks can include:

- A second factor, such as a six-digit one-time code.
- A timestamp attached to the hash or request.
- Server checks that reject stale or mismatched timestamps.

The transcript emphasizes that salting alone does not prevent replay attacks.

## Password Stretching / Hash Chains

Password stretching, also called a hash chain technique in the transcript, is used to make brute force attacks slower.

Instead of storing a single hash, the server applies the hash function multiple times.

Example:

- For password `111`, the system hashes it 10 times and stores the final result.
- When testing a guess such as `112`, the attacker also must hash it 10 times before comparing.
- For every guessed password, the attacker must repeat the multi-hash process.

Because hashing many times takes more computation:

- Guessing speed decreases.
- Brute force attacks become slower.
- Large-scale cracking becomes harder.

The transcript mentions protocols/names such as bcrypt as examples based on this type of technique.

## Effect of Stretching on Guessing Speed

A single hash can be very fast.

Example contrast from the transcript:

- With a normal GPU and simple hashing, an attacker might test a very large number of guesses per second.
- With a stretching-based system such as bcrypt, the attacker may be limited to far fewer guesses per second.

The exact numbers depend on the protocol and hardware, but the principle is:

- More hash iterations per guess reduce guessing speed.
- Lower guessing speed makes brute force attacks harder.

## Password Entropy

Password strength is related to entropy: the amount of uncertainty or number of possible combinations.

Higher entropy means:

- More possible password combinations.
- Longer cracking time.
- Better resistance to guessing.

The transcript compares:

- An 8-character password with more character types.
- A 9-character password with fewer character types.

The conclusion is that longer passwords generally provide more entropy. Adding length can be more valuable than only adding complexity.

## Length Versus Complexity

Password combinations depend on:

- Number of characters in the password.
- Number of possible choices for each character.

Examples discussed:

- Uppercase and lowercase letters give 52 possible choices per character.
- Symbols and numbers add more choices.
- A longer password increases the number of total combinations.

The transcript's practical takeaway:

- Longer passwords are better.
- More complex passwords are also better.
- If possible, make passwords both long and complex.

## Creating Usable Strong Passwords

Very complicated random passwords can be hard to remember.

A practical method is to use a meaningful phrase and modify it:

- Start with a phrase that is meaningful to the user.
- Replace some words or characters with numbers or symbols.
- Use substitutions known only to the user.
- Keep the password long.

The transcript suggests:

- Avoid passwords shorter than 15 characters.
- Passwords longer than 20 characters are better when possible.

## Other Authentication Factors

Authentication does not have to depend only on passwords.

Other factors include:

- **What you have**
- **What you are**

These can be used alone in some systems or combined with passwords for stronger authentication.

## What You Have

"What you have" includes possession-based authentication factors.

Examples:

- One-time pad or one-time password device.
- Time-based one-time code device.
- Hash-result-based OTP device.
- Bank code device.
- Digital certificate.

Advantages:

- More secure than password-only authentication in many cases.

Disadvantages:

- More expensive.
- Requires extra devices or infrastructure.
- Can still be subject to theft or related risks.

## What You Are

"What you are" includes biometric or user-property-based authentication.

Examples:

- Fingerprint.
- Retina or eye scan.
- Face recognition.
- Behavioral analysis.

The transcript uses the term ergonomics for behavior analysis.

Costs and limitations:

- Requires scanners or sensors.
- CPU and memory intensive.
- The system must process and recognize biometric or behavioral data.
- Subject to classification errors.

## False Positives and False Negatives

Biometric and similar systems can make two important kinds of errors:

- **False negative:** the legitimate user is rejected by mistake.
- **False positive:** an illegitimate user is accepted by mistake.

Good system design must reduce both types of error.

Reducing these errors can require more resources and careful design.

## Multi-Factor Authentication

Multi-factor authentication combines more than one authentication factor.

Examples:

- Password plus PIN code.
- Password plus six-digit time-based code.
- Password plus face recognition.

Multi-factor authentication is used because password-only systems have many weaknesses, including:

- Brute force attacks.
- Rainbow table attacks.
- Replay/pass-the-hash attacks.
- Phishing and leakage.

## Password Authentication Summary

Authentication approaches discussed:

- **Plain password**
  - Not good.
  - Exposes passwords if stored, transmitted, or accessed.

- **Encrypted password**
  - Still problematic.
  - The key can be stolen.
  - Same passwords can produce same ciphertext.
  - Password length may leak.

- **Single hash of password**
  - Better than plaintext or encryption for storage.
  - Vulnerable to rainbow table attacks.

- **Salted password hash**
  - Makes rainbow table attacks much harder.
  - Prevents same passwords from necessarily producing same stored hashes.
  - Still vulnerable to brute force guessing.
  - Does not prevent replay attacks.

- **Stretching / multiple hashing**
  - Slows brute force attacks.
  - Requires attackers to spend more computation per guess.
  - Still does not by itself solve replay attacks.

- **Multi-factor authentication**
  - Adds extra proof beyond the password.
  - Helps address replay and password-only weaknesses.

## Passwordless and Public-Key-Based Authentication

The transcript notes that some protocols avoid passwords entirely.

One workshop protocol uses:

- Public/private key-based authentication.
- RSA concepts from the previous week's material.

There are also other authentication protocols that are not based on passwords.

The broader motivation is that the world is over-reliant on passwords, and some alliances or groups are working on alternative protocols to authenticate users without relying on passwords.
