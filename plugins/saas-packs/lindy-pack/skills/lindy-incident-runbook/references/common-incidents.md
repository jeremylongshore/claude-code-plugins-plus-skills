# Common Incidents

## Common Incidents

### Incident: Complete API Outage

**Symptoms:**
- All API calls failing
- 5xx errors from Lindy

**Runbook:**
```markdown
1. [ ] Check https://status.lindy.ai
2. [ ] Verify it's not a local network issue
3. [ ] Check if other services on same network work
4. [ ] Enable fallback mode if available
5. [ ] Notify stakeholders
6. [ ] Open support ticket with Lindy
7. [ ] Monitor status page for updates
```

**Fallback Code:**
```typescript
async function runWithFallback(agentId: string, input: string) {
  try {
    return await lindy.agents.run(agentId, { input });
  } catch (error: any) {
    if (error.status >= 500) {
      // Enable fallback mode
      return {
        output: 'Service temporarily unavailable. Please try again later.',
        fallback: true,
      };
    }
    throw error;
  }
}
```

### Incident: Rate Limiting

**Symptoms:**
- 429 errors
- "Rate limit exceeded" messages

**Runbook:**
```markdown
1. [ ] Check current usage in dashboard
2. [ ] Identify spike source (which agent/automation)
3. [ ] Reduce request rate or implement throttling
4. [ ] Consider upgrading plan if legitimate traffic
5. [ ] Implement request queuing
```

**Throttling Code:**
```typescript
const queue = new PQueue({ concurrency: 5, interval: 1000, intervalCap: 10 });

async function throttledRun(agentId: string, input: string) {
  return queue.add(() => lindy.agents.run(agentId, { input }));
}
```

### Incident: Agent Failures

**Symptoms:**
- Specific agent not responding
- Unexpected outputs
- Timeout errors

**Runbook:**
```markdown
1. [ ] Identify affected agent(s)
2. [ ] Check agent configuration hasn't changed
3. [ ] Review recent runs for patterns
4. [ ] Test with simple input
5. [ ] Check if tools are working
6. [ ] Rollback to previous version if needed
```

**Diagnostic Script:**
```typescript
async function diagnoseAgent(agentId: string) {
  const lindy = new Lindy({ apiKey: process.env.LINDY_API_KEY });

  // Get agent details
  const agent = await lindy.agents.get(agentId);
  console.log('Agent:', agent.name, agent.status);

  // Check recent runs
  const runs = await lindy.runs.list({ agentId, limit: 10 });
  const failures = runs.filter((r: any) => r.status === 'failed');
  console.log(`Failures: ${failures.length}/${runs.length}`);

  // Test run
  try {
    const test = await lindy.agents.run(agentId, { input: 'Hello' });
    console.log('Test run: SUCCESS');
  } catch (e: any) {
    console.log('Test run: FAILED -', e.message);
  }

  return { agent, runs, failures };
}
```

### Incident: High Latency

**Symptoms:**
- Response times > 10 seconds
- Timeouts increasing

**Runbook:**
```markdown
1. [ ] Check Lindy status page for degradation
2. [ ] Review latency metrics by agent
3. [ ] Check if issue is with specific agent
4. [ ] Verify instructions aren't causing long responses
5. [ ] Consider reducing max_tokens
6. [ ] Implement streaming if not already
```