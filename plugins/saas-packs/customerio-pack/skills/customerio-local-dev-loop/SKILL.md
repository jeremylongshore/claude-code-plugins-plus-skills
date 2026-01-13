---
allowed-tools: Read, Write, Edit, Bash, Grep
license: MIT
description: Configure Customer.io local development workflow. Use when setting up
  local testing, development environment, or offline development for Customer.io integrations.
  Trigger with phrases like "customer.io local dev", "test customer.io locally", "cust...
name: customerio-local-dev-loop
---
# Customerio Local Dev Loop

This skill provides automated assistance for customerio local dev loop tasks.

## Prerequisites
- Customer.io SDK installed
- Separate development workspace in Customer.io (recommended)
- Environment variable management tool (dotenv)


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- Environment-aware Customer.io client
- Dry-run mode for safe testing
- Test mocks for unit testing
- Prefixed events for development isolation

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Resources
- [Customer.io Workspaces](https://customer.io/docs/workspaces/)
- [Test Mode Best Practices](https://customer.io/docs/test-mode/)