---
name: lindy-deploy-integration
description: |
  Configure deployment pipelines for Lindy AI integrations.
  Use when deploying to production, setting up staging environments,
  or automating agent deployments.
  Trigger with phrases like "deploy lindy", "lindy deployment",
  "lindy production deploy", "release lindy agents".
allowed-tools: Read, Write, Edit, Bash
version: 1.0.0
license: MIT
author: Jeremy Longshore <jeremy@intentsolutions.io>
---

# Lindy Deploy Integration

## Overview
Configure deployment pipelines for Lindy AI agent integrations.

## Prerequisites
- CI pipeline configured (see `lindy-ci-integration`)
- Production Lindy API key
- Deployment target (Vercel, AWS, GCP, etc.)

## Instructions

### Step 1: Create Deployment Workflow
```yaml
# .github/workflows/lindy-deploy.yml
name: Deploy Lindy Integration

on:
  push:
    branches: [main]
  workflow_dispatch:

env:
  LINDY_ENVIRONMENT: production

jobs:
  deploy:
    runs-on: ubuntu-latest
    environment: production

    steps:
      - uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'

      - name: Install dependencies
        run: npm ci

      - name: Build
        run: npm run build

      - name: Run pre-deploy checks
        run: npm run predeploy
        env:
          LINDY_API_KEY: ${{ secrets.LINDY_PROD_API_KEY }}

      - name: Deploy to Vercel
        uses: amondnet/vercel-action@v25
        with:
          vercel-token: ${{ secrets.VERCEL_TOKEN }}
          vercel-org-id: ${{ secrets.VERCEL_ORG_ID }}
          vercel-project-id: ${{ secrets.VERCEL_PROJECT_ID }}
          vercel-args: '--prod'

      - name: Sync Lindy agents
        run: npm run sync:agents
        env:
          LINDY_API_KEY: ${{ secrets.LINDY_PROD_API_KEY }}

      - name: Notify Slack
        if: success()
        uses: slackapi/slack-github-action@v1
        with:
          payload: |
            {
              "text": "Lindy integration deployed successfully"
            }
```

### Step 2: Create Agent Sync Script
```typescript
// scripts/sync-agents.ts
import { Lindy } from '@lindy-ai/sdk';
import fs from 'fs';

interface AgentConfig {
  id?: string;
  name: string;
  instructions: string;
  tools: string[];
}

async function syncAgents() {
  const lindy = new Lindy({ apiKey: process.env.LINDY_API_KEY });

  // Load agent configurations
  const configPath = './agents/config.json';
  const configs: AgentConfig[] = JSON.parse(fs.readFileSync(configPath, 'utf-8'));

  for (const config of configs) {
    if (config.id) {
      // Update existing agent
      await lindy.agents.update(config.id, {
        name: config.name,
        instructions: config.instructions,
        tools: config.tools,
      });
      console.log(`Updated agent: ${config.id}`);
    } else {
      // Create new agent
      const agent = await lindy.agents.create({
        name: config.name,
        instructions: config.instructions,
        tools: config.tools,
      });
      console.log(`Created agent: ${agent.id}`);

      // Update config with new ID
      config.id = agent.id;
    }
  }

  // Save updated config
  fs.writeFileSync(configPath, JSON.stringify(configs, null, 2));
}

syncAgents().catch(console.error);
```

### Step 3: Configure Environments
```yaml
# .github/workflows/lindy-deploy-staging.yml
name: Deploy to Staging

on:
  push:
    branches: [develop]

jobs:
  deploy:
    environment: staging
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm ci
      - run: npm run build
      - run: npm run deploy:staging
        env:
          LINDY_API_KEY: ${{ secrets.LINDY_STAGING_API_KEY }}
```

### Step 4: Add Rollback Capability
```typescript
// scripts/rollback.ts
import { Lindy } from '@lindy-ai/sdk';

async function rollback(agentId: string, version: string) {
  const lindy = new Lindy({ apiKey: process.env.LINDY_API_KEY });

  // Get version history
  const versions = await lindy.agents.versions.list(agentId);
  const targetVersion = versions.find(v => v.id === version);

  if (!targetVersion) {
    throw new Error(`Version ${version} not found`);
  }

  // Restore to previous version
  await lindy.agents.versions.restore(agentId, version);
  console.log(`Rolled back agent ${agentId} to version ${version}`);
}

rollback(process.argv[2], process.argv[3]).catch(console.error);
```

## Output
- Automated deployment pipeline
- Agent sync mechanism
- Environment-specific deployments
- Rollback capability

## Error Handling
| Issue | Cause | Solution |
|-------|-------|----------|
| Deploy failed | Build error | Check build logs |
| Agent sync failed | Invalid config | Validate JSON |
| Rollback failed | Version missing | Check version history |

## Examples

### Docker Deployment
```yaml
# Dockerfile
FROM node:20-alpine
WORKDIR /app
COPY package*.json ./
RUN npm ci --production
COPY dist ./dist
ENV NODE_ENV=production
CMD ["node", "dist/index.js"]
```

```yaml
# Deploy job
- name: Build and push Docker image
  run: |
    docker build -t my-lindy-app:${{ github.sha }} .
    docker push my-lindy-app:${{ github.sha }}
```

## Resources
- [Lindy Deployment Guide](https://docs.lindy.ai/deployment)
- [Vercel Documentation](https://vercel.com/docs)
- [GitHub Environments](https://docs.github.com/en/actions/deployment)

## Next Steps
Proceed to `lindy-webhooks-events` for event handling.
