import os
import sys
from datetime import datetime, timedelta, timezone
import numpy as np
import pandas as pd

# Add project root to sys.path to access auth
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from auth import get_bigquery_client, load_records_to_bigquery

TABLE_NAME = "meta_ads_performance_raw"

def generate_meta_ads_data() -> list:
    """
    Simulates Meta Graph API (Insights endpoint) ad performance records
    tailored for EdTech acquisition campaigns across Facebook and Instagram.
    """
    campaigns = [
        {
            "campaign_id": "meta_edtech_201",
            "campaign_name": "Meta_LeadGen_InstaReels_DataScience_Masterclass",
            "objective": "OUTCOME_LEADS",
            "cpc_range": (8.5, 22.0),
            "impressions_range": (4500, 12000),
            "ctr_range": (0.018, 0.038),
            "cvr_range": (0.08, 0.16),
            "revenue_attribution_factor": 2500.0
        },
        {
            "campaign_id": "meta_edtech_202",
            "campaign_name": "Meta_Traffic_Python_Roadmap_Carousel",
            "objective": "OUTCOME_TRAFFIC",
            "cpc_range": (4.0, 12.0),
            "impressions_range": (8000, 22000),
            "ctr_range": (0.022, 0.045),
            "cvr_range": (0.025, 0.055),
            "revenue_attribution_factor": 15000.0
        },
        {
            "campaign_id": "meta_edtech_203",
            "campaign_name": "Meta_Retargeting_Website_Visitors_Offer",
            "objective": "OUTCOME_SALES",
            "cpc_range": (18.0, 42.0),
            "impressions_range": (2000, 6000),
            "ctr_range": (0.030, 0.065),
            "cvr_range": (0.05, 0.11),
            "revenue_attribution_factor": 32000.0
        }
    ]

    records = []
    extracted_at = datetime.now(timezone.utc).isoformat()

    for day_offset in range(30, 0, -1):
        target_date = (datetime.now(timezone.utc) - timedelta(days=day_offset)).strftime("%Y-%m-%d")

        for cmp in campaigns:
            day_of_week = (datetime.now(timezone.utc) - timedelta(days=day_offset)).weekday()
            weekend_multiplier = 1.3 if day_of_week in [5, 6] else 1.0

            impressions = int(np.random.randint(*cmp["impressions_range"]) * weekend_multiplier)
            ctr = float(np.random.uniform(*cmp["ctr_range"]))
            clicks = max(1, int(impressions * ctr))

            avg_cpc = float(np.random.uniform(*cmp["cpc_range"]))
            spend = round(clicks * avg_cpc, 2)

            cvr = float(np.random.uniform(*cmp["cvr_range"]))
            conversions = round(float(clicks * cvr), 2)
            conversions_value = round(
                conversions * (cmp["revenue_attribution_factor"] / 12.0) * float(np.random.uniform(0.85, 1.2)),
                2
            )

            records.append({
                "date": target_date,
                "campaign_id": cmp["campaign_id"],
                "campaign_name": cmp["campaign_name"],
                "objective": cmp["objective"],
                "impressions": impressions,
                "clicks": clicks,
                "spend": spend,
                "conversions": conversions,
                "conversions_value": conversions_value,
                "cpc": round(spend / clicks, 2) if clicks > 0 else 0.0,
                "ctr": round((clicks / impressions) * 100.0, 3) if impressions > 0 else 0.0,
                "roas": round(conversions_value / spend, 2) if spend > 0 else 0.0,
                "extracted_at": extracted_at
            })

    df = pd.DataFrame(records)
    print(f"Generated {len(df)} Meta Ads performance records.")
    return df.to_dict(orient="records")

def run_pipeline():
    print("=" * 65)
    print("Starting Pipeline: Meta Ads Ingestion")
    print("=" * 65)

    bq_client = get_bigquery_client()
    records = generate_meta_ads_data()

    if records:
        print(f"Loading {len(records)} records into BigQuery table: {TABLE_NAME}...")
        load_records_to_bigquery(bq_client, TABLE_NAME, records)
        print("Meta Ads ingestion completed successfully.\n")
    else:
        print("No records generated. Ingestion stopped.\n")

if __name__ == "__main__":
    run_pipeline()