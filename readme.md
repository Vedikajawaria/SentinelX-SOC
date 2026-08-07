# SentinelX - AI-Powered SOC Detection & Response Platform

## Overview

SentinelX is an AI-powered Security Operations Center (SOC) platform designed to detect, analyze, and visualize cyber threats using machine learning. It combines log analysis, anomaly detection, and an interactive Streamlit dashboard to help security analysts identify suspicious network activity and gain actionable security insights.

The platform automates the detection of malicious network behavior using an Isolation Forest model and presents the results through a modular dashboard with analytics and reporting capabilities.

---

## Problem Statement

Modern Security Operations Centers process massive volumes of network traffic logs every day. Manually identifying malicious behavior from these logs is time-consuming and error-prone. SentinelX addresses this challenge by leveraging machine learning to automate anomaly detection and provide security analysts with an intuitive dashboard for monitoring and investigating potential threats.

---

## Features

- AI-based network threat detection using Isolation Forest
- Interactive SOC dashboard built with Streamlit
- Executive security summary
- Threat analytics and visualization
- Live monitoring dashboard
- Threat intelligence module
- Security reporting
- Log upload and analysis
- Feature engineering and preprocessing pipeline

---

## Tech Stack

- Python
- Streamlit
- Scikit-learn
- Pandas
- NumPy
- Plotly
- Matplotlib
- Joblib
- Git
- GitHub

---

## Machine Learning Pipeline

- Dataset preprocessing and cleaning
- Feature engineering
- Feature scaling using StandardScaler
- Anomaly detection using Isolation Forest
- Threat classification
- Dashboard visualization and reporting

---

## Project Architecture

```
Network Traffic Logs
          │
          ▼
Data Preprocessing
          │
          ▼
Feature Engineering
          │
          ▼
Feature Scaling
          │
          ▼
Isolation Forest Model
          │
          ▼
Threat Prediction
          │
          ▼
Streamlit Dashboard
      ├── Executive Summary
      ├── Threat Analytics
      ├── Live Monitoring
      ├── Reports
      └── Threat Intelligence
```

---

## Project Structure

```
SentinelX-SOC
│
├── assets/
├── components/
├── dashboard/
├── data/
├── database/
├── detection/
├── notebooks/
├── tests/
├── threat_intelligence/
├── utils/
│
├── app.py
├── config.py
├── requirements.txt
├── README.md
└── LICENSE
```

---

## Workflow

1. Upload or load network traffic logs.
2. Clean and preprocess the raw data.
3. Generate features required for anomaly detection.
4. Scale features using the trained preprocessing pipeline.
5. Predict anomalous network flows using the Isolation Forest model.
6. Display predictions, analytics, and security insights through the Streamlit dashboard.

---

## Dashboard Modules

- Executive Summary
- Threat Analytics
- Live Monitoring
- Reports
- Threat Intelligence

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Vedikajawaria/SentinelX-SOC.git
```

Navigate to the project directory:

```bash
cd SentinelX-SOC
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## Future Improvements

- Real-time network traffic monitoring
- LLM-powered incident summarization
- SIEM integration
- Multiple machine learning models for threat detection
- Cloud deployment
- User authentication and role-based access control
- Automated alert notifications

---

## Author

Vedika Jawaria

Final-Year B.Tech (Artificial Intelligence & Machine Learning)

GitHub: https://github.com/Vedikajawaria
