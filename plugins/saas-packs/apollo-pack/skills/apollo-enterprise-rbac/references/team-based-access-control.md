# Team-Based Access Control

## Team-Based Access Control

```typescript
// src/services/rbac/team-access.ts
export class TeamAccessService {
  async getAccessibleContacts(
    userId: string,
    teamId: string
  ): Promise<string[]> {
    // Check user's team membership
    const membership = await prisma.teamMember.findFirst({
      where: { userId, teamId },
      include: { team: true },
    });

    if (!membership) {
      return [];
    }

    // Build access scope
    const accessScope = await this.buildAccessScope(userId, membership);

    // Return contact IDs user can access
    const contacts = await prisma.contact.findMany({
      where: accessScope,
      select: { id: true },
    });

    return contacts.map(c => c.id);
  }

  private async buildAccessScope(
    userId: string,
    membership: TeamMembership
  ): Promise<any> {
    // Team admins can see all team contacts
    if (membership.role === 'admin' || membership.role === 'manager') {
      return { teamId: membership.teamId };
    }

    // Regular members see own contacts + shared
    return {
      OR: [
        { ownerId: userId },
        { sharedWith: { some: { userId } } },
        { teamId: membership.teamId, isPublic: true },
      ],
    };
  }
}

// Middleware for team-scoped access
export function requireTeamAccess(resourceType: string) {
  return async (req: Request, res: Response, next: NextFunction) => {
    const userId = req.user?.id;
    const resourceId = req.params.id;

    const hasAccess = await teamAccess.canAccessResource(
      userId,
      resourceType,
      resourceId
    );

    if (!hasAccess) {
      return res.status(403).json({
        error: 'You do not have access to this resource',
      });
    }

    next();
  };
}
```