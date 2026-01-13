# Meeting Patterns Report

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