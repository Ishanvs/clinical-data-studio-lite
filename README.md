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

## 🛠 Tech Stack
- Python  
- Streamlit  
- Pandas  

---

## 🚀 How to Run

```bash
pip install -r requirements.txt
streamlit run src/ui.py
