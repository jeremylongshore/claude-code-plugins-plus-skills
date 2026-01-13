# Project Structure

## Project Structure

```
my-fireflies-project/
├── src/
│   ├── fireflies/
│   │   ├── client.ts           # Singleton client wrapper
│   │   ├── config.ts           # Environment configuration
│   │   ├── types.ts            # TypeScript types
│   │   ├── errors.ts           # Custom error classes
│   │   └── handlers/
│   │       ├── webhooks.ts     # Webhook handlers
│   │       └── events.ts       # Event processing
│   ├── services/
│   │   └── fireflies/
│   │       ├── index.ts        # Service facade
│   │       ├── sync.ts         # Data synchronization
│   │       └── cache.ts        # Caching layer
│   ├── api/
│   │   └── fireflies/
│   │       └── webhook.ts      # Webhook endpoint
│   └── jobs/
│       └── fireflies/
│           └── sync.ts         # Background sync job
├── tests/
│   ├── unit/
│   │   └── fireflies/
│   └── integration/
│       └── fireflies/
├── config/
│   ├── fireflies.development.json
│   ├── fireflies.staging.json
│   └── fireflies.production.json
└── docs/
    └── fireflies/
        ├── SETUP.md
        └── RUNBOOK.md
```