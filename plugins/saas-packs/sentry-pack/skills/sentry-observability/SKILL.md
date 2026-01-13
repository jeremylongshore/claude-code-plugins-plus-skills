---
name: sentry-observability
description: |
  Execute integrate sentry with observability stack. use when connecting sentry to logging, metrics, apm tools, or building unified observability dashboards. trigger with phrases like "sentry observability", "sentry logging integration", "sentry met...
allowed-tools: Read, Write, Edit, Grep
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Sentry Observability

This skill provides automated assistance for sentry observability tasks.

## Prerequisites

- Existing observability stack (logging, metrics, APM)
- Trace ID correlation strategy
- Dashboard platform (Grafana, Datadog, etc.)
- Alert routing defined

## Instructions

1. Integrate logging library to send errors to Sentry as breadcrumbs
2. Add request ID tags for log correlation in Sentry scope
3. Track custom metrics using Sentry setMeasurement in transactions
4. Correlate with Prometheus by adding sentry_event_id label
5. Add APM trace IDs to Sentry events in beforeSend hook
6. Enable OpenTelemetry integration for automatic trace correlation
7. Create Grafana dashboard panels using Sentry API data
8. Configure PagerDuty integration for alert escalation
9. Add context links (logs, APM) to Slack alert templates
10. Establish consistent trace ID tagging across all observability tools

## Output
- Sentry integrated with logging system
- Metrics correlated with error events
- Distributed traces connected across tools
- Unified observability dashboard

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [Sentry Integrations](https://docs.sentry.io/product/integrations/)
- [OpenTelemetry Integration](https://docs.sentry.io/platforms/javascript/performance/instrumentation/opentelemetry/)