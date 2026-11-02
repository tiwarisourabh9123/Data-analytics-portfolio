import sys
import os
from datetime import datetime, timezone, timedelta
import pandas as pd
import numpy as np
from googleapiclient.discovery import build

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from auth import get_bigquery_client, load_records_to_bigquery, get_credentials

TABLE_NAME = "gsc_search_performance_raw"

# Use your exact property URL from Google Search Console
SITE_URL = "https://webgisolutions.com/"

def fetch_last_7_days_gsc(site_url: str) -> list:
    credentials = get_credentials()
    service = build("searchconsole", "v1", credentials=credentials)

    # GSC data finalizes with a 2-day lag
    end_date_dt = datetime.now(timezone.utc) - timedelta(days=2)
    start_date_dt = end_date_dt - timedelta(days=6)

    start_date = start_date_dt.strftime("%Y-%m-%d")
    end_date = end_date_dt.strftime("%Y-%m-%d")

    print(f"Querying GSC API: {start_date} to {end_date} for site: {site_url}")

    request_body = {
        "startDate": start_date,
        "endDate": end_date,
        "dimensions": ["date", "query", "page", "country", "device"],
        "rowLimit": 25000,
        "dataState": "final"
    }

    try:
        response = service.searchanalytics().query(siteUrl=site_url, body=request_body).execute()
        rows = response.get("rows", [])
    except Exception as e:
        print(f"Error calling GSC API: {e}")
        return []

    if not rows:
        print(f"No records returned for {site_url} within the date range.")
        return []

    records_list = []
    for r in rows:
        keys = r.get("keys", [])
        records_list.append({
            "date": keys[0] if len(keys) > 0 else None,
            "query": keys[1] if len(keys) > 1 else "",
            "page": keys[2] if len(keys) > 2 else "",
            "country": keys[3] if len(keys) > 3 else "",
            "device": keys[4] if len(keys) > 4 else "",
            "clicks": r.get("clicks", 0),
            "impressions": r.get("impressions", 0),
            "ctr": r.get("ctr", 0.0),
            "position": r.get("position", 0.0),
        })

    df = pd.DataFrame(records_list)

    # Clean with Pandas and NumPy
    df["extracted_at"] = datetime.now(timezone.utc).isoformat()
    df["date"] = pd.to_datetime(df["date"]).dt.strftime("%Y-%m-%d")
    df["clicks"] = pd.to_numeric(df["clicks"], errors="coerce").fillna(0).astype(int)
    df["impressions"] = pd.to_numeric(df["impressions"], errors="coerce").fillna(0).astype(int)
    df["ctr"] = np.round(pd.to_numeric(df["ctr"], errors="coerce").fillna(0.0), 4)
    df["position"] = np.round(pd.to_numeric(df["position"], errors="coerce").fillna(0.0), 2)
    df["query"] = df["query"].astype(str).str.strip()
    df["page"] = df["page"].astype(str).str.strip()
    df["country"] = df["country"].astype(str).str.upper().str.strip()
    df["device"] = df["device"].astype(str).str.lower().str.strip()

    print(f"Processed {len(df)} rows using Pandas.")
    return df.to_dict(orient="records")

def run_pipeline():
    print("=" * 60)
    print("Starting Pipeline: Live GSC 7-Day Ingestion via Pandas")
    print("=" * 60)

    bq_client = get_bigquery_client()
    records = fetch_last_7_days_gsc(SITE_URL)

    if records:
        print(f"Loading {len(records)} records into BigQuery table: {TABLE_NAME}...")
        load_records_to_bigquery(bq_client, TABLE_NAME, records)
        print("Search Console Ingestion completed successfully.\n")
    else:
        print("No records loaded.\n")

if __name__ == "__main__":
    run_pipeline()