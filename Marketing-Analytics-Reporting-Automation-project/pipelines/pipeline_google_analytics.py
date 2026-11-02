import sys
import os
from datetime import datetime, timezone
import pandas as pd
import numpy as np
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    DateRange,
    Dimension,
    Metric,
    RunReportRequest,
)

# Add parent directory to sys.path to import central authentication module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from auth import get_bigquery_client, load_records_to_bigquery, get_credentials

TABLE_NAME = "ga4_traffic_raw"

# Real GA4 Property ID for WebGi Solutions
GA4_PROPERTY_ID = "446290626"

def fetch_last_7_days_ga4(property_id: str) -> list:
    """
    Extracts the last 7 days of website metrics from GA4 Data API,
    processes via Pandas/NumPy, and returns formatted dictionary records.
    """
    credentials = get_credentials()
    client = BetaAnalyticsDataClient(credentials=credentials)
    extracted_at = datetime.now(timezone.utc).isoformat()

    print(f"Querying GA4 Data API for Property ID: {property_id} (Last 7 Days)...")

    request = RunReportRequest(
        property=f"properties/{property_id}",
        dimensions=[
            Dimension(name="date"),
            Dimension(name="sessionDefaultChannelGroup"),
            Dimension(name="sessionSourceMedium"),
            Dimension(name="country"),
            Dimension(name="deviceCategory"),
        ],
        metrics=[
            Metric(name="sessions"),
            Metric(name="engagedSessions"),
            Metric(name="totalUsers"),
            Metric(name="screenPageViews"),
            Metric(name="engagementRate"),
        ],
        date_ranges=[DateRange(start_date="7daysAgo", end_date="yesterday")],
    )

    try:
        response = client.run_report(request)
    except Exception as e:
        print(f"Error fetching GA4 data: {e}")
        return []

    if not response.rows:
        print(f"No GA4 records found for Property ID: {property_id} in this date range.")
        return []

    # 1. Parse API response rows
    records_list = []
    for row in response.rows:
        raw_date = row.dimension_values[0].value
        formatted_date = datetime.strptime(raw_date, "%Y%m%d").strftime("%Y-%m-%d")
        
        records_list.append({
            "date": formatted_date,
            "channel_grouping": row.dimension_values[1].value,
            "source_medium": row.dimension_values[2].value,
            "country": row.dimension_values[3].value,
            "device_category": row.dimension_values[4].value,
            "sessions": row.metric_values[0].value,
            "engaged_sessions": row.metric_values[1].value,
            "total_users": row.metric_values[2].value,
            "screen_page_views": row.metric_values[3].value,
            "engagement_rate": row.metric_values[4].value,
        })

    # 2. Process and sanitize using Pandas & NumPy
    df = pd.DataFrame(records_list)
    df["extracted_at"] = extracted_at

    # Numeric transformations
    df["sessions"] = pd.to_numeric(df["sessions"], errors="coerce").fillna(0).astype(int)
    df["engaged_sessions"] = pd.to_numeric(df["engaged_sessions"], errors="coerce").fillna(0).astype(int)
    df["total_users"] = pd.to_numeric(df["total_users"], errors="coerce").fillna(0).astype(int)
    df["screen_page_views"] = pd.to_numeric(df["screen_page_views"], errors="coerce").fillna(0).astype(int)
    df["engagement_rate"] = np.round(pd.to_numeric(df["engagement_rate"], errors="coerce").fillna(0.0), 4)

    # String sanitization
    df["channel_grouping"] = df["channel_grouping"].astype(str).str.strip()
    df["source_medium"] = df["source_medium"].astype(str).str.strip()
    df["country"] = df["country"].astype(str).str.strip()
    df["device_category"] = df["device_category"].astype(str).str.lower().str.strip()

    print(f"Processed {len(df)} rows using Pandas.")
    return df.to_dict(orient="records")

def run_pipeline():
    print("=" * 60)
    print("Starting Pipeline: Live GA4 Ingestion via Pandas")
    print("=" * 60)

    bq_client = get_bigquery_client()
    records = fetch_last_7_days_ga4(GA4_PROPERTY_ID)

    if records:
        print(f"Loading {len(records)} records into BigQuery table: {TABLE_NAME}...")
        load_records_to_bigquery(bq_client, TABLE_NAME, records)
        print("GA4 Traffic Ingestion completed successfully.\n")
    else:
        print("No records loaded. Ingestion stopped.\n")

if __name__ == "__main__":
    run_pipeline()