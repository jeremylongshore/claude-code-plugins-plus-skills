# Examples

### Python Hello World
```python
import os
from customerio import CustomerIO

cio = CustomerIO(
    site_id=os.environ.get('CUSTOMERIO_SITE_ID'),
    api_key=os.environ.get('CUSTOMERIO_API_KEY')
)

# Identify user
cio.identify(id='user-123', email='hello@example.com', first_name='Hello')
print('User identified')

# Track event
cio.track(customer_id='user-123', name='hello_world', source='sdk-test')
print('Event tracked')
```

### With Anonymous User
```typescript
// Track anonymous user with device ID
await client.identify('device-abc123', {
  anonymous_id: 'device-abc123',
  platform: 'web'
});
```