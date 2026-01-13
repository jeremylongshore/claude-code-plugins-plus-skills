---
name: linear-observability
description: |
  Implement monitoring, logging, and alerting for linear integrations. use when setting up metrics collection, creating dashboards, or configuring alerts for linear api usage. trigger with phrases like "linear monitoring", "linear observability", "l...
allowed-tools: Read, Write, Edit, Grep
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Linear Observability

This skill provides automated assistance for linear observability tasks.

## Prerequisites
- Linear integration deployed
- Metrics infrastructure (Prometheus, Datadog, etc.)
- Logging infrastructure (ELK, CloudWatch, etc.)
- Alerting system configured


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Resources
- [Prometheus Client Library](https://github.com/siimon/prom-client)
- [Grafana Dashboards](https://grafana.com/docs/grafana/latest/dashboards/)
- [Pino Logger](https://getpino.io/)