# ✅ 베이스 이미지
FROM nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04

# ✅ Python 설치
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# ✅ requirements.txt 먼저 복사하고 설치 (변경 적음)
COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

# ✅ 그 다음 소스 코드 복사 (변경 많음)
WORKDIR /app
COPY . .

CMD ["python3", "main.py"]