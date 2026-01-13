# Diagnostic Commands

## Diagnostic Commands

### Test API Connection
```bash
curl -s -H "Authorization: $LINEAR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "{ viewer { name email } }"}' \
  https://api.linear.app/graphql | jq
```

### Check Rate Limit Status
```bash
curl -I -H "Authorization: $LINEAR_API_KEY" \
  https://api.linear.app/graphql
# Look for: X-RateLimit-Limit, X-RateLimit-Remaining
```

### Validate Webhook Signature
```typescript
import crypto from "crypto";

function verifyWebhookSignature(
  body: string,
  signature: string,
  secret: string
): boolean {
  const hmac = crypto.createHmac("sha256", secret);
  const digest = hmac.update(body).digest("hex");
  return crypto.timingSafeEqual(
    Buffer.from(signature),
    Buffer.from(digest)
  );
}
```