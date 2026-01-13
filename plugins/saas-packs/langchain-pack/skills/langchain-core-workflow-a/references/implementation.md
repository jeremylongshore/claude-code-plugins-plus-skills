# Implementation Guide

### Step 1: Create Prompt Templates
```python
from langchain_core.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder
)

# Simple template
simple_prompt = ChatPromptTemplate.from_template(
    "Translate '{text}' to {language}"
)

# Chat-style template
chat_prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "You are a {role}. Respond in {style} style."
    ),
    MessagesPlaceholder(variable_name="history", optional=True),
    HumanMessagePromptTemplate.from_template("{input}")
])
```

### Step 2: Build LCEL Chains
```python
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser

llm = ChatOpenAI(model="gpt-4o-mini")

# Basic chain: prompt -> llm -> parser
basic_chain = simple_prompt | llm | StrOutputParser()

# Invoke the chain
result = basic_chain.invoke({
    "text": "Hello, world!",
    "language": "Spanish"
})
print(result)  # "Hola, mundo!"
```

### Step 3: Chain Composition
```python
from langchain_core.runnables import RunnablePassthrough, RunnableParallel

# Sequential chain
chain1 = prompt1 | llm | StrOutputParser()
chain2 = prompt2 | llm | StrOutputParser()

sequential = chain1 | (lambda x: {"summary": x}) | chain2

# Parallel execution
parallel = RunnableParallel(
    summary=prompt1 | llm | StrOutputParser(),
    keywords=prompt2 | llm | StrOutputParser(),
    sentiment=prompt3 | llm | StrOutputParser()
)

results = parallel.invoke({"text": "Your input text"})
# Returns: {"summary": "...", "keywords": "...", "sentiment": "..."}
```

### Step 4: Branching Logic
```python
from langchain_core.runnables import RunnableBranch

# Conditional branching
branch = RunnableBranch(
    (lambda x: x["type"] == "question", question_chain),
    (lambda x: x["type"] == "command", command_chain),
    default_chain  # Fallback
)

result = branch.invoke({"type": "question", "input": "What is AI?"})
```