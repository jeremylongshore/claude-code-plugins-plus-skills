# Incident Response Procedures

## Incident Response Procedures

### Initial Triage (First 5 Minutes)

```bash
#!/bin/bash
# scripts/triage.sh - Quick assessment script

echo "=== Deepgram Incident Triage ==="
echo "Timestamp: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
echo ""

# 1. Check Deepgram status page
echo "1. Checking Deepgram Status..."
curl -s https://status.deepgram.com/api/v2/status.json | jq '.status.indicator'

# 2. Check our error rate
echo ""
echo "2. Recent Error Rate (last 5 min)..."
curl -s http://localhost:9090/api/v1/query \
  --data-urlencode 'query=sum(rate(deepgram_transcription_requests_total{status="error"}[5m]))/sum(rate(deepgram_transcription_requests_total[5m]))' \
  | jq '.data.result[0].value[1]'

# 3. Check latency
echo ""
echo "3. P95 Latency (last 5 min)..."
curl -s http://localhost:9090/api/v1/query \
  --data-urlencode 'query=histogram_quantile(0.95,sum(rate(deepgram_transcription_latency_seconds_bucket[5m]))by(le))' \
  | jq '.data.result[0].value[1]'

# 4. Quick connectivity test
echo ""
echo "4. API Connectivity Test..."
curl -s -o /dev/null -w "Status: %{http_code}, Time: %{time_total}s\n" \
  -X GET 'https://api.deepgram.com/v1/projects' \
  -H "Authorization: Token $DEEPGRAM_API_KEY"
```

### SEV1: Complete Outage

**Symptoms:**
- 100% transcription failure
- API returning 5xx errors
- Complete service unavailability

**Immediate Actions:**
1. Acknowledge incident in PagerDuty/Slack
2. Check Deepgram status page
3. Verify API key is valid
4. Check network connectivity
5. Activate fallback if available

```typescript
// Fallback activation
import { FallbackManager } from './fallback';

const fallback = new FallbackManager();

// Activate fallback mode
await fallback.activate({
  reason: 'SEV1: Deepgram API outage',
  mode: 'queue', // Queue requests for later
  notifyUsers: true,
});

// Or switch to backup provider
await fallback.switchProvider('backup-stt-provider');
```

**Communication Template:**
```markdown