# Grafana Dashboard

## Grafana Dashboard

```json
{
  "title": "Juicebox Integration",
  "panels": [
    {
      "title": "Request Rate",
      "type": "graph",
      "targets": [
        {
          "expr": "rate(juicebox_requests_total[5m])",
          "legendFormat": "{{operation}} - {{status}}"
        }
      ]
    },
    {
      "title": "Latency P95",
      "type": "graph",
      "targets": [
        {
          "expr": "histogram_quantile(0.95, rate(juicebox_request_duration_seconds_bucket[5m]))",
          "legendFormat": "{{operation}}"
        }
      ]
    },
    {
      "title": "Cache Hit Rate",
      "type": "stat",
      "targets": [
        {
          "expr": "rate(juicebox_cache_hits_total[5m]) / rate(juicebox_requests_total[5m])"
        }
      ]
    }
  ]
}
```