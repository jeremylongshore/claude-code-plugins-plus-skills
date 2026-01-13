# Project Structure

## Project Structure

```
my-ideogram-project/
├── src/
│   ├── ideogram/
│   │   ├── client.ts           # Singleton client wrapper
│   │   ├── config.ts           # Environment configuration
│   │   ├── types.ts            # TypeScript types
│   │   ├── errors.ts           # Custom error classes
│   │   └── handlers/
│   │       ├── webhooks.ts     # Webhook handlers
│   │       └── events.ts       # Event processing
│   ├── services/
│   │   └── ideogram/
│   │       ├── index.ts        # Service facade
│   │       ├── sync.ts         # Data synchronization
│   │       └── cache.ts        # Caching layer
│   ├── api/
│   │   └── ideogram/
│   │       └── webhook.ts      # Webhook endpoint
│   └── jobs/
│       └── ideogram/
│           └── sync.ts         # Background sync job
├── tests/
│   ├── unit/
│   │   └── ideogram/
│   └── integration/
│       └── ideogram/
├── config/
│   ├── ideogram.development.json
│   ├── ideogram.staging.json
│   └── ideogram.production.json
└── docs/
    └── ideogram/
        ├── SETUP.md
        └── RUNBOOK.md
```