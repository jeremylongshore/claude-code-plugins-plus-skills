# Pitfall Categories

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