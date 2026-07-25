import streamlit as st


def show_prediction(result):
    st.subheader("🤖 AI Threat Detection")

    if result["prediction"] == "Benign":
        st.success("✅ Network Traffic is Benign")
    else:
        st.error("🚨 Threat Detected!")

    c1, c2 = st.columns(2)

    c1.metric("Prediction", result["prediction"])
    c2.metric("Anomaly Score", result["anomaly_score"])