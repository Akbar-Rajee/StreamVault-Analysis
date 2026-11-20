# Decision Notes

## Purpose

The StreamVault brief required several judgement calls that were not explicitly defined. This document records each decision, the rationale behind it, alternatives considered, and the potential cost if the decision proves incorrect.

---

# Decision 1: Franchise Classification

## Assumption

A film was classified as a franchise title when TMDb returned a non-null `belongs_to_collection` value.

## Reason

TMDb collections provide an explicit and reproducible grouping mechanism that can be applied automatically during future reruns of the analysis.

## Rejected Alternative

Manually grouping films by title similarity or external franchise knowledge.

## Why Rejected

Manual classification introduces subjectivity and would be difficult for Adjoa to reproduce during future quarterly reruns.

## Cost if Wrong

If collection metadata is incomplete for some titles, certain franchise films may be incorrectly classified as standalones, affecting the franchise-versus-standalone comparison.

---

# Decision 2: Standalone Classification

## Assumption

A film was classified as standalone when no collection information was available.

## Reason

This rule is the direct complement of the franchise classification rule and ensures complete coverage of the dataset.

## Rejected Alternative

Creating a third "unclassified" category.

## Why Rejected

The available data did not support a consistent method for identifying uncertain cases.

## Cost if Wrong

Some films may be misclassified if TMDb collection metadata is incomplete.

---

# Decision 3: Minimum Franchise Evidence Threshold

## Assumption

A franchise required at least three titles within the analyzed dataset before being considered for the franchise shortlist.

## Reason

Single-title and two-title collections provide insufficient evidence of franchise-level performance and may be dominated by individual outliers.

## Rejected Alternative

Include all collections regardless of size.

## Why Rejected

This would allow rankings to be heavily influenced by a single exceptional film.

## Cost if Wrong

Potentially valuable smaller franchises may be excluded from consideration.

---

# Decision 4: Commercial Strength Metrics

## Assumption

Commercial performance was evaluated using:

- Revenue
- Profit
- Return on Investment (ROI)

Where:

Profit = Revenue - Budget

ROI = Profit / Budget

## Reason

The licensing decision is fundamentally a financial decision. Revenue, profit, and ROI collectively capture scale, value creation, and efficiency.

## Rejected Alternative

Using ratings, popularity scores, or vote counts as primary decision drivers.

## Why Rejected

These metrics do not directly measure commercial performance and therefore have limited value for acquisition decisions.

## Cost if Wrong

Some culturally significant or strategically valuable titles may be undervalued.

---

# Decision 5: Time Window Comparison

## Assumption

Results were produced for both:

1. All available years
2. Films released from 2000 onward

## Reason

The brief identified concerns regarding historical box-office reporting and inflation effects on older films.

## Rejected Alternative

Use only a single time window.

## Why Rejected

A single-period analysis would not address stakeholder concerns.

## Cost if Wrong

Differences caused by historical reporting methods may remain hidden.

---

# Decision 6: Director Talent Signal Threshold

## Assumption

A director must appear in at least two analyzed films before being considered a talent signal.

## Reason

One successful film is not sufficient evidence of repeatable commercial performance.

## Rejected Alternative

Include all directors regardless of sample size.

## Why Rejected

Single-film appearances provide weak evidence.

## Cost if Wrong

Emerging directors with limited representation may be overlooked.

---

# Decision 7: Lead Actor Definition

## Assumption

The lead actor was defined as the first billed cast member returned by the TMDb credits endpoint.

## Reason

TMDb cast lists are ordered by billing prominence and provide a consistent, automated approach.

## Rejected Alternative

Treat all cast members equally.

## Why Rejected

The objective was to identify a primary talent signal rather than measure total cast quality.

## Cost if Wrong

Ensemble films may attribute commercial success to the wrong performer.

---

# Decision 8: Failed Retrieval Treatment

## Assumption

Titles that could not be retrieved from the TMDb movie details endpoint were excluded from analysis.

## Reason

Key analytical fields such as revenue, budget, and collection membership were unavailable.

## Rejected Alternative

Impute values or manually source information from other systems.

## Why Rejected

Doing so would reduce reproducibility and introduce inconsistency.

## Cost if Wrong

A commercially important title may be absent from the final recommendation.

# Sensitivity Testing

Three alternative views were tested.

## Test 1: All Years

Result:
Franchises outperformed standalone films.

## Test 2: 2000 Onward

Result:
Franchises continued to outperform standalone films.

## Test 3: Median-Based Comparison

Result:
Franchises continued to outperform standalone films in median revenue, median profit, and median ROI.

## What Remained Stable

Across all three tests:

- Franchise films outperformed standalone films.
- The Avengers Collection remained the strongest franchise candidate.
- Harry Potter and The Lord of the Rings remained among the strongest franchise targets.

The core recommendation did not change.