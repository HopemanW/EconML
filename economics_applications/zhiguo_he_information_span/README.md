# Specialized Lending × Information Span (EconML)

This application turns two mechanisms from Zhiguo He's credit-market research into an estimable heterogeneous-treatment-effect design:

- **Information-Based Pricing in Specialized Lenders**: specialized lenders possess a borrower-relevant signal and can price on private information.
- **Information Span in Credit Market Competition**: financial technology can broaden the set of borrower characteristics that are transferable ("hard") rather than relationship-specific ("soft").

## Research question

> Does the causal pricing advantage of a specialized lender shrink when a larger span of borrower information becomes hard and transferable across competing lenders?

The treatment is borrowing from a specialized lender. The outcome is the loan spread. `CausalForestDML` estimates

\[
\tau(x)=E[\text{Spread}(1)-\text{Spread}(0)\mid X=x],
\]

with heterogeneity in information span, borrower opacity, relationship strength, quality, and market competition.

The synthetic DGP imposes a transparent economic prediction: specialization matters most when information is narrow and soft. As information span expands, nonspecialist lenders can compete on more dimensions and the specialist pricing advantage attenuates.

## Why this extends the papers

The papers develop equilibrium mechanisms around specialized information and the span/precision of hard information. This example adds a **high-dimensional empirical heterogeneity layer**: rather than estimating one average effect, it recovers how the treatment effect varies over borrower and market states.

This is deliberately an **inspired application, not a replication** and does not claim endorsement by the authors.

## Run

```bash
python economics_applications/zhiguo_he_information_span/specialized_lending_causal_forest.py
```

The script prints average true and estimated treatment effects by hard-information-span quintile.

## Real-data design

A real implementation can replace the synthetic DGP with a loan-level panel. Candidate columns:

| Economic object | Example empirical proxy |
|---|---|
| Specialized lender | lender industry concentration / historical sector share |
| Hard-information span | coverage of standardized accounting, ratings, covenant, registry, or machine-readable borrower variables |
| Soft information | relationship duration, geographic proximity, lender-borrower history |
| Outcome | all-in-drawn spread, loan rate, approval, commitment |
| Competition | number / concentration of plausible lenders |
| Balance-sheet capacity | bank capital or liquidity measures |

For syndicated loans, the treatment can be defined at lead-arranger or participant-bank level and the design can be extended to lender-borrower-network heterogeneity.

## Next research extensions

1. Separate **span** from **precision**: estimate a two-dimensional CATE surface.
2. Use lender fixed embeddings/network features as high-dimensional controls.
3. Add an instrument or quasi-experimental rollout for information hardening.
4. Estimate equilibrium spillovers: broader information changes not only treatment assignment but competitors' pricing behavior.
5. Compare causal forest estimates with a structural model of lender competition.

## References

- Zhiguo He research page: https://zhiguohe.net/publications/research/
- EconML: https://github.com/py-why/EconML
