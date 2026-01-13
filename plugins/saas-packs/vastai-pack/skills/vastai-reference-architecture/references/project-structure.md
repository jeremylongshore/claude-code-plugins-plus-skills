# Project Structure

## Project Structure

```
my-vastai-project/
├── src/
│   ├── vastai/
│   │   ├── client.ts           # Singleton client wrapper
│   │   ├── config.ts           # Environment configuration
│   │   ├── types.ts            # TypeScript types
│   │   ├── errors.ts           # Custom error classes
│   │   └── handlers/
│   │       ├── webhooks.ts     # Webhook handlers
│   │       └── events.ts       # Event processing
│   ├── services/
│   │   └── vastai/
│   │       ├── index.ts        # Service facade
│   │       ├── sync.ts         # Data synchronization
│   │       └── cache.ts        # Caching layer
│   ├── api/
│   │   └── vastai/
│   │       └── webhook.ts      # Webhook endpoint
│   └── jobs/
│       └── vastai/
│           └── sync.ts         # Background sync job
├── tests/
│   ├── unit/
│   │   └── vastai/
│   └── integration/
│       └── vastai/
├── config/
│   ├── vastai.development.json
│   ├── vastai.staging.json
│   └── vastai.production.json
└── docs/
    └── vastai/
        ├── SETUP.md
        └── RUNBOOK.md
```