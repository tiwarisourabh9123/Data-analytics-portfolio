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

6. Proposed Data Pipeline

The solution will follow this workflow:

DATA SOURCES
GA4 | GSC | Google Ads | Meta Ads
LinkedIn Ads | ChatGPT Ads | Zoho CRM

      -----------------------------------------------------------------------------------+
|                                           DATA SOURCES                                             |
|  [GA4]   [GSC]   [Google Ads]   [Meta Ads]   [LinkedIn Ads]   [ChatGPT / AI Ads]   [Zoho CRM]      |
+----------------------------------------------------------------------------------------------------+
                                                  │
                                                  ▼
+----------------------------------------------------------------------------------------------------+
|                         EXTRACTION & INGESTION (Python / Cloud Functions)                          |
|  • OAuth2 / API Token Authentication                                                               |
|  • Parameterized Pagination & Rate-Limit Handling (Exponential Backoff)                            |
|  • JSON Normalization & Schema Validation (Pydantic / Pandas)                                      |
+----------------------------------------------------------------------------------------------------+
                                                  │
                                                  ▼
+----------------------------------------------------------------------------------------------------+
|                                    RAW DATA STORAGE (BigQuery)                                     |
|  Dataset: raw_marketing                                                                            |
|  Tables:  raw_ga4_events, raw_gsc_search, raw_google_ads, raw_meta_ads,                            |
|           raw_linkedin_ads, raw_chatgpt_ads, raw_zoho_leads, raw_zoho_deals                        |
|  Strategy: Daily Partitioned (_PARTITIONDATE), Clustered by campaign_id / account_id               |
+----------------------------------------------------------------------------------------------------+
                                                  │
                                                  ▼
+----------------------------------------------------------------------------------------------------+
|                                DBT TRANSFORMATION ENGINE (BigQuery)                               |
|                                                                                                    |
|  [1. Staging Layer (stg_)]                                                                         |
|      - Cast types, standardize snake_case names, unnest payloads, deduplicate via surrogate keys    |
|                                                                                                    |
|  [2. Intermediate Layer (int_)]                                                                    |
|      - Currency standardization (USD/INR conversion)                                               |
|      - UTM Parameter Parsing & Session-to-Lead Matching                                            |
|      - Attribution Modeling (First-Touch, Last-Touch, Linear, Position-Based)                      |
|                                                                                                    |
|  [3. Marts Layer (fct_ & dim_)]                                                                    |
|      - dim_campaigns, dim_channels, dim_customers, dim_dates                                       |
|      - fct_ad_spend_daily (spend, impressions, clicks, channel_id)                                  |
|      - fct_marketing_conversion_journey (lead_id, deal_value, pipeline_stage, attributed_spend)    |
+----------------------------------------------------------------------------------------------------+
                                                  │
                         ┌────────────────────────┴────────────────────────┐
                         ▼                                                 ▼
+-------------------------------------------------+  +-----------------------------------------------+
|         POWER BI REPORTING (Semantic Layer)     |  |       PREDICTIVE & ML ENGINE (BigQuery ML)    |
|  • Import / Composite DirectQuery Models        |  |  • Budget Allocation Optimization             |
|  • Unified Star Schema                          |  |  • Lead Scoring & Churn Propensity (LogReg)   |
|  • Executive KPIs: Blended CAC, MER, ROAS, LTV  |  |  • Multi-Channel Ad Spend Forecasting (ARIMA) |
|  • Attribution Funnel & Lead Velocity Dashboards|  |  • AI Search Attribution & Referral Impact    |
+-------------------------------------------------+  +-----------------------------------------------+
                         ▲                                                 ▲
                         └────────────────────────┬────────────────────────┘
                                                  │
+----------------------------------------------------------------------------------------------------+
|                                  ORCHESTRATION & AUTOMATION                                        |
|  • Google Cloud Scheduler (Cron triggers: 02:00 AM UTC Daily)                                      |
|  • Google Cloud Workflows / Cloud Composer / GitHub Actions Workflow                               |
|  • Step 1: Run Python Ingestion Cloud Run Jobs                                                     |
|  • Step 2: Trigger dbt Cloud API / dbt-core execution (`dbt build --select tag:daily`)              |
|  • Step 3: Trigger BigQuery ML scoring scheduled queries                                           |
|  • Step 4: Call Power BI REST API to trigger Dataset Scheduled Refresh                             |
|  • Step 5: Send Slack / Email alert on task status via Webhook                                     |
+----------------------------------------------------------------------------------------------------+


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
