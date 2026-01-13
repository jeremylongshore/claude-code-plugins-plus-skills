# Production Checklist

## Production Checklist

### 1. Authentication & Security
- [ ] Production API key obtained (not development key)
- [ ] API key stored in secret manager (not env file)
- [ ] Key rotation procedure documented and tested
- [ ] Minimum required scopes configured
- [ ] No secrets in source code or logs

```typescript
// Production client configuration
const gamma = new GammaClient({
  apiKey: await secretManager.getSecret('GAMMA_API_KEY'),
  timeout: 30000,
  retries: 3,
});
```

### 2. Error Handling
- [ ] All API calls wrapped in try/catch
- [ ] Exponential backoff for rate limits
- [ ] Graceful degradation for API outages
- [ ] User-friendly error messages
- [ ] Error tracking integration (Sentry, etc.)

```typescript
import * as Sentry from '@sentry/node';

try {
  await gamma.presentations.create({ ... });
} catch (err) {
  Sentry.captureException(err, {
    tags: { service: 'gamma', operation: 'create' },
  });
  throw new UserError('Unable to create presentation. Please try again.');
}
```

### 3. Performance
- [ ] Client instance reused (singleton pattern)
- [ ] Connection pooling enabled
- [ ] Appropriate timeouts configured
- [ ] Response caching where applicable
- [ ] Async operations for long tasks

### 4. Monitoring & Logging
- [ ] Request/response logging (sanitized)
- [ ] Latency metrics collection
- [ ] Error rate alerting
- [ ] Rate limit monitoring
- [ ] Health check endpoint

```typescript
// Health check
app.get('/health/gamma', async (req, res) => {
  try {
    await gamma.ping();
    res.json({ status: 'healthy', service: 'gamma' });
  } catch (err) {
    res.status(503).json({ status: 'unhealthy', error: err.message });
  }
});
```

### 5. Rate Limiting
- [ ] Rate limit tier confirmed with Gamma
- [ ] Request queuing implemented
- [ ] Backoff strategy in place
- [ ] Usage monitoring alerts
- [ ] Burst protection enabled

### 6. Data Handling
- [ ] PII handling compliant with policies
- [ ] Data retention policies documented
- [ ] Export data properly secured
- [ ] User consent for AI processing
- [ ] GDPR/CCPA compliance verified

### 7. Disaster Recovery
- [ ] Fallback behavior defined
- [ ] Circuit breaker implemented
- [ ] Recovery procedures documented
- [ ] Backup API key available
- [ ] Incident response plan ready

```typescript
import CircuitBreaker from 'opossum';

const breaker = new CircuitBreaker(
  (opts) => gamma.presentations.create(opts),
  {
    timeout: 30000,
    errorThresholdPercentage: 50,
    resetTimeout: 30000,
  }
);

breaker.fallback(() => ({
  error: 'Service temporarily unavailable',
  retry: true,
}));
```

### 8. Testing
- [ ] Integration tests passing
- [ ] Load testing completed
- [ ] Failure scenario testing done
- [ ] API mock for CI/CD
- [ ] Staging environment validated

### 9. Documentation
- [ ] API integration documented
- [ ] Runbooks for common issues
- [ ] Architecture diagrams updated
- [ ] On-call procedures defined
- [ ] Team trained on Gamma features