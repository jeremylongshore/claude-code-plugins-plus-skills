# Api Key Scoping

## API Key Scoping

```typescript
// src/lib/rbac/api-key-scope.ts
interface ApiKeyScope {
  permissions: Permission[];
  rateLimit: number;
  ipAllowlist?: string[];
  expiresAt?: Date;
}

export async function createScopedApiKey(
  userId: string,
  scope: ApiKeyScope
): Promise<string> {
  // Validate user has the permissions they're granting
  const userPermissions = await rbac.getUserPermissions(userId);
  const invalidPermissions = scope.permissions.filter(
    p => !userPermissions.includes(p)
  );

  if (invalidPermissions.length > 0) {
    throw new Error(`Cannot grant permissions you don't have: ${invalidPermissions.join(', ')}`);
  }

  // Generate key
  const apiKey = generateSecureKey();

  // Store with scope
  await prisma.apiKey.create({
    data: {
      key: hashApiKey(apiKey),
      userId,
      permissions: scope.permissions,
      rateLimit: scope.rateLimit,
      ipAllowlist: scope.ipAllowlist,
      expiresAt: scope.expiresAt,
    },
  });

  return apiKey;
}

// Middleware to enforce API key scope
export function enforceApiKeyScope(requiredPermissions: Permission[]) {
  return async (req: Request, res: Response, next: NextFunction) => {
    const apiKey = req.headers['x-api-key'];

    if (!apiKey) {
      return res.status(401).json({ error: 'API key required' });
    }

    const keyRecord = await prisma.apiKey.findFirst({
      where: { key: hashApiKey(apiKey as string) },
    });

    if (!keyRecord) {
      return res.status(401).json({ error: 'Invalid API key' });
    }

    // Check expiration
    if (keyRecord.expiresAt && new Date() > keyRecord.expiresAt) {
      return res.status(401).json({ error: 'API key expired' });
    }

    // Check IP allowlist
    if (keyRecord.ipAllowlist?.length > 0) {
      const clientIp = req.ip;
      if (!keyRecord.ipAllowlist.includes(clientIp)) {
        return res.status(403).json({ error: 'IP not allowed' });
      }
    }

    // Check permissions
    const hasPermission = requiredPermissions.every(
      p => keyRecord.permissions.includes(p)
    );

    if (!hasPermission) {
      return res.status(403).json({
        error: 'API key lacks required permissions',
        required: requiredPermissions,
      });
    }

    next();
  };
}
```