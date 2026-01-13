# Integration Patterns

## Integration Patterns

### CRM Integration (Salesforce)

```typescript
// src/integrations/salesforce.ts
export class SalesforceIntegration {
  async syncContact(contact: Contact): Promise<void> {
    const sfContact = await this.salesforce.sobject('Contact').upsert({
      Email: contact.email,
      FirstName: contact.firstName,
      LastName: contact.lastName,
      Title: contact.title,
      Apollo_ID__c: contact.apolloId,
      LinkedIn_URL__c: contact.linkedinUrl,
    }, 'Email');

    console.log(`Synced contact ${contact.email} to Salesforce`);
  }

  async syncCompany(company: Company): Promise<void> {
    const sfAccount = await this.salesforce.sobject('Account').upsert({
      Name: company.name,
      Website: `https://${company.domain}`,
      Industry: company.industry,
      NumberOfEmployees: company.employeeCount,
      Apollo_ID__c: company.apolloId,
    }, 'Website');
  }
}
```

### Event-Driven Architecture

```typescript
// src/events/apollo.events.ts
export const APOLLO_EVENTS = {
  CONTACT_ENRICHED: 'apollo.contact.enriched',
  COMPANY_ENRICHED: 'apollo.company.enriched',
  SEARCH_COMPLETED: 'apollo.search.completed',
  SEQUENCE_STARTED: 'apollo.sequence.started',
  EMAIL_ENGAGEMENT: 'apollo.email.engagement',
};

// Event handlers
eventBus.on(APOLLO_EVENTS.CONTACT_ENRICHED, async (contact) => {
  // Sync to CRM
  await salesforceIntegration.syncContact(contact);

  // Update search index
  await searchIndex.indexContact(contact);

  // Notify relevant teams
  if (contact.score >= 80) {
    await slackNotifier.sendHighValueLead(contact);
  }
});
```