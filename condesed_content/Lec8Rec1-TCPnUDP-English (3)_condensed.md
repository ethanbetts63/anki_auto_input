# Lecture 8 Recording 1: TCP and UDP

## Transport Layer Segmentation

At the transport layer, a long message can be divided into multiple segments.

Example:

- An email with a large attachment may be separated into three segments.
- A sequence number is attached to each segment.
- The sequence number tells the recipient:
  - How many total segments exist.
  - Which segment this one is, such as 1 of 3, 2 of 3, or 3 of 3.
- The recipient can use these numbers to identify all segments and order them correctly.

## TCP and UDP

There are two main ways to establish communication at the transport layer:

- **TCP**: Transmission Control Protocol.
- **UDP**: User Datagram Protocol.

TCP and UDP differ mainly in how they establish communication:

- TCP uses a connection setup process before data transmission.
- UDP sends data without first establishing a dedicated connection.

## TCP Three-Way Handshake

TCP uses a **three-way handshake** to establish communication between a client and a server.

Process:

1. The client sends a **SYN** message, meaning a synchronization request.
2. The server responds with a **SYN-ACK** message, meaning it acknowledges the synchronization request and is ready to listen.
3. The client sends an **ACK** message, acknowledging the server's response and confirming that communication can begin.

The lecture compares this to a child wanting to talk to a parent:

- The child first checks whether the parent is free.
- If the parent says they are free, the parent gets ready to listen.
- The child confirms and then begins speaking.

TCP is more reliable because it checks readiness before starting communication.

## UDP Communication

UDP does not use a three-way handshake.

UDP is a **connectionless protocol**:

- It transmits data without establishing a dedicated end-to-end connection.
- It is simple.
- It has low overhead.
- It is faster than TCP.
- It is less reliable than TCP.
- It is suitable when speed is important and occasional data loss is acceptable.

The lecture compares UDP to a child who starts talking without checking whether the parent is free. The parent may be busy and may not receive the message.

## TCP Security Issue: SYN Flood Attacks

TCP's three-way handshake can be exploited through **SYN flood** attacks, which can cause denial of service.

### SYN Flood Case 1: Direct SYN Flood

Attack process:

1. The attacker sends many SYN requests to the server.
2. The server replies with SYN-ACK messages.
3. The server reserves ports and resources while waiting for the final ACK.
4. The attacker never sends the final ACK.
5. The server remains busy with incomplete handshakes.

Impact:

- Legitimate users may be unable to connect.
- The server is occupied by fake connection attempts.
- This creates a **Denial of Service (DoS)** attack.

Possible defense mentioned:

- Filter out the attacker's IP address so the server no longer responds to that address.

### SYN Flood Case 2: Spoofed Source Address

Attack process:

1. The attacker spoofs the source IP address.
2. The attacker sends many SYN requests using spoofed addresses.
3. The server sends SYN-ACK responses to those spoofed addresses.
4. The attacker does not send the final ACK.

Impact:

- Filtering a single attacker IP address is no longer effective.
- Requests appear to come from different IP addresses.
- The server remains busy with incomplete connection attempts.

### SYN Flood Case 3: Handshake Completed but No Data Sent

Attack process:

1. The attacker sends SYN requests.
2. The server sends SYN-ACK responses.
3. The attacker sends ACK messages and completes the three-way handshake.
4. The attacker does not send actual data afterward.

Impact:

- The server's resources are still consumed.
- Legitimate service requests may be denied.

All three SYN flood cases can cause denial of service.

## FIN Attack

Normally, when a TCP communication session is completed:

- A message is sent to tell the server that transmission is complete.
- The server responds with a **FIN-ACK** message.

An attacker can exploit this by sending a **FIN** request before a legitimate transmission has finished.

Impact:

- The connection may be closed early.
- Legitimate communication may be disrupted.

## Reset Attack

An attacker can send a **reset** request to the server.

Impact:

- The server may discard previously received messages.
- The server waits for a new start.
- Legitimate communication can be interrupted or lost.

## Distributed Denial of Service Using TCP

TCP vulnerabilities can also be used in a **Distributed Denial of Service (DDoS)** attack.

Examples:

- Direct attack: one attacker sends many SYN requests and does not complete the handshake.
- Spoofing attack: the attacker uses spoofed addresses to send many SYN requests.
- Distributed attack: the attacker controls many computers, which all send SYN requests to the server.

Impact:

- A distributed attack can cause severe server downtime.
- The server may be unable to respond to legitimate users.

## UDP Security Issues

UDP has no three-way handshake and no connection setup.

Security weaknesses mentioned:

- No authentication.
- Easy impersonation of client or server.
- Source IP address can be spoofed.
- Denial of service attacks can exploit UDP vulnerabilities.

## DNS and UDP

The **Domain Name System (DNS)** is an example of a protocol that commonly uses UDP.

DNS allows users to navigate the Internet using hostnames, such as `google.com`, instead of numerical IP addresses.

DNS translates:

- URLs or hostnames into IP addresses.

DNS often uses UDP because:

- UDP is fast.
- UDP is efficient.
- DNS lookups are time sensitive.
- Users do not want long delays when accessing websites.

## DNS Cache Poisoning

**Cache poisoning** can happen in DNS.

Attack process:

1. An attacker injects a fake DNS entry into a DNS server.
2. A client asks the DNS server for the correct IP address.
3. The DNS server returns the fake entry.
4. The client is directed to a fake website instead of the real website.

Possible impact:

- The fake website may infect the client with malware simply when the client visits it.

## DNS Source IP Spoofing and Forgery Attacks

The source IP address can be spoofed in DNS queries.

Attack process:

1. The attacker sends DNS queries with the victim's IP address as the source IP.
2. DNS responses are sent to the spoofed source IP address.
3. The victim receives the responses.

If the victim is a server, many DNS responses can overload it.

This can create a distributed denial of service attack:

- The attacker may control many systems.
- Those systems send DNS queries to servers.
- The victim's IP address is used as the source IP.
- DNS servers respond to the victim.
- The victim server becomes busy and denies other service requests.

## Transport Layer Vulnerabilities Summary

Because TCP and UDP are simple transport-layer protocols and do not provide authentication or encryption by default, several vulnerabilities arise.

The lecture summarizes four types of vulnerabilities:

- **Unauthorized access** due to insufficient access control and weak authentication.
- **Cyber attacks**, including SYN flood attacks and DNS-based attacks.
- **Eavesdropping**, where data may be stolen.
- **Data tampering**, where data may be deliberately modified.

## Mitigation Approaches

Possible mitigation approaches mentioned:

- Firewalls.
- IDS: Intrusion Detection Systems.
- IPS: Intrusion Prevention Systems.
- Adding secure protocols on top of TCP or UDP.

The lecture notes that these defenses will be discussed in more detail in class.
