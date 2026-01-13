---
name: langchain-multi-env-setup
description: |
  Configure LangChain multi-environment setup for dev/staging/prod. Use when managing multiple environments, configuring environment-specific settings, or implementing environment promotion workflows. Trigger with phrases like "langchain environment...
allowed-tools: Read, Write, Edit
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Langchain Multi Env Setup

This skill provides automated assistance for langchain multi env setup tasks.

## Prerequisites
- LangChain application ready for deployment
- Access to multiple deployment environments
- Secrets management solution (e.g., GCP Secret Manager)


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- Multi-environment configuration structure
- Environment-aware configuration loader
- Secrets management per environment
- Docker Compose for local development

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [Pydantic Settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/)
- [GCP Secret Manager](https://cloud.google.com/secret-manager/docs)
- [12-Factor App Config](https://12factor.net/config)