FROM python:3.10-slim

# 작업 디렉토리
WORKDIR /app

# 필수 패키지 설치: pip + 한글 폰트 + 폰트 설정 도구
RUN apt-get update && \
    apt-get install -y python3-pip fonts-nanum fontconfig && \
    fc-cache -fv && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# 의존성 복사 및 설치
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# 코드 복사
COPY . .

# 실행 명령
CMD ["python", "main.py"]
