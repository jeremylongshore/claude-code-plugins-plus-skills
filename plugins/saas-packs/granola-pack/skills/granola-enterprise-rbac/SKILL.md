---
name: granola-enterprise-rbac
license: MIT
allowed-tools: Read, Write, Edit
description: Enterprise role-based access control for granola. use when configuring
  user roles, setting permissions, or implementing access control policies. trigger
  with phrases like "granola roles", "granola permissions", "granola access control",
  "granola r...
---
# Granola Enterprise RBAC

## Overview
Configure enterprise role-based access control for Granola meeting notes.

## Prerequisites
- Granola Business or Enterprise plan
- Organization admin access
- SSO configured (recommended)
- Security policy defined

## Role Hierarchy

### Built-in Roles
```
Organization Owner (Super Admin)
        ↓
Organization Admin
        ↓
Workspace Admin
        ↓
Team Lead
        ↓
Member
        ↓
Viewer
        ↓
Guest (External)
```

### Role Definitions

#### Organization Owner
```yaml
Role: Organization Owner
Level: Super Admin
Scope: Entire organization

Permissions:
  billing: full
  organization_settings: full
  workspace_management: full
  user_management: full
  data_export: full
  audit_logs: read
  integrations: full
  sso_configuration: full

Limits:
  max_per_org: 1-3
  cannot_be_removed: by other admins
```

#### Organization Admin
```yaml
Role: Organization Admin
Level: High
Scope: Entire organization

Permissions:
  billing: read
  organization_settings: read_write
  workspace_management: full
  user_management: full
  data_export: full
  audit_logs: read
  integrations: full
  sso_configuration: read

Limits:
  max_per_org: unlimited
  assigned_by: org_owner
```

#### Workspace Admin
```yaml
Role: Workspace Admin
Level: Medium-High
Scope: Assigned workspace(s)

Permissions:
  workspace_settings: full
  member_management: full
  templates: full
  integrations: workspace_only
  data_export: workspace_only
  sharing_controls: full

Limits:
  scope: specific workspaces
  assigned_by: org_admin
```

#### Team Lead
```yaml
Role: Team Lead
Level: Medium
Scope: Assigned team(s)

Permissions:
  team_members: manage
  templates: create_edit
  notes: team_visibility
  sharing: within_org
  reports: team_only

Limits:
  cannot: modify workspace settings
  cannot: manage other teams
```

#### Member
```yaml
Role: Member
Level: Standard
Scope: Own notes + shared

Permissions:
  notes: create_edit_own
  sharing: as_configured
  templates: use
  export: own_notes
  integrations: use_configured

Limits:
  cannot: manage users
  cannot: modify settings
```

#### Viewer
```yaml
Role: Viewer
Level: Low
Scope: Shared notes only

Permissions:
  notes: read_shared
  sharing: none
  templates: none
  export: none

Limits:
  read_only: true
  cannot: create notes
```

#### Guest
```yaml
Role: Guest
Level: External
Scope: Specific shared content

Permissions:
  notes: read_specific
  sharing: none
  time_limited: yes
  workspace_access: none

Limits:
  requires: explicit invite
  expires: configurable
```

## Permission Matrix

### Note Permissions
| Action | Owner | Admin | Lead | Member | Viewer | Guest |
|--------|-------|-------|------|--------|--------|-------|
| Create | Yes | Yes | Yes | Yes | No | No |
| Edit Own | Yes | Yes | Yes | Yes | No | No |
| Edit Others | Yes | Yes | Team | No | No | No |
| Delete Own | Yes | Yes | Yes | Yes | No | No |
| Delete Others | Yes | Yes | No | No | No | No |
| View All | Yes | Yes | Team | Shared | Shared | Specific |

### Sharing Permissions
| Action | Owner | Admin | Lead | Member | Viewer |
|--------|-------|-------|------|--------|--------|
| Share Internal | Yes | Yes | Yes | Config | No |
| Share External | Yes | Yes | Config | No | No |
| Public Links | Yes | Config | No | No | No |
| Revoke Access | Yes | Yes | Team | Own | No |

### Admin Permissions
| Action | Org Owner | Org Admin | WS Admin | Lead | Member |
|--------|-----------|-----------|----------|------|--------|
| Manage Billing | Yes | View | No | No | No |
| SSO Config | Yes | View | No | No | No |
| Create Workspace | Yes | Yes | No | No | No |
| Delete Workspace | Yes | Yes | No | No | No |
| Manage Users | Yes | Yes | WS Only | Team | No |
| View Audit Logs | Yes | Yes | WS Only | No | No |

## Configuration

### Assign Roles
```markdown
## Role Assignment

Via Admin Panel:
1. Settings > Users
2. Find user
3. Click "Edit Role"
4. Select role
5. Choose workspace scope (if applicable)
6. Save changes

Via SSO Group Mapping:
1. Settings > SSO > Group Mapping
2. Map SSO group to Granola role
3. Set default workspace
4. Enable auto-provisioning
```

### Custom Roles (Enterprise)
```yaml
# Custom Role Definition
Role: Content Manager
Base: Member
Scope: Marketing Workspace

Additional Permissions:
  templates: create_edit_delete
  shared_notes: edit_all
  external_sharing: enabled
  analytics: workspace_view

Restrictions:
  cannot: delete_others_notes
  cannot: manage_users
```

### Role Inheritance
```markdown
## Inheritance Rules

1. Workspace role inherits org permissions
2. Higher role can access lower role data
3. Explicit deny overrides inheritance
4. Guest role has no inheritance

Example:
- User is Org Admin → auto Workspace Admin everywhere
- User is Team Lead in Eng → Member elsewhere
```

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

## Access Policies

### Sharing Policy
```yaml
# Organization Sharing Policy

Internal Sharing:
  default: enabled
  team_sharing: automatic
  cross_workspace: admin_approval

External Sharing:
  enabled: true
  require_approval: workspace_admin
  link_expiration: 30_days
  password_protection: optional

Public Links:
  enabled: false  # Disabled for security
```

### Data Access Policy
```yaml
# Data Access Restrictions

By Workspace:
  Corporate:
    visibility: owners_only
    download: disabled
    external: prohibited

  Engineering:
    visibility: workspace
    download: enabled
    external: with_approval

  Sales:
    visibility: workspace
    download: enabled
    external: enabled
    crm_sync: automatic
```

## Audit & Compliance

### Role Change Auditing
```markdown
## Audit Events

Logged Actions:
- Role assigned
- Role removed
- Permission changed
- Workspace access granted
- Workspace access revoked
- Guest invited
- Guest expired

Log Format:
{
  "timestamp": "2025-01-06T15:00:00Z",
  "actor": "admin@company.com",
  "action": "role_changed",
  "target": "user@company.com",
  "old_role": "member",
  "new_role": "team_lead",
  "workspace": "engineering"
}
```

### Access Review
```markdown
## Quarterly Access Review

Checklist:
- [ ] Export user role report
- [ ] Review admin access
- [ ] Check guest accounts
- [ ] Verify workspace assignments
- [ ] Remove inactive users
- [ ] Update role mappings
- [ ] Document changes
```

## Best Practices

### Principle of Least Privilege
```markdown
## Access Guidelines

1. Start with Viewer role
2. Upgrade as needed
3. Use workspace-specific roles
4. Review access quarterly
5. Remove access promptly when role changes

Anti-patterns:
✗ Everyone as Admin
✗ Permanent guest access
✗ Unused workspace admin rights
✗ Orphaned accounts
```

### Role Lifecycle
```markdown
## User Lifecycle

Onboarding:
1. Create via SSO/JIT
2. Assign default role
3. Add to relevant workspaces
4. Provide training

Role Change:
1. Request from manager
2. Approve by workspace admin
3. Update role
4. Verify access

Offboarding:
1. Triggered by HR system
2. Disable account
3. Revoke all access
4. Transfer note ownership
5. Archive after 30 days
```

## Resources
- [Granola Admin Guide](https://granola.ai/admin)
- [SSO Configuration](https://granola.ai/help/sso)
- [Security Best Practices](https://granola.ai/security)

## Next Steps
Proceed to `granola-migration-deep-dive` for migration from other tools.
