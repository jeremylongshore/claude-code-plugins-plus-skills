---
name: langchain-debug-bundle
license: MIT
allowed-tools: Read, Write, Edit, Bash, Grep
description: Collect langchain debug evidence for troubleshooting and support. use
  when preparing bug reports, collecting traces, or gathering diagnostic information
  for complex issues. trigger with phrases like "langchain debug bundle", "langchain
  diagnostics...
---
# LangChain Debug Bundle

## Overview
Collect comprehensive debug information for LangChain issues including traces, versions, and reproduction steps.

## Prerequisites
- LangChain installed
- Reproducible error condition
- Access to logs and environment

## Instructions

### Step 1: Collect Environment Info
```python
# debug_bundle.py
import sys
import platform
import subprocess

def collect_environment():
    """Collect system and package information."""
    info = {
        "python_version": sys.version,
        "platform": platform.platform(),
        "packages": {}
    }

    # Get LangChain package versions
    packages = [
        "langchain",
        "langchain-core",
        "langchain-community",
        "langchain-openai",
        "langchain-anthropic",
        "openai",
        "anthropic"
    ]

    for pkg in packages:
        try:
            result = subprocess.run(
                [sys.executable, "-m", "pip", "show", pkg],
                capture_output=True, text=True
            )
            for line in result.stdout.split("\n"):
                if line.startswith("Version:"):
                    info["packages"][pkg] = line.split(":")[1].strip()
        except:
            info["packages"][pkg] = "not installed"

    return info

print(collect_environment())
```

### Step 2: Enable Full Tracing
```python
import os
import langchain

# Enable debug mode
langchain.debug = True

# Enable LangSmith tracing (if available)
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "debug-session"

# Custom callback for logging
from langchain_core.callbacks import BaseCallbackHandler
from datetime import datetime

class DebugCallback(BaseCallbackHandler):
    def __init__(self):
        self.logs = []

    def on_llm_start(self, serialized, prompts, **kwargs):
        self.logs.append({
            "event": "llm_start",
            "time": datetime.now().isoformat(),
            "prompts": prompts
        })

    def on_llm_end(self, response, **kwargs):
        self.logs.append({
            "event": "llm_end",
            "time": datetime.now().isoformat(),
            "response": str(response)
        })

    def on_llm_error(self, error, **kwargs):
        self.logs.append({
            "event": "llm_error",
            "time": datetime.now().isoformat(),
            "error": str(error)
        })

    def on_tool_start(self, serialized, input_str, **kwargs):
        self.logs.append({
            "event": "tool_start",
            "time": datetime.now().isoformat(),
            "tool": serialized.get("name"),
            "input": input_str
        })

    def on_tool_error(self, error, **kwargs):
        self.logs.append({
            "event": "tool_error",
            "time": datetime.now().isoformat(),
            "error": str(error)
        })
```

### Step 3: Create Minimal Reproduction
```python
# minimal_repro.py
"""
Minimal reproduction script for LangChain issue.
Run with: python minimal_repro.py
"""
import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# Setup (redact actual API key in report)
os.environ["OPENAI_API_KEY"] = "sk-..."

def reproduce_issue():
    """Reproduce the issue with minimal code."""
    try:
        llm = ChatOpenAI(model="gpt-4o-mini")
        prompt = ChatPromptTemplate.from_template("Test: {input}")
        chain = prompt | llm

        # This is where the error occurs
        result = chain.invoke({"input": "test"})
        print(f"Success: {result}")
    except Exception as e:
        print(f"Error: {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    reproduce_issue()
```

### Step 4: Generate Debug Bundle
```python
import json
from datetime import datetime
from pathlib import Path

def create_debug_bundle(error_description: str, logs: list):
    """Create a complete debug bundle."""
    bundle = {
        "created_at": datetime.now().isoformat(),
        "description": error_description,
        "environment": collect_environment(),
        "trace_logs": logs,
        "steps_to_reproduce": [
            "1. Install packages: pip install langchain langchain-openai",
            "2. Set OPENAI_API_KEY environment variable",
            "3. Run: python minimal_repro.py"
        ]
    }

    # Save bundle
    output_path = Path("debug_bundle.json")
    output_path.write_text(json.dumps(bundle, indent=2))
    print(f"Debug bundle saved to: {output_path}")

    return bundle

# Usage
debug_callback = DebugCallback()
# Run your code with callback...
# llm = ChatOpenAI(callbacks=[debug_callback])

create_debug_bundle(
    error_description="Chain fails with OutputParserException",
    logs=debug_callback.logs
)
```

## Output
- `debug_bundle.json` with full diagnostic information
- `minimal_repro.py` for issue reproduction
- Environment and version information
- Trace logs with timestamps

## Debug Bundle Contents
```json
{
  "created_at": "2025-01-06T12:00:00",
  "description": "Issue description",
  "environment": {
    "python_version": "3.11.0",
    "platform": "Linux-6.8.0",
    "packages": {
      "langchain": "0.3.0",
      "langchain-core": "0.3.0",
      "langchain-openai": "0.2.0"
    }
  },
  "trace_logs": [...],
  "steps_to_reproduce": [...]
}
```

## Checklist Before Submitting
- [ ] API keys redacted from all files
- [ ] Minimal reproduction script works independently
- [ ] Error message and stack trace included
- [ ] Package versions documented
- [ ] Expected vs actual behavior described

## Resources
- [LangChain GitHub Issues](https://github.com/langchain-ai/langchain/issues)
- [LangSmith Tracing](https://docs.smith.langchain.com/)
- [LangChain Discord](https://discord.gg/langchain)

## Next Steps
Use `langchain-common-errors` for quick fixes or escalate with the bundle.
