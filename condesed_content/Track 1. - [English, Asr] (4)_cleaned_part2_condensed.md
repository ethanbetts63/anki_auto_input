# Cyberattacks: CSRF Continuation, XSS, SQL Injection, and Hardware Threats

## CSRF Account Takeover Consequences

If a CSRF attack changes the victim's social media email address to the attacker's email address:

- The victim may not receive the six-digit authentication code needed to log in.
- If two-factor or email-based verification is enabled, the code may go to the attacker's email.
- If the attacker also cracks or obtains the password, the attacker can log in as the victim.
- The attacker can steal the social media account.
- The attacker may access:
  - Friend contact lists.
  - Marketplace information.
  - Credit card information if stored.
  - Other account data.
- The attacker may perform transactions or other actions using the victim's account.

## CSRF in Online Shopping

CSRF can also affect shopping sites such as Amazon or eBay.

Example flow:

1. The user logs in to an online shopping site.
2. The user does not log out after shopping.
3. The user clicks an email link or visits another interesting site.
4. The user is redirected to an attacker's website.
5. The user browses or clicks something on that site.
6. The browser is still recognized by the shopping site because the login session cookie remains active.
7. The attacker sends a request to the shopping site.
8. The shopping site believes the request came from the user.
9. The attacker may purchase valuable products or perform transactions without the user's awareness.

## CSRF Defense Habits

CSRF is a major vulnerability type and appears frequently in vulnerability statistics.

User-side habits that reduce CSRF risk:

- Log out immediately after finishing online banking, shopping, or other sensitive sessions.
- Do not browse unrelated websites while logged in to sensitive accounts.
- Do not check suspicious emails or click links during an active banking or shopping session.
- Avoid keeping accounts logged in unnecessarily.
- Always check that URLs are legitimate.
- Avoid fake or suspicious websites.

Reasoning:

- CSRF depends on the browser still having an active authenticated session.
- If the user logs out, the forged request cannot use the active session cookie in the same way.
- Even legitimate websites can have vulnerabilities, so careless browsing can still be risky.

## Cross-Site Scripting (XSS)

XSS is a different type of web attack from CSRF.

In XSS:

- The attacker first discovers a vulnerability in a trusted website.
- The attacker injects malicious JavaScript or another malicious script into that trusted site.
- The victim visits the trusted site.
- The victim clicks a link or triggers content that executes the malicious script.
- The malicious script runs in the victim's browser.
- The script may send the victim's cookie to the attacker.
- The attacker can use the stolen session cookie or credentials to impersonate the victim.

### Bank Site XSS Example

Attack flow:

1. A bank site has a vulnerability in its webpage.
2. The attacker injects malicious JavaScript into the bank site.
3. The user trusts the bank site and visits it.
4. The user clicks a link or otherwise triggers the injected script.
5. The script steals the user's session cookie.
6. The attacker uses the stolen cookie to impersonate the victim on the bank site.
7. The attacker can:
   - Transfer funds.
   - Change account details.
   - Perform other malicious actions on the victim's behalf.

XSS cannot be prevented only by logging out after use, because the attack abuses the user's trust in the site and the site's own vulnerability.

## CSRF vs XSS

Both CSRF and XSS exploit trust, but in different directions.

### CSRF

- Exploits the trust a site has in its users.
- The trusted site believes a forged request came from the authenticated user.
- A malicious site causes the user's browser to perform unwanted actions on a trusted website.
- Example outcome:
  - Transfer money.
  - Change account email.
  - Perform unwanted account actions.

### XSS

- Exploits the trust a user has in a trusted site.
- A malicious website or attacker leverages bugs in the trusted website.
- The trusted website causes unwanted actions or script execution in the user's browser.
- Example outcome:
  - Steal cookies.
  - Steal credentials.
  - Impersonate the user.
  - Transfer money or change account details.

## SQL Injection

SQL injection is a web attack against database-backed applications.

SQL means Structured Query Language. It is used to communicate with databases.

SQL injection occurs when an attacker injects SQL-related input into a query so that the database returns more information or performs actions the application did not intend.

## Basic SQL Behavior

SQL code often follows human-readable logic, such as:

- Select data from a table.
- Apply conditions using `WHERE`.
- Return records matching those conditions.

Important SQL syntax from the lecture:

- `--` is a comment indicator.
- Anything after `--` is treated as a comment and is not executed.

Attackers can abuse this if user input is inserted directly into SQL queries.

## SQL Injection Example: Product Search

Normal situation:

- A user visits a shopping site such as Amazon.
- The user searches for a category such as gifts.
- The site queries its database for products where:
  - Category is `gifts`.
  - Release status equals `1`, meaning the product is released, in stock, or ready for sale.

Intended query logic:

- Return products only when category is gifts and release status is valid.

Attack input:

- The attacker enters something like `gifts'--` into the search field.

Effect:

- The single quote closes the original string.
- The `--` comments out the remaining condition.
- The release-status condition is no longer executed.
- The database returns all products in the gifts category, including unreleased products.

This lets the attacker view data that should have been hidden.

## SQL Injection Example: Login Bypass

Normal login logic:

- The user must provide the correct username and password.
- Example username: `administrator`.
- Example password: `secret`.
- The query checks both username and password.

Attack input:

- The attacker uses `administrator'--` or similar input.

Effect:

- The username condition remains.
- The password condition is commented out.
- The system checks only whether the username is `administrator`.
- The attacker may bypass authentication without providing the correct password.

The core problem is that the developer allowed unsanitized strings to be treated as valid SQL input.

## SQL Injection Defense

Ways to prevent SQL injection include:

- Use parameterized queries.
- Use prepared statements.
- Avoid unsafe string concatenation in SQL queries.
- Sanitize user input.
- Restrict user input when possible.
- Use dropdown boxes or controlled choices instead of free-text input where appropriate.
- Prevent users from inserting logic-changing characters or conditions into SQL queries.

Example:

- Instead of allowing arbitrary category text, a site can provide fixed category options such as gifts or appliances.
- This prevents users from adding comment markers or extra logic such as `OR` conditions.

## Hardware Threats

Hardware threats are grouped into categories such as:

- Environmental threats.
- Technical threats.
- Human-caused threats.

Human-caused threats may arise from different human actions or mistakes.

## Emerging Threats

Emerging cybersecurity threats include:

- Internet of Things, or IoT, devices.
- Botnets leveraging IoT devices.
- Distributed denial-of-service attacks using many compromised devices.
- Better malware.
- State-sponsored threats.
- New connected devices exposing new risks.
- Poorly maintained firmware.
- Changing corporate network environments.

## IoT, BYOD, and Cloud Risks

Modern environments create new risks:

- Many small businesses use cloud services instead of maintaining their own servers.
- Organizations and universities often allow bring your own device, or BYOD.
- BYOD increases flexibility but adds risk.
- A poorly maintained personal laptop can infect other computers on the same subnet.
- University networks, such as Griffith's, may be exposed to risk when students bring unmanaged devices.

## Preventing Attacks

General prevention ideas from the lecture:

- Use clean software and apps.
- Check whether software is clean.
- Use reputable antivirus software.
- Keep antivirus software updated.
- Check software, malware signatures, or hash values using analysis websites.
- Compare whether different antivirus tools detect a given malware signature.
- Prefer reputable antivirus software over tools that fail to detect known malware.

Workshop practice includes:

- Testing hashes or signatures using websites.
- Checking whether a hash is recognized as a malware signature.
- Seeing which antivirus engines detect the malware.
- Comparing antivirus tools based on detection results.

Additional prevention topics mentioned:

- Securing a home router.
- Choosing stronger encryption algorithms.
- Understanding encryption through upcoming cryptography weeks.
- Following safer email practices.

## Course Logistics

- Workshop activities are scheduled for the week.
- Students should register their Azure VM account using the invitation link.
- Students who did not receive an Azure VM account should contact the tutor.
- Late-enrolled students should follow the announcement instructions.
- Questions can be asked through Teams.
