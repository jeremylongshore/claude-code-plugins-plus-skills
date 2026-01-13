# Advanced Patterns

## Advanced Patterns

### Custom Tool with Async Support
```python
from langchain_core.tools import StructuredTool

async def async_search(query: str) -> str:
    """Async search implementation."""
    import aiohttp
    async with aiohttp.ClientSession() as session:
        # Implement async search
        return f"Async results for: {query}"

search_tool = StructuredTool.from_function(
    func=lambda q: "sync fallback",
    coroutine=async_search,
    name="search",
    description="Search the web"
)
```

### Agent with Memory
```python
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

message_history = ChatMessageHistory()

agent_with_memory = RunnableWithMessageHistory(
    agent_executor,
    lambda session_id: message_history,
    input_messages_key="input",
    history_messages_key="chat_history"
)

result = agent_with_memory.invoke(
    {"input": "Remember, I prefer Python"},
    config={"configurable": {"session_id": "user123"}}
)
```