---
name: detecting-sql-injection-vulnerabilities
license: MIT
allowed-tools: Read, Write, Edit, Grep, Glob, Bash
description: Detect and analyze sql injection vulnerabilities in application code
  and database queries. use when you need to scan code for sql injection risks, review
  query construction, validate input sanitization, or implement secure query patterns.
  trigger ...
---
# Detecting Sql Injection Vulnerabilities

## Overview

This skill provides automated assistance for the described functionality.

## Prerequisites

Before using this skill, ensure:
- Application source code accessible in {baseDir}/
- Database query files and ORM configurations available
- Framework information (Django, Rails, Express, Spring, etc.)
- Write permissions for security reports in {baseDir}/security-reports/

## Instructions

1. Identify input surfaces and data flows into database queries.
2. Review query construction and parameterization patterns.
3. Flag injection vectors and document impact.
4. Recommend fixes (parameterized queries, ORM patterns, validation) and tests.


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output

The skill produces:

**Primary Output**: SQL injection vulnerability report saved to {baseDir}/security-reports/sqli-scan-YYYYMMDD.md

**Report Structure**:
```
# SQL Injection Vulnerability Report
Scan Date: 2024-01-15
Application: E-commerce Platform
Framework: Django 4.2

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources

- SQL Injection Prevention Cheat Sheet: https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html
- OWASP Top 10 - Injection: https://owasp.org/www-project-top-ten/
- CWE-89: SQL Injection: https://cwe.mitre.org/data/definitions/89.html
- CAPEC-66: SQL Injection: https://capec.mitre.org/data/definitions/66.html
- Django Security: https://docs.djangoproject.com/en/stable/topics/security/
