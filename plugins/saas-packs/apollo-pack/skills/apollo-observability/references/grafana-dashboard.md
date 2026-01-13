# Grafana Dashboard

## Grafana Dashboard

```json
{
  "dashboard": {
    "title": "Apollo.io Integration",
    "panels": [
      {
        "title": "Request Rate",
        "type": "graph",
        "targets": [
          {
            "expr": "sum(rate(apollo_requests_total[5m])) by (endpoint)",
            "legendFormat": "{{ endpoint }}"
          }
        ]
      },
      {
        "title": "Error Rate",
        "type": "graph",
        "targets": [
          {
            "expr": "sum(rate(apollo_errors_total[5m])) by (error_type)",
            "legendFormat": "{{ error_type }}"
          }
        ]
      },
      {
        "title": "Request Duration (P95)",
        "type": "graph",
        "targets": [
          {
            "expr": "histogram_quantile(0.95, rate(apollo_request_duration_seconds_bucket[5m]))",
            "legendFormat": "P95"
          }
        ]
      },
      {
        "title": "Rate Limit Status",
        "type": "gauge",
        "targets": [
          {
            "expr": "apollo_rate_limit_remaining",
            "legendFormat": "Remaining"
          }
        ],
        "thresholds": [
          { "value": 0, "color": "red" },
          { "value": 20, "color": "yellow" },
          { "value": 50, "color": "green" }
        ]
      },
      {
        "title": "Cache Hit Rate",
        "type": "stat",
        "targets": [
          {
            "expr": "sum(rate(apollo_cache_hits_total[5m])) / (sum(rate(apollo_cache_hits_total[5m])) + sum(rate(apollo_cache_misses_total[5m])))",
            "legendFormat": "Hit Rate"
          }
        ]
      },
      {
        "title": "Credits Used Today",
        "type": "stat",
        "targets": [
          {
            "expr": "increase(apollo_credits_used_total[24h])"
          }
        ]
      }
    ]
  }
}
```