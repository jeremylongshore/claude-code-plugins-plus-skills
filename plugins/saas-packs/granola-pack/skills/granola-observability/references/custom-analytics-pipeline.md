# Custom Analytics Pipeline

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