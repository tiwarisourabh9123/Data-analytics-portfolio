import io
import json
import os
from google.auth.transport.requests import Request
from google.cloud import bigquery
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

PROJECT_ID = "marketing-analytics-9123"
DATASET_ID = "raw"

SCOPES = [
    "https://www.googleapis.com/auth/bigquery",
    "https://www.googleapis.com/auth/cloud-platform",
    "https://www.googleapis.com/auth/webmasters.readonly",
    "https://www.googleapis.com/auth/analytics.readonly",
]

def authenticate_google():
    """
    Authenticates using OAuth 2.0 flow and manages token.json.
    Refreshes the token if expired or launches local server for new login.
    """
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            try:
                creds.refresh(Request())
            except Exception:
                creds = None

        if not creds:
            if not os.path.exists("client_secret.json"):
                raise FileNotFoundError(
                    "client_secret.json file missing. Place it in the project root."
                )
            flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", SCOPES)
            creds = flow.run_local_server(port=0)

        with open("token.json", "w") as token_file:
            token_file.write(creds.to_json())

    return creds

def get_credentials():
    return authenticate_google()

def get_bigquery_client():
    creds = authenticate_google()
    return bigquery.Client(project=PROJECT_ID, credentials=creds)

def load_records_to_bigquery(client, table_name, records):
    """
    Appends records into BigQuery raw tables.
    """
    if not records:
        print(f"No records provided to load into {table_name}.")
        return

    table_id = f"{PROJECT_ID}.{DATASET_ID}.{table_name}"

    ndjson_data = "\n".join([json.dumps(record) for record in records])
    ndjson_file = io.BytesIO(ndjson_data.encode("utf-8"))

    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON,
        autodetect=True,
        write_disposition=bigquery.WriteDisposition.WRITE_APPEND
    )

    load_job = client.load_table_from_file(ndjson_file, table_id, job_config=job_config)
    load_job.result()
    print(f"Success: {len(records)} rows written to {table_id}")

if __name__ == "__main__":
    client = get_bigquery_client()
    print("Authentication successful! Connected to BigQuery.")