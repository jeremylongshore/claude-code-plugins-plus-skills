# Customer.Io Incident Response Runbook

## Customer.io Incident Response Runbook

### P1: Complete API Outage
1. Check https://status.customer.io/
2. Verify credentials haven't expired
3. Test with curl directly
4. Enable circuit breaker if available
5. Queue events for retry
6. Notify stakeholders

### P2: High Error Rate (>5%)
1. Check error distribution by type
2. Identify affected operations
3. Review recent code deployments
4. Check for rate limiting
5. Scale down if self-inflicted

### P3: Delivery Issues
1. Check bounce/complaint rates
2. Review suppression list
3. Verify sender reputation
4. Check campaign configuration
5. Review segment conditions

### P4: Webhook Failures
1. Verify webhook secret
2. Check endpoint availability
3. Review payload format
4. Check for duplicate events
5. Verify idempotency handling
```