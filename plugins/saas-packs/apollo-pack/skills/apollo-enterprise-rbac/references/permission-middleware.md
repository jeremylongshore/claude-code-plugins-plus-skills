# Permission Middleware

## Permission Middleware

```typescript
// src/middleware/rbac.middleware.ts
import { Request, Response, NextFunction } from 'express';
import { rbac } from '../services/rbac/rbac.service';
import { Permission } from '../lib/rbac/permissions';

export function requirePermission(...permissions: Permission[]) {
  return async (req: Request, res: Response, next: NextFunction) => {
    const userId = req.user?.id;

    if (!userId) {
      return res.status(401).json({ error: 'Authentication required' });
    }

    const hasPermission = await rbac.hasAnyPermission(userId, permissions);

    if (!hasPermission) {
      // Audit failed access attempt
      await auditLog.create({
        action: 'PERMISSION_DENIED',
        actor: userId,
        resource: req.path,
        metadata: { requiredPermissions: permissions },
      });

      return res.status(403).json({
        error: 'Permission denied',
        required: permissions,
      });
    }

    next();
  };
}

// Usage in routes
router.get('/contacts',
  requirePermission('contacts:read'),
  contactController.list
);

router.post('/contacts',
  requirePermission('contacts:create'),
  contactController.create
);

router.delete('/contacts/:id',
  requirePermission('contacts:delete'),
  contactController.delete
);

router.post('/search/bulk',
  requirePermission('search:bulk', 'search:advanced'),
  searchController.bulkSearch
);
```