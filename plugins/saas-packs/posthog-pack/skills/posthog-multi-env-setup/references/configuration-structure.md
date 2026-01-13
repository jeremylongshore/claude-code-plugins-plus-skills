# Configuration Structure

## Configuration Structure

```
config/
├── posthog/
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
  "apiKey": "${POSTHOG_API_KEY}",
  "baseUrl": "https://api-sandbox.posthog.com",
  "debug": true,
  "cache": {
    "enabled": false
  }
}
```

### staging.json
```json
{
  "apiKey": "${POSTHOG_API_KEY_STAGING}",
  "baseUrl": "https://api-staging.posthog.com",
  "debug": false
}
```

### production.json
```json
{
  "apiKey": "${POSTHOG_API_KEY_PROD}",
  "baseUrl": "https://api.posthog.com",
  "debug": false,
  "retries": 5
}
```