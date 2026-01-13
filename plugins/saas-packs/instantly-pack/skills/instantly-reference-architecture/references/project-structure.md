# Project Structure

## Project Structure

```
my-instantly-project/
├── src/
│   ├── instantly/
│   │   ├── client.ts           # Singleton client wrapper
│   │   ├── config.ts           # Environment configuration
│   │   ├── types.ts            # TypeScript types
│   │   ├── errors.ts           # Custom error classes
│   │   └── handlers/
│   │       ├── webhooks.ts     # Webhook handlers
│   │       └── events.ts       # Event processing
│   ├── services/
│   │   └── instantly/
│   │       ├── index.ts        # Service facade
│   │       ├── sync.ts         # Data synchronization
│   │       └── cache.ts        # Caching layer
│   ├── api/
│   │   └── instantly/
│   │       └── webhook.ts      # Webhook endpoint
│   └── jobs/
│       └── instantly/
│           └── sync.ts         # Background sync job
├── tests/
│   ├── unit/
│   │   └── instantly/
│   └── integration/
│       └── instantly/
├── config/
│   ├── instantly.development.json
│   ├── instantly.staging.json
│   └── instantly.production.json
└── docs/
    └── instantly/
        ├── SETUP.md
        └── RUNBOOK.md
```