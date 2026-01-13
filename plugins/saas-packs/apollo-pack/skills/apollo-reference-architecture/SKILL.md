---
name: apollo-reference-architecture
description: |
  Implement apollo.io reference architecture. use when designing apollo integrations, establishing patterns, or building production-grade sales intelligence systems. trigger with phrases like "apollo architecture", "apollo system design", "apollo in...
allowed-tools: Read, Write, Edit, Bash(cmd:*)
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Apollo Reference Architecture

This skill provides automated assistance for apollo reference architecture tasks.

## Output
- Layered architecture (client, service, job, model)
- Background job processing with Bull
- Database models with TypeORM
- RESTful API endpoints
- CRM integration patterns
- Event-driven architecture

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Resources
- [NestJS Documentation](https://docs.nestjs.com/)
- [Bull Queue](https://github.com/OptimalBits/bull)
- [TypeORM](https://typeorm.io/)
- [Event Sourcing Patterns](https://martinfowler.com/eaaDev/EventSourcing.html)