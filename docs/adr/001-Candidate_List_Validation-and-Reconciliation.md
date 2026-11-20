# ADR-001: Candidate List Validation and Reconciliation

## Status

Accepted

## Problem

The supplied candidate list could not be assumed to be analysis-ready.

The list contained duplicate IDs, missing values, invalid IDs, and identifiers that did not correspond to valid TMDb movie records.

## Impact

Analyzing the list without validation could:

- Double-count films
- Exclude films silently
- Produce incorrect rankings
- Undermine confidence in the final recommendation

The acquisition rubric specifically requires every supplied ID to be accounted for.

## Decision

The candidate list was validated before acquisition.

The following checks were performed:

- Duplicate detection
- Missing value detection
- Identifier format validation
- Retrieval success tracking

Every supplied record was assigned a final status through a reconciliation process.

## Alternative Considered

### Attempt retrieval without validation

Retrieve every record and ignore failures.

### Why Someone Might Choose It

It is faster to implement and requires less code.

### Why Rejected

Failures become difficult to explain and recommendation quality cannot be defended.

## Trade-Off

Additional validation effort was required before analysis.

## Cost if Wrong

Undetected data-quality issues may produce misleading recommendations.

## Evidence

Validation identified:

- 126 candidate rows
- 6 duplicate IDs
- 1 missing ID
- 1 IMDb identifier
- 1 invalid negative ID
- 117 valid TMDb IDs
- 112 successful retrievals
- 5 failed retrievals (http: 404)