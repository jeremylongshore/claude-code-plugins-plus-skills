---
name: responding-to-security-incidents
description: |
  Analyze and guide security incident response, investigation, and remediation processes. Use when you need to handle security breaches, classify incidents, develop response playbooks, gather forensic evidence, or coordinate remediation efforts. Tri...
allowed-tools: Read, Write, Edit, Grep, Glob, Bash(cmd:*)
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Responding To Security Incidents

This skill provides automated assistance for responding to security incidents tasks.

## Overview

This skill provides automated assistance for the described functionality.

## Prerequisites

Before using this skill, ensure:
- Access to system and application logs in {baseDir}/logs/
- Network traffic captures or SIEM data available
- Incident response team contact information
- Backup systems operational and accessible
- Write permissions for incident documentation in {baseDir}/incidents/
- Communication channels established for stakeholder updates

## Instructions

1. Triage the incident and scope affected systems/data.
2. Preserve evidence (logs, snapshots, network captures) before making changes.
3. Contain the blast radius and eradicate root cause.
4. Recover safely and document follow-ups (AAR + backlog).


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output

The skill produces:

**Primary Output**: Incident response playbook saved to {baseDir}/incidents/incident-YYYYMMDD-HHMM.md

**Playbook Structure**:
```
# Security Incident Response - [Incident Type]

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources

- NIST Computer Security Incident Handling Guide: https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-61r2.pdf
- SANS Incident Handler's Handbook: https://www.sans.org/white-papers/33901/
- CISA Incident Response Guide: https://www.cisa.gov/incident-response
- Memory analysis: Volatility Framework
- Disk forensics: Autopsy, FTK Imager