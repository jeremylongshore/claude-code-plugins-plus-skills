# Runbook: Webhook Failures

## Runbook: Webhook Failures

### Symptoms
- Events not being received
- Webhook signature validation failing
- Processing timeouts

### Diagnosis
```bash
# Check webhook endpoint is reachable
curl -I https://yourapp.com/api/webhooks/linear

# Check recent webhook logs
tail -100 /var/log/webhooks.log | grep linear

# Verify webhook secret
echo $LINEAR_WEBHOOK_SECRET | wc -c
# Should be > 20 characters
```

### Resolution Steps
1. **Verify endpoint health**
   ```typescript
   app.get("/api/webhooks/linear/health", (req, res) => {
     res.json({ status: "ok", timestamp: new Date().toISOString() });
   });
   ```

2. **Check signature verification**
   ```typescript
   // Debug signature verification
   function debugVerifySignature(payload: string, signature: string): boolean {
     const secret = process.env.LINEAR_WEBHOOK_SECRET!;
     const expected = crypto.createHmac("sha256", secret).update(payload).digest("hex");

     console.log("Debug: Received signature:", signature);
     console.log("Debug: Expected signature:", expected);
     console.log("Debug: Secret length:", secret.length);

     return signature === expected;
   }
   ```

3. **Recreate webhook if needed**
   - Go to Linear Settings > API > Webhooks
   - Delete existing webhook
   - Create new webhook with same URL
   - Update webhook secret in secrets manager