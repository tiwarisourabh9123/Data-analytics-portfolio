
    
    

with dbt_test__target as (

  select lead_id as unique_field
  from `marketing-analytics-9123`.`raw`.`zoho_crm_leads_raw`
  where lead_id is not null

)

select
    unique_field,
    count(*) as n_records

from dbt_test__target
group by unique_field
having count(*) > 1


