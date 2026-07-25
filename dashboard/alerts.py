import streamlit as st


def show_logs(df):
    st.subheader("📋 Security Logs")

    st.dataframe(df, use_container_width=True)