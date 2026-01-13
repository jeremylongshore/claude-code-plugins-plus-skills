# Project Structure

## Project Structure
```
linear-integration/
├── src/
│   ├── api/                    # REST/GraphQL API
│   │   ├── routes/
│   │   └── middleware/
│   ├── services/               # Business logic
│   │   ├── issue-service.ts
│   │   ├── project-service.ts
│   │   └── sync-service.ts
│   ├── infrastructure/         # External integrations
│   │   ├── linear/
│   │   │   ├── client.ts
│   │   │   ├── cache.ts
│   │   │   └── webhook-handler.ts
│   │   ├── database/
│   │   └── cache/
│   ├── domain/                 # Domain models
│   │   ├── issue.ts
│   │   └── project.ts
│   └── config/                 # Configuration
│       └── index.ts
├── tests/
│   ├── unit/
│   ├── integration/
│   └── e2e/
└── infrastructure/             # IaC
    ├── terraform/
    └── kubernetes/
```