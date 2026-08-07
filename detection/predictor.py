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

    def predict(self, flow_df: pd.DataFrame):
        """
        Predict anomalies for one or more network flows.

        Args:
            flow_df (pd.DataFrame):
                DataFrame containing network flow features.

        Returns:
            tuple:
                predictions (list)
                anomaly_scores (list)
        """

        X = flow_df[SELECTED_FEATURES]

        X_scaled = transform_features(X, self.scaler)

        predictions = self.model.predict(X_scaled)

        anomaly_scores = self.model.decision_function(X_scaled)

        return (
            predictions.tolist(),
            anomaly_scores.tolist(),
        )