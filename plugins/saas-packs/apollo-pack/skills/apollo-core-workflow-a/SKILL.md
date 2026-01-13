---
allowed-tools: Read, Write, Edit, Bash, Grep
license: MIT
description: Implement apollo.io lead search and enrichment workflow. use when building
  lead generation features, searching for contacts, or enriching prospect data from
  apollo. trigger with phrases like "apollo lead search", "search apollo contacts",
  "find le...
name: apollo-core-workflow-a
---
# Apollo Core Workflow A

This skill provides automated assistance for apollo core workflow a tasks.

## Prerequisites
- Completed `apollo-sdk-patterns` setup
- Valid Apollo API credentials
- Understanding of your target market criteria

## Output
- Paginated people search results
- Enriched company firmographic data
- Enriched contact data with emails
- Combined lead pipeline with scoring

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Resources
- [Apollo People Search Docs](https://apolloio.github.io/apollo-api-docs/#search-for-people)
- [Apollo Organization Enrichment](https://apolloio.github.io/apollo-api-docs/#enrich-organization)
- [Apollo Person Enrichment](https://apolloio.github.io/apollo-api-docs/#enrich-person)