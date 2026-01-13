---
allowed-tools: Read, Write, Edit
license: MIT
description: Manage Windsurf licenses and seat allocation. Activate when users mention
  "license management", "seat allocation", "billing optimization", "user licenses",
  or "subscription management". Handles license administration. Use when working with
  windsur...
name: windsurf-license-management
---
# Windsurf License Management

This skill provides automated assistance for windsurf license management tasks.

## Overview

This skill enables enterprise license management for Windsurf deployments. It covers seat allocation, usage tracking, cost optimization, and compliance reporting. Administrators can provision new users, reclaim inactive seats, analyze utilization patterns, and optimize subscription tiers based on actual usage data.

## Prerequisites

- Windsurf Enterprise subscription with admin access
- Organization administrator role
- Access to billing portal
- User directory integration (optional: SCIM, Azure AD, Okta)
- Understanding of organization structure and teams

## Instructions

1. **Inventory Current Licenses**
2. **Set Allocation Policies**
3. **Configure Usage Tracking**
4. **Optimize Subscription**
5. **Monitor and Report**


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output

- License inventory with current allocations
- Utilization reports with recommendations
- Cost analysis with optimization opportunities
- Compliance reports for audits

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources

- [Windsurf License Administration](https://docs.windsurf.ai/admin/licensing)
- [SCIM Integration Guide](https://docs.windsurf.ai/admin/scim)
- [Cost Optimization Best Practices](https://docs.windsurf.ai/admin/cost-optimization)