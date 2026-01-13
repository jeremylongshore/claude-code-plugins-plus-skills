# Implementation Guide

### Step 1: Define Roles
```typescript
// rbac/roles.ts
interface Role {
  name: string;
  description: string;
  permissions: Permission[];
}

enum Permission {
  // Agent permissions
  AGENT_CREATE = 'agent:create',
  AGENT_READ = 'agent:read',
  AGENT_UPDATE = 'agent:update',
  AGENT_DELETE = 'agent:delete',
  AGENT_RUN = 'agent:run',

  // Automation permissions
  AUTOMATION_CREATE = 'automation:create',
  AUTOMATION_READ = 'automation:read',
  AUTOMATION_UPDATE = 'automation:update',
  AUTOMATION_DELETE = 'automation:delete',

  // Admin permissions
  USER_MANAGE = 'user:manage',
  BILLING_VIEW = 'billing:view',
  AUDIT_VIEW = 'audit:view',
  SETTINGS_MANAGE = 'settings:manage',
}

const roles: Role[] = [
  {
    name: 'viewer',
    description: 'Read-only access to agents and runs',
    permissions: [
      Permission.AGENT_READ,
      Permission.AUTOMATION_READ,
    ],
  },
  {
    name: 'developer',
    description: 'Create and manage agents',
    permissions: [
      Permission.AGENT_CREATE,
      Permission.AGENT_READ,
      Permission.AGENT_UPDATE,
      Permission.AGENT_RUN,
      Permission.AUTOMATION_CREATE,
      Permission.AUTOMATION_READ,
      Permission.AUTOMATION_UPDATE,
    ],
  },
  {
    name: 'operator',
    description: 'Run agents and view automations',
    permissions: [
      Permission.AGENT_READ,
      Permission.AGENT_RUN,
      Permission.AUTOMATION_READ,
    ],
  },
  {
    name: 'admin',
    description: 'Full administrative access',
    permissions: Object.values(Permission),
  },
];
```

### Step 2: Implement Permission Checker
```typescript
// rbac/checker.ts
import { Lindy } from '@lindy-ai/sdk';

class PermissionChecker {
  private lindy: Lindy;
  private userPermissions: Map<string, Permission[]> = new Map();

  constructor() {
    this.lindy = new Lindy({ apiKey: process.env.LINDY_API_KEY });
  }

  async loadUserPermissions(userId: string): Promise<Permission[]> {
    // Get user's role from Lindy
    const user = await this.lindy.users.get(userId);
    const role = roles.find(r => r.name === user.role);

    if (!role) {
      throw new Error(`Unknown role: ${user.role}`);
    }

    this.userPermissions.set(userId, role.permissions);
    return role.permissions;
  }

  hasPermission(userId: string, permission: Permission): boolean {
    const permissions = this.userPermissions.get(userId);
    if (!permissions) {
      return false;
    }
    return permissions.includes(permission);
  }

  requirePermission(userId: string, permission: Permission): void {
    if (!this.hasPermission(userId, permission)) {
      throw new Error(`Permission denied: ${permission}`);
    }
  }
}
```

### Step 3: Create Protected Operations
```typescript
// rbac/protected-lindy.ts
import { Lindy } from '@lindy-ai/sdk';
import { PermissionChecker, Permission } from './checker';

class ProtectedLindy {
  private lindy: Lindy;
  private checker: PermissionChecker;
  private currentUserId: string;

  constructor(userId: string) {
    this.lindy = new Lindy({ apiKey: process.env.LINDY_API_KEY });
    this.checker = new PermissionChecker();
    this.currentUserId = userId;
  }

  async createAgent(config: any) {
    this.checker.requirePermission(this.currentUserId, Permission.AGENT_CREATE);
    return this.lindy.agents.create(config);
  }

  async runAgent(agentId: string, input: string) {
    this.checker.requirePermission(this.currentUserId, Permission.AGENT_RUN);
    return this.lindy.agents.run(agentId, { input });
  }

  async deleteAgent(agentId: string) {
    this.checker.requirePermission(this.currentUserId, Permission.AGENT_DELETE);
    return this.lindy.agents.delete(agentId);
  }

  async viewBilling() {
    this.checker.requirePermission(this.currentUserId, Permission.BILLING_VIEW);
    return this.lindy.billing.current();
  }
}
```

### Step 4: Team Management
```typescript
// rbac/teams.ts
interface Team {
  id: string;
  name: string;
  members: TeamMember[];
  agents: string[]; // Agent IDs accessible to team
}

interface TeamMember {
  userId: string;
  role: string;
  addedAt: Date;
}

class TeamManager {
  private lindy: Lindy;

  constructor() {
    this.lindy = new Lindy({ apiKey: process.env.LINDY_API_KEY });
  }

  async createTeam(name: string, adminUserId: string): Promise<Team> {
    const team = await this.lindy.teams.create({
      name,
      members: [{ userId: adminUserId, role: 'admin' }],
    });
    return team;
  }

  async addMember(teamId: string, userId: string, role: string): Promise<void> {
    await this.lindy.teams.addMember(teamId, { userId, role });
  }

  async removeMember(teamId: string, userId: string): Promise<void> {
    await this.lindy.teams.removeMember(teamId, userId);
  }

  async assignAgentToTeam(teamId: string, agentId: string): Promise<void> {
    await this.lindy.teams.assignAgent(teamId, agentId);
  }

  async canAccessAgent(userId: string, agentId: string): Promise<boolean> {
    const teams = await this.lindy.teams.list({ userId });

    for (const team of teams) {
      if (team.agents.includes(agentId)) {
        return true;
      }
    }

    return false;
  }
}
```

### Step 5: Audit Logging
```typescript
// rbac/audit.ts
interface AuditEvent {
  timestamp: Date;
  userId: string;
  action: string;
  resource: string;
  resourceId: string;
  result: 'success' | 'denied' | 'error';
  metadata?: Record<string, any>;
}

class AuditLogger {
  async log(event: Omit<AuditEvent, 'timestamp'>): Promise<void> {
    const auditEvent: AuditEvent = {
      ...event,
      timestamp: new Date(),
    };

    // Store audit log
    console.log('AUDIT:', JSON.stringify(auditEvent));

    // Send to SIEM if configured
    if (process.env.SIEM_ENDPOINT) {
      await fetch(process.env.SIEM_ENDPOINT, {
        method: 'POST',
        body: JSON.stringify(auditEvent),
      });
    }
  }
}

// Wrap operations with audit logging
async function auditedOperation<T>(
  operation: () => Promise<T>,
  eventDetails: Omit<AuditEvent, 'timestamp' | 'result'>
): Promise<T> {
  const audit = new AuditLogger();

  try {
    const result = await operation();
    await audit.log({ ...eventDetails, result: 'success' });
    return result;
  } catch (error: any) {
    const result = error.message.includes('Permission denied') ? 'denied' : 'error';
    await audit.log({ ...eventDetails, result, metadata: { error: error.message } });
    throw error;
  }
}
```