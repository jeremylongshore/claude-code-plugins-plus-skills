# Examples

### Webhook Development with ngrok
```bash
# Terminal 1: Start your webhook server
npm run dev

# Terminal 2: Start ngrok tunnel
ngrok http 3000

# Copy the https URL and add to Linear webhook settings
```

### Integration Test Example
```typescript
// tests/integration.test.ts
import { describe, it, expect, afterAll } from "vitest";
import { createTestIssue, cleanupTestIssues } from "../src/test-utils";

describe("Linear Integration", () => {
  const teamKey = "ENG"; // Your test team

  afterAll(async () => {
    await cleanupTestIssues(teamKey);
  });

  it("should create and fetch an issue", async () => {
    const issue = await createTestIssue(teamKey);
    expect(issue).toBeDefined();
    expect(issue?.title).toContain("[TEST]");
  });
});
```