# Examples

### One-Line Health Check
```bash
curl -sf https://api.yourapp.com/health | jq '.services.coderabbit.status' || echo "UNHEALTHY"
```