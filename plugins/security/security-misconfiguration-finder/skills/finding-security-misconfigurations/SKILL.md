---
name: finding-security-misconfigurations
license: MIT
allowed-tools: Read, Write, Edit, Grep, Glob, Bash
description: Configure identify security misconfigurations in infrastructure-as-code,
  application settings, and system configurations. Use when you need to audit Terraform/CloudFormation
  templates, check application config files, validate system security setti...
---
# Finding Security Misconfigurations

## Overview

This skill provides automated assistance for the described functionality.

## Prerequisites

Before using this skill, ensure:
- Configuration files accessible in {baseDir}/ (Terraform, CloudFormation, YAML, JSON)
- Infrastructure-as-code files (.tf, .yaml, .json, .template)
- Application configuration files (application.yml, config.json, .env.example)
- System configuration exports available
- Write permissions for findings report in {baseDir}/security-findings/

## Instructions

1. Identify the target system/service and gather current configuration.
2. Compare settings against baseline hardening guidance.
3. Flag risky defaults, drift, and missing controls with severity.
4. Provide a minimal-change remediation plan and verification steps.


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output

The skill produces:

**Primary Output**: Security misconfigurations report saved to {baseDir}/security-findings/misconfig-YYYYMMDD.md

**Report Structure**:
```
# Security Misconfiguration Findings

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources

- CIS Benchmarks: https://www.cisecurity.org/cis-benchmarks/
- OWASP Configuration Guide: https://cheatsheetseries.owasp.org/cheatsheets/Infrastructure_as_Code_Security_Cheatsheet.html
- Cloud Security Alliance: https://cloudsecurityalliance.org/
- tfsec (Terraform): https://github.com/aquasecurity/tfsec
- Checkov (Multi-cloud): https://www.checkov.io/
