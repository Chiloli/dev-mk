# model.py
import joblib
import os

# 모델 로드
vectorizer = joblib.load(os.path.join(os.path.dirname(__file__), "vectorizer.joblib"))
model = joblib.load(os.path.join(os.path.dirname(__file__), "anomaly_model.joblib"))

def detect_anomaly(buffer):
    if not buffer:
        return False

    latest_msg = buffer[-1]["message"]
    X = vectorizer.transform([latest_msg])
    prediction = model.predict(X)

    return prediction[0] == -1  # -1: 이상, 1: 정상
