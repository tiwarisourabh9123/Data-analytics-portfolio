
    
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    



select interaction_id
from `marketing-analytics-9123`.`raw`.`chatgpt_interactions_raw`
where interaction_id is null



  
  
      
    ) dbt_internal_test