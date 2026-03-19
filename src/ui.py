import streamlit as st
import pandas as pd

# -------------------------
# PAGE CONFIG
# -------------------------
st.set_page_config(page_title="Clinical Data Studio Lite", layout="wide")

# -------------------------
# HEADER
# -------------------------
st.title("Clinical Data Studio Lite")
st.caption("AI-assisted clinical data review prototype")

# -------------------------
# LOAD DATA
# -------------------------
uploaded_file = st.file_uploader("Upload Clinical Data (CSV)", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
else:
    df = pd.read_csv("data/sample_clinical_data.csv")

# -------------------------
# KPI SECTION
# -------------------------
st.subheader("📊 Key Metrics")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Rows", len(df))
col2.metric("Columns", len(df.columns))
col3.metric("Missing Values", int(df.isna().sum().sum()))
col4.metric("Flagged Rows", int(df.isna().any(axis=1).sum()))

st.markdown("---")

# -------------------------
# TABS (REAL PRODUCT FEEL)
# -------------------------
tab1, tab2, tab3 = st.tabs(["📁 Data Preview", "⚠️ Data Quality", "📈 Insights"])

# -------------------------
# TAB 1: DATA PREVIEW
# -------------------------
with tab1:
    st.subheader("Dataset Preview")
    st.dataframe(df, use_container_width=True)

# -------------------------
# TAB 2: DATA QUALITY
# -------------------------
with tab2:
    st.subheader("Flagged Records (Missing Values)")

    flagged = df[df.isna().any(axis=1)]

    if flagged.empty:
        st.success("No issues found 🎉")
    else:
        st.dataframe(flagged, use_container_width=True)

    st.markdown("### Missing Values by Column")
    missing = df.isna().sum()
    st.bar_chart(missing)

# -------------------------
# TAB 3: INSIGHTS
# -------------------------
with tab3:
    st.subheader("Basic Insights")

    if "status" in df.columns:
        st.markdown("### Status Distribution")
        st.bar_chart(df["status"].value_counts())

    if "lab_value" in df.columns:
        st.markdown("### Lab Value Distribution")
        st.line_chart(df["lab_value"].fillna(0))

# -------------------------
# FOOTER
# -------------------------
st.markdown("---")
st.caption("Prototype for clinical data quality & AI-ready workflows")
