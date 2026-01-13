---
name: generating-security-audit-reports
description: |
  Generate comprehensive security audit reports for applications and systems.
  Use when you need to assess security posture, identify vulnerabilities, evaluate compliance status, or create formal security documentation.
  Trigger with phrases like "create security audit report", "generate security assessment", "audit security posture", or "PCI-DSS compliance report".
  
allowed-tools: Read, Write, Edit, Grep, Glob, Bash
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---

# Generating Security Audit Reports

## Overview

This skill provides automated assistance for the described functionality.

## Prerequisites

Before using this skill, ensure:
- Security scan data or logs are available in {baseDir}/security/
- Access to application configuration files
- Security tool outputs (e.g., vulnerability scanners, SAST/DAST results)
- Compliance framework documentation (if applicable)
- Write permissions for generating report files

## Instructions

1. Collect available security signals (scanner outputs, configs, logs).
2. Analyze findings and map to risk + compliance requirements.
3. Generate a report with prioritized remediation guidance.
4. Format outputs (Markdown/HTML/PDF) and include evidence links.


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output

The skill produces:

**Primary Output**: Comprehensive security audit report saved to {baseDir}/reports/security-audit-YYYYMMDD.md

**Report Structure**:
```
# Security Audit Report - [System Name]

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources

- OWASP Top 10: https://owasp.org/www-project-top-ten/
- CWE Top 25: https://cwe.mitre.org/top25/
- NIST Cybersecurity Framework: https://www.nist.gov/cyberframework
- PCI-DSS Requirements: https://www.pcisecuritystandards.org/
- GDPR Compliance Checklist: https://gdpr.eu/checklist/
