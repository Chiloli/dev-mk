import random
import re
from datetime import datetime, timedelta
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import IsolationForest

# 1. 정상 로그 생성 함수
zones = ["INZENSS_R&D", "INZENSS_DMZ", "INZENSS_MGMT"]
actions = ["Deny", "Permit"]
ips = ["100.255.255.246", "192.168.0.1", "10.0.0.15", "172.16.10.5"]
src_ips = ["50.255.255.242", "60.70.80.90", "8.8.8.8", "123.45.67.89"]
ports = [25, 80, 443, 587, 8080, 3000]

def generate_log(index):
    policy_id = random.randint(100, 200)
    src_zone = random.choice(zones)
    dst_zone = random.choice(zones)
    action = random.choice(actions)
    sent = random.randint(100, 1000)
    rcvd = random.randint(100, 1000)
    src_ip = random.choice(src_ips)
    dst_ip = random.choice(ips)
    src_port = random.randint(1024, 65535)
    dst_port = random.choice(ports)
    start_time = (datetime.now() - timedelta(seconds=index * 5)).strftime("%Y-%m-%d %H:%M:%S")

    log = (
        f"Cyberone-HQ-FW-NS208: NetScreen device_id=Cyberone-HQ-FW-NS208  "
        f"[Root]system-notification-00257(traffic): duration=4 policy_id={policy_id} "
        f"service=smtp (tcp) proto=6 src zone={src_zone} dst zone={dst_zone} "
        f"action={action} sent={sent} rcvd={rcvd} src={src_ip} dst={dst_ip} "
        f"src_port={src_port} dst_port={dst_port} "
        f"src-xlated ip=11.26.15.20 port=13605 dst-xlated ip=111.11.11.189 port=25 "
        f"session_id=127863 reason=Close - TCP FIN start_time=\"{start_time}\""
    )
    return log

# 2. 로그 파일 생성
normal_logs = [generate_log(i) for i in range(500)]
with open("normal_logs.txt", "w", encoding="utf-8") as f:
    for log in normal_logs:
        f.write(log + "\n")

# 3. TF-IDF 벡터화
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(normal_logs)

# 4. Isolation Forest 모델 훈련
model = IsolationForest(contamination=0.01, random_state=42)
model.fit(X)

# 5. 모델 및 벡터 저장
joblib.dump(model, "anomaly_model.joblib")
joblib.dump(vectorizer, "vectorizer.joblib")

print("모델 학습 완료 및 저장됨.")
