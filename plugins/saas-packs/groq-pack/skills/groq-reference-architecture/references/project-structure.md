# Project Structure

## Project Structure

```
my-groq-project/
├── src/
│   ├── groq/
│   │   ├── client.ts           # Singleton client wrapper
│   │   ├── config.ts           # Environment configuration
│   │   ├── types.ts            # TypeScript types
│   │   ├── errors.ts           # Custom error classes
│   │   └── handlers/
│   │       ├── webhooks.ts     # Webhook handlers
│   │       └── events.ts       # Event processing
│   ├── services/
│   │   └── groq/
│   │       ├── index.ts        # Service facade
│   │       ├── sync.ts         # Data synchronization
│   │       └── cache.ts        # Caching layer
│   ├── api/
│   │   └── groq/
│   │       └── webhook.ts      # Webhook endpoint
│   └── jobs/
│       └── groq/
│           └── sync.ts         # Background sync job
├── tests/
│   ├── unit/
│   │   └── groq/
│   └── integration/
│       └── groq/
├── config/
│   ├── groq.development.json
│   ├── groq.staging.json
│   └── groq.production.json
└── docs/
    └── groq/
        ├── SETUP.md
        └── RUNBOOK.md
```