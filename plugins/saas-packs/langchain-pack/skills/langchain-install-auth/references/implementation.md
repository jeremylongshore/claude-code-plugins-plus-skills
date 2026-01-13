# Implementation Guide

### Step 1: Install LangChain Core
```bash
# Python (recommended)
pip install langchain langchain-core langchain-community

# Or with specific providers
pip install langchain-openai langchain-anthropic langchain-google-genai

# Node.js
npm install langchain @langchain/core @langchain/community
```

### Step 2: Configure Authentication
```bash
# OpenAI
export OPENAI_API_KEY="your-openai-key"

# Anthropic
export ANTHROPIC_API_KEY="your-anthropic-key"

# Google
export GOOGLE_API_KEY="your-google-key"

# Or create .env file
echo 'OPENAI_API_KEY=your-openai-key' >> .env
```

### Step 3: Verify Connection
```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini")
response = llm.invoke("Say hello!")
print(response.content)
```