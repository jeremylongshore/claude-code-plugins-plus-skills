---
name: customerio-known-pitfalls
license: MIT
allowed-tools: Read, Write, Edit, Bash
description: Identify and avoid customer.io anti-patterns. use when reviewing integrations,
  avoiding common mistakes, or optimizing existing customer.io implementations. trigger
  with phrases like "customer.io mistakes", "customer.io anti-patterns", "customer.i...
---
# Customer.io Known Pitfalls

## Overview
Avoid common mistakes and anti-patterns when integrating with Customer.io.

## Pitfall Categories

### 1. Authentication & Setup

#### Pitfall: Using App API key for Track API
```typescript
// WRONG: Using App API key for tracking
const client = new TrackClient(siteId, appApiKey); // Will fail!

// CORRECT: Use Track API key for tracking
const client = new TrackClient(siteId, trackApiKey);

// Use App API key only for transactional and reporting APIs
const apiClient = new APIClient(appApiKey);
```

#### Pitfall: Millisecond timestamps
```typescript
// WRONG: JavaScript milliseconds
{ created_at: Date.now() } // 1704067200000 - will be rejected!

// CORRECT: Unix seconds
{ created_at: Math.floor(Date.now() / 1000) } // 1704067200
```

#### Pitfall: Hardcoded credentials
```typescript
// WRONG: Credentials in code
const client = new TrackClient('abc123', 'secret-key'); // Security risk!

// CORRECT: Environment variables
const client = new TrackClient(
  process.env.CUSTOMERIO_SITE_ID!,
  process.env.CUSTOMERIO_API_KEY!
);
```

### 2. User Identification

#### Pitfall: Tracking events before identify
```typescript
// WRONG: Track before identify
await client.track(userId, { name: 'signup' }); // User doesn't exist!
await client.identify(userId, { email: 'user@example.com' });

// CORRECT: Always identify first
await client.identify(userId, { email: 'user@example.com' });
await client.track(userId, { name: 'signup' });
```

#### Pitfall: Changing user IDs
```typescript
// WRONG: User ID changes when email changes
const userId = user.email; // Changing email = new user!

// CORRECT: Use immutable identifier
const userId = user.databaseId; // UUIDs or auto-increment IDs
```

#### Pitfall: Anonymous ID not merged
```typescript
// WRONG: No anonymous_id linking
await client.identify(newUserId, { email: 'user@example.com' });
// Anonymous activity is orphaned!

// CORRECT: Include anonymous_id for merging
await client.identify(newUserId, {
  email: 'user@example.com',
  anonymous_id: previousAnonymousId
});
```

### 3. Event Tracking

#### Pitfall: Inconsistent event names
```typescript
// WRONG: Inconsistent casing and naming
await client.track(userId, { name: 'UserSignedUp' });
await client.track(userId, { name: 'user-signed-up' });
await client.track(userId, { name: 'user_signedup' });

// CORRECT: Consistent snake_case
await client.track(userId, { name: 'user_signed_up' });
```

#### Pitfall: Too many unique events
```typescript
// WRONG: Dynamic event names create clutter
await client.track(userId, { name: `viewed_product_${productId}` });
// Creates thousands of unique events!

// CORRECT: Use properties for variations
await client.track(userId, {
  name: 'product_viewed',
  data: { product_id: productId }
});
```

#### Pitfall: Blocking on analytics
```typescript
// WRONG: Waiting for analytics in request path
app.post('/signup', async (req, res) => {
  const user = await createUser(req.body);
  await client.identify(user.id, { email: user.email }); // Blocks!
  res.json({ user });
});

// CORRECT: Fire-and-forget
app.post('/signup', async (req, res) => {
  const user = await createUser(req.body);
  client.identify(user.id, { email: user.email })
    .catch(err => console.error('Customer.io error:', err));
  res.json({ user });
});
```

### 4. Data Quality

#### Pitfall: Missing required attributes
```typescript
// WRONG: No email attribute
await client.identify(userId, { name: 'John' });
// User can't receive emails!

// CORRECT: Always include email for email campaigns
await client.identify(userId, {
  email: 'john@example.com',
  name: 'John'
});
```

#### Pitfall: Inconsistent attribute types
```typescript
// WRONG: Sometimes string, sometimes number
await client.identify(userId1, { plan: 'premium' });
await client.identify(userId2, { plan: 1 });

// CORRECT: Consistent types
await client.identify(userId, { plan: 'premium' });
```

#### Pitfall: PII in segment names or event names
```typescript
// WRONG: PII exposed
await client.track(userId, { name: `email_${user.email}` });
// Creates segment: "email_john@example.com"

// CORRECT: Use attributes, not names
await client.track(userId, {
  name: 'email_action',
  data: { email: user.email }
});
```

### 5. Campaign Configuration

#### Pitfall: No unsubscribe handling
```markdown
## WRONG: No unsubscribe link
Email template without {{{ unsubscribe_url }}}

## CORRECT: Always include unsubscribe
<a href="{{{ unsubscribe_url }}}">Unsubscribe</a>
```

#### Pitfall: Trigger on every attribute update
```yaml
# WRONG: Trigger fires on every identify
trigger:
  event: "identify"

# CORRECT: Trigger on specific events
trigger:
  event: "signed_up"
```

### 6. Delivery Issues

#### Pitfall: Ignoring bounces
```typescript
// WRONG: No bounce handling
webhooks.on('email_bounced', () => {
  // Do nothing
});

// CORRECT: Suppress or update on bounce
webhooks.on('email_bounced', async (event) => {
  await client.suppress(event.data.customer_id);
  // Or mark email as invalid in your database
});
```

#### Pitfall: Not monitoring complaint rate
```typescript
// WRONG: Ignoring spam complaints
// Leads to deliverability issues!

// CORRECT: Alert on complaints
webhooks.on('email_complained', async (event) => {
  // Immediately suppress
  await client.suppress(event.data.customer_id);
  // Alert the team
  await alertTeam(`Spam complaint from ${event.data.email_address}`);
});
```

### 7. Performance Issues

#### Pitfall: No connection pooling
```typescript
// WRONG: New client per request
app.get('/api', async (req, res) => {
  const client = new TrackClient(siteId, apiKey); // Creates new connection!
  await client.identify(userId, data);
});

// CORRECT: Reuse client
const client = new TrackClient(siteId, apiKey);
app.get('/api', async (req, res) => {
  await client.identify(userId, data);
});
```

#### Pitfall: No rate limiting
```typescript
// WRONG: Uncontrolled burst
for (const user of users) {
  await client.identify(user.id, user.data); // 10k requests instantly!
}

// CORRECT: Rate limited
const limiter = new Bottleneck({ maxConcurrent: 10, minTime: 10 });
for (const user of users) {
  await limiter.schedule(() => client.identify(user.id, user.data));
}
```

## Anti-Pattern Detection Script

```typescript
// scripts/audit-integration.ts
interface AuditResult {
  issues: string[];
  warnings: string[];
  score: number;
}

async function auditIntegration(): Promise<AuditResult> {
  const result: AuditResult = { issues: [], warnings: [], score: 100 };

  // Check for hardcoded credentials
  const files = await glob('**/*.{ts,js}');
  for (const file of files) {
    const content = await readFile(file, 'utf-8');
    if (content.includes('site_') && content.includes('api_')) {
      result.issues.push(`Possible hardcoded credentials in ${file}`);
      result.score -= 20;
    }
  }

  // Check for millisecond timestamps
  if (await hasPattern(/Date\.now\(\)(?!\s*\/\s*1000)/)) {
    result.warnings.push('Possible millisecond timestamps detected');
    result.score -= 5;
  }

  // Check for track before identify pattern
  if (await hasPattern(/track\([^)]+\)[\s\S]{0,500}identify\(/)) {
    result.issues.push('Track before identify pattern detected');
    result.score -= 15;
  }

  return result;
}
```

## Quick Reference

| Pitfall | Fix |
|---------|-----|
| Wrong API key | Track API for tracking, App API for transactional |
| Milliseconds | Use `Math.floor(Date.now() / 1000)` |
| Track before identify | Always identify first |
| Changing user IDs | Use immutable database IDs |
| No email attribute | Include email for email campaigns |
| Dynamic event names | Use properties instead |
| Blocking requests | Fire-and-forget pattern |
| No bounce handling | Suppress on bounce |
| No rate limiting | Use Bottleneck or similar |

## Resources
- [Customer.io Best Practices](https://customer.io/docs/best-practices/)
- [Common Issues](https://customer.io/docs/troubleshooting/)

## Conclusion

Following these guidelines will help you avoid common pitfalls and build a reliable Customer.io integration. Regularly audit your implementation against this checklist to catch issues early.
