---
name: analyzing-security-headers
license: MIT
allowed-tools: Read, WebFetch, WebSearch, Grep
description: Analyze HTTP security headers of web domains to identify vulnerabilities
  and misconfigurations. Use when you need to audit website security headers, assess
  header compliance, or get security recommendations for web applications. Trigger
  with phras...
---
# Analyzing Security Headers

## Overview

This skill provides automated assistance for the described functionality.

## Prerequisites

Before using this skill, ensure:
- Target URL or domain name is accessible
- Network connectivity for HTTP requests
- Permission to scan the target domain
- Optional: Save results to {baseDir}/security-reports/

## Instructions

1. Collect the target URL/domain and environment context (CDN/proxy, redirects).
2. Fetch response headers (HTTP/HTTPS) and capture redirects/cookies.
3. Compare headers to recommended baselines and score gaps.
4. Provide concrete remediation steps and verify fixes.


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output

The skill produces:

**Primary Output**: Security headers analysis report

**Report Structure**:
```
# Security Headers Analysis - example.com

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources

- OWASP Secure Headers Project: https://owasp.org/www-project-secure-headers/
- MDN Security Headers Guide: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers#security
- Security Headers Scanner: https://securityheaders.com/
- CSP Reference: https://content-security-policy.com/
- HSTS Preload: https://hstspreload.org/
