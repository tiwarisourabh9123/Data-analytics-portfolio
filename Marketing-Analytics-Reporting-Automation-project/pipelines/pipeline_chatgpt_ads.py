import os
import sys
import uuid
from datetime import datetime, timedelta, timezone
import numpy as np
import pandas as pd

# Add project root to sys.path to access the auth helper
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from auth import get_bigquery_client, load_records_to_bigquery

TABLE_NAME = "chatgpt_interactions_raw"

def generate_chatgpt_interaction_data() -> list:
    """
    Generates realistic EdTech conversational lead data simulating an AI chatbot 
    (e.g., website course assistant, AI lead qualifier, or Custom GPT integration).
    """
    intents = [
        {"intent": "Course Syllabus Inquiry", "lead_capture_prob": 0.40, "base_sentiment": 0.8},
        {"intent": "Fee & EMI Options", "lead_capture_prob": 0.70, "base_sentiment": 0.6},
        {"intent": "Placement & Hiring Partners", "lead_capture_prob": 0.85, "base_sentiment": 0.9},
        {"intent": "Upcoming Batch Timing", "lead_capture_prob": 0.50, "base_sentiment": 0.7},
        {"intent": "Prerequisites & Eligibility", "lead_capture_prob": 0.35, "base_sentiment": 0.75},
        {"intent": "General Casual Chat", "lead_capture_prob": 0.05, "base_sentiment": 0.5}
    ]

    courses = [
        "Data Science & AI Masterclass",
        "Full Stack Python Web Development",
        "Cloud Computing & DevOps",
        "Business Analytics with Power BI"
    ]

    channels = ["Website Chat Widget", "WhatsApp Bot Link", "Meta Ad Click-to-Chat", "Google Ad Chat Extension"]
    
    records = []
    extracted_at = datetime.now(timezone.utc).isoformat()

    # Generate interactions over the last 30 days
    for day_offset in range(30, 0, -1):
        target_date = (datetime.now(timezone.utc) - timedelta(days=day_offset)).strftime("%Y-%m-%d")
        daily_interactions = np.random.randint(15, 45)

        for _ in range(daily_interactions):
            intent_obj = np.random.choice(intents)
            is_lead_captured = bool(np.random.rand() < intent_obj["lead_capture_prob"])
            message_count = int(np.random.randint(2, 14))
            
            # Simulated sentiment score between 0.0 (negative) and 1.0 (positive)
            sentiment_score = round(float(np.clip(np.random.normal(intent_obj["base_sentiment"], 0.15), 0.1, 1.0)), 2)
            
            records.append({
                "interaction_id": f"chat_{uuid.uuid4().hex[:12]}",
                "interaction_date": target_date,
                "session_channel": str(np.random.choice(channels)),
                "inquired_course": str(np.random.choice(courses)),
                "primary_intent": intent_obj["intent"],
                "total_messages": message_count,
                "sentiment_score": sentiment_score,
                "lead_captured": is_lead_captured,
                "crm_synced": is_lead_captured and (np.random.rand() > 0.10), # 90% sync success rate to CRM
                "extracted_at": extracted_at
            })

    df = pd.DataFrame(records)
    print(f"Generated {len(df)} conversational records across the last 30 days.")
    return df.to_dict(orient="records")

def run_pipeline():
    print("=" * 65)
    print("Starting Pipeline: ChatGPT / AI Conversational Interactions")
    print("=" * 65)

    bq_client = get_bigquery_client()
    records = generate_chatgpt_interaction_data()

    if records:
        print(f"Loading {len(records)} records into BigQuery table: {TABLE_NAME}...")
        load_records_to_bigquery(bq_client, TABLE_NAME, records)
        print("ChatGPT interactions ingestion completed successfully.\n")
    else:
        print("No records generated. Ingestion stopped.\n")

if __name__ == "__main__":
    run_pipeline()