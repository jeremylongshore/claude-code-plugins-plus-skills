# Examples

### Quick Layer Test
```bash
# Test each layer in sequence
curl -v https://api.windsurf.com/health 2>&1 | grep -E "(Connected|TLS|HTTP)"
```