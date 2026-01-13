# Project Structure

## Project Structure

```
my-windsurf-project/
├── src/
│   ├── windsurf/
│   │   ├── client.ts           # Singleton client wrapper
│   │   ├── config.ts           # Environment configuration
│   │   ├── types.ts            # TypeScript types
│   │   ├── errors.ts           # Custom error classes
│   │   └── handlers/
│   │       ├── webhooks.ts     # Webhook handlers
│   │       └── events.ts       # Event processing
│   ├── services/
│   │   └── windsurf/
│   │       ├── index.ts        # Service facade
│   │       ├── sync.ts         # Data synchronization
│   │       └── cache.ts        # Caching layer
│   ├── api/
│   │   └── windsurf/
│   │       └── webhook.ts      # Webhook endpoint
│   └── jobs/
│       └── windsurf/
│           └── sync.ts         # Background sync job
├── tests/
│   ├── unit/
│   │   └── windsurf/
│   └── integration/
│       └── windsurf/
├── config/
│   ├── windsurf.development.json
│   ├── windsurf.staging.json
│   └── windsurf.production.json
└── docs/
    └── windsurf/
        ├── SETUP.md
        └── RUNBOOK.md
```