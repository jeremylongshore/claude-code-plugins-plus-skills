# Daily Health Check

## Daily Health Check

Automated Monitoring:
- [ ] Granola status page: status.granola.ai
- [ ] Integration connectivity
- [ ] Processing latency
- [ ] Error rate

Manual Weekly Check:
- [ ] User adoption trending up
- [ ] Transcription quality stable
- [ ] Action items being captured
- [ ] Integrations firing correctly
```

### Alerting Rules
```yaml
# PagerDuty/Slack Alerts

Alerts:
  - name: Processing Failure Spike
    condition: error_rate > 5%
    window: 15 minutes
    severity: warning
    notify: #ops-alerts

  - name: Integration Down
    condition: integration_health != "healthy"
    window: 5 minutes
    severity: critical
    notify: pagerduty

  - name: Low Adoption
    condition: weekly_active_users < 50%
    window: 7 days
    severity: info
    notify: #product-team
```