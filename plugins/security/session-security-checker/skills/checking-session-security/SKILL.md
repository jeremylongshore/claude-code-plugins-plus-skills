---
name: checking-session-security
license: MIT
allowed-tools: Read, Write, Edit, Grep, Glob, Bash
description: Analyze session management implementations to identify security vulnerabilities
  in web applications. Use when you need to audit session handling, check for session
  fixation risks, review session timeout configurations, or validate session ID gener...
---
# Checking Session Security

## Overview

This skill provides automated assistance for the described functionality.

## Prerequisites

Before using this skill, ensure:
- Source code accessible in {baseDir}/
- Session management code locations known (auth modules, middleware)
- Framework information (Express, Django, Spring, etc.)
- Configuration files for session settings
- Write permissions for security report in {baseDir}/security-reports/

## Instructions

1. Review session creation, storage, and transport security controls.
2. Validate cookie flags, rotation, expiration, and invalidation behavior.
3. Identify common attack paths (fixation, CSRF, replay) and mitigations.
4. Provide prioritized fixes with configuration/code examples.


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output

The skill produces:

**Primary Output**: Session security report saved to {baseDir}/security-reports/session-security-YYYYMMDD.md

**Report Structure**:
```
# Session Security Analysis Report
Analysis Date: 2024-01-15
Application: Web Portal
Framework: Express.js

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources

- Session Management Cheat Sheet: https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html
- OWASP Top 10 - Broken Authentication: https://owasp.org/www-project-top-ten/
- NIST 800-63B Authentication: https://pages.nist.gov/800-63-3/sp800-63b.html
- PCI-DSS Session Requirements: https://www.pcisecuritystandards.org/
- Express.js Session Security: https://expressjs.com/en/advanced/best-practice-security.html
