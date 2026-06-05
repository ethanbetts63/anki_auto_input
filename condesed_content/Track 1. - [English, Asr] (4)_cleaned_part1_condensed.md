# Cyberattacks: Malware, Blended Threats, and CSRF

## Lecture Focus

This lecture covers cyberattacks. The pre-lecture recording covered:

- Software threats.
- Network attacks.

This session focuses on:

- Web attacks.
- Hardware threats.

Study objectives:

- Understand different types of cyberattacks.
- Understand how attacks happen.
- Learn strategies for defending against attacks.

## Brief History of Cyberattacks

Examples from cyberattack history:

- 1971 phone phreaking:
  - Attackers used a special high tone from a whistle to obtain free long-distance calls through telecommunication networks.
- Morris worm:
  - A well-known early worm created by a student.
  - Infected about 2,000 Unix machines within 15 hours after launch.
  - The original worm is preserved in a museum in the United States.
- Email attachment malware:
  - Malware spread through email attachments and infected many users.
- Dirty COW, Heartbleed, and Shellshock:
  - Examples of major vulnerabilities or attacks.
  - Some are connected to software flaws, scripts, or internet protocols.
  - They show why software security can be a full course and why secure coding and input sanitization matter.

## Malware

Malware means malicious software.

Popular malware types include:

- Trojan horse:
  - Malware disguised as something legitimate or useful.
  - Spyware and adware can be considered particular types related to Trojan behavior.
- Spyware:
  - Spies on user behavior.
  - May capture keystrokes.
  - May include covert payloads.
- Adware:
  - Targets advertising.
  - Tracks user behavior.
  - Supports targeted analysis and advertising.
  - Can manipulate users by showing content or products likely to interest them.
- Keylogger:
  - Specifically captures keystrokes.
  - Can steal passwords, credit card details, and other sensitive input.
- Botnet:
  - A group of computers controlled by software robots.
  - Can launch large payloads against a target.
  - Often used to overload servers.
  - A busy server may fail to respond to legitimate requests.

## Blended Threats

A blended threat combines multiple attack techniques or malware types.

### Faceworm Example

The lecture uses Faceworm as an example of a blended threat. It became popular around 2018 and still appears in social media contexts.

Attack flow:

1. A malicious link appears in a user's Facebook Messenger or social media account.
2. The link appears to come from a friend, making the user more likely to trust it.
3. The user clicks the link, often believing it is a funny video or YouTube link.
4. The user is redirected to a fake YouTube page.
5. A malicious Google Chrome extension is installed.
6. The infected device communicates with a remote command-and-control server.
7. The device downloads malicious JavaScript.
8. The malware can:
   - Launch cryptocurrency miner scripts.
   - Redirect the user to scam webpages.
   - Steal credentials.
   - Perform transactions on the user's behalf.
   - Redirect the user to other malicious programs.
9. The malware sends malicious links to the user's Facebook contacts.
10. Friends click the link and repeat the infection cycle.

Faceworm is considered a worm because it has self-propagation capability.

It is also a blended threat because it can combine:

- Worm-like propagation.
- Malicious browser extension behavior.
- Cryptocurrency mining.
- Credential theft.
- Social engineering.
- Targeted behavior based on user or contact analysis.

Two main characteristics emphasized:

- It targets cryptocurrency.
- It spreads through Facebook Messenger, a popular social media application.

### Social Engineering in Blended Threats

Social engineering is involved because:

- The malicious link appears to come from a trusted friend.
- Attacks may be targeted at users who show cryptocurrency-related behavior.
- The attacker may analyze users or their friends before deciding what payload to launch.

## Malware Evolution and Antivirus Detection

Malware continues to evolve because attackers repeatedly create, test, and modify malware.

### Malware Signatures

- Each malware type has a signature.
- A signature is an abstract representation of a specific malware type.
- Antivirus systems use signature databases to detect known malware.

### Malware Generation Cycle

Attackers or malware manufacturers may:

1. Maintain databases of malware signatures.
2. Use genetic algorithm modules to mutate signatures.
3. Apply crossover or mutation to create new malware signatures.
4. Attach code to the new signatures.
5. Generate malware samples.
6. Test those samples against major antivirus tools such as Kaspersky, McAfee, and others.
7. If antivirus software detects the malware, mutate it again.
8. If antivirus software does not detect it, launch it to the market.

This creates a cycle of malware evolution and testing.

### Antivirus Update Cycle

Antivirus companies also maintain signature databases.

- They analyze new malware found in the market.
- They extract signatures or abstract representations.
- They update their databases regularly.
- Updates may occur monthly, weekly, or daily.

Users must keep antivirus software updated because:

- New malware signatures are added over time.
- Old antivirus databases cannot detect new malware.
- Ignoring update prompts leaves computers at risk.
- Paid or reputable antivirus tools may provide stronger protection because they update databases more reliably.

## Web Attacks

Three popular web attacks are introduced:

- Cross-site request forgery, or CSRF.
- Cross-site scripting, or XSS.
- SQL injection.

This part of the transcript focuses mainly on CSRF.

## Cross-Site Request Forgery (CSRF)

CSRF occurs when a malicious site causes a user's browser to send an unwanted request to a trusted site where the user is already authenticated.

The trusted site accepts the request because it includes the user's authentication cookie.

### Bank Transaction Example

Attack flow:

1. The victim logs in to a legitimate bank site.
2. The bank gives the victim a session cookie for authentication.
3. The user remains logged in for a period, such as several minutes.
4. While still logged in, the victim visits another website or clicks a link from an email.
5. The second website is malicious.
6. The victim clicks a button, advertisement, lottery prompt, or other element.
7. Hidden HTML behind the button sends a forged request to the bank.
8. The request may instruct the bank to transfer money, such as `$1000`, to the attacker's account.
9. The request includes the victim's authentication cookie.
10. The bank believes the request came from the legitimate user and processes it.

The key issue is that the user's browser sends the authenticated request while the user is still logged in.

### Authentication Cookies

An authentication cookie may contain:

- The user's ID, likely encrypted.
- A session visiting ID, likely encrypted.
- Information that allows the site to recognize the logged-in browser.

The bank may keep the user logged in for several minutes even when inactive. CSRF exploits that active session window.

### Social Media Account Example

CSRF can also target social media accounts.

Attack flow:

1. The victim is logged in to a social media account such as Facebook.
2. The social media site keeps a session cookie and recognizes the browser.
3. The victim clicks a malicious link or visits a malicious website.
4. The malicious page contains a button or script.
5. Hidden HTML sends a forged request to the social media site.
6. The forged request changes the victim's email address to the attacker's email address.
7. The social media site believes the request came from the victim because the browser includes the session cookie.

This can lead to account takeover because future authentication codes may be sent to the attacker's email address instead of the victim's.
