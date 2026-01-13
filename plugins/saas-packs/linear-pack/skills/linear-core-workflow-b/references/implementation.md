# Implementation Guide

### Step 1: Project Management
```typescript
import { LinearClient } from "@linear/sdk";

const client = new LinearClient({ apiKey: process.env.LINEAR_API_KEY });

// List all projects
async function getProjects(teamKey?: string) {
  const filter = teamKey
    ? { accessibleTeams: { some: { key: { eq: teamKey } } } }
    : undefined;

  const projects = await client.projects({ filter });
  return projects.nodes;
}

// Create a project
async function createProject(options: {
  name: string;
  description?: string;
  teamIds: string[];
  targetDate?: Date;
  state?: "planned" | "started" | "paused" | "completed" | "canceled";
}) {
  const result = await client.createProject({
    name: options.name,
    description: options.description,
    teamIds: options.teamIds,
    targetDate: options.targetDate?.toISOString(),
    state: options.state ?? "planned",
  });

  return result.project;
}

// Update project status
async function updateProjectStatus(
  projectId: string,
  status: "planned" | "started" | "paused" | "completed" | "canceled"
) {
  return client.updateProject(projectId, { state: status });
}
```

### Step 2: Cycle (Sprint) Management
```typescript
// Get current and upcoming cycles
async function getActiveCycles(teamKey: string) {
  const teams = await client.teams({ filter: { key: { eq: teamKey } } });
  const team = teams.nodes[0];

  const now = new Date().toISOString();
  const cycles = await team.cycles({
    filter: {
      or: [
        { endsAt: { gte: now } }, // Current or future
        { startsAt: { gte: now } }, // Future
      ],
    },
    orderBy: "startsAt",
  });

  return cycles.nodes;
}

// Create a new cycle
async function createCycle(options: {
  teamId: string;
  name?: string;
  startsAt: Date;
  endsAt: Date;
}) {
  const result = await client.createCycle({
    teamId: options.teamId,
    name: options.name,
    startsAt: options.startsAt.toISOString(),
    endsAt: options.endsAt.toISOString(),
  });

  return result.cycle;
}

// Add issues to a cycle
async function addIssuesToCycle(issueIds: string[], cycleId: string) {
  const results = await Promise.all(
    issueIds.map(issueId =>
      client.updateIssue(issueId, { cycleId })
    )
  );

  return results.filter(r => r.success).length;
}

// Get cycle metrics
async function getCycleMetrics(cycleId: string) {
  const cycle = await client.cycle(cycleId);
  const issues = await cycle.issues();

  const states = new Map<string, number>();
  let totalEstimate = 0;
  let completedEstimate = 0;

  for (const issue of issues.nodes) {
    const state = await issue.state;
    const stateName = state?.name ?? "Unknown";
    states.set(stateName, (states.get(stateName) ?? 0) + 1);

    totalEstimate += issue.estimate ?? 0;
    if (state?.type === "completed") {
      completedEstimate += issue.estimate ?? 0;
    }
  }

  return {
    totalIssues: issues.nodes.length,
    byState: Object.fromEntries(states),
    totalEstimate,
    completedEstimate,
    completionRate: totalEstimate ? completedEstimate / totalEstimate : 0,
  };
}
```

### Step 3: Roadmap Operations
```typescript
// Get roadmap items (projects with milestones)
async function getRoadmap(options?: {
  includeCompleted?: boolean;
  monthsAhead?: number;
}) {
  const futureDate = new Date();
  futureDate.setMonth(futureDate.getMonth() + (options?.monthsAhead ?? 6));

  const filter: Record<string, unknown> = {
    targetDate: { lte: futureDate.toISOString() },
  };

  if (!options?.includeCompleted) {
    filter.state = { neq: "completed" };
  }

  const projects = await client.projects({
    filter,
    orderBy: "targetDate",
  });

  return projects.nodes.map(p => ({
    id: p.id,
    name: p.name,
    state: p.state,
    targetDate: p.targetDate,
    progress: p.progress,
  }));
}

// Create project milestone
async function createMilestone(options: {
  projectId: string;
  name: string;
  targetDate: Date;
}) {
  return client.createProjectMilestone({
    projectId: options.projectId,
    name: options.name,
    targetDate: options.targetDate.toISOString(),
  });
}
```

### Step 4: Planning Utilities
```typescript
// Move unfinished issues to next cycle
async function rolloverCycle(fromCycleId: string, toCycleId: string) {
  const fromCycle = await client.cycle(fromCycleId);
  const issues = await fromCycle.issues({
    filter: {
      state: { type: { nin: ["completed", "canceled"] } },
    },
  });

  const movedCount = await addIssuesToCycle(
    issues.nodes.map(i => i.id),
    toCycleId
  );

  return { movedCount, totalUnfinished: issues.nodes.length };
}

// Calculate team velocity
async function calculateVelocity(teamKey: string, cycleCount = 3) {
  const teams = await client.teams({ filter: { key: { eq: teamKey } } });
  const team = teams.nodes[0];

  const cycles = await team.cycles({
    filter: {
      completedAt: { neq: null }
    },
    orderBy: "completedAt",
    first: cycleCount,
  });

  const velocities = await Promise.all(
    cycles.nodes.map(async cycle => {
      const issues = await cycle.issues({
        filter: { state: { type: { eq: "completed" } } },
      });
      return issues.nodes.reduce((sum, i) => sum + (i.estimate ?? 0), 0);
    })
  );

  const avgVelocity = velocities.reduce((a, b) => a + b, 0) / velocities.length;

  return {
    velocities,
    average: Math.round(avgVelocity * 10) / 10,
  };
}
```