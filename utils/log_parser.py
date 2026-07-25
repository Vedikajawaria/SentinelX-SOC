import pandas as pd


def load_logs(file_path):
    """
    Load security logs from CSV.
    """
    return pd.read_csv(file_path)


def clean_logs(df):
    """
    Clean the security logs.
    """
    df = df.drop_duplicates()
    df = df.dropna()

    return df


def failed_login_count(df):
    """
    Count failed login attempts.
    """
    if "status" in df.columns:
        return len(df[df["status"] == "Failed"])
    return 0


def create_features(df):
    """
    Create simple engineered features for the dashboard.
    """

    # Is Login Event
    if "event" in df.columns:
        df["is_login"] = df["event"].str.contains("login", case=False, na=False).astype(int)

    # Failed Login
    if "status" in df.columns:
        df["is_failed"] = (df["status"] == "Failed").astype(int)

    # Hour of Event (only if timestamp exists)
    if "timestamp" in df.columns:
        df["timestamp"] = pd.to_datetime(df["timestamp"])
        df["hour"] = df["timestamp"].dt.hour

    return df