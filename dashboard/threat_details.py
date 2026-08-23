import streamlit as st
import pandas as pd


def get_severity(score):
    """
    Convert anomaly score into a severity level.
    """

    if score < -0.5:
        return "Critical"

    elif score < -0.3:
        return "High"

    elif score < -0.1:
        return "Medium"

    else:
        return "Low"


def show_prediction(predictions, anomaly_scores, df):
    """
    Display AI anomaly detection results,
    severity distribution, filtering and
    threat investigation.
    """

    st.subheader("🤖 AI Threat Detection")

    # ==================================================
    # 1. BASIC STATISTICS
    # ==================================================

    total_flows = len(predictions)

    threats = sum(
        1
        for prediction in predictions
        if prediction == -1
    )

    threat_rate = (
        (threats / total_flows) * 100
        if total_flows > 0
        else 0
    )

    # ==================================================
    # 2. OVERALL STATUS
    # ==================================================

    if threats == 0:

        st.success(
            "✅ No Anomalous Network Traffic Detected"
        )

    else:

        st.error(
            f"🚨 {threats:,} Anomalous Network Flows Detected"
        )

    # ==================================================
    # 3. SUMMARY METRICS
    # ==================================================

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

    # ==================================================
    # 4. FIND ANOMALOUS FLOWS
    # ==================================================

    threat_indices = [
        i
        for i, prediction in enumerate(predictions)
        if prediction == -1
    ]

    if not threat_indices:

        st.info(
            "No anomalous flows detected."
        )

        return

    # ==================================================
    # 5. SORT ANOMALIES
    # ==================================================

    # Lower score = more anomalous

    threat_indices = sorted(
        threat_indices,
        key=lambda i: anomaly_scores[i]
    )

    # ==================================================
    # 6. SEVERITY DISTRIBUTION
    # ==================================================

    st.markdown(
        "### 🚨 Threat Severity Distribution"
    )

    critical = 0
    high = 0
    medium = 0
    low = 0

    for i in threat_indices:

        severity = get_severity(
            anomaly_scores[i]
        )

        if severity == "Critical":
            critical += 1

        elif severity == "High":
            high += 1

        elif severity == "Medium":
            medium += 1

        else:
            low += 1

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "🔴 Critical",
        f"{critical:,}"
    )

    c2.metric(
        "🟠 High",
        f"{high:,}"
    )

    c3.metric(
        "🟡 Medium",
        f"{medium:,}"
    )

    c4.metric(
        "🟢 Low",
        f"{low:,}"
    )

    # ==================================================
    # 7. ALERT FILTER
    # ==================================================

    st.markdown(
        "### 🔎 Filter Alerts"
    )

    selected_severity = st.selectbox(
        "Select severity:",
        [
            "All",
            "Critical",
            "High",
            "Medium",
            "Low"
        ]
    )

    # ==================================================
    # 8. FILTER FLOWS
    # ==================================================

    filtered_threats = []

    for i in threat_indices:

        score = anomaly_scores[i]

        severity = get_severity(score)

        if (
            selected_severity == "All"
            or severity == selected_severity
        ):

            filtered_threats.append(i)

    # ==================================================
    # 9. FILTER RESULT
    # ==================================================

    st.write(
        f"Showing **{len(filtered_threats):,}** "
        f"matching anomalous flows."
    )

    if not filtered_threats:

        st.warning(
            "No anomalous flows match this severity."
        )

        return

    # ==================================================
    # 10. CREATE SOC ALERT TABLE
    # ==================================================

    top_filtered = filtered_threats[:10]

    alert_data = []

    for i in top_filtered:

        flow = df.iloc[i]

        score = anomaly_scores[i]

        severity = get_severity(score)

        alert_data.append(
            {
                "Flow": i + 1,

                "Protocol": flow["Protocol"],

                "Flow Duration": round(
                    flow["Flow Duration"],
                    2
                ),

                "Fwd Packets": flow[
                    "Total Fwd Packets"
                ],

                "Bwd Packets": flow[
                    "Total Backward Packets"
                ],

                "Flow Bytes/s": round(
                    flow["Flow Bytes/s"],
                    2
                ),

                "Flow Packets/s": round(
                    flow["Flow Packets/s"],
                    2
                ),

                "Anomaly Score": round(
                    score,
                    4
                ),

                "Severity": severity
            }
        )

    alert_df = pd.DataFrame(
        alert_data
    )

    # ==================================================
    # 11. DISPLAY ALERT TABLE
    # ==================================================

    st.markdown(
        "### 🚨 Detected Threat Flows"
    )

    st.dataframe(
        alert_df,
        use_container_width=True,
        hide_index=True
    )

    # ==================================================
    # 12. THREAT INVESTIGATION
    # ==================================================

    st.markdown(
        "### 🔍 Threat Investigation"
    )

    selected_flow = st.selectbox(
        "Select a flow to investigate:",
        top_filtered,
        format_func=lambda i:
            (
                f"Flow {i + 1} "
                f"| Score: "
                f"{anomaly_scores[i]:.4f} "
                f"| "
                f"{get_severity(anomaly_scores[i])}"
            )
    )

    # ==================================================
    # 13. SELECTED FLOW INFORMATION
    # ==================================================

    score = anomaly_scores[selected_flow]

    severity = get_severity(score)

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

    # ==================================================
    # 14. NETWORK FLOW DETAILS
    # ==================================================

    st.markdown(
        "### 📡 Network Flow Details"
    )

    flow = df.iloc[selected_flow]

    flow_details = flow.to_frame(
        name="Value"
    )

    st.dataframe(
        flow_details,
        use_container_width=True
    )

    # ==================================================
    # 15. AI ASSESSMENT
    # ==================================================

    st.markdown(
        "### 🧠 AI Assessment"
    )

    st.info(
        "The Isolation Forest model identified this "
        "network flow as anomalous because its behavior "
        "differs from the patterns learned from normal "
        "network traffic."
    )