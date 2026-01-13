# Examples

### Testing Webhooks Locally
```bash
# Use ngrok to expose local server
ngrok http 3000

# Send test webhook
curl -X POST https://your-ngrok-url/webhooks/posthog \
  -H "Content-Type: application/json" \
  -d '{"type": "test", "data": {}}'
```