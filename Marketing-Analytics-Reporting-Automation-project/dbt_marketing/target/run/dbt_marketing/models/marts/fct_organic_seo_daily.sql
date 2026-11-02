
  
    

    create or replace table `marketing-analytics-9123`.`marts`.`fct_organic_seo_daily`
      
    
    

    
    OPTIONS()
    as (
      with gsc_performance as (
    select
        search_date as report_date, landing_page, search_query, country,
        sum(organic_clicks) as total_clicks, sum(organic_impressions) as total_impressions, avg(average_position) as avg_position
    from `marketing-analytics-9123`.`staging`.`stg_gsc_search`
    group by 1, 2, 3, 4
),
ga4_traffic as (
    select
        traffic_date as report_date,
        sum(sessions) as total_sessions, sum(engaged_sessions) as total_engaged_sessions,
        sum(total_users) as total_users, sum(screen_page_views) as total_page_views, avg(engagement_rate) as avg_engagement_rate
    from `marketing-analytics-9123`.`staging`.`stg_ga4_traffic`
    group by 1
)
select
    coalesce(g.report_date, t.report_date) as report_date,
    g.landing_page, g.search_query, g.country,
    coalesce(g.total_clicks, 0) as organic_clicks,
    coalesce(g.total_impressions, 0) as organic_impressions,
    round(g.avg_position, 2) as avg_search_position,
    coalesce(t.total_sessions, 0) as ga4_sessions,
    coalesce(t.total_engaged_sessions, 0) as ga4_engaged_sessions,
    coalesce(t.total_users, 0) as ga4_total_users,
    round(coalesce(t.avg_engagement_rate, 0.0), 4) as avg_engagement_rate
from gsc_performance g
full outer join ga4_traffic t on g.report_date = t.report_date
    );
  