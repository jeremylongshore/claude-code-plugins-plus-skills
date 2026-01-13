---
name: langchain-observability
license: MIT
allowed-tools: Read, Write, Edit
description: Set up comprehensive observability for langchain integrations. use when
  implementing monitoring, setting up dashboards, or configuring alerting for langchain
  application health. trigger with phrases like "langchain monitoring", "langchain
  metrics"...
---
# LangChain Observability

## Overview
Set up comprehensive observability for LangChain applications with LangSmith, OpenTelemetry, and Prometheus.

## Prerequisites
- LangChain application in staging/production
- LangSmith account (optional but recommended)
- Prometheus/Grafana infrastructure
- OpenTelemetry collector (optional)

## Instructions

### Step 1: Enable LangSmith Tracing
```python
import os

# Configure LangSmith
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = "your-langsmith-api-key"
os.environ["LANGCHAIN_PROJECT"] = "my-production-app"

# Optional: Set endpoint for self-hosted
# os.environ["LANGCHAIN_ENDPOINT"] = "https://langsmith.example.com"

from langchain_openai import ChatOpenAI

# All chains are automatically traced
llm = ChatOpenAI(model="gpt-4o-mini")
response = llm.invoke("Hello!")  # Traced in LangSmith
```

### Step 2: Prometheus Metrics
```python
from prometheus_client import Counter, Histogram, Gauge, start_http_server
from langchain_core.callbacks import BaseCallbackHandler
import time

# Define metrics
LLM_REQUESTS = Counter(
    "langchain_llm_requests_total",
    "Total LLM requests",
    ["model", "status"]
)

LLM_LATENCY = Histogram(
    "langchain_llm_latency_seconds",
    "LLM request latency",
    ["model"],
    buckets=[0.1, 0.25, 0.5, 1.0, 2.5, 5.0, 10.0]
)

LLM_TOKENS = Counter(
    "langchain_llm_tokens_total",
    "Total tokens processed",
    ["model", "type"]  # type: input or output
)

ACTIVE_REQUESTS = Gauge(
    "langchain_active_requests",
    "Currently active LLM requests"
)

class PrometheusCallback(BaseCallbackHandler):
    """Export metrics to Prometheus."""

    def __init__(self):
        self.start_times = {}

    def on_llm_start(self, serialized, prompts, run_id, **kwargs) -> None:
        ACTIVE_REQUESTS.inc()
        self.start_times[str(run_id)] = time.time()

    def on_llm_end(self, response, run_id, **kwargs) -> None:
        ACTIVE_REQUESTS.dec()
        model = response.llm_output.get("model_name", "unknown") if response.llm_output else "unknown"

        # Record latency
        if str(run_id) in self.start_times:
            latency = time.time() - self.start_times.pop(str(run_id))
            LLM_LATENCY.labels(model=model).observe(latency)

        # Record success
        LLM_REQUESTS.labels(model=model, status="success").inc()

        # Record tokens
        if response.llm_output and "token_usage" in response.llm_output:
            usage = response.llm_output["token_usage"]
            LLM_TOKENS.labels(model=model, type="input").inc(usage.get("prompt_tokens", 0))
            LLM_TOKENS.labels(model=model, type="output").inc(usage.get("completion_tokens", 0))

    def on_llm_error(self, error, run_id, **kwargs) -> None:
        ACTIVE_REQUESTS.dec()
        LLM_REQUESTS.labels(model="unknown", status="error").inc()

# Start Prometheus HTTP server
start_http_server(9090)  # Metrics at http://localhost:9090/metrics
```

### Step 3: OpenTelemetry Integration
```python
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.httpx import HTTPXClientInstrumentor

# Configure OpenTelemetry
provider = TracerProvider()
processor = BatchSpanProcessor(OTLPSpanExporter(endpoint="http://localhost:4317"))
provider.add_span_processor(processor)
trace.set_tracer_provider(provider)

# Instrument HTTP client (used by LangChain)
HTTPXClientInstrumentor().instrument()

tracer = trace.get_tracer(__name__)

class OpenTelemetryCallback(BaseCallbackHandler):
    """Add OpenTelemetry spans for LangChain operations."""

    def __init__(self):
        self.spans = {}

    def on_chain_start(self, serialized, inputs, run_id, **kwargs) -> None:
        span = tracer.start_span(
            name=f"chain.{serialized.get('name', 'unknown')}",
            attributes={
                "langchain.chain_type": serialized.get("id", ["unknown"])[-1],
                "langchain.run_id": str(run_id),
            }
        )
        self.spans[str(run_id)] = span

    def on_chain_end(self, outputs, run_id, **kwargs) -> None:
        if str(run_id) in self.spans:
            span = self.spans.pop(str(run_id))
            span.set_attribute("langchain.output_keys", list(outputs.keys()))
            span.end()

    def on_llm_start(self, serialized, prompts, run_id, parent_run_id, **kwargs) -> None:
        parent_span = self.spans.get(str(parent_run_id))
        context = trace.set_span_in_context(parent_span) if parent_span else None

        span = tracer.start_span(
            name=f"llm.{serialized.get('name', 'unknown')}",
            context=context,
            attributes={
                "langchain.llm_type": serialized.get("id", ["unknown"])[-1],
                "langchain.prompt_count": len(prompts),
            }
        )
        self.spans[str(run_id)] = span

    def on_llm_end(self, response, run_id, **kwargs) -> None:
        if str(run_id) in self.spans:
            span = self.spans.pop(str(run_id))
            if response.llm_output and "token_usage" in response.llm_output:
                usage = response.llm_output["token_usage"]
                span.set_attribute("langchain.prompt_tokens", usage.get("prompt_tokens", 0))
                span.set_attribute("langchain.completion_tokens", usage.get("completion_tokens", 0))
            span.end()
```

### Step 4: Structured Logging
```python
import structlog
from datetime import datetime

# Configure structlog
structlog.configure(
    processors=[
        structlog.stdlib.filter_by_level,
        structlog.stdlib.add_logger_name,
        structlog.stdlib.add_log_level,
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.JSONRenderer()
    ],
    logger_factory=structlog.stdlib.LoggerFactory(),
)

logger = structlog.get_logger()

class StructuredLoggingCallback(BaseCallbackHandler):
    """Emit structured logs for LangChain operations."""

    def on_llm_start(self, serialized, prompts, run_id, **kwargs) -> None:
        logger.info(
            "llm_start",
            run_id=str(run_id),
            model=serialized.get("name"),
            prompt_count=len(prompts)
        )

    def on_llm_end(self, response, run_id, **kwargs) -> None:
        token_usage = {}
        if response.llm_output and "token_usage" in response.llm_output:
            token_usage = response.llm_output["token_usage"]

        logger.info(
            "llm_end",
            run_id=str(run_id),
            generations=len(response.generations),
            **token_usage
        )

    def on_llm_error(self, error, run_id, **kwargs) -> None:
        logger.error(
            "llm_error",
            run_id=str(run_id),
            error_type=type(error).__name__,
            error_message=str(error)
        )
```

### Step 5: Grafana Dashboard
```json
{
  "title": "LangChain Observability",
  "panels": [
    {
      "title": "Request Rate",
      "type": "graph",
      "targets": [
        {
          "expr": "rate(langchain_llm_requests_total[5m])",
          "legendFormat": "{{model}} - {{status}}"
        }
      ]
    },
    {
      "title": "Latency P95",
      "type": "graph",
      "targets": [
        {
          "expr": "histogram_quantile(0.95, rate(langchain_llm_latency_seconds_bucket[5m]))",
          "legendFormat": "{{model}}"
        }
      ]
    },
    {
      "title": "Token Usage",
      "type": "graph",
      "targets": [
        {
          "expr": "rate(langchain_llm_tokens_total[5m])",
          "legendFormat": "{{model}} - {{type}}"
        }
      ]
    },
    {
      "title": "Error Rate",
      "type": "singlestat",
      "targets": [
        {
          "expr": "sum(rate(langchain_llm_requests_total{status='error'}[5m])) / sum(rate(langchain_llm_requests_total[5m]))"
        }
      ]
    }
  ]
}
```

### Step 6: Alerting Rules
```yaml
# prometheus/alerts.yml
groups:
  - name: langchain
    rules:
      - alert: HighErrorRate
        expr: |
          sum(rate(langchain_llm_requests_total{status="error"}[5m]))
          / sum(rate(langchain_llm_requests_total[5m])) > 0.05
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: "High LLM error rate"
          description: "Error rate is {{ $value | humanizePercentage }}"

      - alert: HighLatency
        expr: |
          histogram_quantile(0.95, rate(langchain_llm_latency_seconds_bucket[5m])) > 5
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "High LLM latency"
          description: "P95 latency is {{ $value }}s"

      - alert: TokenBudgetExceeded
        expr: |
          sum(increase(langchain_llm_tokens_total[1h])) > 1000000
        labels:
          severity: warning
        annotations:
          summary: "High token usage"
          description: "Used {{ $value }} tokens in the last hour"
```

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

## Next Steps
Use `langchain-incident-runbook` for incident response procedures.
