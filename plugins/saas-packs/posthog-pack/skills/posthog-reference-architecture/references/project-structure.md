# Project Structure

## Project Structure

```
my-posthog-project/
├── src/
│   ├── posthog/
│   │   ├── client.ts           # Singleton client wrapper
│   │   ├── config.ts           # Environment configuration
│   │   ├── types.ts            # TypeScript types
│   │   ├── errors.ts           # Custom error classes
│   │   └── handlers/
│   │       ├── webhooks.ts     # Webhook handlers
│   │       └── events.ts       # Event processing
│   ├── services/
│   │   └── posthog/
│   │       ├── index.ts        # Service facade
│   │       ├── sync.ts         # Data synchronization
│   │       └── cache.ts        # Caching layer
│   ├── api/
│   │   └── posthog/
│   │       └── webhook.ts      # Webhook endpoint
│   └── jobs/
│       └── posthog/
│           └── sync.ts         # Background sync job
├── tests/
│   ├── unit/
│   │   └── posthog/
│   └── integration/
│       └── posthog/
├── config/
│   ├── posthog.development.json
│   ├── posthog.staging.json
│   └── posthog.production.json
└── docs/
    └── posthog/
        ├── SETUP.md
        └── RUNBOOK.md
```