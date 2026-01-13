# Pre-Deployment Checklist

## Pre-Deployment Checklist

### 1. API Configuration
```bash
# Verify production API key
echo "Key length: $(echo -n $APOLLO_API_KEY | wc -c)"
echo "Key prefix: ${APOLLO_API_KEY:0:8}..."

# Test API connectivity
curl -s "https://api.apollo.io/v1/auth/health?api_key=$APOLLO_API_KEY" | jq
```

- [ ] Production API key configured
- [ ] API key stored in secure secrets manager
- [ ] API key has appropriate permissions
- [ ] Backup/secondary key configured

### 2. Error Handling
```typescript
// Verify error handlers are in place
const requiredHandlers = [
  'ApolloAuthError',
  'ApolloRateLimitError',
  'ApolloValidationError',
  'ApolloServerError',
];

// Check each handler exists and is tested
```

- [ ] All error types handled
- [ ] Error logging configured
- [ ] Alert thresholds set
- [ ] Fallback behavior defined

### 3. Rate Limiting
```typescript
// Verify rate limit configuration
const config = {
  maxRequestsPerMinute: 90, // Buffer below 100
  retryConfig: {
    maxRetries: 3,
    initialDelay: 1000,
    maxDelay: 60000,
  },
  queueConcurrency: 5,
};
```

- [ ] Rate limiter implemented
- [ ] Exponential backoff configured
- [ ] Request queue with concurrency limits
- [ ] Rate limit monitoring enabled

### 4. Security
- [ ] API keys not in code
- [ ] .env files in .gitignore
- [ ] HTTPS only
- [ ] PII redaction in logs
- [ ] Data retention policy implemented

### 5. Monitoring
- [ ] Request/response logging
- [ ] Error rate alerts
- [ ] Latency monitoring
- [ ] Rate limit utilization tracking
- [ ] Health check endpoint