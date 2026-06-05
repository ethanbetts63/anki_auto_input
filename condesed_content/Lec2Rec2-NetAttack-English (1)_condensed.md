# Network Attacks

## Packet Sniffing

Packet sniffing is a data interception technique that captures and analyzes network packets through traffic control or monitoring devices.

Packet sniffing can be performed by many parties, including:

- Internet service providers, such as Telstra or Optus
- Governments
- Advertising companies
- Attackers
- Network administrators

### Legitimate Uses

Network administrators can use packet sniffing as a network protocol analysis and troubleshooting tool. It can help:

- Identify congested links
- Identify applications generating the most traffic
- Collect data for predictive analysis
- Highlight peaks and troughs in network demand

Tools such as Wireshark can capture and analyze packets.

### Malicious Uses

Attackers can use sniffed packets to steal information and launch further attacks. Examples of stolen information include:

- Email attachments
- Company files
- Other sensitive network traffic

Because free packet-sniffing tools are available, packet sniffing is accessible to many attackers.

## Packet Spoofing

Packet spoofing is the technique of creating packets with false identity information, especially a false source IP address.

The goals of spoofing include:

- Disguising the origin of a packet
- Impersonating another device or user
- Launching network-based attacks

Packet spoofing is a fundamental technique used in many network attacks.

### Types of Spoofing

- **ARP spoofing:** Spoofs the physical address associated with an IP address.
- **IP spoofing:** Spoofs an IP address.
- **Email spoofing:** Falsifies or cheats the email address.
- **DNS spoofing:** Causes a domain name to resolve to a false destination.

## DNS Spoofing

DNS stands for **Domain Name Server**. DNS acts like a translator between human-readable website names and IP addresses.

When a user enters a URL such as `google.com`, the browser cannot use that name directly as a network address. DNS translates the domain name into an IP address so the user can be brought to the correct site.

In DNS spoofing, the DNS translator provides a false address. The user enters a legitimate website URL but is directed to a spoofed domain instead of the intended site.

DNS spoofing is a common way for attackers to spread worms and viruses into networks.

## TCP/IP Attacks

TCP/IP is the protocol suite that allows modern networks to run properly. There are many attacks against TCP/IP. More detailed TCP/IP network attacks are covered later in the network security part of the course.

## Denial of Service and Distributed Denial of Service

DoS means **Denial of Service**. DDoS means **Distributed Denial of Service**.

A spoofing-based denial-of-service attack can work as follows:

1. The attacker sends packets with a spoofed IP address.
2. The spoofed source IP address belongs to the victim.
3. Many computers receive the packets and believe the victim sent the requests.
4. Those computers reply to the victim.
5. The victim receives a very large volume of responses.

In a distributed version, the attacker may control a set of computers called **bots**. The attacker and bots send packets to many receivers while spoofing the victim's IP address.

The receivers believe the packets came from the victim and send their replies back to the victim. If the victim is a company server, the huge number of replies can prevent it from responding to legitimate requests.

One example is a DoS attack based on spoofed ICMP request and reply packets.

## Key Takeaways

- Packet sniffing captures and analyzes packets; it has both legitimate administrative uses and malicious uses.
- Packet spoofing falsifies packet identity information to disguise the source or impersonate another device.
- DNS spoofing redirects users from an intended domain to a false destination.
- Spoofed packets can be used to amplify traffic toward a victim in DoS or DDoS attacks.
