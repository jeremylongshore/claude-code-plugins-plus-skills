# Correct: Always Include Unsubscribe

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