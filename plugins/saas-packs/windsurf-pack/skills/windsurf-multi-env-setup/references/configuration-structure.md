# Configuration Structure

## Configuration Structure

```
config/
├── windsurf/
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
  "apiKey": "${WINDSURF_API_KEY}",
  "baseUrl": "https://api-sandbox.windsurf.com",
  "debug": true,
  "cache": {
    "enabled": false
  }
}
```

### staging.json
```json
{
  "apiKey": "${WINDSURF_API_KEY_STAGING}",
  "baseUrl": "https://api-staging.windsurf.com",
  "debug": false
}
```

### production.json
```json
{
  "apiKey": "${WINDSURF_API_KEY_PROD}",
  "baseUrl": "https://api.windsurf.com",
  "debug": false,
  "retries": 5
}
```