# Integration Per Environment

## Integration Per Environment

### Environment-Specific Integrations
```yaml
# Production Environment
Environment: Production

Workspaces:
  Sales:
    hubspot:
      portal_id: prod-12345
      sync: bidirectional
      auto_create: true
    slack:
      workspace: acme-corp
      channel: #sales-meetings

  Engineering:
    linear:
      team_id: ENG
      auto_tasks: true
    github:
      org: acme-corp
      repo_linking: true

# Staging Environment (for testing)
Environment: Staging

Workspaces:
  Test-Sales:
    hubspot:
      portal_id: sandbox-67890
      sync: unidirectional
      auto_create: false
```

### Integration Testing
```markdown