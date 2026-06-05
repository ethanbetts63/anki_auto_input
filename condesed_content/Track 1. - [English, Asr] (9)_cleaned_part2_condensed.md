# Link-Layer and Network-Layer Security

## Secure Wireless Router Configuration

- Use **WPA2**; WPA2 Personal fits home use.
- Avoid **WEP**.
- Use **AES**; avoid DES/Triple DES.
- Weak protocols/encryption expose traffic.

## Public Wi-Fi Safety

- Public hotspots are risky because users do not control them.
- Enable firewall.
- Disable network discovery.
- Disable file/printer/public-folder sharing.
- Verify **SSID**; fake hotspots can sniff traffic.
- Prefer **HTTPS**.
- Use **VPN** for sensitive transactions.
- Disable unused Wi-Fi, Bluetooth, NFC, wireless interfaces.
- Keep AV/security tools updated.

## ARP and MAC/IP Translation

- **MAC address:** physical local-delivery address.
- **ARP = Address Resolution Protocol:** maps IP address to MAC address.
- **ARP table:** stores IP-to-MAC mappings.

### ARP Security Issue

- Devices can lie about IP-to-MAC mappings.
- False ARP records can redirect/block traffic.
- Mitigations: correct/static ARP records; improve/replace ARP.

## Sniffing

- **Sniffing:** capturing/analyzing network traffic.
- Legitimate: troubleshooting, bottlenecks, capacity planning.
- Malicious: steal credentials/payment/sensitive data.
- **Wireshark:** common packet-sniffing tool.
- Anti-sniffing tools can detect/respond.

## Network Layer Basics

- Uses **IP addresses** for routing.
- Main risks: routing table vulnerabilities and IP address vulnerabilities.

## Routing Table Vulnerabilities

- Dynamic routing tables can be attacked.
- Attacks: DoS, route poisoning, routing-table flooding, routing-path spoofing, QoS-path spoofing.
- **QoS = Quality of Service.**

## IP Address Vulnerabilities

- Weak authentication of IP ownership/use.
- Hard to prove who used an IP.

### Fake Address / IP Conflict Attacks

- Attacker uses same IP as another device in same subnet.
- Effects: unreliable communication, blocked packets, router disruption if router IP is duplicated.

## DHCP Fake Release Attack

- **DHCP = Dynamic Host Configuration Protocol.**
- False release frees an in-use IP.
- DHCP may assign it to another device, causing duplicate-IP conflict.

## ICMP Flooding / Smurf Attack

- **ICMP:** checks if a host is alive/online.
- Attacker sends spoofed ICMP requests using victim IP.
- Replies flood victim; causes DoS.
- Spoofed-source ICMP flood = **Smurf attack**.

## Network-Layer Countermeasures

- **IPv6:** newer IP protocol; migration incomplete.
- **IPsec:** secures IPv4 communication.
- Disable ICMP where appropriate.
- **IP filtering:** firewalls, IDS, IPS block bad IPs.
- **NAT = Network Address Translation:** hides internal IPs via address translation.

## Key Takeaways

- Use WPA2 + AES.
- Treat public Wi-Fi as risky.
- ARP can be poisoned.
- Sniffing can diagnose or steal.
- Network attacks: routing attacks, IP conflicts, DHCP fake release, ICMP/Smurf.
- Defenses: IPv6, IPsec, ICMP limits, filtering, NAT.
