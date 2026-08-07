import streamlit as st
import plotly.express as px


def show_event_distribution(df):

    st.subheader("📊 Network Traffic Analytics")

    # -----------------------------
    # Event Distribution
    # -----------------------------
    if "event" in df.columns:
        event_counts = (
            df["event"]
            .value_counts()
            .reset_index()
        )

        event_counts.columns = ["Event", "Count"]

        fig = px.bar(
            event_counts,
            x="Event",
            y="Count",
            title="Network Events",
            text_auto=True,
        )

        st.plotly_chart(fig, use_container_width=True)

    # -----------------------------
    # Login Success vs Failed
    # -----------------------------
    if "status" in df.columns:

        status_counts = (
            df["status"]
            .value_counts()
            .reset_index()
        )

        status_counts.columns = ["Status", "Count"]

        fig2 = px.pie(
            status_counts,
            values="Count",
            names="Status",
            title="Login Status Distribution"
        )

        st.plotly_chart(fig2, use_container_width=True)

    # -----------------------------
    # Activity by Hour
    # -----------------------------
    if "hour" in df.columns:

        hourly = (
            df["hour"]
            .value_counts()
            .sort_index()
            .reset_index()
        )

        hourly.columns = ["Hour", "Events"]

        fig3 = px.line(
            hourly,
            x="Hour",
            y="Events",
            markers=True,
            title="Activity Timeline"
        )

        st.plotly_chart(fig3, use_container_width=True)