# Connect Hubspot

## Connect HubSpot

1. Granola Settings > Integrations > HubSpot
2. Click "Connect HubSpot"
3. Authorize with HubSpot account
4. Select permissions:
   - Read/Write contacts
   - Read/Write notes
   - Read/Write deals
5. Configure contact matching
```

#### Contact Matching Rules
| Attendee Email | Action |
|----------------|--------|
| Exists in HubSpot | Attach note to contact |
| New email | Create contact (optional) |
| Internal domain | Skip CRM entry |

#### Note Format
```
Meeting with {{contact_name}}
Date: {{date}}
Duration: {{duration}}

Summary: {{summary}}

Next Steps:
{{action_items}}

---
Captured with Granola
```