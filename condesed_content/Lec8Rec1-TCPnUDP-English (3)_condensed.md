# Lecture 8 Recording 1: TCP and UDP

## Transport Segmentation - long messages split into numbered segments for ordering/reassembly.

## TCP - Transmission Control Protocol; connection setup before data.

## UDP - User Datagram Protocol; connectionless sending.

## TCP Handshake - SYN, SYN-ACK, ACK.

## TCP Reliability - checks readiness before communication.

## UDP Traits - no handshake, simple, low overhead, fast, less reliable.

## UDP Use Case - speed matters and some loss is acceptable.

## SYN Flood - many incomplete TCP handshakes consume server resources.

## Direct SYN Flood - attacker sends SYNs; server waits for missing ACKs.

## Direct Defense - filter attacker IP if identifiable.

## Spoofed SYN Flood - fake source IPs make filtering one address ineffective.

## Completed-Handshake Attack - attacker completes handshake but sends no data, consuming resources.

## SYN Flood Impact - denial of service for legitimate users.

## FIN Attack - attacker sends FIN early to close/disrupt legitimate connection.

## Reset Attack - attacker sends reset; server discards messages and waits for restart.

## TCP DDoS - many controlled computers send SYNs or spoofed requests to overload server.

## UDP Security Issues - no handshake, no authentication, easy impersonation/spoofing, DoS risk.

## DNS - translates hostnames/URLs like `google.com` to IP addresses.

## DNS Uses UDP - fast, efficient, time-sensitive lookups.

## DNS Cache Poisoning - fake DNS entry sends clients to fake site.

## Cache Poisoning Impact - fake site may infect users with malware.

## DNS Spoofing DDoS - queries spoof victim IP; DNS responses overload victim.

## Transport Vulnerabilities - unauthorized access, cyber attacks, eavesdropping, tampering.

## Mitigations - firewalls, IDS, IPS, secure protocols on top of TCP/UDP.
