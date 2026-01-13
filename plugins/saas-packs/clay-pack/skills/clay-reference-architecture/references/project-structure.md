# Project Structure

## Project Structure

```
my-clay-project/
├── src/
│   ├── clay/
│   │   ├── client.ts           # Singleton client wrapper
│   │   ├── config.ts           # Environment configuration
│   │   ├── types.ts            # TypeScript types
│   │   ├── errors.ts           # Custom error classes
│   │   └── handlers/
│   │       ├── webhooks.ts     # Webhook handlers
│   │       └── events.ts       # Event processing
│   ├── services/
│   │   └── clay/
│   │       ├── index.ts        # Service facade
│   │       ├── sync.ts         # Data synchronization
│   │       └── cache.ts        # Caching layer
│   ├── api/
│   │   └── clay/
│   │       └── webhook.ts      # Webhook endpoint
│   └── jobs/
│       └── clay/
│           └── sync.ts         # Background sync job
├── tests/
│   ├── unit/
│   │   └── clay/
│   └── integration/
│       └── clay/
├── config/
│   ├── clay.development.json
│   ├── clay.staging.json
│   └── clay.production.json
└── docs/
    └── clay/
        ├── SETUP.md
        └── RUNBOOK.md
```