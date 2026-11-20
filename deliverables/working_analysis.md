# Working Analysis

## Objective

The objective of this analysis was to determine whether StreamVault should prioritize franchise bundle acquisitions or standalone film acquisitions and to identify the strongest licensing targets within the candidate portfolio.

---

# Acquisition Summary

The candidate list contained 126 rows.

Data validation identified:

- 6 duplicate identifiers
- 1 missing identifier
- 1 IMDb identifier mistakenly included in the TMDb field
- 1 invalid negative identifier

After validation and deduplication:

- 117 valid TMDb identifiers remained for retrieval

Retrieval results:

- 112 successful movie-detail retrievals
- 5 unsuccessful movie-detail retrievals

Only successfully retrieved titles were included in the final analysis.

---

# Data Transformation

TMDb movie-detail responses were transformed into a movie-level analytical table.

Key fields included:

- Movie ID
- Title
- Release Date
- Budget
- Revenue
- Collection Information
- Popularity
- Vote Metrics

Derived fields:

## Profit

Profit = Revenue − Budget

## ROI

ROI = Profit / Budget

## Franchise Flag

A title was flagged as a franchise film when collection metadata was available.

## Release Year

Release year was extracted from the release date field to support time-window analysis.

---

# Analytical Structure

Three analytical tables were created:

## Movies Table

One row per movie.

Rows: 112

## Directors Table

One row per movie-director relationship.

Rows: 122

Some films contained multiple directors, resulting in additional rows.

## Actors Table

One row per movie.

The first billed actor was treated as the lead actor.

Rows: 112

---

# Join Validation

Coverage checks were performed following transformation.

| Dataset | Unique Movies |
|----------|----------|
| Movies | 112 |
| Directors | 112 |
| Actors | 112 |

No movies were lost during transformation.

Additional director rows were expected because some films contained multiple directors.

---

# Franchise vs Standalone Analysis

Commercial performance was evaluated using:

- Revenue
- Profit
- ROI

## All Years

Franchise films outperformed standalone films on:

- Average revenue
- Average profit
- Average ROI

## 2000 Onward

Franchise films continued to outperform standalone films on:

- Average revenue
- Average profit
- Average ROI

The recommendation did not change after restricting the analysis to films released from 2000 onward.

---

# Median Sensitivity Test

Average values can be influenced by blockbuster outliers.

To test recommendation stability, median performance was also evaluated.

| Metric | Standalone | Franchise |
|----------|------------|------------|
| Median Revenue | $161.8M | $578.9M |
| Median Profit | $135.6M | $489.3M |
| Median ROI | 2.84 | 4.62 |

Franchise films outperformed standalone films across all median measures.

The recommendation remained unchanged.

---

# Franchise Ranking

Franches were ranked using:

- Average Profit
- Average Revenue
- ROI
- Minimum Evidence Threshold (3 titles)

Top franchise targets:

1. The Avengers Collection
2. Harry Potter Collection
3. The Lord of the Rings Collection

---

# Standalone Ranking

Standalone films were ranked using commercial performance measures.

Top standalone targets:

1. Inception
2. Forrest Gump
3. Interstellar
4. WALL·E
5. Schindler's List

---

# Talent Signals

## Directors

Strongest director signals:

- Peter Jackson
- David Yates
- Christopher Nolan

## Lead Actors

Strongest lead actor signals:

- Robert Downey Jr.
- Daniel Radcliffe
- Tom Hanks

Talent signals required multiple appearances within the analyzed dataset.

---

# Runtime and Scalability

The analytical workflow completed in approximately 0.06 seconds on the analyzed dataset.

The acquisition phase scales with the number of API requests.

Transformation, aggregation, and statistical calculations were performed using vectorized pandas operations and are expected to scale efficiently to future candidate lists containing approximately 500 titles.

---

# Key Finding

Across all tested scenarios:

- All Years
- 2000 Onward
- Median-Based Comparison

Franchise films consistently outperformed standalone films.

The recommendation therefore remained stable across all sensitivity tests.