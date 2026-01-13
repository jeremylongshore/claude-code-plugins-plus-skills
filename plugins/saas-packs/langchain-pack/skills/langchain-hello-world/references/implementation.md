# Implementation Guide

### Step 1: Create Entry File
Create a new file `hello_langchain.py` for your hello world example.

### Step 2: Import and Initialize
```python
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

llm = ChatOpenAI(model="gpt-4o-mini")
```

### Step 3: Create Your First Chain
```python
from langchain_core.output_parsers import StrOutputParser

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("user", "{input}")
])

chain = prompt | llm | StrOutputParser()

response = chain.invoke({"input": "Hello, LangChain!"})
print(response)
```