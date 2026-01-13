# Examples

### One-Line Health Check
```bash
curl -sf https://api.yourapp.com/health | jq '.services.ideogram.status' || echo "UNHEALTHY"
```