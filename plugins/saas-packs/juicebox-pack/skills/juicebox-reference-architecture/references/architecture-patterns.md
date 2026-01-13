# Architecture Patterns

## Architecture Patterns

### Pattern 1: Simple Integration
```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   Client    │────▶│   Backend   │────▶│  Juicebox   │
│   (React)   │     │   (Node)    │     │    API      │
└─────────────┘     └─────────────┘     └─────────────┘
```

**Best for:** Small applications, MVPs, single-tenant systems

### Pattern 2: Cached Architecture
```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   Client    │────▶│   Backend   │────▶│   Redis     │
│   (React)   │     │   (Node)    │     │   Cache     │
└─────────────┘     └─────────────┘     └──────┬──────┘
                                                │
                                        ┌───────▼───────┐
                                        │   Juicebox    │
                                        │     API       │
                                        └───────────────┘
```

**Best for:** Medium applications, cost optimization

### Pattern 3: Enterprise Architecture
```
                    ┌─────────────────────────────────────────┐
                    │             Load Balancer               │
                    └────────────────────┬────────────────────┘
                                         │
            ┌────────────────────────────┼────────────────────────────┐
            │                            │                            │
    ┌───────▼───────┐           ┌────────▼────────┐          ┌────────▼────────┐
    │   API Server  │           │   API Server    │          │   API Server    │
    │   (Node.js)   │           │   (Node.js)     │          │   (Node.js)     │
    └───────┬───────┘           └────────┬────────┘          └────────┬────────┘
            │                            │                            │
            └────────────────────────────┼────────────────────────────┘
                                         │
                    ┌────────────────────┼────────────────────┐
                    │                    │                    │
            ┌───────▼───────┐   ┌────────▼────────┐  ┌────────▼────────┐
            │   Redis       │   │   PostgreSQL    │  │   Message       │
            │   (Cache)     │   │   (Profiles)    │  │   Queue         │
            └───────────────┘   └─────────────────┘  └────────┬────────┘
                                                              │
                                                     ┌────────▼────────┐
                                                     │   Worker Pool   │
                                                     │   (Enrichment)  │
                                                     └────────┬────────┘
                                                              │
                                                     ┌────────▼────────┐
                                                     │   Juicebox API  │
                                                     └─────────────────┘
```

**Best for:** Large-scale applications, multi-tenant, high availability