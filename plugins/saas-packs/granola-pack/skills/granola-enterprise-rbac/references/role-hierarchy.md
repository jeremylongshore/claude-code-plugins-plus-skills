# Role Hierarchy

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