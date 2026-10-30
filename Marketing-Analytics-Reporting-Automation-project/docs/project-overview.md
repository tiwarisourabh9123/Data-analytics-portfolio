# Marketing Analytics & Reporting Automation

## 1. Project Overview

This project aims to build an end-to-end marketing analytics and reporting automation solution for an EdTech training company offering online and offline courses across India and international markets.

The company invests in multiple digital marketing channels, including SEO, paid search, and social media advertising, to generate enquiries and acquire students. However, marketing performance data is distributed across different platforms, while lead and enrolment information is maintained separately in Zoho CRM.

The objective is to integrate these data sources into a centralized cloud data warehouse, automate data extraction and transformation, and develop Power BI dashboards that connect marketing activities with lead generation, lead quality, and actual student enrolments.

The solution will use Python, Google Cloud Platform (GCP), BigQuery, dbt, SQL, and Power BI. It will also establish a reliable historical data foundation for future predictive analytics and machine learning.

## 2. Business Background

The EdTech company offers various training programs through online and offline learning models. It uses multiple digital marketing channels to attract potential students, generate enquiries, and increase course enrolments.

Marketing activities are managed across different platforms, including Google Ads, Meta Ads, LinkedIn Ads, and organic search channels. Website performance is tracked through Google Analytics 4 and Google Search Console, while lead and enrolment information is maintained in Zoho CRM.

Since these platforms maintain data separately, consolidating marketing performance and connecting advertising expenditure with actual business outcomes can be challenging.

The proposed solution will bring these datasets together to provide a centralized view of marketing performance and support better business decisions.

## 3. Business Problems

The project aims to address the following business challenges:

1. **Fragmented Marketing Data:** Marketing and CRM information is distributed across multiple platforms, making consolidated reporting difficult.

2. **Manual Reporting:** Collecting, combining, and preparing reports from different sources requires repetitive manual effort.

3. **Unclear Marketing ROI:** Difficulty connecting marketing expenditure with qualified leads and actual student enrolments.

4. **Limited Lead Quality Visibility:** Difficulty identifying which marketing channels and campaigns generate high-quality leads.

5. **Campaign Performance Analysis:** Limited visibility into which campaigns deliver meaningful business outcomes rather than just clicks and website traffic.

6. **Marketing Budget Allocation:** Lack of consolidated performance insights to support informed marketing investment decisions.

7. **Course-Level Performance:** Difficulty understanding which courses generate more enquiries, qualified leads, and enrolments.

8. **Geographical Performance:** Difficulty comparing marketing performance across domestic and international markets.

9. **Data Quality Issues:** Different platforms use different data structures, naming conventions, and reporting formats.

10. **Limited Historical Analysis:** Lack of a centralized historical dataset to support long-term analysis and future predictive modelling.

## 4. Data Sources

The project will integrate data from the following marketing, website analytics, and CRM platforms.

| Data Source | Purpose |
|---|---|
| Google Analytics 4 (GA4) | Website traffic, user behaviour, sessions, and tracked conversions |
| Google Search Console (GSC) | Organic search queries, clicks, impressions, CTR, and search visibility |
| Google Ads | Paid search campaign performance, advertising expenditure, clicks, and available conversion metrics |
| Meta Ads Manager | Facebook and Instagram advertising performance, expenditure, and lead generation |
| LinkedIn Ads | LinkedIn campaign performance, advertising expenditure, and lead generation |
| ChatGPT Ads Manager | ChatGPT advertising campaign performance and reporting, subject to advertiser access |
| Zoho CRM | Lead information, lead sources, qualification stages, course interests, and enrolment outcomes |

### Data Integration Considerations

- Data extraction will depend on available APIs, account permissions, and platform reporting capabilities.
- CSV exports may be used where automated API access is unavailable.
- ChatGPT advertising data and ChatGPT-related referral traffic will be treated as separate data categories.
- Marketing-to-CRM matching will depend on reliable identifiers, UTM parameters, and available tracking information.
- Platform-reported conversions will be distinguished from CRM-confirmed enrolments.

## 5. Project Objectives

The primary objectives of this project are:

1. Integrate data from multiple marketing platforms and Zoho CRM.
2. Automate data extraction using Python and available APIs.
3. Build a centralized cloud data warehouse using Google BigQuery.
4. Clean, standardize, and transform data using SQL and dbt.
5. Connect marketing performance with CRM leads and enrolments wherever reliable matching is possible.
6. Develop interactive Power BI dashboards for consolidated marketing reporting.
7. Analyze marketing performance across channels, campaigns, courses, and geographical markets.
8. Measure marketing efficiency using advertising spend, cost per lead, cost per qualified lead, and cost per enrolment wherever attribution is reliable.
9. Reduce repetitive manual reporting and improve access to actionable business insights.
10. Establish a historical data foundation for future predictive analytics.

## 6. Technology Stack

| Technology | Purpose |
|---|---|
| Python | API extraction, data processing, and automation |
| SQL | Data querying, transformation, and analytical calculations |
| Google Cloud Platform (GCP) | Cloud infrastructure and pipeline execution |
| Google BigQuery | Centralized cloud data warehouse |
| dbt | Data transformation, modelling, testing, and documentation |
| Power BI | Interactive dashboards and business intelligence reporting |
| Git and GitHub | Version control and project documentation |

## 7. Proposed Data Architecture

The proposed solution follows a structured data pipeline to collect, process, store, transform, and analyze marketing and CRM data.

### 7.1 Data Flow

**1. Data Sources**

The pipeline will collect data from the following platforms:

- Google Analytics 4 (GA4)
- Google Search Console (GSC)
- Google Ads
- Meta Ads Manager
- LinkedIn Ads
- ChatGPT Ads Manager
- Zoho CRM

↓

**2. Data Extraction and Ingestion**

Python will be used to extract data from available platform APIs and load it into Google BigQuery.

Key activities include:

- API authentication and authorization.
- Automated data extraction.
- Pagination and API rate-limit handling.
- Data normalization and schema validation.
- CSV-based extraction where API access is unavailable.

↓

**3. Cloud Data Warehouse — Google BigQuery**

BigQuery will act as the centralized storage layer for all collected marketing and CRM data.

Key activities include:

- Creating separate datasets for raw and transformed data.
- Storing source-level data in structured tables.
- Maintaining historical records.
- Organizing data for efficient querying and analysis.

↓

**4. Data Transformation — dbt and SQL**

dbt and SQL will be used to clean, standardize, transform, and organize the raw data into analytical models.

The transformation process will include:

- **Staging Layer:** Data cleaning, column standardization, type casting, and duplicate removal.
- **Intermediate Layer:** Currency standardization, UTM parsing, and preparation of marketing and CRM datasets for integration.
- **Marts Layer:** Analytical datasets for campaign performance, marketing channels, advertising expenditure, leads, and enrolments.

↓

**5. Business Intelligence — Power BI**

Power BI will connect to the transformed BigQuery datasets to develop interactive dashboards.

The proposed dashboards will cover:

- Marketing performance overview.
- SEO performance.
- Paid advertising performance.
- Lead funnel and conversion analysis.
- Course-level performance.
- Geographical performance.

↓

**6. Business Insights**

The dashboards will help business stakeholders:

- Identify high-performing marketing channels and campaigns.
- Understand lead quality and enrolment performance.
- Evaluate advertising expenditure and acquisition costs.
- Compare performance across courses and geographical markets.
- Make informed marketing budget allocation decisions.

### 7.2 Proposed Data Warehouse Structure

The BigQuery data warehouse will use separate layers to organize source data and transformed analytical datasets.

**Raw Layer — `raw_marketing`**

This layer will store data extracted from individual platforms.

Proposed tables:

- `raw_ga4_events`
- `raw_gsc_search`
- `raw_google_ads`
- `raw_meta_ads`
- `raw_linkedin_ads`
- `raw_chatgpt_ads`
- `raw_zoho_leads`
- `raw_zoho_deals`

**Staging Layer — `stg_`**

This layer will prepare source data for further transformation.

Key activities:

- Standardize column names and data types.
- Normalize dates and timestamps.
- Handle missing and duplicate records.
- Validate source data.

**Intermediate Layer — `int_`**

This layer will prepare data for business-level analysis.

Key activities:

- Standardize currencies where required.
- Parse UTM parameters.
- Prepare marketing and CRM datasets for integration.
- Match sessions and leads where reliable identifiers exist.
- Prepare datasets for agreed attribution calculations.

**Marts Layer — `fct_` and `dim_`**

This layer will contain business-ready analytical datasets.

Potential models include:

- `dim_campaigns`
- `dim_channels`
- `dim_dates`
- `fct_ad_spend_daily`
- `fct_marketing_leads`
- `fct_marketing_conversion_journey`

The final warehouse schema will depend on actual source fields, available identifiers, and validated business definitions.

## 8. Data Pipeline and Automation

The initial implementation will focus on automating data extraction, storage, transformation, validation, and reporting.

### Proposed Automation Workflow

1. **Scheduling:** Google Cloud Scheduler will trigger pipeline execution according to a configured schedule.
2. **Data Extraction:** Python scripts will retrieve available data from marketing and CRM platforms through authorized APIs.
3. **Data Ingestion:** Extracted data will be normalized, validated, and loaded into BigQuery raw tables.
4. **Data Transformation:** dbt will execute staging, intermediate, and mart models.
5. **Data Quality Testing:** dbt tests will validate required fields, uniqueness, relationships, and data consistency.
6. **Dashboard Refresh:** Power BI datasets will be refreshed after successful data processing, subject to configured refresh and API permissions.
7. **Notifications:** Email or Slack notifications will communicate pipeline execution status and failures.

The pipeline will include API error handling, pagination, rate-limit management, logging, and incremental extraction wherever supported.

Machine learning inference is not part of the initial reporting pipeline. Predictive model execution will be considered separately as a future enhancement.

## 9. Key Business Metrics

The Power BI dashboards will focus on the following business metrics.

| Category | Key Metrics |
|---|---|
| Website Performance | Users, sessions, engagement, tracked conversions |
| SEO Performance | Organic clicks, impressions, CTR, average search position |
| Paid Advertising | Impressions, clicks, expenditure, CPC, available conversions |
| Lead Generation | Total enquiries, leads by source, qualified leads |
| Enrolment Performance | Confirmed enrolments, lead-to-enrolment rate |
| Marketing Efficiency | Cost per lead, cost per qualified lead, cost per enrolment where attributable |
| Campaign Performance | Spend, leads, qualified leads, and enrolments by campaign |
| Business Performance | Course, channel, country, and geographical comparisons |

KPI definitions and attribution rules will be validated before implementation. Advertising expenditure will only be connected to CRM outcomes where reliable attribution is available.

## 10. Expected Power BI Dashboards

The reporting solution will include the following proposed dashboards.

### 10.1 Marketing Overview Dashboard

- Website traffic and acquisition channels.
- Total marketing expenditure.
- Total enquiries and qualified leads.
- Confirmed student enrolments.
- Marketing performance trends.
- Overall channel performance.

### 10.2 SEO Performance Dashboard

- Organic search clicks and impressions.
- Search queries and landing pages.
- Click-through rate and average search position.
- Organic traffic trends.
- Available organic enquiry information.

### 10.3 Paid Advertising Performance Dashboard

- Google Ads campaign performance.
- Meta Ads campaign performance.
- LinkedIn Ads campaign performance.
- ChatGPT Ads performance, subject to available reporting data.
- Advertising expenditure, clicks, leads, and available conversion metrics.

### 10.4 Lead Funnel Analysis Dashboard

- Total leads and lead sources.
- Lead qualification stages.
- Qualified leads and enrolments.
- Lead-to-qualified and lead-to-enrolment rates.
- Funnel drop-off analysis.

### 10.5 Course and Geographical Analysis Dashboard

- Enquiries by course.
- Qualified leads and enrolments by course.
- Marketing performance across India and international markets.
- Country-level lead and enrolment trends.

## 11. Data Quality and Validation

Data quality is an important part of the proposed analytics solution.

The project will include data validation checks to improve the reliability and consistency of reporting.

Key checks will include:

- Missing and null value identification.
- Duplicate record detection.
- Data type validation.
- Date and timestamp consistency.
- Standardization of campaign and channel names.
- Validation of advertising expenditure and currency fields.
- Validation of CRM lead and enrolment records.
- Referential integrity checks for related analytical models.

dbt tests will be used to automate relevant data quality checks during the transformation process.

## 12. Future Scope: Predictive Analytics

After the initial reporting solution is implemented and sufficient historical data is collected and validated, BigQuery ML may be introduced for future machine learning initiatives.

Potential enhancements include:

- **Lead Conversion Prediction:** Estimate the likelihood of a lead becoming an enrolled student.
- **Lead Quality Scoring:** Prioritize leads based on their likelihood of progressing through the sales funnel.
- **Campaign Performance Forecasting:** Estimate future campaign performance using historical data.
- **Marketing Budget Optimization:** Support better allocation of marketing expenditure across channels.
- **Course Demand Forecasting:** Estimate future interest in different training programs.
- **Enrolment Forecasting:** Identify potential enrolment trends across courses and geographical markets.

These enhancements are part of the future scope and are not included in the initial implementation.

## 13. Expected Business Outcomes

The completed solution is expected to provide:

- A centralized view of marketing and CRM performance.
- Reduced manual reporting effort.
- Better visibility into channel and campaign effectiveness.
- Improved understanding of lead quality and enrolment conversion.
- More informed marketing budget allocation decisions.
- Consistent historical reporting across courses and geographical markets.
- A structured data foundation for future predictive analytics.

Ultimately, the solution will help the business understand which marketing channels and campaigns generate valuable leads and actual student enrolments, enabling more informed decisions about where to invest marketing resources.

## 14. Assumptions and Dependencies

The project depends on the following:

- Access to the required marketing and CRM accounts.
- API availability and appropriate permissions for automated extraction.
- CSV exports as an alternative where API access is unavailable.
- Consistent source data and agreed business definitions.
- Reliable tracking identifiers and UTM parameters for marketing-to-CRM matching.
- Validated lead qualification and enrolment definitions.
- Appropriate Google Cloud and Power BI permissions for pipeline execution and reporting.

The availability and quality of source data may affect the level of integration and attribution possible.

## 15. Project Scope and Status

**Project Type:** End-to-End Marketing Analytics, Data Engineering, Reporting Automation, and Business Intelligence.

**Initial Implementation Scope:**

- Marketing and CRM data integration.
- Python-based data extraction.
- Google BigQuery data warehousing.
- SQL and dbt transformations.
- Data quality validation.
- Power BI dashboard development.
- Pipeline scheduling and reporting automation.

**Future Scope:**

- Predictive analytics.
- Machine learning.
- Lead conversion prediction and scoring.
- Campaign performance forecasting.
- Marketing budget optimization.
- Course demand and enrolment forecasting.

**Project Status:** In Progress

The project will be developed incrementally, with each component implemented, tested, and documented before being marked as completed.
