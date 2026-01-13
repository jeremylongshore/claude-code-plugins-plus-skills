# Export & Reporting

## Export & Reporting

### Scheduled Reports
```yaml
# Monthly Executive Report

Schedule: 1st of month

Content:
  - Total meetings YTD
  - Meeting time per employee
  - Action item velocity
  - Top meeting participants
  - Cost savings estimate

Format: PDF
Recipients: leadership@company.com
```

### API Export
```bash
# If custom API access available (Enterprise)
curl -X GET "https://api.granola.ai/v1/analytics" \
  -H "Authorization: Bearer $GRANOLA_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "start_date": "2025-01-01",
    "end_date": "2025-01-31",
    "metrics": ["meeting_count", "duration", "action_items"]
  }'
```