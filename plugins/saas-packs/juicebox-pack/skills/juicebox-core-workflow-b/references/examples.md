# Examples

### Enrichment Pipeline
```typescript
const enrichmentService = new ProfileEnrichmentService(juicebox);
const storage = new ProfileStorage();

// Enrich search results
const candidates = await searchPipeline.searchCandidates(criteria);
const profileIds = candidates.slice(0, 20).map(c => c.id);

const enriched = await enrichmentService.batchEnrich(profileIds);

for (const profile of enriched) {
  await storage.saveEnrichedProfile(profile);
  console.log(`Enriched: ${profile.basicInfo.name}`);
}
```