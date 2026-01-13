---
allowed-tools: Read, Write, Edit, Bash
license: MIT
description: Implement customer.io load testing and scaling. use when preparing for
  high traffic, load testing, or scaling integrations for enterprise workloads. trigger
  with phrases like "customer.io load test", "customer.io scale", "customer.io high
  volume",...
name: customerio-load-scale
---
# Customerio Load Scale

This skill provides automated assistance for customerio load scale tasks.

## Prerequisites
- Customer.io integration working
- Load testing tools (k6, Artillery)
- Staging environment with test workspace


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Resources
- [k6 Documentation](https://k6.io/docs/)
- [Customer.io Rate Limits](https://customer.io/docs/api/track/#section/Limits)