---
allowed-tools: Read, Grep, Bash
license: MIT
description: Execute retell ai incident response procedures with triage, mitigation,
  and postmortem. use when responding to retell ai-related outages, investigating
  errors, or running post-incident reviews for retell ai integration failures. trigger
  with phras...
name: retellai-incident-runbook
---
# Retellai Incident Runbook

This skill provides automated assistance for retellai incident runbook tasks.

## Prerequisites
- Access to Retell AI dashboard and status page
- kubectl access to production cluster
- Prometheus/Grafana access
- Communication channels (Slack, PagerDuty)

## Instructions

### Step 1: Quick Triage
Run the triage commands to identify the issue source.

### Step 2: Follow Decision Tree
Determine if the issue is Retell AI-side or internal.

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
- [Retell AI Status Page](https://status.retellai.com)
- [Retell AI Support](https://support.retellai.com)