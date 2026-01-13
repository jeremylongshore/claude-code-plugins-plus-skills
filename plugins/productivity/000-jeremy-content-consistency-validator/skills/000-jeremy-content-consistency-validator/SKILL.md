---
name: 000-jeremy-content-consistency-validator
description: |
  Validate messaging consistency across website, GitHub repos, and local documentation generating read-only discrepancy reports. Use when checking content alignment or finding mixed messaging. Trigger with phrases like "check consistency", "validate...
allowed-tools: Read, WebFetch, WebSearch, Grep, Bash(cmd:*)
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# 000 Jeremy Content Consistency Validator

This skill provides automated assistance for 000 jeremy content consistency validator tasks.

## Overview

This skill provides automated assistance for the described functionality.

## Prerequisites

- Access to website content (local build or deployed site)
- Access to GitHub repositories
- Local documentation in {baseDir}/docs/ or claudes-docs/
- WebFetch permissions for remote content

## Instructions

1. Identify and discover all content sources (website, GitHub, local docs)
2. Extract key messaging, features, versions from each source
3. Compare content systematically across sources
4. Identify critical discrepancies, warnings, and informational notes
5. Generate comprehensive Markdown report
6. Provide prioritized action items for consistency fixes

## Output

- Comprehensive consistency validation report in Markdown format
- Executive summary with discrepancy counts by severity
- Detailed comparison by source pairs (website vs GitHub, etc.)
- Terminology consistency matrix
- Prioritized action items with file locations and line numbers
- Reports saved to consistency-reports/YYYY-MM-DD-HH-MM-SS.md

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources

- Content consistency best practices
- Documentation style guides
- Version control strategies for content
- Multi-platform content management approaches