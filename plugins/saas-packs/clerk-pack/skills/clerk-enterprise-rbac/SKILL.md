---
allowed-tools: Read, Write, Edit, Grep
license: MIT
description: Configure enterprise SSO, role-based access control, and organization
  management. Use when implementing SSO integration, configuring role-based permissions,
  or setting up organization-level controls. Trigger with phrases like "clerk SSO",
  "clerk R...
name: clerk-enterprise-rbac
---
# Clerk Enterprise Rbac

This skill provides automated assistance for clerk enterprise rbac tasks.

## Prerequisites
- Clerk Enterprise tier subscription
- Identity Provider (IdP) with SAML/OIDC support
- Understanding of role-based access patterns
- Organization structure defined

## Instructions

1. Go to Configure > SSO Connections
2. Add SAML Connection
3. Configure IdP settings:


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- SAML SSO configured
- Roles and permissions defined
- RBAC enforcement in middleware
- Organization management

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Resources
- [Clerk SSO Guide](https://clerk.com/docs/authentication/saml)
- [Organizations](https://clerk.com/docs/organizations/overview)
- [Roles & Permissions](https://clerk.com/docs/organizations/roles-permissions)