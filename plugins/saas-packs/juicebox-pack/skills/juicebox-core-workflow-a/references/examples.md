# Examples

### Full Pipeline Usage
```typescript
const pipeline = new CandidateSearchPipeline(juiceboxService);

const candidates = await pipeline.searchCandidates({
  role: 'Senior Software Engineer',
  skills: ['typescript', 'react', 'node.js'],
  location: 'San Francisco Bay Area',
  experienceYears: { min: 5 }
});

console.log(`Found ${candidates.length} matching candidates`);
candidates.slice(0, 10).forEach(c => {
  console.log(`${c.name} (Score: ${c.score}) - ${c.title} at ${c.company}`);
});
```