---
allowed-tools: Read, Write, Edit, Bash
license: MIT
description: Implement exa lint rules, policy enforcement, and automated guardrails.
  use when setting up code quality rules for exa integrations, implementing pre-commit
  hooks, or configuring ci policy checks for exa best practices. trigger with phrases
  like "...
name: exa-policy-guardrails
---
# Exa Policy Guardrails

This skill provides automated assistance for exa policy guardrails tasks.

## Prerequisites
- ESLint configured in project
- Pre-commit hooks infrastructure
- CI/CD pipeline with policy checks
- TypeScript for type enforcement

## Instructions

### Step 1: Create ESLint Rules
Implement custom lint rules for Exa patterns.

### Step 2: Configure Pre-Commit Hooks
Set up hooks to catch issues before commit.

### Step 3: Add CI Policy Checks
Implement policy-as-code in CI pipeline.

### Step 4: Enable Runtime Guardrails
Add production safeguards for dangerous operations.

## Output
- ESLint plugin with Exa rules
- Pre-commit hooks blocking secrets
- CI policy checks passing
- Runtime guardrails active

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [ESLint Plugin Development](https://eslint.org/docs/latest/extend/plugins)
- [Pre-commit Framework](https://pre-commit.com/)
- [Open Policy Agent](https://www.openpolicyagent.org/)