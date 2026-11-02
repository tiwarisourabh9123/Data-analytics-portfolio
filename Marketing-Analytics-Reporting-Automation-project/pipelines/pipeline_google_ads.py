import sys
import os
from datetime import datetime, timezone, timedelta
import pandas as pd
import numpy as np

# Import BigQuery functions from root auth module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from auth import get_bigquery_client, load_records_to_bigquery

TABLE_NAME = "google_ads_performance_raw"

def generate_edtech_google_ads_data() -> list:
    """
    Generates realistic EdTech Google Ads performance records for the last 30 days.
    Includes Search (Lead Gen), Performance Max (Multi-Channel), and Display (Remarketing).
    """
    campaigns = [
        {
            "campaign_id": "gads_edtech_101",
            "campaign_name": "EdTech_Search_DataScience_Certification_India",
            "advertising_channel_type": "SEARCH",
            "cpc_range": (45.0, 95.0),
            "impressions_range": (800, 2200),
            "ctr_range": (0.052, 0.091),
            "cvr_range": (0.045, 0.085),       # Lead form submission rate
            "lead_to_enrollment_value": 35000.0 # Average fee value attributed per lead batch
        },
        {
            "campaign_id": "gads_edtech_102",
            "campaign_name": "EdTech_Search_FullStack_Python_Bootcamp",
            "advertising_channel_type": "SEARCH",
            "cpc_range": (35.0, 70.0),
            "impressions_range": (1200, 3100),
            "ctr_range": (0.048, 0.082),
            "cvr_range": (0.040, 0.075),
            "lead_to_enrollment_value": 28000.0
        },
        {
            "campaign_id": "gads_edtech_103",
            "campaign_name": "EdTech_PMax_Masterclass_Webinar_Regs",
            "advertising_channel_type": "PERFORMANCE_MAX",
            "cpc_range": (18.0, 38.0),
            "impressions_range": (3500, 8500),
            "ctr_range": (0.022, 0.048),
            "cvr_range": (0.070, 0.140),       # Higher conversion rate for free/low-cost masterclass
            "lead_to_enrollment_value": 4500.0
        },
        {
            "campaign_id": "gads_edtech_104",
            "campaign_name": "EdTech_Display_Remarketing_LMS_Dropoffs",
            "advertising_channel_type": "DISPLAY",
            "cpc_range": (7.0, 15.0),
            "impressions_range": (6000, 16000),
            "ctr_range": (0.009, 0.019),
            "cvr_range": (0.020, 0.045),
            "lead_to_enrollment_value": 25000.0
        }
    ]

    records = []
    extracted_at = datetime.now(timezone.utc).isoformat()

    # Generate 30 days of campaign performance
    for day_offset in range(30, 0, -1):
        target_date = (datetime.now(timezone.utc) - timedelta(days=day_offset)).strftime("%Y-%m-%d")

        for cmp in campaigns:
            # Weekend variance factor: EdTech searches often rise on weekends as students/pros browse
            day_of_week = (datetime.now(timezone.utc) - timedelta(days=day_offset)).weekday()
            weekend_multiplier = 1.25 if day_of_week in [5, 6] else 1.0

            impressions = int(np.random.randint(*cmp["impressions_range"]) * weekend_multiplier)
            ctr = float(np.random.uniform(*cmp["ctr_range"]))
            clicks = max(1, int(impressions * ctr))

            avg_cpc = float(np.random.uniform(*cmp["cpc_range"]))
            cost = round(clicks * avg_cpc, 2)

            cvr = float(np.random.uniform(*cmp["cvr_range"]))
            conversions = round(float(clicks * cvr), 2)

            # Revenue / Enrollment value attributed
            value_variance = float(np.random.uniform(0.85, 1.25))
            conversions_value = round((conversions * (cmp["lead_to_enrollment_value"] / 10.0)) * value_variance, 2)

            records.append({
                "date": target_date,
                "campaign_id": cmp["campaign_id"],
                "campaign_name": cmp["campaign_name"],
                "advertising_channel_type": cmp["advertising_channel_type"],
                "impressions": impressions,
                "clicks": clicks,
                "cost": cost,
                "conversions": conversions,
                "conversions_value": conversions_value,
                "cpc": round(cost / clicks, 2) if clicks > 0 else 0.0,
                "ctr": round((clicks / impressions) * 100.0, 3) if impressions > 0 else 0.0,
                "roas": round(conversions_value / cost, 2) if cost > 0 else 0.0
            })

    df = pd.DataFrame(records)
    df["extracted_at"] = extracted_at

    # Cast to strict BigQuery-compatible data types
    df["impressions"] = pd.to_numeric(df["impressions"]).astype(int)
    df["clicks"] = pd.to_numeric(df["clicks"]).astype(int)
    df["cost"] = pd.to_numeric(df["cost"]).astype(float)
    df["conversions"] = pd.to_numeric(df["conversions"]).astype(float)
    df["conversions_value"] = pd.to_numeric(df["conversions_value"]).astype(float)
    df["cpc"] = pd.to_numeric(df["cpc"]).astype(float)
    df["ctr"] = pd.to_numeric(df["ctr"]).astype(float)
    df["roas"] = pd.to_numeric(df["roas"]).astype(float)

    print(f"Generated {len(df)} EdTech Google Ads performance records across {len(campaigns)} campaigns.")
    return df.to_dict(orient="records")

def run_pipeline():
    print("=" * 65)
    print("Starting Pipeline: EdTech Google Ads Performance Ingestion")
    print("=" * 65)

    bq_client = get_bigquery_client()
    records = generate_edtech_google_ads_data()

    if records:
        print(f"Loading {len(records)} records into BigQuery table: {TABLE_NAME}...")
        load_records_to_bigquery(bq_client, TABLE_NAME, records)
        print("EdTech Google Ads Ingestion completed successfully.\n")
    else:
        print("No records loaded. Ingestion stopped.\n")

if __name__ == "__main__":
    run_pipeline()