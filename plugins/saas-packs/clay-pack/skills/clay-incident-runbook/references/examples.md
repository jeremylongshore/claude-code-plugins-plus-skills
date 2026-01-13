# Examples

### One-Line Health Check
```bash
curl -sf https://api.yourapp.com/health | jq '.services.clay.status' || echo "UNHEALTHY"
```