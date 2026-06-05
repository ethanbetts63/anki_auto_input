# Persuasion, Mobile Awareness, URL Hijacking, and Security Awareness

## Persuasion for Security Behavior

- **Social proof:** show peers following secure behavior.
- **Commitment / consistency:** require signed AUP.
- **AUP:** rules for email, passwords, online behavior, security practices, risks.

## Mobile Device Attack Surface

- Phones expose many interfaces: NFC, Bluetooth, Wi-Fi, SIM, storage cards, sensors.
- **NFC = Near Field Communication:** tap-to-pay; not Bluetooth/Wi-Fi.
- More interfaces = more attack surface.

## Mobile Permission Timing

- **Installation-time permission:** granted at install; may stay active.
- **Runtime permission:** requested when app/feature needs it; supports "while using app."

## Mobile Permission Categories and Risks

1. **Network communication:** internet access; can exfiltrate data.
2. **Personal information:** contact access; with internet can exfiltrate contacts.
3. **SMS:** can read verification codes; avoid unless necessary.
4. **Location:** grant only when needed; disable unnecessary constant access.

## URL Hijacking

- Names: direct linking, cybersquatting, typosquatting, URL hijacking, fake URL, brandjacking.
- Method: attacker uses lookalike domains: typos, wrong extension, hyphen changes, altered spelling, brand imitation.

## URL Hijacking Defenses

- Use trusted sites.
- Confirm URLs before pressing Enter.
- Search official site if unsure.
- Never click suspicious links.
- Use separate computer/VLAN for casual browsing where possible.
- Register likely typo domains first.

### VLAN

- **VLAN = Virtual Local Area Network.**
- Limits malware spread between network segments.
- Separate casual browsing from work systems.

### Defensive Domain Registration - register typo versions of domains.

## Why Email and Web-Based Attacks Succeed

- **No AUP:** no formal security rules/commitment.
- **No awareness training:** users miss phishing/persuasion signs.
- **No employee buy-in:** users do not see security relevance.
- **Poor email/web awareness:** users trust unsafe links/sites.
- **Poor endpoint protection:** outdated/missing AV, anti-spam, BYOD controls.

## Awareness Plan Guideline

- Create/enforce AUP.
- Run awareness training.
- Teach phishing indicators.
- Explain social engineering/persuasion.
- Build employee buy-in.
- Improve email/web-risk awareness.
- Improve endpoint protection.
- Keep AV/anti-spam updated.
- Manage BYOD risk.
