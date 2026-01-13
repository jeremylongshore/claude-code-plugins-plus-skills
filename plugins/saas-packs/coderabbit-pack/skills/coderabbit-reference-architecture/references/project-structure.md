# Project Structure

## Project Structure

```
my-coderabbit-project/
├── src/
│   ├── coderabbit/
│   │   ├── client.ts           # Singleton client wrapper
│   │   ├── config.ts           # Environment configuration
│   │   ├── types.ts            # TypeScript types
│   │   ├── errors.ts           # Custom error classes
│   │   └── handlers/
│   │       ├── webhooks.ts     # Webhook handlers
│   │       └── events.ts       # Event processing
│   ├── services/
│   │   └── coderabbit/
│   │       ├── index.ts        # Service facade
│   │       ├── sync.ts         # Data synchronization
│   │       └── cache.ts        # Caching layer
│   ├── api/
│   │   └── coderabbit/
│   │       └── webhook.ts      # Webhook endpoint
│   └── jobs/
│       └── coderabbit/
│           └── sync.ts         # Background sync job
├── tests/
│   ├── unit/
│   │   └── coderabbit/
│   └── integration/
│       └── coderabbit/
├── config/
│   ├── coderabbit.development.json
│   ├── coderabbit.staging.json
│   └── coderabbit.production.json
└── docs/
    └── coderabbit/
        ├── SETUP.md
        └── RUNBOOK.md
```