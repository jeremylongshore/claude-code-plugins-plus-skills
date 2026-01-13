# Role Assignment

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