---
allowed-tools: Read, Grep, Bash
license: MIT
description: Execute ideogram incident response procedures with triage, mitigation,
  and postmortem. use when responding to ideogram-related outages, investigating errors,
  or running post-incident reviews for ideogram integration failures. trigger with
  phrases ...
name: ideogram-incident-runbook
---
# Ideogram Incident Runbook

This skill provides automated assistance for ideogram incident runbook tasks.

## Prerequisites
- Access to Ideogram dashboard and status page
- kubectl access to production cluster
- Prometheus/Grafana access
- Communication channels (Slack, PagerDuty)

## Instructions

### Step 1: Quick Triage
Run the triage commands to identify the issue source.

### Step 2: Follow Decision Tree
Determine if the issue is Ideogram-side or internal.

### Step 3: Execute Immediate Actions
Apply the appropriate remediation for the error type.

### Step 4: Communicate Status
Update internal and external stakeholders.

## Output
- Issue identified and categorized
- Remediation applied
- Stakeholders notified
- Evidence collected for postmortem

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [Ideogram Status Page](https://status.ideogram.com)
- [Ideogram Support](https://support.ideogram.com)