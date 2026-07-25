from sklearn.ensemble import IsolationForest
import joblib


def build_model():

    model = IsolationForest(
        contamination=0.02,
        random_state=42
    )

    return model


def save_model(model, path):

    joblib.dump(model, path)


def load_model(path):

    return joblib.load(path)