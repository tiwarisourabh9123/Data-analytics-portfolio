with source as (
    select * from {{ source('raw', 'zoho_crm_leads_raw') }}
),

cleaned as (
    select
        cast(lead_id as string) as lead_id,
        cast(created_date as date) as lead_date,
        cast(extracted_at as timestamp) as extracted_at,
        
        -- Align channel naming directly with ad platforms
        case 
            when lower(trim(lead_source)) like '%google%' then 'google_ads'
            when lower(trim(lead_source)) like '%meta%' or lower(trim(lead_source)) like '%facebook%' then 'meta_ads'
            when lower(trim(lead_source)) like '%chatgpt%' or lower(trim(lead_source)) like '%ai%' then 'chatgpt_assistant'
            when lower(trim(lead_source)) like '%organic%' or lower(trim(lead_source)) like '%seo%' then 'organic_search'
            when lower(trim(lead_source)) like '%direct%' then 'direct_website'
            else lower(replace(trim(lead_source), ' ', '_'))
        end as lead_source_clean,
        
        lower(trim(interested_course)) as interested_course,
        lower(trim(stage)) as lead_stage,
        coalesce(cast(deal_value_inr as float64), 0.0) as deal_value_inr,
        
        case 
            when lower(trim(stage)) like '%closed won%' then 1 
            else 0 
        end as is_enrolled

    from source
)

select * from cleaned