---
name: juicebox-observability
description: |
  Set up juicebox monitoring and observability. use when implementing logging, metrics, tracing, or alerting for juicebox integrations. trigger with phrases like "juicebox monitoring", "juicebox metrics", "juicebox logging", "juicebox observability".
allowed-tools: Read, Write, Edit, Bash(cmd:*)
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Juicebox Observability

This skill provides automated assistance for juicebox observability tasks.

## Prerequisites
- Observability platform (DataDog, Grafana, etc.)
- Juicebox integration running
- Access to deploy monitoring agents


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- Structured logging
- Prometheus metrics
- Distributed tracing
- Health checks
- Alerting rules

## Resources
- [Monitoring Guide](https://juicebox.ai/docs/monitoring)
- [OpenTelemetry](https://opentelemetry.io/)