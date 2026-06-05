# Network Security: Physical and Data Link Layers

## TCP/IP Layer Model

1. Physical
2. Data link
3. Network
4. Transport
5. Application

- 5-layer model groups 7-layer top layers into application.
- Security problems/countermeasures are handled layer by layer.

## Physical Layer Security

- Strategies: link shielding, physical separation, redundancy, service/security controls.

## Transmission Link Shielding

- Protects cables from leakage/interference/tapping.
- Cable parts: conductor, dielectric, foil shield, braided shield, outer rubber.
- Purpose: reduce electromagnetic leakage and physical penetration.
- Shielded rooms can reduce wireless/electromagnetic leakage.

## Physical Separation

- Prevents direct connection between networks.
- **Internet:** external network.
- **Intranet:** internal/private network.
- **Air gap / separation switch:** physically separates networks.

## Separation Switch vs Firewall

- **Firewall:** keeps connection; applies security controls.
- **Physical separation:** prioritizes security; no direct Internet-intranet connection.
- Use cases: e-government, stock trading, high-confidentiality systems.

## E-Government Separation Example

- External data goes to storage first, is checked, then loaded inward if safe.
- Internal data goes to storage, disconnects from intranet, then connects outward.
- Result: external network and intranet are never directly connected.

## Data Link Layer Security

- Topics: link encryption, WLAN, SSID, WEP/WPA, spoofing prevention, ARP/MAC mapping, anti-sniffing.

## Link-Layer Encryption

- Encrypts whole frame/package, including headers/trailers.
- Advantage: protects metadata on the link.
- Weakness: intermediate switches may decrypt/re-encrypt and see plaintext.

## End-to-End / Application-Layer Encryption

- Encrypts message content before lower-layer headers are added.
- Intermediate devices can route but cannot read message body.

## Combining Encryption Layers

- Use application-layer encryption for content + link-layer encryption for frames.
- If a switch decrypts link layer, message body remains ciphertext.

## Wireless LAN and SSID

- **WLAN = Wireless Local Area Network.**
- **SSID = Service Set Identifier:** Wi-Fi network name; up to 32 characters.
- Users must identify correct SSID before connecting.

## Broadcasting and Hiding SSID

- Broadcasting announces the network name.
- Hiding SSID is weak security; devices may still reconnect.
- Do not rely on hidden SSID as protection.

## Default SSID and Password Risks

- Change default SSID; it may reveal router model.
- Change default password/key; defaults may be known online.
- Use long keys: at least 13 characters; around 20+ better.

## Wireless Security Types

- Open network = least secure.
- Use strongest available security/encryption options.
