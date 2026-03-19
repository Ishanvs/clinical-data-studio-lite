import streamlit as st
import pandas as pd

st.set_page_config(page_title="Clinical Data Studio Lite", layout="wide")

st.title("Clinical Data Studio Lite")
st.subheader("AI-Assisted Clinical Data Platform")

uploaded_file = st.file_uploader("Upload Clinical Data (CSV)")

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.markdown("## Data Preview")
    st.dataframe(df)

    col1, col2, col3 = st.columns(3)
    col1.metric("Rows", len(df))
    col2.metric("Columns", len(df.columns))
    col3.metric("Missing Values", int(df.isna().sum().sum()))

    st.markdown("## Flagged Issues")
    issues = df[df.isna().any(axis=1)]
    st.dataframe(issues)

else:
    st.info("Upload a CSV file to begin")
