FROM python:3.12-slim

WORKDIR /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends curl ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Kompose 1.38.0, matching the version used in the completed notebook.
RUN curl -L https://github.com/kubernetes/kompose/releases/download/v1.38.0/kompose-linux-amd64 \
    -o /usr/local/bin/kompose \
    && chmod +x /usr/local/bin/kompose

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app

RUN mkdir -p app/uploads app/generated

EXPOSE 5000

CMD ["python", "app/main.py"]
