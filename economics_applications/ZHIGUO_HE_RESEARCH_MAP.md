# Research Map: Zhiguo He → Machine Learning / AI Applications

This note maps the research program listed on Zhiguo He's research page into empirical/ML objects. It is a **research-inspired roadmap**, not a replication, collaboration, or endorsement.

The key principle is to preserve the economics: flexible ML is used to estimate a well-defined mechanism (heterogeneity, information, state dependence, text measurement, or nuisance functions), not as a substitute for identification.

## 1. Information, screening, and credit-market competition

Representative papers/projects:
- Information-Based Pricing in Specialized Lenders
- Information Span in Credit Market Competition
- Investing in Lending Technology: IT Spending in Banking
- Open Banking: Credit Market Competition When Borrowers Own the Data
- Tech-Driven Intermediation in the Originate-to-Distribute Model
- Information Acquisition in Rumor-based Bank Runs
- The Sale of Multiple Assets with Private Information

ML extensions:
- causal forests for heterogeneous specialist-lender effects,
- NLP/LLMs to measure how soft information becomes hard/transferable,
- Double ML for high-dimensional technology-adoption designs,
- causal graphs separating information quality from intermediation capacity.

## 2. Intermediary balance sheets, liquidity, and systemic risk

Representative papers/projects:
- Intermediation via Credit Chains
- A Macroeconomic Framework for Quantifying Systemic Risk
- Intermediary Asset Pricing and the Financial Crisis
- Intermediary Asset Pricing: New Evidence from Many Asset Classes
- Intermediary Asset Pricing
- A Model of Capital and Crises
- Balance Sheet Adjustment in the 2008 Crisis
- Treasury Inconvenience Yields during the COVID-19 Crisis
- Commonality in Credit Spread Changes: Dealer Inventory and Intermediary Distress
- Quantifying Liquidity and Default Risks of Corporate Bonds over the Business Cycle
- Endogenous Liquidity and Defaultable Bonds
- Rollover Risk and Credit Risk
- Dynamic Debt Runs

ML extensions:
- nonlinear state-dependent forecasting with intermediary capital,
- sequence models for stress propagation through credit chains,
- graph neural networks for multi-layer intermediary networks,
- regime-sensitive models of credit spreads and liquidity.

## 3. Asset demand, market equilibrium, and identification

Representative papers/projects:
- Demand Elasticity in Dynamic Asset Pricing
- Causal Inference for Asset Pricing
- Agency MBS as Safe Assets
- A Model of Safe Asset Determination
- What Makes US Government Bonds Safe Assets?
- Debt Financing in Asset Markets
- Delegated Asset Management, Investment Mandates, and Capital Immobility
- Inefficient Investment Waves

ML extensions:
- high-dimensional demand estimation with explicit equilibrium correction,
- tests showing that predictive/causal ML cannot recover the "missing coefficient" from cross-sectional variation alone,
- neural approximations to equilibrium policies paired with structural restrictions,
- state-dependent demand elasticities rather than a single static coefficient.

## 4. Dynamic capital structure, debt maturity, and contracting

Representative papers/projects:
- More Frequent Than You Think: Revisiting Capital Structure Adjustment
- Sovereign Debt Ratchets and Welfare Destruction
- Leverage Dynamics without Commitment
- Dynamic Debt Maturity
- Debt and Creative Destruction: Why Could Subsidizing Corporate Debt Be Optimal?
- A Theory of Debt Maturity: The Long and Short of Debt Overhang
- Optimal Long-term Contracting with Learning
- Uncertainty, Risk, and Incentives: Theory and Evidence
- Dynamic Compensation Contracts with Private Savings
- A Model of Dynamic Compensation and Capital Structure
- Dynamic Agency and q Theory of Investment
- Optimal Executive Compensation when Firm Size Follows Geometric Brownian Motion

ML extensions:
- survival/hazard models for refinancing and maturity adjustment,
- neural dynamic programming as an approximation tool, with economics retained in state/action constraints,
- heterogeneous policy functions by firm size,
- reinforcement learning as a numerical comparison to commitment/no-commitment benchmarks.

## 5. Technology adoption, organization, and measurement

Representative papers/projects:
- Why Don't Old Firms Do New Things?
- An Economic Model of Consensus on Distributed Ledgers
- Don't Trust, Verify: The Case of Slashing from a Popular Ethereum Explorer
- Decentralized Mining in Centralized Pools
- Blockchain Disruption and Smart Contracts
- What Gets Measured Gets Managed: Investment and the Cost of Capital

ML extensions:
- transformer classification of workstyle/task changes induced by new technologies,
- text embeddings to measure technological distance from incumbent organizational routines,
- causal ML around staggered technology or measurement reforms,
- graph/network ML for decentralized consensus and pool formation.

## 6. China: policy shocks, market design, and spatial/financial frictions

Representative papers/projects:
- Earnings Management and Price Informativeness
- Homemade Foreign Trading
- Household Migration and Collateral Constraint
- Land (Mis)allocation and Local Public Financing in China
- Share Pledging in China: Funding Listed Firms or Funding Entrepreneurship?
- The Drivers and Implications of Retail Margin Trading
- Valuing Long-Term Property Rights with Anticipated Political Regime Shifts
- China's Financial System and Economy: A Review
- The Stock Connect to China
- Pledgeability and Asset Prices: Evidence from the Chinese Corporate Bond Markets
- The Financing of Local Government in China: Stimulus Loan Wanes and Shadow Banking Waxes
- Chinese Bond Market and Interbank Market

ML extensions:
- causal ML to characterize treatment heterogeneity around reforms,
- NLP measures of earnings/corporate disclosure manipulation,
- anomaly/network detection for round-tripping and cross-border flows,
- spatial ML combined with structural location choice,
- heterogeneous effects of collateral/pledgeability shocks.

## The six implementations in these forks

| Repository | Application | Economic object |
|---|---|---|
| EconML | Specialized lending × information span | CATE of specialized lending |
| DoubleML | Bank IT and lending | causal effect with high-dimensional nuisance functions |
| CausalML | Open banking | distribution of borrower treatment effects |
| DoWhy | Technology-driven intermediation | explicit causal mechanism/DAG |
| NeuralForecast | Intermediary stress | nonlinear dynamic state dependence |
| FinGPT | Soft-to-hard information | text-based span vs precision measurement |

## What should come next

The most ambitious extension is to connect the modules:

```text
financial text / loan documents
        ↓
FinGPT: span + precision measures
        ↓
EconML / DoubleML: causal effects and heterogeneity
        ↓
DoWhy: mechanism audit
        ↓
NeuralForecast: aggregate/intermediary dynamics
        ↓
structural equilibrium model: competition + welfare
```

That pipeline would move from unstructured information to micro causal evidence and then to equilibrium consequences, which is much closer to an economics research program than a standalone ML benchmark.

Source map: https://zhiguohe.net/publications/research/
