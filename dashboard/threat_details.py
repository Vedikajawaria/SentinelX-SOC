import streamlit as st


def show_prediction(predictions, anomaly_scores, df):
    """
    Display the most anomalous network flows.
    """

    st.subheader("🤖 AI Threat Detection")

    # --------------------------------------------------
    # Basic statistics
    # --------------------------------------------------

    total_flows = len(predictions)

    threats = sum(
        1 for prediction in predictions
        if prediction == -1
    )

    threat_rate = (
        (threats / total_flows) * 100
        if total_flows > 0
        else 0
    )

    # --------------------------------------------------
    # Overall status
    # --------------------------------------------------

    if threats == 0:
        st.success("✅ No Anomalous Network Traffic Detected")
    else:
        st.error(
            f"🚨 {threats:,} Anomalous Network Flows Detected"
        )

    # --------------------------------------------------
    # Metrics
    # --------------------------------------------------

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "🌐 Total Flows",
        f"{total_flows:,}"
    )

    c2.metric(
        "🚨 Anomalies",
        f"{threats:,}"
    )

    c3.metric(
        "📈 Threat Rate",
        f"{threat_rate:.2f}%"
    )

    # --------------------------------------------------
    # Find anomalous flows
    # --------------------------------------------------

    threat_indices = [
        i
        for i, prediction in enumerate(predictions)
        if prediction == -1
    ]

    if not threat_indices:
        st.info("No anomalous flows detected.")
        return

    # --------------------------------------------------
    # Sort anomalies
    # Lowest score = most anomalous
    # --------------------------------------------------

    threat_indices = sorted(
        threat_indices,
        key=lambda i: anomaly_scores[i]
    )

    # Show only top 10
    top_threats = threat_indices[:10]

    # --------------------------------------------------
    # Create threat table
    # --------------------------------------------------

    threat_data = []

    for i in top_threats:

        score = anomaly_scores[i]

        if score < -0.5:
            severity = "🔴 Critical"
        elif score < -0.3:
            severity = "🟠 High"
        elif score < -0.1:
            severity = "🟡 Medium"
        else:
            severity = "🟢 Low"

        threat_data.append({
            "Flow": i + 1,
            "Anomaly Score": round(score, 4),
            "Severity": severity
        })

    # --------------------------------------------------
    # Display top threats
    # --------------------------------------------------

    st.markdown("### 🚨 Top 10 Most Anomalous Flows")

    st.dataframe(
        threat_data,
        use_container_width=True,
        hide_index=True
    )

    # --------------------------------------------------
    # Threat investigation
    # --------------------------------------------------

    st.markdown("### 🔍 Investigate a Threat")

    selected_flow = st.selectbox(
        "Select a flow to investigate:",
        top_threats,
        format_func=lambda i: f"Flow {i + 1}"
    )

    score = anomaly_scores[selected_flow]

    if score < -0.5:
        severity = "🔴 Critical"
    elif score < -0.3:
        severity = "🟠 High"
    elif score < -0.1:
        severity = "🟡 Medium"
    else:
        severity = "🟢 Low"

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Prediction",
        "Anomaly"
    )

    c2.metric(
        "Anomaly Score",
        f"{score:.4f}"
    )

    c3.metric(
        "Severity",
        severity
    )

    # --------------------------------------------------
    # Network flow details
    # --------------------------------------------------

    st.markdown("### 📡 Network Flow Details")

    flow = df.iloc[selected_flow]

    st.dataframe(
        flow.to_frame("Value"),
        use_container_width=True
    )