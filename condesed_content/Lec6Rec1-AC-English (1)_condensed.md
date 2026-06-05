# Access Control Models

## Access Control Models - frameworks controlling resource/data access for security, privacy, compliance.

## Environments - corporate networks, cloud, PCs, social media, government/military.

## Four Models - DAC, MAC, RBAC, ABAC.

## DAC - resource owner decides who can access.

## DAC Basis - permissions assigned by user identity and modifiable by owner.

## DAC Examples - personal OS files, shared documents, app permissions, social-media visibility.

## DAC Pros - flexible and user friendly.

## DAC Risk - users may grant unauthorized access.

## MAC - central authority enforces predefined classification/clearance policy.

## MAC Rule - users cannot freely change permissions.

## MAC Environments - military/government/high-security systems.

## MAC Labels - unclassified, confidential, secret, top secret.

## MAC Clearance Example - Secret user accesses Secret/Confidential/Unclassified, not Top Secret.

## MAC Pros - stronger security and less human error.

## MAC Cons - complex implementation and high admin overhead.

## RBAC - permissions assigned to roles; users assigned to roles.

## RBAC Benefit - simpler management than per-user permissions.

## RBAC Examples - CEO all resources; accountant financial database.

## RBAC Limit - complex when many non-role attributes matter.

## ABAC - access based on user/resource/environment attributes and policies.

## ABAC Aliases - policy-based or rule-based access control.

## ABAC Attributes - user attributes, resource attributes, environment, role, classification, context.

## ABAC Example - send email only if size under 5 MB.

## ABAC Pros - adaptable, fine-grained, flexible, secure, distributed-environment friendly.

## ABAC Cons - complex implementation and policy management.

## Movie RBAC - roles by age: adult, juvenile, child.

## Movie ABAC - age plus rating rules: `>17`, `13-17`, `<13`.

## Extra Attributes - membership level and release date.

## RBAC Attribute Growth - adding attributes multiplies roles/permissions.

## ABAC Attribute Growth - add rules while preserving existing rules.

## Comparison - DAC owner-driven; MAC authority-driven; RBAC role-driven; ABAC attribute/rule-driven.
