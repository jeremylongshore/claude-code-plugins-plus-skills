# Examples

### Multi-Step Processing Chain
```python
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = ChatOpenAI(model="gpt-4o-mini")

# Step 1: Extract key points
extract_prompt = ChatPromptTemplate.from_template(
    "Extract 3 key points from: {text}"
)

# Step 2: Summarize
summarize_prompt = ChatPromptTemplate.from_template(
    "Create a one-sentence summary from these points: {points}"
)

# Compose the chain
chain = (
    {"points": extract_prompt | llm | StrOutputParser()}
    | summarize_prompt
    | llm
    | StrOutputParser()
)

summary = chain.invoke({"text": "Long article text here..."})
```

### With Context Injection
```python
from langchain_core.runnables import RunnablePassthrough

def get_context(input_dict):
    """Fetch relevant context from database."""
    return f"Context for: {input_dict['query']}"

chain = (
    RunnablePassthrough.assign(context=get_context)
    | prompt
    | llm
    | StrOutputParser()
)

result = chain.invoke({"query": "user question"})
```