import streamlit as st
import pandas as pd


def show_event_distribution(df):
    """
    Display Network Traffic Analytics and
    CICIDS2017 Attack Analytics.
    """

    # ==================================================
    # NETWORK TRAFFIC ANALYTICS
    # ==================================================

    st.subheader("📊 Network Traffic Analytics")

    if df is None or df.empty:
        st.warning("No network traffic data available.")
        return

    # ==================================================
    # 1. PROTOCOL DISTRIBUTION
    # ==================================================

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("### 🌐 Protocol Distribution")

        if "Protocol" in df.columns:

            protocol_counts = (
                df["Protocol"]
                .value_counts()
                .reset_index()
            )

            protocol_counts.columns = [
                "Protocol",
                "Flows"
            ]

            st.bar_chart(
                protocol_counts.set_index("Protocol")
            )

        else:

            st.warning(
                "Protocol column not available."
            )

    # ==================================================
    # 2. TRAFFIC RATE
    # ==================================================

    with col2:

        st.markdown("### 📈 Traffic Rate")

        if "Flow Bytes/s" in df.columns:

            traffic_data = df[
                ["Flow Bytes/s"]
            ].copy()

            traffic_data = (
                traffic_data
                .replace(
                    [float("inf"), -float("inf")],
                    pd.NA
                )
                .dropna()
            )

            if not traffic_data.empty:

                traffic_data = (
                    traffic_data
                    .sort_values(
                        "Flow Bytes/s"
                    )
                    .reset_index(drop=True)
                )

                traffic_data = traffic_data.head(100)

                traffic_data.index.name = "Flow"

                st.line_chart(
                    traffic_data
                )

            else:

                st.info(
                    "No valid traffic-rate data."
                )

        else:

            st.warning(
                "Flow Bytes/s column not available."
            )

    # ==================================================
    # 3. PACKET DISTRIBUTION
    # ==================================================

    st.markdown("### 📦 Packet Distribution")

    packet_columns = [
        "Total Fwd Packets",
        "Total Backward Packets"
    ]

    available_packet_columns = [
        column
        for column in packet_columns
        if column in df.columns
    ]

    if available_packet_columns:

        packet_data = df[
            available_packet_columns
        ].copy()

        packet_data = (
            packet_data
            .replace(
                [float("inf"), -float("inf")],
                pd.NA
            )
            .dropna()
        )

        packet_data = packet_data.head(100)

        st.line_chart(
            packet_data
        )

    else:

        st.warning(
            "Packet information is not available."
        )

    # ==================================================
    # 4. FLOW DURATION
    # ==================================================

    st.markdown("### ⏱️ Flow Duration")

    if "Flow Duration" in df.columns:

        duration_data = df[
            ["Flow Duration"]
        ].copy()

        duration_data = (
            duration_data
            .replace(
                [float("inf"), -float("inf")],
                pd.NA
            )
            .dropna()
        )

        duration_data = duration_data.head(100)

        st.area_chart(
            duration_data
        )

    else:

        st.warning(
            "Flow Duration column not available."
        )

    # ==================================================
    # ATTACK ANALYTICS
    # ==================================================

    st.divider()

    st.subheader("🧠 Attack Analytics")

    # --------------------------------------------------
    # Check for CICIDS Label column
    # --------------------------------------------------

    if "Label" not in df.columns:

        st.info(
            "Attack analytics require a CICIDS2017 "
            "'Label' column."
        )

        return

    # --------------------------------------------------
    # Clean labels
    # --------------------------------------------------

    labels = (
        df["Label"]
        .astype(str)
        .str.strip()
    )

    label_counts = (
        labels
        .value_counts()
        .reset_index()
    )

    label_counts.columns = [
        "Traffic Type",
        "Flows"
    ]

    # ==================================================
    # 5. TRAFFIC CLASSIFICATION
    # ==================================================

    col1, col2 = st.columns(2)

    with col1:

        st.markdown(
            "### 🏷️ Traffic Classification"
        )

        st.bar_chart(
            label_counts.set_index(
                "Traffic Type"
            )
        )

    # ==================================================
    # 6. BENIGN VS ATTACK
    # ==================================================

    with col2:

        st.markdown(
            "### 🛡️ Benign vs Attack Traffic"
        )

        benign_mask = (
            labels.str.upper() == "BENIGN"
        )

        benign_count = int(
            benign_mask.sum()
        )

        attack_count = int(
            (~benign_mask).sum()
        )

        traffic_summary = pd.DataFrame(
            {
                "Flows": [
                    benign_count,
                    attack_count
                ]
            },
            index=[
                "Benign",
                "Attack"
            ]
        )

        st.bar_chart(
            traffic_summary
        )

    # ==================================================
    # 7. ATTACK SUMMARY METRICS
    # ==================================================

    total = len(labels)

    attack_rate = (
        (attack_count / total) * 100
        if total > 0
        else 0
    )

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "📊 Total Classified Flows",
        f"{total:,}"
    )

    c2.metric(
        "🚨 Dataset-Labeled Attacks",
        f"{attack_count:,}"
    )

    c3.metric(
        "📈 Dataset Attack Rate",
        f"{attack_rate:.2f}%"
    )

    # ==================================================
    # 8. ATTACK DISTRIBUTION TABLE
    # ==================================================

    st.markdown(
        "### 📋 Attack Distribution"
    )

    st.dataframe(
        label_counts,
        use_container_width=True,
        hide_index=True
    )

    # ==================================================
    # 9. IMPORTANT CONTEXT
    # ==================================================

    st.info(
        "ℹ️ The traffic labels shown above are the "
        "ground-truth labels provided by the CICIDS2017 "
        "dataset. They are separate from the Isolation "
        "Forest anomaly predictions."
    )