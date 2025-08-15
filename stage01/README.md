# ETF Strategy Sustainability Analysis
**Stage:** Problem Framing & Scoping (Stage 01)

## Problem Statement
In our investment research team, we regularly evaluate exchange-traded fund (ETF) strategies to decide whether to continue using them in the next fiscal year.  
Currently, one of our quantitative ETF strategies has performed strongly over the past three years, but there is uncertainty about its performance in the upcoming year given possible market regime changes, interest rate shifts, and macroeconomic conditions.  
If the strategy stops outperforming its benchmark, continuing to allocate capital to it could reduce portfolio returns.

## Stakeholder & User
- **Decision Owner (Stakeholder):** Chief Investment Officer (CIO)
- **End User:** Portfolio managers who allocate capital to ETF strategies
- **Usage Context & Cadence:** Decision will be made during the annual investment strategy review in Q4; output will feed into next-year allocation plans.

## Useful Answer & Decision
- **Type:** Predictive
- **Form:** Analytical report with backtest updates, forward-looking scenario analysis, and statistical performance projections
- **Supports Decision:** Decide whether to keep, scale, or retire the ETF strategy for the next fiscal year

## Assumptions & Constraints
- Historical performance and factor exposure data for the ETF are available for at least 5 years
- Macroeconomic and sector data are accessible from Bloomberg/Refinitiv
- Forecasting will be based on publicly available economic indicators; no inside information will be used
- Analysis must be completed within 3 weeks before Q4 strategy meeting

## Known Unknowns / Risks
- Future market regimes may differ significantly from historical patterns
- Macro shocks (e.g., geopolitical crises) could invalidate predictions
- Data availability for certain ETFs may be incomplete

## Lifecycle Mapping
Goal → Stage → Deliverable
- Determine if ETF strategy remains viable → Stage 01 → Problem framing, repo setup, stakeholder memo

## Repo Plan
/data/, /src/, /notebooks/, /docs/; updates twice per week
