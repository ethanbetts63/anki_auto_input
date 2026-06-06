##### CIA: confidentiality, integrity, availability. (expanded: authenticity, non-repudiation.)

## Asset Inventory - list hardware, software, applications, customer data.

## Valuable Assets - IP, trade secrets, payment data, PII.

## PII - personally identifiable information (eg name, license)

## Threat Identification - depends on knowing protected assets.

## Known Threat - recognized signature/characteristics; detectable.

## Unknown Threat - new/zero-day; not yet detected by AV.

## APT - long-term effort to gather information, compromise systems, and cause severe damage.

## Vulnerability Examples - outdated firmware, unlocked computer, careless password habits.

## Exploit - using a vulnerability to compromise/harm an asset.

## Risk Formula - `Risk = Probability x Impact`.

## Safeguards - security officer identifies protections for assets against threats.

## MAO Mapping - motivation = threat actors; ability = exploits; opportunity = vulnerabilities. all 3 true=cybercrime.

## Learning Focus - crypto as technical countermeasure; confidentiality primary; other goals need combinations.

## Secret Online Message - confidentiality.

## Clean Software - integrity: prove no malicious modification.

## Banking MITM - integrity; often also authenticity and non-repudiation for transactions.

## Certificate Check - authenticity plus integrity.

## E-Signed Document - authenticity plus non-repudiation.

## Security Services - symmetric gives confidentiality; asymmetric gives confidentiality/authenticity/non-repudiation; integrity needs hashes.


# Malware and Software Threats

## Software Threats:

## Worm - standalone malware; spreads automatically after initial execution.

## Virus - attached to executable file.

## Worm vs Virus - worm self-spreads; virus needs host/user action.

## Malware - malicious software; bad code hidden in/with good code.

## Rootkit - hides malware, files, programs, network connections, or compromise signs.

## Macro Virus - macro-language malware in apps like Word.

## Macro Defense - enable macros only from trusted sources; use "Disable all macros with notification" or stricter.

## Word Macro Path - `File > Options > Trust Center > Trust Center Settings > Macro Settings`.

## File-Infecting Virus - infects executables such as `.exe`, `.com`, `.dll`.

## File-Infecting Behavior - runs with host executable, replicates, infects more executables.

## File-Infecting Non-Targets - does not directly infect `.doc`, `.xls`, `.jpg`, `.png`, `.txt`.

## Boot-Sector/Master-Record Virus - executes during boot before OS loads.

## Trojan Backdoor - hidden condition/password grants attacker later access.

##### Spyware (/trojan) - monitors behavior, keystrokes, and sensitive activity.

## Software Inspection Problem - users usually cannot inspect closed-source app code.

## Antivirus Need - helps inspect/detect what users cannot manually verify.

## Ransomware - encrypts victim files and demands ransom, often cryptocurrency.

## Trojan Horse - disguised as legitimate/useful software.

## Adware - tracks users for targeted ads/manipulation.

## Keylogger - records keystrokes to steal passwords/cards/data.

## Botnet - remotely controlled computers used for large payloads/server overload.

## Blended Threat - combines multiple attack methods or malware types.

## Faceworm - Facebook Messenger worm using fake video links and malicious Chrome extensions.

## Faceworm Flow - trusted contact link -> fake YouTube -> extension -> C2 -> JavaScript payload -> spreads to contacts.

## Faceworm Payloads - crypto mining, scam redirects, credential theft, transactions, more malware.

## Faceworm Traits - self-propagating worm plus social engineering, mining, credential theft, targeted behavior.

## Malware Signatures - abstract malware identifiers used by antivirus detection.

## Malware Evolution - attackers mutate signatures/code, test against antivirus, launch if undetected.

## Antivirus Updates - vendors extract new signatures and update databases; users must keep AV current.

## Attack Prevention - clean software, reputable/updated AV, hash/signature checks, safe email/router practices.

## Malware Hash Checking - analysis sites show whether AV engines detect a sample.


# Web Attacks

## Web Attacks - CSRF, XSS, SQL injection.

## CSRF - malicious site makes authenticated browser send unwanted request to trusted site.

## CSRF Bank Example - logged-in victim clicks malicious page; hidden request transfers money using session cookie.

## Auth Cookies - encrypted user/session identifiers let sites recognize logged-in browsers.

## CSRF Social Media Example - forged request changes account email to attacker email, enabling takeover.

## CSRF Account Takeover - changed email sends auth codes to attacker; attacker can steal account/data.

## CSRF Shopping - active session cookie lets attacker trigger purchases/actions on Amazon/eBay-style sites.

## CSRF Defense Habits - log out, avoid suspicious links.

## CSRF Dependency - needs active authenticated browser session.

## XSS - attacker injects malicious script into trusted site; victim executes it in browser.

## XSS Bank Example - injected script steals cookie; attacker impersonates victim and changes/transfers funds.

## XSS Limit - logging out alone cannot prevent it because trusted site is vulnerable.

## CSRF vs XSS - CSRF exploits site trust in user; XSS exploits user trust in site.

## SQL Injection - attacker-controlled input changes SQL query behavior.

## SQL example  - `WHERE` filters records; `--` comments out remaining query text.

## SQLi Defenses - parameterized queries, prepared statements, input sanitization, avoid string concatenation.

## Controlled Inputs - dropdown/fixed choices reduce logic-changing characters like quotes, `--`, `OR`.

## Hardware Threats - environmental, technical, and human-caused threats.

## IoT/BYOD/Cloud Risks - unmanaged devices and cloud use expand attack surfaces.

## BYOD Example - infected personal laptop can spread on university subnet.

## Packet Sniffing - ISPs, governments, advertisers, attackers, admins.

##### Wireshark - packet capture/analysis tool.

## Malicious Sniffing - steals emails, files, and sensitive traffic.

## Packet Spoofing - creates packets with false identity/source IP.

## Spoofing Types - ARP, IP, email, DNS spoofing.

## DNS Spoofing - legitimate URL resolves to attacker/false destination.

## TCP/IP Attacks - attacks against protocol suite enabling modern networking.

## DoS/DDoS.

## Spoofed DoS Flow - attacker spoofs victim IP; receivers reply to victim; victim overloaded.

## Bots - compromised computers controlled for distributed attacks.

## ICMP DoS - spoofed ICMP request/reply amplification example.

## Transport Segmentation - long messages split into numbered segments for ordering/reassembly.

## TCP - Transmission Control Protocol (SYN, SYN-ACK, ACK); connection setup before data.

## UDP - User Datagram Protocol; connectionless sending.

## SYN Flood (D/DOS) - many incomplete TCP handshakes..

## Direct SYN Flood - attacker sends SYNs; server waits for missing ACKs.

## Direct Defense - filter attacker IP if identifiable.

## Spoofed SYN Flood - fake source IPs make filtering one address ineffective.

## Completed-Handshake Attack - attacker completes handshake but sends no data.

## FIN Attack - attacker sends FIN early to close legitimate connection.

## Reset Attack - attacker sends reset; server discards messages and waits for restart.

## DNS Uses UDP.

## DNS Cache Poisoning - fake DNS entry sends clients to fake site.

## DNS Spoofing DDoS - queries spoof victim IP; DNS responses overload victim.

## Mitigations - firewalls, IDS, IPS, secure protocols on top of TCP/UDP.

##### Classical Crypto - based on transposition (rearrange) and substitution (replace) for secret messages.

## Shift Substitution - shift letters by fixed key; receiver shifts back.

## Caesar Cipher - fixed-position letter shift.

## Variable Shift Key - key like `0351` shifts each position differently, then repeats/reverses.

## Breaking Classical Crypto - analyze preserved ciphertext patterns.

## Frequency Analysis - compare ciphertext letter frequencies to normal language frequencies.

## English Frequency Clues - `E`, `T`, `A` common; `Z` rare.

## Monoalphabetic Substitution - each plaintext symbol always maps to same ciphertext symbol.

## Polyalphabetic Substitution - frequency analysis alone insufficient; needs other clues.

## Decryption Process - count frequencies (hard on small text), guess mappings (common pairs/triples: `THE`), substitute.

##### Modern Cryptography - prevents eavesdropping.

## XOR Encryption - `M XOR K = C`.

## XOR Decryption - `C XOR K = M`.

## XOR Reason - `(M XOR K) XOR K = M XOR (K XOR K) = M`.

## Ideal Key - random, uncrackable, plaintext-length, one-time use but randomness and secure key sharing are impractical.

## Symmetric Encryption:

## ECB (block cipher)- split message into key-sized blocks; pad last block. Parallel encryption/decryption; very fast but repeated plaintext blocks produce repeated ciphertext blocks. (image pattern example)

##### Replay Attack. unique IDs/timestamps plus MAC to stop.

## CBC - each block depends on previous ciphertext; repeated plaintext patterns are hidden.

## Initialization Vector - IV starts first block; different IV changes ciphertext; receiver needs same IV.

## CBC Encryption - `P1 XOR IV -> encrypt = C1`; `Pi XOR C(i-1) -> encrypt = Ci`.

## CBC Speed - encryption is serial and slower than ECB.

##### CBC Example - 2-bit blocks with IV `10`; each ciphertext feeds the next plaintext block.
##### CBC Example - ciphertext `11` reverses to `10`; `10 XOR IV 10 = plaintext 00`.

## CBC Decryption Intro - reverse cipher table plus same IV recovers plaintext.

## CBC Decryption - decrypt `Ci`, then XOR IV for first block or `C(i-1)` for later blocks.

## Parallel Decryption - each block uses available ciphertext blocks; encryption serial, decryption parallel.

## Symmetric Key / IV - sender and receiver share same secret key; CBC receiver also needs IV.

## Leaked Key - disclosed symmetric key breaks confidentiality.

## IV Changes - different IV changes ciphertext for same message and helps against repeats/replay.

## Other Modes - output feedback and others trade speed and security differently.

## Simple Bitwise Limits - single XOR, short keys, or disclosed key/IV are unsafe.

## DES - 64-bit blocks, 32/32 split, permutation/XOR/swaps, 16 rounds; cracked.

## Triple DES - DES applied three times; 48 rounds; safer than DES, very slow, still risky.

## AES - faster and stronger than Triple DES; variable key sizes; choose AES when available.

## Standards Comparison - DES cracked; 3DES slow; AES fast, strong, widely used; all symmetric.

## Symmetric Applications - secure internet, files, server data, banking, payments, protocols.

## Why Symmetric Is Fast - bitwise calculations remain faster than asymmetric exponential math.

## Symmetric Goals - confidentiality only by itself; integrity/authenticity/non-repudiation need other mechanisms.

## Key Exchange Problem - secret key must be shared securely; CBC IV must match.

##### Key Exhaustion - pairwise keys grow as `n x (n - 1) / 2`.
##### Symmetric Conferencing Problem - pairwise keys required: `n x (n - 1) / 2`.

## Key Count Examples - 2 parties need 1 key; 3 need 3; 4 need 6; 5 need 10.

##### E-Commerce Scalability - millions of customers would require millions of symmetric keys.
##### Symmetric E-Commerce Problem - one secret key per customer does not scale to millions.

## KDC Problem - trusted center can generate/distribute keys but may read all conversations.

## Motivation for Asymmetric Crypto - scalable key model; different encryption/decryption keys; supports auth/integrity/non-repudiation with hashes.


# Asymmetric Cryptography / RSA / Diffie-Hellman

## RSA - public-key cryptography for secure transmission, signatures, key exchange.

## RSA Security - hard to factor large `n = p * q`.

## Key Generation - choose primes `p`, `q`.

## Calculate n - `n = p * q`; example `2 * 7 = 14`.

## Calculate v - `v = (p - 1) * (q - 1)`; example `6`.

## Choose e - odd, prime to `v`, example `6 mod 5 = 1`, so `e = 5`.

## Public Key - `(e, n)`; example `(5, 14)`.

## Choose d - `d * e mod v = 1`; example `11 * 5 mod 6 = 1`, so `d = 11`.

## Private Key - `(d, n)`; example `(11, 14)`.

## Small RSA Weakness - small `n` is easy to factor, exposing `p`, `q`, `v`, and `d`.

## Real RSA Security - large primes make factoring `n` infeasible.

## Size Example - `2^1000 approx 10^300`; huge factorization problem.

## Legitimate User - knows `p`, `q`; derives `n` and private `d`.

## Attacker - knows `n` but cannot feasibly recover large `p`, `q`, or `d`.

## Encryption Formula - `ciphertext = message^e mod n`; example `2^5 mod 14 = 4`.

## Decryption Formula - `message = ciphertext^d mod n`; example `4^11 mod 14 = 2`.

## Diffie-Hellman - shared secret over public channel without prior shared secret/third party.

## Process - agree public parameters, choose private keys, compute/exchange public keys, compute shared secret.

## Example Public Parameters - `g = 7`, `p = 23`.

## Example Private Keys - Alice `3`, Bob `6`.

## Alice Public Key - `7^3 mod 23 = 21`.

## Bob Public Key - `7^6 mod 23 = 4`.

## Alice Shared Secret - Bob public key with Alice private: `4^3 mod 23 = 18`.

## Bob Shared Secret - Alice public key with Bob private: `21^6 mod 23 = 18`.

## Shared Secret - both compute `18`.

## Attacker Sees public keys, but lacks private exponents. Hard to derive private exponent from `A = g^x mod p`.

## Applications - SSL, TLS, VPNs, secure messaging.

## Lecture Context - RSA/Diffie-Hellman applications; public/private key pair; different encryption/decryption keys.

## Goals - asymmetric crypto supports confidentiality, authenticity, non-repudiation, and integrity with hashes.

## Combining Algorithms - symmetric ciphers plus hashes/signatures combine confidentiality with integrity/authenticity.

## Symmetric Authentication Problem - shared key with the wrong party defeats secrecy; receiver identity must be trusted.

## RSA Confidentiality - encrypt with receiver public key; decrypt with receiver private key.

##### Amazon Credit Card Example - customers encrypt with Amazon public key; only Amazon private key decrypts.
##### Online Purchase Confidentiality - Amazon publishes public key; customers encrypt; only Amazon private key decrypts.

## Confidentiality Caveat - sender must have the receiver's real public key.

## RSA Authenticity - sign/encrypt with sender private key; verify/decrypt with sender public key.

## Amazon Authenticity Example - Amazon signs with private key; customer verifies with Amazon public key.

## Asymmetric vs Symmetric Purchase Keys - one Amazon key pair replaces per-customer symmetric key distribution/storage.

## Public-Key Authenticity Problem - MITM can swap Amazon public key; customer encrypts to attacker.

## Classroom Public Keys - trusted name-to-public-key list lets students verify lecturer-signed announcements.

## Signature Text - private-key-created text verified by the matching public key.

## Public-Key Trust Assumption - first public-key exchange can be replaced; needs a trust mechanism.

## Why Public Keys Scale - public key can be shared openly; private key stays secret; avoids many symmetric secrets.

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

## Future Topics - PKI authentication, SSL/TLS, and symmetric/asymmetric combinations.

# Hashing

## Hash Output - hash value/code/digital fingerprint, often hexadecimal must be Deterministic, Fixed Length, Pre-Image resistance, Collision Resistance, Avalanche Effect

## Hash Uses - integrity, tamper detection, unauthorized-access protection.

## Hash Combinations - combine with RSA/DH for integrity/authentication.

## MD5 - early 128-bit hash; command example `md5sum`.

## MD5 Internals - 64 operations using 32-bit values, message blocks, constants, shifts, modular addition.

## MD5 Caveat - collision resistance broken.

## SHA Family - SHA-1, SHA-2, SHA-3.

## SHA-1 - collision resistance weakened.

## SHA-2 - stronger than MD5/SHA-1.

## SHA-3 - newer SHA standard; released 2015.

## MD5 vs SHA - MD5 faster/smaller/weaker; SHA longer/more secure.

## SSH - secure remote connection over unsecured networks.

## SSH Protects - encryption against eavesdropping, leakage, tampering.

## SSH Uses - remote login, server management, file transfer, commands.

## SSH Auth Types - password-based and public-key authentication.

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

## AAA - authentication, authorization, accountability.

## Identification - subject claims identity.

## Authentication - verifies claimed identity; one-way or two-way.

## Authorization / Access Control - grants permissions/resources after authentication.

## Accountability - logs actions such as login time, duration, transactions; costs storage/resources.

## Auth Flow - initiation, challenge, proof, validation, decision.

## Auth Zones - client secrets, transmission interception, server credential storage.

## Auth Factors - know: password; have: certificate/OTP/token; are: biometric.

##### Password Auth - cheap/familiar/interoperable but weak alone and vulnerable in all zones.

## Client-Zone Attacks - local exposure, brute force, phishing.

## Transmission-Zone Attacks - sniffing/interception.

## Server-Zone Attacks - insider access, compromise, dictionary attacks.

## Password Managers - encrypted storage for many passwords.

## Plain Passwords - never store/send; leak via insiders, compromise, sniffing.

## Encrypted Password Issues - stolen key exposes data; same passwords/lengths may leak.

## Password Hashing - fixed-length, deterministic, one-way, no key; store/compare hashes.

## Hash Reset Caveat - original password cannot be recovered; reset instead.

##### Rainbow Table - precomputed password-hash lookup; cracks weak/common hashes.

## Password Rule - long, complex, uncommon passwords.

## Salting Password Hashes - random value added before hashing; stored with hash; not secret.

## Linux Shadow Salt Format - fields show hash type, salt, and salted hash; `$6$` indicates SHA-512-style password hashing.

## Why Salting Helps - same password plus different salts creates different hashes; hides password equality.

## Salting vs Rainbow Tables - attacker must precompute every password times every salt; 12-bit salt multiplies table by `2^12`.

## Salting Limits - hardens precomputation/equality attacks; does not stop brute force or replay.

## Brute Force - attacker guesses directly; salt cannot help once the correct password is guessed.

## Brute Force Difficulty - depends on password space, guess rate, length, and complexity.

## Replay / Pass-the-Hash - captured salted hash can be reused if server accepts it as proof.

##### Replay Defenses - MFA codes, timestamps, freshness checks, stale-request rejection.

## Password Stretching / Hash Chains - hash many times before storage; bcrypt-style systems slow each guess.

## Stretching Effect - more iterations reduce guesses per second and make cracking harder.

## Password Entropy - more possible combinations means longer cracking time.

## Length vs Complexity - combinations equal character-set size to password length; best is long and complex.

## Usable Strong Passwords - use memorable modified phrases; avoid under 15 characters; over 20 is better.

## Other Factors - authentication can use what you know, have, or are.

## What You Have - OTP devices, bank code devices, certificates; stronger but costly and stealable.

## What You Are - fingerprints, eye scans, face recognition, behavioral analysis; needs sensors/processing.

## Biometric Errors - false negative rejects legitimate users; false positive accepts illegitimate users.

## MFA - combines factors to reduce password-only risks: brute force, rainbow tables, replay, phishing, leakage.

## Password Auth Summary - plaintext bad; encryption has key/ciphertext issues; hashes face rainbow tables; salts harden rainbow attacks; stretching slows brute force; MFA adds proof.

## Passwordless / Public-Key Auth - RSA public/private-key protocols reduce dependence on passwords.

##### DAC - owners/privileged users set permissions; traditional Unix/Linux.

##### MAC - central authority enforces predefined policy. stronger security but complex + high admin overhead.

## RBAC - permissions assigned to roles; users assigned to roles. simpler management than per-user permissions. (CEO all resources; accountant financial database.)

## ABAC (rule based)- access based on user/resource/environment (send email only if size under 5 MB).

## RBAC Attribute Growth - adding attributes multiplies roles/permissions.

## ABAC Attribute Growth - add rules while preserving existing rules.

# Access Control in Operating Systems

## OS Access Models - DAC, MAC, RBAC, rule/attribute-based access.

## Subjects / Objects - subjects: users/commands/programs; objects: files/pipes/sockets/resources.

## Permissions - read, write, execute for owner/group/others; `777` = full access for all.

## DAC Risk - root can grant dangerous broad permissions like `chmod 777`.

## Malware Privilege - malware inherits current user privilege; admin/root login increases damage.

##### Shadow File Dilemma - users need password changes but cannot directly edit protected password file.

## Two-Tier Approach - user calls privileged program that performs only restricted action.

##### SetUID - program runs with owner privilege, not launcher privilege.

##### passwd - root-owned SetUID program updates only user's password field.

##### RUID / EUID - RUID = launcher; EUID = identity used for permissions.

##### SetUID RUID/EUID - RUID stays normal user; EUID becomes program owner.

##### SetUID Display - `s` in owner execute position.

##### SetUID Numeric - normal `0755`; SetUID `4755`; leading `4` = SetUID bit.

## Delegation vs Service - SetUID grants temporary program privilege; daemon service performs privileged tasks.

##### SetUID - program runs with owner privilege, not launcher privilege. `4755`; leading `4`; owner execute shows `s`; runs with owner/root EUID.

## Purpose - controlled privilege escalation for specific protected operations.

## Linux Ownership - user owner and group owner.

## Permission Categories - owner, group, other.

## Permission Types - read `r`, write `w`, execute `x`.

## File Permissions - `r` read; `w` modify; `x` execute.

## Permission Triplets - example `rwxr-x---`: owner full, group read/execute, others none.

## Full Permissions - `rwxrwxrwx`.

## Directory Permissions - `r` list; `w` create/remove; `x` enter/access.

## Listing Format - first character file type; then owner/group/other triplets.

##### SetUID Bit Display - owner execute becomes `s`, e.g. `rws`.

##### RUID / EUID - RUID = launcher; EUID = identity used for permissions.

## Normal Execution - RUID = EUID = runner.

##### SetUID RUID/EUID - RUID stays normal user; EUID becomes program owner.

## Root-Owned SetUID - program temporarily runs with root privilege.

##### passwd - root-owned SetUID program updates only user's password field.

##### Shadow File Dilemma - users need password changes but cannot directly edit protected password file.

## SetUID passwd Flow - normal user runs `passwd`; EUID root writes shadow file.

## Enable SetUID Step 1 - change owner to root with `chown`.

## Enable SetUID Step 2 - turn on SetUID bit with `chmod 4755`.

## Numeric Permissions - `rwx = 111 = 7`; `r-x = 101 = 5`; `rwxr-xr-x = 755`.

##### Special Leading Digit - `0` normal; `4` SetUID.
##### `4755` - SetUID enabled plus `755` normal permissions.
##### SetUID Numeric - normal `0755`; SetUID `4755`; leading `4` = SetUID bit.

## Disable SetUID - `chmod 0755`.

## Security Risk - elevated privileges make SetUID dangerous if poorly managed.

## Takeaway - useful for narrow privilege delegation, but use carefully and only when necessary.

# SetUID, SetGID, Sticky Bit, and Access-Control Vulnerabilities

## SetGID - `2755`; leading `2`; group execute shows `s`; runs with file group or inherits directory group.

## Sticky Bit - `1755`; leading `1`; other execute shows `t`; shared dirs like `/tmp`.

## Sticky Bit Purpose - users can create files but not delete/modify others' files.

## Special Bits - SetUID owner privilege; SetGID group privilege/inheritance; sticky restricts deletion.

## SetUID Principle - privilege goes to program, not user; user can only do program-coded actions.

## SetUID Safety - safer than broad root only when program is tightly constrained.

## Bad SetUID Design - flawed logic/environment assumptions expose protected files/actions.

## Root SetUID Editors - `vi`, `nano`, `pico` should not be SetUID root; can edit protected files.

## Race Condition - timing bug where check/update order changes outcome.

## Race Example - two withdrawals accepted before balance update.

## Privileged Race Risk - exploit before privilege is dropped.

## Dirty COW - 2016 copy-on-write race exploit modifying protected read-only files.

## Accountability - logs show what happened and where.

## Access-Control Risk - misconfigured permissions, flawed privileged programs, race conditions.

## TCP/IP.

## Segmentation - divide large data into smaller pieces.

## Encapsulation - add source, destination, protocol, and handling information as data moves through layers.

## Package Analogy - split large item, label packages, deliver through transport links.

## Multiplexing - combine multiple data streams into shared transport capacity.

## Delivery - protocols read destination info and coordinate across layers.

## TCP/IP Security Problem - designed for connectivity/reliability, not security.

## Identity Weakness - IP addresses are not strongly tied to real identities.

## Attack Tool Availability - free tools and Internet scale increase risk.

## Open Systems Security Architecture - later framework for security services/mechanisms.

# Network Security: Physical and Data Link Layers

## TCP/IP Layers - physical, data link, network, transport, application.

## Layer Security - handle problems/countermeasures layer by layer.

## Physical Security - shielding, physical separation, redundancy, service/security controls.

## Link Shielding - protects cables from leakage, interference, tapping.

## Shielded Cable - conductor, dielectric, foil, braid, outer rubber.

## Shielded Rooms - reduce wireless/electromagnetic leakage.

## Physical Separation - no direct connection between Internet and intranet.

## Internet / Intranet - external network vs internal/private network.

## Air Gap / Separation Switch - physically separates networks.

## Firewall vs Separation - firewall keeps connection with controls; separation prioritizes no direct connection.

## Separation Use Cases - e-government, stock trading, high-confidentiality systems.

## E-Government Flow - external/internal data moves through checked storage, never direct network link.

## Data Link Security - link encryption, WLAN/SSID, WEP/WPA, spoofing, ARP/MAC, anti-sniffing.

## Link-Layer Encryption - encrypts whole frame including headers/trailers.

## Link-Layer Weakness - switches may decrypt/re-encrypt and see plaintext.

## End-to-End Encryption - encrypts content before lower-layer headers; devices route but cannot read body.

## Layered Encryption - app encryption protects content even if link layer is decrypted.

## WLAN / SSID - wireless LAN; SSID = Wi-Fi name up to 32 chars.

## Hidden SSID - weak protection; devices may still reveal/reconnect.

## Default SSID/Password - change both; defaults may reveal model or be known online.

## Wi-Fi Key Length - 13+ characters minimum; 20+ better.

## Wireless Security - avoid open networks; use strongest available encryption.

# Link-Layer and Network-Layer Security

## Router Security - use WPA2 Personal and AES; avoid WEP, DES, 3DES.

## Public Wi-Fi - risky because users do not control hotspot.

## Public Wi-Fi Defenses - firewall on, discovery/sharing off, verify SSID, prefer HTTPS/VPN.

## Wireless Hygiene - disable unused Wi-Fi, Bluetooth, NFC; keep AV/security tools updated.

## MAC Address - physical local-delivery address.

## ARP - maps IP addresses to MAC addresses; ARP table stores mappings.

## ARP Risk - devices can lie, redirect, or block traffic.

## ARP Mitigation - correct/static ARP records or improved ARP.

## Sniffing - capture/analyze traffic; used for troubleshooting or data theft.

## Network Layer - routes using IP addresses.

## Routing Attacks - DoS, route poisoning, table flooding, routing-path spoofing, QoS-path spoofing.

## QoS - Quality of Service.

## IP Vulnerability - weak proof of IP ownership/use.

## IP Conflict Attack - duplicate IP disrupts communication or router behavior.

## DHCP Fake Release - false release frees in-use IP and causes duplicate-IP conflict.

## ICMP - checks if host is alive/online.

## Smurf Attack - spoof victim IP in ICMP requests; replies flood victim.

## Network Defenses - IPv6, IPsec, disable ICMP where appropriate, IP filtering, NAT.

## IP Filtering - firewalls/IDS/IPS block bad IPs.

## NAT - hides internal IPs through address translation.

## Takeaway - WPA2/AES, cautious public Wi-Fi, ARP awareness, anti-sniffing, routing/IP/ICMP defenses.


# IDS, IPS, and Firewalls

## IDS/IPS - tools for malicious activity detection/prevention.

## IDS - passive monitor of network/system activity; logs and alerts.

## IDS Looks For - malicious behavior and policy violations.

## IPS - active detection plus real-time blocking/prevention.

## IPS Actions - drop packets, block attacks, quarantine systems.

## IDS vs IPS - IDS reports; IPS intervenes and needs stricter configuration.

## IDS Types - host-based and network-based.

## Host-Based IDS - installed on local devices for host protection.

## Network-Based IDS - monitors traffic before/after firewall or beside switch on replicated traffic.

## IDS Placement - helps evaluate firewall behavior and rule quality.

## Honeypot - isolated decoy system used to lure attackers and study attacks.

## Honeypot Use - extract anomaly signatures for IDS/IPS.

## IPS Types - host-based and network-based.

## Network IPS Placement - must sit inline in traffic path to block packets.

## Firewall - hardware/software barrier controlling traffic.

## Firewall Purpose - allow/block traffic, log activity, enhance security.

## Default Deny - allow specified traffic; block everything else.

## Firewall Benefits - security, traffic control, logs, threat barrier.

## Firewall Caveats - slower traffic, blocked legitimate traffic, complex config, false positives.

## Firewall Techniques - packet filtering, proxy firewall, stateful inspection.

## Packet Filtering - allow/block by rule such as suspicious IP address.

## Stateful Inspection - decide using traffic state/history.

## Proxy Firewall - single external contact point; hides internal IPs and evaluates requests.

## Proxy SYN Defense - only completed handshakes pass, reducing SYN flood impact.

## Combined Security - firewalls, IDS, IPS can work together but require cost/time/configuration.

## Human Error - wrong recipient, no BCC, careless sensitive-data handling.

## Awareness Training - reduces human cyber risk.

##### Social Engineering - psychological deception to make people click, disclose, grant access.

## Phishing.

## Spear Phishing - targeted at specific people/roles.

## Whaling - targeted at executives/high-value users.

## Smishing / Vishing - SMS phishing / voice-call phishing.

## Phishing Indicators - generic greeting, odd sender, mismatched hover link, fake URL, bad grammar, urgency, missing contacts, spoofed branding.

## Watering Hole - compromise trusted site used by target group.

## Watering Hole Defense - secure websites, limit oversharing, avoid personal social media on work devices.

## Tailgating - unauthorized person follows unnoticed.

## Piggybacking - authorized person knowingly allows entry.

## Mantrap - two-door access control stopping unauthorized following.

## Shimming - payment-terminal/card attack stealing money/card data.

## Impersonation - pretending to be inspector, pentester, employee, contractor, provider, etc.

## Dumpster Diving - collecting discarded info: IPs, invoices, processes, vendors, suppliers.

## Shoulder Surfing - observing passwords, PINs, codes, sensitive info.

## USB Dropping - malicious USB left for victim; never plug in unknown USBs.

## Hoaxing - fake warnings/messages spreading misinformation.

## Persuasion Principles - reciprocity, commitment/consistency, social proof, liking, authority, scarcity.

## Phishing Persuasion - authority, rewards/community, urgency/scarcity drive unsafe clicks.

# Persuasion, Mobile Awareness, URL Hijacking, and Security Awareness

## Security Persuasion - social proof and commitment/consistency encourage secure behavior.

## AUP - acceptable use policy for email, passwords, online behavior, security practices, risks.

## Mobile Attack Surface - NFC, Bluetooth, Wi-Fi, SIM, storage cards, sensors.

## NFC - Near Field Communication; tap-to-pay; not Bluetooth/Wi-Fi.

## Permission Timing - install-time permissions persist; runtime permissions request when needed.

## Network Permission - internet access can exfiltrate data.

## Personal Info Permission - contacts plus internet can exfiltrate contacts.

## SMS Permission - can read verification codes; avoid unless necessary.

## Location Permission - grant only when needed; avoid constant access.

## URL Hijacking - lookalike domains via typos, extensions, hyphens, spelling changes, brand imitation.

## URL Hijacking Names - direct linking, cybersquatting, typosquatting, fake URL, brandjacking.

## URL Defenses - use trusted sites, verify URLs, search official site, avoid suspicious links.

## Separate Browsing - use separate computer/VLAN for casual browsing where possible.

## VLAN - virtual LAN limiting malware spread between segments.

## Defensive Domain Registration - register typo versions of domains.

## Email/Web Attack Causes - no AUP, no training, no buy-in, poor link/site awareness, weak endpoint protection.

## Awareness Plan - enforce AUP, train phishing/social engineering, build buy-in, improve endpoint/BYOD controls.

## Endpoint Protection - keep AV and anti-spam updated.
