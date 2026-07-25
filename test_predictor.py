from detection.predictor import ThreatPredictor

predictor = ThreatPredictor()

sample_flow = {
    "Protocol": 6,
    "Flow Duration": 50000,
    "Total Fwd Packets": 10,
    "Total Backward Packets": 8,
    "Flow Bytes/s": 1000,
    "Flow Packets/s": 20,
    "Fwd Packet Length Mean": 150,
    "Bwd Packet Length Mean": 120,
    "Flow IAT Mean": 1000,
    "Flow IAT Std": 250,
    "Active Mean": 300,
    "Idle Mean": 2000,
}

result = predictor.predict(sample_flow)

print(result)