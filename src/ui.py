import streamlit as st
import pandas as pd

st.set_page_config(page_title="Clinical Data Studio Lite", layout="wide")

st.title("Clinical Data Studio Lite")
st.caption("AI-assisted clinical data review prototype inspired by Medidata CDS")

tab1, tab2, tab3 = st.tabs(["Overview", "Data Review", "Architecture"])

with tab1:
    st.subheader("Upload and review a clinical dataset")
    uploaded_file = st.file_uploader("Upload Clinical Data (CSV)", type=["csv"])

    if uploaded_file:
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_csv("data/sample_clinical_data.csv")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Rows", len(df))
    col2.metric("Columns", len(df.columns))
    col3.metric("Missing Values", int(df.isna().sum().sum()))
    col4.metric("Flagged Rows", int(df.isna().any(axis=1).sum()))

    st.markdown("### Dataset preview")
    st.dataframe(df, use_container_width=True)

with tab2:
    st.subheader("Flagged records")
    flagged = df[df.isna().any(axis=1)].copy()

    if len(flagged) == 0:
        st.success("No flagged records found.")
    else:
        flagged["issue"] = "Missing value detected"
        st.dataframe(flagged, use_container_width=True)

    st.markdown("### Missing values by column")
    missing = df.isna().sum()
    st.bar_chart(missing)

with tab3:
    st.subheader("System architecture")
    st.markdown("""
**Conceptual flow**

Clinical Data Sources  
→ Ingestion Layer  
→ Standardization Layer  
→ Validation Layer  
→ Review & Monitoring UI

**Future architecture direction**
- Streaming ingestion
- Rule-based anomaly detection
- Patient-level review
- Audit trail
- AI-assisted explanations
""")
