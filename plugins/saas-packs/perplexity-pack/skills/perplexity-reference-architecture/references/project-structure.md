# Project Structure

## Project Structure

```
my-perplexity-project/
├── src/
│   ├── perplexity/
│   │   ├── client.ts           # Singleton client wrapper
│   │   ├── config.ts           # Environment configuration
│   │   ├── types.ts            # TypeScript types
│   │   ├── errors.ts           # Custom error classes
│   │   └── handlers/
│   │       ├── webhooks.ts     # Webhook handlers
│   │       └── events.ts       # Event processing
│   ├── services/
│   │   └── perplexity/
│   │       ├── index.ts        # Service facade
│   │       ├── sync.ts         # Data synchronization
│   │       └── cache.ts        # Caching layer
│   ├── api/
│   │   └── perplexity/
│   │       └── webhook.ts      # Webhook endpoint
│   └── jobs/
│       └── perplexity/
│           └── sync.ts         # Background sync job
├── tests/
│   ├── unit/
│   │   └── perplexity/
│   └── integration/
│       └── perplexity/
├── config/
│   ├── perplexity.development.json
│   ├── perplexity.staging.json
│   └── perplexity.production.json
└── docs/
    └── perplexity/
        ├── SETUP.md
        └── RUNBOOK.md
```