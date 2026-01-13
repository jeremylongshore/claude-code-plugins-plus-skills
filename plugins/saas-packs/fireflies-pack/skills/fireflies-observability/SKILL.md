---
allowed-tools: Read, Write, Edit
license: MIT
description: Set up comprehensive observability for fireflies.ai integrations with
  metrics, traces, and alerts. use when implementing monitoring for fireflies.ai operations,
  setting up dashboards, or configuring alerting for fireflies.ai integration health.
  tr...
name: fireflies-observability
---
# Fireflies Observability

This skill provides automated assistance for fireflies observability tasks.

## Prerequisites
- Prometheus or compatible metrics backend
- OpenTelemetry SDK installed
- Grafana or similar dashboarding tool
- AlertManager configured

## Instructions

### Step 1: Set Up Metrics Collection
Implement Prometheus counters, histograms, and gauges for key operations.

### Step 2: Add Distributed Tracing
Integrate OpenTelemetry for end-to-end request tracing.

### Step 3: Configure Structured Logging
Set up JSON logging with consistent field names.

### Step 4: Create Alert Rules
Define Prometheus alerting rules for error rates and latency.

## Output
- Metrics collection enabled
- Distributed tracing configured
- Structured logging implemented
- Alert rules deployed

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [Prometheus Best Practices](https://prometheus.io/docs/practices/naming/)
- [OpenTelemetry Documentation](https://opentelemetry.io/docs/)
- [Fireflies.ai Observability Guide](https://docs.fireflies.com/observability)