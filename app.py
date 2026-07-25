import streamlit as st
import pandas as pd

from detection.predictor import ThreatPredictor

from dashboard.overview import show_overview
from dashboard.analytics import show_event_distribution
from dashboard.alerts import show_logs
from dashboard.threat_details import show_prediction

from utils.log_parser import (
    load_logs,
    clean_logs,
    create_features
)

# --------------------------
# Page Config
# --------------------------
st.set_page_config(
    page_title="SentinelX",
    page_icon="🛡️",
    layout="wide"
)

# --------------------------
# Title
# --------------------------
st.title("🛡️ SentinelX")
st.subheader("AI-Powered SOC Detection & Response Platform")

st.divider()
predictor = ThreatPredictor()

# --------------------------
# Load Logs
# --------------------------
from utils.log_parser import load_logs, clean_logs
df = load_logs("data/raw_logs/sample_logs.csv")

df = clean_logs(df)
from utils.log_parser import create_features

df = create_features(df)
st.subheader("Engineered Features")

st.dataframe(df)

# --------------------------
# Statistics
# --------------------------
total_logs = len(df)
successful = len(df[df["status"] == "Success"])
failed = len(df[df["status"] == "Failed"])
unique_users = df["user"].nunique()

# --------------------------
from dashboard.overview import show_overview

show_overview(
    total_logs,
    successful,
    failed,
    unique_users
)
show_event_distribution(df)

st.divider()

# --------------------------
# Security Logs
# --------------------------
show_logs(df)
st.divider()

sample_flow = {
    "Protocol": 6,
    "Flow Duration": 50000,
    "Total Fwd Packets": 10,
    "Total Backward Packets": 8,
    "Flow Bytes/s": 1000,
    "Flow Packets/s": 20,
    "Fwd Packet Length Mean": 150,
    "Bwd Packet Length Mean": 120,
    "Flow IAT Mean": 1000,
    "Flow IAT Std": 250,
    "Active Mean": 300,
    "Idle Mean": 2000,
}

result = predictor.predict(sample_flow)

show_prediction(result)