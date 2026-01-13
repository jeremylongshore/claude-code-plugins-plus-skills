# Project Structure

## Project Structure

```
src/
├── lib/
│   └── apollo/
│       ├── client.ts          # Apollo API client
│       ├── cache.ts           # Caching layer
│       ├── rate-limiter.ts    # Rate limiting
│       ├── errors.ts          # Custom errors
│       └── types.ts           # TypeScript types
├── services/
│   └── apollo/
│       ├── search.service.ts  # People/org search
│       ├── enrich.service.ts  # Enrichment logic
│       ├── sequence.service.ts # Email sequences
│       └── sync.service.ts    # Data synchronization
├── jobs/
│   └── apollo/
│       ├── enrich.job.ts      # Background enrichment
│       ├── sync.job.ts        # Periodic sync
│       └── cleanup.job.ts     # Cache cleanup
├── routes/
│   └── api/
│       └── apollo/
│           ├── search.ts      # Search endpoints
│           ├── enrich.ts      # Enrichment endpoints
│           └── webhooks.ts    # Webhook handlers
├── models/
│   ├── contact.model.ts       # Contact entity
│   ├── company.model.ts       # Company entity
│   └── engagement.model.ts    # Email engagement
└── config/
    └── apollo.config.ts       # Apollo configuration
```