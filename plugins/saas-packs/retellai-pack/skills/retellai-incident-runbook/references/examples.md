# Examples

### One-Line Health Check
```bash
curl -sf https://api.yourapp.com/health | jq '.services.retellai.status' || echo "UNHEALTHY"
```