from datetime import datetime


def calculate_summary(predictions, anomaly_scores):
    """
    Calculate executive dashboard metrics.

    Args:
        predictions:
            1  -> Normal
            -1 -> Anomaly

        anomaly_scores:
            Isolation Forest anomaly scores.

    Returns:
        dict: Dashboard summary metrics.
    """

    # ==================================================
    # BASIC METRICS
    # ==================================================

    total_flows = len(predictions)

    threats_detected = sum(
        1
        for prediction in predictions
        if prediction == -1
    )

    normal_flows = total_flows - threats_detected

    threat_rate = (
        (threats_detected / total_flows) * 100
        if total_flows > 0
        else 0
    )

    # ==================================================
    # SEVERITY CALCULATION
    # Same thresholds used in threat_details.py
    # ==================================================

    critical = 0
    high = 0
    medium = 0
    low = 0

    for prediction, score in zip(
        predictions,
        anomaly_scores
    ):

        # Only anomalous flows are considered threats
        if prediction != -1:
            continue

        if score < -0.5:
            critical += 1

        elif score < -0.3:
            high += 1

        elif score < -0.1:
            medium += 1

        else:
            low += 1

    # ==================================================
    # AVERAGE ANOMALY SCORE
    # ==================================================

    average_anomaly_score = (
        sum(anomaly_scores) / len(anomaly_scores)
        if len(anomaly_scores) > 0
        else 0
    )

    # ==================================================
    # SYSTEM STATUS
    # ==================================================

    if critical > 0:
        system_status = "🔴 Critical"

    elif high > 0:
        system_status = "🟠 High Risk"

    elif threat_rate < 2:
        system_status = "🟢 Secure"

    elif threat_rate < 10:
        system_status = "🟡 Warning"

    else:
        system_status = "🔴 Critical"

    # ==================================================
    # LAST SCAN
    # ==================================================

    last_scan = datetime.now().strftime(
        "%d %b %Y %I:%M %p"
    )

    # ==================================================
    # RETURN SUMMARY
    # ==================================================

    return {
        "system_status": system_status,

        "total_flows": total_flows,

        "normal_flows": normal_flows,

        "threats_detected": threats_detected,

        "critical": critical,

        "high_risk": high,

        "medium": medium,

        "low": low,

        "threat_rate": round(
            threat_rate,
            2
        ),

        "average_anomaly_score": round(
            average_anomaly_score,
            4
        ),

        "last_scan": last_scan,
    }