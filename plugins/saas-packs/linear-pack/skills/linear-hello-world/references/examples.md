# Examples

### Complete Hello World Script
```typescript
import { LinearClient } from "@linear/sdk";

async function helloLinear() {
  const client = new LinearClient({
    apiKey: process.env.LINEAR_API_KEY
  });

  // 1. Get current user
  const viewer = await client.viewer;
  console.log(`Hello, ${viewer.name}!`);

  // 2. List teams
  const teams = await client.teams();
  const team = teams.nodes[0];
  console.log(`Using team: ${team.name}`);

  // 3. Create issue
  const result = await client.createIssue({
    teamId: team.id,
    title: "Hello from Linear SDK!",
    description: "Testing the Linear API integration.",
    priority: 2, // Medium priority
  });

  if (result.success) {
    const issue = await result.issue;
    console.log(`Created: ${issue?.identifier}`);
  }

  // 4. Query issues
  const issues = await client.issues({ first: 5 });
  console.log(`\nYour latest ${issues.nodes.length} issues:`);
  issues.nodes.forEach(i => console.log(`  - ${i.identifier}: ${i.title}`));
}

helloLinear().catch(console.error);
```

### Using GraphQL Directly
```typescript
const query = `
  query Me {
    viewer {
      id
      name
      email
    }
  }
`;

const response = await fetch("https://api.linear.app/graphql", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "Authorization": process.env.LINEAR_API_KEY,
  },
  body: JSON.stringify({ query }),
});

const data = await response.json();
console.log(data);
```