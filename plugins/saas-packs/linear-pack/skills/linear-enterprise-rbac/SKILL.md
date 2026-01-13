---
allowed-tools: Read, Write, Edit, Grep
license: MIT
description: Implement enterprise role-based access control with linear. use when
  setting up team permissions, implementing sso, or managing access control for linear
  integrations. trigger with phrases like "linear rbac", "linear permissions", "linear
  enterpri...
name: linear-enterprise-rbac
---
# Linear Enterprise Rbac

This skill provides automated assistance for linear enterprise rbac tasks.

## Prerequisites
- Linear organization admin access
- Understanding of Linear's permission model
- SSO provider (Okta, Azure AD, Google Workspace)


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Resources
- [Linear OAuth Documentation](https://developers.linear.app/docs/oauth)
- [RBAC Best Practices](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html)
- [SSO Integration Guide](https://linear.app/docs/sso)