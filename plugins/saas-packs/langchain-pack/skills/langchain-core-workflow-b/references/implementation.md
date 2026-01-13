# Implementation Guide

### Step 1: Define Tools
```python
from langchain_core.tools import tool
from pydantic import BaseModel, Field

class SearchInput(BaseModel):
    query: str = Field(description="The search query")

@tool(args_schema=SearchInput)
def search_web(query: str) -> str:
    """Search the web for information."""
    # Implement actual search logic
    return f"Search results for: {query}"

@tool
def calculate(expression: str) -> str:
    """Evaluate a mathematical expression."""
    try:
        result = eval(expression)  # Use safer alternative in production
        return str(result)
    except Exception as e:
        return f"Error: {e}"

@tool
def get_current_time() -> str:
    """Get the current date and time."""
    from datetime import datetime
    return datetime.now().isoformat()

tools = [search_web, calculate, get_current_time]
```

### Step 2: Create Agent with Tools
```python
from langchain_openai import ChatOpenAI
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

llm = ChatOpenAI(model="gpt-4o-mini")

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant with access to tools."),
    MessagesPlaceholder(variable_name="chat_history", optional=True),
    ("human", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad"),
])

agent = create_tool_calling_agent(llm, tools, prompt)

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    max_iterations=10,
    handle_parsing_errors=True
)
```

### Step 3: Run the Agent
```python
# Simple invocation
result = agent_executor.invoke({
    "input": "What's 25 * 4 and what time is it?"
})
print(result["output"])

# With chat history
from langchain_core.messages import HumanMessage, AIMessage

history = [
    HumanMessage(content="Hi, I'm Alice"),
    AIMessage(content="Hello Alice! How can I help you?")
]

result = agent_executor.invoke({
    "input": "What's my name?",
    "chat_history": history
})
```

### Step 4: Streaming Agent Output
```python
async def stream_agent():
    async for event in agent_executor.astream_events(
        {"input": "Search for LangChain news"},
        version="v2"
    ):
        if event["event"] == "on_chat_model_stream":
            print(event["data"]["chunk"].content, end="", flush=True)
        elif event["event"] == "on_tool_start":
            print(f"\n[Using tool: {event['name']}]")
```