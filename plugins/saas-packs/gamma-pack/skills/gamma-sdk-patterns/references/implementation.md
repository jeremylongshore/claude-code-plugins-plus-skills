# Implementation Guide

### Pattern 1: Client Singleton
```typescript
// lib/gamma.ts
import { GammaClient } from '@gamma/sdk';

let client: GammaClient | null = null;

export function getGammaClient(): GammaClient {
  if (!client) {
    client = new GammaClient({
      apiKey: process.env.GAMMA_API_KEY,
      timeout: 30000,
      retries: 3,
    });
  }
  return client;
}
```

### Pattern 2: Presentation Builder
```typescript
// lib/presentation-builder.ts
import { getGammaClient } from './gamma';

interface SlideContent {
  title: string;
  content: string;
  layout?: 'title' | 'content' | 'image' | 'split';
}

export class PresentationBuilder {
  private slides: SlideContent[] = [];
  private title: string = '';
  private style: string = 'professional';

  setTitle(title: string): this {
    this.title = title;
    return this;
  }

  addSlide(slide: SlideContent): this {
    this.slides.push(slide);
    return this;
  }

  setStyle(style: string): this {
    this.style = style;
    return this;
  }

  async build() {
    const gamma = getGammaClient();
    return gamma.presentations.create({
      title: this.title,
      slides: this.slides,
      style: this.style,
    });
  }
}
```

### Pattern 3: Error Handling Wrapper
```typescript
// lib/safe-gamma.ts
import { GammaError } from '@gamma/sdk';

export async function safeGammaCall<T>(
  fn: () => Promise<T>
): Promise<{ data: T; error: null } | { data: null; error: string }> {
  try {
    const data = await fn();
    return { data, error: null };
  } catch (err) {
    if (err instanceof GammaError) {
      return { data: null, error: err.message };
    }
    throw err;
  }
}
```

### Pattern 4: Template Factory
```typescript
// lib/templates.ts
type TemplateType = 'pitch-deck' | 'report' | 'tutorial' | 'proposal';

const TEMPLATES: Record<TemplateType, object> = {
  'pitch-deck': { slides: 10, style: 'bold' },
  'report': { slides: 15, style: 'professional' },
  'tutorial': { slides: 8, style: 'friendly' },
  'proposal': { slides: 12, style: 'corporate' },
};

export function fromTemplate(type: TemplateType, title: string) {
  return { ...TEMPLATES[type], title };
}
```