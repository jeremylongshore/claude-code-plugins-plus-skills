---
allowed-tools: Read, Write, Edit, Bash, Grep
license: MIT
description: Execute customer.io primary messaging workflow. use when setting up email
  campaigns, push notifications, sms messaging, or in-app message workflows. trigger
  with phrases like "customer.io campaign", "customer.io workflow", "customer.io email
  autom...
name: customerio-primary-workflow
---
# Customerio Primary Workflow

This skill provides automated assistance for customerio primary workflow tasks.

## Prerequisites
- Customer.io SDK configured
- Campaign/workflow created in Customer.io dashboard
- Understanding of your user lifecycle events

## Instructions

1. Go to Campaigns > Create Campaign
2. Select trigger: Event "signed_up"
3. Add workflow steps:


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- User lifecycle event definitions
- Customer.io service integration
- Application route integration
- Campaign workflow triggering

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Resources
- [Customer.io Campaigns](https://customer.io/docs/campaigns/)
- [Trigger Events](https://customer.io/docs/events/)