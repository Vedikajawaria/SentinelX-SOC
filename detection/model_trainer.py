from utils.preprocessing import (
    load_dataset,
    select_features,
    fit_scaler,
    save_scaler
)

from detection.anomaly_detector import (
    build_model,
    save_model
)


DATASET_PATH = "data/datasets/Portscan-Friday-no-metadata.parquet"

MODEL_PATH = "models/isolation_forest.pkl"

SCALER_PATH = "models/scaler.pkl"


print("Loading dataset...")

df = load_dataset(DATASET_PATH)

print("Selecting features...")

X = select_features(df)

print("Scaling data...")

X_scaled, scaler = fit_scaler(X)

print("Training Isolation Forest...")

model = build_model()

model.fit(X_scaled)

print("Saving model...")

save_model(model, MODEL_PATH)

save_scaler(scaler, SCALER_PATH)

print("===================================")
print("Model Trained Successfully!")
print("===================================")