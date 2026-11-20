# StreamVault-Analysis
=======
# StreamVault Licensing Analysis

## Overview

This project analyzes a candidate portfolio of films provided by StreamVault to support a $14 million licensing decision.

The objective is to determine whether StreamVault should prioritize franchise bundle acquisitions or standalone film acquisitions, identify the strongest licensing targets, evaluate talent signals, and communicate a defensible recommendation to business stakeholders.

The analysis uses film metadata and credits retrieved from The Movie Database (TMDb) API and transforms nested JSON responses into analytical datasets suitable for business evaluation.

---

# Business Objective

Kwame Boateng, VP of Content Acquisition, requires evidence to support an upcoming licensing decision.

The analysis seeks to answer the following questions:

1. Should StreamVault prioritize franchise bundles or standalone films?
2. Which three franchises represent the strongest acquisition targets?
3. Which five standalone films represent the strongest alternatives?
4. Which directors and lead actors consistently signal commercial success?
5. What risks and uncertainties remain in the recommendation?

---

# Project Structure

```text
StreamVault Analysis
│
├── data
│   ├── raw
│   └── processed
│
├── deliverables
├── docs
│   └── adr
├── outputs
├── pipeline
│
├── src
└── tests
```

---

# Data Source

Data was retrieved from:

- TMDb Movie Details Endpoint
- TMDb Movie Credits Endpoint

Source:

https://developer.themoviedb.org/docs

The supplied candidate list consisted of TMDb movie identifiers.

---

# Environment Setup

## Create Virtual Environment

```powershell
python -m venv .venv
```

Activate:

```powershell
.venv\Scripts\Activate.ps1
```

---

## Install Dependencies

```powershell
pip install -r requirements.txt
```
---

# First-Time Execution

The first run requires data acquisition from TMDb.

Execute:

```powershell
python src/acquire_data.py
```

This step:

- Reads the candidate list
- Retrieves movie metadata
- Retrieves movie credits
- Stores raw JSON responses
- Generates a reconciliation report

Outputs:

```text
data/raw/details/
data/raw/credits/
data/processed/reconciliation.csv
```

---

# Running the Analysis Pipeline

After acquisition has completed, execute:

```powershell
python src/pipeline.py
```

The pipeline performs:

1. Movie transformation
2. Director extraction
3. Actor extraction
4. Analytical processing

without making additional API requests.

Outputs are written to:

```text
data/processed/
outputs/
```

---

# Alternative Manual Execution

Run each step separately:

## Transform Raw Data

```powershell
python src/transform_data.py
```

## Extract Directors

```powershell
python src/extract_directors.py
```

## Extract Actors

```powershell
python src/extract_actors.py
```

## Run Analysis

```powershell
python src/run_analysis.py
```

---

# Validation

## Data Validation

```powershell
python src/validation_checks.py
```

Checks:

- Movie coverage
- Director coverage
- Actor coverage
- Reconciliation consistency

---

## Pipeline Testing

```powershell
python src/test_pipeline.py
```

Tests:

- Unique movie IDs
- Join consistency
- No movie loss during transformation
- Reconciliation integrity
- Metric generation

---

# Key Business Rules

## Franchise Classification

A title is classified as a franchise film when:

```text
belongs_to_collection != null
```

A title is classified as standalone when:

```text
belongs_to_collection == null
```

---

## Franchise Shortlist Threshold

Only collections containing at least three analyzed titles are eligible for franchise recommendations.

This reduces the influence of single-film outliers.

---

## Lead Actor Definition

The lead actor is defined as the first billed cast member returned by the TMDb credits endpoint.

---

## Talent Reliability Threshold

Directors and actors must appear in at least two analyzed films before being considered a talent signal.

---

# Outputs

Generated analysis outputs are stored in:

```text
outputs/
```

Including:

- franchise_rankings.csv
- standalone_rankings.csv
- director_signals.csv
- actor_signals.csv
- franchise_vs_standalone.csv
- franchise_vs_standalone_2000.csv
- reconciliation_summary.csv

---

# Validation

The workflow includes:

- Candidate-list validation
- Identifier validation
- Duplicate detection
- Reconciliation reporting
- Join validation
- Sensitivity testing

This ensures that recommendations can be traced back to supporting evidence.

---

# Key Findings

The analysis found that:

- Franchise films outperformed standalone films on revenue, profit, and ROI.
- The recommendation remained stable under both all-years and 2000-onward analyses.
- The recommendation remained stable under median-based sensitivity testing.
- The Avengers Collection emerged as the strongest franchise candidate.
- Harry Potter and The Lord of the Rings represented additional high-confidence franchise opportunities.

Detailed findings are available in:

```text
docs/findings.md
```

---

# Deliverables

The submission includes:

- Client Memo
- Working Analysis
- Data Diagnosis
- Decision Notes
- Improvement Beyond the Brief
- Supporting Outputs
- Source Code
- Architecture Decision Records (ADRs)

---

# Reproducibility

The analysis was designed to be rerun on future candidate lists with minimal modification.

Raw acquisition data is separated from transformed datasets, enabling reprocessing without repeating API requests.

All major assumptions and decisions are documented within ADRs and Decision Notes.
