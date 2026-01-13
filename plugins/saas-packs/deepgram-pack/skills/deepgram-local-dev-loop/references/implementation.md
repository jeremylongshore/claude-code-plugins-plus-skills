# Implementation Guide

### Step 1: Create Project Structure
```bash
mkdir -p src tests fixtures
touch src/transcribe.ts tests/transcribe.test.ts
```

### Step 2: Set Up Environment Files
```bash
# .env.development
DEEPGRAM_API_KEY=your-dev-api-key
DEEPGRAM_MODEL=nova-2

# .env.test
DEEPGRAM_API_KEY=your-test-api-key
DEEPGRAM_MODEL=nova-2
```

### Step 3: Create Test Fixtures
```bash
# Download sample audio for testing
curl -o fixtures/sample.wav https://static.deepgram.com/examples/nasa-podcast.wav
```

### Step 4: Set Up Watch Mode
```json
{
  "scripts": {
    "dev": "tsx watch src/transcribe.ts",
    "test": "vitest",
    "test:watch": "vitest --watch"
  }
}
```