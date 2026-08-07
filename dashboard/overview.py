import streamlit as st
from dashboard.executive_summary import calculate_summary


def show_overview(df, predictions, anomaly_scores):
    """
    Display the Executive Summary Dashboard.
    """

    summary = calculate_summary(predictions, anomaly_scores)

    st.subheader("📊 Executive Summary")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "🌐 Total Flows",
        summary["total_flows"]
    )

    c2.metric(
        "🚨 Threats",
        summary["threats_detected"]
    )

    c3.metric(
        "📈 Threat Rate",
        f'{summary["threat_rate"]}%'
    )

    c4.metric(
        "🔥 High Risk",
        summary["high_risk"]
    )

    st.divider()

    c5, c6, c7, c8 = st.columns(4)

    c5.metric(
        "🟢 Normal Flows",
        summary["normal_flows"]
    )

    c6.metric(
        "🛡️ System Status",
        summary["system_status"]
    )

    c7.metric(
        "📉 Avg Anomaly Score",
        summary["average_anomaly_score"]
    )

    c8.metric(
        "🕒 Last Scan",
        summary["last_scan"]
    )