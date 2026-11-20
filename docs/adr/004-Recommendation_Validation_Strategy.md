# ADR-004: Recommendation Validation Strategy

## Status

Accepted

## Problem

A recommendation based on a single analytical view may be influenced by historical reporting differences or blockbuster outliers.

Finance explicitly raised concerns regarding older films.

## Impact

The board may challenge recommendations that only work under one analytical perspective.

## Decision

The recommendation was tested using three separate approaches:

1. All-years analysis
2. 2000-onward analysis
3. Median-based comparison

## Alternative Considered

### Single Analysis View

Perform one franchise-versus-standalone comparison using all available data.

### Why Someone Might Choose It

It is simpler and faster to implement.

### Why Rejected

It does not demonstrate whether the recommendation is stable.

## Trade-Off

Additional analytical work was required.

## Cost if Wrong

The final recommendation may appear stronger than the underlying evidence supports.

## Evidence

Across all three tests:

- Franchises outperformed standalones
- The recommendation did not change
- The Avengers Collection remained the strongest franchise candidate

This increased confidence in the final recommendation.