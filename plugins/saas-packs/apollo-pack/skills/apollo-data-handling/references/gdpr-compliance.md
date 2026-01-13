# Gdpr Compliance

## GDPR Compliance

### Right to Access (Subject Access Request)

```typescript
// src/services/gdpr/access.service.ts
import { Contact } from '../../models/contact.model';
import { Engagement } from '../../models/engagement.model';

interface SubjectAccessResponse {
  personalData: {
    contact: Partial<Contact>;
    engagements: Partial<Engagement>[];
  };
  processingPurposes: string[];
  dataRetention: string;
  dataSources: string[];
}

export async function handleSubjectAccessRequest(
  email: string
): Promise<SubjectAccessResponse> {
  // Find all data for this subject
  const contact = await prisma.contact.findFirst({
    where: { email },
    select: {
      id: true,
      email: true,
      name: true,
      firstName: true,
      lastName: true,
      title: true,
      phone: true,
      linkedinUrl: true,
      company: {
        select: {
          name: true,
          domain: true,
        },
      },
      createdAt: true,
      updatedAt: true,
    },
  });

  if (!contact) {
    return {
      personalData: { contact: {}, engagements: [] },
      processingPurposes: [],
      dataRetention: 'No data found',
      dataSources: [],
    };
  }

  const engagements = await prisma.engagement.findMany({
    where: { contactId: contact.id },
    select: {
      type: true,
      occurredAt: true,
      sequenceId: true,
    },
  });

  return {
    personalData: {
      contact,
      engagements,
    },
    processingPurposes: [
      'B2B sales outreach',
      'Lead qualification',
      'Marketing communications',
    ],
    dataRetention: '2 years from last activity',
    dataSources: ['Apollo.io API', 'User-provided forms'],
  };
}
```

### Right to Erasure (Right to be Forgotten)

```typescript
// src/services/gdpr/erasure.service.ts
interface ErasureResult {
  success: boolean;
  recordsDeleted: {
    contacts: number;
    engagements: number;
    sequences: number;
  };
  apolloNotified: boolean;
}

export async function handleErasureRequest(email: string): Promise<ErasureResult> {
  const result: ErasureResult = {
    success: false,
    recordsDeleted: { contacts: 0, engagements: 0, sequences: 0 },
    apolloNotified: false,
  };

  try {
    // Start transaction
    await prisma.$transaction(async (tx) => {
      // Find contact
      const contact = await tx.contact.findFirst({ where: { email } });
      if (!contact) {
        throw new Error('Contact not found');
      }

      // Delete engagements
      const deletedEngagements = await tx.engagement.deleteMany({
        where: { contactId: contact.id },
      });
      result.recordsDeleted.engagements = deletedEngagements.count;

      // Remove from sequences
      const deletedSequences = await tx.sequenceEnrollment.deleteMany({
        where: { contactId: contact.id },
      });
      result.recordsDeleted.sequences = deletedSequences.count;

      // Delete contact
      await tx.contact.delete({ where: { id: contact.id } });
      result.recordsDeleted.contacts = 1;

      // Notify Apollo (if they support it)
      try {
        await notifyApolloOfDeletion(email);
        result.apolloNotified = true;
      } catch (e) {
        console.warn('Could not notify Apollo of deletion', e);
      }
    });

    result.success = true;

    // Log for audit
    await auditLog.create({
      type: 'GDPR_ERASURE',
      subject: hashEmail(email), // Don't store email in audit log
      timestamp: new Date(),
      recordsAffected: result.recordsDeleted,
    });

    return result;
  } catch (error) {
    console.error('Erasure request failed:', error);
    throw error;
  }
}

async function notifyApolloOfDeletion(email: string): Promise<void> {
  // Apollo doesn't have a deletion API, but we can:
  // 1. Remove from all sequences
  // 2. Mark as do-not-contact
  // 3. Open support ticket for full removal

  console.log(`Note: Contact Apollo support to fully delete ${email} from their system`);
}
```

### Consent Management

```typescript
// src/services/consent/consent.service.ts
import { z } from 'zod';

const ConsentSchema = z.object({
  email: z.string().email(),
  purposes: z.array(z.enum([
    'sales_outreach',
    'marketing_email',
    'analytics',
    'third_party_sharing',
  ])),
  timestamp: z.date(),
  source: z.string(),
  ipAddress: z.string().optional(),
});

type Consent = z.infer<typeof ConsentSchema>;

export async function recordConsent(consent: Consent): Promise<void> {
  await prisma.consent.create({
    data: {
      email: consent.email,
      purposes: consent.purposes,
      grantedAt: consent.timestamp,
      source: consent.source,
      ipAddress: consent.ipAddress,
    },
  });
}

export async function checkConsent(email: string, purpose: string): Promise<boolean> {
  const consent = await prisma.consent.findFirst({
    where: {
      email,
      purposes: { has: purpose },
      revokedAt: null,
    },
    orderBy: { grantedAt: 'desc' },
  });

  return !!consent;
}

export async function revokeConsent(email: string, purpose?: string): Promise<void> {
  if (purpose) {
    // Revoke specific purpose
    await prisma.consent.updateMany({
      where: { email, purposes: { has: purpose } },
      data: { revokedAt: new Date() },
    });
  } else {
    // Revoke all
    await prisma.consent.updateMany({
      where: { email },
      data: { revokedAt: new Date() },
    });
  }
}
```