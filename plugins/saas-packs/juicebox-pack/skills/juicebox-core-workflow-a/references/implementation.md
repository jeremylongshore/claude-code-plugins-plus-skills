# Implementation Guide

### Step 1: Define Search Parameters
```typescript
// types/search.ts
export interface CandidateSearch {
  role: string;
  skills: string[];
  location?: string;
  experienceYears?: { min?: number; max?: number };
  companies?: string[];
  education?: string[];
}

export function buildSearchQuery(params: CandidateSearch): string {
  const parts = [params.role];

  if (params.skills.length > 0) {
    parts.push(`skills:(${params.skills.join(' OR ')})`);
  }

  if (params.location) {
    parts.push(`location:"${params.location}"`);
  }

  return parts.join(' AND ');
}
```

### Step 2: Implement Search Pipeline
```typescript
// workflows/candidate-search.ts
import { JuiceboxService } from '../lib/juicebox-client';

export class CandidateSearchPipeline {
  constructor(private juicebox: JuiceboxService) {}

  async searchCandidates(criteria: CandidateSearch) {
    const query = buildSearchQuery(criteria);

    // Initial broad search
    const results = await this.juicebox.searchPeople(query, {
      limit: 100,
      fields: ['name', 'title', 'company', 'location', 'skills', 'experience']
    });

    // Score and rank candidates
    const scored = results.profiles.map(profile => ({
      ...profile,
      score: this.calculateFitScore(profile, criteria)
    }));

    // Sort by fit score
    return scored.sort((a, b) => b.score - a.score);
  }

  private calculateFitScore(profile: Profile, criteria: CandidateSearch): number {
    let score = 0;

    // Skills match
    const matchedSkills = profile.skills.filter(s =>
      criteria.skills.includes(s.toLowerCase())
    );
    score += matchedSkills.length * 10;

    // Experience match
    if (criteria.experienceYears) {
      const years = profile.experienceYears || 0;
      if (years >= (criteria.experienceYears.min || 0)) {
        score += 20;
      }
    }

    return score;
  }
}
```

### Step 3: Handle Pagination
```typescript
async function* searchAllCandidates(
  juicebox: JuiceboxService,
  query: string
): AsyncGenerator<Profile> {
  let cursor: string | undefined;

  do {
    const results = await juicebox.searchPeople(query, {
      limit: 50,
      cursor
    });

    for (const profile of results.profiles) {
      yield profile;
    }

    cursor = results.nextCursor;
  } while (cursor);
}
```