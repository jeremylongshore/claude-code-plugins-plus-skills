# Examples

### Complete Issue Creation Flow
```typescript
async function createFeatureIssue(options: {
  teamKey: string;
  title: string;
  description: string;
  priority: 1 | 2 | 3 | 4;
}) {
  // Get team and default state
  const teams = await client.teams({ filter: { key: { eq: options.teamKey } } });
  const team = teams.nodes[0];

  // Get "Backlog" state
  const states = await team.states();
  const backlog = states.nodes.find(s => s.name === "Backlog");

  // Create issue
  const result = await client.createIssue({
    teamId: team.id,
    title: options.title,
    description: options.description,
    priority: options.priority,
    stateId: backlog?.id,
  });

  const issue = await result.issue;

  // Add initial comment
  await client.createComment({
    issueId: issue!.id,
    body: "Issue created via API integration",
  });

  return issue;
}
```