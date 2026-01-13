---
name: deepgram-incident-runbook
license: MIT
allowed-tools: Read, Write, Edit, Bash
description: Execute deepgram incident response procedures for production issues.
  use when handling deepgram outages, debugging production failures, or responding
  to service degradation. trigger with phrases like "deepgram incident", "deepgram
  outage", "deepgr...
---
# Deepgram Incident Runbook

## Overview
Standardized procedures for responding to Deepgram-related incidents in production.

## Quick Reference

| Resource | URL |
|----------|-----|
| Deepgram Status | https://status.deepgram.com |
| Deepgram Console | https://console.deepgram.com |
| Support | support@deepgram.com |
| Discord | https://discord.gg/deepgram |

## Incident Severity Levels

| Level | Definition | Response Time | Examples |
|-------|------------|---------------|----------|
| SEV1 | Complete outage | Immediate | All transcriptions failing |
| SEV2 | Major degradation | < 15 min | 50%+ error rate |
| SEV3 | Minor degradation | < 1 hour | Elevated latency |
| SEV4 | Minor issue | < 24 hours | Single feature affected |

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
## Incident: Deepgram Service Outage

**Status:** Investigating
**Severity:** SEV1
**Started:** [TIME]
**Impact:** All transcription services unavailable

### Summary
We are experiencing a complete outage of our transcription service due to
Deepgram API unavailability.

### Current Actions
- [ ] Verified Deepgram status page shows incident
- [ ] Contacted Deepgram support
- [ ] Activated fallback queueing
- [ ] Notified affected customers

### Next Update
In 15 minutes or when status changes.
```

### SEV2: Major Degradation

**Symptoms:**
- 50%+ error rate
- Intermittent failures
- Significantly elevated latency

**Investigation Steps:**
```typescript
// scripts/investigate-degradation.ts
import { createClient } from '@deepgram/sdk';
import { logger } from './logger';

async function investigateDegradation() {
  const client = createClient(process.env.DEEPGRAM_API_KEY!);
  const testUrls = [
    'https://static.deepgram.com/examples/nasa-podcast.wav',
    'https://your-test-audio.com/sample1.wav',
    'https://your-test-audio.com/sample2.wav',
  ];

  console.log('Testing transcription across multiple samples...\n');

  const results = await Promise.allSettled(
    testUrls.map(async (url) => {
      const startTime = Date.now();
      const { result, error } = await client.listen.prerecorded.transcribeUrl(
        { url },
        { model: 'nova-2' }
      );

      return {
        url,
        success: !error,
        latency: Date.now() - startTime,
        error: error?.message,
        requestId: result?.metadata?.request_id,
      };
    })
  );

  // Analyze results
  const successful = results.filter(r => r.status === 'fulfilled' && r.value.success);
  const failed = results.filter(r => r.status === 'rejected' || !r.value?.success);

  console.log(`Success: ${successful.length}/${results.length}`);
  console.log(`Failed: ${failed.length}/${results.length}`);

  if (failed.length > 0) {
    console.log('\nFailed requests:');
    failed.forEach(f => {
      if (f.status === 'fulfilled') {
        console.log(`  - ${f.value.url}: ${f.value.error}`);
      } else {
        console.log(`  - Exception: ${f.reason}`);
      }
    });
  }

  // Check if it's a specific model or feature
  console.log('\nTesting different models...');
  for (const model of ['nova-2', 'nova', 'base']) {
    const { error } = await client.listen.prerecorded.transcribeUrl(
      { url: testUrls[0] },
      { model }
    );
    console.log(`  ${model}: ${error ? 'FAIL' : 'OK'}`);
  }
}

investigateDegradation().catch(console.error);
```

**Mitigation Options:**
1. Reduce request rate
2. Disable non-critical features
3. Switch to simpler model
4. Enable request retries

### SEV3: Minor Degradation

**Symptoms:**
- Elevated latency (2-3x normal)
- Occasional timeouts
- Reduced throughput

**Actions:**
```typescript
// Enable graceful degradation
const gracefulConfig = {
  // Increase timeouts
  timeout: 60000, // 60s instead of 30s

  // Enable aggressive retry
  retryConfig: {
    maxRetries: 5,
    baseDelay: 2000,
    maxDelay: 30000,
  },

  // Use simpler model for faster processing
  model: 'nova', // Instead of nova-2

  // Disable expensive features
  features: {
    diarization: false,
    smartFormat: true, // Keep basic formatting
  },
};
```

### Post-Incident Review

```markdown
## Post-Incident Review: [INCIDENT-ID]

### Timeline
- **HH:MM** - First alert triggered
- **HH:MM** - Incident acknowledged
- **HH:MM** - Root cause identified
- **HH:MM** - Mitigation applied
- **HH:MM** - Service restored
- **HH:MM** - Incident resolved

### Root Cause
[Detailed explanation of what caused the incident]

### Impact
- Duration: X hours Y minutes
- Affected requests: N
- Failed transcriptions: N
- Revenue impact: $X

### What Went Well
- [List of things that worked]

### What Needs Improvement
- [List of areas for improvement]

### Action Items
| Item | Owner | Due Date |
|------|-------|----------|
| [Action] | [Name] | [Date] |

### Detection
- How was the incident detected?
- Could it have been detected earlier?

### Response
- Was the runbook followed?
- Were there gaps in the runbook?

### Prevention
- What changes will prevent recurrence?
- What monitoring needs to be added?
```

## Diagnostic Commands

### Check Current Status
```bash
# API connectivity
curl -s -w "\nStatus: %{http_code}\nTime: %{time_total}s\n" \
  -X GET 'https://api.deepgram.com/v1/projects' \
  -H "Authorization: Token $DEEPGRAM_API_KEY"

# Test transcription
curl -X POST 'https://api.deepgram.com/v1/listen?model=nova-2' \
  -H "Authorization: Token $DEEPGRAM_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://static.deepgram.com/examples/nasa-podcast.wav"}'
```

### Check Application Metrics
```bash
# Error rate
curl -s 'http://localhost:9090/api/v1/query?query=rate(deepgram_errors_total[5m])'

# Request latency
curl -s 'http://localhost:9090/api/v1/query?query=histogram_quantile(0.95,rate(deepgram_latency_bucket[5m]))'

# Active connections
curl -s 'http://localhost:9090/api/v1/query?query=deepgram_active_connections'
```

### Check Kubernetes Resources
```bash
# Pod status
kubectl get pods -l app=deepgram-service

# Recent logs
kubectl logs -l app=deepgram-service --tail=100

# Resource usage
kubectl top pods -l app=deepgram-service
```

## Escalation Contacts

| Level | Contact | When |
|-------|---------|------|
| L1 | On-call engineer | First response |
| L2 | Team lead | 15 min without resolution |
| L3 | Deepgram support | Confirmed Deepgram issue |
| L4 | Engineering director | SEV1 > 1 hour |

## Resources
- [Deepgram Status Page](https://status.deepgram.com)
- [Deepgram Support](https://developers.deepgram.com/support)
- [Internal Runbooks](https://wiki.example.com/deepgram)

## Next Steps
Proceed to `deepgram-data-handling` for data management best practices.
