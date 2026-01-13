# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

Claude Code plugins marketplace (270+ plugins, 739 skills). Live at https://claudecodeplugins.io/

**Monorepo structure:** pnpm workspaces (v9.15.9+)
- `plugins/mcp/*` - MCP server plugins (TypeScript, ~2% of plugins)
- `plugins/[category]/*` - AI instruction plugins (Markdown, ~98%)
- `plugins/saas-packs/*-pack` - SaaS skill packs
- `marketplace/` - Astro website (**uses npm, not pnpm**)
- `packages/` - CLI, validator, analytics

**Package manager:** `pnpm` at root, `npm` for marketplace only.

## Essential Commands

```bash
# Before ANY commit (MANDATORY)
pnpm run sync-marketplace           # Regenerate marketplace.json from .extended.json
./scripts/validate-all-plugins.sh   # Full validation
./scripts/quick-test.sh             # Fast validation (~30s)

# Build & test
pnpm install && pnpm build          # Install and build all
pnpm test && pnpm typecheck         # Run tests and type check

# Single MCP plugin
cd plugins/mcp/[name]/ && pnpm build && chmod +x dist/index.js

# Marketplace website
cd marketplace/ && npm run dev      # Dev server at localhost:4321

# Validation
./scripts/validate-all-plugins.sh plugins/[category]/[name]/
python3 scripts/validate-skills-schema.py   # 2025 skills schema + grading
```

## Two Catalog System (Critical)

| File | Purpose | Edit? |
|------|---------|-------|
| `.claude-plugin/marketplace.extended.json` | Source of truth with extended metadata | ✅ Yes |
| `.claude-plugin/marketplace.json` | CLI-compatible (auto-generated) | ❌ Never |

Run `pnpm run sync-marketplace` after editing `.extended.json`. CI fails if out of sync.

## Plugin Structure

### AI Instruction Plugins
```
plugins/[category]/[plugin-name]/
├── .claude-plugin/plugin.json    # Required: name, version, description, author
├── README.md
├── commands/*.md                 # Slash commands
├── agents/*.md                   # Custom agents
└── skills/[skill-name]/SKILL.md  # Auto-activating skills
```

### MCP Server Plugins
```
plugins/mcp/[plugin-name]/
├── .claude-plugin/plugin.json
├── src/*.ts                      # TypeScript source
├── dist/index.js                 # Must be executable with shebang
├── package.json
└── .mcp.json
```

### SKILL.md Frontmatter (2025 Spec)
```yaml
---
name: skill-name
description: |
  When to use this skill. Include trigger phrases.
allowed-tools: Read, Write, Edit, Bash(npm:*), Glob
version: 1.0.0
author: Name <email>
---
```

Valid tools: `Read`, `Write`, `Edit`, `Bash`, `Glob`, `Grep`, `WebFetch`, `WebSearch`, `Task`, `TodoWrite`, `NotebookEdit`, `AskUserQuestion`, `Skill`

## Adding a New Plugin

1. Copy from `templates/` (minimal, command, agent, or full)
2. Create `.claude-plugin/plugin.json` with required fields
3. Add entry to `.claude-plugin/marketplace.extended.json`
4. `pnpm run sync-marketplace`
5. `./scripts/validate-all-plugins.sh plugins/[category]/[name]/`

## Conventions

- **Hooks:** Use `${CLAUDE_PLUGIN_ROOT}` for portability
- **Scripts:** All `.sh` files must be `chmod +x`
- **Model IDs in skills:** Use `sonnet` or `haiku` (not `opus`)

## Key Identifiers

- **Slug:** `claude-code-plugins-plus`
- **Install:** `/plugin marketplace add jeremylongshore/claude-code-plugins`

## Task Tracking (Beads)

See `AGENTS.md` for full protocol. Work isn't done until `git push` succeeds.

```bash
bd ready                            # Available tasks
bd update <id> --status in_progress # Claim task
bd close <id> --reason "..."        # Complete task
bd sync && git push                 # MANDATORY at session end
```
