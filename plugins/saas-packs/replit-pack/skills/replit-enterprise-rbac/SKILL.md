---
allowed-tools: Read, Write, Edit
license: MIT
description: Configure Replit enterprise SSO, role-based access control, and organization
  management. Use when implementing SSO integration, configuring role-based permissions,
  or setting up organization-level controls for Replit. Trigger with phrases like
  "re...
name: replit-enterprise-rbac
---
# Replit Enterprise Rbac

This skill provides automated assistance for replit enterprise rbac tasks.

## Prerequisites
- Replit Enterprise tier subscription
- Identity Provider (IdP) with SAML/OIDC support
- Understanding of role-based access patterns
- Audit logging infrastructure

## Instructions

### Step 1: Define Roles
Map organizational roles to Replit permissions.

### Step 2: Configure SSO
Set up SAML or OIDC integration with your IdP.

### Step 3: Implement Middleware
Add permission checks to API endpoints.

### Step 4: Enable Audit Logging
Track all access for compliance.

## Output
- Role definitions implemented
- SSO integration configured
- Permission middleware active
- Audit trail enabled

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [Replit Enterprise Guide](https://docs.replit.com/enterprise)
- [SAML 2.0 Specification](https://wiki.oasis-open.org/security/FrontPage)
- [OpenID Connect Spec](https://openid.net/specs/openid-connect-core-1_0.html)