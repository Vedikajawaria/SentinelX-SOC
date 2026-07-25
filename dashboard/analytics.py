import streamlit as st


def show_event_distribution(df):
    st.subheader("📊 Event Distribution")

    event_counts = df["event"].value_counts()

    st.bar_chart(event_counts)