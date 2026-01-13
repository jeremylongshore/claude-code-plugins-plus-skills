# Provisioning Methods

## Provisioning Methods

Manual:
1. Settings > Members
2. Invite by email
3. Assign to workspace(s)
4. Set role

SSO/SCIM:
1. Configure SSO provider
2. Enable SCIM provisioning
3. Map groups to workspaces
4. Roles assigned by group

JIT (Just-in-Time):
1. Enable JIT provisioning
2. User signs in via SSO
3. Auto-added to default workspace
4. Upgrade as needed
```

### Role Definitions
| Role | Permissions | Use Case |
|------|------------|----------|
| Owner | Full admin + billing | Organization owner |
| Admin | Workspace management | Team leads |
| Member | Create + edit notes | Regular users |
| Viewer | Read only | Stakeholders |
| Guest | Single workspace | Contractors |

### Group Mappings
```yaml
# SSO Group → Granola Workspace Mapping

SSO Groups:
  engineering-team:
    workspace: Engineering
    role: member

  engineering-leads:
    workspace: Engineering
    role: admin

  sales-team:
    workspace: Sales
    role: member

  all-employees:
    workspace: General
    role: member
```