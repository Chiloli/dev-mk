FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY train_model.py ./
COPY model.py ./
COPY utils.py ./
COPY vectorizer.joblib ./
COPY anomaly_model.joblib ./
COPY main.py ./

CMD ["python3", "main.py"]
