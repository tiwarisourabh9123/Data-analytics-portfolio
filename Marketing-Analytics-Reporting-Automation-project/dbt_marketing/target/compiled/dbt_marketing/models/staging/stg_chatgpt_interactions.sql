with source as (
    select * from `marketing-analytics-9123`.`raw`.`chatgpt_interactions_raw`
),

cleaned as (
    select
        cast(interaction_id as string) as interaction_id,
        cast(interaction_date as date) as interaction_date,
        trim(session_channel) as session_channel,
        lower(trim(inquired_course)) as inquired_course,
        lower(trim(primary_intent)) as primary_intent,
        cast(sentiment_score as float64) as sentiment_score,
        cast(total_messages as int64) as total_messages,
        cast(lead_captured as boolean) as is_lead_captured,
        cast(crm_synced as boolean) as is_crm_synced
    from source
)

select * from cleaned