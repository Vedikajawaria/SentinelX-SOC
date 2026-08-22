import streamlit as st
import pandas as pd

from components.uploader import upload_dataset
from detection.predictor import ThreatPredictor

from dashboard.overview import show_overview
from dashboard.analytics import show_event_distribution
from dashboard.alerts import show_logs
from dashboard.threat_details import show_prediction

from utils.log_parser import (
    load_logs,
    clean_logs,
    create_features,
)

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="SentinelX",
    page_icon="🛡️",
    layout="wide"
)

# --------------------------------------------------
# Title
# --------------------------------------------------

st.title("🛡️ SentinelX")
st.subheader("AI-Powered SOC Detection & Response Platform")

st.divider()

# --------------------------------------------------
# Initialize AI Predictor
# --------------------------------------------------

predictor = ThreatPredictor()

# --------------------------------------------------
# Dataset Upload
# --------------------------------------------------

uploaded_df = upload_dataset()

from utils.preprocessing import load_dataset

CICIDS_PATH = "data/datasets/Portscan-Friday-no-metadata.parquet"

df = load_dataset(CICIDS_PATH)
predictions, anomaly_scores = predictor.predict(df)

# --------------------------------------------------
# Executive Summary
# --------------------------------------------------

show_overview(df, predictions, anomaly_scores)

st.divider()

# --------------------------------------------------
# Engineered Features
# --------------------------------------------------

st.subheader("📊 Engineered Features")
st.dataframe(df)

# --------------------------------------------------
# Event Analytics
# --------------------------------------------------

show_event_distribution(df)

st.divider()

# --------------------------------------------------
# Security Logs
# --------------------------------------------------

show_logs(df)

st.divider()

# --------------------------------------------------
# AI Threat Prediction
# --------------------------------------------------

show_prediction(predictions, anomaly_scores)