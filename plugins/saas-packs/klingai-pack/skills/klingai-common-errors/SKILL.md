---
name: klingai-common-errors
description: |
  Execute diagnose and fix common kling ai api errors. use when troubleshooting failed video generation or api issues. trigger with phrases like 'kling ai error', 'klingai not working', 'fix klingai', 'klingai failed'.
allowed-tools: Read, Write, Edit, Grep
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Kling AI Common Errors

This skill provides automated assistance for klingai common errors tasks.

## Overview

Comprehensive guide to identifying, diagnosing, and resolving common Kling AI API errors during video generation.

## Prerequisites

- Kling AI integration experiencing errors
- Access to request/response logs
- API key configured

## Instructions

1. Identify the HTTP status code from the error response
2. Match the error code to the reference table below
3. Review the specific causes for your error
4. Apply the recommended solution
5. Test with a simple request to verify the fix
6. Add proper error handling to prevent recurrence

## Output

- Diagnostic report identifying error type and root cause
- Code fixes with corrected authentication or retry logic
- Verified resolution through successful API test
- Enhanced error handling patterns integrated into codebase

## Error Handling

| Error Code | Cause | Solution |
|------------|-------|----------|
| 401 Unauthorized | Invalid/missing API key | Verify key, check Bearer format |
| 400 Bad Request | Invalid parameters | Validate all required fields |
| 403 Forbidden | Account/content issue | Check account status, review prompt |
| 429 Rate Limited | Too many requests | Implement exponential backoff |
| 402 Payment Required | Insufficient credits | Check balance, add credits |
| 500/502/503 Server | Service outage | Wait and retry with backoff |
| Generation Failed | Complex prompt/timeout | Simplify prompt, reduce duration |

## Examples

**Example: Diagnose Authentication Error**
Request: "My Kling AI video generation keeps failing with 401 errors"
Result: Identified missing Bearer prefix in Authorization header, applied fix, verified with successful test generation

**Example: Handle Rate Limiting**
Request: "Getting too many requests errors when batch processing videos"
Result: Implemented exponential backoff retry decorator, added request queuing, batch processes without rate limit errors

**Example: Debug Generation Failure**
Request: "Video generation fails with no clear error message"
Result: Analyzed job details, identified prompt complexity issue, simplified scene description, successful on retry

## Resources

- [Kling AI API Documentation](https://docs.klingai.com/)
- [Kling AI Error Reference](https://docs.klingai.com/errors)
- [Kling AI Status Page](https://status.klingai.com)

## Detailed Error Reference

See `{baseDir}/references/error-codes.md` for comprehensive error handling code patterns including:
- HTTP 401 authentication fixes with proper Bearer token format
- HTTP 400 parameter validation with pre-flight checks
- HTTP 429 rate limiting with exponential backoff retry decorator
- HTTP 500 server error handling with retry logic
- Generation failure diagnosis and recovery patterns