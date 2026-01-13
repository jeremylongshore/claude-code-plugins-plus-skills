# Rbac Service

## RBAC Service

```typescript
// src/services/rbac/rbac.service.ts
import { User } from '../../models/user.model';
import { ROLES } from '../../lib/rbac/roles';
import { Permission } from '../../lib/rbac/permissions';

export class RBACService {
  async getUserPermissions(userId: string): Promise<Permission[]> {
    const user = await prisma.user.findUnique({
      where: { id: userId },
      include: {
        roles: true,
        customPermissions: true,
      },
    });

    if (!user) {
      return [];
    }

    const permissions = new Set<Permission>();

    // Add role permissions
    for (const role of user.roles) {
      const roleDef = ROLES[role.name];
      if (roleDef) {
        roleDef.permissions.forEach(p => permissions.add(p));
      }
    }

    // Add custom permissions
    user.customPermissions.forEach(p => {
      if (p.granted) {
        permissions.add(p.permission as Permission);
      } else {
        permissions.delete(p.permission as Permission);
      }
    });

    return Array.from(permissions);
  }

  async hasPermission(userId: string, permission: Permission): Promise<boolean> {
    const permissions = await this.getUserPermissions(userId);
    return permissions.includes(permission);
  }

  async hasAnyPermission(userId: string, permissions: Permission[]): Promise<boolean> {
    const userPermissions = await this.getUserPermissions(userId);
    return permissions.some(p => userPermissions.includes(p));
  }

  async hasAllPermissions(userId: string, permissions: Permission[]): Promise<boolean> {
    const userPermissions = await this.getUserPermissions(userId);
    return permissions.every(p => userPermissions.includes(p));
  }
}

export const rbac = new RBACService();
```