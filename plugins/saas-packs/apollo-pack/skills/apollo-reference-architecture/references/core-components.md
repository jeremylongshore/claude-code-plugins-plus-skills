# Core Components

## Core Components

### 1. Apollo Service Layer

```typescript
// src/services/apollo/apollo.service.ts
import { Injectable } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { Repository } from 'typeorm';
import { ApolloClient } from '../../lib/apollo/client';
import { ApolloCache } from '../../lib/apollo/cache';
import { Contact } from '../../models/contact.model';
import { Company } from '../../models/company.model';

@Injectable()
export class ApolloService {
  constructor(
    private readonly client: ApolloClient,
    private readonly cache: ApolloCache,
    @InjectRepository(Contact)
    private readonly contactRepo: Repository<Contact>,
    @InjectRepository(Company)
    private readonly companyRepo: Repository<Company>,
  ) {}

  async searchAndEnrich(criteria: SearchCriteria): Promise<EnrichedLead[]> {
    // 1. Search Apollo
    const searchResults = await this.client.searchPeople(criteria);

    // 2. Filter and score
    const qualified = this.qualifyLeads(searchResults.people, criteria);

    // 3. Enrich top leads
    const enriched = await Promise.all(
      qualified.slice(0, 25).map(lead => this.enrichLead(lead))
    );

    // 4. Persist to database
    await this.persistLeads(enriched);

    return enriched;
  }

  private async enrichLead(lead: RawLead): Promise<EnrichedLead> {
    // Check cache
    const cached = await this.cache.get(`lead:${lead.id}`);
    if (cached) return cached;

    // Enrich from Apollo
    const [personData, companyData] = await Promise.all([
      this.client.enrichPerson({ id: lead.id }),
      lead.organization?.primary_domain
        ? this.client.enrichOrganization(lead.organization.primary_domain)
        : null,
    ]);

    const enriched = this.mergeData(lead, personData, companyData);

    // Cache result
    await this.cache.set(`lead:${lead.id}`, enriched, 86400); // 24h

    return enriched;
  }

  private async persistLeads(leads: EnrichedLead[]): Promise<void> {
    for (const lead of leads) {
      // Upsert contact
      await this.contactRepo.upsert({
        apolloId: lead.id,
        email: lead.email,
        name: lead.name,
        title: lead.title,
        linkedinUrl: lead.linkedinUrl,
        companyId: lead.company?.id,
        enrichedAt: new Date(),
      }, ['apolloId']);

      // Upsert company
      if (lead.company) {
        await this.companyRepo.upsert({
          apolloId: lead.company.id,
          name: lead.company.name,
          domain: lead.company.domain,
          industry: lead.company.industry,
          employeeCount: lead.company.employeeCount,
          enrichedAt: new Date(),
        }, ['apolloId']);
      }
    }
  }
}
```

### 2. Background Job Processing

```typescript
// src/jobs/apollo/enrich.job.ts
import { Job, Queue } from 'bull';
import { Process, Processor } from '@nestjs/bull';
import { ApolloService } from '../../services/apollo/apollo.service';

interface EnrichJobData {
  contactIds: string[];
  priority: 'high' | 'normal' | 'low';
}

@Processor('apollo-enrich')
export class EnrichProcessor {
  constructor(private readonly apolloService: ApolloService) {}

  @Process('enrich-contacts')
  async handleEnrich(job: Job<EnrichJobData>): Promise<void> {
    const { contactIds, priority } = job.data;

    // Process in batches to respect rate limits
    const batchSize = priority === 'high' ? 10 : 5;

    for (let i = 0; i < contactIds.length; i += batchSize) {
      const batch = contactIds.slice(i, i + batchSize);

      await Promise.all(
        batch.map(id => this.apolloService.enrichContact(id))
      );

      // Update progress
      await job.progress(((i + batchSize) / contactIds.length) * 100);

      // Rate limit delay
      if (i + batchSize < contactIds.length) {
        await new Promise(r => setTimeout(r, 1000));
      }
    }
  }
}

// Queue producer
@Injectable()
export class EnrichQueue {
  constructor(@InjectQueue('apollo-enrich') private queue: Queue) {}

  async enqueueContacts(contactIds: string[], priority: 'high' | 'normal' | 'low' = 'normal') {
    await this.queue.add('enrich-contacts', {
      contactIds,
      priority,
    }, {
      priority: priority === 'high' ? 1 : priority === 'normal' ? 5 : 10,
      attempts: 3,
      backoff: {
        type: 'exponential',
        delay: 5000,
      },
    });
  }
}
```

### 3. Data Models

```typescript
// src/models/contact.model.ts
import { Entity, Column, PrimaryGeneratedColumn, ManyToOne, Index } from 'typeorm';
import { Company } from './company.model';

@Entity('contacts')
export class Contact {
  @PrimaryGeneratedColumn('uuid')
  id: string;

  @Index({ unique: true })
  @Column()
  apolloId: string;

  @Index()
  @Column({ nullable: true })
  email: string;

  @Column()
  name: string;

  @Column({ nullable: true })
  firstName: string;

  @Column({ nullable: true })
  lastName: string;

  @Column({ nullable: true })
  title: string;

  @Column({ nullable: true })
  seniority: string;

  @Column({ nullable: true })
  linkedinUrl: string;

  @Column({ nullable: true })
  phone: string;

  @Column({ type: 'jsonb', nullable: true })
  customFields: Record<string, any>;

  @ManyToOne(() => Company, company => company.contacts)
  company: Company;

  @Column()
  companyId: string;

  @Column({ type: 'timestamp' })
  enrichedAt: Date;

  @Column({ type: 'timestamp', default: () => 'CURRENT_TIMESTAMP' })
  createdAt: Date;

  @Column({ type: 'timestamp', default: () => 'CURRENT_TIMESTAMP' })
  updatedAt: Date;
}

// src/models/company.model.ts
@Entity('companies')
export class Company {
  @PrimaryGeneratedColumn('uuid')
  id: string;

  @Index({ unique: true })
  @Column()
  apolloId: string;

  @Column()
  name: string;

  @Index()
  @Column()
  domain: string;

  @Column({ nullable: true })
  industry: string;

  @Column({ nullable: true })
  subIndustry: string;

  @Column({ nullable: true })
  employeeCount: number;

  @Column({ nullable: true })
  annualRevenue: number;

  @Column({ nullable: true })
  foundedYear: number;

  @Column({ type: 'text', nullable: true })
  description: string;

  @Column({ type: 'jsonb', nullable: true })
  technologies: string[];

  @Column({ type: 'jsonb', nullable: true })
  location: {
    city: string;
    state: string;
    country: string;
  };

  @OneToMany(() => Contact, contact => contact.company)
  contacts: Contact[];
}
```

### 4. API Routes

```typescript
// src/routes/api/apollo/search.ts
import { Router } from 'express';
import { ApolloService } from '../../../services/apollo/apollo.service';
import { validateRequest } from '../../../middleware/validation';

const router = Router();

router.post('/search', validateRequest(SearchSchema), async (req, res) => {
  const { domains, titles, locations, minEmployees, maxEmployees } = req.body;

  const results = await apolloService.searchAndEnrich({
    domains,
    titles,
    locations,
    minEmployees,
    maxEmployees,
  });

  res.json({
    success: true,
    data: results,
    meta: {
      count: results.length,
      timestamp: new Date().toISOString(),
    },
  });
});

router.post('/enrich/bulk', validateRequest(BulkEnrichSchema), async (req, res) => {
  const { contactIds, priority } = req.body;

  // Queue for background processing
  await enrichQueue.enqueueContacts(contactIds, priority);

  res.json({
    success: true,
    message: `Queued ${contactIds.length} contacts for enrichment`,
    jobId: 'job-id-here',
  });
});

export default router;
```