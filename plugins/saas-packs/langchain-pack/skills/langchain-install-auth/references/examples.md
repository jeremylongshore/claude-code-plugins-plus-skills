# Examples

### Python Setup (OpenAI)
```python
import os
from langchain_openai import ChatOpenAI

# Ensure API key is set
assert os.environ.get("OPENAI_API_KEY"), "Set OPENAI_API_KEY"

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.7,
    max_tokens=1000
)
```

### Python Setup (Anthropic)
```python
from langchain_anthropic import ChatAnthropic

llm = ChatAnthropic(
    model="claude-3-5-sonnet-20241022",
    temperature=0.7
)
```

### TypeScript Setup
```typescript
import { ChatOpenAI } from "@langchain/openai";

const llm = new ChatOpenAI({
  modelName: "gpt-4o-mini",
  temperature: 0.7
});
```