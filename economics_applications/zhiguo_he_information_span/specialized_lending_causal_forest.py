"""Specialized lending and information span: a causal-forest application.

This is a synthetic, reproducible research design inspired by:
- He, Jiang, Li, and Zhou, "Information-Based Pricing in Specialized Lenders"
- He, Li, and Zhou, "Information Span in Credit Market Competition"

The script asks whether the pricing advantage from specialized lending is
heterogeneous in the span of transferable ("hard") borrower information.
It is an application/extension, not a replication of either paper.
"""

from __future__ import annotations

import numpy as np
import pandas as pd
from econml.dml import CausalForestDML
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor


def simulate_credit_market(n: int = 12_000, seed: int = 42):
    rng = np.random.default_rng(seed)

    hard_info_span = rng.beta(2.2, 2.0, n)
    borrower_quality = rng.normal(size=n)
    opacity = rng.beta(2.0, 3.0, n)
    relationship_strength = rng.beta(2.0, 2.0, n)
    bank_capital = rng.normal(size=n)
    market_competition = rng.uniform(0, 1, n)
    loan_size = np.exp(rng.normal(2.0, 0.7, n))
    specialist_signal = borrower_quality + rng.normal(
        scale=0.35 + 0.9 * hard_info_span, size=n
    )

    # Selection into specialist lending is endogenous in observables.
    index = (
        -0.35
        + 0.65 * opacity
        + 0.55 * relationship_strength
        - 0.35 * market_competition
        + 0.20 * borrower_quality
        + 0.15 * np.log1p(loan_size)
    )
    propensity = 1 / (1 + np.exp(-index))
    specialist = rng.binomial(1, propensity)

    # Economic extension:
    # specialist informational rents/advantages are largest when information
    # is narrow/soft, and shrink as more borrower information becomes hard
    # and transferable across lenders.
    true_cate = -90.0 * (1 - hard_info_span) * (0.55 + 0.45 * opacity)

    base_spread = (
        260
        - 38 * borrower_quality
        + 55 * opacity
        - 22 * bank_capital
        - 18 * market_competition
        - 5 * relationship_strength
        + 3.5 * np.log1p(loan_size)
    )
    spread_bps = base_spread + specialist * true_cate + rng.normal(0, 28, n)

    X = pd.DataFrame(
        {
            "hard_info_span": hard_info_span,
            "opacity": opacity,
            "relationship_strength": relationship_strength,
            "borrower_quality": borrower_quality,
            "market_competition": market_competition,
        }
    )
    W = pd.DataFrame(
        {
            "bank_capital": bank_capital,
            "log_loan_size": np.log1p(loan_size),
            "specialist_signal": specialist_signal,
        }
    )
    return spread_bps, specialist, X, W, true_cate


def estimate_cate(seed: int = 42) -> pd.DataFrame:
    y, treatment, X, W, true_cate = simulate_credit_market(seed=seed)

    est = CausalForestDML(
        model_y=RandomForestRegressor(
            n_estimators=250, min_samples_leaf=20, random_state=seed, n_jobs=-1
        ),
        model_t=RandomForestClassifier(
            n_estimators=250, min_samples_leaf=20, random_state=seed, n_jobs=-1
        ),
        discrete_treatment=True,
        n_estimators=600,
        min_samples_leaf=30,
        max_depth=None,
        random_state=seed,
        n_jobs=-1,
    )
    est.fit(y, treatment, X=X, W=W)
    cate_hat = est.effect(X)

    out = X.copy()
    out["true_cate_bps"] = true_cate
    out["estimated_cate_bps"] = cate_hat
    out["span_quintile"] = pd.qcut(
        out["hard_info_span"], 5, labels=["Q1 narrow", "Q2", "Q3", "Q4", "Q5 broad"]
    )
    return out


def summarize_by_information_span(results: pd.DataFrame) -> pd.DataFrame:
    return (
        results.groupby("span_quintile", observed=True)
        .agg(
            mean_span=("hard_info_span", "mean"),
            true_effect_bps=("true_cate_bps", "mean"),
            estimated_effect_bps=("estimated_cate_bps", "mean"),
            n=("estimated_cate_bps", "size"),
        )
        .reset_index()
    )


if __name__ == "__main__":
    results = estimate_cate()
    summary = summarize_by_information_span(results)
    print(summary.to_string(index=False))
    print(
        "\nPrediction: the specialized-lender spread advantage should attenuate "
        "as hard-information span broadens."
    )
