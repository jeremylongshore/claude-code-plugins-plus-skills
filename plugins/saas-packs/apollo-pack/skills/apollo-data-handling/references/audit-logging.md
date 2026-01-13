# Audit Logging

## Audit Logging

```typescript
// src/services/audit/audit.service.ts
interface AuditEntry {
  action: string;
  actor: string;
  resource: string;
  resourceId: string;
  changes?: Record<string, { old: any; new: any }>;
  metadata?: Record<string, any>;
  timestamp: Date;
}

export async function logDataAccess(entry: AuditEntry): Promise<void> {
  await prisma.auditLog.create({
    data: {
      action: entry.action,
      actor: entry.actor,
      resource: entry.resource,
      resourceId: entry.resourceId,
      changes: entry.changes ? JSON.stringify(entry.changes) : null,
      metadata: entry.metadata ? JSON.stringify(entry.metadata) : null,
      occurredAt: entry.timestamp,
    },
  });
}

// Middleware to audit all data access
export function auditMiddleware(req: any, res: any, next: any) {
  const originalSend = res.send;

  res.send = function(body: any) {
    // Log data access
    if (req.path.includes('/apollo/') && req.method === 'GET') {
      logDataAccess({
        action: 'DATA_ACCESS',
        actor: req.user?.id || 'anonymous',
        resource: 'apollo_contact',
        resourceId: req.params.id || 'bulk',
        metadata: {
          path: req.path,
          query: req.query,
          responseSize: body?.length,
        },
        timestamp: new Date(),
      });
    }

    return originalSend.call(this, body);
  };

  next();
}
```