---
name: juicebox-enterprise-rbac
description: |
  Configure Juicebox enterprise role-based access control. Use when implementing team permissions, configuring access policies, or setting up enterprise security controls. Trigger with phrases like "juicebox RBAC", "juicebox permissions", "juicebox ...
allowed-tools: Read, Write, Edit, Bash(cmd:*)
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Juicebox Enterprise Rbac

This skill provides automated assistance for juicebox enterprise rbac tasks.

## Prerequisites
- Enterprise Juicebox plan
- Identity provider (Okta, Auth0, Azure AD)
- Understanding of access control patterns


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- Role and permission definitions
- Permission checker implementation
- Authorization middleware
- Team access control
- Audit logging

## Resources
- [Enterprise Security Guide](https://juicebox.ai/docs/enterprise/security)
- [SSO Configuration](https://juicebox.ai/docs/sso)