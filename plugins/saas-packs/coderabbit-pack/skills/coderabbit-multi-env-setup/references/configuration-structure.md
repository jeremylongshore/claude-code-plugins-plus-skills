# Configuration Structure

## Configuration Structure

```
config/
├── coderabbit/
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
  "apiKey": "${CODERABBIT_API_KEY}",
  "baseUrl": "https://api-sandbox.coderabbit.com",
  "debug": true,
  "cache": {
    "enabled": false
  }
}
```

### staging.json
```json
{
  "apiKey": "${CODERABBIT_API_KEY_STAGING}",
  "baseUrl": "https://api-staging.coderabbit.com",
  "debug": false
}
```

### production.json
```json
{
  "apiKey": "${CODERABBIT_API_KEY_PROD}",
  "baseUrl": "https://api.coderabbit.com",
  "debug": false,
  "retries": 5
}
```