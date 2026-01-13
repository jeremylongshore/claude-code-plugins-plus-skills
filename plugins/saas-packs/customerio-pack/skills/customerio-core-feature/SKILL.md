---
name: customerio-core-feature
description: |
  Implement customer.io core feature integration. use when implementing segments, transactional messages, data pipelines, or broadcast campaigns. trigger with phrases like "customer.io segments", "customer.io transactional", "customer.io broadcast",...
allowed-tools: Read, Write, Edit, Bash(cmd:*), Grep
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Customerio Core Feature

This skill provides automated assistance for customerio core feature tasks.

## Prerequisites
- Customer.io SDK configured
- Understanding of customer data model
- App API credentials for transactional emails


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- Transactional email sending capability
- Segment-ready user attributes
- Anonymous to known user merging
- B2B object tracking (companies)
- CDP data pipeline integration

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Resources
- [Transactional API](https://customer.io/docs/transactional-api/)
- [Segments](https://customer.io/docs/segments/)
- [Anonymous Events](https://customer.io/docs/anonymous-events/)