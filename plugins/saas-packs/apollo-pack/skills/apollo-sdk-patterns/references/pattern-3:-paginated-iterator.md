# Pattern 3: Paginated Iterator

## Pattern 3: Paginated Iterator

```typescript
// src/lib/apollo/pagination.ts
export async function* paginateSearch(
  searchFn: (page: number) => Promise<PeopleSearchResponse>,
  options: { maxPages?: number } = {}
): AsyncGenerator<Person[], void, unknown> {
  const maxPages = options.maxPages || Infinity;
  let page = 1;
  let totalPages = 1;

  while (page <= Math.min(totalPages, maxPages)) {
    const response = await searchFn(page);
    totalPages = response.pagination.total_pages;

    yield response.people;
    page++;

    // Respect rate limits
    await new Promise((resolve) => setTimeout(resolve, 100));
  }
}

// Usage
async function getAllPeople(domain: string): Promise<Person[]> {
  const allPeople: Person[] = [];

  for await (const batch of paginateSearch(
    (page) => apollo.searchPeople({ q_organization_domains: [domain], page, per_page: 100 })
  )) {
    allPeople.push(...batch);
  }

  return allPeople;
}
```