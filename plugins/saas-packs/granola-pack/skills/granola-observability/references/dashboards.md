# Dashboards

## Dashboards

### Metabase/Looker Dashboard
```yaml
Dashboard: Granola Analytics

Cards:
  1. Meeting Volume:
     Type: Time series
     Metric: Daily meeting count
     Timeframe: Last 30 days

  2. Active Users:
     Type: Number
     Metric: Unique users (7 days)

  3. Time in Meetings:
     Type: Bar chart
     Metric: Hours per team
     Breakdown: By workspace

  4. Action Items:
     Type: Line chart
     Metric: Actions created vs completed
     Timeframe: Last 90 days

  5. Top Meeting Types:
     Type: Pie chart
     Metric: Meeting count
     Breakdown: By template

  6. Adoption Trend:
     Type: Area chart
     Metric: Active users over time
     Timeframe: Last 6 months
```

### Slack Reporting
```yaml
# Weekly Digest Automation

Schedule: Every Monday 9 AM

Slack Message:
  Channel: #leadership
  Blocks:
    - header: "Weekly Meeting Analytics"
    - section:
        text: |
          *Last Week Summary*
          - Meetings: {{total_meetings}}
          - Hours: {{total_hours}}
          - Action Items: {{total_actions}}
          - Completion Rate: {{completion_rate}}%

          *Top Insights*
          - Busiest day: {{busiest_day}}
          - Most meetings: {{top_user}}
          - Largest meeting: {{largest_meeting}}
```