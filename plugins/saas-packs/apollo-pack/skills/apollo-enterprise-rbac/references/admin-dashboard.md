# Admin Dashboard

## Admin Dashboard

```typescript
// src/routes/admin/rbac.ts
router.get('/users/:id/permissions',
  requirePermission('admin:users'),
  async (req, res) => {
    const permissions = await rbac.getUserPermissions(req.params.id);
    res.json({ permissions });
  }
);

router.post('/users/:id/roles',
  requirePermission('admin:roles'),
  async (req, res) => {
    const { roles } = req.body;
    await rbac.assignRoles(req.params.id, roles);
    res.json({ success: true });
  }
);

router.get('/audit/access-denied',
  requirePermission('admin:audit'),
  async (req, res) => {
    const logs = await prisma.auditLog.findMany({
      where: { action: 'PERMISSION_DENIED' },
      orderBy: { createdAt: 'desc' },
      take: 100,
    });
    res.json({ logs });
  }
);
```