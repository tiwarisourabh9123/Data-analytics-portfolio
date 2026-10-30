Marketing Analytics & Reporting Automation Project Overview 

1. Project Overview

This project aims to build an end-to-end marketing analytics and reporting automation solution for an EdTech training company offering online and offline courses across India and international markets.

The company invests in multiple digital marketing channels, including SEO, paid search, and social media advertising, to generate enquiries and acquire students. However, marketing performance data is spread across different platforms, while lead and enrolment information is maintained separately in Zoho CRM.

The objective is to integrate these data sources into a centralized cloud data warehouse, automate data extraction and transformation, and develop Power BI dashboards that connect marketing activities with lead generation and actual student enrolments.

The solution will use Python, Google Cloud Platform (GCP), BigQuery, dbt, SQL, and Power BI. It will also establish a reliable historical data foundation for future predictive analytics and machine learning.

2. Business Problems

The project aims to address the following business challenges:

Fragmented Data: Marketing and CRM data are distributed across multiple platforms, making consolidated reporting difficult.

Manual Reporting: Collecting, combining, and preparing reports from different sources requires repetitive manual effort.

Unclear Marketing ROI: Difficulty connecting marketing expenditure with qualified leads and actual student enrolments.

Lead Quality Analysis: Limited visibility into which channels and campaigns generate high-quality leads.

Campaign Performance: Difficulty identifying campaigns that deliver meaningful business outcomes rather than just clicks and traffic.

Budget Allocation: Lack of consolidated performance insights to support marketing investment decisions.

Market and Course Analysis: Difficulty comparing marketing performance across countries, regions, and training programs.

Historical Data Management: Lack of a centralized, structured dataset for long-term analysis and future predictive modelling.

3. Data Sources

The project will integrate the following platforms:

Data Source

Purpose

Google Analytics 4 (GA4)

Website traffic, user behaviour, sessions, and conversions

Google Search Console (GSC)

Organic search performance, queries, clicks, and impressions

Google Ads

Paid search campaign performance and advertising expenditure

Meta Ads Manager

Facebook and Instagram advertising performance

LinkedIn Ads

LinkedIn campaign performance and lead generation

ChatGPT Ads Manager

ChatGPT advertising campaign performance and reporting

Zoho CRM

Lead details, qualification stages, course interests, and enrolment outcomes

Data availability and automated extraction will depend on API access, account permissions, and platform reporting capabilities. CSV exports may be used where API access is unavailable.

4. Project Objectives

Integrate data from multiple marketing platforms and Zoho CRM.

Automate data extraction using Python and available APIs.

Build a centralized cloud data warehouse using Google BigQuery.

Clean, standardize, and transform data using SQL and dbt.

Connect marketing performance with CRM leads and enrolments wherever reliable matching is possible.

Develop interactive Power BI dashboards for consolidated marketing reporting.

Analyze channel, campaign, course, and geographical performance.

Measure marketing efficiency using KPIs such as advertising spend, cost per lead, cost per qualified lead, and cost per enrolment where attribution is reliable.

Reduce repetitive manual reporting and improve access to actionable insights.

Build a historical data foundation for future predictive analytics.

5. Technology Stack

Technology

Purpose

Python

API extraction, data processing, and automation

SQL

Data querying and transformation

Google Cloud Platform

Cloud infrastructure

Google BigQuery

Centralized data warehouse

dbt

Data transformation, modelling, and quality testing

Power BI

Dashboards and business intelligence

Git & GitHub

Version control and project documentation


The solution follows an end-to-end data pipeline, moving from multi-platform data collection to automated reporting and predictive analytics.

6. Proposed Data Architecture

The solution follows an end-to-end data pipeline, moving from multi-platform data collection to automated reporting and predictive analytics.

Architecture Overview

```text
[ 1. DATA SOURCES ]
  ├── Google Analytics 4 (GA4)
  ├── Google Search Console (GSC)
  ├── Google Ads
  ├── Meta Ads Manager
  ├── LinkedIn Ads
  ├── ChatGPT Ads / AI Referral
  └── Zoho CRM (Leads & Deals)
            │
            ▼
[ 2. EXTRACTION & INGESTION ]
  ├── Python API Extraction (Cloud Run Jobs)
  ├── OAuth2 & API Authentication
  ├── Pagination & Rate-Limit Handling (Exponential Backoff)
  └── JSON Normalization & Schema Validation (Pydantic / Pandas)
            │
            ▼
[ 3. RAW DATA STORAGE - GOOGLE BIGQUERY ]
  └── Dataset: raw_marketing (Partitioned by Date, Clustered by Campaign/Account)
        ├── raw_ga4_events
        ├── raw_gsc_search
        ├── raw_google_ads
        ├── raw_meta_ads
        ├── raw_linkedin_ads
        ├── raw_chatgpt_ads
        └── raw_zoho_leads & raw_zoho_deals
            │
            ▼
[ 4. DBT TRANSFORMATION - BIGQUERY ]
  ├── Staging Layer (stg_)
  │     └── Type casting, naming standardization, deduplication
  ├── Intermediate Layer (int_)
  │     └── Currency conversion, UTM parsing, session-to-lead matching
  └── Marts Layer (fct_ & dim_)
        ├── dim_campaigns, dim_channels, dim_customers, dim_dates
        ├── fct_ad_spend_daily (spend, clicks, impressions)
        └── fct_marketing_conversion_journey (multi-touch attribution)
            │
            ├─────────────────────────────────────────┐
            ▼                                         ▼
[ 5. BUSINESS INTELLIGENCE ]              [ 6. PREDICTIVE ANALYTICS ]
  Power BI Interactive Dashboards           BigQuery ML (BQML)
  ├── Executive Marketing Overview          ├── Multi-Channel Budget Optimization
  ├── SEO & Paid Channel Deep Dives         ├── Lead Scoring & Conversion Propensity
  ├── End-to-End Lead Funnel                └── Ad Spend & Lead Forecasting (ARIMA)
  └── Attribution & Conversion ROI
            ▲                                         ▲
            └────────────────────┬────────────────────┘
                                 │
[ 7. ORCHESTRATION & AUTOMATION ]
  └── Google Cloud Scheduler (Cron Trigger: 02:00 AM UTC Daily)
        └── Google Cloud Workflows / Cloud Run
              ├── 1. Trigger Python Extraction Services
              ├── 2. Run dbt Build & Data Quality Tests
              ├── 3. Execute BigQuery ML Inference Models
              ├── 4. Trigger Power BI Dataset Refresh (REST API)
              └── 5. Dispatch Slack / Email Execution Alerts
Pipeline ComponentsLayerTechnologyResponsibilityData SourcesGA4, GSC, Google Ads, Meta Ads, LinkedIn Ads, ChatGPT Ads, Zoho CRMCollect marketing, website, lead, and customer journey data.ExtractionPython, REST APIs, Cloud Run JobsAuthenticate, extract, normalize, and validate raw payload data.Raw StorageGoogle BigQueryPersist immutable, partitioned source-level tables.Transformationdbt, SQL, BigQueryClean, standardize, deduplicate, and model dimensional star schemas.ReportingPower BIDeliver executive dashboards and actionable business metrics.Predictive AnalyticsBigQuery MLPower lead scoring, budget optimization, and time-series forecasting.OrchestrationCloud Scheduler, Cloud WorkflowsAutomate end-to-end execution, health checks, and alerting.Automation WorkflowTrigger: Cloud Scheduler initiates the workflow execution daily at 02:00 UTC.Extraction: Python containers extract the latest incremental data via source APIs.Ingestion: Validated payloads are staged into date-partitioned BigQuery raw tables.Transformation: dbt builds staging, intermediate, and dimensional mart tables.Quality Checks: dbt tests enforce schema validity, unique constraints, and non-null values.BI Refresh: Power BI REST API triggers a scheduled refresh of the semantic model.Notification: Webhooks dispatch execution logs and success/failure alerts to Slack/Email.ML Inference: BigQuery ML models calculate updated lead scores and 30-day performance forecasts.Implementation Note: This architecture represents the target production design. Features such as multi-touch attribution algorithms, dynamic currency conversion, BigQuery ML models, and direct Power BI REST API refreshes are enabled progressively as source credentials and data schemas are confirmed.
```

7. Key Business Metrics

The dashboards will focus on:

Website users and sessions.

Organic clicks, impressions, and CTR.

Advertising impressions, clicks, and expenditure.

Campaign-level performance.

Total enquiries and qualified leads.

Confirmed student enrolments.

Lead-to-qualified and lead-to-enrolment conversion rates.

Cost per lead and cost per qualified lead.

Cost per enrolment where reliable attribution is available.

Marketing performance by channel, campaign, course, and country.

8. Expected Dashboards

The Power BI reporting solution will include:

Marketing Overview: Consolidated view of website traffic, marketing expenditure, enquiries, and enrolments.

SEO Performance: Organic search traffic, queries, landing pages, and search visibility.

Paid Advertising Performance: Google, Meta, LinkedIn, and ChatGPT campaign performance.

Lead Funnel Analysis: Lead sources, qualification stages, conversion rates, and enrolments.

Course and Geographical Analysis: Performance across training programs and domestic and international markets.

9. Future Scope: Predictive Analytics

Once sufficient historical data is collected and validated, the warehouse can support future machine learning initiatives such as:

Lead conversion prediction.

Lead quality scoring.

Campaign performance forecasting.

Marketing budget optimization.

Course demand and enrolment forecasting.

These are future enhancements, not part of the initial implemented scope.

10. Expected Outcome

The final solution will provide a centralized and automated marketing analytics system that connects digital marketing performance with CRM lead and enrolment outcomes.

It will help the business understand which channels and campaigns generate valuable leads, evaluate marketing expenditure, identify growth opportunities, and make more informed marketing investment decisions.

It will also establish a structured historical data foundation for advanced analytics and future predictive modelling.

Project Status: In Progress

Project Type: End-to-End Marketing Analytics, Data Engineering, Reporting Automation, and Business Intelligence
