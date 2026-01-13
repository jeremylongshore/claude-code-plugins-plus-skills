# Mode System (V3.1.1)

## Mode System (v3.1.1)

This skill supports four modes to adapt to different cognitive styles and accessibility needs:

### Mode Selection

**Base Modes** (choose one):
1. **Neurodivergent Mode** - ADHD-friendly, energy-aware, compassionate language
2. **Neurotypical Mode** - Direct, efficient, standard cognitive load

**Accessibility Modes** (optional, combinable with base modes):
3. **Colorblind-Safe Mode** - Pattern-based differentiation for all color vision types
4. **Monochrome Mode** - Pure black & white optimized for printing and e-ink displays

#### Mode Combinations Available:
- Neurodivergent + Colorblind-Safe
- Neurodivergent + Monochrome
- Neurotypical + Colorblind-Safe
- Neurotypical + Monochrome
- Colorblind-Safe only (no base mode features)
- Monochrome only (no base mode features)

#### Selection Methods:

#### 1. Auto-Detect (Default)
- Analyzes user language for distress signals ("overwhelmed", "paralyzed", "stuck")
- Detects mentions of neurodivergent conditions or executive dysfunction
- Detects accessibility requests ("colorblind-safe", "print-friendly", "grayscale")
- Defaults to neurodivergent mode when ambiguous (inclusive design)

#### 2. Explicit Mode Request
- User says: "Use neurotypical mode" or "Use ADHD mode"
- User says: "Use colorblind-safe mode" or "Make it print-friendly"
- User says: "Combine neurodivergent and colorblind-safe modes"
- Persists for current conversation unless changed

#### 3. Configuration File
- User creates: `.claude/neurodivergent-visual-org-preference.yml`
- Sets default base mode, accessibility modes, time multipliers, chunk sizes
- Can set auto-enable rules (e.g., monochrome for PDFs)

### Mode Characteristics

#### Base Mode Features:

| Aspect | Neurodivergent Mode | Neurotypical Mode |
|--------|---------------------|-------------------|
| Chunk size | 3-5 items | 5-7 items |
| Time estimates | 1.5-2x with buffer | Standard |
| Task granularity | 3-10 min micro-steps | 15-30 min tasks |
| Language | Compassionate, validating | Direct, efficient |
| Colors | Calming (blues/greens) | Standard themes |
| Energy scaffolding | Explicit (spoons, breaks) | Minimal |

#### Accessibility Mode Features:

| Aspect | Colorblind-Safe Mode | Monochrome Mode |
|--------|---------------------|-----------------|
| Color usage | Redundant (patterns + color) | Pure B&W only (#000/#fff) |
| Border patterns | Dashed/dotted variations | Solid/dashed/dotted styles |
| Text labels | Prefixed ([KEEP], [DONATE]) | Verbose ([✓ KEEP], [? MAYBE]) |
| Shape coding | Diamond/hexagon/trapezoid | Distinct geometric shapes |
| Fill patterns | N/A (white fill, patterned borders) | Solid/crosshatch/dots/white |
| Border thickness | 1-3px for hierarchy | 1-3px for hierarchy |
| Symbols | Redundant icons (✅ 📦 🤔) | Text-based (✓ → ?) |
| Best for | All color vision types | B&W printing, e-ink displays |
| WCAG compliance | 2.1 AA (Use of Color 1.4.1) | 2.1 AAA (Maximum contrast) |

#### Mode Combination Notes:
- Base mode controls language, time estimates, and cognitive scaffolding
- Accessibility mode controls visual encoding (patterns, contrast, shapes)
- Both can be active simultaneously for maximum accommodation

### Backward Compatibility

v3.1.1 maintains v3.0 behavior:
- Defaults to neurodivergent base mode (v2.0 compatible)
- Accessibility modes are opt-in (not enabled by default)
- v3.0 visualizations remain valid (no breaking changes)