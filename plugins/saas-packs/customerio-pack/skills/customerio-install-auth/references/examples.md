# Examples

### TypeScript Setup
```typescript
import { TrackClient, RegionUS, RegionEU } from '@customerio/track';

// US region (default)
const client = new TrackClient(
  process.env.CUSTOMERIO_SITE_ID!,
  process.env.CUSTOMERIO_API_KEY!,
  { region: RegionUS }
);

// EU region
const euClient = new TrackClient(
  process.env.CUSTOMERIO_SITE_ID!,
  process.env.CUSTOMERIO_API_KEY!,
  { region: RegionEU }
);
```

### Python Setup
```python
import os
from customerio import CustomerIO

cio = CustomerIO(
    site_id=os.environ.get('CUSTOMERIO_SITE_ID'),
    api_key=os.environ.get('CUSTOMERIO_API_KEY')
)
```