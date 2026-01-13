# Examples

### Complete Agent Creation Flow
```typescript
async function main() {
  // Create agent
  const agent = await createAgent(agentSpec);

  // Configure tools
  await configureTools(agent.id, agentSpec.tools);

  // Test agent
  await testAgent(agent.id);

  console.log(`Agent ${agent.id} is ready!`);
}

main().catch(console.error);
```