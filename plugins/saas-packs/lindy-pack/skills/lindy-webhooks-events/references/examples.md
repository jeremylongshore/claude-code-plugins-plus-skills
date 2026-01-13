# Examples

### Async Processing Pattern
```typescript
router.post('/lindy', async (req, res) => {
  // Verify signature first
  if (!verifySignature(req)) {
    return res.status(401).send('Invalid');
  }

  // Acknowledge immediately
  res.status(200).send('OK');

  // Process asynchronously
  const event = JSON.parse(req.body);
  await queue.push('lindy-events', event);
});
```