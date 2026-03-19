# clinical-data-studio-lite
AI-assisted clinical data platform prototype (CDS-inspired)

## Overview
This project is a lightweight prototype of a clinical data review platform. It simulates how fragmented datasets from multiple sources can be uploaded, reviewed, and monitored in a simple product interface.

## What this demonstrates
- Product thinking for a clinical data platform
- A simple UX for data upload and review
- Basic data quality monitoring
- A foundation for future anomaly detection and validation workflows

## Current features
- Upload a CSV file
- Preview the dataset
- View row, column, and missing-value metrics
- Review rows with missing data

## Tech stack
- Python
- Streamlit
- Pandas

## How to run
```bash
pip install -r requirements.txt
streamlit run src/ui.py
Why I built this

Clinical trial data is often fragmented across systems and vendors, which creates review delays, manual reconciliation work, and quality risks. This prototype shows how a unified review layer can simplify that workflow.

Author

Ishan
