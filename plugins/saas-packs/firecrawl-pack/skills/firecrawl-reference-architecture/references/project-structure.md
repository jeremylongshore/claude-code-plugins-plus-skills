# Project Structure

## Project Structure

```
my-firecrawl-project/
├── src/
│   ├── firecrawl/
│   │   ├── client.ts           # Singleton client wrapper
│   │   ├── config.ts           # Environment configuration
│   │   ├── types.ts            # TypeScript types
│   │   ├── errors.ts           # Custom error classes
│   │   └── handlers/
│   │       ├── webhooks.ts     # Webhook handlers
│   │       └── events.ts       # Event processing
│   ├── services/
│   │   └── firecrawl/
│   │       ├── index.ts        # Service facade
│   │       ├── sync.ts         # Data synchronization
│   │       └── cache.ts        # Caching layer
│   ├── api/
│   │   └── firecrawl/
│   │       └── webhook.ts      # Webhook endpoint
│   └── jobs/
│       └── firecrawl/
│           └── sync.ts         # Background sync job
├── tests/
│   ├── unit/
│   │   └── firecrawl/
│   └── integration/
│       └── firecrawl/
├── config/
│   ├── firecrawl.development.json
│   ├── firecrawl.staging.json
│   └── firecrawl.production.json
└── docs/
    └── firecrawl/
        ├── SETUP.md
        └── RUNBOOK.md
```