with source as (
    select * from {{ source('raw', 'ga4_traffic_raw') }}
),

renamed as (
    select
        cast(date as date) as traffic_date,
        cast(total_users as int64) as total_users,
        cast(sessions as int64) as sessions,
        cast(engaged_sessions as int64) as engaged_sessions,
        cast(screen_page_views as int64) as screen_page_views,
        cast(engagement_rate as float64) as engagement_rate,
        cast(extracted_at as timestamp) as extracted_at
    from source
)

select * from renamed