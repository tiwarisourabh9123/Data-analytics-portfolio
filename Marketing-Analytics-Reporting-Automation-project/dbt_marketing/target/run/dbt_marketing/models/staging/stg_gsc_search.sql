

  create or replace view `marketing-analytics-9123`.`staging`.`stg_gsc_search`
  OPTIONS()
  as with source as (
    select * from `marketing-analytics-9123`.`raw`.`gsc_search_performance_raw`
),

renamed as (
    select
        cast(date as date) as search_date,
        lower(trim(query)) as search_query,
        trim(page) as landing_page,
        upper(trim(country)) as country,
        cast(clicks as int64) as organic_clicks,
        coalesce(cast(impressions as int64), 0) as organic_impressions,
        cast(ctr as float64) as ctr,
        round(cast(position as float64), 2) as average_position,
        cast(extracted_at as timestamp) as extracted_at
    from source
)

select * from renamed;

