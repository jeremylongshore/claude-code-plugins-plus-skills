---
allowed-tools: Read, Write, Edit, Bash
license: MIT
description: Configure Apollo.io multi-environment setup. Use when setting up development,
  staging, and production environments, or managing multiple Apollo configurations.
  Trigger with phrases like "apollo environments", "apollo staging", "apollo dev prod",
  "...
name: apollo-multi-env-setup
---
# Apollo Multi Env Setup

This skill provides automated assistance for apollo multi env setup tasks.

## Output
- Environment-specific configurations
- Kubernetes ConfigMaps and Secrets
- Environment-aware client
- Feature flags per environment
- Environment promotion scripts

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Resources
- [12-Factor App Configuration](https://12factor.net/config)
- [Kubernetes ConfigMaps](https://kubernetes.io/docs/concepts/configuration/configmap/)
- [External Secrets Operator](https://external-secrets.io/)