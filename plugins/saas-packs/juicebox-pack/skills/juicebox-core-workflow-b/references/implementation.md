# Implementation Guide

### Step 1: Define Enrichment Schema
```typescript
// types/enrichment.ts
export interface EnrichedProfile {
  id: string;
  basicInfo: {
    name: string;
    title: string;
    company: string;
    location: string;
  };
  contact: {
    email?: string;
    phone?: string;
    linkedin?: string;
  };
  experience: WorkExperience[];
  education: Education[];
  skills: Skill[];
  lastEnriched: Date;
}

export interface WorkExperience {
  company: string;
  title: string;
  startDate: string;
  endDate?: string;
  description?: string;
}
```

### Step 2: Implement Enrichment Service
```typescript
// services/enrichment.ts
import { JuiceboxService } from '../lib/juicebox-client';

export class ProfileEnrichmentService {
  constructor(private juicebox: JuiceboxService) {}

  async enrichProfile(profileId: string): Promise<EnrichedProfile> {
    // Fetch full profile details
    const fullProfile = await this.juicebox.getProfile(profileId, {
      include: ['contact', 'experience', 'education', 'skills']
    });

    // Validate and structure data
    const enriched: EnrichedProfile = {
      id: profileId,
      basicInfo: {
        name: fullProfile.name,
        title: fullProfile.title,
        company: fullProfile.company,
        location: fullProfile.location
      },
      contact: {
        email: fullProfile.email,
        phone: fullProfile.phone,
        linkedin: fullProfile.linkedinUrl
      },
      experience: this.parseExperience(fullProfile.workHistory),
      education: this.parseEducation(fullProfile.education),
      skills: this.parseSkills(fullProfile.skills),
      lastEnriched: new Date()
    };

    return enriched;
  }

  async batchEnrich(profileIds: string[]): Promise<EnrichedProfile[]> {
    const batchSize = 10;
    const results: EnrichedProfile[] = [];

    for (let i = 0; i < profileIds.length; i += batchSize) {
      const batch = profileIds.slice(i, i + batchSize);
      const enriched = await Promise.all(
        batch.map(id => this.enrichProfile(id))
      );
      results.push(...enriched);

      // Rate limit protection
      if (i + batchSize < profileIds.length) {
        await sleep(1000);
      }
    }

    return results;
  }
}
```

### Step 3: Store Enriched Data
```typescript
// storage/profiles.ts
export class ProfileStorage {
  async saveEnrichedProfile(profile: EnrichedProfile): Promise<void> {
    await db.profiles.upsert({
      where: { id: profile.id },
      create: profile,
      update: {
        ...profile,
        lastEnriched: new Date()
      }
    });
  }

  async getStaleProfiles(olderThan: Date): Promise<string[]> {
    const stale = await db.profiles.findMany({
      where: {
        lastEnriched: { lt: olderThan }
      },
      select: { id: true }
    });
    return stale.map(p => p.id);
  }
}
```