# Configuration Structure

## Configuration Structure

```
config/
├── perplexity/
│   ├── base.json           # Shared config
│   ├── development.json    # Dev overrides
│   ├── staging.json        # Staging overrides
│   └── production.json     # Prod overrides
```

### base.json
```json
{
  "timeout": 30000,
  "retries": 3,
  "cache": {
    "enabled": true,
    "ttlSeconds": 60
  }
}
```

### development.json
```json
{
  "apiKey": "${PERPLEXITY_API_KEY}",
  "baseUrl": "https://api-sandbox.perplexity.com",
  "debug": true,
  "cache": {
    "enabled": false
  }
}
```

### staging.json
```json
{
  "apiKey": "${PERPLEXITY_API_KEY_STAGING}",
  "baseUrl": "https://api-staging.perplexity.com",
  "debug": false
}
```

### production.json
```json
{
  "apiKey": "${PERPLEXITY_API_KEY_PROD}",
  "baseUrl": "https://api.perplexity.com",
  "debug": false,
  "retries": 5
}
```