# Examples

### Alert Configuration
```yaml
# alerts/lindy.yml
groups:
  - name: lindy
    rules:
      - alert: LindyHighErrorRate
        expr: rate(lindy_agent_runs_total{status="error"}[5m]) > 0.1
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: "High Lindy error rate"

      - alert: LindyHighLatency
        expr: histogram_quantile(0.95, rate(lindy_agent_duration_ms_bucket[5m])) > 10000
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "Lindy P95 latency above 10s"
```