# 🛡️ SentinelX - AI-Powered SOC Detection & Response Platform

SentinelX is an AI-powered Security Operations Center (SOC) platform designed to detect, analyze, and visualize cyber threats using Machine Learning.

The platform combines log analysis, threat detection, and an interactive Streamlit dashboard to help security analysts monitor suspicious activities and gain actionable insights.

---
## Problem Statement

Security Operations Centers (SOCs) generate massive volumes of network logs every day, making it difficult for analysts to identify malicious activities quickly. SentinelX leverages Machine Learning to automate threat detection and provide actionable insights through an interactive dashboard, enabling faster and more efficient security monitoring.

## Features

- Threat Detection using Machine Learning
- Interactive Streamlit Dashboard
- Executive Security Summary
- Threat Intelligence Dashboard
- Live Threat Monitoring
- Security Reports
- Log Upload & Analysis
- Threat Analytics & Visualization

---

## Tech Stack

- Python
- Streamlit
- Scikit-learn
- Pandas
- NumPy
- Plotly
- Matplotlib

---

## Project Structure

```
SentinelX-SOC
│
├── dashboard/
├── detection/
├── threat_intelligence/
├── components/
├── utils/
├── notebooks/
└── tests/
```

## Architecture

```text
              Network Traffic Logs
                      │
                      ▼
              Data Preprocessing
                      │
                      ▼
             Feature Engineering
                      │
                      ▼
      Isolation Forest Anomaly Detection
                      │
                      ▼
            Threat Classification
                      │
                      ▼
          Streamlit Dashboard (SOC)
         ├── Executive Summary
         ├── Threat Analytics
         ├── Reports
         ├── Live Monitoring
         └── Threat Intelligence

---

## ⚙️ Workflow

1. Upload security logs
2. Preprocess log data
3. Generate features
4. Predict malicious activity using ML
5. Display results in dashboard
6. Generate reports and analytics

---

## 📊 Dashboard Modules

- Executive Summary
- Threat Overview
- Live Monitoring
- Reports
- Threat Intelligence

## Screenshots

<img width="1917" height="843" alt="image" src="https://github.com/user-attachments/assets/e2e15535-7568-4ab2-8fdd-17b3b8a02bc1" />
<img width="1917" height="551" alt="image" src="https://github.com/user-attachments/assets/78d1c671-7c72-43cc-9053-e35be045ad99" />
<img width="1917" height="718" alt="image" src="https://github.com/user-attachments/assets/95673203-75c1-41c9-a6f3-85ef7544f217" />
<img width="1917" height="637" alt="image" src="https://github.com/user-attachments/assets/4698062f-9d1d-45c7-8e4d-2b59756fdcde" />
<img width="1917" height="618" alt="image" src="https://github.com/user-attachments/assets/fbefd3a8-4210-4d7f-8798-d0b9b39ba5e8" />
<img width="1917" height="580" alt="image" src="https://github.com/user-attachments/assets/e17d927c-d9f6-417b-82aa-f42d344a5ac5" />
<img width="1917" height="343" alt="image" src="https://github.com/user-attachments/assets/2b4167c7-1ebf-431b-8aa3-ddc66a3937a8" />


---

## 🛠 Future Improvements

- Real-time log streaming
- LLM-powered incident summaries
- SIEM integration
- Multi-model threat detection
- Cloud deployment
- Role-based authentication

---

## 👩‍💻 Author

Vedika Jawaria
