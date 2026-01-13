---
name: logging-api-requests
description: |
  Monitor and log API requests with correlation IDs, performance metrics, and security audit trails. Use when auditing API requests and responses. Trigger with phrases like "log API requests", "add API logging", or "track API calls".
allowed-tools: Read, Write, Edit, Grep, Glob, Bash(cmd:*)
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Logging Api Requests

This skill provides automated assistance for logging api requests tasks.

## Overview


This skill provides automated assistance for api request logger tasks.
This skill provides automated assistance for the described functionality.

## Prerequisites

Before using this skill, ensure you have:
- API design specifications or requirements documented
- Development environment with necessary frameworks installed
- Database or backend services accessible for integration
- Authentication and authorization strategies defined
- Testing tools and environments configured

## Instructions

1. Use Read tool to examine existing API specifications from {baseDir}/api-specs/
2. Define resource models, endpoints, and HTTP methods
3. Document request/response schemas and data types
4. Identify authentication and authorization requirements
5. Plan error handling and validation strategies
1. Generate boilerplate code using Bash(api:log-*) with framework scaffolding
2. Implement endpoint handlers with business logic
3. Add input validation and schema enforcement
4. Integrate authentication and authorization middleware
5. Configure database connections and ORM models
1. Write integration tests covering all endpoints


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output

- `{baseDir}/src/routes/` - Endpoint route definitions
- `{baseDir}/src/controllers/` - Business logic handlers
- `{baseDir}/src/models/` - Data models and schemas
- `{baseDir}/src/middleware/` - Authentication, validation, logging
- `{baseDir}/src/config/` - Configuration and environment variables
- OpenAPI 3.0 specification with complete endpoint definitions

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources

- Express.js and Fastify for Node.js APIs
- Flask and FastAPI for Python APIs
- Spring Boot for Java APIs
- Gin and Echo for Go APIs
- OpenAPI Specification 3.0+ for API documentation