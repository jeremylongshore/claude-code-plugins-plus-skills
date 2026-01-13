---
name: deepgram-enterprise-rbac
license: MIT
allowed-tools: Read, Write, Edit, Bash
description: Configure enterprise role-based access control for Deepgram integrations.
  Use when implementing team permissions, managing API key scopes, or setting up organization-level
  access controls. Trigger with phrases like "deepgram RBAC", "deepgram permi...
---
# Deepgram Enterprise RBAC

## Overview
Implement role-based access control for enterprise Deepgram deployments with team management and scoped permissions.

## Prerequisites
- Deepgram enterprise account
- Multiple projects configured
- Team management system
- Audit logging enabled

## Deepgram Permission Scopes

| Scope | Description | Use Case |
|-------|-------------|----------|
| `listen:*` | All transcription operations | Production services |
| `manage:*` | All management operations | Admin users |
| `usage:read` | View usage data | Billing team |
| `usage:write` | Modify usage | Service accounts |
| `keys:read` | View API keys | Security audits |
| `keys:write` | Create/delete keys | Admin users |

## Role Definitions

```typescript
// config/roles.ts
export interface Role {
  name: string;
  description: string;
  deepgramScopes: string[];
  appPermissions: string[];
}

export const roles: Record<string, Role> = {
  admin: {
    name: 'Administrator',
    description: 'Full access to all Deepgram resources',
    deepgramScopes: ['manage:*', 'listen:*', 'usage:*', 'keys:*'],
    appPermissions: ['*'],
  },
  developer: {
    name: 'Developer',
    description: 'Transcription and development access',
    deepgramScopes: ['listen:*', 'usage:read'],
    appPermissions: [
      'transcription:create',
      'transcription:read',
      'projects:read',
    ],
  },
  analyst: {
    name: 'Analyst',
    description: 'Read-only access to transcriptions and usage',
    deepgramScopes: ['usage:read'],
    appPermissions: [
      'transcription:read',
      'usage:read',
      'reports:read',
    ],
  },
  service: {
    name: 'Service Account',
    description: 'Automated service access',
    deepgramScopes: ['listen:*'],
    appPermissions: [
      'transcription:create',
      'transcription:read',
    ],
  },
  auditor: {
    name: 'Auditor',
    description: 'Security and compliance access',
    deepgramScopes: ['usage:read', 'keys:read'],
    appPermissions: [
      'audit:read',
      'usage:read',
      'keys:read',
    ],
  },
};
```

## Implementation

### RBAC Service
```typescript
// services/rbac.ts
import { createClient } from '@deepgram/sdk';
import { roles, Role } from '../config/roles';
import { db } from './database';

interface User {
  id: string;
  email: string;
  role: string;
  teamId: string;
  apiKeyId?: string;
}

interface Team {
  id: string;
  name: string;
  projectId: string;
  members: string[];
}

export class RBACService {
  private adminClient;

  constructor(adminApiKey: string) {
    this.adminClient = createClient(adminApiKey);
  }

  async createUserApiKey(user: User): Promise<string> {
    const role = roles[user.role];
    if (!role) {
      throw new Error(`Unknown role: ${user.role}`);
    }

    const team = await db.teams.findOne({ id: user.teamId });
    if (!team) {
      throw new Error(`Team not found: ${user.teamId}`);
    }

    // Create scoped API key
    const { result, error } = await this.adminClient.manage.createProjectKey(
      team.projectId,
      {
        comment: `User: ${user.email} | Role: ${role.name}`,
        scopes: role.deepgramScopes,
        expiration_date: this.getExpirationDate(role),
      }
    );

    if (error) throw error;

    // Store key reference (not the key itself)
    await db.users.updateOne(
      { id: user.id },
      { $set: { apiKeyId: result.key_id } }
    );

    // Log key creation
    await this.auditLog('KEY_CREATED', user.id, {
      keyId: result.key_id,
      role: user.role,
      scopes: role.deepgramScopes,
    });

    return result.key;
  }

  async revokeUserApiKey(userId: string): Promise<void> {
    const user = await db.users.findOne({ id: userId });
    if (!user?.apiKeyId) return;

    const team = await db.teams.findOne({ id: user.teamId });
    if (!team) return;

    await this.adminClient.manage.deleteProjectKey(
      team.projectId,
      user.apiKeyId
    );

    await db.users.updateOne(
      { id: userId },
      { $unset: { apiKeyId: '' } }
    );

    await this.auditLog('KEY_REVOKED', userId, {
      keyId: user.apiKeyId,
    });
  }

  async checkPermission(
    userId: string,
    permission: string
  ): Promise<boolean> {
    const user = await db.users.findOne({ id: userId });
    if (!user) return false;

    const role = roles[user.role];
    if (!role) return false;

    // Check wildcard
    if (role.appPermissions.includes('*')) return true;

    // Check specific permission
    return role.appPermissions.includes(permission);
  }

  async updateUserRole(userId: string, newRole: string): Promise<void> {
    const role = roles[newRole];
    if (!role) {
      throw new Error(`Unknown role: ${newRole}`);
    }

    const user = await db.users.findOne({ id: userId });
    if (!user) {
      throw new Error(`User not found: ${userId}`);
    }

    // Revoke old key
    if (user.apiKeyId) {
      await this.revokeUserApiKey(userId);
    }

    // Update role
    await db.users.updateOne(
      { id: userId },
      { $set: { role: newRole } }
    );

    // Create new key with new scopes
    await this.createUserApiKey({ ...user, role: newRole });

    await this.auditLog('ROLE_CHANGED', userId, {
      oldRole: user.role,
      newRole,
    });
  }

  private getExpirationDate(role: Role): Date {
    const days = role.name === 'Service Account' ? 90 : 365;
    const date = new Date();
    date.setDate(date.getDate() + days);
    return date;
  }

  private async auditLog(
    action: string,
    userId: string,
    details: Record<string, unknown>
  ): Promise<void> {
    await db.auditLog.insertOne({
      timestamp: new Date(),
      action,
      userId,
      details,
    });
  }
}
```

### Permission Middleware
```typescript
// middleware/authorization.ts
import { Request, Response, NextFunction } from 'express';
import { RBACService } from '../services/rbac';

const rbac = new RBACService(process.env.DEEPGRAM_ADMIN_KEY!);

export function requirePermission(permission: string) {
  return async (req: Request, res: Response, next: NextFunction) => {
    const userId = req.user?.id;

    if (!userId) {
      return res.status(401).json({ error: 'Unauthorized' });
    }

    const hasPermission = await rbac.checkPermission(userId, permission);

    if (!hasPermission) {
      return res.status(403).json({
        error: 'Forbidden',
        message: `Missing permission: ${permission}`,
      });
    }

    next();
  };
}

// Usage in routes
app.post(
  '/transcribe',
  requirePermission('transcription:create'),
  transcribeHandler
);

app.get(
  '/usage',
  requirePermission('usage:read'),
  usageHandler
);

app.post(
  '/admin/keys',
  requirePermission('keys:write'),
  createKeyHandler
);
```

### Team Management
```typescript
// services/teams.ts
import { RBACService } from './rbac';
import { db } from './database';

interface CreateTeamRequest {
  name: string;
  projectId: string;
  adminUserId: string;
}

export class TeamService {
  private rbac: RBACService;

  constructor(rbac: RBACService) {
    this.rbac = rbac;
  }

  async createTeam(request: CreateTeamRequest): Promise<string> {
    const teamId = crypto.randomUUID();

    // Create team
    await db.teams.insertOne({
      id: teamId,
      name: request.name,
      projectId: request.projectId,
      members: [request.adminUserId],
      createdAt: new Date(),
    });

    // Set admin as team admin
    await db.users.updateOne(
      { id: request.adminUserId },
      { $set: { teamId, role: 'admin' } }
    );

    // Create API key for admin
    const user = await db.users.findOne({ id: request.adminUserId });
    if (user) {
      await this.rbac.createUserApiKey(user);
    }

    return teamId;
  }

  async addMember(
    teamId: string,
    userId: string,
    role: string
  ): Promise<void> {
    // Update team
    await db.teams.updateOne(
      { id: teamId },
      { $addToSet: { members: userId } }
    );

    // Update user
    await db.users.updateOne(
      { id: userId },
      { $set: { teamId, role } }
    );

    // Create API key
    const user = await db.users.findOne({ id: userId });
    if (user) {
      await this.rbac.createUserApiKey(user);
    }
  }

  async removeMember(teamId: string, userId: string): Promise<void> {
    // Revoke API key
    await this.rbac.revokeUserApiKey(userId);

    // Remove from team
    await db.teams.updateOne(
      { id: teamId },
      { $pull: { members: userId } }
    );

    // Clear user team
    await db.users.updateOne(
      { id: userId },
      { $unset: { teamId: '', role: '' } }
    );
  }

  async getTeamUsage(teamId: string): Promise<{
    totalMinutes: number;
    byMember: Array<{ userId: string; minutes: number }>;
  }> {
    const team = await db.teams.findOne({ id: teamId });
    if (!team) throw new Error('Team not found');

    const usage = await db.usage.aggregate([
      { $match: { userId: { $in: team.members } } },
      {
        $group: {
          _id: '$userId',
          minutes: { $sum: '$audioMinutes' },
        },
      },
    ]).toArray();

    return {
      totalMinutes: usage.reduce((sum, u) => sum + u.minutes, 0),
      byMember: usage.map(u => ({
        userId: u._id,
        minutes: u.minutes,
      })),
    };
  }
}
```

### API Key Rotation
```typescript
// services/key-rotation.ts
import { RBACService } from './rbac';
import { db } from './database';

export class KeyRotationService {
  private rbac: RBACService;

  constructor(rbac: RBACService) {
    this.rbac = rbac;
  }

  async rotateExpiredKeys(): Promise<{
    rotated: number;
    failed: number;
  }> {
    const stats = { rotated: 0, failed: 0 };

    // Find users with keys expiring soon
    const expiringUsers = await db.users.find({
      keyExpiration: {
        $lt: new Date(Date.now() + 7 * 24 * 60 * 60 * 1000), // 7 days
      },
    }).toArray();

    for (const user of expiringUsers) {
      try {
        // Revoke old key
        await this.rbac.revokeUserApiKey(user.id);

        // Create new key
        await this.rbac.createUserApiKey(user);

        // Notify user
        await this.notifyKeyRotation(user);

        stats.rotated++;
      } catch (error) {
        console.error(`Failed to rotate key for ${user.id}:`, error);
        stats.failed++;
      }
    }

    return stats;
  }

  private async notifyKeyRotation(user: any): Promise<void> {
    // Send email notification
    // Implementation depends on your notification system
  }
}
```

### Admin Dashboard API
```typescript
// routes/admin.ts
import express from 'express';
import { requirePermission } from '../middleware/authorization';
import { RBACService } from '../services/rbac';
import { TeamService } from '../services/teams';

const router = express.Router();
const rbac = new RBACService(process.env.DEEPGRAM_ADMIN_KEY!);
const teams = new TeamService(rbac);

// List all users
router.get(
  '/users',
  requirePermission('admin:users:read'),
  async (req, res) => {
    const users = await db.users.find({}).toArray();
    res.json({ users });
  }
);

// Update user role
router.patch(
  '/users/:id/role',
  requirePermission('admin:users:write'),
  async (req, res) => {
    const { role } = req.body;
    await rbac.updateUserRole(req.params.id, role);
    res.json({ success: true });
  }
);

// Create team
router.post(
  '/teams',
  requirePermission('admin:teams:write'),
  async (req, res) => {
    const teamId = await teams.createTeam(req.body);
    res.json({ teamId });
  }
);

// Get team usage
router.get(
  '/teams/:id/usage',
  requirePermission('admin:usage:read'),
  async (req, res) => {
    const usage = await teams.getTeamUsage(req.params.id);
    res.json(usage);
  }
);

// Rotate API key
router.post(
  '/users/:id/rotate-key',
  requirePermission('admin:keys:write'),
  async (req, res) => {
    await rbac.revokeUserApiKey(req.params.id);
    const user = await db.users.findOne({ id: req.params.id });
    if (user) {
      const newKey = await rbac.createUserApiKey(user);
      res.json({ success: true, keyCreated: true });
    } else {
      res.status(404).json({ error: 'User not found' });
    }
  }
);

export default router;
```

## Resources
- [Deepgram API Key Management](https://developers.deepgram.com/docs/api-key-management)
- [Project Management](https://developers.deepgram.com/docs/projects)
- [Enterprise Features](https://deepgram.com/enterprise)

## Next Steps
Proceed to `deepgram-migration-deep-dive` for complex migration scenarios.
