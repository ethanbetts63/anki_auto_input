# Lecture 8 Recording 2: IDS, IPS, and Firewalls

## IDS and IPS Overview

In cybersecurity, **Intrusion Detection Systems (IDS)** and **Intrusion Prevention Systems (IPS)** help protect networks and systems from malicious activities.

## Intrusion Detection System (IDS)

An **Intrusion Detection System (IDS)** is a security tool designed to monitor:

- Network traffic.
- System activities.

It looks for:

- Signs of malicious behavior.
- Policy violations.

Functionally, IDS is passive:

- It monitors.
- It reports.
- It sends alerts.
- It does not directly block traffic by itself.

When a threat is detected, an IDS may:

- Write to a log file.
- Send a notification.

## Intrusion Prevention System (IPS)

An **Intrusion Prevention System (IPS)** is an advanced security solution that detects potential threats and takes proactive measures to prevent harm.

IPS is active:

- It monitors and analyzes traffic.
- It intervenes in real time.
- It blocks or prevents attacks.
- It can drop packets.
- It may quarantine affected systems.

IPS requires stricter configuration than IDS because it actively affects traffic flow.

## IDS vs IPS

Key functional difference:

- **IDS** detects and reports threats passively.
- **IPS** detects threats and actively blocks or prevents them.

Response difference:

- IDS writes logs or sends notifications after detecting a threat.
- IPS can drop malicious packets or take immediate action.

Configuration difference:

- IPS needs stricter configuration because it can block traffic and affect communication.
- IDS is less intrusive because it mainly observes and reports.

## Host-Based and Network-Based IDS

There are two main types of IDS:

- **Host-based IDS**.
- **Network-based IDS**.

A host-based IDS can be installed on local devices to provide extra protection for those devices.

A network-based IDS monitors network traffic. It can be placed:

- Before a firewall.
- After a firewall.
- Beside a switch, where it can inspect replicated traffic.

Placing IDS before or after a firewall can help administrators understand:

- How the firewall is working.
- Which traffic has been blocked by the firewall.
- Whether firewall configuration needs improvement.

## Honeypot Systems

A **honeypot** is a cybersecurity tool that acts as a decoy.

Purpose:

- Lure attackers.
- Trap attackers.
- Allow security researchers to study attacker behavior.
- Help identify vulnerabilities.

Characteristics:

- It mimics a real system or network.
- It is isolated and monitored.
- It allows analysis of attacks without endangering real systems.

Researchers and network administrators can use honeypots to extract anomaly signatures for IDS and IPS.

## Host-Based and Network-Based IPS

Like IDS, IPS can also be categorized as:

- **Network-based IPS**.
- **Host-based IPS**.

A network-based IPS protects network traffic.

A host-based IPS protects individual hosts.

Deployment distinction:

- Network-based IDS can be placed beside a switch and work on replicated traffic.
- Network-based IPS should be placed directly in the route of traffic flow.

Reason:

- IPS must provide immediate input and response to incidents in real time.
- To block packets or take action, IPS must be in the actual traffic path.

## Firewall Overview

A **firewall** can be hardware or software.

Compared with physical separation, a firewall prioritizes connection and then provides security on a best-effort basis.

Firewall purpose:

- Control which traffic may pass through.
- Block unwanted or unauthorized traffic.
- Provide a barrier against threats.
- Generate logs.
- Enhance security.

## Firewall Rules and Default Deny

Firewall rules define which traffic is allowed through.

Example principle:

- Rules specify traffic that can pass.
- All other traffic is blocked.

This is called the **default deny principle**.

Default deny supports a more secure firewall configuration because unspecified traffic is blocked.

## Firewall Advantages

Advantages of firewalls:

- Enhanced security.
- Controlled traffic.
- Generated logs.
- Barrier against threats.

## Firewall Disadvantages and Caveats

Firewalls can also create challenges:

- They may slow network communication.
- Some traffic may not pass if rules are strict.
- Configuration can be complex.
- Experienced network administrators may be needed.
- False positives may occur.

The lecture describes false positives as cases where abnormal traffic is regarded as legitimate traffic and passed through.

## Firewall Techniques

Three firewall techniques are discussed:

- Packet filtering.
- Proxy servers or proxy firewalls.
- Stateful firewall tracking or stateful inspection.

## Packet Filtering

Packet filtering blocks or allows data based on predefined rules.

Example:

- Traffic may be blocked if the IP address equals a specific suspicious IP address.

## Stateful Inspection

Stateful inspection makes decisions based on the state of traffic.

It uses historical traffic state information:

- The firewall studies traffic state.
- Decisions are made based on those traffic states.

## Proxy Firewall

A proxy firewall acts as a single point of contact with the external world.

It hides internal IP addresses of users and devices.

Security benefit:

- Attackers have more difficulty identifying and targeting specific machines or users inside the internal network.

How it works:

- It intercepts requests.
- It evaluates them against security rules.
- Traffic passes only after the proxy examines and allows it.

The lecture notes that only completed three-way-handshake packet communication can pass through in the shown example.

Security impact:

- This can help stop SYN flood attacks involving incomplete three-way handshakes.
- SYN requests from incomplete handshakes cannot directly burden the actual server behind the firewall.

## Combined Security Solutions

In real systems, firewalls, IDS, and IPS can be used together as added security solutions.

They can enhance security against TCP/IP problems, but they require effort, including:

- Cost.
- Time.
- Configuration work.

## Course Focus

Although firewalls, IDS, and IPS are useful, the course will focus on the design of secure protocols that do not rely on extra equipment or software.
