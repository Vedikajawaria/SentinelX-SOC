import streamlit as st
import pandas as pd


def upload_dataset():

    st.sidebar.header("📂 Upload Dataset")

    uploaded = st.sidebar.file_uploader(
        "Choose a CSV or Parquet file",
        type=["csv", "parquet"]
    )

    if uploaded is None:
        return None

    if uploaded.name.endswith(".csv"):
        df = pd.read_csv(uploaded)
    else:
        df = pd.read_parquet(uploaded)

    st.sidebar.success("Dataset Loaded Successfully!")

    return df