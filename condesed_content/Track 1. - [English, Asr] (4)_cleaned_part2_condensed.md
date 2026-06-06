# Cyberattacks: CSRF, XSS, SQL Injection, and Hardware Threats

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

## Attack Prevention - clean software, reputable/updated AV, hash/signature checks, safe email/router practices.

## Malware Hash Checking - analysis sites show whether AV engines detect a sample.
