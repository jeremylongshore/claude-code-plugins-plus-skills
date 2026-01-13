---
name: lindy-observability
description: |
  Implement observability for lindy ai integrations. use when setting up monitoring, logging, tracing, or building dashboards for lindy operations. trigger with phrases like "lindy monitoring", "lindy observability", "lindy metrics", "lindy logging"...
allowed-tools: Read, Write, Edit
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Lindy Observability

This skill provides automated assistance for lindy observability tasks.

## Prerequisites
- Production Lindy integration
- Observability stack (Datadog, New Relic, Prometheus, etc.)
- Log aggregation system


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- Structured logging
- Prometheus metrics
- Distributed tracing
- Grafana dashboards
- Alerting rules

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [OpenTelemetry](https://opentelemetry.io/)
- [Prometheus](https://prometheus.io/)
- [Grafana](https://grafana.com/)