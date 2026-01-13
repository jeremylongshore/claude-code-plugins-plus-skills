# Implementation Guide

### Step 1: Define Roles and Permissions
```typescript
// models/rbac.ts
enum Permission {
  // Presentation permissions
  PRESENTATION_VIEW = 'presentation:view',
  PRESENTATION_CREATE = 'presentation:create',
  PRESENTATION_EDIT_OWN = 'presentation:edit:own',
  PRESENTATION_EDIT_TEAM = 'presentation:edit:team',
  PRESENTATION_EDIT_ALL = 'presentation:edit:all',
  PRESENTATION_DELETE = 'presentation:delete',
  PRESENTATION_EXPORT = 'presentation:export',

  // Team permissions
  TEAM_VIEW = 'team:view',
  TEAM_MANAGE = 'team:manage',

  // Workspace permissions
  WORKSPACE_VIEW = 'workspace:view',
  WORKSPACE_MANAGE = 'workspace:manage',

  // Admin permissions
  BILLING_VIEW = 'billing:view',
  BILLING_MANAGE = 'billing:manage',
  API_KEYS_MANAGE = 'api_keys:manage',
}

interface Role {
  name: string;
  permissions: Permission[];
  inherits?: string;
}

const roles: Record<string, Role> = {
  viewer: {
    name: 'Viewer',
    permissions: [
      Permission.PRESENTATION_VIEW,
      Permission.TEAM_VIEW,
      Permission.WORKSPACE_VIEW,
    ],
  },
  editor: {
    name: 'Editor',
    permissions: [
      Permission.PRESENTATION_CREATE,
      Permission.PRESENTATION_EDIT_OWN,
      Permission.PRESENTATION_EXPORT,
    ],
    inherits: 'viewer',
  },
  team_lead: {
    name: 'Team Lead',
    permissions: [
      Permission.PRESENTATION_EDIT_TEAM,
      Permission.PRESENTATION_DELETE,
      Permission.TEAM_MANAGE,
    ],
    inherits: 'editor',
  },
  workspace_admin: {
    name: 'Workspace Admin',
    permissions: [
      Permission.PRESENTATION_EDIT_ALL,
      Permission.WORKSPACE_MANAGE,
      Permission.BILLING_VIEW,
    ],
    inherits: 'team_lead',
  },
  org_admin: {
    name: 'Organization Admin',
    permissions: [
      Permission.BILLING_MANAGE,
      Permission.API_KEYS_MANAGE,
    ],
    inherits: 'workspace_admin',
  },
};
```

### Step 2: Permission Resolution
```typescript
// services/rbac-service.ts
class RBACService {
  private rolePermissions: Map<string, Set<Permission>> = new Map();

  constructor() {
    this.resolveRoleHierarchy();
  }

  private resolveRoleHierarchy() {
    const resolve = (roleName: string): Set<Permission> => {
      if (this.rolePermissions.has(roleName)) {
        return this.rolePermissions.get(roleName)!;
      }

      const role = roles[roleName];
      const permissions = new Set<Permission>(role.permissions);

      if (role.inherits) {
        const inherited = resolve(role.inherits);
        inherited.forEach(p => permissions.add(p));
      }

      this.rolePermissions.set(roleName, permissions);
      return permissions;
    };

    Object.keys(roles).forEach(resolve);
  }

  hasPermission(userRole: string, permission: Permission): boolean {
    const permissions = this.rolePermissions.get(userRole);
    return permissions?.has(permission) ?? false;
  }

  getAllPermissions(userRole: string): Permission[] {
    return Array.from(this.rolePermissions.get(userRole) ?? []);
  }
}

export const rbac = new RBACService();
```

### Step 3: Authorization Middleware
```typescript
// middleware/authorize.ts
import { rbac } from '../services/rbac-service';

function authorize(...requiredPermissions: Permission[]) {
  return async (req: Request, res: Response, next: NextFunction) => {
    const user = req.user;

    if (!user) {
      return res.status(401).json({ error: 'Unauthorized' });
    }

    const userRole = await getUserRole(user.id, req.params.workspaceId);

    const hasAllPermissions = requiredPermissions.every(permission =>
      rbac.hasPermission(userRole, permission)
    );

    if (!hasAllPermissions) {
      return res.status(403).json({
        error: 'Forbidden',
        required: requiredPermissions,
        userRole,
      });
    }

    next();
  };
}

// Usage in routes
app.post('/api/presentations',
  authorize(Permission.PRESENTATION_CREATE),
  async (req, res) => {
    const presentation = await gamma.presentations.create(req.body);
    res.json(presentation);
  }
);

app.delete('/api/presentations/:id',
  authorize(Permission.PRESENTATION_DELETE),
  async (req, res) => {
    await gamma.presentations.delete(req.params.id);
    res.status(204).send();
  }
);
```

### Step 4: Resource-Level Authorization
```typescript
// services/resource-auth.ts
interface ResourcePolicy {
  action: string;
  conditions: (user: User, resource: any) => boolean;
}

const presentationPolicies: ResourcePolicy[] = [
  {
    action: 'edit',
    conditions: (user, presentation) => {
      // Owner can always edit
      if (presentation.ownerId === user.id) return true;

      // Team leads can edit team presentations
      if (user.role === 'team_lead' && presentation.teamId === user.teamId) {
        return true;
      }

      // Workspace admins can edit all
      if (user.role === 'workspace_admin' || user.role === 'org_admin') {
        return true;
      }

      return false;
    },
  },
];

async function canPerformAction(
  user: User,
  action: string,
  resource: any
): Promise<boolean> {
  const policy = presentationPolicies.find(p => p.action === action);
  return policy?.conditions(user, resource) ?? false;
}

// Usage
app.put('/api/presentations/:id', async (req, res) => {
  const presentation = await db.presentations.findUnique({
    where: { id: req.params.id },
  });

  if (!await canPerformAction(req.user, 'edit', presentation)) {
    return res.status(403).json({ error: 'Cannot edit this presentation' });
  }

  // Proceed with edit
});
```

### Step 5: Multi-Tenant Isolation
```typescript
// middleware/tenant.ts
async function tenantIsolation(req: Request, res: Response, next: NextFunction) {
  const user = req.user;
  const workspaceId = req.params.workspaceId || req.headers['x-workspace-id'];

  // Verify user belongs to workspace
  const membership = await db.workspaceMemberships.findUnique({
    where: {
      userId_workspaceId: {
        userId: user.id,
        workspaceId: workspaceId,
      },
    },
  });

  if (!membership) {
    return res.status(403).json({ error: 'Not a member of this workspace' });
  }

  // Attach workspace context
  req.workspace = await db.workspaces.findUnique({
    where: { id: workspaceId },
  });

  req.userRole = membership.role;

  next();
}

// All workspace routes use tenant isolation
app.use('/api/workspaces/:workspaceId', tenantIsolation);
```

### Step 6: Audit Authorization Events
```typescript
// lib/auth-audit.ts
async function logAuthorizationEvent(
  userId: string,
  action: string,
  resource: string,
  resourceId: string,
  granted: boolean,
  reason?: string
) {
  await db.authAuditLog.create({
    data: {
      userId,
      action,
      resource,
      resourceId,
      granted,
      reason,
      timestamp: new Date(),
    },
  });

  if (!granted) {
    // Alert on suspicious denied access
    metrics.increment('authorization.denied', {
      action,
      resource,
    });
  }
}
```