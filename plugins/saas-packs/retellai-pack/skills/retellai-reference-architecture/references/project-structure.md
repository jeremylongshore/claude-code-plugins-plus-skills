# Project Structure

## Project Structure

```
my-retellai-project/
├── src/
│   ├── retellai/
│   │   ├── client.ts           # Singleton client wrapper
│   │   ├── config.ts           # Environment configuration
│   │   ├── types.ts            # TypeScript types
│   │   ├── errors.ts           # Custom error classes
│   │   └── handlers/
│   │       ├── webhooks.ts     # Webhook handlers
│   │       └── events.ts       # Event processing
│   ├── services/
│   │   └── retellai/
│   │       ├── index.ts        # Service facade
│   │       ├── sync.ts         # Data synchronization
│   │       └── cache.ts        # Caching layer
│   ├── api/
│   │   └── retellai/
│   │       └── webhook.ts      # Webhook endpoint
│   └── jobs/
│       └── retellai/
│           └── sync.ts         # Background sync job
├── tests/
│   ├── unit/
│   │   └── retellai/
│   └── integration/
│       └── retellai/
├── config/
│   ├── retellai.development.json
│   ├── retellai.staging.json
│   └── retellai.production.json
└── docs/
    └── retellai/
        ├── SETUP.md
        └── RUNBOOK.md
```