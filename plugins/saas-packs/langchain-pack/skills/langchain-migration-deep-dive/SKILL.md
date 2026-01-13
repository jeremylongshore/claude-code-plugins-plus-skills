---
name: langchain-migration-deep-dive
description: |
  Complex migration strategies for LangChain applications.
  Use when migrating from legacy LLM frameworks, refactoring large codebases,
  or implementing phased migration approaches.
  Trigger with phrases like "langchain migration strategy", "migrate to langchain",
  "langchain refactor", "legacy LLM migration", "langchain transition".
allowed-tools: Read, Write, Edit, Bash, Grep
version: 1.0.0
license: MIT
author: Jeremy Longshore <jeremy@intentsolutions.io>
---

# LangChain Migration Deep Dive

## Overview
Comprehensive strategies for migrating to LangChain from legacy LLM implementations or other frameworks.

## Prerequisites
- Existing LLM application to migrate
- Understanding of current architecture
- Test coverage for validation
- Staging environment for testing

## Migration Scenarios

### Scenario 1: Raw OpenAI SDK to LangChain

#### Before (Raw SDK)
```python
# legacy_openai.py
import openai

client = openai.OpenAI()

def chat(message: str, history: list = None) -> str:
    messages = [{"role": "system", "content": "You are helpful."}]

    if history:
        messages.extend(history)

    messages.append({"role": "user", "content": message})

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        temperature=0.7
    )

    return response.choices[0].message.content
```

#### After (LangChain)
```python
# langchain_chat.py
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage, AIMessage

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are helpful."),
    MessagesPlaceholder(variable_name="history"),
    ("user", "{message}")
])

chain = prompt | llm | StrOutputParser()

def chat(message: str, history: list = None) -> str:
    # Convert legacy format to LangChain messages
    lc_history = []
    if history:
        for msg in history:
            if msg["role"] == "user":
                lc_history.append(HumanMessage(content=msg["content"]))
            elif msg["role"] == "assistant":
                lc_history.append(AIMessage(content=msg["content"]))

    return chain.invoke({"message": message, "history": lc_history})
```

### Scenario 2: LlamaIndex to LangChain

#### Before (LlamaIndex)
```python
# legacy_llamaindex.py
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.llms.openai import OpenAI

documents = SimpleDirectoryReader("data").load_data()
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine(llm=OpenAI(model="gpt-4o-mini"))

def query(question: str) -> str:
    response = query_engine.query(question)
    return str(response)
```

#### After (LangChain)
```python
# langchain_rag.py
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.document_loaders import DirectoryLoader
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

# Load documents
loader = DirectoryLoader("data")
documents = loader.load()

# Split documents
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
splits = splitter.split_documents(documents)

# Create vector store
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(splits, embeddings)
retriever = vectorstore.as_retriever()

# Create RAG chain
llm = ChatOpenAI(model="gpt-4o-mini")

prompt = ChatPromptTemplate.from_template("""
Answer based on the context:

Context: {context}

Question: {question}
""")

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

def query(question: str) -> str:
    return chain.invoke(question)
```

### Scenario 3: Custom Agent to LangChain Agent

#### Before (Custom)
```python
# legacy_agent.py
import json

def run_agent(query: str, tools: dict) -> str:
    messages = [{"role": "user", "content": query}]

    while True:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            functions=[{"name": k, **v["schema"]} for k, v in tools.items()]
        )

        msg = response.choices[0].message

        if msg.function_call:
            # Execute tool
            tool_name = msg.function_call.name
            tool_args = json.loads(msg.function_call.arguments)
            result = tools[tool_name]["func"](**tool_args)

            messages.append({"role": "function", "name": tool_name, "content": result})
        else:
            return msg.content
```

#### After (LangChain)
```python
# langchain_agent.py
from langchain_openai import ChatOpenAI
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.tools import tool

# Convert tools to LangChain format
@tool
def search(query: str) -> str:
    """Search for information."""
    return f"Results for: {query}"

@tool
def calculate(expression: str) -> str:
    """Calculate a math expression."""
    return str(eval(expression))

tools = [search, calculate]

llm = ChatOpenAI(model="gpt-4o")

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant with tools."),
    ("human", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad"),
])

agent = create_tool_calling_agent(llm, tools, prompt)
executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

def run_agent(query: str) -> str:
    result = executor.invoke({"input": query})
    return result["output"]
```

## Migration Strategy

### Phase 1: Assessment
```python
# migration_assessment.py
import ast
import os
from pathlib import Path
from dataclasses import dataclass
from typing import List

@dataclass
class MigrationItem:
    file: str
    line: int
    pattern: str
    complexity: str  # low, medium, high

def assess_codebase(directory: str) -> List[MigrationItem]:
    """Scan codebase for migration items."""
    items = []
    patterns = {
        "openai.ChatCompletion": ("OpenAI SDK v0", "medium"),
        "openai.OpenAI": ("OpenAI SDK v1", "low"),
        "llama_index": ("LlamaIndex", "high"),
        "langchain.chains": ("LangChain legacy chains", "medium"),
        "LLMChain": ("Legacy LLMChain", "low"),
    }

    for path in Path(directory).rglob("*.py"):
        with open(path) as f:
            content = f.read()
            for i, line in enumerate(content.split("\n"), 1):
                for pattern, (name, complexity) in patterns.items():
                    if pattern in line:
                        items.append(MigrationItem(
                            file=str(path),
                            line=i,
                            pattern=name,
                            complexity=complexity
                        ))

    return items

# Generate migration report
items = assess_codebase("src/")
print(f"Found {len(items)} migration items:")
for item in items:
    print(f"  {item.file}:{item.line} - {item.pattern} ({item.complexity})")
```

### Phase 2: Parallel Implementation
```python
# Run both systems in parallel for validation
class DualRunner:
    """Run legacy and new implementations side by side."""

    def __init__(self, legacy_fn, new_fn):
        self.legacy_fn = legacy_fn
        self.new_fn = new_fn
        self.discrepancies = []

    async def run(self, *args, **kwargs):
        """Run both and compare."""
        legacy_result = await self.legacy_fn(*args, **kwargs)
        new_result = await self.new_fn(*args, **kwargs)

        if not self._compare(legacy_result, new_result):
            self.discrepancies.append({
                "args": args,
                "kwargs": kwargs,
                "legacy": legacy_result,
                "new": new_result
            })

        # Return new implementation result
        return new_result

    def _compare(self, a, b) -> bool:
        """Compare results for equivalence."""
        # Implement comparison logic
        return True  # Placeholder
```

### Phase 3: Gradual Rollout
```python
# Feature flag based rollout
import random

class FeatureFlag:
    """Control rollout percentage."""

    def __init__(self, rollout_percentage: float = 0):
        self.percentage = rollout_percentage

    def is_enabled(self, user_id: str = None) -> bool:
        """Check if feature is enabled for user."""
        if user_id:
            # Consistent per-user
            hash_val = hash(user_id) % 100
            return hash_val < self.percentage
        return random.random() * 100 < self.percentage

# Usage
langchain_flag = FeatureFlag(rollout_percentage=10)  # 10% rollout

def process_request(user_id: str, message: str):
    if langchain_flag.is_enabled(user_id):
        return langchain_chat(message)
    else:
        return legacy_chat(message)
```

### Phase 4: Validation and Cleanup
```python
# Validation script
import pytest

class MigrationValidator:
    """Validate migration is complete and correct."""

    def __init__(self, test_cases: list):
        self.test_cases = test_cases

    def run_validation(self, new_fn) -> dict:
        """Run all test cases and report."""
        results = {"passed": 0, "failed": 0, "errors": []}

        for case in self.test_cases:
            try:
                result = new_fn(**case["input"])
                if self._validate(result, case["expected"]):
                    results["passed"] += 1
                else:
                    results["failed"] += 1
                    results["errors"].append({
                        "case": case,
                        "actual": result
                    })
            except Exception as e:
                results["failed"] += 1
                results["errors"].append({
                    "case": case,
                    "error": str(e)
                })

        return results

    def _validate(self, actual, expected) -> bool:
        """Validate result meets expectations."""
        # Implement validation logic
        return True

# Run validation
validator = MigrationValidator([
    {"input": {"message": "Hello"}, "expected": {"type": "greeting"}},
    # ... more test cases
])

results = validator.run_validation(langchain_chat)
print(f"Passed: {results['passed']}, Failed: {results['failed']}")
```

## Migration Checklist
- [ ] Codebase assessed for migration items
- [ ] Test coverage added for current behavior
- [ ] LangChain equivalents implemented
- [ ] Parallel running validation passed
- [ ] Gradual rollout completed
- [ ] Legacy code removed
- [ ] Documentation updated

## Common Issues

| Issue | Solution |
|-------|----------|
| Different response format | Add output parser adapter |
| Missing streaming support | Implement streaming callbacks |
| Memory format mismatch | Convert message history format |
| Tool schema differences | Update tool definitions |

## Resources
- [LangChain Migration Guide](https://python.langchain.com/docs/versions/migrating_chains/)
- [OpenAI SDK Migration](https://github.com/openai/openai-python/discussions/742)
- [Feature Flags Best Practices](https://launchdarkly.com/blog/best-practices-feature-flags/)

## Next Steps
Use `langchain-upgrade-migration` for LangChain version upgrades.
