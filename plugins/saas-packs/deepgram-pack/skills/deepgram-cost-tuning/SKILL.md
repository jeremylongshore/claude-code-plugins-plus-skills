---
name: deepgram-cost-tuning
license: MIT
allowed-tools: Read, Write, Edit, Bash
description: Optimize Deepgram costs and usage for budget-conscious deployments. Use
  when reducing transcription costs, implementing usage controls, or optimizing pricing
  tier utilization. Trigger with phrases like "deepgram cost", "reduce deepgram spending",
  ...
---
# Deepgram Cost Tuning

## Overview
Optimize Deepgram usage and costs through smart model selection, audio preprocessing, and usage monitoring.

## Deepgram Pricing Overview

| Model | Price per Minute | Best For |
|-------|-----------------|----------|
| Nova-2 | $0.0043 | General transcription |
| Nova | $0.0043 | General transcription |
| Whisper Cloud | $0.0048 | Multilingual |
| Enhanced | $0.0145 | Legacy support |
| Base | $0.0048 | Basic transcription |

Additional Features:
- Speaker Diarization: +$0.0044/min
- Smart Formatting: Included
- Punctuation: Included

## Cost Optimization Strategies

### 1. Model Selection
Choose the most cost-effective model for your use case.

### 2. Audio Preprocessing
Reduce audio duration and optimize format.

### 3. Usage Monitoring
Track and control usage in real-time.

### 4. Caching
Avoid re-transcribing the same content.

## Examples

### Cost-Optimized Transcription Service
```typescript
// services/cost-optimized-transcription.ts
import { createClient } from '@deepgram/sdk';

interface CostConfig {
  maxMonthlySpend: number;
  warningThreshold: number; // percentage
  model: string;
  enabledFeatures: {
    diarization: boolean;
    smartFormat: boolean;
  };
}

interface CostMetrics {
  currentMonthMinutes: number;
  currentMonthCost: number;
  projectedMonthlyCost: number;
}

export class CostOptimizedTranscription {
  private client;
  private config: CostConfig;
  private metrics: CostMetrics;
  private modelCosts: Record<string, number> = {
    'nova-2': 0.0043,
    'nova': 0.0043,
    'base': 0.0048,
    'enhanced': 0.0145,
  };

  constructor(apiKey: string, config: Partial<CostConfig> = {}) {
    this.client = createClient(apiKey);
    this.config = {
      maxMonthlySpend: config.maxMonthlySpend ?? 100,
      warningThreshold: config.warningThreshold ?? 80,
      model: config.model ?? 'nova-2',
      enabledFeatures: config.enabledFeatures ?? {
        diarization: false,
        smartFormat: true,
      },
    };
    this.metrics = {
      currentMonthMinutes: 0,
      currentMonthCost: 0,
      projectedMonthlyCost: 0,
    };
  }

  private calculateCost(durationMinutes: number): number {
    let cost = durationMinutes * this.modelCosts[this.config.model];

    if (this.config.enabledFeatures.diarization) {
      cost += durationMinutes * 0.0044;
    }

    return cost;
  }

  private checkBudget(estimatedMinutes: number): void {
    const estimatedCost = this.calculateCost(estimatedMinutes);
    const projectedTotal = this.metrics.currentMonthCost + estimatedCost;

    if (projectedTotal > this.config.maxMonthlySpend) {
      throw new Error(`Budget exceeded. Current: $${this.metrics.currentMonthCost.toFixed(2)}, Estimated: $${estimatedCost.toFixed(2)}, Limit: $${this.config.maxMonthlySpend}`);
    }

    const percentage = (projectedTotal / this.config.maxMonthlySpend) * 100;
    if (percentage >= this.config.warningThreshold) {
      console.warn(`Budget warning: ${percentage.toFixed(1)}% of monthly limit used`);
    }
  }

  async transcribe(audioUrl: string, estimatedDurationMinutes: number) {
    this.checkBudget(estimatedDurationMinutes);

    const startTime = Date.now();

    const { result, error } = await this.client.listen.prerecorded.transcribeUrl(
      { url: audioUrl },
      {
        model: this.config.model,
        smart_format: this.config.enabledFeatures.smartFormat,
        diarize: this.config.enabledFeatures.diarization,
      }
    );

    if (error) throw error;

    // Track actual usage
    const actualDuration = result.metadata.duration / 60; // seconds to minutes
    const cost = this.calculateCost(actualDuration);

    this.metrics.currentMonthMinutes += actualDuration;
    this.metrics.currentMonthCost += cost;

    return {
      transcript: result.results.channels[0].alternatives[0].transcript,
      metadata: {
        duration: actualDuration,
        cost,
        model: this.config.model,
      },
    };
  }

  getMetrics(): CostMetrics & { budgetRemaining: number } {
    return {
      ...this.metrics,
      budgetRemaining: this.config.maxMonthlySpend - this.metrics.currentMonthCost,
    };
  }
}
```

### Audio Duration Reducer
```typescript
// lib/audio-reducer.ts
import ffmpeg from 'fluent-ffmpeg';

interface ReductionOptions {
  silenceThreshold: string; // dB
  silenceMinDuration: number; // seconds
  speed: number; // 1.0 = normal, 1.25 = 25% faster
}

export async function reduceDuration(
  inputPath: string,
  outputPath: string,
  options: Partial<ReductionOptions> = {}
): Promise<{ originalDuration: number; reducedDuration: number; savings: number }> {
  const {
    silenceThreshold = '-30dB',
    silenceMinDuration = 0.5,
    speed = 1.0,
  } = options;

  return new Promise((resolve, reject) => {
    let originalDuration = 0;
    let reducedDuration = 0;

    ffmpeg(inputPath)
      .on('codecData', (data) => {
        originalDuration = parseDuration(data.duration);
      })
      // Remove silence
      .audioFilters([
        `silenceremove=start_periods=1:start_silence=${silenceMinDuration}:start_threshold=${silenceThreshold}`,
        `silenceremove=stop_periods=-1:stop_silence=${silenceMinDuration}:stop_threshold=${silenceThreshold}`,
        // Optionally speed up
        ...(speed !== 1.0 ? [`atempo=${speed}`] : []),
      ])
      .output(outputPath)
      .on('end', () => {
        ffmpeg.ffprobe(outputPath, (err, metadata) => {
          if (err) return reject(err);
          reducedDuration = metadata.format.duration || 0;
          resolve({
            originalDuration,
            reducedDuration,
            savings: ((originalDuration - reducedDuration) / originalDuration) * 100,
          });
        });
      })
      .on('error', reject)
      .run();
  });
}

function parseDuration(duration: string): number {
  const parts = duration.split(':').map(Number);
  return parts[0] * 3600 + parts[1] * 60 + parts[2];
}
```

### Usage Dashboard
```typescript
// lib/usage-dashboard.ts
import { createClient } from '@deepgram/sdk';

interface UsageSummary {
  period: { start: Date; end: Date };
  totalMinutes: number;
  totalCost: number;
  byModel: Record<string, { minutes: number; cost: number }>;
  byDay: Array<{ date: string; minutes: number; cost: number }>;
  projections: {
    monthlyMinutes: number;
    monthlyCost: number;
  };
}

export class UsageDashboard {
  private client;
  private projectId: string;

  constructor(apiKey: string, projectId: string) {
    this.client = createClient(apiKey);
    this.projectId = projectId;
  }

  async getUsageSummary(daysBack = 30): Promise<UsageSummary> {
    const end = new Date();
    const start = new Date(end.getTime() - daysBack * 24 * 60 * 60 * 1000);

    // Get usage data from Deepgram API
    const { result, error } = await this.client.manage.getProjectUsageRequest(
      this.projectId,
      {
        start: start.toISOString(),
        end: end.toISOString(),
      }
    );

    if (error) throw error;

    // Aggregate data
    const byModel: Record<string, { minutes: number; cost: number }> = {};
    const byDay: Map<string, { minutes: number; cost: number }> = new Map();

    let totalMinutes = 0;
    let totalCost = 0;

    for (const request of result.requests || []) {
      const minutes = (request.duration || 0) / 60;
      const model = request.model || 'unknown';
      const cost = this.calculateCost(minutes, model);
      const dateKey = new Date(request.created).toISOString().split('T')[0];

      totalMinutes += minutes;
      totalCost += cost;

      if (!byModel[model]) {
        byModel[model] = { minutes: 0, cost: 0 };
      }
      byModel[model].minutes += minutes;
      byModel[model].cost += cost;

      if (!byDay.has(dateKey)) {
        byDay.set(dateKey, { minutes: 0, cost: 0 });
      }
      const day = byDay.get(dateKey)!;
      day.minutes += minutes;
      day.cost += cost;
    }

    // Calculate projections
    const dailyAverage = totalMinutes / daysBack;
    const daysInMonth = 30;

    return {
      period: { start, end },
      totalMinutes,
      totalCost,
      byModel,
      byDay: Array.from(byDay.entries()).map(([date, data]) => ({
        date,
        ...data,
      })),
      projections: {
        monthlyMinutes: dailyAverage * daysInMonth,
        monthlyCost: (totalCost / daysBack) * daysInMonth,
      },
    };
  }

  private calculateCost(minutes: number, model: string): number {
    const rates: Record<string, number> = {
      'nova-2': 0.0043,
      'nova': 0.0043,
      'base': 0.0048,
      'enhanced': 0.0145,
    };
    return minutes * (rates[model] || 0.0043);
  }
}
```

### Cost Alerts
```typescript
// lib/cost-alerts.ts
import { UsageDashboard } from './usage-dashboard';

interface AlertConfig {
  dailyLimit: number;
  weeklyLimit: number;
  monthlyLimit: number;
  alertChannels: Array<'email' | 'slack' | 'webhook'>;
}

export class CostAlerts {
  private dashboard: UsageDashboard;
  private config: AlertConfig;
  private alertsSent: Set<string> = new Set();

  constructor(dashboard: UsageDashboard, config: Partial<AlertConfig> = {}) {
    this.dashboard = dashboard;
    this.config = {
      dailyLimit: config.dailyLimit ?? 10,
      weeklyLimit: config.weeklyLimit ?? 50,
      monthlyLimit: config.monthlyLimit ?? 200,
      alertChannels: config.alertChannels ?? ['email'],
    };
  }

  async checkAndAlert(): Promise<void> {
    const daily = await this.dashboard.getUsageSummary(1);
    const weekly = await this.dashboard.getUsageSummary(7);
    const monthly = await this.dashboard.getUsageSummary(30);

    const alerts: string[] = [];

    if (daily.totalCost > this.config.dailyLimit) {
      alerts.push(`Daily spend ($${daily.totalCost.toFixed(2)}) exceeds limit ($${this.config.dailyLimit})`);
    }

    if (weekly.totalCost > this.config.weeklyLimit) {
      alerts.push(`Weekly spend ($${weekly.totalCost.toFixed(2)}) exceeds limit ($${this.config.weeklyLimit})`);
    }

    if (monthly.totalCost > this.config.monthlyLimit) {
      alerts.push(`Monthly spend ($${monthly.totalCost.toFixed(2)}) exceeds limit ($${this.config.monthlyLimit})`);
    }

    // Send alerts (deduplicated)
    for (const alert of alerts) {
      const alertKey = `${new Date().toDateString()}-${alert}`;
      if (!this.alertsSent.has(alertKey)) {
        await this.sendAlert(alert);
        this.alertsSent.add(alertKey);
      }
    }
  }

  private async sendAlert(message: string): Promise<void> {
    console.log(`COST ALERT: ${message}`);

    for (const channel of this.config.alertChannels) {
      switch (channel) {
        case 'slack':
          await this.sendSlackAlert(message);
          break;
        case 'email':
          await this.sendEmailAlert(message);
          break;
        case 'webhook':
          await this.sendWebhookAlert(message);
          break;
      }
    }
  }

  private async sendSlackAlert(message: string): Promise<void> {
    const webhookUrl = process.env.SLACK_WEBHOOK_URL;
    if (!webhookUrl) return;

    await fetch(webhookUrl, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        text: `Deepgram Cost Alert: ${message}`,
      }),
    });
  }

  private async sendEmailAlert(message: string): Promise<void> {
    // Implement email sending
  }

  private async sendWebhookAlert(message: string): Promise<void> {
    // Implement webhook sending
  }
}
```

### Model Selection for Cost
```typescript
// lib/cost-aware-model.ts
interface ModelRecommendation {
  model: string;
  estimatedCost: number;
  qualityLevel: 'high' | 'medium' | 'low';
  reason: string;
}

export function recommendModel(params: {
  audioDurationMinutes: number;
  monthlyBudget: number;
  currentMonthSpend: number;
  qualityRequirement: 'high' | 'medium' | 'any';
}): ModelRecommendation {
  const { audioDurationMinutes, monthlyBudget, currentMonthSpend, qualityRequirement } = params;
  const budgetRemaining = monthlyBudget - currentMonthSpend;

  const models = [
    { name: 'nova-2', rate: 0.0043, quality: 'high' as const },
    { name: 'nova', rate: 0.0043, quality: 'high' as const },
    { name: 'base', rate: 0.0048, quality: 'low' as const },
  ];

  // Filter by quality requirement
  const eligible = models.filter(m => {
    if (qualityRequirement === 'high') return m.quality === 'high';
    if (qualityRequirement === 'medium') return m.quality !== 'low';
    return true;
  });

  // Find cheapest that fits budget
  for (const model of eligible.sort((a, b) => a.rate - b.rate)) {
    const cost = audioDurationMinutes * model.rate;
    if (cost <= budgetRemaining) {
      return {
        model: model.name,
        estimatedCost: cost,
        qualityLevel: model.quality,
        reason: `Best value within budget ($${budgetRemaining.toFixed(2)} remaining)`,
      };
    }
  }

  // Fallback to cheapest
  const cheapest = eligible[0];
  return {
    model: cheapest.name,
    estimatedCost: audioDurationMinutes * cheapest.rate,
    qualityLevel: cheapest.quality,
    reason: 'Warning: May exceed budget',
  };
}
```

## Resources
- [Deepgram Pricing](https://deepgram.com/pricing)
- [Usage API Reference](https://developers.deepgram.com/reference/get-usage)
- [Cost Optimization Guide](https://developers.deepgram.com/docs/cost-optimization)

## Next Steps
Proceed to `deepgram-reference-architecture` for architecture patterns.
