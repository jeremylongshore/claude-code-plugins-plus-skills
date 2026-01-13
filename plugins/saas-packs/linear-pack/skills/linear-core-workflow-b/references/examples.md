# Examples

### Sprint Planning Flow
```typescript
async function setupSprint(options: {
  teamKey: string;
  name: string;
  durationDays: number;
  issueIdentifiers: string[];
}) {
  const teams = await client.teams({ filter: { key: { eq: options.teamKey } } });
  const team = teams.nodes[0];

  const startsAt = new Date();
  const endsAt = new Date();
  endsAt.setDate(endsAt.getDate() + options.durationDays);

  // Create cycle
  const cycleResult = await client.createCycle({
    teamId: team.id,
    name: options.name,
    startsAt: startsAt.toISOString(),
    endsAt: endsAt.toISOString(),
  });

  const cycle = await cycleResult.cycle;

  // Add issues
  for (const identifier of options.issueIdentifiers) {
    const issue = await client.issue(identifier);
    await client.updateIssue(issue.id, { cycleId: cycle!.id });
  }

  return cycle;
}
```