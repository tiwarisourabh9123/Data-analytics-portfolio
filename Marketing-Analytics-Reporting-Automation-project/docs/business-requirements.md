
# Business Requirements Document (BRD)
## Marketing Analytics & Reporting Automation

## 1. Document Overview

| Item | Description |
|---|---|
| Project Name | Marketing Analytics & Reporting Automation |
| Industry | EdTech / Education and Training |
| Project Type | Data Analytics, Data Engineering, and Business Intelligence |
| Primary Objective | Centralize marketing and CRM data and automate performance reporting |
| Data Warehouse | Google BigQuery |
| Reporting Tool | Power BI |
| Project Status | In Progress |

## 2. Business Background

The company provides online and offline training programs to students and professionals across India and international markets.

To generate enquiries and acquire students, the company invests in multiple digital marketing channels, including search engine optimization, paid search advertising, social media advertising, and professional networking platforms.

Marketing data is generated across multiple advertising and analytics platforms, while prospective student information, lead progress, and enrolment details are managed through Zoho CRM.

The business requires a centralized analytics solution to combine these datasets, monitor marketing performance, understand lead quality, and evaluate how marketing investments contribute to student enrolments.

## 3. Business Objectives

The solution should help the business:

1. Consolidate marketing and CRM data into a centralized data warehouse.
2. Automate data collection and reporting to reduce manual effort.
3. Monitor performance across organic search, paid search, and social advertising channels.
4. Identify campaigns that generate qualified leads and actual enrolments.
5. Measure marketing expenditure against lead generation and enrolment outcomes.
6. Compare marketing performance across courses, countries, and channels.
7. Identify opportunities to improve campaign performance and budget allocation.
8. Maintain historical data for trend analysis and future predictive modelling.

## 4. Stakeholders and Users

| Stakeholder | Requirements |
|---|---|
| Business Management | Overall marketing performance, expenditure, enrolment trends, and business growth insights |
| Marketing Manager | Channel performance, campaign results, lead generation, and budget efficiency |
| SEO Team | Organic traffic, search visibility, queries, and landing-page performance |
| Paid Advertising Team | Campaign expenditure, clicks, conversions, CPL, and campaign comparisons |
| Sales / Admissions Team | Lead quality, lead stages, follow-ups, and enrolment conversion |
| Data / Analytics Team | Data extraction, transformation, validation, reporting, and pipeline monitoring |

## 5. Business Requirements

### BR-01: Centralized Data Integration

The system must collect data from the following platforms:

- Google Analytics 4 (GA4)
- Google Search Console (GSC)
- Google Ads
- Meta Ads Manager
- LinkedIn Ads
- ChatGPT Ads Manager
- Zoho CRM

The collected data should be organized and stored in Google BigQuery.

### BR-02: Automated Data Extraction

The system should automate data collection using Python and authorized APIs wherever available.

The extraction process should support:

- Secure API authentication.
- Pagination and rate-limit handling.
- Configurable reporting periods.
- Incremental data extraction where supported.
- Error handling and logging.
- Data validation before loading.

CSV-based ingestion may be used for platforms where suitable API access is unavailable.

### BR-03: Data Warehouse Management

The system must maintain a structured BigQuery data warehouse.

The warehouse should:

- Preserve source-level data in raw tables.
- Maintain consistent naming conventions.
- Support historical data storage.
- Support incremental updates and reprocessing.
- Organize datasets for efficient querying and analysis.

### BR-04: Data Cleaning and Transformation

The system must transform raw data into reliable analytical datasets using dbt and SQL.

Required transformations include:

- Data type standardization.
- Date and timestamp normalization.
- Missing-value handling.
- Duplicate identification and removal where appropriate.
- Campaign and channel name standardization.
- Currency normalization where required.
- UTM parameter parsing.
- Validation of business metrics.
- Integration of marketing and CRM datasets where reliable identifiers exist.

### BR-05: Marketing Performance Analysis

The system should provide consolidated performance reporting across marketing channels.

Users should be able to analyze:

- Website traffic and engagement.
- Organic search performance.
- Paid advertising expenditure.
- Campaign impressions and clicks.
- Enquiries and available conversion metrics.
- Cost per lead and cost per qualified lead.
- Marketing performance over time.

### BR-06: Lead and Enrolment Analysis

The system should integrate available Zoho CRM information to analyze the lead lifecycle.

Users should be able to understand:

- Total enquiries.
- Lead sources.
- Lead qualification status.
- Lead-stage progression.
- Course interest.
- Confirmed student enrolments.
- Lead-to-qualified and lead-to-enrolment conversion rates.
- Lead drop-off patterns.

Marketing-to-CRM matching must use reliable identifiers and agreed business rules. Unmatched records should not be assigned to campaigns through assumptions.

### BR-07: Campaign and Channel Performance

The system should help identify which marketing campaigns and channels contribute to business outcomes.

Users should be able to compare:

- Advertising expenditure.
- Impressions and clicks.
- Cost per click.
- Enquiries generated.
- Qualified leads generated.
- Confirmed enrolments.
- Cost per lead.
- Cost per qualified lead.
- Cost per enrolment, where reliable attribution is available.

### BR-08: Course and Geographical Analysis

The reporting solution should support analysis across training programs and geographical markets.

Users should be able to identify:

- Courses generating the highest enquiry volumes.
- Courses generating more qualified leads.
- Courses achieving higher enrolment rates.
- Marketing performance across India and international markets.
- Countries generating stronger lead and enrolment outcomes.

### BR-09: Interactive Business Intelligence Reporting

The system must provide Power BI dashboards with appropriate filters and drill-down capabilities.

Users should be able to filter reports by:

- Date and reporting period.
- Marketing channel.
- Campaign.
- Country or geographical region.
- Course or training program.
- Lead source.
- Lead stage.

### BR-10: Pipeline Monitoring and Automation

The solution should support scheduled pipeline execution and monitoring.

It should:

- Run extraction jobs on a configured schedule.
- Trigger dbt transformations.
- Execute data quality tests.
- Refresh Power BI datasets.
- Record execution status and errors.
- Send notifications when important pipeline tasks fail.

## 6. Functional Requirements

| ID | Functional Requirement | Priority |
|---|---|---|
| FR-01 | Extract data from authorized marketing and CRM APIs | High |
| FR-02 | Handle API authentication, pagination, and rate limits | High |
| FR-03 | Load source data into BigQuery raw tables | High |
| FR-04 | Implement dbt staging and transformation models | High |
| FR-05 | Perform data quality checks and validation | High |
| FR-06 | Integrate marketing data with CRM leads where possible | High |
| FR-07 | Calculate agreed marketing and conversion KPIs | High |
| FR-08 | Develop Power BI marketing dashboards | High |
| FR-09 | Schedule and monitor pipeline execution | Medium |
| FR-10 | Implement predictive analytics using historical data | Future |

## 7. Non-Functional Requirements

| Area | Requirement |
|---|---|
| Security | Protect API credentials, access tokens, and confidential business data |
| Reliability | Include error handling, logging, and failure notifications |
| Data Quality | Maintain consistent, validated, and traceable datasets |
| Scalability | Support additional platforms, campaigns, and historical data |
| Performance | Design efficient BigQuery tables and queries |
| Maintainability | Use modular Python scripts and reusable dbt models |
| Documentation | Maintain technical documentation, KPI definitions, and data dictionaries |
| Privacy | Use approved access controls and anonymized data in public demonstrations |

## 8. Key Business KPIs

| KPI | Business Definition |
|---|---|
| Total Website Users | Number of users visiting the website |
| Total Sessions | Number of website sessions |
| Organic Clicks | Clicks received through organic search |
| Organic Impressions | Search result impressions |
| Organic CTR | Organic clicks divided by organic impressions |
| Ad Spend | Total advertising expenditure |
| Ad Impressions | Number of advertising impressions |
| Ad Clicks | Number of advertising clicks |
| CPC | Advertising expenditure divided by clicks |
| Total Leads | Enquiries recorded in the defined reporting scope |
| Qualified Leads | Leads meeting the agreed qualification criteria |
| Enrolments | Confirmed student enrolments recorded in CRM |
| Lead-to-Qualified Rate | Qualified leads divided by eligible leads |
| Lead-to-Enrolment Rate | Enrolments divided by the relevant eligible lead cohort |
| Cost Per Lead | Attributable advertising expenditure divided by attributable leads |
| Cost Per Qualified Lead | Attributable advertising expenditure divided by attributable qualified leads |
| Cost Per Enrolment | Attributable advertising expenditure divided by attributable enrolments |

KPI definitions, attribution windows, currency conversions, and reporting periods must be agreed before final implementation.

## 9. Reporting Requirements

The Power BI solution should contain the following reports:

| Dashboard | Reporting Requirements |
|---|---|
| Marketing Overview | Website traffic, advertising spend, leads, qualified leads, and enrolments |
| SEO Performance | Organic clicks, impressions, CTR, search queries, and landing pages |
| Paid Advertising | Google, Meta, LinkedIn, and ChatGPT campaign performance |
| Lead Funnel | Lead sources, qualification stages, conversions, and enrolments |
| Course Performance | Enquiries, qualified leads, and enrolments by course |
| Geographical Performance | Marketing and enrolment performance by country or region |

## 10. Future Business Requirements

After the initial reporting solution is implemented and sufficient historical data is available, the business may introduce:

- Lead conversion prediction.
- Automated lead quality scoring.
- Campaign performance forecasting.
- Marketing budget optimization.
- Course demand forecasting.
- Enrolment trend prediction.
- AI-assisted marketing performance summaries.

These requirements are outside the initial implementation scope.

## 11. Assumptions and Dependencies

- The company will provide authorized access to the required marketing and CRM accounts.
- API access and reporting permissions will be available for the selected platforms, subject to their respective limitations.
- Required historical data will be available where supported by each platform.
- Zoho CRM will contain sufficiently structured lead and enrolment information.
- Marketing campaign tracking and UTM conventions will be reviewed for consistency.
- Currency conversion rules and reporting currency will be agreed.
- Business stakeholders will validate lead stages, enrolment definitions, and KPI calculations.
- ChatGPT advertising data availability will depend on the applicable Ads Manager reporting and API access.

## 12. Acceptance Criteria

The initial solution will be considered ready for business review when:

1. Required source data can be extracted or ingested through approved methods.
2. Source datasets are stored in the appropriate BigQuery raw tables.
3. dbt transformations produce the agreed analytical datasets.
4. Data quality tests run and their results are documented.
5. Marketing and CRM data are connected where reliable matching is possible.
6. Agreed KPIs are calculated and validated.
7. Power BI dashboards display the required reporting metrics and filters.
8. Scheduled pipeline execution and failure monitoring are tested.
9. Technical and business documentation is available.

## 13. Project Scope and Status

**Initial Scope:**
- Marketing and CRM data integration.
- Python-based data extraction and ingestion.
- BigQuery data warehouse development.
- dbt transformations and data quality testing.
- Marketing and lead funnel analysis.
- Power BI dashboard development.
- Reporting automation and monitoring.

**Future Scope:**
- Machine learning and predictive analytics.
- Lead scoring and conversion prediction.
- Campaign forecasting.
- Marketing budget optimization.

**Project Status:** In Progress

**Primary Business Goal:** Build a reliable, automated marketing analytics solution that helps the business understand which channels and campaigns generate qualified leads and actual student enrolments, enabling better marketing investment decisions.
