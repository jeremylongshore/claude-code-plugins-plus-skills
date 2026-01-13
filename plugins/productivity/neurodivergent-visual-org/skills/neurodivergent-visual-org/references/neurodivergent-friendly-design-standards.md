# Neurodivergent-Friendly Design Standards

## Neurodivergent-Friendly Design Standards

### Color Psychology for ADHD

#### Primary Palette (Use These)
- **Blues and greens** in soft, muted tones - promote tranquility and focus
- **Muted browns** - provide grounding without stimulation
- **Soft pastels** (light blues, lavenders, pale greens) - reduce visual stress
- **Muted yellows** (sparingly) - boost energy without overstimulation

#### Avoid
- Bright reds, oranges, intense yellows - increase hyperactivity/agitation
- Bright saturated colors - cause sensory overload
- Clashing color combinations - create visual stress

#### Implementation
- Use `forest` theme (green-based) or `neutral` theme (muted earth tones)
- Apply 60-30-10 rule: 60% calming background, 30% secondary, 10% accent
- Maintain 4.5:1 contrast ratio minimum (WCAG compliance)
- Never rely on color alone - pair with icons, patterns, or text labels

### Information Density Management

#### Miller's Law + ADHD Considerations
- Working memory holds 5-7 chunks (neurotypical) or 3-5 chunks (ADHD)
- Stay at lower end (3-5 chunks) to prevent cognitive overload
- Increased cognitive load reduces ADHD performance more severely

#### Practical Limits
- **Flowcharts**: 15-20 nodes maximum before splitting into multiple diagrams
- **Mindmaps**: 3-4 levels deep maximum
- **Pie charts**: 6-8 slices for readability
- **Lists**: No more than 2 lists of 3-5 items per diagram
- **Sections**: Use timeline/journey sections to chunk events logically

#### Implementation
- Break complex diagrams into digestible sections
- Use progressive disclosure (show relevant info upfront, details on demand)
- Provide TL;DR sections at beginning of complex diagrams
- Include generous white space between elements

### Visual Hierarchy Principles

**Size Contrast** (must be dramatic for ADHD attention)
- H1 significantly larger than H2, which is notably larger than body text
- Important nodes visibly larger than standard nodes
- Use `classDef` to style critical elements distinctly

#### Priority Signaling
- Distinguish important information through bold or color
- Use visual highlights for critical numbers or elements
- Separate each instruction clearly
- Implement color-coded systems for immediate visual feedback

#### Avoid
- Competing visual elements fighting for attention
- Auto-playing animations or flashy effects (extremely distracting)
- Blinking or flashing elements
- More than 2 fonts per diagram