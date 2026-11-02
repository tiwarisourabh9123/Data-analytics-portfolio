FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends git && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt dbt-bigquery

COPY . .

RUN chmod +x run_pipeline.sh

ENV DBT_PROFILES_DIR=/app/dbt_marketing

CMD ["./run_pipeline.sh"]
