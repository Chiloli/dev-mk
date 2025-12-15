import os
import joblib
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.feature_extraction.text import HashingVectorizer

# 벡터라이저 설정 (fit 없이 사용 가능)
vectorizer = HashingVectorizer(n_features=2**12, alternate_sign=False, norm='l2')

# 모델 경로
model_path = "anomaly_model.joblib"

# 모델 로딩 또는 초기화
if os.path.exists(model_path):
    model = joblib.load(model_path)
else:
    model = PassiveAggressiveClassifier()
    model.partial_fit(vectorizer.transform(["init"]), [1], classes=[0, 1])

# 이상 탐지 함수
def detect_anomaly(msg: str) -> bool:
    X = vectorizer.transform([msg])
    return model.predict(X)[0] == 0  # 0: 이상, 1: 정상

# 모델 업데이트 (온라인 학습)
def update_model(msg: str, label: int):
    X = vectorizer.transform([msg])
    model.partial_fit(X, [label])

# 저장
def save_model():
    joblib.dump(model, model_path)
