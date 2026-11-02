
    
    

with dbt_test__target as (

  select interaction_id as unique_field
  from `marketing-analytics-9123`.`raw`.`chatgpt_interactions_raw`
  where interaction_id is not null

)

select
    unique_field,
    count(*) as n_records

from dbt_test__target
group by unique_field
having count(*) > 1


