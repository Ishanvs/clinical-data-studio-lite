# Clinical Data Studio Lite

AI-assisted clinical data review prototype inspired by Medidata Clinical Data Studio.

## Overview
Clinical Data Studio Lite is a lightweight portfolio project that simulates how fragmented clinical datasets can be uploaded, reviewed, and monitored in a unified product interface.

This project is designed to demonstrate:
- product thinking for a clinical data platform
- UX for data upload and review
- basic data quality monitoring
- a foundation for anomaly detection and validation workflows

## Problem
Clinical trial data is often fragmented across systems, sites, and vendors. This creates manual reconciliation work, slower review cycles, and higher quality risk.

## Current features
- Upload a CSV dataset
- Automatically fall back to sample data
- Preview the dataset in a simple interface
- View row, column, missing-value, and flagged-row metrics
- Review records with missing values
- View a conceptual architecture tab

## Repo structure
```text
clinical-data-studio-lite/
├── README.md
├── requirements.txt
├── src/
│   └── ui.py
├── data/
│   └── sample_clinical_data.csv
├── docs/
│   └── product-requirements.md
└── architecture/
    └── architecture-notes.md

Tech stack

Python

Streamlit

Pandas

How to run
pip install -r requirements.txt
streamlit run src/ui.py

A sample dataset is included in data/sample_clinical_data.csv.

Product framing

This prototype represents the early foundation of a clinical data platform:

ingestion and review

quality monitoring

issue identification

future AI-assisted workflows

Next enhancements

anomaly detection

patient profile view

validation rules

audit trail

explainable AI layer

Author

Ishan
