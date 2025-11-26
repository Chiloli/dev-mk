FROM python:3.10-slim

# 작업 디렉토리 설정
WORKDIR /app

# 의존성 복사
COPY requirements.txt .

# 이미 설치된 패키지는 건너뛰고 설치
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir --requirement requirements.txt

# 나머지 소스 복사
COPY . .

# 기본 실행 파일 지정
CMD ["python", "main.py"]
