---
name: granola-performance-tuning
license: MIT
allowed-tools: Read, Write, Edit
description: Optimize Granola transcription quality and note performance. Use when
  improving transcription accuracy, reducing processing time, or enhancing note quality.
  Trigger with phrases like "granola performance", "granola accuracy", "granola quality",
  "i...
---
# Granola Performance Tuning

## Overview
Optimize Granola for best transcription accuracy and note quality.

## Transcription Quality Factors

### Audio Quality Hierarchy
```
Transcription Accuracy
        ↑
[Professional Microphone] 98%
        ↑
[Quality Headset Mic] 95%
        ↑
[Laptop Built-in Mic] 85%
        ↑
[Phone Speaker] 70%
```

### Environmental Factors
| Factor | Impact | Optimization |
|--------|--------|--------------|
| Background noise | High | Use quiet room, noise cancellation |
| Echo/reverb | High | Soft furnishings, smaller room |
| Distance from mic | Medium | Within 12 inches of microphone |
| Multiple speakers | Medium | Use identification phrases |
| Accent variation | Low | Improves over time with usage |

## Audio Setup Optimization

### Recommended Equipment
```markdown
## Microphone Recommendations

Budget (~$50):
- Blue Snowball iCE
- Fifine K669

Mid-Range (~$100):
- Blue Yeti
- Rode NT-USB Mini
- Audio-Technica AT2020USB+

Professional (~$200+):
- Shure MV7
- Elgato Wave:3
- Rode PodMic + interface
```

### Microphone Settings (macOS)
```bash
# Check current input device
system_profiler SPAudioDataType | grep -A5 "Default Input"

# Adjust input volume (System Preferences)
# Aim for: Input level peaks at 75% during normal speech
```

### Room Optimization
```markdown
## Environment Checklist
- [ ] Close windows to reduce outside noise
- [ ] Turn off fans, AC if possible
- [ ] Use soft surfaces (carpet, curtains)
- [ ] Position away from keyboard clicks
- [ ] Mute when not speaking
```

## Note Quality Optimization

### Meeting Preparation
```markdown
## Pre-Meeting Checklist
- [ ] Share agenda in advance
- [ ] Send attendee list to calendar
- [ ] Prepare context notes in template
- [ ] Test audio before meeting
```

### During Meeting
```markdown
## Best Practices
1. State names when addressing people
   "Sarah, what do you think about..."

2. Summarize decisions verbally
   "So we're agreed: deadline is Friday."

3. Spell out technical terms
   "The API endpoint, A-P-I..."

4. Avoid crosstalk
   One person speaking at a time

5. Use clear action item language
   "Action item: Mike will review the PR by Thursday."
```

### Post-Meeting Enhancement
```markdown
## Note Review Checklist (5 min)
- [ ] Correct obvious transcription errors
- [ ] Add context AI might have missed
- [ ] Verify action items are complete
- [ ] Add links to referenced documents
- [ ] Tag key decisions
```

## Template Optimization

### Effective Template Structure
```markdown
# Meeting Template: Sprint Planning

## Agenda (Pre-filled)
-

## Context
[Add links to relevant docs]

## Discussion Notes
[AI-enhanced during meeting]

## Decisions
- [ ] Decision 1: [Clear statement]

## Action Items
Format: - [ ] What (@who, by when)

## Follow-up
Next meeting: [date]
```

### Template Best Practices
| Practice | Reason | Impact |
|----------|--------|--------|
| Use headers | Better AI parsing | +20% accuracy |
| Pre-fill context | Reduces ambiguity | +15% relevance |
| Standard formats | Consistent output | +10% usability |
| Action item format | Auto-extraction | +25% detection |

## Processing Speed Optimization

### Factors Affecting Speed
| Factor | Impact | Optimization |
|--------|--------|--------------|
| Meeting length | Linear | Expect 1 min processing per 10 min meeting |
| Internet speed | High | Ensure stable connection during upload |
| Peak times | Medium | Processing queue varies |
| Audio quality | Low | Cleaner audio = faster processing |

### Speed Expectations
```
Meeting Duration → Processing Time
15 minutes → 1-2 minutes
30 minutes → 2-3 minutes
60 minutes → 3-5 minutes
120 minutes → 5-8 minutes
```

## Integration Performance

### Zapier Optimization
```markdown
## Reduce Zapier Latency

1. Use Instant triggers (not polling)
2. Minimize steps in Zap
3. Avoid unnecessary filters
4. Use multi-step Zaps efficiently
5. Monitor task usage
```

### Batch Processing
```yaml
# Instead of real-time, batch for efficiency
Schedule: Every 30 minutes
Process:
  - Collect all new notes
  - Batch update Notion
  - Single Slack summary
  - Aggregate CRM updates
```

## Accuracy Improvement

### Training the AI
```markdown
## Improve Over Time

1. Correct errors when you see them
   - AI learns from corrections

2. Use consistent terminology
   - Builds vocabulary

3. Identify speakers
   - Improves attribution

4. Regular editing
   - Provides feedback loop
```

### Custom Vocabulary
```markdown
## Teach Domain Terms

Add to meeting intros:
"We'll discuss the OAuth2 implementation,
that's O-Auth-Two, and the GraphQL API,
spelled G-R-A-P-H-Q-L..."

Common terms to spell out:
- Acronyms (API, SDK, CI/CD)
- Product names
- People names with unusual spellings
```

## Performance Metrics

### What to Track
| Metric | Target | How to Measure |
|--------|--------|----------------|
| Transcription accuracy | >95% | Sample review |
| Action item detection | >90% | Compare to meeting |
| Processing time | <5 min | Timestamp comparison |
| Note usefulness | 4+/5 | Team survey |

### Weekly Review
```markdown
## Performance Check

Monday:
- [ ] Review last week's meeting notes
- [ ] Note common transcription errors
- [ ] Identify improvement opportunities
- [ ] Adjust templates if needed
```

## Resources
- [Granola Quality Tips](https://granola.ai/tips)
- [Audio Equipment Guide](https://granola.ai/help/audio)

## Next Steps
Proceed to `granola-cost-tuning` for cost optimization strategies.
