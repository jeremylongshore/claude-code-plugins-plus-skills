---
name: customerio-observability
description: |
  Set up customer.io monitoring and observability. use when implementing metrics, logging, alerting, or dashboards for customer.io integrations. trigger with phrases like "customer.io monitoring", "customer.io metrics", "customer.io dashboard", "cus...
allowed-tools: Read, Write, Edit, Bash(cmd:*)
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Customerio Observability

This skill provides automated assistance for customerio observability tasks.

## Prerequisites
- Customer.io integration deployed
- Monitoring infrastructure (Prometheus, Grafana, etc.)
- Log aggregation system


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Resources
- [Prometheus Best Practices](https://prometheus.io/docs/practices/)
- [OpenTelemetry Node.js](https://opentelemetry.io/docs/instrumentation/js/)