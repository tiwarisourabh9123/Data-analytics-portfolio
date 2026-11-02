with ad_spend_summary as (
    select
        ad_date as event_date, platform as channel,
        sum(spend) as total_spend, sum(clicks) as total_clicks, sum(impressions) as total_impressions
    from {{ ref('fct_paid_ad_performance_daily') }}
    group by 1, 2
),
crm_leads_summary as (
    select
        lead_date as event_date, lead_source_clean as channel,
        count(lead_id) as total_leads, sum(is_enrolled) as total_enrollments, sum(deal_value_inr) as total_revenue_inr
    from {{ ref('stg_zoho_crm_leads') }}
    group by 1, 2
)
select
    coalesce(a.event_date, c.event_date) as report_date,
    coalesce(a.channel, c.channel) as channel,
    coalesce(a.total_spend, 0.0) as total_spend,
    coalesce(a.total_clicks, 0) as total_clicks,
    coalesce(a.total_impressions, 0) as total_impressions,
    coalesce(c.total_leads, 0) as total_leads,
    coalesce(c.total_enrollments, 0) as total_enrollments,
    coalesce(c.total_revenue_inr, 0.0) as total_revenue_inr,
    case 
        when coalesce(a.total_spend, 0.0) > 0 and coalesce(c.total_revenue_inr, 0.0) > 0 
            then round(c.total_revenue_inr / a.total_spend, 2)
        else 0.0 
    end as channel_roi,
    case 
        when coalesce(c.total_leads, 0) > 0 and coalesce(a.total_spend, 0.0) > 0 
            then round(a.total_spend / c.total_leads, 2)
        else 0.0 
    end as cost_per_lead
from ad_spend_summary a
full outer join crm_leads_summary c
    on a.event_date = c.event_date and a.channel = c.channel
