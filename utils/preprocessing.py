import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler


SELECTED_FEATURES = [
    "Protocol",
    "Flow Duration",
    "Total Fwd Packets",
    "Total Backward Packets",
    "Flow Bytes/s",
    "Flow Packets/s",
    "Fwd Packet Length Mean",
    "Bwd Packet Length Mean",
    "Flow IAT Mean",
    "Flow IAT Std",
    "Active Mean",
    "Idle Mean"
]


def load_dataset(file_path):
    """
    Load dataset from parquet file.
    """
    return pd.read_parquet(file_path)


def select_features(df):
    """
    Select important columns.
    """
    return df[SELECTED_FEATURES]


def fit_scaler(X):
    """
    Train StandardScaler.
    """
    scaler = StandardScaler()

    X_scaled = scaler.fit_transform(X)

    return X_scaled, scaler


def transform_features(X, scaler):
    """
    Scale new incoming data.
    """
    return scaler.transform(X)


def save_scaler(scaler, path):
    joblib.dump(scaler, path)


def load_scaler(path):
    return joblib.load(path)