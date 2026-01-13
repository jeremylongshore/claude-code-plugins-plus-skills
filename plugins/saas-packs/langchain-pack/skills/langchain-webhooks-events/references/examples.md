# Examples

### Using Callbacks
```python
from langchain_openai import ChatOpenAI

webhook_handler = WebhookCallbackHandler("https://api.example.com/webhook")

llm = ChatOpenAI(
    model="gpt-4o-mini",
    callbacks=[webhook_handler]
)

# All LLM calls will trigger webhook events
response = llm.invoke("Hello!")
```

### Client-Side SSE Consumption
```javascript
// JavaScript client
const eventSource = new EventSource('/chat/stream?message=Hello');

eventSource.onmessage = (event) => {
    if (event.data === '[DONE]') {
        eventSource.close();
        return;
    }
    document.getElementById('output').textContent += event.data;
};
```