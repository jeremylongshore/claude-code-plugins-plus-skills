# Github Actions Setup

## GitHub Actions Setup

### Basic CI Workflow
```yaml
# .github/workflows/apollo-ci.yml
name: Apollo Integration CI

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

env:
  NODE_VERSION: '20'

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}
          cache: 'npm'

      - name: Install dependencies
        run: npm ci

      - name: Run linting
        run: npm run lint

      - name: Run unit tests
        run: npm run test:unit
        env:
          APOLLO_API_KEY: ${{ secrets.APOLLO_API_KEY_TEST }}

      - name: Run integration tests
        if: github.event_name == 'push' && github.ref == 'refs/heads/main'
        run: npm run test:integration
        env:
          APOLLO_API_KEY: ${{ secrets.APOLLO_API_KEY_TEST }}

  validate-apollo:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}
          cache: 'npm'

      - name: Install dependencies
        run: npm ci

      - name: Validate Apollo configuration
        run: npm run apollo:validate
        env:
          APOLLO_API_KEY: ${{ secrets.APOLLO_API_KEY_TEST }}

      - name: Check API health
        run: |
          curl -sf "https://api.apollo.io/v1/auth/health?api_key=$APOLLO_API_KEY" \
            || echo "Warning: Apollo API health check failed"
        env:
          APOLLO_API_KEY: ${{ secrets.APOLLO_API_KEY_TEST }}
```

### Integration Test Workflow
```yaml
# .github/workflows/apollo-integration.yml
name: Apollo Integration Tests

on:
  schedule:
    - cron: '0 6 * * *'  # Daily at 6 AM UTC
  workflow_dispatch:

jobs:
  integration-tests:
    runs-on: ubuntu-latest
    timeout-minutes: 30

    steps:
      - uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'

      - name: Install dependencies
        run: npm ci

      - name: Run Apollo integration tests
        run: npm run test:apollo
        env:
          APOLLO_API_KEY: ${{ secrets.APOLLO_API_KEY_TEST }}
          APOLLO_TEST_DOMAIN: 'apollo.io'

      - name: Upload test results
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: apollo-test-results
          path: test-results/

      - name: Notify on failure
        if: failure()
        uses: slackapi/slack-github-action@v1
        with:
          payload: |
            {
              "text": "Apollo integration tests failed!",
              "blocks": [
                {
                  "type": "section",
                  "text": {
                    "type": "mrkdwn",
                    "text": "*Apollo Integration Tests Failed*\n<${{ github.server_url }}/${{ github.repository }}/actions/runs/${{ github.run_id }}|View Run>"
                  }
                }
              ]
            }
        env:
          SLACK_WEBHOOK_URL: ${{ secrets.SLACK_WEBHOOK_URL }}
```