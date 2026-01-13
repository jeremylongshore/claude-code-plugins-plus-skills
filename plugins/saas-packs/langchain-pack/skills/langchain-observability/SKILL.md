---
allowed-tools: Read, Write, Edit
license: MIT
description: Set up comprehensive observability for langchain integrations. use when
  implementing monitoring, setting up dashboards, or configuring alerting for langchain
  application health. trigger with phrases like "langchain monitoring", "langchain
  metrics"...
name: langchain-observability
---
# Langchain Observability

This skill provides automated assistance for langchain observability tasks.

## Prerequisites
- LangChain application in staging/production
- LangSmith account (optional but recommended)
- Prometheus/Grafana infrastructure
- OpenTelemetry collector (optional)


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- LangSmith tracing enabled
- Prometheus metrics exported
- OpenTelemetry spans
- Structured logging
- Grafana dashboard and alerts

## Resources
- [LangSmith Documentation](https://docs.smith.langchain.com/)
- [OpenTelemetry Python](https://opentelemetry.io/docs/languages/python/)
- [Prometheus Python Client](https://prometheus.io/docs/instrumenting/clientlibs/)