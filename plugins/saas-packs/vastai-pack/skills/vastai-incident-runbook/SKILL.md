---
allowed-tools: Read, Grep, Bash
license: MIT
description: Execute vast.ai incident response procedures with triage, mitigation,
  and postmortem. use when responding to vast.ai-related outages, investigating errors,
  or running post-incident reviews for vast.ai integration failures. trigger with
  phrases lik...
name: vastai-incident-runbook
---
# Vastai Incident Runbook

This skill provides automated assistance for vastai incident runbook tasks.

## Prerequisites
- Access to Vast.ai dashboard and status page
- kubectl access to production cluster
- Prometheus/Grafana access
- Communication channels (Slack, PagerDuty)

## Instructions

### Step 1: Quick Triage
Run the triage commands to identify the issue source.

### Step 2: Follow Decision Tree
Determine if the issue is Vast.ai-side or internal.

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
- [Vast.ai Status Page](https://status.vastai.com)
- [Vast.ai Support](https://support.vastai.com)