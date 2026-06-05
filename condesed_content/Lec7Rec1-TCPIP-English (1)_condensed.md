# Lecture 7 Recording 1: TCP/IP Model

## Network Models

A network model is a conceptual framework that breaks network communication into manageable layers. Each layer is responsible for specific tasks.

Layered models help because:

- Each layer has a specific function.
- Network communication can be processed logically.
- Failures are easier to locate because issues can be traced to a layer.

Two popular models for Internet communication are:

- **OSI model**: Open Systems Interconnection model, with seven layers.
- **TCP/IP model**: commonly described with four layers; some people use a five-layer TCP/IP model.

## OSI Model vs TCP/IP Model

Both OSI and TCP/IP use layers to organize communication and information processing.

The main difference is that:

- The **OSI model** separates more functions into more layers.
- The **TCP/IP model** groups some of those functions into fewer layers, such as grouping functions into the application layer.

The TCP/IP model is more practical and protocol-oriented:

- It addresses specific communication challenges.
- It relies on standardized protocols.
- It is the model used in this course.

The OSI model is broader and more conceptual:

- It is a comprehensive framework.
- It is protocol independent.
- It is designed to describe many forms of network communication.

## Segmentation

**Segmentation** means dividing a large item or data message into smaller pieces.

The lecture compares this to posting letters or packages:

- A large item may need to be divided into smaller packages.
- Each package needs extra information attached to it.
- That information helps the delivery system know where it came from, where it should go, and how it should be handled.

In network communication, data is encapsulated as it passes through layers. Extra information is added, such as:

- Source information: where the data is from.
- Destination information: where the data should go.
- Protocol information: which protocol should be used.

After encapsulation, the data and its added information are carried through physical transportation links.

## Multiplexing

**Multiplexing** means combining multiple pieces of data into a shared transport mechanism to maximize delivery capacity.

The lecture compares multiplexing to shipment containers:

- Letters and packages are placed into regular containers.
- Containers improve transportation efficiency.
- Similarly, Internet communication uses multiplexing to carry many data streams efficiently.

When data is delivered:

- Protocols read the destination information.
- The message is distributed to the correct destination.
- Protocols in different layers coordinate with each other to complete delivery.

## TCP/IP Security Problems

TCP/IP was not designed with security as a main goal.

Reasons TCP/IP is vulnerable include:

- It was designed for a reliable environment.
- It was invented in the 1970s, when the Internet was not widely used.
- Hackers and large-scale malicious Internet activity were not expected at the time.
- The original purpose was connectivity among different types of networks.
- The system allows anonymous users.
- There is no enforced link between an IP address and a person's real identity.
- Attack tools are now widely available on the Internet, including free tools.
- The rapid development and popularity of the Internet introduced many security issues.

The lecture contrasts IP addresses with mobile phone service:

- Mobile phone numbers are commonly linked to a user's identity.
- IP addresses do not have an enforced identity link in the same way.

## Security Architecture for Open Systems

Security architecture for open systems was developed later to address security concerns.

This security model:

- Focuses on security architecture for open systems interconnection.
- Provides a framework for security services and mechanisms.
- Helps support secure communication between systems.

The course will discuss:

- Security issues in each TCP/IP layer.
- How security goals can be achieved through protocol design.

## Security Attributes

The lecture states that five security attributes are considered across different layers. These attributes are part of the course's security focus, although this recording does not list them individually.

## Course Focus

The course uses the TCP/IP model as the main model for discussion.

The security focus is:

- What security issues exist in each layer.
- How protocols can be designed to meet security goals.
- Why TCP/IP's original design creates vulnerabilities in modern Internet use.
