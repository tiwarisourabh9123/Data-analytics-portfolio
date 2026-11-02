
# Automated Marketing Analytics Pipeline & dbt Transformations

An end-to-end data pipeline that extracts multi-channel marketing data (Meta Ads, Google Ads, GA4, Google Search Console, Zoho CRM, and ChatGPT interactions), loads it into Google BigQuery, transforms it into analytics-ready data marts using dbt, validates data integrity with 14 automated quality tests, and connects directly to Power BI for executive reporting.

---

## Architecture Overview

```
[Meta / Google Ads / GA4 / GSC / Zoho / ChatGPT]
                       │
                       ▼  (Python Ingestion Layer)
          [Google BigQuery: raw_* tables]
                       │
                       ▼  (dbt Transformations)
         [BigQuery Staging: stg_* views]
                       │
                       ▼
       [BigQuery Marts: fct_* analytics tables]
                       │
                       ▼
   [dbt Data Quality Tests (14 automated checks)]
                       │
                       ▼
   [Power BI Dashboard / Automated Scheduling]

```

---

## Project Structure

```text
marketing_analytics_pipeline/
├── dbt_marketing/             # dbt transformations project
│   ├── dbt_project.yml        # dbt configurations
│   ├── models/
│   │   ├── staging/           # stg_* views and source definitions (_sources.yml)
│   │   └── marts/             # fct_* production fact tables (ROI, SEO, Paid Ads)
│   └── tests/                 # Automated custom and generic schema tests
├── pipelines/                 # Python ingestion scripts
│   ├── pipeline_facebook_ads.py
│   ├── pipeline_google_ads.py
│   ├── pipeline_google_analytics.py
│   ├── pipeline_search_console.py
│   ├── pipeline_crm_leads.py
│   └── pipeline_chatgpt_ads.py
├── images/                    # Execution logs, BigQuery tables, DAG lineage, Power BI screenshots
├── power bi/                  # Power BI report template files (.pbit)
├── run_all_pipelines.py       # Master Python ingestion coordinator
├── run_pipeline.ps1           # Windows PowerShell end-to-end automation runner
├── run_pipeline.sh            # Linux/Container automation entrypoint
├── Dockerfile                 # Container image specification for Cloud Run deployment
├── requirements.txt           # Python dependencies
└── .gcloudignore              # Deployment exclusion rules

```

---

## Quick Start & Setup

### 1. Clone & Set Up Virtual Environment

```powershell
# Clone the repository
git clone https://github.com/tiwarisourabh9123/Data-analytics-portfolio.git
cd Data-analytics-portfolio/Marketing-Analytics-Reporting-Automation-project

# Create and activate virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1

# Install required dependencies
pip install -r requirements.txt dbt-bigquery

```

### 2. Configure Credentials

Place your Google Cloud service account key (`sa-key.json`) in the project root with the following IAM permissions:

* BigQuery Admin
* BigQuery Job User
* BigQuery Data Editor

---

## Running the Pipeline

### Manual End-to-End Execution (Windows)

Run the master automation script to execute the Python ingestion, dbt models, and data tests in sequence:

```powershell
.\run_pipeline.ps1

```

### Individual Execution Commands

```powershell
# 1. Ingest marketing source data into BigQuery raw tables
python run_all_pipelines.py

# 2. Run dbt models (Staging & Marts)
cd dbt_marketing
dbt run

# 3. Execute all 14 data quality and schema validation tests
dbt test

# 4. View interactive DAG lineage graph in your browser
dbt docs generate
dbt docs serve --port 8085

```

---

## Power BI Integration

The reporting layer connects directly to BigQuery production mart tables via DirectQuery/Import:

1. Open Power BI Desktop.
2. Select **Get Data** > **Google BigQuery**.
3. Authenticate with your Google account or Service Account key.
4. Select the transformed fact marts under project `marketing-analytics-9123`:
* `fct_marketing_roi_daily` (Omnichannel spend, revenue, ROAS, and conversion metrics)
* `fct_paid_ad_performance_daily` (Platform-level impressions, clicks, CPC, CTR)
* `fct_organic_seo_daily` (Search queries, impressions, CTR, organic positions)


5. Load the included report template: `power bi/marketing_analytics.pbit` to view pre-built executive dashboards.

---

## Production Orchestration & Automation

### Method A: Local Automated Daily Cron (Windows Task Scheduler)

Schedules the pipeline to execute automatically every day at 05:00 AM IST:

```powershell
$Action = New-ScheduledTaskAction -Execute "PowerShell.exe" -Argument "-ExecutionPolicy Bypass -File C:\Users\soura\marketing_analytics_pipeline\run_pipeline.ps1"
$Trigger = New-ScheduledTaskTrigger -Daily -At 5:00AM
Register-ScheduledTask -TaskName "DailyMarketingPipelineSync" -Action $Action -Trigger $Trigger -Description "Daily Marketing Ingestion and dbt Transformations"

```

### Method B: Serverless Container Deployment (Google Cloud Run & Cloud Scheduler)

Builds the container image and registers it with GCP Artifact Registry for scheduled serverless cloud execution:

```powershell
# 1. Build and push container to Google Artifact Registry
gcloud builds submit --tag asia-south1-docker.pkg.dev/marketing-analytics-9123/dbt-repo/marketing-pipeline:v1

# 2. Create the Cloud Run Job
gcloud run jobs create marketing-daily-sync `
    --image asia-south1-docker.pkg.dev/marketing-analytics-9123/dbt-repo/marketing-pipeline:v1 `
    --region asia-south1

# 3. Schedule execution daily at 5:00 AM IST via Cloud Scheduler
gcloud scheduler jobs create http trigger-marketing-sync `
    --location asia-south1 `
    --schedule "0 5 * * *" `
    --time-zone "Asia/Kolkata" `
    --uri "https://asia-south1-run.googleapis.com/apis/run.googleapis.com/v1/namespaces/marketing-analytics-9123/jobs/marketing-daily-sync:run" `
    --http-method POST `
    --oauth-service-account-email "marketing-analytics-9123@appspot.gserviceaccount.com"

```
