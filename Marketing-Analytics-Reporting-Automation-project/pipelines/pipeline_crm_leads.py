import os
import sys
import uuid
from datetime import datetime, timedelta, timezone
import numpy as np
import pandas as pd

# Add project root to sys.path to access auth
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from auth import get_bigquery_client, load_records_to_bigquery

TABLE_NAME = "zoho_crm_leads_raw"

def generate_crm_leads_data() -> list:
    """
    Simulates CRM lead stage transitions and course sales pipeline
    data matching a standard Zoho CRM Leads module schema.
    """
    stages = [
        {"stage": "New Lead", "weight": 0.35, "deal_value": 0},
        {"stage": "Counseling Scheduled", "weight": 0.25, "deal_value": 0},
        {"stage": "Masterclass Attended", "weight": 0.20, "deal_value": 0},
        {"stage": "Closed Won (Enrolled)", "weight": 0.12, "deal_value": 35000},
        {"stage": "Closed Lost", "weight": 0.08, "deal_value": 0}
    ]

    lead_sources = [
        "Google Ads",
        "Meta Ads",
        "Organic Search (SEO)",
        "Direct / Website",
        "ChatGPT / AI Assistant"
    ]

    courses = [
        "Data Science & AI Masterclass",
        "Full Stack Python Web Development",
        "Cloud Computing & DevOps",
        "Business Analytics with Power BI"
    ]

    stage_choices = [s["stage"] for s in stages]
    stage_weights = [s["weight"] for s in stages]
    deal_lookup = {s["stage"]: s["deal_value"] for s in stages}

    records = []
    extracted_at = datetime.now(timezone.utc).isoformat()

    for day_offset in range(30, 0, -1):
        target_date = (datetime.now(timezone.utc) - timedelta(days=day_offset)).strftime("%Y-%m-%d")
        daily_leads = np.random.randint(12, 28)

        for _ in range(daily_leads):
            chosen_stage = np.random.choice(stage_choices, p=stage_weights)
            base_value = deal_lookup[chosen_stage]
            actual_value = round(base_value * float(np.random.uniform(0.9, 1.2)), 2) if base_value > 0 else 0.0

            records.append({
                "lead_id": f"crm_{uuid.uuid4().hex[:10]}",
                "created_date": target_date,
                "lead_source": str(np.random.choice(lead_sources)),
                "interested_course": str(np.random.choice(courses)),
                "stage": chosen_stage,
                "deal_value_inr": actual_value,
                "extracted_at": extracted_at
            })

    df = pd.DataFrame(records)
    print(f"Generated {len(df)} EdTech CRM lead records.")
    return df.to_dict(orient="records")

def run_pipeline():
    print("=" * 65)
    print("Starting Pipeline: Zoho CRM Leads Ingestion")
    print("=" * 65)

    bq_client = get_bigquery_client()
    records = generate_crm_leads_data()

    if records:
        print(f"Loading {len(records)} records into BigQuery table: {TABLE_NAME}...")
        load_records_to_bigquery(bq_client, TABLE_NAME, records)
        print("CRM leads ingestion completed successfully.\n")
    else:
        print("No records generated. Ingestion stopped.\n")

if __name__ == "__main__":
    run_pipeline()