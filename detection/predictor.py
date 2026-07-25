import joblib
import pandas as pd

from utils.preprocessing import (
    SELECTED_FEATURES,
    transform_features,
)

MODEL_PATH = "models/isolation_forest.pkl"
SCALER_PATH = "models/scaler.pkl"


class ThreatPredictor:
    def __init__(self):
        self.model = joblib.load(MODEL_PATH)
        self.scaler = joblib.load(SCALER_PATH)

    def predict(self, flow_data: dict):
        """
        Predict whether a network flow is normal or anomalous.

        Returns:
            dict
        """

        df = pd.DataFrame([flow_data])

        X = df[SELECTED_FEATURES]

        X_scaled = transform_features(X, self.scaler)

        prediction = self.model.predict(X_scaled)[0]

        score = self.model.decision_function(X_scaled)[0]

        if prediction == -1:
            label = "Anomaly"
        else:
            label = "Benign"

        return {
            "prediction": label,
            "anomaly_score": round(float(score), 4)
        }