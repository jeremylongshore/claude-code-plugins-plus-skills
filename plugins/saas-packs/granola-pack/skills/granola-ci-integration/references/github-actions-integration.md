# Github Actions Integration

## GitHub Actions Integration

### Workflow: Process Meeting Notes
```yaml
# .github/workflows/process-meeting-notes.yml
name: Process Meeting Notes

on:
  repository_dispatch:
    types: [granola-meeting-completed]

jobs:
  process-notes:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Parse Meeting Notes
        id: parse
        run: |
          echo "Processing meeting: ${{ github.event.client_payload.title }}"
          echo "Date: ${{ github.event.client_payload.date }}"

      - name: Update Meeting Log
        run: |
          # Append to meetings log
          echo "| ${{ github.event.client_payload.date }} | ${{ github.event.client_payload.title }} | [Link](${{ github.event.client_payload.url }}) |" >> docs/meetings.md

      - name: Create Issue for Action Items
        uses: actions/github-script@v7
        with:
          script: |
            const actions = JSON.parse('${{ github.event.client_payload.action_items }}');

            for (const action of actions) {
              await github.rest.issues.create({
                owner: context.repo.owner,
                repo: context.repo.repo,
                title: `Meeting Action: ${action.task}`,
                body: `From: ${{ github.event.client_payload.title }}\n\n${action.task}`,
                labels: ['meeting-action']
              });
            }

      - name: Commit Changes
        run: |
          git config user.name "Granola Bot"
          git config user.email "bot@granola.ai"
          git add docs/meetings.md
          git commit -m "docs: add meeting notes from ${{ github.event.client_payload.date }}"
          git push
```

### Trigger Workflow from Zapier
```yaml
# Zapier Webhook Action
Method: POST
URL: https://api.github.com/repos/your-org/your-repo/dispatches
Headers:
  Authorization: Bearer {{github_token}}
  Accept: application/vnd.github.v3+json
Body:
  {
    "event_type": "granola-meeting-completed",
    "client_payload": {
      "title": "{{meeting_title}}",
      "date": "{{meeting_date}}",
      "url": "{{granola_link}}",
      "summary": "{{summary}}",
      "action_items": {{action_items_json}}
    }
  }
```