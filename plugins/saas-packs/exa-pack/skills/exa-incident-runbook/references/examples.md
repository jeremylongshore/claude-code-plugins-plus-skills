# Examples

### One-Line Health Check
```bash
curl -sf https://api.yourapp.com/health | jq '.services.exa.status' || echo "UNHEALTHY"
```