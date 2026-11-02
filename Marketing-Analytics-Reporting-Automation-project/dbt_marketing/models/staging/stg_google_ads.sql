with source as (
    select * from {{ source('raw', 'google_ads_performance_raw') }}
),

renamed as (
    select
        cast(date as date) as ad_date,
        'google_ads' as platform,
        cast(campaign_id as string) as campaign_id,
        trim(campaign_name) as campaign_name,
        lower(trim(advertising_channel_type)) as campaign_channel_type,
        cast(cost as float64) as spend,
        cast(impressions as int64) as impressions,
        cast(clicks as int64) as clicks,
        cast(conversions as int64) as conversions,
        coalesce(cast(conversions_value as float64), 0.0) as conversion_value,
        cast(extracted_at as timestamp) as extracted_at
    from source
)

select * from renamed