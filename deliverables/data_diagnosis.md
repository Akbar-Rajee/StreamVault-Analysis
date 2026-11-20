# Data Diagnosis

## Executive Summary

The supplied candidate list required validation before analysis. Several data quality issues were identified and addressed prior to creating recommendations.

Original candidate rows: 126

Valid unique TMDb IDs: 117

Successfully analyzed titles: 112

Failed retrievals (http: 404): 5

---

# Risk-Ranked Findings

| Rank | Issue | Evidence | Potential Impact | Risk |
|--------|---------|---------|---------|---------|
| 1 | Unretrievable TMDb IDs | 5 IDs failed movie-detail retrieval | Titles could not be analyzed and were excluded from recommendations | High |
| 2 | Dependence on collection metadata | Franchise classification relies on TMDb collection information | Misclassification could affect franchise-versus-standalone comparisons | High |
| 3 | Historical reporting effects | Older films may be affected by inflation and historical box-office reporting differences | Could distort financial comparisons | Medium |
| 4 | Duplicate candidate records | 6 duplicate entries identified | Could inflate franchise or standalone performance if not removed | Medium |
| 5 | IMDb identifier present in TMDb list | One IMDb-style identifier (tt0468569) identified | Candidate unavailable for analysis | Low |
| 6 | Missing identifier | One missing ID identified | Candidate unavailable for analysis | Low |
| 7 | Invalid negative identifier | One invalid ID (-1) identified | Candidate unavailable for analysis | Low |

---

# Candidate List Validation

The supplied candidate list contained:

- 126 total rows
- 6 duplicate IDs
- 1 missing ID
- 1 IMDb identifier
- 1 invalid negative identifier

After validation and deduplication, 117 valid TMDb IDs remained for retrieval.

---

# Acquisition Results

Movie details were successfully retrieved for 112 titles.

Five records could not be retrieved through the TMDb movie-details endpoint and were excluded from analysis.

Excluded IDs:

- 8471293
- 9412887
- 8471294
- 9412888
- 7733901

---

# Recommendation Impact

The recommendation was based on 112 successfully analyzed films.

The unavailable titles could not be evaluated and therefore introduce uncertainty. However, the franchise recommendation remained stable across:

- All-years analysis
- 2000-onward analysis
- Average-based comparisons
- Median-based comparisons

This suggests that the core recommendation is reasonably robust despite the excluded records.

---

# Data Reconciliation

| Stage | Count |
|---------|---------|
| Candidate rows received | 126 |
| Valid unique TMDb IDs | 117 |
| Successful retrievals | 112 |
| Failed retrievals | 5 |

The totals reconcile successfully.