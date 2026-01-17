# ARD: Gas Fee Optimizer

## Architecture Pattern

**Analytics Pipeline Pattern** - Python CLI that fetches gas data, analyzes patterns, and provides optimization recommendations.

## Workflow

```
Data Collection → Analysis → Recommendation → Display
      ↓             ↓            ↓              ↓
  RPC + APIs    Historical   Timing/Price     Table/JSON
```

## Data Flow

```
Input: User request (current gas, optimal time, estimate for operation)
          ↓
Fetch: Multiple gas oracles (RPC, Etherscan, Blocknative)
          ↓
Aggregate: Combine sources, calculate percentiles
          ↓
Analyze: Compare to historical patterns
          ↓
Recommend: Optimal timing, price recommendation
          ↓
Output: Formatted results with USD costs
```

## Directory Structure

```
skills/optimizing-gas-fees/
├── PRD.md                    # This requirements doc
├── ARD.md                    # This architecture doc
├── SKILL.md                  # Agent instructions
├── scripts/
│   ├── gas_optimizer.py      # Main CLI entry point
│   ├── gas_fetcher.py        # Multi-source gas data
│   ├── pattern_analyzer.py   # Historical pattern detection
│   ├── cost_estimator.py     # Transaction cost estimation
│   └── formatters.py         # Output formatting
├── references/
│   ├── errors.md             # Error handling guide
│   └── examples.md           # Usage examples
└── config/
    └── settings.yaml         # Default configuration
```

## API Integration

### Ethereum RPC
- **Method**: `eth_gasPrice`, `eth_feeHistory`
- **Data**: Current gas price, base fee history

### Etherscan Gas Tracker
- **Endpoint**: `https://api.etherscan.io/api?module=gastracker`
- **Data**: Safe/Proposed/Fast gas prices

### Blocknative (Optional)
- **Endpoint**: `https://api.blocknative.com/gasprices/blockprices`
- **Data**: Confidence-based predictions

## Component Design

### gas_fetcher.py
```python
class GasFetcher:
    def get_current_gas(chain) -> GasData
    def get_gas_history(chain, blocks) -> List[GasData]
    def get_base_fee_trend() -> BaseFeeInfo
```

### pattern_analyzer.py
```python
class PatternAnalyzer:
    def analyze_hourly_pattern(history) -> HourlyPattern
    def analyze_daily_pattern(history) -> DailyPattern
    def find_optimal_window() -> TimeWindow
    def predict_gas(time) -> GasPrediction
```

### cost_estimator.py
```python
class CostEstimator:
    def estimate_transfer(gas_price) -> Cost
    def estimate_swap(gas_price, dex) -> Cost
    def estimate_nft_mint(gas_price) -> Cost
    def estimate_custom(gas_price, gas_limit) -> Cost
```

## Gas Price Tiers

| Tier | Percentile | Confirmation Target |
|------|------------|---------------------|
| Slow | 10th | 10+ blocks (~2+ min) |
| Standard | 50th | 3-5 blocks (~1 min) |
| Fast | 75th | 1-2 blocks (~30 sec) |
| Instant | 90th | Next block (~12 sec) |

## Historical Pattern Sources

1. **Hourly patterns**: Gas is typically lower during off-peak hours
2. **Daily patterns**: Weekends often have lower gas
3. **Event patterns**: NFT mints, token launches spike gas
4. **Network upgrades**: EIP implementations affect base fee

## Error Handling Strategy

| Error | Handling |
|-------|----------|
| RPC unavailable | Fallback to Etherscan oracle |
| Rate limited | Use cached data with staleness warning |
| Price fetch failed | Use last known good value |
| Invalid chain | Return error with supported chains list |

## Multi-Chain Support

| Chain | RPC Method | Oracle |
|-------|------------|--------|
| Ethereum | eth_feeHistory | Etherscan |
| Polygon | eth_feeHistory | Polygonscan |
| Arbitrum | eth_gasPrice | Arbiscan |
| Optimism | eth_gasPrice | Optimistic Etherscan |
| Base | eth_gasPrice | Basescan |

## Performance Considerations

- Cache gas data for 10-15 seconds
- Batch RPC calls where possible
- Store historical data locally for pattern analysis
- Limit history fetch to needed window

## Security

- No private keys required
- RPC URLs may contain API keys (handle securely)
- Read-only operations only
