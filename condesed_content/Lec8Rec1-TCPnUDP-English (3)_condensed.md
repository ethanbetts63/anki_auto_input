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
