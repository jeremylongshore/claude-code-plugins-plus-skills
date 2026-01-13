---
allowed-tools: Read, Write, Edit
license: MIT
description: Configure Vast.ai enterprise SSO, role-based access control, and organization
  management. Use when implementing SSO integration, configuring role-based permissions,
  or setting up organization-level controls for Vast.ai. Trigger with phrases like
  "...
name: vastai-enterprise-rbac
---
# Vastai Enterprise Rbac

This skill provides automated assistance for vastai enterprise rbac tasks.

## Prerequisites
- Vast.ai Enterprise tier subscription
- Identity Provider (IdP) with SAML/OIDC support
- Understanding of role-based access patterns
- Audit logging infrastructure

## Instructions

### Step 1: Define Roles
Map organizational roles to Vast.ai permissions.

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
- [Vast.ai Enterprise Guide](https://docs.vastai.com/enterprise)
- [SAML 2.0 Specification](https://wiki.oasis-open.org/security/FrontPage)
- [OpenID Connect Spec](https://openid.net/specs/openid-connect-core-1_0.html)