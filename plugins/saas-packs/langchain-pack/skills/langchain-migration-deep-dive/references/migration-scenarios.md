# Migration Scenarios

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