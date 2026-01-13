---
name: customerio-reference-architecture
description: |
  Implement customer.io reference architecture. use when designing integrations, planning architecture, or implementing enterprise patterns. trigger with phrases like "customer.io architecture", "customer.io design", "customer.io enterprise", "custo...
allowed-tools: Read, Write, Edit, Bash(cmd:*)
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Customerio Reference Architecture


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- Core Customer.io service layer
- Event bus integration (Kafka)
- Repository pattern for user messaging
- Webhook handler with signature verification
- Terraform infrastructure code

## Resources
- [Customer.io API Reference](https://customer.io/docs/api/)
- [Webhook Documentation](https://customer.io/docs/webhooks/)
