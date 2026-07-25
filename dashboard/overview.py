import streamlit as st


def show_overview(total_logs, successful, failed, unique_users):
    """
    Display KPI cards.
    """

    st.subheader("📊 SOC Overview")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("📄 Total Logs", total_logs)
    c2.metric("✅ Successful", successful)
    c3.metric("❌ Failed", failed)
    c4.metric("👤 Users", unique_users)