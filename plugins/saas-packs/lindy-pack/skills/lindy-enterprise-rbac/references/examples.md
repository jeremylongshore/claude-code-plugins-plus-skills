# Examples

### Complete RBAC Setup
```typescript
async function setupRBAC() {
  const lindy = new Lindy({ apiKey: process.env.LINDY_API_KEY });

  // Create teams
  const devTeam = await lindy.teams.create({ name: 'Development' });
  const opsTeam = await lindy.teams.create({ name: 'Operations' });

  // Add members with roles
  await lindy.teams.addMember(devTeam.id, { userId: 'user1', role: 'developer' });
  await lindy.teams.addMember(opsTeam.id, { userId: 'user2', role: 'operator' });

  console.log('RBAC configured successfully');
}
```