# Production Checklist

## Production Checklist

### Authentication & Security
```markdown
[ ] Production API key generated
[ ] API key stored in secret manager (not env file)
[ ] Key rotation process documented
[ ] Different keys for each environment
[ ] Keys have appropriate scopes/permissions
[ ] Service accounts configured (not personal keys)
```

### Agent Configuration
```markdown
[ ] All agents tested with production-like data
[ ] Agent instructions reviewed and finalized
[ ] Tool permissions minimized (least privilege)
[ ] Timeout values appropriate for workloads
[ ] Error handling tested for all failure modes
[ ] Fallback behaviors defined
```

### Monitoring & Observability
```markdown
[ ] Logging configured and tested
[ ] Error alerting set up (PagerDuty/Slack/etc)
[ ] Usage metrics dashboards created
[ ] Rate limit alerts configured
[ ] Latency monitoring enabled
[ ] Cost tracking implemented
```

### Performance & Reliability
```markdown
[ ] Load testing completed
[ ] Rate limit handling implemented
[ ] Retry logic with exponential backoff
[ ] Circuit breaker pattern for failures
[ ] Graceful degradation defined
[ ] SLA targets documented
```

### Compliance & Documentation
```markdown
[ ] Data handling documented
[ ] Privacy review completed
[ ] Security review completed
[ ] Runbooks created for incidents
[ ] Escalation paths defined
[ ] On-call schedule set up
```