import streamlit as st


def show_prediction(predictions, anomaly_scores):
    st.subheader("🤖 AI Threat Detection")

    prediction = predictions[0]
    anomaly_score = round(anomaly_scores[0], 4)

    # Isolation Forest:
    # 1  -> Normal
    # -1 -> Anomaly

    if prediction == 1:
        st.success("✅ Network Traffic is Benign")
        prediction_text = "Benign"
    else:
        st.error("🚨 Threat Detected!")
        prediction_text = "Threat"

    c1, c2 = st.columns(2)

    c1.metric("Prediction", prediction_text)
    c2.metric("Anomaly Score", anomaly_score)