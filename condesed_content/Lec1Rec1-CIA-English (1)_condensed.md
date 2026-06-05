# Lec1Rec1: CIA Model and Core Cybersecurity Goals

## Core Cybersecurity Goals

Cybersecurity begins with the **CIA model**, which describes the core goals of security:

- **Confidentiality**
- **Integrity**
- **Availability**

The CIA model was proposed in **1974**. As online environments developed, it became clear that CIA does not cover every security goal. Two additional goals are commonly added:

- **Authenticity**
- **Non-repudiation**

Together, these make five important cybersecurity goals:

1. Confidentiality
2. Integrity
3. Availability
4. Authenticity
5. Non-repudiation

## Confidentiality

**Confidentiality** means only authorized people can see or access data.

It is mainly related to **data security** and aims to prevent unauthorized access to sensitive digital assets.

Documents may be classified differently depending on the organization or sector. For example, in a private-sector organization, documents might be classified as:

- Public
- Internal
- Confidential

Methods used to achieve confidentiality include:

- Encryption
- Authentication
- Access control

## Integrity

**Integrity** means there is assurance that data has not been manipulated, corrupted, or changed without authorization.

It is also related to **data or information security** and protects data against:

- Unauthorized change
- Accidental change

Integrity is important when releasing software or data. Users or receivers should be confident that:

- No malicious data or code has been attached to the original software.
- The original data has not been changed.

Methods used to protect integrity include:

- Security programs that manage and detect changes
- Permission controls for access
- Auditing and accounting processes that record changes to data

## Availability

**Availability** means data, systems, services, users, and applications remain accessible when needed.

Availability is also connected to data and information security. The goal is to ensure that services and information are accessible continuously or reliably.

Common threats to availability include:

- **Accidental threats**, such as:
  - Natural disasters
  - Equipment failure
- **Deliberate threats**, such as:
  - Attacks by hackers or malicious users
  - Attempts to make a service unavailable or unusable

## Authenticity

**Authenticity** means there is assurance about who created or sent data.

The goal is to verify the claimed origin of information, such as confirming that an email or message really came from the stated sender.

## Non-Repudiation

**Non-repudiation** means there is assurance that the author or sender cannot deny an action later.

For example, if an issuing body provides a digital certificate, non-repudiation helps ensure that the issuer cannot later deny having issued it.

Non-repudiation can be accomplished through methods such as:

- Digital signatures

## Example Scenarios

### Software Without Malicious Code

Scenario: A software provider wants to guarantee that no malicious code has been attached to the original clean code.

Goal: **Integrity**

Reason: Users need confidence that the downloaded software is still clean and has not been modified by an attacker.

### Service Always Accessible

Scenario: A service provider wants to provide service to users all the time.

Goal: **Availability**

Reason: The service should remain accessible and usable.

### Financial Department Email

Scenario: A financial department wants the receiver to trust that an email is really from the department.

Goal: **Authenticity**

Reason: The receiver needs assurance about the sender's identity.

### Degree Certificate Issued Years Ago

Scenario: A university should not be able to deny that it issued a degree certificate after many years.

Goal: **Non-repudiation**

Reason: The issuing body should not be able to deny the action of issuing the certificate.

### Exam Papers and Answers

Scenario: A university learning system provides access to teaching materials, but exam papers and answers must not be accessed by students at the wrong time.

Goal: **Confidentiality**

Reason: Sensitive exam materials should only be accessible to authorized people at authorized times.
