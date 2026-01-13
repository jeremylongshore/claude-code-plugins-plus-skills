---
name: changelog-orchestrator
description: |
  Draft changelog prs by collecting github/slack/git changes, formatting with templates, running quality gates, and preparing a branch/pr. use when generating weekly/monthly release notes or when the user asks to create a changelog from recent merge...
allowed-tools: Read, Write, Edit, Grep, Glob, Bash(cmd:*)
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Changelog Orchestrator

This skill provides automated assistance for changelog orchestrator tasks.

## Overview

This skill turns raw repo activity (merged PRs, issues, commits, optional Slack updates) into a publishable changelog draft and prepares a branch/PR for review.

## Prerequisites

- A project config file at `.changelog-config.json` in the target repo.
- Required environment variables set (at minimum `GITHUB_TOKEN` for GitHub source).
- Git available in PATH; `gh` optional (used for PR creation if configured).

## Instructions

1. Read `.changelog-config.json` from the repo root.
2. Validate it with `{baseDir}/scripts/validate_config.py`.
3. Decide date range:
1. Load the configured markdown template (or fall back to `{baseDir}/assets/weekly-template.md`).
2. Render the final markdown using `{baseDir}/scripts/render_template.py`.
3. Ensure frontmatter contains at least `date` (ISO) and `version` (SemVer if known; otherwise `0.0.0`).
1. Run deterministic checks using `{baseDir}/scripts/quality_score.py`.
2. If score is below threshold:
1. Write the changelog file to the configured `output_path`.
2. Create a branch `changelog-YYYY-MM-DD`, commit with `docs: add changelog for YYYY-MM-DD`.
3. If `gh` is configured, open a PR; otherwise, print the exact commands the user should run.


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output

- A markdown changelog draft (usually `CHANGELOG.md`), plus an optional PR URL.
- A quality report (score + findings) from `{baseDir}/scripts/quality_score.py`.

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources

- Validate config: `{baseDir}/scripts/validate_config.py`
- Render template: `{baseDir}/scripts/render_template.py`
- Quality scoring: `{baseDir}/scripts/quality_score.py`
- Default templates:
  - `{baseDir}/assets/default-changelog.md`
  - `{baseDir}/assets/weekly-template.md`
  - `{baseDir}/assets/release-template.md`