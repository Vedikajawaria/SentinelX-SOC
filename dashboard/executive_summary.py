from datetime import datetime


def calculate_summary(predictions, anomaly_scores):
    """
    Calculate executive dashboard metrics.

    Args:
        predictions (list or array):
            Model predictions
            1  -> Normal
            -1 -> Anomaly

        anomaly_scores (list or array):
            Isolation Forest anomaly scores.

    Returns:
        dict: Dashboard summary metrics.
    """

    # -------------------------------
    # Basic Metrics
    # -------------------------------
    total_flows = len(predictions)

    threats_detected = sum(
        1 for prediction in predictions
        if prediction == -1
    )

    normal_flows = total_flows - threats_detected

    threat_rate = (
        (threats_detected / total_flows) * 100
        if total_flows > 0
        else 0
    )

    # -------------------------------
    # High Risk Threats
    # Very negative scores indicate
    # stronger anomalies.
    # -------------------------------
    HIGH_RISK_THRESHOLD = -0.8

    high_risk = sum(
        1 for score in anomaly_scores
        if score < HIGH_RISK_THRESHOLD
    )

    # -------------------------------
    # Average Anomaly Score
    # (Not AI Confidence)
    # -------------------------------
    average_anomaly_score = (
        sum(anomaly_scores) / len(anomaly_scores)
        if len(anomaly_scores) > 0
        else 0
    )

    # -------------------------------
    # System Status
    # -------------------------------
    if threat_rate < 2:
        system_status = "🟢 Secure"

    elif threat_rate < 10:
        system_status = "🟡 Warning"

    else:
        system_status = "🔴 Critical"

    # -------------------------------
    # Last Scan Time
    # -------------------------------
    last_scan = datetime.now().strftime("%d %b %Y %I:%M %p")

    # -------------------------------
    # Return Summary
    # -------------------------------
    return {
        "system_status": system_status,
        "total_flows": total_flows,
        "normal_flows": normal_flows,
        "threats_detected": threats_detected,
        "high_risk": high_risk,
        "threat_rate": round(threat_rate, 2),
        "average_anomaly_score": round(average_anomaly_score, 4),
        "last_scan": last_scan,
    }