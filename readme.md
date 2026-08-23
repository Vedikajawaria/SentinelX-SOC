# 🛡️ SentinelX

## AI-Powered SOC Detection & Response Platform

SentinelX is an AI-powered Security Operations Center (SOC) platform designed to analyze network traffic, detect anomalous behavior, classify threat severity, and provide an interactive interface for security investigation.

The platform uses **Machine Learning-based anomaly detection** with an **Isolation Forest** model and the **CICIDS2017 network traffic dataset** to identify suspicious network flows.

---

## Features

### 🤖 AI Threat Detection

- Isolation Forest-based anomaly detection
- Detects abnormal network traffic patterns
- Generates anomaly scores for every network flow
- Separates normal and anomalous traffic
- Identifies the most anomalous network flows

### 📊 Executive Security Dashboard

Provides a high-level overview of the analyzed network traffic:

- Total network flows
- Total detected anomalies
- Threat rate
- High-risk threats
- Normal flows
- System security status
- Average anomaly score
- Last scan timestamp

### 🚨 Threat Severity Classification

Anomalous flows are categorized according to their anomaly score:

| Severity | Anomaly Score |
|----------|---------------|
| 🔴 Critical | `< -0.5` |
| 🟠 High | `< -0.3` |
| 🟡 Medium | `< -0.1` |
| 🟢 Low | `>= -0.1` |

This provides analysts with a quick way to prioritize suspicious network activity.

### 🔎 Threat Filtering

Security analysts can filter detected anomalies based on severity:

- All
- Critical
- High
- Medium
- Low

The dashboard dynamically displays the number of matching anomalous flows.

### 🚨 Threat Investigation

SentinelX allows analysts to investigate individual suspicious flows.

For a selected flow, the platform displays:

- Prediction
- Anomaly score
- Severity
- Network-flow features
- AI assessment

### 📡 Network Flow Analysis

Individual network flows can be inspected using important CICIDS2017 features such as:

- Protocol
- Flow Duration
- Total Forward Packets
- Total Backward Packets
- Flow Bytes/s
- Flow Packets/s
- Forward Packet Length
- Backward Packet Length
- Flow IAT
- Active/Idle statistics

### 📊 Network Traffic Analytics

SentinelX provides visual analytics for:

- 🌐 Protocol distribution
- 📈 Traffic rate
- 📦 Packet distribution
- ⏱️ Flow duration

These visualizations help analysts understand network traffic behavior.

### 🧠 Attack Analytics

The platform also uses the `Label` column from CICIDS2017 to display dataset-provided traffic classifications.

It provides:

- Traffic classification
- Benign vs attack traffic
- Dataset attack rate
- Attack distribution
- Attack classification table

> **Important:** CICIDS2017 labels represent the ground-truth labels provided by the dataset. They are separate from the Isolation Forest anomaly predictions.

---

# 🏗️ System Architecture

```text
                  ┌─────────────────────┐
                  │   Network Dataset   │
                  │     CICIDS2017      │
                  └──────────┬──────────┘
                             │
                             ▼
                  ┌─────────────────────┐
                  │ Data Preprocessing  │
                  │                     │
                  │ Feature Selection   │
                  │ Data Cleaning       │
                  │ Standard Scaling    │
                  └──────────┬──────────┘
                             │
                             ▼
                  ┌─────────────────────┐
                  │   Isolation Forest  │
                  │    ML Detection     │
                  └──────────┬──────────┘
                             │
                             ▼
                  ┌─────────────────────┐
                  │ Anomaly Prediction  │
                  │                     │
                  │  1  → Normal        │
                  │ -1  → Anomaly       │
                  └──────────┬──────────┘
                             │
                             ▼
                  ┌─────────────────────┐
                  │ Severity Analysis   │
                  │                     │
                  │ Critical / High     │
                  │ Medium / Low        │
                  └──────────┬──────────┘
                             │
                             ▼
              ┌──────────────────────────────┐
              │      Streamlit SOC UI        │
              │                              │
              │ Executive Summary            │
              │ Threat Detection             │
              │ Alert Filtering              │
              │ Threat Investigation         │
              │ Traffic Analytics            │
              │ Attack Analytics             │
              └──────────────────────────────┘
