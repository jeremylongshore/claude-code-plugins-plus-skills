# Sso Integration

## SSO Integration

### Group Mapping
```yaml
# SAML/OIDC Group → Granola Role

SSO Provider: Okta

Group Mappings:
  "Granola-Owners":
    role: organization_owner
    workspaces: all

  "Granola-Admins":
    role: organization_admin
    workspaces: all

  "Engineering-Team":
    role: member
    workspaces: [engineering]

  "Engineering-Leads":
    role: workspace_admin
    workspaces: [engineering]

  "Sales-Team":
    role: member
    workspaces: [sales]

  "External-Partners":
    role: guest
    workspaces: [partner-collab]
```

### JIT Provisioning
```yaml
# Just-in-Time User Creation

Settings:
  jit_provisioning: enabled
  default_role: member
  default_workspace: general
  require_email_domain: "@company.com"

Process:
  1. User signs in via SSO
  2. Account created automatically
  3. Groups evaluated
  4. Role assigned based on groups
  5. Access granted immediately
```