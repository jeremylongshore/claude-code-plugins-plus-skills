---
name: granola-observability
license: MIT
allowed-tools: Read, Write, Edit
description: Monitor Granola usage, analytics, and meeting insights. Use when tracking
  meeting patterns, analyzing team productivity, or building meeting analytics dashboards.
  Trigger with phrases like "granola analytics", "granola metrics", "granola monitorin...
---
# Granola Observability

## Overview
Monitor Granola usage, track meeting metrics, and gain insights into team productivity.

## Prerequisites
- Granola Business or Enterprise plan
- Admin access for organization metrics
- Analytics destination (optional: BI tool)

## Built-in Analytics

### Dashboard Metrics
```markdown
## Granola Admin Dashboard

Accessible at: Settings > Analytics

Metrics Available:
- Total meetings captured
- Meeting hours per week
- Active users
- Notes shared
- Action items created
- Integration usage
```

### Individual Metrics
```markdown
## Personal Analytics

View at: Profile > Activity

Metrics:
- Meetings this month
- Time in meetings
- Notes created
- Action items assigned
- Sharing activity
```

## Key Metrics to Track

### Usage Metrics
| Metric | Description | Target |
|--------|-------------|--------|
| Adoption Rate | Active users / Total users | > 80% |
| Capture Rate | Recorded / Eligible meetings | > 70% |
| Edit Rate | Notes edited / Notes created | > 50% |
| Share Rate | Notes shared / Notes created | > 60% |

### Quality Metrics
| Metric | Description | Target |
|--------|-------------|--------|
| Action Item Detection | AI-detected / Actual | > 90% |
| Transcription Accuracy | Correct words / Total | > 95% |
| User Satisfaction | Survey score | > 4.0/5.0 |

### Efficiency Metrics
| Metric | Description | Calculation |
|--------|-------------|-------------|
| Time Saved | Minutes saved per meeting | ~20 min |
| Follow-up Speed | Time to share notes | < 10 min |
| Action Completion | Actions done / Actions created | > 80% |

## Custom Analytics Pipeline

### Export to Data Warehouse
```yaml
# Zapier → BigQuery Pipeline

Trigger: New Granola Note

Transform:
  meeting_id: {{note_id}}
  meeting_date: {{date}}
  duration_minutes: {{duration}}
  attendee_count: {{attendees.count}}
  action_item_count: {{action_items.count}}
  word_count: {{transcript.word_count}}

Load:
  Destination: BigQuery
  Dataset: meetings
  Table: granola_notes
```

### Schema Design
```sql
-- BigQuery Table Schema
CREATE TABLE meetings.granola_notes (
  meeting_id STRING NOT NULL,
  meeting_title STRING,
  meeting_date DATE,
  start_time TIMESTAMP,
  end_time TIMESTAMP,
  duration_minutes INT64,
  attendee_count INT64,
  attendees ARRAY<STRING>,
  action_item_count INT64,
  word_count INT64,
  workspace STRING,
  shared BOOLEAN,
  created_at TIMESTAMP
);

-- Aggregation View
CREATE VIEW meetings.daily_summary AS
SELECT
  meeting_date,
  COUNT(*) as total_meetings,
  SUM(duration_minutes) as total_minutes,
  AVG(attendee_count) as avg_attendees,
  SUM(action_item_count) as total_actions
FROM meetings.granola_notes
GROUP BY meeting_date;
```

### Analytics Queries
```sql
-- Meeting frequency by user
SELECT
  user_email,
  COUNT(*) as meeting_count,
  SUM(duration_minutes) / 60 as hours_in_meetings
FROM meetings.granola_notes
WHERE meeting_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)
GROUP BY user_email
ORDER BY meeting_count DESC;

-- Action item trends
SELECT
  DATE_TRUNC(meeting_date, WEEK) as week,
  SUM(action_item_count) as actions_created,
  COUNT(*) as meetings
FROM meetings.granola_notes
GROUP BY week
ORDER BY week;

-- Peak meeting times
SELECT
  EXTRACT(HOUR FROM start_time) as hour,
  COUNT(*) as meeting_count
FROM meetings.granola_notes
GROUP BY hour
ORDER BY hour;
```

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

## Health Monitoring

### System Health Checks
```markdown
## Daily Health Check

Automated Monitoring:
- [ ] Granola status page: status.granola.ai
- [ ] Integration connectivity
- [ ] Processing latency
- [ ] Error rate

Manual Weekly Check:
- [ ] User adoption trending up
- [ ] Transcription quality stable
- [ ] Action items being captured
- [ ] Integrations firing correctly
```

### Alerting Rules
```yaml
# PagerDuty/Slack Alerts

Alerts:
  - name: Processing Failure Spike
    condition: error_rate > 5%
    window: 15 minutes
    severity: warning
    notify: #ops-alerts

  - name: Integration Down
    condition: integration_health != "healthy"
    window: 5 minutes
    severity: critical
    notify: pagerduty

  - name: Low Adoption
    condition: weekly_active_users < 50%
    window: 7 days
    severity: info
    notify: #product-team
```

## Meeting Intelligence

### Pattern Analysis
```markdown
## Meeting Patterns Report

Weekly Analysis:
1. Meeting distribution by day
2. Peak hours analysis
3. Average meeting duration trends
4. One-on-one vs group ratio
5. External vs internal meeting ratio

Monthly Analysis:
1. Meeting time per person
2. Action item completion rates
3. Cross-functional meeting frequency
4. Recurring meeting effectiveness
```

### Insights Queries
```sql
-- Meeting efficiency score
WITH meeting_scores AS (
  SELECT
    meeting_id,
    CASE
      WHEN action_item_count > 0 THEN 1 ELSE 0
    END as had_actions,
    CASE
      WHEN duration_minutes <= 30 THEN 1 ELSE 0
    END as efficient_length,
    CASE
      WHEN attendee_count <= 5 THEN 1 ELSE 0
    END as right_sized
  FROM meetings.granola_notes
)
SELECT
  AVG(had_actions + efficient_length + right_sized) / 3 as efficiency_score
FROM meeting_scores;
```

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

## Resources
- [Granola Analytics Guide](https://granola.ai/help/analytics)
- [Admin Dashboard](https://app.granola.ai/admin)
- [Status Page](https://status.granola.ai)

## Next Steps
Proceed to `granola-incident-runbook` for incident response procedures.
