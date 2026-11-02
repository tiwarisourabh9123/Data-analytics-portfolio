with meta_ads as (
    select
        ad_date, platform, campaign_id, campaign_name,
        spend, impressions, clicks, conversions, conversion_value
    from {{ ref('stg_meta_ads') }}
),
google_ads as (
    select
        ad_date, platform, campaign_id, campaign_name,
        spend, impressions, clicks, conversions, conversion_value
    from {{ ref('stg_google_ads') }}
),
combined as (
    select * from meta_ads
    union all
    select * from google_ads
)
select
    ad_date, platform, campaign_id, campaign_name,
    spend, impressions, clicks, conversions, conversion_value,
    case when impressions > 0 then round((clicks / impressions) * 100, 2) else 0.0 end as click_through_rate,
    case when clicks > 0 then round(spend / clicks, 2) else 0.0 end as cost_per_click,
    case when spend > 0 then round(conversion_value / spend, 2) else 0.0 end as roas
from combined
