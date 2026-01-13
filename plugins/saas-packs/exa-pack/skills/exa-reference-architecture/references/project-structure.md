# Project Structure

## Project Structure

```
my-exa-project/
├── src/
│   ├── exa/
│   │   ├── client.ts           # Singleton client wrapper
│   │   ├── config.ts           # Environment configuration
│   │   ├── types.ts            # TypeScript types
│   │   ├── errors.ts           # Custom error classes
│   │   └── handlers/
│   │       ├── webhooks.ts     # Webhook handlers
│   │       └── events.ts       # Event processing
│   ├── services/
│   │   └── exa/
│   │       ├── index.ts        # Service facade
│   │       ├── sync.ts         # Data synchronization
│   │       └── cache.ts        # Caching layer
│   ├── api/
│   │   └── exa/
│   │       └── webhook.ts      # Webhook endpoint
│   └── jobs/
│       └── exa/
│           └── sync.ts         # Background sync job
├── tests/
│   ├── unit/
│   │   └── exa/
│   └── integration/
│       └── exa/
├── config/
│   ├── exa.development.json
│   ├── exa.staging.json
│   └── exa.production.json
└── docs/
    └── exa/
        ├── SETUP.md
        └── RUNBOOK.md
```