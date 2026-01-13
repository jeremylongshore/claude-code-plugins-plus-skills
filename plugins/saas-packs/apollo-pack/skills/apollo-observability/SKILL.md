---
allowed-tools: Read, Write, Edit, Bash
license: MIT
description: Set up apollo.io monitoring and observability. use when implementing
  logging, metrics, tracing, and alerting for apollo integrations. trigger with phrases
  like "apollo monitoring", "apollo metrics", "apollo observability", "apollo logging",
  "apoll...
name: apollo-observability
---
# Apollo Observability

This skill provides automated assistance for apollo observability tasks.

## Output
- Prometheus metrics for all Apollo operations
- Structured JSON logging with PII redaction
- OpenTelemetry distributed tracing
- Alerting rules for errors, rate limits, latency
- Grafana dashboard configuration
- Health check endpoints

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Resources
- [Prometheus Documentation](https://prometheus.io/docs/)
- [OpenTelemetry](https://opentelemetry.io/)
- [Grafana Dashboards](https://grafana.com/grafana/dashboards/)
- [Pino Logger](https://getpino.io/)