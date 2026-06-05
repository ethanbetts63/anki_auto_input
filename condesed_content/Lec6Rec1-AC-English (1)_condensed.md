# Access Control Models

## Overview

Access control models are frameworks that determine how resources and information are accessed and managed within a system.

They are important for:

- Security
- Privacy
- Compliance

They are used in many environments, including:

- Corporate networks
- Cloud services
- Personal computers
- Social media platforms
- High-security government or military systems

## Four Access Control Models

The lecture covers four access control models:

- Discretionary Access Control (DAC)
- Mandatory Access Control (MAC)
- Role-Based Access Control (RBAC)
- Attribute-Based Access Control (ABAC)

## Discretionary Access Control (DAC)

Discretionary Access Control is an access control model where the owner of a resource has authority to decide who can access that resource.

Permissions are assigned based on user identity and can be modified by the resource owner.

### DAC Examples

Examples of DAC include:

- Personal computers running Linux, Windows, or macOS
- Sharing a file with someone and setting permission so others can edit it
- Allowing an application to access your location
- Granting applications access on platforms such as Facebook or Instagram
- Controlling who can see, comment on, or share social media posts

### DAC Advantages

DAC is:

- Flexible
- User friendly

### DAC Risks

DAC can create security risks if not managed properly because users may grant access to unauthorized individuals.

## Mandatory Access Control (MAC)

Mandatory Access Control is a stricter access control model where access rights are regulated by a central authority according to predefined policies.

In MAC:

- Users cannot freely change access permissions.
- Access is determined by information classification and user security clearance.
- A central authority enforces the access rules.

MAC is often used in high-security environments such as:

- Military systems
- Government systems

### MAC Clearance Example

A system access control policy may define security clearance levels and associate system objects with those levels.

Example object labels:

- Unclassified
- Confidential
- Secret
- Top Secret

Access is granted or denied based on the subject's clearance level.

Example:

- A senior engineer with Secret clearance can access Secret, Confidential, and Unclassified objects.
- The same engineer cannot access Top Secret objects.

### MAC Advantages

MAC provides:

- Higher security than DAC
- Reduced risk of human error

### MAC Disadvantages

MAC involves:

- Complex implementation
- Higher administrative overhead

## Role-Based Access Control (RBAC)

Role-Based Access Control assigns permissions based on the roles users have within an organization.

Instead of assigning permissions directly to each individual user:

- Permissions are associated with roles.
- Users are assigned to roles.
- Users receive access based on their assigned roles.

RBAC simplifies management and improves security by ensuring users access only the information needed for their job functions.

### RBAC Examples

Examples:

- A CEO can access all resources.
- An accountant can access only the financial database.
- A user is granted access according to their actual role in the company.

## Attribute-Based Access Control (ABAC)

Attribute-Based Access Control is also called:

- Policy-Based Access Control
- Rule-Based Access Control

ABAC evaluates attributes of users, resources, and the environment to make access decisions.

It is dynamic and fine grained.

### ABAC Attribute Types

ABAC policies may consider:

- User attributes
- Resource attributes
- Environmental conditions
- User roles
- Resource classification
- Context

### ABAC Example

An example rule:

- Only send an email when the email size is less than 5 MB.

### ABAC Advantages

ABAC provides:

- High adaptability
- Fine-grained policy control
- Flexibility
- Strong security
- Suitability for distributed or rapidly changing environments

### ABAC Disadvantages

ABAC requires:

- More complex implementation
- More challenging policy management

## Case Study: Movie Database Management System

The lecture compares RBAC and ABAC using a movie database management system.

### RBAC Version

In the RBAC model, users are assigned roles based on age:

- Adult
- Juvenile
- Child

Access is granted based on these roles.

### ABAC Version

In the ABAC model, access is granted based on detailed attribute rules involving user age and movie rating.

Rules:

- If age is greater than 17 and the movie rating belongs to the allowed rating group, access is granted.
- If age is between 13 and 17 and the movie rating is PG-13 or G, access is granted.
- If age is less than 13 and the movie rating is G, access is granted.

The ABAC model uses explicit conditions rather than only broad roles.

## Adding More Attributes

The lecture then adds two more attributes to the movie database:

- User membership level
- Movie release date

This shows how RBAC and ABAC respond differently when the access policy must consider more information.

### Effect on RBAC

In RBAC, adding new attributes causes the number of roles and permissions to grow.

The original three roles must be expanded to include membership level:

- Adult with premium membership
- Adult with regular membership
- Juvenile with premium membership
- Juvenile with regular membership
- Child with premium membership
- Child with regular membership

The permissions grow rapidly as the number of attributes increases.

The lecture describes this growth as exponential when more attributes are added.

### Effect on ABAC

In ABAC, the original age and rating rule does not need to be changed.

New rules can be added for the new attributes.

Example added rules:

- Access is allowed if membership is premium.
- Access is allowed if membership is regular and the movie has been released.
- Access is granted when the original rule and the new attribute rules are satisfied together.

ABAC adapts by adding new rules while preserving the original rule.

This illustrates ABAC's finer-grained and more flexible policy structure.

## Comparison Summary

### DAC

- Resource owner controls access.
- Flexible and user friendly.
- Risky if users grant access carelessly.

### MAC

- Central authority controls access.
- Uses classifications and clearances.
- Strong security.
- More complex and administratively heavy.

### RBAC

- Access is based on organizational roles.
- Easier to manage than assigning permissions user by user.
- Works well when roles map cleanly to job functions.
- Can become complicated when many attributes must be considered.

### ABAC

- Access is based on attributes and policies.
- More dynamic and fine grained than RBAC.
- Handles changing or complex environments well.
- Requires more complex implementation and policy management.

## Final Takeaway

Access control models are fundamental for maintaining security and managing access to resources.

Understanding DAC, MAC, RBAC, and ABAC helps organizations choose an access control model that fits their security needs, protects sensitive information, and supports compliance requirements.
