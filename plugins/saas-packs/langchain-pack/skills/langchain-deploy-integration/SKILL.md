---
allowed-tools: Read, Write, Edit, Bash
license: MIT
description: Deploy LangChain integrations to production environments. Use when deploying
  to cloud platforms, configuring containers, or setting up production infrastructure
  for LangChain apps. Trigger with phrases like "deploy langchain", "langchain productio...
name: langchain-deploy-integration
---
# Langchain Deploy Integration

This skill provides automated assistance for langchain deploy integration tasks.

## Prerequisites
- LangChain application ready for production
- Docker installed
- Cloud provider account (GCP, AWS, or Azure)
- API keys stored in secrets manager


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- Production-ready Dockerfile with multi-stage build
- FastAPI application with health checks
- Cloud Run deployment configuration
- Kubernetes manifests with autoscaling

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [Cloud Run Documentation](https://cloud.google.com/run/docs)
- [Kubernetes Best Practices](https://kubernetes.io/docs/concepts/configuration/overview/)
- [Docker Multi-stage Builds](https://docs.docker.com/build/building/multi-stage/)