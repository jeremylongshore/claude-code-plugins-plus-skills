---
allowed-tools: Read, Write, Edit
license: MIT
description: Configure FireCrawl enterprise SSO, role-based access control, and organization
  management. Use when implementing SSO integration, configuring role-based permissions,
  or setting up organization-level controls for FireCrawl. Trigger with phrases li...
name: firecrawl-enterprise-rbac
---
# Firecrawl Enterprise Rbac

This skill provides automated assistance for firecrawl enterprise rbac tasks.

## Prerequisites
- FireCrawl Enterprise tier subscription
- Identity Provider (IdP) with SAML/OIDC support
- Understanding of role-based access patterns
- Audit logging infrastructure

## Instructions

### Step 1: Define Roles
Map organizational roles to FireCrawl permissions.

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
- [FireCrawl Enterprise Guide](https://docs.firecrawl.com/enterprise)
- [SAML 2.0 Specification](https://wiki.oasis-open.org/security/FrontPage)
- [OpenID Connect Spec](https://openid.net/specs/openid-connect-core-1_0.html)