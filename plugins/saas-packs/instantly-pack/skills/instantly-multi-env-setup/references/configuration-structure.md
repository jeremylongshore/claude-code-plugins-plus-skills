# Configuration Structure

## Configuration Structure

```
config/
├── instantly/
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
  "apiKey": "${INSTANTLY_API_KEY}",
  "baseUrl": "https://api-sandbox.instantly.com",
  "debug": true,
  "cache": {
    "enabled": false
  }
}
```

### staging.json
```json
{
  "apiKey": "${INSTANTLY_API_KEY_STAGING}",
  "baseUrl": "https://api-staging.instantly.com",
  "debug": false
}
```

### production.json
```json
{
  "apiKey": "${INSTANTLY_API_KEY_PROD}",
  "baseUrl": "https://api.instantly.com",
  "debug": false,
  "retries": 5
}
```