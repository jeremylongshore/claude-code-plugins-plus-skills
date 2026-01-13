# Implementation Guide

### Step 1: Prompt-Based Generation
```typescript
import { GammaClient } from '@gamma/sdk';

const gamma = new GammaClient({ apiKey: process.env.GAMMA_API_KEY });

async function generateFromPrompt(topic: string, slides: number = 10) {
  const presentation = await gamma.presentations.generate({
    prompt: topic,
    slideCount: slides,
    style: 'professional',
    includeImages: true,
    includeSpeakerNotes: true,
  });

  return presentation;
}

// Usage
const deck = await generateFromPrompt('Introduction to Machine Learning', 8);
console.log('Generated:', deck.url);
```

### Step 2: Document-Based Generation
```typescript
async function generateFromDocument(filePath: string) {
  const document = await fs.readFile(filePath, 'utf-8');

  const presentation = await gamma.presentations.generate({
    sourceDocument: document,
    sourceType: 'markdown', // or 'pdf', 'docx', 'text'
    extractKeyPoints: true,
    maxSlides: 15,
  });

  return presentation;
}
```

### Step 3: Structured Content Generation
```typescript
interface SlideOutline {
  title: string;
  points: string[];
  imagePrompt?: string;
}

async function generateFromOutline(outline: SlideOutline[]) {
  const presentation = await gamma.presentations.generate({
    slides: outline.map(slide => ({
      title: slide.title,
      content: slide.points.join('\n'),
      generateImage: slide.imagePrompt,
    })),
    style: 'modern',
  });

  return presentation;
}
```

### Step 4: Batch Generation Pipeline
```typescript
async function batchGenerate(topics: string[]) {
  const results = await Promise.allSettled(
    topics.map(topic =>
      gamma.presentations.generate({
        prompt: topic,
        slideCount: 5,
      })
    )
  );

  return results.map((r, i) => ({
    topic: topics[i],
    status: r.status,
    url: r.status === 'fulfilled' ? r.value.url : null,
    error: r.status === 'rejected' ? r.reason.message : null,
  }));
}
```